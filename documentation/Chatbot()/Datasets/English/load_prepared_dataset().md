# `bot.prepared_datasets.english.load_prepared_dataset()`

## Description

Upload a prepared dataset in English, ready with training examples. This is a useful feature if you want to quickly load many training examples for testing without having to write them all from scratch.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`dataset_name`|It may contain an access keyword for a prepared dataset, allowing a specific dataset to be loaded from the available ones (e.g., `'low'`, `'mid'`, `'high'`, etc.).|`str`|

## Returns

no return value excepted (only a saved file on your disk)

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

# We load a specific dataset (Default English Dataset: HIGH-END) and immediately begin training.
bot.prepared_datasets.english.load_prepared_dataset("high")
bot.trainer.start()

# The infinite conversation loop (stopping on demand, depending on the input)
while True:

    user_input = input("USER: ")

    if user_input.lower() in ("pa", "bb", "exit"): # Type one of these words to exit the loop.
        break

    else:
        print("BOT: " + str(bot.reply_at(
            prompt=user_input
        )))
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_