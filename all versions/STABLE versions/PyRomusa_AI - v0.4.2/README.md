# `PyRomusa AI` — v0.4.2 🤖

- **Version type:** STABLE
- **Release date:** 2026-02-23

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

`📁PyRomusa_AI - vX.Y.Z/` — The main folder containing everything for that version of the framework (full framework code + README.md)

 - `📄README.md` — Documentation for this specific version 

- `📁PyRomusa_AI/` — The secondary folder, which only has all the code that contributes to the 100% functional PyRomusa AI

    - `🐍PyRomusa_AI.py` — **`PyRomusa AI` framework main code** of this version  

    - `📁Datasets/` - Folder with some optional code for the main framework code (`🐍PyRomusa_AI.py`) for ready-made data to train your chatbot

        - more Python files...
   

---

## What's New



- **Bug fixed in the reply engine _`modern`_**: Now, if you select the `modern` engine, it works perfectly if you choose for the chatbot to ignore the last conversation with the user using the `with_memory` parameter in the `bot.reply_at()` function.
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
from PyRomusa_AI import Chatbot

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
from PyRomusa_AI import Chatbot

# Create a chatbot
bot = Chatbot()

# Get help
bot.helper.how_to_start()
```