# PyRomusa_AI — v0.4.0 🤖

- **Version type:** STABLE
- **Release date:** 2026-02-19

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

### IMPORTANT UPDATE: v0.3.0 -> v0.4.0

- **New Reply Engine: 'modern':** With the help of this reply engine, based on NumPy, it now understands prompts of any length, it is not so sensitive whether you write letters with diacritics/accents or not, so the chances of returning a fallback message are lower compared to the 'stable' and 'chaos' reply engines.

- **Upgrade at 'Teacher for PyRomusa AI' prepared dataset:**  Now, chatbots that have this dataset prepared are able to respond to more prompts than in the latest STABLE version (0.3.0)

#### What small updates are planned to appear in v0.4.X?
_Indeed, these update plans were planned to appear in v0.3.X, but we decided to work a little more on the overall quality of the chatbots (creating the 'modern' engine), so, having achieved this goal, we went straight to version 0.4.0._

- The first prepared datasets in English
- Chatbot that can speak on demand (if you specify this in the code)
- Improving the prepared dataset called _'Teacher for PyRomusa AI'_ for the Romanian language, adding more training data to it.

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
```