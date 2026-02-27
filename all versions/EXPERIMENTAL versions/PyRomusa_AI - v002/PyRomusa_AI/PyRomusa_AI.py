# Cod pentru evitarea erorilor când codul întâlnește litere românești (ă, î, â, ș, ț)
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    # Fallback pentru versiuni Python mai învechite
    import io
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass


# Începutul real al librăriei începe de aici
class Chatbot:
    def __init__(self, total_vocabulary=None, training_dataset=None, tokens=None, chatbot_name="ChatBot"):
        self.total_vocabulary = total_vocabulary if total_vocabulary is not None else {}
        self.training_dataset = training_dataset if training_dataset is not None else []
        self.tokens = tokens if tokens is not None else []
        self.chatbot_name = chatbot_name

        self.translated_input_and_output_examples = []
        # Pentru contextul conversației: ultimul prompt al utilizatorului și ultimul output generat
        self.last_user_prompt = ""
        self.last_bot_output = ""

        self.trainer = self.Train(self)
        self.helper = self.Help(self)
        self.prepared_datasets = self.Datasets(self)


    class Help:
        def __init__(self, parent):
            self.parent = parent

        def examples_of_scripts_as_rookie(self):
            return print("-----\n--- Here you will find some script examples to practice and learn how to work with this library. ---\n\nExample 1: The most basic use of this library (creating a functional chatbot)\nfrom PyRomusa_AI import Chatbot\n\nbot = Chatbot()\nbot.trainer.add_data('Hello chatbot!', 'Hello human! What is your name and how can I help you today?')\nbot.trainer.start()\nbot.reply_at('Hello chatbot!')\n\nExample 2: Creating multiple chatbots in a single script and naming them\nfrom PyRomusa_AI import Chatbot\n\nbot = Chatbot(chatbot_name='Romusa1')\nbot1 = Chatbot(chatbot_name='Romusa2')\nbot2 = Chatbot(chatbot_name='Romusa3')\n-----")

        def questions(self):
            return print("-----\n--- Here you will find some questions about the possibilities and usage of this library, which you probably wanted answers to. ---\n\nQuestion 1: Is it possible to create multiple chatbots in a single script?\nAnswer: Yes, it is 100% possible to create more than one chatbot. You just need to create multiple instances (bot = Chatbot(), bot1 = Chatbot(), bot2 = Chatbot(), ...). You can also assign a name to your chatbot using the 'chatbot_name' attribute (e.g. bot = Chatbot(chatbot_name='PyRomusa Bot 1')). The names of the chatbots do not affect the performance or behavior of the chatbot during training or replying.\n-----")

        def how_to_start(self):
            return print("-----\n\nFirst, we need to understand what this library is. This library is a technology specialized in creating your own chatbot in the simplest way possible (just 5 lines of code to train your first chatbot: import the library, create a chatbot, add a simple input/output example, start the training, and generate a response).\n\nWARNING! The logic of this library (the 'create a chatbot from scratch' concept) is not the same as a 100% traditional AI. It is built using the creator's own logic and is ONLY INSPIRED by traditional AI concepts. For example, you will not find things like hidden layers, different optimizers, or loss functions in this library.\n\n--- HOW TO START? ---\nA special helper function was created to guide you through using this library (you already used it if you wrote something like: bot.helper.how_to_start()). If you want more information, just replace how_to_start() with one of the following (depending on your needs): \n- examples_of_scripts_as_rookie() - Shows complete examples of how to use this library; \n- describe_functions() - Displays a table with important functions and their descriptions; \n- questions() - Answers some frequently asked questions.\n-----")

        def describe_functions(self):
            import pandas as pd
            tabel_functions = pd.DataFrame({
                "function": ["bot.trainer.add_data()", "bot.trainer.show_dataset()", "bot.trainer.start()", "bot.trainer.show_translated_examples()", "bot.trainer.show_relationed_output_with_input_words()", "bot.trainer.show_relationed_output_with_input_ids()", "bot.reply_at()", "bot.prepared_datasets.romanian.load_prepared_dataset()", "bot.trainer.show_number_of_examples()"],
                "min number of values": [2, 0, 0, 0, 0, 0, 1, 1, 0],
                "info": ["Adds examples type input/output in the dataset for the training chatbot", "Shows the current train examples for the chatbot (the dataset)", "Starts you train for chatbot, using the examples input/output finded in the dataset", "Shows you the examples in chatbot language (words -> tokens)", "Shows the words what can use the chatbot (value) if exist a any unique word (key)", "Shows the tokens what can use the chatbot (value) if exist a any unique token (key) in the input", "Generates a output using a prompt", "Loads a prepared dataset for training in romanian language", "Shows the total number of examples what exist in the current dataset of a chatbot"]
            })
            return print(f"\n-----\n--- Here are the most important functions of this library, explained in the simplest and clearest way possible. As a beginner, it is recommended to read these descriptions to better understand what each function does. ---\n\nNOTE: Before using any of these functions, make sure you have this line in your code:\nbot = Chatbot()\n\n{tabel_functions}\n-----")


    class Datasets:
        def __init__(self, parent):
            self.parent = parent

            self.romanian = self.Romanian(self)

        def add_data(self, training_input_example: str, training_output_example: str, if_last_input: str = None, if_last_output: str = None):
            # Salvăm intrările într-un format compatibil cu versiunile vechi (dict pentru extensibilitate)
            entry = {
                'input': training_input_example,
                'output': training_output_example,
                'if_last_input': if_last_input,
                'if_last_output': if_last_output,
            }
            self.parent.training_dataset.append(entry)

        class Romanian:
            def __init__(self, parent):
                self.parent = parent
            
            
            def load_prepared_dataset(self, dataset_name: str):
                # Dataset 1:
                # NAME: --- Default Romanian Dataset: LOW-END ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 250
                # TOTAL VOCABULARY: aprox. 3625 elements (words)
                if dataset_name.lower() in ["low", "low end", "low-end", 'low-dataset', 'low dataset']:
                    
                    try:
                        from .Datasets import Default_Romanian_Dataset_LOW_END
                        
                        Default_Romanian_Dataset_LOW_END.load_dataset(self.parent.parent)
                        
                        print("INFO: Dataset 'Default Romanian Dataset: LOW-END' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'Default Romanian Dataset: LOW-END' module. Reason: {e}")
                    except Exception as e:

                        print(f"ERROR: An error occurred while loading 'Default Romanian Dataset: LOW-END' dataset: {e}")

                # Dataset 2:
                # NAME: --- Default Romanian Dataset: MID-RANGE ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 500
                # TOTAL VOCABULARY: aprox. 8242 elements (words)
                if dataset_name.lower() in ['mid', 'mid-range', 'mid range', 'mid-dataset', 'mid dataset']:
                    
                    try:
                        from .Datasets import Default_Romanian_Dataset_MID_RANGE

                        Default_Romanian_Dataset_MID_RANGE.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'Default Romanian Dataset: MID-RANGE' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'Default Romanian Dataset: MID-RANGE' module. Reason: {e}")
                    except Exception as e:
                        
                        print(f"ERROR: An error occurred while loading 'Default Romanian Dataset: MID-RANGE' dataset: {e}")

                # Dataset 3:
                # NAME: --- Default Romanian Dataset: HIGH-END ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 1000
                # TOTAL VOCABULARY: aprox. 11581 elements (words)
                if dataset_name.lower() in ('high', 'high-end', 'high end', 'high-dataset', 'high dataset'):
                    
                    try:
                        from .Datasets import Default_Romanian_Dataset_HIGH_END

                        Default_Romanian_Dataset_HIGH_END.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'Default Romanian Dataset: HIGH-END' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'Default Romanian Dataset: HIGH-END' module. Reason: {e}")
                    except Exception as e:
                        
                        print(f"ERROR: An error occurred while loading 'Default Romanian Dataset: HIGH-END' dataset: {e}")


                # Dataset 4
                # NAME: --- High Quality, Very Low Quantity Romanian Dataset  ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 50
                # TOTAL VOCABULARY: aprox. 496 elements (words)
                if dataset_name.lower() in ('high quality very low quantity', 'high-quality-very-low-quantity', 'high quality 1', 'high-quality-1'):

                    try:
                        from .Datasets import High_Quality_Very_Low_Quantity_Romanian_Dataset

                        High_Quality_Very_Low_Quantity_Romanian_Dataset.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'High Quality, Very Low Quantity Romanian Dataset' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'High Quality, Very Low Quantity Romanian Dataset' module. Reason: {e}")
                    except Exception as e:
                        
                        print(f"ERROR: An error occurred while loading 'High Quality, Very Low Quantity Romanian Dataset' dataset: {e}")


                # Dataset 5
                # NAME: --- High Quality, Low Quantity Romanian Dataset ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 100
                # TOTAL VOCABULARY: aprox. 874 elements (words)
                if dataset_name.lower() in ('high quality low quantity', 'high-quality-low-quantity', 'high quality 2', 'high-quality-2'):
                    
                    try:
                        from .Datasets import High_Quality_Low_Quantity_Romanian_Dataset

                        High_Quality_Low_Quantity_Romanian_Dataset.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'High Quality, Low Quantity Romanian Dataset' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'High Quality, Low Quantity Romanian Dataset' module. Reason: {e}")
                    except Exception as e:
                        
                        print(f"ERROR: An error occurred while loading 'High Quality, Low Quantity Romanian Dataset' dataset: {e}")

                
                # Dataset 6
                # NAME: --- Teacher for PyRomusa AI ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 110
                # TOTAL VOCABULARY: aprox. 397 elements (words)
                if dataset_name.lower() in ('teacher', 'pyromusa ai tutorial', 'pyromusa ai teacher', 'pyromusa-ai-teacher', 'pyromusa-ai-tutorial'):

                    try:
                        from .Datasets import Teacher_for_PyRomusa_AI
                        
                        Teacher_for_PyRomusa_AI.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'Teacher for PyRomusa AI' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'Teacher for PyRomusa AI' module. Reason: {e}")
                    except Exception as e:
                        
                        print(f"ERROR: An error occurred while loading 'Teacher for PyRomusa AI' dataset: {e}")

    class Train:    
        def __init__(self, parent):
            # Salvăm referința către instanța de chatbot
            self.parent = parent

        def add_data(self, training_input_example: str, training_output_example: str, if_last_input: str = None, if_last_output: str = None):
            # Acceptăm și format extins cu condiții opționale
            entry = {
                'input': training_input_example,
                'output': training_output_example,
                'if_last_input': if_last_input,
                'if_last_output': if_last_output,
            }
            self.parent.training_dataset.append(entry)

        def show_dataset(self):
            return print(self.parent.training_dataset)

        def start(self):
            # 1. Transformăm toate cuvintele găsite în exemplele input-output în tokene numerice + le adăugăm la vocabularul chatbot-ului (fiecare număr ce cuvânt înseamnă)
            # Normalizăm intrările: susținem atât vechiul format (tuple/list), cât și dict-urile noi
            for sample in self.parent.training_dataset:
                if isinstance(sample, dict):
                    fields = [sample.get('input', ''), sample.get('output', ''), sample.get('if_last_input', ''), sample.get('if_last_output', '')]
                elif isinstance(sample, (list, tuple)):
                    # tuple vechi: (input, output) or (input, output, if_last_input, if_last_output)
                    fields = list(sample) + [None] * (4 - len(sample))
                else:
                    fields = [str(sample), '', None, None]

                for part in fields:
                    if not part:
                        continue
                    for word in str(part).split():
                        if word not in self.parent.total_vocabulary:
                            self.parent.total_vocabulary[word] = len(self.parent.total_vocabulary) + 1
                            self.parent.tokens.append(self.parent.total_vocabulary[word])

            # 2. Traducem exemplele input-output: string (cuvinte) -> tokens (numere)

            self.input_words = []
            self.output_words = []
            translated = []

            for sample in self.parent.training_dataset:
                if isinstance(sample, dict):
                    inp = str(sample.get('input', ''))
                    out = str(sample.get('output', ''))
                    if_last_in = sample.get('if_last_input')
                    if_last_out = sample.get('if_last_output')
                elif isinstance(sample, (list, tuple)):
                    # suportăm și tuple/list vechi
                    inp = str(sample[0]) if len(sample) > 0 else ''
                    out = str(sample[1]) if len(sample) > 1 else ''
                    if_last_in = sample[2] if len(sample) > 2 else None
                    if_last_out = sample[3] if len(sample) > 3 else None
                else:
                    inp = str(sample)
                    out = ''
                    if_last_in = None
                    if_last_out = None

                # transformăm în id-uri
                inp_ids = [self.parent.total_vocabulary[w] for w in inp.split() if w in self.parent.total_vocabulary]
                out_ids = [self.parent.total_vocabulary[w] for w in out.split() if w in self.parent.total_vocabulary]

                self.input_words.append(inp_ids)
                self.output_words.append(out_ids)

                translated.append({
                    'input_ids': inp_ids,
                    'output_ids': out_ids,
                    'if_last_input_words': set(str(if_last_in).lower().split()) if if_last_in else set(),
                    'if_last_output_words': set(str(if_last_out).lower().split()) if if_last_out else set(),
                    'input_words': set(str(inp).lower().split()),
                    'output_words': set(str(out).lower().split()),
                })

            # stocăm exemplele traduse ca listă de dict-uri pentru acces extins
            self.parent.translated_input_and_output_examples = translated
                        

            # 3. Pentru fiecare cuvânt găsit în input-urile din translated_input_and_output_examples, găsim toate cuvintele posibile pentru fiecare cuvânt din output
            
            # Construim o hartă inversă id -> cuvânt
            id_to_word = {v: k for k, v in self.parent.total_vocabulary.items()}

            # Mapări: cuvânt (string) -> listă de cuvinte (string)
            # și id_cuvânt (int) -> listă de id-uri (int)
            input_word_to_output_words = {}
            input_word_id_to_output_ids = {}

            for ex in self.parent.translated_input_and_output_examples:
                inp_ids = ex.get('input_ids', [])
                out_ids = ex.get('output_ids', [])
                for in_id in inp_ids:
                    input_word_id_to_output_ids.setdefault(in_id, []).extend(out_ids)
                    input_word_to_output_words.setdefault(
                        id_to_word.get(in_id, str(in_id)),
                        []).extend([id_to_word.get(o, str(o)) for o in out_ids])

            # Funcție auxiliară pentru a elimina duplicate păstrând ordinea
            def _unique_preserve(seq):
                seen = set()
                res = []
                for x in seq:
                    if x not in seen:
                        seen.add(x)
                        res.append(x)
                return res

            for k in list(input_word_id_to_output_ids.keys()):
                input_word_id_to_output_ids[k] = _unique_preserve(input_word_id_to_output_ids[k])
            for k in list(input_word_to_output_words.keys()):
                input_word_to_output_words[k] = _unique_preserve(input_word_to_output_words[k])

            # Salvăm pe parent pentru a fi folosite și la răspunsuri
            self.parent.input_word_to_output_words = input_word_to_output_words
            self.parent.input_word_id_to_output_ids = input_word_id_to_output_ids
            self.parent.id_to_word = id_to_word

            return self.parent.total_vocabulary, self.parent.tokens
        
        def show_translated_examples(self):
            return print(self.parent.translated_input_and_output_examples)
        
        def show_number_of_examples(self):
            count = len(getattr(self.parent, "training_dataset", []))
            return print(count)
        
        def show_relationed_output_with_input_words(self):
            return print(self.parent.input_word_to_output_words)
        
        def show_relationed_output_with_input_ids(self):
            return print(self.parent.input_word_id_to_output_ids)



    def reply_at(self, prompt: str, engine_name="stable", sensitivity: int = 1, with_memory: bool = True, fallback_language="english", fallback_empty_string_message="", fallback_no_understanded_message="", fallback_not_sure_message=""):
        if engine_name.lower() in ("stable"):
            
            if with_memory == True:
                # 1. Transformăm întrebarea utilizatorului în ID-uri (tokens)
                words = str(prompt).lower().split()

                # Dacă prompt-ul este complet gol, se merge pe ramura asta
                if not words:
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Te ascult..."
                        except Exception:
                            pass
                        return "Te ascult..."
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "I am listening to you..."
                        except Exception:
                            pass
                        return "I am listening to you..."
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Te estoy escuchando..."
                        except Exception:
                            pass
                        return "Te estoy escuchando..."
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral") and fallback_empty_string_message:
                            try:
                                self.last_user_prompt = str(prompt)
                                self.last_bot_output = fallback_empty_string_message
                            except Exception:
                                pass
                            return fallback_empty_string_message


                # Obținem ID-urile pentru cuvintele cunoscute
                input_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]
    
                if not input_ids:
                    if not words:
                        if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                            try:
                                self.last_user_prompt = str(prompt)
                                self.last_bot_output = "Interesant, poți să-mi zici mai multe?"
                            except Exception:
                                pass
                            return "Interesant, poți să-mi zici mai multe?"
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Interesting, can you tell me more?"
                        except Exception:
                            pass
                        return "Interesting, can you tell me more?"
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Interesante, ¿puedes contarme más?"
                        except Exception:
                            pass
                        return "Interesante, ¿puedes contarme más?"
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_no_understanded_message:
                            try:
                                self.last_user_prompt = str(prompt)
                                self.last_bot_output = fallback_no_understanded_message
                            except Exception:
                                pass
                            return fallback_no_understanded_message

                best_score = -1
                best_response = []

                # Pregătim seturi pentru ultima conversație
                last_user_words = set(str(self.last_user_prompt).lower().split()) if getattr(self, 'last_user_prompt', None) else set()
                last_bot_words = set(str(self.last_bot_output).lower().split()) if getattr(self, 'last_bot_output', None) else set()

                # 2. Căutăm în exemplele de antrenament cea mai bună potrivire
                # translated_input_and_output_examples este lista de dict-uri
                for ex in self.translated_input_and_output_examples:
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

                    if combined_score > best_score and accept_example:
                        best_score = combined_score
                        best_response = train_out_ids if train_out_ids else list(ex.get('output_words', []))

                # 3. Traducem ID-urile răspunsului înapoi în cuvinte
                if best_score > 0:
                    id_to_word = self.id_to_word
                    # Dacă best_response conține id-uri, traducem; altfel considerăm că sunt cuvinte
                    if all(isinstance(i, int) for i in best_response):
                        response_words = [id_to_word.get(i, "") for i in best_response]
                        response = " ".join(response_words).strip()
                    else:
                        # best_response poate fi listă de stringuri (output_words)
                        response = " ".join([str(w) for w in best_response]).strip()

                    # Actualizăm contextul conversației
                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = response
                    except Exception:
                        pass

                    return response

                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = "Nu sunt sigur că am înțeles, dar sună interesant!"
                    except Exception:
                        pass
                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
            
                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = "I'm not sure if I understand, but it sounds interesting!"
                    except Exception:
                        pass
                    return "I'm not sure if I understand, but it sounds interesting!"
                
                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                    except Exception:
                        pass
                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                
                else:
                    if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_not_sure_message:
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = fallback_not_sure_message
                        except Exception:
                            pass
                        return fallback_not_sure_message
            
            elif with_memory == False:

                # 1. Transformăm întrebarea utilizatorului în ID-uri (tokens)
                words = str(prompt).lower().split()

                # Dacă prompt-ul este complet gol, se merge pe ramura asta
                if not words:
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        return "Te ascult..."
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        return "I am listening to you..."
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        return "Te estoy escuchando..."
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral") and fallback_empty_string_message:
                            return fallback_empty_string_message


                # Obținem ID-urile pentru cuvintele cunoscute
                input_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]
    
                if not input_ids:
                    if not words:
                        if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                            return "Interesant, poți să-mi zici mai multe?"
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        return "Interesting, can you tell me more?"
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        return "Interesante, ¿puedes contarme más?"
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_no_understanded_message:
                            return fallback_no_understanded_message

                best_score = -1
                best_response = []

                # 2. Căutăm în exemplele de antrenament cea mai bună potrivire
                # translated_input_and_output_examples este lista de dict-uri
                    # Pentru a garanta că `with_memory=False` nu va lua în seamă contextul ultimei conversații,
                    # curățăm temporar atributele de context pe durata căutării și le restaurăm la final.
                orig_last_user = getattr(self, 'last_user_prompt', None)
                orig_last_bot = getattr(self, 'last_bot_output', None)
                try:
                    self.last_user_prompt = ""
                    self.last_bot_output = ""
                    for ex in self.translated_input_and_output_examples:
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
                            last_in_overlap = len(ex['if_last_input_words'].intersection(set(str(getattr(self, 'last_user_prompt', '')).lower().split())))
                        if ex.get('if_last_output_words'):
                            last_out_overlap = len(ex['if_last_output_words'].intersection(set(str(getattr(self, 'last_bot_output', '')).lower().split())))

                        has_condition = bool(ex.get('if_last_input_words')) or bool(ex.get('if_last_output_words'))
                        ctx_threshold = sensitivity if (sensitivity and sensitivity > 0) else 1
                        context_matches = (last_in_overlap >= ctx_threshold) or (last_out_overlap >= ctx_threshold)

                        # Dacă exemplul este condiționat și contextul nu se potrivește, sărim exemplul
                        if has_condition and not context_matches:
                            continue

                        # Dacă am găsit o potrivire mai bună, o memorăm
                        if current_score > best_score:
                            best_score = current_score
                            best_response = train_out_ids
                finally:
                    try:
                        self.last_user_prompt = orig_last_user
                        self.last_bot_output = orig_last_bot
                    except Exception:
                        pass

                # 3. Traducem ID-urile răspunsului înapoi în cuvinte
                if best_score > 0:
                    id_to_word = self.id_to_word
                    response_words = [id_to_word.get(i, "") for i in best_response]
                    return " ".join(response_words).strip()

                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
            
                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                    return "I'm not sure if I understand, but it sounds interesting!"
                
                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                
                else:
                    if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_not_sure_message:
                        return fallback_not_sure_message


        elif engine_name.lower() == "chaos":

            # Transformăm prompt-ul în cuvinte și obținem id-urile cunoscute
            words = str(prompt).split()
            if not words:
                return ""
        
            known_word_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]

            # Numărăm, aproximativ, numărul de cuvinte (pentru a decide lungimea răspunsului)
            prompt_list_type = list(prompt) 
            words_total_number = 1
            for word in prompt_list_type:
                if word == " ":
                    words_total_number += 1
                else:
                    continue
       
            # Colectăm sugestii de id-uri din maparea construită la antrenare
            suggestions = []
            mapping = getattr(self, 'input_word_id_to_output_ids', {})
            for wid in known_word_ids:
                if wid is None:
                    continue
                suggestions.extend(mapping.get(wid, []))

            # Dacă nu avem sugestii, revenim cu o propoziție fallback (primele tokens cunoscute)
            id_to_word = getattr(self, 'id_to_word', {v: k for k, v in self.total_vocabulary.items()})
            if not suggestions:
                if getattr(self, 'tokens', None):
                    return " ".join([id_to_word.get(t, "") for t in self.tokens[:1]]).strip()
                return ""

            # Rangăm id-urile după frecvență și reconstruim cuvintele cele mai probabile
            from collections import Counter
            cnt = Counter(suggestions)
            most_common_ids = [item for item, _ in cnt.most_common(9 * words_total_number)]
            response_words = [id_to_word.get(i, str(i)) for i in most_common_ids if i in id_to_word]

            # Returnăm răspunsul construit simplu, prin concatenarea cu spațiu
            return " ".join(response_words)
