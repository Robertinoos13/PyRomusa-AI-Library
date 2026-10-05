# `RealChatbot()`

## What is this?

**In programming terms**, it is an object—specifically, a Python class—that requires instantiation to function correctly.

**Within the context of this framework (`PyRomusa AI`)**, is a type of chatbot capable of generating text (provided you configure it correctly using specific functionalities of this object).

---

## What is so special about this object?

**Since this class is essentially a type of chatbot**, you can—in theory—train it on your own examples and use it to generate text.

**What makes it even more special is that:**
- It relies primarily on `PyTorch` for the AI ​​logic.
- He can generalize the text he tried to learn.
- It exhibits exactly the symptoms of a true LLM (overfitting, long training times, etc.).
- has the potential to invent words.
- LLM trained from scratch, but with minimal code
- It can learn at the character level or the word level, allowing you to optimize your objective.

---

## How do I create an instance of it to start using certain functionalities?

``` python
from pyromusa_ai import RealChatbot

# That is roughly how the instance is created in minimal mode.
bot = RealChatbot()

# From this point on, you can start using the created instance. For example:
bot.show_basic_specs()

```
---
_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_