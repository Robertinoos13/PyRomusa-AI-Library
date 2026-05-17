# `PyRomusa AI` — v0.7.0 🤖

- **Version type:** STABLE
- **Release date:** 2026-05-11

---

## Overview

This version/framework focuses on creating a **very simple, beginner-friendly chatbot system**, built with custom logic instead of real machine learning models.

It exists to:
- help beginners understand how chatbot logic can work
- allow fast experimentation with simple AI-like behaviour
- avoid complex frameworks and heavy dependencies

What makes it different:
- no neural networks
- no hidden layers
- no external ML libraries
- fully custom, readable logic

> This version implements a basic chatbot that learns from full words and example-based responses.  
> No hidden layers or machine learning models are used in this implementation.

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

### More exact structure (if you search in the `📁pyromusa-ai` folder):
```
|-📁pyromusa-ai/
|----📄README.md
|----⚙️pyproject.toml
|
|----📁pyromusa_ai/
|-------- 🐍core.py
|-------- 🐍errors.py
|-------- 🐍__init__.py
|
|-------- 📁Datasets/
|------------ more Python files...
|
|-------- 📁Reply_Engines/
|------------ more Python files...
```



### Where:
|File/Folder name|Description|
|:-:|:--|
|`📁PyRomusa_AI - vX.Y.Z` , `📁pyromusa-ai/`|The main folder containing everything for that version of the framework (full framework code + `📄README.md`)|
|`📄README.md`|Documentation for this specific version |
|`📁PyRomusa_AI/` , `📁pyromusa_ai/`|The secondary folder, which only has all the code that contributes to the 100% functional `PyRomusa AI`|
|`🐍PyRomusa_AI.py` , `🐍core.py`|The main/core code of `PyRomusa AI`|
|`📁Datasets/`|Folder with some optional code for the main framework code (`🐍PyRomusa_AI.py`) for ready-made data to train your chatbot|
|`⚙️pyproject.toml`|A very important file to be able to install with pip install, but completely useless if you install `PyRomusa AI` manually|
|`🐍errors.py`|A new file from 0.6.0, here you find different types of errors that you can catch in `PyRomusa AI`|
|`📁Reply_Engines/`|The folder containing the most important lines of code for the main goal of `PyRomusa AI`. These lines of code are mandatory for generating responses based on a prompt.|



---

## What's New

- **Saving and loading your chatbot based on `json` files:** Now it is possible to transform your chatbot into a simple `json` file on demand. Now you will not need to rewrite all your Python code with training examples, because now you have chatbots saved in `json` files.

- **Update to the Romanian language dataset, 'Teacher for PyRomusa AI':** It has been added more training examples to be able to answer more prompts. It is now a better dataset than in the previous version.

- **New Reply Engine, `optimized`:** Now with this Reply Engine, you have an extra option if the others don't meet your goal very well. This new Reply Engine is focused on processing speed, minimal creativity compared to what is seen in the training examples, and good quality.

- **New code structure, more clear code:** The code sequences that represented a Reply Engine are no longer found in the core of the framework, but in a folder called `📁Reply_Engines`. Now the core and code of Reply Engines is more organized.

- **More functions in `bot.helper.describe_functions()`:** If you don't know yet, this function returns the most important functions of the framework and their description in a table. Now you find 2 more functions than the previous version.

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

### a) If you installed with `pip install git+https://github.com/Robertinoos13/PyRomusa-AI-Library.`:
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

>
