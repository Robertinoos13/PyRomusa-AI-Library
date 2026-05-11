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
import json
import os
from datetime import datetime


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
        self.storage = self.Storage(self)


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
                "function": ["bot.trainer.add_data()", "bot.trainer.show_dataset()", "bot.trainer.start()", "bot.trainer.show_translated_examples()", "bot.trainer.show_relationed_output_with_input_words()", "bot.trainer.show_relationed_output_with_input_ids()", "bot.reply_at()", "bot.prepared_datasets.romanian.load_prepared_dataset()", "bot.trainer.show_number_of_examples()", "bot.storage.save_on_file()", "bot.storage.load_from_file()"],
                "min number of values": [2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                "info": ["Adds examples type input/output in the dataset for the training chatbot", "Shows the current train examples for the chatbot (the dataset)", "Starts you train for chatbot, using the examples input/output finded in the dataset", "Shows you the examples in chatbot language (words -> tokens)", "Shows the words what can use the chatbot (value) if exist a any unique word (key)", "Shows the tokens what can use the chatbot (value) if exist a any unique token (key) in the input", "Generates a output using a prompt", "Loads a prepared dataset for training in romanian language", "Shows the total number of examples what exist in the current dataset of a chatbot", "Saves chatbot data in a new JSON file", "Loads chatbot data from a JSON file and rebuilds the chatbot state"]
            })
            return print(f"\n-----\n--- Here are the most important functions of this library, explained in the simplest and clearest way possible. As a beginner, it is recommended to read these descriptions to better understand what each function does. ---\n\nNOTE: Before using any of these functions, make sure you have this line in your code:\nbot = Chatbot()\n\n{tabel_functions}\n-----")

    class Storage:
        def __init__(self, parent):
            self.parent = parent

        def _normalize_dataset_for_json(self):
            normalized = []
            for sample in getattr(self.parent, "training_dataset", []):
                if isinstance(sample, dict):
                    normalized.append({
                        "input": str(sample.get("input", "")),
                        "output": str(sample.get("output", "")),
                        "if_last_input": sample.get("if_last_input"),
                        "if_last_output": sample.get("if_last_output"),
                    })
                elif isinstance(sample, (list, tuple)):
                    normalized.append({
                        "input": str(sample[0]) if len(sample) > 0 else "",
                        "output": str(sample[1]) if len(sample) > 1 else "",
                        "if_last_input": sample[2] if len(sample) > 2 else None,
                        "if_last_output": sample[3] if len(sample) > 3 else None,
                    })
                else:
                    normalized.append({
                        "input": str(sample),
                        "output": "",
                        "if_last_input": None,
                        "if_last_output": None,
                    })
            return normalized

        def _to_json_filename(self, file_name: str):
            cleaned_name = str(file_name).strip()
            if cleaned_name.lower().endswith(".json"):
                cleaned_name = cleaned_name[:-5]
            if cleaned_name == "":
                cleaned_name = "chatbot_backup"
            return cleaned_name + ".json"

        def save_on_file(self, file_name="no_name_chatbot", file_location: str = None):
            if file_name is None or str(file_name).strip() == "":
                file_name = "no_name_chatbot"

            if file_location is None or str(file_location).strip() == "":
                directory_path = os.path.abspath(os.getcwd())
            else:
                directory_path = os.path.abspath(str(file_location))
            os.makedirs(directory_path, exist_ok=True)

            base_filename = self._to_json_filename(file_name)
            base_name_only, _ = os.path.splitext(base_filename)
            final_path = os.path.join(directory_path, base_filename)

            # La fiecare save trebuie fișier nou, fără suprascriere.
            index = 1
            while os.path.exists(final_path):
                final_path = os.path.join(directory_path, f"{base_name_only}_{index}.json")
                index += 1

            payload = {
                "chatbot_name": str(getattr(self.parent, "chatbot_name", "ChatBot")),
                "created_on": datetime.now().strftime("%Y/%m/%d"),
                "training_dataset": self._normalize_dataset_for_json(),
                "last_user_prompt": str(getattr(self.parent, "last_user_prompt", "")),
                "last_bot_output": str(getattr(self.parent, "last_bot_output", "")),
            }

            with open(final_path, "w", encoding="utf-8") as json_file:
                json.dump(payload, json_file, ensure_ascii=False, indent=4)

            print(f"INFO: Chatbot saved successfully in '{final_path}'.")
            return final_path

        def load_from_file(self, file_location: str, file_name: str = None):
            if file_location is None or str(file_location).strip() == "":
                raise ValueError("Parameter 'file_location' should not be empty.")

            directory_path = os.path.abspath(str(file_location))
            if not os.path.isdir(directory_path):
                raise FileNotFoundError(f"Folder not found at '{directory_path}'.")
            if file_name is None or str(file_name).strip() == "":
                all_json_files = [
                    os.path.join(directory_path, current_file)
                    for current_file in os.listdir(directory_path)
                    if str(current_file).lower().endswith(".json")
                ]
                if not all_json_files:
                    raise FileNotFoundError(f"No JSON files found in '{directory_path}'.")
                file_path = max(all_json_files, key=os.path.getmtime)
            else:
                requested_name = self._to_json_filename(file_name)
                file_path = os.path.join(directory_path, requested_name)

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"JSON file not found at '{file_path}'.")

            with open(file_path, "r", encoding="utf-8") as json_file:
                payload = json.load(json_file)

            if not isinstance(payload, dict):
                raise ValueError("Invalid JSON format. Root should be an object.")

            raw_dataset = payload.get("training_dataset", [])
            if not isinstance(raw_dataset, list):
                raise ValueError("Invalid JSON format. 'training_dataset' should be a list.")

            normalized_dataset = []
            for sample in raw_dataset:
                if isinstance(sample, dict):
                    normalized_dataset.append({
                        "input": str(sample.get("input", "")),
                        "output": str(sample.get("output", "")),
                        "if_last_input": sample.get("if_last_input"),
                        "if_last_output": sample.get("if_last_output"),
                    })

            # Reset total starea internă, apoi reconstruim mapările necesare engine-urilor.
            self.parent.total_vocabulary = {}
            self.parent.tokens = []
            self.parent.training_dataset = normalized_dataset
            self.parent.translated_input_and_output_examples = []
            self.parent.input_word_to_output_words = {}
            self.parent.input_word_id_to_output_ids = {}
            self.parent.id_to_word = {}

            self.parent.chatbot_name = str(payload.get("chatbot_name", self.parent.chatbot_name))
            self.parent.last_user_prompt = str(payload.get("last_user_prompt", ""))
            self.parent.last_bot_output = str(payload.get("last_bot_output", ""))

            # Rebuild intern pentru a permite reply immediate pe toate engine-urile.
            self.parent.trainer.start()

            print(f"INFO: Chatbot loaded successfully from '{file_path}'.")
            return file_path


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
    
    def _choose_by_temperature(self, candidates, temp):
        """Helper method for temperature-based sampling of candidates"""
        import random
        import math
        
        if not candidates:
            return None
        try:
            t = float(temp)
        except Exception:
            t = 0.0
        if t <= 0.0:
            best = max(candidates, key=lambda x: x[0])
            return best[1]
        
        scores = [c[0] for c in candidates]
        max_score = max(scores)
        exps = [math.exp((s - max_score) / t) for s in scores]
        ssum = sum(exps)
        if ssum <= 0:
            return candidates[0][1]
        probs = [e / ssum for e in exps]
        idx = random.choices(range(len(candidates)), weights=probs, k=1)[0]
        return candidates[idx][1]
    
    def _thinking(self, message: str, show_thinking: bool, allow_long_text_thinking: bool):
        """Helper method to print thinking messages"""
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
    
    def _debug(self, category: str, message: str, show_debug: bool):
        """Helper method to print debug messages"""
        if not show_debug:
            return
        print(f"[DEBUG] {category}: {message}")
    
    def _stop_thinking(self, show_thinking: bool):
        """Helper method to end thinking output"""
        if show_thinking:
            print("[STOP THINKING]")
            print("---")

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

        def _debug(category: str, message: str, show_debug: bool):
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

        if engine_name.lower() == "stable":
            
            from .Reply_Engines import stable

            try:
                return stable.use_engine(self, 
                    prompt=prompt, 
                    sensitivity=sensitivity, 
                    with_memory=with_memory, 
                    fallback_language=fallback_language, 
                    fallback_empty_string_message=fallback_empty_string_message, 
                    fallback_no_understanded_message=fallback_no_understanded_message, 
                    fallback_not_sure_message=fallback_not_sure_message, 
                    temperature=temperature,
                    show_thinking=show_thinking,
                    allow_long_text_thinking=allow_long_text_thinking,
                    show_debug=show_debug
                )
            
            except Exception as e:
                raise("An error occurred: {e}")


        elif engine_name.lower() == "chaos":
            from .Reply_Engines import chaos

            try:
                return chaos.use_engine(self, 
                    prompt=prompt, 
                    sensitivity=sensitivity, 
                    with_memory=with_memory, 
                    fallback_language=fallback_language, 
                    fallback_empty_string_message=fallback_empty_string_message, 
                    fallback_no_understanded_message=fallback_no_understanded_message, 
                    fallback_not_sure_message=fallback_not_sure_message, 
                    temperature=temperature,
                    show_thinking=show_thinking,
                    allow_long_text_thinking=allow_long_text_thinking,
                    show_debug=show_debug
                )
            
            except Exception as e:
                raise("An error occurred: {e}")

        elif engine_name.lower() == "modern":
            from .Reply_Engines import modern

            try:
                return modern.use_engine(self, 
                    prompt=prompt, 
                    sensitivity=sensitivity, 
                    with_memory=with_memory, 
                    fallback_language=fallback_language, 
                    fallback_empty_string_message=fallback_empty_string_message, 
                    fallback_no_understanded_message=fallback_no_understanded_message, 
                    fallback_not_sure_message=fallback_not_sure_message, 
                    temperature=temperature,
                    show_thinking=show_thinking,
                    allow_long_text_thinking=allow_long_text_thinking,
                    show_debug=show_debug
                )
            
            except Exception as e:
                raise("An error occurred: {e}")

        elif engine_name.lower() == "optimized":
            from .Reply_Engines import optimized

            try:
                return optimized.use_engine(self, 
                    prompt=prompt, 
                    sensitivity=sensitivity, 
                    with_memory=with_memory, 
                    fallback_language=fallback_language, 
                    fallback_empty_string_message=fallback_empty_string_message, 
                    fallback_no_understanded_message=fallback_no_understanded_message, 
                    fallback_not_sure_message=fallback_not_sure_message, 
                    temperature=temperature,
                    show_thinking=show_thinking,
                    allow_long_text_thinking=allow_long_text_thinking,
                    show_debug=show_debug
                )
            
            except Exception as e:
                raise("An error occurred: {e}")


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
