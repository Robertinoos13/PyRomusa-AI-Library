# `PyRomusa AI` — v0.6.0 🤖

- **Version type:** STABLE
- **Release date:** 2026-04-07

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
|
|-------- 📁Datasets/
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
|`🐍errors.py`|A new file from 0.6.0, here you find different types of errors that you can catch in PyRomusa AI|



---

## What's New

- **New parameters on `bot.reply_at()` and `bot.reply_with_audio()`; `show_debug`, `show_thinking` and `allow_long_text_thinking`:** With these parameters set to True (`show_debug` or `show_thinking`), you can discover why your chatbot generates a certain response. Be ready to optimize your training examples and select the perfect reply engine for your needs in an easier way!

- **The 'modern' reply engine, set as default value:** Now, as the `modern` engine is the most balanced reply engine of all in the latest version, it has replaced the `'stable'` engine as the default value in the `bot.reply_at()` and `bot.reply_with_audio()` functions, in the `engine_name` parameter

- **Specific errors of `PyRomusa AI`:** Now, `PyRomusa AI` specific errors have started to be added. The first of them is `SameNotAllowedError`, which rejects 2 parameters having the same value that are not allowed to be the same value.

- **Improved Romanian language prepared dataset, Teacher for PyRomusa AI:** Added more input-output training examples for more vocabulary and responding to more prompts without returning a fallback message

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
