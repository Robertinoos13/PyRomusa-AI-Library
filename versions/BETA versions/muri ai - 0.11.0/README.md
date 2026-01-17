# muri_ai — v0.11.0 🤖

**Version type:** BETA  
**Release date:** 2026-01-17

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

- `muri_ai.py` — Full implementation of the library for this version  
- `README.md` — Documentation for this specific version  

---

## What's New

- 2 functions in the Help class were completed, without replacing their real context with 'pass'
- **FUNCTION NAME CHANGED:** 
`bot.responding_at()` -> `bot.reply_at()`

⚠️ **BETA notice:**
- API may change in future versions
- Logic is not optimised
- Some behaviours may feel inconsistent
- This version may contain bugs or unfinished features

## Quick Usage Examples

### 1. Creating your first functional chatbot ever
```python
from muri_ai import Chatbot

# Create a chatbot
bot = Chatbot(chatbot_name="MuriBot")

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
from muri_ai import Chatbot

# Create a chatbot
bot = Chatbot()

# Get help
bot.helper.how_to_start()