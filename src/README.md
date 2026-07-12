# `PyRomusa AI` — v0.9.0 🤖

- **Version type:** STABLE
- **Release date:** 2026-07-05

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

- **The new object, `RealChatbot()`:** Do you want to train a real, yet untrained LLM architecture on your own Q&A examples? Then this is the perfect chatbot type for you.

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
