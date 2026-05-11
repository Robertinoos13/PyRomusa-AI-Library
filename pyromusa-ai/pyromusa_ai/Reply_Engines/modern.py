# Reply Engine Code (modern)
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
    
            if show_thinking == True:
                print(f"I was given the prompt '{prompt}' and I need to generate an answer based on it.\n")

            try:
                import numpy as np
                import unicodedata
            except Exception:

                # Fallback pentru situația în care NumPy nu este instalat
                # Folosim o logică simplificată bazată pe seturi (intersecție de cuvinte)
                try:
                    words = str(prompt).lower().split()

                    if show_thinking == True:
                        print(f"The first step to process it, I would need to take the user's prompt and turn it into a list, with each word in the prompt being a value of the list in an individual way. I generated the list and it gave me the list '{words}'\n")

                    if not words:
                        if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                            return "Te ascult..."
                        return fallback_empty_string_message or ""
                    
                    prompt_set = set(words)
                    dataset = getattr(bot_instance, "translated_input_and_output_examples", [])
                    
                    # Căutăm primul exemplu care are măcar un cuvânt comun
                    for ex in dataset:
                        if prompt_set & ex.get('input_words', set()):
                            out_ids = ex.get('output_ids', [])
                            # Reconstruim răspunsul din ID-uri
                            id_to_word = getattr(bot_instance, "id_to_word", {})
                            # Dacă nu avem id_to_word, încercăm să inversăm total_vocabulary
                            if not id_to_word:
                                vocab = getattr(bot_instance, "total_vocabulary", {})
                                id_to_word = {v: k for k, v in vocab.items()}
                            
                            out_str = " ".join([id_to_word.get(i, str(i)) for i in out_ids])
                            
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = out_str
                            return out_str
                    
                    # Dacă nu găsim nimic nici cu metoda simplă
                    return fallback_no_understanded_message or ""
                except Exception:
                    return ""

            def strip_diacritics(s: str) -> str:
                # "ă, î, â, ș, ț" -> normalizare
                return ''.join(ch for ch in unicodedata.normalize('NFKD', s) if not unicodedata.combining(ch)).lower()

            # 1) Tokenizare și mapare cuvinte -> id-uri
            words = [w for w in str(prompt).lower().split()]

            if show_thinking == True:
                print(f"The first step to process it, I would need to take the user's prompt and turn it into a list, with each word in the prompt being a value of the list in an individual way. I generated the list and it gave me the list '{words}'\n")

            if not words:
                if show_thinking == True:
                    print("What to see? I got an empty prompt. I have nothing to do with it. For this reason, I will generate a fallback response.\n")
                    print("[STOP THINKING]")
                    print("---")
                
                if show_debug == True:
                    print("---\n")
                    print("[STOP DEBUG] \n\n")

                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                    try:
                        bot_instance.last_user_prompt = str(prompt)
                        bot_instance.last_bot_output = "Te ascult..."
                    except Exception:
                        pass
                    return getattr(bot_instance, "last_bot_output", "Te ascult...")
                return fallback_empty_string_message or ""

            total_vocab = getattr(bot_instance, "total_vocabulary", {}) or {}

            if show_thinking == True:
                print("I need to see what my exact vocabulary is so I can turn the prompt into my natural language, i.e. 'tokenize' it. ")
                print("Aha, I found it, that's my entire vocabulary!")
                if allow_long_text_thinking == True:
                    print(total_vocab)

            if not total_vocab:
                if show_thinking == True:
                    print("From what I can see, I have an absolutely empty vocabulary and there is nothing in it. Someone should teach me something at some point, various words, giving me examples of question-answer type. Because of this, I can't answer with anything at all, thus returning a fallback message.\n")
                    print("[STOP THINKING]")
                    print("---")

                if show_debug == True:
                    print("---\n")
                    print("[STOP DEBUG] \n\n")

                return fallback_no_understanded_message or ""

            # helper: găsește id pentru un cuvânt (exact sau fără diacritice)
            def word_to_id(word: str):
                if word in total_vocab:
                    return total_vocab[word]
                stripped = strip_diacritics(word)
                for k, v in total_vocab.items():
                    if strip_diacritics(k) == stripped:
                        return v
                return None

            if show_thinking == True:
                print("\nOk, now that I still have a few words in my vocabulary, theoretically I could respond to the user's prompt, because that's what I was asked to do.")
                print("Starting the tokenization process...")

            prompt_ids_full = [word_to_id(w) for w in words]
            
            if show_thinking == True:
                print(f"STEP 1 (full user prompt translation): {prompt_ids_full}")

            prompt_ids = [i for i in prompt_ids_full if i is not None]

            if show_thinking == True:
                print(f"STEP 2 (cleaning the user prompt of useless elements): {prompt_ids}\n")
                print(f"From the user prompt, I know {len(prompt_ids)} of {len(prompt_ids_full)} words\n")

            # Încorporăm memoria (ultimul prompt) ca semnal slab
            if with_memory == True and getattr(bot_instance, "last_user_prompt", None):
                if show_thinking == True:
                    print(f"But hey, I was also asked to access and consider my last conversation with the user, but what was that? Let me check...")
                    print(f"This is what I remember as the last conversation:\n     my last message: '{bot_instance.last_bot_output}'\n     user's last message: '{bot_instance.last_user_prompt}'\n")
                    print("Let's start tokenizing the user's last prompt...")

                last_words = [w for w in str(bot_instance.last_user_prompt).lower().split()]
                
                if show_thinking == True:
                    print(f"STEP 1 (turning the last prompt into a list of strings): {last_words}")

                last_ids_full = [word_to_id(w) for w in last_words]

                if show_thinking == True:
                    print(f"STEP 2 (tokenizing the list of strings to better understand it): {last_ids_full}")

                last_ids = [i for i in last_ids_full if i is not None]

                if show_thinking == True:
                    print(f"STEP 3 (removing all unnecessary values ​​that I don't understand): {last_ids} \n")
                    print(f"From the user last prompt, I know {len(last_ids)} of {len(last_ids_full)} words\n")
            else:
                last_ids = []

            # Dacă nu recunoaștem niciun cuvânt, returnăm fallback specific limbii
            if not prompt_ids and not last_ids:
                if show_thinking == True:
                    print("Um? How strange. I don't understand anything the user said. Because of this, I will return an automated fallback message as a final response.")
                    print("\n\n[STOP THINKING]\n")
                    print("---\n")

                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                    return "I'm not sure if I understand, but it sounds interesting!"
                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                
                bot_instance.last_user_prompt = str(prompt)
                bot_instance.last_bot_output = fallback_no_understanded_message or ""
                return bot_instance.last_bot_output

            # 2) Construim vectorul prompt (histogramă pe id-uri)
            all_ids = list(total_vocab.values())
            max_id = max(all_ids) if all_ids else 0
            
            prompt_hist = np.bincount(prompt_ids, minlength=max_id + 1).astype(float)

            if show_thinking and allow_long_text_thinking:
                print("Now, I would like to find the location and count of all the words in the prompt in my word vocabulary, noting them with a minimum of 1 or higher if there is at least 1 in the user's prompt or more:")
                print(f'{prompt_hist} \n')

            elif show_thinking and not allow_long_text_thinking:
                print("It's a bit long to display it in the console, so let's skip it.")

            if last_ids:
                last_hist = np.bincount(last_ids, minlength=max_id + 1).astype(float)
                prompt_hist += 0.4 * last_hist
                if show_thinking and allow_long_text_thinking:
                    print("But hey, I forgot to take into account the last words the user said in the previous prompt. Let's complete our information")
                    print(f'{prompt_hist} \n')

            # 3) Construim matricea exemplelor (cu pre-filtrare contextuală strictă)
            dataset_list = getattr(bot_instance, "translated_input_and_output_examples", [])

            if show_thinking:
                print("Now, I should access my training dataset, get some inspiration from them to see how I should respond.")
                
                if allow_long_text_thinking:
                    print(dataset_list)
                
                else:
                    print("It's a bit long to display it in the console, so let's skip it.")

            examples = []
            outputs = []
            examples_meta = []

            if show_thinking:
                print("\nLet's see exactly what else I could extract from the last conversation, something useful.")

            # Pregătim variabilele de context dacă with_memory este activ
            last_user_words_list = [w for w in str(getattr(bot_instance, 'last_user_prompt', '')).lower().split()] if with_memory else []
            last_bot_words_list = [w for w in str(getattr(bot_instance, 'last_bot_output', '')).lower().split()] if with_memory else []
            last_user_words = set(last_user_words_list)
            last_bot_words = set(last_bot_words_list)
            last_user_count = len(last_user_words_list)
            last_bot_count = len(last_bot_words_list)

            if show_thinking:
                if not last_bot_words and not last_user_words:
                    print("Nothing lol\n")
                else:
                    print("Aha! These are:")
                    print(last_user_words)
                    print(last_bot_words)

            try:
                sens = float(sensitivity)
            except Exception:
                sens = 1.0

            if show_thinking:
                print("Now I need to see which examples in my dataset depend on the last conversation with the user...")
                
            prompt_words = set(words)
            for ex in dataset_list:
                # Verificăm dacă exemplul este condiționat de o conversație anterioară
                has_condition = bool(ex.get('if_last_input_words')) or bool(ex.get('if_last_output_words'))

                if show_thinking and allow_long_text_thinking:
                    print(has_condition)
    
                if not with_memory:
                    # REGULA STRICTĂ: Dacă with_memory=False, ignorăm complet orice exemplu dependent de context
                    if has_condition:
                        continue
                    examples.append(ex.get('input_ids', []))
                    outputs.append(ex.get('output_ids', []))
                    examples_meta.append(ex)
                else:
                    # Dacă with_memory=True, validăm dacă exemplul condiționat îndeplinește criteriile contextuale curente
                    if has_condition:
                        # Dacă istoria conversației este prea scurtă, nu folosim exemplele condiționate
                        if last_user_count < sens and last_bot_count < sens:
                            continue

                        # Condițiile cu if_last_... trebuie să fie relevante pentru promptul curent.
                        # Dacă input-ul exemplului condiționat nu se leagă de prompt, nu îl includem.
                        current_prompt_overlap = len(ex.get('input_words', set()).intersection(prompt_words))
                        if current_prompt_overlap == 0:
                            continue
                        
                        last_in_overlap = len(ex.get('if_last_input_words', set()).intersection(last_user_words))
                        last_out_overlap = len(ex.get('if_last_output_words', set()).intersection(last_bot_words))
            
                        if last_in_overlap > 0 or last_out_overlap > 0:
                            examples.append(ex.get('input_ids', []))
                            outputs.append(ex.get('output_ids', []))
                            examples_meta.append(ex)
                    else:
                        # Exemplele standard (necondiționate) sunt mereu incluse
                        examples.append(ex.get('input_ids', []))
                        outputs.append(ex.get('output_ids', []))
                        examples_meta.append(ex)

            if show_thinking:
                print("Ready!\n")

            if not examples:
                return fallback_no_understanded_message or ""

            if not examples:
                return fallback_no_understanded_message or ""

            try:
                matrix_rows = []
                for ex in examples:
                    row = np.bincount(ex, minlength=max_id + 1).astype(float)
                    matrix_rows.append(row)
                example_matrix = np.vstack(matrix_rows)

                # 4) Calcul vectorizat: dot-products -> cosine similarity
                dots = example_matrix.dot(prompt_hist)
                ex_norms = np.linalg.norm(example_matrix, axis=1)
                prompt_norm = np.linalg.norm(prompt_hist) + 1e-12
                cos_sim = dots / (ex_norms * prompt_norm + 1e-12)

                # 5) Aplicăm 'sensitivity'
                try:
                    sens = float(sensitivity)
                except Exception:
                    sens = 1.0
                cos_sim = cos_sim * sens

                # 6) Alegem cel mai bun exemplu (posibil sampled by temperature)
                try:
                    cos_list = list(map(float, cos_sim.tolist())) if hasattr(cos_sim, 'tolist') else list(map(float, cos_sim))
                except Exception:
                    cos_list = [float(x) for x in cos_sim]

                # Ajustăm scorurile cu un boost pentru potrivirea memoriei și pentru saluturi la prima interacțiune
                try:
                    inv_vocab = {v: k for k, v in total_vocab.items()}
                except Exception:
                    inv_vocab = {}

                # Pregătim vectorul de boost-uri
                boosts = [0.0] * len(cos_list)

                # Factori de boost (ajustabili)
                MEMORY_BOOST_FACTOR = 1.0
                GREETING_BOOST_FACTOR = 1.0

                # Detectăm dacă prompt-ul este un salut simplu (heuristic)
                GREET_WORDS = set(['salut', 'salut!', 'hello', 'hey', 'hei', 'buna', 'bună'])
                prompt_words_set = set(words)
                is_greeting_prompt = bool(prompt_words_set.intersection(GREET_WORDS))

                # Aplicați boost pe fiecare exemplu pe baza metadatelor (dacă avem)
                try:
                    for i, meta in enumerate(examples_meta):
                        # boost pentru exemplele condiționate care au o potrivire de context activă
                        has_cond = bool(meta.get('if_last_input_words')) or bool(meta.get('if_last_output_words'))
                        if has_cond:
                            mem_match = 0
                            try:
                                mem_match += len(meta.get('if_last_input_words', set()).intersection(last_user_words))
                                mem_match += len(meta.get('if_last_output_words', set()).intersection(last_bot_words))
                            except Exception:
                                mem_match = 0
                            if mem_match > 0:
                                boosts[i] += MEMORY_BOOST_FACTOR * float(mem_match)

                        # boost pentru răspunsuri care sunt saluturi când prompt-ul e salut și nu există istorie
                        if is_greeting_prompt and not last_user_words:
                            out_ids = outputs[i] if i < len(outputs) else []
                            out_words = set()
                            for oid in out_ids:
                                w = inv_vocab.get(oid)
                                if w:
                                    out_words.add(w.lower())
                            if out_words & GREET_WORDS:
                                boosts[i] += GREETING_BOOST_FACTOR
                except Exception:
                    pass

                # Aplicăm boost-urile la lista de scoruri pentru a determina alegerea finală
                adj_scores = [float(cos_list[i]) + boosts[i] for i in range(len(cos_list))]

                best_idx = int(np.argmax(adj_scores))
                best_score = float(adj_scores[best_idx])

                # If temperature > 0, sample among examples proportionally to similarity
                if temperature and float(temperature) > 0.0:
                    # Folosim scorurile ajustate (with memory/greeting boosts) pentru sampling
                    candidates = [(adj_scores[i], i) for i in range(len(cos_list))]
                    chosen_idx = bot_instance._choose_by_temperature(candidates, temperature)
                    try:
                        best_idx = int(chosen_idx)
                        best_score = float(cos_list[best_idx])
                    except Exception:
                        pass

                # Prag minimal de încredere
                MIN_ACCEPT_SCORE = 0.05
                if best_score < MIN_ACCEPT_SCORE:
                    # CORECTURĂ: Fallback pe limbi, similar cu engine-ul 'stable'
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        resp = "Nu sunt sigur că am înțeles, dar sună interesant!"
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        resp = "I'm not sure if I understand, but it sounds interesting!"
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        resp = "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                    else:
                        resp = fallback_no_understanded_message or fallback_not_sure_message or ""
                    
                    bot_instance.last_user_prompt = str(prompt)
                    bot_instance.last_bot_output = resp
                    return resp

                # 7) Extragem output-ul asociat exemplului ales
                chosen_output_ids = outputs[best_idx] if best_idx < len(outputs) else []
                
                # Reconstruim string din id-uri
                id_to_word = getattr(bot_instance, "id_to_word", None)
                if id_to_word:
                    out_tokens = [id_to_word.get(i, str(i)) for i in chosen_output_ids]
                else:
                    inv = {v: k for k, v in total_vocab.items()}
                    out_tokens = [inv.get(i, str(i)) for i in chosen_output_ids]

                response = " ".join(out_tokens).strip()

                # Salvăm "memoria" locală
                bot_instance.last_user_prompt = str(prompt) if with_memory == True else None
                bot_instance.last_bot_output = response if with_memory == True else None

                if show_thinking:
                    print("I'm done processing the prompt. Now I can send the final response.\n")
                    print("[STOP THINKING]\n")
                    print("---")

                if show_debug:
                    print("---")
                    print("[START DEBUG]\n")
                    print("user prompt: " + prompt)
                    print("\nINPUT METRICS:")
                    print(f"total vocabulary size: {len(total_vocab)}")
                    print(f"prompt words count: {len(words)}")
                    print(f"prompt_ids_full: {prompt_ids_full}")
                    print(f"prompt_ids filtered: {prompt_ids}")
                    print(f"last_ids: {last_ids}")
                    print(f"examples considered: {len(examples)}")
                    print(f"best index: {best_idx}, best_score: {best_score:.4f}")

                    print("\nDEBUG CATEGORIES:")
                    understood_count = len(prompt_ids)
                    total_count = len(prompt_ids_full)
                    understanding_pct = 0.0
                    if total_count > 0:
                        understanding_pct = understood_count / total_count * 100.0
                    print(f"- Understanding: detected {understood_count}/{total_count} words")
                    print(f"- Understanding rate: {understanding_pct:.2f}%")
                    print("- Cosine matches sample (first 8): {}".format(cos_list[:8] if len(cos_list) > 0 else []))
                    print("- Memory boost applied: {}".format('yes' if with_memory and last_ids else 'no'))

                    print("\nOUTPUT CHOICE:")
                    print(f"chosen example index: {best_idx}")
                    print(f"chosen_output_ids: {chosen_output_ids}")
                    print(f"final response: {response}")

                    print("\n[STOP DEBUG]")
                    print("---")

                return response

            except MemoryError:
                # Fallback la metoda liniară în caz de eroare de memorie cu numpy
                prompt_set = set(prompt_ids)
                if last_ids:
                    prompt_set.update(last_ids)
                
                best_idx = -1
                best_score = -1.0
                
                for idx, ex in enumerate(examples):
                    # scor = intersecția simplă
                    inter = len(prompt_set & set(ex))
                    score = inter / (len(ex) + 1e-9)
                    if score > best_score:
                        best_score = score
                        best_idx = idx

                if best_idx == -1 or best_score <= 0:
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        return "Nu sunt sigur că am înțeles, dar sună interesant!"
                    return fallback_no_understanded_message or ""

                chosen_output_ids = outputs[best_idx] if best_idx < len(outputs) else []
                id_to_word = getattr(bot_instance, "id_to_word", {v: k for k, v in total_vocab.items()})
                response = " ".join(id_to_word.get(i, str(i)) for i in chosen_output_ids).strip()
                
                bot_instance.last_user_prompt = str(prompt) if with_memory == True else None
                bot_instance.last_bot_output = response if with_memory == True else None
                return response

            except Exception:
                # Fallback final
                return ""