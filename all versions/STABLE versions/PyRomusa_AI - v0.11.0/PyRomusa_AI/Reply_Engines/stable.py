# Reply Engine Code (stable)
def use_engine(bot_instance, prompt: str, 
            sensitivity: int = 1, 
            with_memory: bool = True, 
            max_inflenced_memory: int = 3,
            new_lines_system: bool = True,
            fallback_language="english", 
            fallback_empty_string_message="", 
            fallback_no_understanded_message="", 
            fallback_not_sure_message="", 
            temperature: float = 0.0,
            show_thinking=False,
            allow_long_text_thinking=True,
            show_debug=False):
    
    def format_new_lines(text):
        if hasattr(bot_instance, "_decode_new_lines"):
            return bot_instance._decode_new_lines(text, new_lines_system=new_lines_system)
        return text

    if with_memory == True:
                # 1. Transformăm întrebarea utilizatorului în ID-uri (tokens)
                words = str(prompt).lower().split()
                bot_instance._thinking(f"I hear the prompt, so I am reading it and splitting it into words: {words}", show_thinking, allow_long_text_thinking)
                bot_instance._thinking("I will now match these words with my known vocabulary.", show_thinking, allow_long_text_thinking)

                # Dacă prompt-ul este complet gol, se merge pe ramura asta
                if not words:
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        try:
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = "Te ascult..."
                        except Exception:
                            pass
                        bot_instance._stop_thinking(show_thinking)
                        return "Te ascult..."
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        try:
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = "I am listening to you..."
                        except Exception:
                            pass
                        bot_instance._stop_thinking(show_thinking)
                        return "I am listening to you..."
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        try:
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = "Te estoy escuchando..."
                        except Exception:
                            pass
                        bot_instance._stop_thinking(show_thinking)
                        return "Te estoy escuchando..."
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral") and fallback_empty_string_message:
                            try:
                                bot_instance.last_user_prompt = str(prompt)
                                bot_instance.last_bot_output = fallback_empty_string_message
                            except Exception:
                                pass
                        bot_instance._stop_thinking(show_thinking)

                # Obținem ID-urile pentru cuvintele cunoscute
                input_ids = [bot_instance.total_vocabulary.get(w) for w in words if w in bot_instance.total_vocabulary]
                bot_instance._thinking(f"I found these known words in my vocabulary: {input_ids}", show_thinking, allow_long_text_thinking)
                bot_instance._thinking("Next, I will score each training example based on the overlap with input words.", show_thinking, allow_long_text_thinking)
                bot_instance._debug("prompt words", str(words), show_debug)
                bot_instance._debug("known ids", str(input_ids), show_debug)
                if words:
                    understanding_rate = (len(input_ids)/len(words))*100.0
                    bot_instance._debug("understanding rate", f"{understanding_rate:.2f}%", show_debug)
                else:
                    bot_instance._debug("understanding rate", "0.00%", show_debug)
    
                if not input_ids:
                    if not words:
                        if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                            try:
                                bot_instance.last_user_prompt = str(prompt)
                                bot_instance.last_bot_output = "Interesant, poți să-mi zici mai multe?"
                            except Exception:
                                pass
                            bot_instance._stop_thinking(show_thinking)
                            return "Interesant, poți să-mi zici mai multe?"
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        try:
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = "Interesting, can you tell me more?"
                        except Exception:
                            pass
                            bot_instance._stop_thinking(show_thinking)
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        try:
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = "Interesante, ¿puedes contarme más?"
                        except Exception:
                            pass
                            bot_instance._stop_thinking(show_thinking)
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_no_understanded_message:
                            try:
                                bot_instance.last_user_prompt = str(prompt)
                                bot_instance.last_bot_output = fallback_no_understanded_message
                            except Exception:
                                pass
                            bot_instance._stop_thinking(show_thinking)
                            return fallback_no_understanded_message

                best_score = -1
                best_response = []
                # collect candidates for optional temperature sampling
                candidates = []

                # Pregătim contextul din ultimele N mesaje.
                recent_user_words, recent_bot_words = bot_instance._get_recent_conversation_words(max_inflenced_memory)
                last_user_words = set(recent_user_words)
                last_bot_words = set(recent_bot_words)

                # 2. Căutăm în exemplele de antrenament cea mai bună potrivire
                # translated_input_and_output_examples este lista de dict-uri
                bot_instance._thinking("I am now checking every training example to compute overlap scores.", show_thinking, allow_long_text_thinking)
                for ex in bot_instance.translated_input_and_output_examples:
                    train_inp_ids = ex.get('input_ids', [])
                    train_out_ids = ex.get('output_ids', [])

                    # overlap pe input-ul curent
                    current_score = 0
                    for token in input_ids:
                        if token in train_inp_ids:
                            current_score += 1

                    # overlap-uri contextuale pe baza campurilor if_last_*
                    last_in_overlap = 0
                    last_out_overlap = 0
                    if ex.get('if_last_input_words'):
                        last_in_overlap = len(ex['if_last_input_words'].intersection(last_user_words))
                    if ex.get('if_last_output_words'):
                        last_out_overlap = len(ex['if_last_output_words'].intersection(last_bot_words))

                    # Scor final combinat: contextul poate compensa lipsa unei potriviri directe
                    combined_score = current_score + last_in_overlap + last_out_overlap

                    # Dacă exemplul are condiții pe ultima conversație (if_last_input/if_last_output), tratăm
                    # acel exemplu ca fiind condiționat și nu îl acceptăm doar pe baza potrivirii de input.
                    has_condition = bool(ex.get('if_last_input_words')) or bool(ex.get('if_last_output_words'))

                    # Determinăm dacă contextul satisface pragul (folosim `sensitivity` când e > 0,
                    # altfel considerăm că este nevoie de cel puțin o potrivire contextuală).
                    ctx_threshold = sensitivity if (sensitivity and sensitivity > 0) else 1
                    context_matches = (last_in_overlap >= ctx_threshold) or (last_out_overlap >= ctx_threshold)

                    # Acceptăm exemplul dacă are cel puțin o potrivire de input sau dacă contextul (dacă e permis)
                    # îl declanșează. Dacă exemplul este condiționat, atunci cerem neapărat context_matches pentru
                    # a putea folosi exemplul.
                    if has_condition:
                        accept_example = context_matches and (combined_score > 0 or context_matches)
                    else:
                        accept_example = (combined_score > 0) or context_matches

                    if accept_example and combined_score > 0:
                        resp_obj = train_out_ids if train_out_ids else list(ex.get('output_words', []))
                        candidates.append((combined_score, resp_obj))
                        if combined_score > best_score:
                            best_score = combined_score
                            best_response = resp_obj

                # 3. Traducem ID-urile răspunsului înapoi în cuvinte
                if best_score > 0 and candidates:
                    bot_instance._thinking(f"I have {len(candidates)} candidate responses; selecting best with score {best_score}.", show_thinking, allow_long_text_thinking)
                    chosen = bot_instance._choose_by_temperature(candidates, temperature)
                    bot_instance._thinking(f"Response token ids selected: {chosen}", show_thinking, allow_long_text_thinking)
                    id_to_word = bot_instance.id_to_word
                    if all(isinstance(i, int) for i in chosen):
                        response_words = [id_to_word.get(i, "") for i in chosen]
                        response = " ".join(response_words).strip()
                    else:
                        response = " ".join([str(w) for w in chosen]).strip()

                    try:
                        bot_instance.last_user_prompt = str(prompt)
                        bot_instance.last_bot_output = response
                    except Exception:
                        pass

                    bot_instance._debug("candidate_count", str(len(candidates)), show_debug)
                    bot_instance._debug("best score", str(best_score), show_debug)
                    bot_instance._debug("final response", response, show_debug)
                    
                    if show_debug == True:
                        print("[STOP DEBUG] \n\n")
                        print("---\n")

                    bot_instance._stop_thinking(show_thinking)

                    return format_new_lines(response)

                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                    try:
                        bot_instance.last_user_prompt = str(prompt)
                        bot_instance.last_bot_output = "Nu sunt sigur că am înțeles, dar sună interesant!"
                    except Exception:
                        pass
                    bot_instance._stop_thinking(show_thinking)
                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
            
                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                    try:
                        bot_instance.last_user_prompt = str(prompt)
                        bot_instance.last_bot_output = "I'm not sure if I understand, but it sounds interesting!"
                    except Exception:
                        pass
                    bot_instance._stop_thinking(show_thinking)
                    return "I'm not sure if I understand, but it sounds interesting!"
                
                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                    try:
                        bot_instance.last_user_prompt = str(prompt)
                        bot_instance.last_bot_output = "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                    except Exception:
                        pass
                    bot_instance._stop_thinking(show_thinking)
                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                
                else:
                    if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_not_sure_message:
                        try:
                            bot_instance.last_user_prompt = str(prompt)
                            bot_instance.last_bot_output = fallback_not_sure_message
                        except Exception:
                            pass
                        bot_instance._stop_thinking(show_thinking)
                        return fallback_not_sure_message
            
    elif with_memory == False:

                # 1. Transformăm întrebarea utilizatorului în ID-uri (tokens)
                words = str(prompt).lower().split()
                bot_instance._thinking(f"I read the prompt and split it into words: {words}", show_thinking, allow_long_text_thinking)
                bot_instance._debug("prompt words", str(words), show_debug)
                bot_instance._thinking("No memory mode: I will ignore past dialog and only use direct input.", show_thinking, allow_long_text_thinking)

                # Dacă prompt-ul este complet gol, se merge pe ramura asta
                if not words:
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        bot_instance._stop_thinking(show_thinking)
                        return "Te ascult..."
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        bot_instance._stop_thinking(show_thinking)
                        return "I am listening to you..."
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        bot_instance._stop_thinking(show_thinking)
                        return "Te estoy escuchando..."
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral") and fallback_empty_string_message:
                            bot_instance._stop_thinking(show_thinking)
                            return fallback_empty_string_message


                # Obținem ID-urile pentru cuvintele cunoscute
                input_ids = [bot_instance.total_vocabulary.get(w) for w in words if w in bot_instance.total_vocabulary]
                bot_instance._thinking(f"I matched known words to IDs: {input_ids}", show_thinking, allow_long_text_thinking)
                bot_instance._thinking("Now I will compute matching scores for existing training examples.", show_thinking, allow_long_text_thinking)
                bot_instance._debug("known ids", str(input_ids), show_debug)
                if words:
                    understanding_rate = (len(input_ids)/len(words))*100.0
                    bot_instance._debug("understanding rate", f"{understanding_rate:.2f}%", show_debug)
                else:
                    bot_instance._debug("understanding rate", "0.00%", show_debug)
    
                if not input_ids:
                    if not words:
                        if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                            bot_instance._stop_thinking(show_thinking)
                            return "Interesant, poți să-mi zici mai multe?"
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        bot_instance._stop_thinking(show_thinking)
                        return "Interesting, can you tell me more?"
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        bot_instance._stop_thinking(show_thinking)
                        return "Interesante, ¿puedes contarme más?"
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_no_understanded_message:
                            bot_instance._stop_thinking(show_thinking)
                            return fallback_no_understanded_message

                best_score = -1
                best_response = []
                candidates = []

                # 2. Căutăm în exemplele de antrenament cea mai bună potrivire
                # translated_input_and_output_examples este lista de dict-uri
                # Pentru a garanta că `with_memory=False` nu va lua în seamă contextul ultimei conversații,
                # curățăm temporar atributele de context pe durata căutării și le restaurăm la final.
                orig_last_user = getattr(bot_instance, 'last_user_prompt', None)
                orig_last_bot = getattr(bot_instance, 'last_bot_output', None)
                try:
                    bot_instance.last_user_prompt = ""
                    bot_instance.last_bot_output = ""
                    for ex in bot_instance.translated_input_and_output_examples:
                        train_inp_ids = ex.get('input_ids', [])
                        train_out_ids = ex.get('output_ids', [])
                        # Calculăm scorul: câte ID-uri din prompt se găsesc în acest exemplu de antrenament
                        current_score = 0
                        for token in input_ids:
                            if token in train_inp_ids:
                                current_score += 1

                        # overlap-uri contextuale pe baza campurilor if_last_*
                        last_in_overlap = 0
                        last_out_overlap = 0
                        if ex.get('if_last_input_words'):
                            last_in_overlap = len(ex['if_last_input_words'].intersection(set(str(getattr(bot_instance, 'last_user_prompt', '')).lower().split())))
                        if ex.get('if_last_output_words'):
                            last_out_overlap = len(ex['if_last_output_words'].intersection(set(str(getattr(bot_instance, 'last_bot_output', '')).lower().split())))

                        has_condition = bool(ex.get('if_last_input_words')) or bool(ex.get('if_last_output_words'))
                        ctx_threshold = sensitivity if (sensitivity and sensitivity > 0) else 1
                        context_matches = (last_in_overlap >= ctx_threshold) or (last_out_overlap >= ctx_threshold)

                        # Dacă exemplul este condiționat și contextul nu se potrivește, sărim exemplul
                        if has_condition and not context_matches:
                            continue

                        # Dacă am găsit o potrivire mai bună, o memorăm
                        if current_score > 0:
                            candidates.append((current_score, train_out_ids))
                            if current_score > best_score:
                                best_score = current_score
                                best_response = train_out_ids
                finally:
                    try:
                        bot_instance.last_user_prompt = orig_last_user
                        bot_instance.last_bot_output = orig_last_bot
                    except Exception:
                        pass

                # 3. Traducem ID-urile răspunsului înapoi în cuvinte
                if best_score > 0 and candidates:
                    chosen = bot_instance._choose_by_temperature(candidates, temperature)
                    id_to_word = bot_instance.id_to_word
                    response_words = [id_to_word.get(i, "") for i in chosen]
                    bot_instance._debug("best score", str(best_score), show_debug)
                    bot_instance._debug("response token ids", str(chosen), show_debug)
                    
                    if show_debug == True:
                        print("[STOP DEBUG] \n\n")
                        print("---\n")

                    bot_instance._stop_thinking(show_thinking)

                    return format_new_lines(" ".join(response_words).strip())

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
