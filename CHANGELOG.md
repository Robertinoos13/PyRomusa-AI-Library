# CHANGELOG 🕑

Here you will find all updates maked at PyRomusa AI of all time (STABLE & BETA versions)

---

## UPDATE TYPES

|emoji|description|
|:-:|:-:|
|🦠|bug fixed|
|🔧|API/sintax modified|
|➕|new functionality|
|✨|impoved a existing functionality|
|📁|modified files structure|
|❓|other type of update|

---

## UPDATE HYSTORY

### `v0.0.1 BETA` (2026/01/11)

- ❓ the initial BETA version 

---

### `v0.0.2 BETA` (2026/01/17)

- ✨ 2 functions in the Help class were completed, without replacing their real context with 'pass' 

- 🔧 **FUNCTION NAME CHANGED:** 
`bot.responding_at()` -> `bot.reply_at()` 

---


### `v0.1.0 STABLE` (2026/01/18)

- ❓ the initial STABLE version 

---


### `v0.1.1 STABLE` (2026/01/24)

- ➕ New prepared dataset, ready to use: _**High Quality, Very Low Quantity Romanian Dataset**_ 

---


### `v0.2.0 STABLE` (2026/02/04)

- ➕ NEW CONCEPT: **Reply Engines** 

- 🦠 A minor bug fixed 

- ➕ New 2 prepared datasets: **Teacher for PyRomusa AI & High Quality, Low Quantity Romanian Dataset** 

- 📁 New `PyRomusa AI` folder structure: The main code has been separated from the prepared datasets

- ➕ Fallback messages personalization 

---

### `v0.3.0 STABLE` (2026/02/14)

- ➕ **New chatbot ability:** Now chatbots can generate responses, influenced by the last conversation with the user. 

- ✨ **Upgrade at 'Teacher for PyRomusa AI' prepared dataset:**  Now, chatbots that have this dataset prepared are able to respond to more prompts than in the latest STABLE version (0.2.0) 

---

### `v0.4.0 STABLE` (2026/02/19)

- ➕ New Reply Engine: `modern` 

- ✨ Upgrade at `Teacher for PyRomusa AI` prepared dataset 

---

### `v0.4.1 STABLE` (2026/02/20)

- ➕ The first datasets prepared in English: _Default English Dataset: LOW-END, MID-RANGE, HIGH-END_ 

---

### `v0.4.2 STABLE` (2026/02/23)

- 🦠 **Bug fixed in the reply engine _`modern`_**: Now, if you select the `modern` engine, it works perfectly if you choose for the chatbot to ignore the last conversation with the user using the `with_memory` parameter in the `bot.reply_at()` function. 

- ✨ Improved Romanian language prepared dataset, `Teacher for PyRomusa AI` 

---

### `v0.4.3 STABLE` (2026/03/05)

- ➕ **New parameter in `bot.reply_at()`, `temperature`**: Now chatbots can generate different messages at the same prompt using this new parameter (this influences the 'creativity' of the chatbot).

- ✨ Improved Romanian language prepared dataset, `Teacher for PyRomusa AI` 

---

### `v0.5.0 STABLE` (2026/03/15)

- ➕ **Talking chatbots**: Using the `bot.reply_with_audio()` function, chatbots can now speak the generated response out loud, using the PyroSpeak library (based on specialized TTS frameworks, such as gTTS and pyttsx3).

- ✨ Improved Romanian language prepared dataset, `Teacher for PyRomusa AI` 

---

### `v0.6.0 STABLE` (2026/04/07)

- ➕ New parameters on `bot.reply_at()` and `bot.reply_with_audio()`; `show_debug`, `show_thinking` and `allow_long_text_thinking`

- 🔧 The `modern` reply engine, set as default value

- ➕ **Specific errors of `PyRomusa AI`:** Now, `PyRomusa AI` specific errors have started to be added. The first of them is `SameNotAllowedError`, which rejects 2 parameters having the same value that are not allowed to be the same value.

- ✨ Improved Romanian language prepared dataset, `Teacher for PyRomusa AI`

---

### `v0.6.1 STABLE` (2026/04/10)

- 🦠 **Bux fixed on 'modern' reply engine** - In training examples that involved inputs and parameters like `if_last_...`, whatever they were, only those were chosen by the chatbot as the final answer at a given time. Now chatbots with this reply engine will respond more logically and correctly based on the current prompt.

- ➕ **New function, `show_basic_specs()`** - It is now possible to see the number of the chatbot's current vocabulary (total tokens) and the number of training examples entered into the training dataset using just one function.

- ➕ **New parameter in functions like `trainer.show_translated_examples()`, `trainer.show_number_of_examples()`** - Now you have the `with_print` parameter, which is set to `True` by default. This parameter, when set to `True`, no longer requires you to manually write the `print()` function to display a number.

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version

---

### `v0.6.2 STABLE` (2026/04/16)

- ✨ **More questions and answers in the `bot.helper.questions()` function:** Now, by calling this function, you will be able to find the answers to more questions. _MORE QUESTIONS = MORE CHANCES OF FINDING THE ANSWER TO YOUR QUESTION_ 

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version

---

### `v0.7.0 STABLE` (2026/05/11)

- ➕ **Saving and loading your chatbot based on `json` files:** Now it is possible to transform your chatbot into a simple `json` file on demand. Now you will not need to rewrite all your Python code with training examples, because now you have chatbots saved in `json` files.

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.

- ➕ **New Reply Engine, `optimized`:** Now with this Reply Engine, you have an extra option if the others don't meet your goal very well. This new Reply Engine is focused on processing speed, minimal creativity compared to what is seen in the training examples, and good quality.

- 📁 **New code structure, more clear code:** The code sequences that represented a Reply Engine are no longer found in the core of the framework, but in a folder called `📁Reply_Engines`. Now the core and code of Reply Engines is more organized.

- ✨ **More functions in `bot.helper.describe_functions()`:** If you don't know yet, this function returns the most important functions of the framework and their description in a table. Now you find 2 more functions than the previous version.

---

### `v0.7.1 STABLE` (2026/05/17)

- ➕ **Description at your chatbot:** Now, using the `chatbot_description` parameter in the `Chatbot()` class, it is possible to describe your chatbot in your own words. This can be saved in the chatbot files (json)

- ➕ **Completely reset your chatbot:** Using the `bot.reset()` function, everything from the training examples and the last conversation with the user to the chatbot's description and name is reset.

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.

---

### `v0.8.0 STABLE` (2026/06/15)

- ➕ **New Reply Engine, `unsmarty`:** More reply engine options = more response generation options

- ➕ **Censored words system:** Now there is `censored_words` parameter in the `bot.reply_at()` function, with which you can tell your chatbot to avoid saying certain words and replace them with another word.

- ➕ **New lines system:** If you use `\n` in the training examples, the chatbot will learn that the message should be written on multiple lines (the new line starts where you put `\n`)

- ✨ **Modified returned text on `bot.helper.questions()`:** To be up to date, I have updated a statement of a text in an answer

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.

- ✨ **Bigger conversations memory:** Now a chatbot can remember the entire conversation in a session, not just the last conversation

---

### `v0.9.0 STABLE` (2026/07/05)

- ➕ **The new object, `RealChatbot()`:** Do you want to train a real, yet untrained LLM architecture on your own Q&A examples? Then this is the perfect chatbot type for you.

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.

---

### `v0.9.1 STABLE` (2026/08/11)

- ➕ **_|`RealChatbot()` object|_ New parameter on `bot.show_number_of_parameters()`, `with_print`:** Do you want a printed value directly or just the return value? Now you can modify the with_print parameter of this function, depending on your needs.

- ➕ **_|`RealChatbot()` object|_ New functions, `bot.show_current_training_text()`, `bot.trainer.create_personalized_dataset()` and `bot.reset()`:** Now you can view the chatbot's training text using a function, create your own dataset structure, or reset the chatbot's specifications to factory defaults in the same script.

- ✨ **_|`RealChatbot()` object|_ More exactly error when using `bot.trainer.start()` function:** When you run this function and it should return an error, you can clearly see if the error produced is actually due to the length of the dataset or some other unexpected error.

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.

---

### `v0.10.0 STABLE` (2026/08/22)

- 🦠 **_|`RealChatbot()` object|_ Bug fixed when loading a chatbot from a `.pt` file:** An attempt was made to solve the problem so that when loading a pretrained model from a file, it would be possible to train it on new examples and, at the same time, preserve the previous pretraining process, without returning errors.

- 🔧 **_|`RealChatbot()` object|_ Corrected parameter name `learn_late` -> `learn_rate`:** A small spelling mistake in the name of a parameter in the `bot.trainer.start()` function has been corrected.

- ➕ **_|`RealChatbot()` object|_ Added `word-level` tokenizer:** With the new word-level tokenizer, you have more possibilities to customize your chatbot the way you want. If you want faster training and the chatbot to look like it has 'hard-learned' to spell most words correctly, but more sensitivity if you misspell a word, then this tokenizer is perfect for you.

- ➕ **_|`RealChatbot()` object|_ Added auto checkpoint/ask to stop while training:** Using the `ask_to_stop_every_x_epochs` and `auto_checkpoint_every_x_epochs` parameters from the `bot.trainer.start()` function, you can stop the chatbot training during training and periodically save the chatbot process.  

- ✨ **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.
---