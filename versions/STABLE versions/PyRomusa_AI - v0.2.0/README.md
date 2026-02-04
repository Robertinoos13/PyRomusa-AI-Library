# PyRomusa_AI — v0.2.0 🤖

- **Version type:** STABLE
- **Release date:** 2026-02-04

---

## Overview

This version/library focuses on creating a **very simple, beginner-friendly chatbot system**, built with custom logic instead of real machine learning models.

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

`📁PyRomusa_AI - vX.Y.Z/` — The main folder containing everything for that version of the library (full library code + README.md)

 - `📄README.md` — Documentation for this specific version 

- `📁PyRomusa_AI/` — The secondary folder, which only has all the code that contributes to the 100% functional PyRomusa AI

    - `🐍PyRomusa_AI.py` — **PyRomusa AI library main code** of this version  

    - `📁Datasets/` - Folder with some optional code for the main library code (`🐍PyRomusa_AI.py`) for ready-made data to train your chatbot

        - more Python files...
   

---

## What's New

### BIG UPDATE: v0.1.1 -> v0.2.0

- NEW CONCEPT: **Reply Engines**
- A minor bug fixed
- New 2 prepared datasets: **Teacher for PyRomusa AI & High Quality, Low Quantity Romanian Dataset**
- New `PyRomusa AI` folder structure: The main code has been separated from the prepared datasets
- Fallback messages personalization

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

### 2. Learn to start using the library

```python
from PyRomusa_AI import Chatbot

# Create a chatbot
bot = Chatbot()

# Get help
bot.helper.how_to_start()