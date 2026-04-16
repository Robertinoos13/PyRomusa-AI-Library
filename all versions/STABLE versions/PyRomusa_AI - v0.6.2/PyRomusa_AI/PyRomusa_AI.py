# -*- coding: utf-8 -*-
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
            return print("-----\n--- Here you will find some questions about the possibilities and usage of this library, which you probably wanted answers to. ---\n\nQUESTION 1: Is it possible to create multiple chatbots in a single script?\nANSWER: Yes, it is 100% possible to create more than one chatbot. You just need to create multiple instances (bot = Chatbot(), bot1 = Chatbot(), bot2 = Chatbot(), ...). You can also assign a name to your chatbot using the 'chatbot_name' attribute (e.g. bot = Chatbot(chatbot_name='PyRomusa Bot 1')). The names of the chatbots do not affect the performance or behavior of the chatbot during training or replying.\n\nQUESTION 2: Does PyRomusa AI have a tokenization system?\nANSWER: Yes, it has a simplified tokenization system. More precisely, it consists of transforming the words found in the training examples into integers and all these tokens are saved in the chatbot's vocabulary (i.e. in the 'total_vocabulary' variable)\n\nQUESTION 3: Can chatbots created with this framework generate ASCII art?\nANSWER: Unfortunately, as of April 2026, chatbots made with this framework are not capable of generating ASCII art directly, because the only problem here is that when chatbots generate a response, they cannot start a new line to generate a response for you.\n-----")

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
            self.english = self.English(self)

        def add_data(self, training_input_example: str, training_output_example: str, if_last_input: str = None, if_last_output: str = None):
            # Salvăm intrările într-un format compatibil cu versiunile vechi (dict pentru extensibilitate)
            entry = {
                'input': training_input_example,
                'output': training_output_example,
                'if_last_input': if_last_input,
                'if_last_output': if_last_output,
            }
            self.parent.training_dataset.append(entry)

        class English:
            def __init__(self, parent):
                self.parent = parent

            def load_prepared_dataset(self, dataset_name: str):

                # Dataset 1
                # NAME: --- Default English Dataset: LOW-END ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 250
                # TOTAL VOCABULARY: aprox. 949 elements (words)
                if dataset_name.lower() in ("low", "low-end-dataset", "low-end", "low-dataset", "low dataset"):

                    try:
                        from .Datasets import Default_English_Dataset_LOW_END

                        Default_English_Dataset_LOW_END.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'Default English Dataset: LOW-END' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'Default English Dataset: LOW-END' module. Reason: {e}")
                    except Exception as e:

                        print(f"ERROR: An error occurred while loading 'Default English Dataset: LOW-END' dataset: {e}")

                # Dataset 2
                # NAME: --- Default English Dataset: MID-RANGE ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 500
                # TOTAL VOCABULARY: aprox. 1713 elements (words)
                if dataset_name.lower() in ("mid", "mid-range-dataset", "mid-range", "mid-dataset", "mid dataset"):

                    try:
                        from .Datasets import Default_English_Dataset_MID_RANGE

                        Default_English_Dataset_MID_RANGE.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'Default English Dataset: MID-RANGE' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'Default English Dataset: MID-RANGE' module. Reason: {e}")
                    except Exception as e:

                        print(f"ERROR: An error occurred while loading 'Default English Dataset: MID-RANGE' dataset: {e}")

                # Dataset 3
                # NAME: --- Default English Dataset: HIGH-END ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 1000
                # TOTAL VOCABULARY: aprox. 3100 elements (words)
                if dataset_name.lower() in ("high", "high-end-dataset", "high-end", "high-dataset", "high dataset"):

                    try:
                        from .Datasets import Default_English_Dataset_HIGH_END

                        Default_English_Dataset_HIGH_END.load_dataset(self.parent.parent)

                        print("INFO: Dataset 'Default English Dataset: HIGH-END' loaded successfully.")
                    
                    except ImportError as e:
                        
                        print(f"MINOR ERROR: Could not import dataset 'Default English Dataset: HIGH-END' module. Reason: {e}")
                    except Exception as e:

                        print(f"ERROR: An error occurred while loading 'Default English Dataset: HIGH-END' dataset: {e}")

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
        
        def show_translated_examples(self, with_print=True):
            if with_print:
                return print(self.parent.translated_input_and_output_examples)
            else:
                return self.parent.translated_input_and_output_examples
        
        def show_number_of_examples(self, with_print=True):
            count = len(getattr(self.parent, "training_dataset", []))
            if with_print:
                return print(count)
            else:
                return count
        
        def show_relationed_output_with_input_words(self, with_print=True):
            if with_print:
                return print(self.parent.input_word_to_output_words)
            else:
                return self.parent.input_word_to_output_words
        
        def show_relationed_output_with_input_ids(self, with_print=True):
            if with_print:
                return print(self.parent.input_word_id_to_output_ids)
            else:
                return self.parent.input_word_id_to_output_ids
        
    def show_basic_specs(self):
        print("total training examples: " + str(self.trainer.show_number_of_examples(with_print=False)))
        
        print("total vocabulary length: " + str(len(self.total_vocabulary)))

    def reply_at(
            self, 
            prompt: str, 
            engine_name="modern", 
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
        # Convertire parametru 'temperature', pentru a fi compatibil cu logica engine-urilor
        # helper: sampling function that preserves deterministic behaviour when temperature==0
        import math
        import random

        def _choose_by_temperature(candidates, temp):
            # candidates: list of (score, response_obj)
            if not candidates:
                return None
            # deterministic if temp is None or 0.0
            try:
                t = float(temp)
            except Exception:
                t = 0.0
            if t <= 0.0:
                # choose max score (stable behaviour)
                best = max(candidates, key=lambda x: x[0])
                return best[1]

            # convert scores into probabilities via softmax(score / temp)
            scores = [c[0] for c in candidates]
            # numerical stability: subtract max
            max_score = max(scores)
            exps = [math.exp((s - max_score) / t) for s in scores]
            ssum = sum(exps)
            if ssum <= 0:
                return candidates[0][1]
            probs = [e / ssum for e in exps]
            idx = random.choices(range(len(candidates)), weights=probs, k=1)[0]
            return candidates[idx][1]

        def _thinking(message: str):
            if not show_thinking:
                return
            msg = str(message)
            if allow_long_text_thinking:
                print(f"[THINKING] {msg}")
            else:
                short = msg.splitlines()[0] if msg else ""
                if len(short) > 180:
                    short = short[:177] + "..."
                print(f"[THINKING] {short}")

        def _debug(category: str, message: str):
            if not show_debug:
                return
            print(f"[DEBUG] {category}: {message}")

        def _stop_thinking():
            if show_thinking:
                print("[STOP THINKING]")
                print("---")

        if show_debug and show_thinking:
            from .errors import SameNotAllowedError
            raise SameNotAllowedError("The parameters 'show_debug' and 'show_thinking' should not have the value 'True' at the same time. Please set one of the parameters mentioned to the value 'False' and try again.")
        if show_thinking == True:
            print("---\n")
            print("[START THINKING] \n\n")
        
        if show_debug == True:
            print("---\n")
            print("[START DEBUG] \n\n")

        if engine_name.lower() in ("stable"):
            
            if with_memory == True:
                # 1. Transformăm întrebarea utilizatorului în ID-uri (tokens)
                words = str(prompt).lower().split()
                _thinking(f"I hear the prompt, so I am reading it and splitting it into words: {words}")
                _thinking("I will now match these words with my known vocabulary.")

                # Dacă prompt-ul este complet gol, se merge pe ramura asta
                if not words:
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Te ascult..."
                        except Exception:
                            pass
                        _stop_thinking()
                        return "Te ascult..."
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "I am listening to you..."
                        except Exception:
                            pass
                        _stop_thinking()
                        return "I am listening to you..."
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Te estoy escuchando..."
                        except Exception:
                            pass
                        _stop_thinking()
                        return "Te estoy escuchando..."
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral") and fallback_empty_string_message:
                            try:
                                self.last_user_prompt = str(prompt)
                                self.last_bot_output = fallback_empty_string_message
                            except Exception:
                                pass
                            _stop_thinking()
                            return fallback_empty_string_message


                # Obținem ID-urile pentru cuvintele cunoscute
                input_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]
                _thinking(f"I found these known words in my vocabulary: {input_ids}")
                _thinking("Next, I will score each training example based on the overlap with input words.")
                _debug("prompt words", str(words))
                _debug("known ids", str(input_ids))
                if words:
                    understanding_rate = (len(input_ids)/len(words))*100.0
                    _debug("understanding rate", f"{understanding_rate:.2f}%")
                else:
                    _debug("understanding rate", "0.00%")
    
                if not input_ids:
                    if not words:
                        if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                            try:
                                self.last_user_prompt = str(prompt)
                                self.last_bot_output = "Interesant, poți să-mi zici mai multe?"
                            except Exception:
                                pass
                            _stop_thinking()
                            return "Interesant, poți să-mi zici mai multe?"
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Interesting, can you tell me more?"
                        except Exception:
                            pass
                        _stop_thinking()
                        return "Interesting, can you tell me more?"
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = "Interesante, ¿puedes contarme más?"
                        except Exception:
                            pass
                        _stop_thinking()
                        return "Interesante, ¿puedes contarme más?"
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_no_understanded_message:
                            try:
                                self.last_user_prompt = str(prompt)
                                self.last_bot_output = fallback_no_understanded_message
                            except Exception:
                                pass
                            _stop_thinking()
                            return fallback_no_understanded_message

                best_score = -1
                best_response = []
                # collect candidates for optional temperature sampling
                candidates = []

                # Pregătim seturi pentru ultima conversație
                last_user_words = set(str(self.last_user_prompt).lower().split()) if getattr(self, 'last_user_prompt', None) else set()
                last_bot_words = set(str(self.last_bot_output).lower().split()) if getattr(self, 'last_bot_output', None) else set()

                # 2. Căutăm în exemplele de antrenament cea mai bună potrivire
                # translated_input_and_output_examples este lista de dict-uri
                _thinking("I am now checking every training example to compute overlap scores.")
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

                    if accept_example and combined_score > 0:
                        resp_obj = train_out_ids if train_out_ids else list(ex.get('output_words', []))
                        candidates.append((combined_score, resp_obj))
                        if combined_score > best_score:
                            best_score = combined_score
                            best_response = resp_obj

                # 3. Traducem ID-urile răspunsului înapoi în cuvinte
                if best_score > 0 and candidates:
                    _thinking(f"I have {len(candidates)} candidate responses; selecting best with score {best_score}.")
                    chosen = _choose_by_temperature(candidates, temperature)
                    _thinking(f"Response token ids selected: {chosen}")
                    id_to_word = self.id_to_word
                    if all(isinstance(i, int) for i in chosen):
                        response_words = [id_to_word.get(i, "") for i in chosen]
                        response = " ".join(response_words).strip()
                    else:
                        response = " ".join([str(w) for w in chosen]).strip()

                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = response
                    except Exception:
                        pass

                    _debug("candidate_count", str(len(candidates)))
                    _debug("best score", str(best_score))
                    _debug("final response", response)
                    
                    if show_debug == True:
                        print("[STOP DEBUG] \n\n")
                        print("---\n")

                    _stop_thinking()

                    return response

                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = "Nu sunt sigur că am înțeles, dar sună interesant!"
                    except Exception:
                        pass
                    _stop_thinking()
                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
            
                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = "I'm not sure if I understand, but it sounds interesting!"
                    except Exception:
                        pass
                    _stop_thinking()
                    return "I'm not sure if I understand, but it sounds interesting!"
                
                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                    try:
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                    except Exception:
                        pass
                    _stop_thinking()
                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                
                else:
                    if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_not_sure_message:
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = fallback_not_sure_message
                        except Exception:
                            pass
                        _stop_thinking()
                        return fallback_not_sure_message
            
            elif with_memory == False:

                # 1. Transformăm întrebarea utilizatorului în ID-uri (tokens)
                words = str(prompt).lower().split()
                _thinking(f"I read the prompt and split it into words: {words}")
                _debug("prompt words", str(words))
                _thinking("No memory mode: I will ignore past dialog and only use direct input.")

                # Dacă prompt-ul este complet gol, se merge pe ramura asta
                if not words:
                    if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                        _stop_thinking()
                        return "Te ascult..."
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        _stop_thinking()
                        return "I am listening to you..."
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        _stop_thinking()
                        return "Te estoy escuchando..."
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral") and fallback_empty_string_message:
                            _stop_thinking()
                            return fallback_empty_string_message


                # Obținem ID-urile pentru cuvintele cunoscute
                input_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]
                _thinking(f"I matched known words to IDs: {input_ids}")
                _thinking("Now I will compute matching scores for existing training examples.")
                _debug("known ids", str(input_ids))
                if words:
                    understanding_rate = (len(input_ids)/len(words))*100.0
                    _debug("understanding rate", f"{understanding_rate:.2f}%")
                else:
                    _debug("understanding rate", "0.00%")
    
                if not input_ids:
                    if not words:
                        if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                            _stop_thinking()
                            return "Interesant, poți să-mi zici mai multe?"
                
                    elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                        _stop_thinking()
                        return "Interesting, can you tell me more?"
                
                    elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                        _stop_thinking()
                        return "Interesante, ¿puedes contarme más?"
                
                    else:
                        if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_no_understanded_message:
                            _stop_thinking()
                            return fallback_no_understanded_message

                best_score = -1
                best_response = []
                candidates = []

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
                        if current_score > 0:
                            candidates.append((current_score, train_out_ids))
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
                if best_score > 0 and candidates:
                    chosen = _choose_by_temperature(candidates, temperature)
                    id_to_word = self.id_to_word
                    response_words = [id_to_word.get(i, "") for i in chosen]
                    _debug("best score", str(best_score))
                    _debug("response token ids", str(chosen))
                    
                    if show_debug == True:
                        print("[STOP DEBUG] \n\n")
                        print("---\n")

                    _stop_thinking()

                    return " ".join(response_words).strip()

                if fallback_language.lower() in ("romanian", "romana", "română", "rom"):
                    _stop_thinking()
                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
            
                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                    _stop_thinking()
                    return "I'm not sure if I understand, but it sounds interesting!"
                
                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                    _stop_thinking()
                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                
                else:
                    if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_not_sure_message:
                        _stop_thinking()
                        return fallback_not_sure_message


        elif engine_name.lower() == "chaos":

            if with_memory == True:
                # Similar cu ramura fără memorie, dar influențată ușor de ultima conversație
                words = str(prompt).split()
                _thinking(f"I read the prompt words: {words}")
                _debug("prompt words", str(words))
                _thinking("With memory on: I will also incorporate the last turn into the suggestion process.")
                if not words:
                    _stop_thinking()
                    return ""

                known_word_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]
                _thinking(f"I map known words to IDs: {known_word_ids}")
                _debug("known ids", str(known_word_ids))
                if words:
                    _debug("understanding rate", f"{(len(known_word_ids)/len(words))*100:.2f}%")
                else:
                    _debug("understanding rate", "0.00%")

                # Colectăm sugestii din mapping-ul id -> output_ids (performant: nu parcurgem toate exemplele)
                suggestions = []
                mapping = getattr(self, 'input_word_id_to_output_ids', {})
                for wid in known_word_ids:
                    if wid is None:
                        continue
                    suggestions.extend(mapping.get(wid, []))

                # Încorporăm memoria ultimei conversații, dar cu greutate mai mică (nu afectăm mult performanța)
                last_user = getattr(self, 'last_user_prompt', '') or ''
                last_bot = getattr(self, 'last_bot_output', '') or ''
                last_user_ids = [self.total_vocabulary.get(w) for w in str(last_user).split() if w in self.total_vocabulary]
                last_bot_ids = [self.total_vocabulary.get(w) for w in str(last_bot).split() if w in self.total_vocabulary]

                # Dăm o mică greutate sugestiilor venite din ultima conversație
                for wid in last_user_ids:
                    if wid is None:
                        continue
                    suggestions.extend(mapping.get(wid, []) * 2)

                for wid in last_bot_ids:
                    if wid is None:
                        continue
                    suggestions.extend(mapping.get(wid, []))

                id_to_word = getattr(self, 'id_to_word', {v: k for k, v in self.total_vocabulary.items()})
                if not suggestions:
                    _debug("suggestions", "none")
                    if show_debug == True:
                        print("[STOP DEBUG] \n\n")
                        print("---\n")
                    _stop_thinking()
                    if getattr(self, 'tokens', None):
                        resp = " ".join([id_to_word.get(t, "") for t in self.tokens[:1]]).strip()
                        try:
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = resp
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
                _debug("response text", response)
                _debug("most common ids", str(most_common_ids))
                if show_debug == True:
                    print("[STOP DEBUG] \n\n")
                    print("---\n")
                _stop_thinking()
                try:
                    self.last_user_prompt = str(prompt)
                    self.last_bot_output = response
                except Exception:
                    pass

                return response

            elif with_memory == False:
                # Ignorăm complet ultima conversație: salvăm și curățăm temporar atributele
                orig_last_user = getattr(self, 'last_user_prompt', None)
                orig_last_bot = getattr(self, 'last_bot_output', None)
                try:
                    try:
                        self.last_user_prompt = ""
                        self.last_bot_output = ""
                    except Exception:
                        pass

                    # Transformăm prompt-ul în cuvinte și obținem id-urile cunoscute
                    words = str(prompt).split()
                    _thinking(f"I read the prompt words: {words}")
                    _debug("prompt words", str(words))
                    _thinking("No memory mode: I ignore previous turns and score based only on this prompt.")
                    if not words:
                        _stop_thinking()
                        return ""

                    known_word_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]
                    _thinking(f"I map known words to IDs: {known_word_ids}")
                    _debug("known ids", str(known_word_ids))
                    if words:
                        _debug("understanding rate", f"{(len(known_word_ids)/len(words))*100:.2f}%")
                    else:
                        _debug("understanding rate", "0.00%")

                    # Numărăm, aproximativ, numărul de cuvinte (pentru a decide lungimea răspunsului)
                    prompt_list_type = list(prompt)
                    words_total_number = 1
                    for word in prompt_list_type:
                        if word == " ":
                            words_total_number += 1

                    # În primul rând, verificăm dacă există un exemplu de training cu input-ul
                    # EXACT egal cu prompt-ul (comparare case-insensitive). Dacă da și exemplul
                    # nu este condiționat de ultima conversație, returnăm output-ul original.
                    for sample in getattr(self, 'training_dataset', []):
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
                                    _stop_thinking()
                                    return "Nu sunt sigur că am înțeles, dar sună interesant!"
                                elif fallback_language.lower() in ("english", "engleza", "engleză", "eng"):
                                    _stop_thinking()
                                    return "I'm not sure if I understand, but it sounds interesting!"
                                elif fallback_language.lower() in ("spanish", "spaniola", "spaniolă", "spa"):
                                    _stop_thinking()
                                    return "No estoy seguro si lo entiendo, pero ¡suena interesante!"
                                else:
                                    if fallback_language.lower() in ("", "none", "null", "neutral", "false") and fallback_not_sure_message:
                                        _stop_thinking()
                                        return fallback_not_sure_message
                                    _stop_thinking()
                                    return ""
                            else:
                                try:
                                    _stop_thinking()
                                    return sample_out
                                except Exception:
                                    _stop_thinking()
                                    return sample_out

                    # Colectăm sugestii de id-uri din exemplele de antrenament, dar IGNORĂM
                    # exemplele condiționate de ultima conversație (if_last_*) pentru a nu folosi memorie
                    suggestions = []
                    examples = getattr(self, 'translated_input_and_output_examples', [])
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
                    id_to_word = getattr(self, 'id_to_word', {v: k for k, v in self.total_vocabulary.items()})
                    if not suggestions:
                        if show_debug == True:
                            print("[STOP DEBUG] \n\n")
                            print("---\n")
                        _stop_thinking()
                        if getattr(self, 'tokens', None):
                            return " ".join([id_to_word.get(t, "") for t in self.tokens[:1]]).strip()
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
                        _debug("response text", response)
                        _debug("most common ids", str(most_common_ids))
                        _stop_thinking()
                        return response
                finally:
                    # Restaurăm contextul original
                    try:
                        self.last_user_prompt = orig_last_user
                        self.last_bot_output = orig_last_bot
                    except Exception:
                        pass

        elif engine_name == "modern":
            
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
                    dataset = getattr(self, "translated_input_and_output_examples", [])
                    
                    # Căutăm primul exemplu care are măcar un cuvânt comun
                    for ex in dataset:
                        if prompt_set & ex.get('input_words', set()):
                            out_ids = ex.get('output_ids', [])
                            # Reconstruim răspunsul din ID-uri
                            id_to_word = getattr(self, "id_to_word", {})
                            # Dacă nu avem id_to_word, încercăm să inversăm total_vocabulary
                            if not id_to_word:
                                vocab = getattr(self, "total_vocabulary", {})
                                id_to_word = {v: k for k, v in vocab.items()}
                            
                            out_str = " ".join([id_to_word.get(i, str(i)) for i in out_ids])
                            
                            self.last_user_prompt = str(prompt)
                            self.last_bot_output = out_str
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
                        self.last_user_prompt = str(prompt)
                        self.last_bot_output = "Te ascult..."
                    except Exception:
                        pass
                    return getattr(self, "last_bot_output", "Te ascult...")
                return fallback_empty_string_message or ""

            total_vocab = getattr(self, "total_vocabulary", {}) or {}

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
            if with_memory == True and getattr(self, "last_user_prompt", None):
                if show_thinking == True:
                    print(f"But hey, I was also asked to access and consider my last conversation with the user, but what was that? Let me check...")
                    print(f"This is what I remember as the last conversation:\n     my last message: '{self.last_bot_output}'\n     user's last message: '{self.last_user_prompt}'\n")
                    print("Let's start tokenizing the user's last prompt...")

                last_words = [w for w in str(self.last_user_prompt).lower().split()]
                
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
                
                self.last_user_prompt = str(prompt)
                self.last_bot_output = fallback_no_understanded_message or ""
                return self.last_bot_output

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
            dataset_list = getattr(self, "translated_input_and_output_examples", [])

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
            last_user_words_list = [w for w in str(getattr(self, 'last_user_prompt', '')).lower().split()] if with_memory else []
            last_bot_words_list = [w for w in str(getattr(self, 'last_bot_output', '')).lower().split()] if with_memory else []
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
                    chosen_idx = _choose_by_temperature(candidates, temperature)
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
                    
                    self.last_user_prompt = str(prompt)
                    self.last_bot_output = resp
                    return resp

                # 7) Extragem output-ul asociat exemplului ales
                chosen_output_ids = outputs[best_idx] if best_idx < len(outputs) else []
                
                # Reconstruim string din id-uri
                id_to_word = getattr(self, "id_to_word", None)
                if id_to_word:
                    out_tokens = [id_to_word.get(i, str(i)) for i in chosen_output_ids]
                else:
                    inv = {v: k for k, v in total_vocab.items()}
                    out_tokens = [inv.get(i, str(i)) for i in chosen_output_ids]

                response = " ".join(out_tokens).strip()

                # Salvăm "memoria" locală
                self.last_user_prompt = str(prompt) if with_memory == True else None
                self.last_bot_output = response if with_memory == True else None

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
                id_to_word = getattr(self, "id_to_word", {v: k for k, v in total_vocab.items()})
                response = " ".join(id_to_word.get(i, str(i)) for i in chosen_output_ids).strip()
                
                self.last_user_prompt = str(prompt) if with_memory == True else None
                self.last_bot_output = response if with_memory == True else None
                return response

            except Exception:
                # Fallback final
                return ""

    def reply_with_audio(self, prompt, engine_name="modern", sensitivity: int = 1, with_memory: bool = True, fallback_language="english", fallback_empty_string_message="", fallback_no_understanded_message="", fallback_not_sure_message="", temperature: float = 0.0, show_thinking=False, allow_long_text_thinking=True, show_debug=False,
                         audio_engine="gTTS", audio_language='en', elevenlabs_voice_id="21m00Tcm4TlvDq8ikWAM", elevenlabs_api_key="", elevenlabs_model_id="eleven_multilingual_v2"):
        from pyrospeak import speak

        # Text generat de chatbot, salvat într-o variabilă
        text = self.reply_at(
            prompt=prompt,
            engine_name=engine_name,
            sensitivity=sensitivity,
            with_memory=with_memory,
            temperature=temperature,
            fallback_language=fallback_language,
            fallback_empty_string_message=fallback_empty_string_message,
            fallback_no_understanded_message=fallback_no_understanded_message,
            fallback_not_sure_message=fallback_not_sure_message,
            show_thinking=show_thinking,
            allow_long_text_thinking=allow_long_text_thinking,
            show_debug=show_debug,
        )

        speak(
            text_to_procces=text,
            engine=audio_engine,
            language=audio_language,
            elevenlabs_api_key=elevenlabs_api_key,
            elevenlabs_model_id=elevenlabs_model_id,
            elevenlabs_voice_id=elevenlabs_voice_id
        )

        return text