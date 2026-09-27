# `bot.trainer.start()`

## Description

Start training the chatbot so that, once invoked, it can generate human-like text based on the input prompt. It is an important function when you know you have uploaded all the necessary training data.

## Parameters

no parameters required


## Returns

no returns excepeted

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

# We are loading the smallest prepared dataset in English.
bot.prepared_datasets.english.load_prepared_dataset("low")

"""
The moment of truth: 
Why is the `bot.trainer.start()` function so important? 
↓↓↓
"""

# We are testing our chatbot before training (empty output).
print(f"BOT: {bot.reply_at(prompt=input("USER: "))}")

# We begin training.
bot.trainer.start()

# We are testing our chatbot after training (will generates something).
print(f"BOT: {bot.reply_at(prompt=input("USER: "))}")
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_