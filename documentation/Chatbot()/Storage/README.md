# `Storage()`

## Description

Programmatically speaking, it is a class nested within the main `Chatbot()` object that has several methods/functions you can use.

This nested class contains special functions directly related to saving and loading a chatbot, allowing the library's syntax to remain as clean and logical as possible.

---

## How do you access certain functions/methods within it?

``` python
from pyromusa_ai import Chatbot

# Step 1: Creating the instance of the main object
bot = Chatbot()

# Step 2: Using a function from Storage() (accessed via 'storage')
bot.storage.save_on_file()
```
---
_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_