# `Chatbot()`

## What is this?

**In programming terms**, it is an object—specifically, a Python class—that requires instantiation to function correctly.

**Within the context of this framework (`PyRomusa AI`)**, is a type of chatbot capable of generating text (provided you configure it correctly using specific functionalities of this object).

---

## What is so special about this object?

**Since this class is essentially a type of chatbot**, you can—in theory—train it on your own examples and use it to generate text.

**What makes it even more special is that:**
- Optimized for low-end hardware
- Maximum speed for training and response generation
- Architecture that differs from what is found elsewhere
- Special concept: Reply Engines
- Correct generated answers even with few training examples
- The use of external dependencies is minimal (only `NumPy` is used in the `modern` Reply Engine, and `Pandas` in a `Helper` function).
- It is so lightweight that it even runs on a phone ([tested on Pydroid 3](https://www.tiktok.com/@pyromusa_ai/video/7690226335301504278?is_from_webapp=1&sender_device=pc), september 2026).

---

## How do I create an instance of it to start using certain functionalities?

``` python
from pyromusa_ai import Chatbot

# That is roughly how the instance is created in minimal mode.
bot = Chatbot()

# From this point on, you can start using the created instance. For example:
bot.show_basic_specs()

```
---
_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_