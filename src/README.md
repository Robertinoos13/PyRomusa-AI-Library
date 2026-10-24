# `PyRomusa AI` — v0.11.0 🤖

- **Version type:** STABLE
- **Release date:** 2026-10-24

---

## Overview

This version/framework focuses on creating a **very simple, beginner-friendly chatbot system**, built with:
- custom logic _(`Chatbot()` object)_ 
- real machine learning models _(`RealChatbot()` object)_

It exists to:
- help beginners understand how chatbot logic can work
- allow fast experimentation with simple AI-like behaviour
- avoid complex frameworks and heavy dependencies (`Chatbot()` object)

What makes it different:
- you can avoid neural networks, hidden layers, ML libraries (`Chatbot()` object)
- you can using LLM tehnologies (`RealChatbot()` object)
- fully custom, readable logic

> This version implements two types of chatbot objects: 
> - `Chatbot()` _(optimized for few training examples and hardware-undemanding)_
> - `RealChatbot()` _(optimized for large, serious projects, real experimentation and hardware-demanding)_

---

## Files Included

### General structure (exactly this structure will be found if you search in `📁all versions` of this repository):
```
|-📁PyRomusa_AI - vX.Y.Z/
|----📄README.md
|
|----📁PyRomusa_AI/
|-------- 🐍PyRomusa_AI.py
|-------- 🐍errors.py
|
|-------- 📁Datasets/
|------------ more Python files...
|
|-------- 📁Reply_Engines/
|------------ more Python files...
```

<br>

### More exact structure (if you search in the `📁src` folder):
```
|- 📁src/
|--- ⚙️pyproject.toml
|--- 📄README.md
├─── 📁pyromusa_ai/
    |--- 🐍core.py
    |--- 🐍__init__.py
    |--- 🐍errors.py
    ├─── 📁Datasets
    └─── 📁Reply_Engines
```



### Where:
|File/Folder name|Description|
|:-:|:--|
|`📁PyRomusa_AI - vX.Y.Z` , `📁src/`|The main folder containing everything for that version of the framework (full framework code + `📄README.md`)|
|`📄README.md`|Documentation for this specific version |
|`📁PyRomusa_AI/` , `📁pyromusa_ai/`|The secondary folder, which only has all the code that contributes to the 100% functional `PyRomusa AI`|
|`🐍PyRomusa_AI.py` , `🐍core.py`|The main/core code of `PyRomusa AI`|
|`📁Datasets/`|Folder with some optional code for the main framework code (`🐍PyRomusa_AI.py`) for ready-made data to train your chatbot|
|`⚙️pyproject.toml`|A very important file to be able to install with pip install, but completely useless if you install `PyRomusa AI` manually|
|`🐍errors.py`|A new file from 0.6.0, here you find different types of errors that you can catch in `PyRomusa AI`|
|`📁Reply_Engines/`|The folder containing the most important lines of code for the main goal of `PyRomusa AI`. These lines of code are mandatory for generating responses based on a prompt.|



---

## What's New

- **Docstrings for all available functions:** Now, to find out in an instant what a specific function does and what role each of its parameters plays, you simply need to hover your cursor over that function; you will then see a description of the function along with all the available parameters. _(works on VSCode)_

- **_|`RealChatbot()` object|_ Raw text as training example:** Do you want your chatbot to learn how the language you’re training it on works, or perhaps you simply lack question-answer pairs? Well, you can now use the `bot.trainer.start()` function: set the `example_type` parameter to `"raw"` and provide your raw text in the `training_input_example` parameter—it’s as simple as that.

- **_|`RealChatbot()` object|_ Timer on training loop:** Find out how many seconds your training session lasted by setting the `show_total_time_of_training_when_ends` parameter to `True`. The result will appear when the training session ends.

- **_|`RealChatbot()` object|_ Censored words system:** This system has actually been in place within `Chatbot()` for some time now. If you aren't yet familiar with it, its purpose is to replace certain words with others, thereby helping to reduce the use of vulgar language in the responses.

- **_|`RealChatbot()` object|_ New parameters added (`weight_decay` & `optimizer_type`) in `bot.trainer.start()` function:** For greater flexibility, you can now change the optimizer type _(currently AdamW or Adam)_ for training. The `weight_decay` parameter serves the exact same purpose as it does in PyTorch optimizers.

- **_|`RealChatbot()` object|_ Specified value type for all parameters available on `bot.trainer.start()` function:** Each parameter here should accept only one type of value _(integer, string, float, or boolean)_. To prevent future errors and avoid running code unnecessarily, you can now receive an error before the code executes, allowing you to correct the mistake immediately.

- **_|`RealChatbot()` object|_ New tokenizer type option, `"semiwords-level"`:** Are you looking for something between a word and a character—a balance between the quality of the responses and the flexibility of generation? Well, this tokenizer groups about 2–3 letters _(on average)_ into a single token.

- **_|`RealChatbot()` object|_ A optional feedback system (with y/n) while you are talking to the chatbot:** This system is recommended if you call the `bot.reply_at()` function multiple times during a single execution. It serves to refine the chatbot's final responses based on user preferences by calculating the similarity between the most recently generated response and a list of previously rejected responses. If the similarity exceeds the value defined by the `max_allowed_similarity_procent_with_banned_replies` parameter _(a float representing a percentage)_, the system will attempt to regenerate the response until one with a lower similarity score is produced, subject to a specified maximum number of attempts.

- **_|`RealChatbot()` object|_ Clear separation between special tokens and normal tokens:** In case you didn't know, special tokens form an important part of the training text structure, while normal tokens are those entered by the user to help the chatbot converse more naturally. Well, chatbots can now generate special tokens directly and fully; this positively influences the quality of the generated response, making it less likely that the chatbot will say things unrelated to the prompt _(though this also depends on the training examples)_.

- **_|`RealChatbot()` object|_ Removing unnecessary comments from the code:** To keep the source code cleaner, I have removed many unnecessary comments. This does not, in any way, affect the practical use of the framework.

- **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.

---

✅ **STABLE release notice:**

- The API is considered stable and ready for regular use
- Core logic is implemented and tested
- Behaviour is consistent across typical use cases
- Minor bugs may still exist, but no breaking changes are expected

## Quick Usage Examples

### 1. Creating your first functional chatbot ever
```python
from pyromusa_ai import Chatbot

# Create a chatbot
bot = Chatbot(chatbot_name="RomusaBot")

# Add training data
bot.trainer.add_data("Hello!", "Hi there!")
bot.trainer.add_data("Bye!", "Goodbye!")

# Start training
bot.trainer.start()

# Get a response
print(bot.reply_at("Hello!"))
```
---

### 2. Learn to start using the framework

```python
from pyromusa_ai import Chatbot

# Create a chatbot
bot = Chatbot()

# Get help
bot.helper.how_to_start()
```

---
## Note:

Depending on how you installed `PyRomusa AI`, this framework, in your code, must be imported like this, one of these 2 variants:

### a) If you installed with `pip install ...`:
```python
from pyromusa_ai import Chatbot
```

### b) If you installed manually from this repository, preserving file names, from `📁all versions` folder:
```python
from PyRomusa_AI import Chatbot # If your code is located in the same folder as 🐍PyRomusa_AI.py
```

or
```python
from PyRomusa_AI.PyRomusa_AI import Chatbot # If your code is in the same folder as the folder that has all the resources for PyRomusa AI (📁PyRomusa_AI)
```
