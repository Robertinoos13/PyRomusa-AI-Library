# `bot.show_current_training_text()`

## Description

Display the raw text the chatbot uses for training. It is useful to see the training text already prepared before wasting time waiting for the training process to complete.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`with_print`|Use this parameter to specify whether you want to manually write the print() function (True if not, False if yes).|`True`|

## Returns

- **value type(s):** string
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** optional (no by default)

## Codes examples

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot()

# Loading the smallest dataset in english available
bot.prepared_datasets.english.load_prepared_dataset("low")

# Displays what the chatbot will learn next.
bot.show_current_training_text()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_