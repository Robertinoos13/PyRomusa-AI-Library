# `Datasets()`

## Description

Programmatically speaking, it is a class nested within the main `Chatbot()` object that has several methods/functions you can use.

This nested class contains special functions directly related to loading a dataset that is already prepared for training, thereby reducing the time required to write training examples from scratch, allowing the library's syntax to remain as clean and logical as possible.

---

## How do you access certain functions/methods within it?

``` python
from pyromusa_ai import Chatbot

# Step 1: Creating the instance of the main object
bot = Chatbot()

# Step 2: Using a function from Datasets() (accessed via 'prepared_datasets')
bot.prepared_datasets.english.load_prepared_dataset("high")
```
---
_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_