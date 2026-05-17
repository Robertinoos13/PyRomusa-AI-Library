# Reply Engine Code (chaos)
def use_engine(bot_instance, prompt: str, 
            sensitivity: int = 1, 
            with_memory: bool = True, 
            fallback_language="english", 
            fallback_empty_string_message="", 
            fallback_no_understanded_message="", 
            fallback_not_sure_message="", 
            temperature: float = 0.0,
            show_thinking=False,
            allow_long_text_thinking=True,
            show_debug=False):

    if with_memory == True:
                # Similar cu ramura fără memorie, dar influențată ușor de ultima conversație
                words = str(prompt).split()
                bot_instance._thinking(f"I read the prompt words: {words}", show_thinking, allow_long_text_thinking)
                bot_instance._debug("prompt words", str(words), show_debug)
                bot_instance._thinking("With memory on: I will also incorporate the last turn into the suggestion process.", show_thinking, allow_long_text_thinking)
                if not words:
                    bot_instance._stop_thinking(show_thinking)
                    return ""

                known_word_ids = [bot_instance.total_vocabulary.get(w) for w in words if w in bot_instance.total_vocabulary]
                bot_instance._thinking(f"I map known words to IDs: {known_word_ids}", show_thinking, allow_long_text_thinking)
                bot_instance._debug("known ids", str(known_word_ids), show_debug)
                if words:
                    bot_instance._debug("understanding rate", f"{(len(known_word_ids)/len(words))*100:.2f}%", show_debug)
                else:
                    bot_instance._debug("understanding rate", "0.00%", show_debug)

                # Colectăm sugestii din mapping-ul id -> output_ids (performant: nu parcurgem toate exemplele)
                suggestions = []
                mapping = getattr(bot_instance, 'input_word_id_to_output_ids', {})
                for wid in known_word_ids:
                    if wid is None:
                        continue
                    suggestions.extend(mapping.get(wid, []))

                # Încorporăm memoria ultimei conversații, dar cu greutate mai mică (nu afectăm mult performanța)
                last_user = getattr(bot_instance, 'last_user_prompt', '') or ''
                last_bot = getattr(bot_instance, 'last_bot_output', '') or ''
                last_user_ids = [bot_instance.total_vocabulary.get(w) for w in str(last_user).split() if w in bot_instance.total_vocabulary]
                last_bot_ids = [bot_instance.total_vocabulary.get(w) for w in str(last_bot).split() if w in bot_instance.total_vocabulary]

                # Dăm o mică greutate sugestiilor venite din ultima conversație
                for wid in last_user_ids:
                    if wid is None:
                        continue
                    suggestions.extend(mapping.get(wid, []) * 2)

                for wid in last_bot_ids:
                    if wid is None:
                        continue
                    suggestions.extend(mapping.get(wid, []))

                id_to_word = getattr(bot_instance, 'id_to_word', {v: k for k, v in bot_instance.total_vocabulary.items()})
                if not suggestions:
                    bot_instance._debug("suggestions", "none", show_debug)
                    if show_debug == True:
                        print("[STOP DEBUG] \n\n")
                        print("---\n")
                    bot_instance._stop_thinking(show_thinking)
                    if getattr(bot_instance, 'tokens', None):
                        resp = " ".join([id_to_word.get(t, "") for t in bot_instance.tokens[:1]]).strip()
                        try:
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = resp
                        except Exception:
                            pass
                        return resp
                    return ""

                from collections import Counter
                cnt = Counter(suggestions)
                prompt_list_type = list(prompt)
                words_total_number = 1
                for ch in prompt_list_type:
                    if ch == " ":
                        words_total_number += 1

                # Default behaviour: use most common ids
                if temperature and float(temperature) > 0.0 and suggestions:
                    import random

                    # probabilistic sampling from repeated suggestions list biases by frequency
                    pool = suggestions
                    sample_k = min(len(pool), 9 * words_total_number)
                    try:
                        sampled = random.sample(pool, k=sample_k)
                    except Exception:
                        sampled = pool[:sample_k]
                    # preserve order and unique
                    seen = set()
                    most_common_ids = []
                    for i in sampled:
                        if i not in seen:
                            seen.add(i)
                            most_common_ids.append(i)
                else:
                    most_common_ids = [item for item, _ in cnt.most_common(9 * words_total_number)]

                response_words = [id_to_word.get(i, str(i)) for i in most_common_ids if i in id_to_word]

                response = " ".join(response_words).strip()
                bot_instance._debug("response text", response, show_debug)
                bot_instance._debug("most common ids", str(most_common_ids), show_debug)
                if show_debug == True:
                    print("[STOP DEBUG] \n\n")
                    print("---\n")
                bot_instance._stop_thinking(show_thinking)
                try:
                    bot_instance.last_user_prompt = str(prompt)
                    bot_instance.last_bot_output = response
                except Exception:
                    pass

                return response

    elif with_memory == False:
                # Ignorăm complet ultima conversație: salvăm și curățăm temporar atributele
                orig_last_user = getattr(bot_instance, 'last_user_prompt', None)
                orig_last_bot = getattr(bot_instance, 'last_bot_output', None)
                try:
                    try:
                        bot_instance.last_user_prompt = ""
                        bot_instance.last_bot_output = ""
                    except Exception:
                        pass

                    # Transformăm prompt-ul în cuvinte și obținem id-urile cunoscute
                    words = str(prompt).split()
                    bot_instance._thinking(f"I read the prompt words: {words}", show_thinking, allow_long_text_thinking)
                    bot_instance._debug("prompt words", str(words), show_debug)
                    bot_instance._thinking("No memory mode: I ignore previous turns and score based only on this prompt.", show_thinking, allow_long_text_thinking)
                    if not words:
                        bot_instance._stop_thinking(show_thinking)
                        return ""

                    known_word_ids = [bot_instance.total_vocabulary.get(w) for w in words if w in bot_instance.total_vocabulary]
                    bot_instance._thinking(f"I map known words to IDs: {known_word_ids}", show_thinking, allow_long_text_thinking)
                    bot_instance._debug("known ids", str(known_word_ids), show_debug)
                    if words:
                        bot_instance._debug("understanding rate", f"{(len(known_word_ids)/len(words))*100:.2f}%", show_debug)
                    else:
                        bot_instance._debug("understanding rate", "0.00%", show_debug)

                    # Numărăm, aproximativ, numărul de cuvinte (pentru a decide lungimea răspunsului)
                    prompt_list_type = list(prompt)
                    words_total_number = 1
                    for word in prompt_list_type:
                        if word == " ":
                            words_total_number += 1

                    # În primul rând, verificăm dacă există un exemplu de training cu input-ul
                    # EXACT egal cu prompt-ul (comparare case-insensitive). Dacă da și exemplul
                    # nu este condiționat de ultima conversație, returnăm output-ul original.
                    for sample in getattr(bot_instance, 'training_dataset', []):
                        if isinstance(sample, dict):
                            sample_inp = str(sample.get('input', '')).strip().lower()
                            sample_out = str(sample.get('output', '')).strip()
                            if_last_in = sample.get('if_last_input')
                            if_last_out = sample.get('if_last_output')
                        elif isinstance(sample, (list, tuple)):
                            sample_inp = str(sample[0]).strip().lower() if len(sample) > 0 else ''
                            sample_out = str(sample[1]).strip() if len(sample) > 1 else ''
                            if_last_in = sample[2] if len(sample) > 2 else None
                            if_last_out = sample[3] if len(sample) > 3 else None
                        else:
                            sample_inp = str(sample).strip().lower()
                            sample_out = ''
                            if_last_in = None
                            if_last_out = None

                        if sample_inp and sample_inp == str(prompt).strip().lower():
                            # dacă exemplul are condiții pe ultima conversație, în ramura no-memory
                            # returnăm un fallback (nu dezvăluim că știm ultima conversație)
                            if if_last_in or if_last_out:
                                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                                    bot_instance._stop_thinking(show_thinking)
                                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
                                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                                    bot_instance._stop_thinking(show_thinking)
                                    return "I'm not sure if I understand, but it sounds interesting!"
                                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                                    bot_instance._stop_thinking(show_thinking)
                                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                                else:
                                    if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_not_sure_message:
                                        bot_instance._stop_thinking(show_thinking)
                                        return fallback_not_sure_message
                                    bot_instance._stop_thinking(show_thinking)
                                    return ""
                            else:
                                try:
                                    bot_instance._stop_thinking(show_thinking)
                                    return sample_out
                                except Exception:
                                    bot_instance._stop_thinking(show_thinking)
                                    return sample_out

                    # Colectăm sugestii de id-uri din exemplele de antrenament, dar IGNORĂM
                    # exemplele condiționate de ultima conversație (if_last_*) pentru a nu folosi memorie
                    suggestions = []
                    examples = getattr(bot_instance, 'translated_input_and_output_examples', [])
                    for wid in known_word_ids:
                        if wid is None:
                            continue
                        for ex in examples:
                            # dacă exemplul are condiții pe ultima conversație, sărim în ramura no-memory
                            if ex.get('if_last_input_words') or ex.get('if_last_output_words'):
                                continue
                            if wid in ex.get('input_ids', []):
                                suggestions.extend(ex.get('output_ids', []))

                    # Dacă nu avem sugestii, revenim cu o propoziție fallback (primele tokens cunoscute)
                    id_to_word = getattr(bot_instance, 'id_to_word', {v: k for k, v in bot_instance.total_vocabulary.items()})
                    if not suggestions:
                        if show_debug == True:
                            print("[STOP DEBUG] \n\n")
                            print("---\n")
                        bot_instance._stop_thinking(show_thinking)
                        if getattr(bot_instance, 'tokens', None):
                            return " ".join([id_to_word.get(t, "") for t in bot_instance.tokens[:1]]).strip()
                        return ""

                    # Rangăm id-urile după frecvență și reconstruim cuvintele cele mai probabile
                        from collections import Counter
                        cnt = Counter(suggestions)
                        if temperature and float(temperature) > 0.0 and suggestions:
                            pool = suggestions
                            sample_k = min(len(pool), 9 * words_total_number)
                            try:
                                sampled = random.sample(pool, k=sample_k)
                            except Exception:
                                sampled = pool[:sample_k]
                            seen = set()
                            most_common_ids = []
                            for i in sampled:
                                if i not in seen:
                                    seen.add(i)
                                    most_common_ids.append(i)
                        else:
                            most_common_ids = [item for item, _ in cnt.most_common(9 * words_total_number)]

                        response_words = [id_to_word.get(i, str(i)) for i in most_common_ids if i in id_to_word]

                        # Returnăm răspunsul construit simplu, prin concatenarea cu spațiu
                        response = " ".join(response_words)
                        bot_instance._debug("response text", response)
                        bot_instance._debug("most common ids", str(most_common_ids))
                        bot_instance._stop_thinking(show_thinking)
                        return response
                finally:
                    # Restaurăm contextul original
                    try:
                        bot_instance.last_user_prompt = orig_last_user
                        bot_instance.last_bot_output = orig_last_bot
                    except Exception:
                        pass