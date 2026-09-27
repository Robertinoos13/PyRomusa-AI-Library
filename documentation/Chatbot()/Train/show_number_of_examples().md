# `bot.trainer.show_number_of_examples()`

## Description

Displays the number of training examples from the entire dataset loaded into the chatbot. This is a useful function for getting an idea of ​​roughly how many questions the chatbot can answer correctly (theoretically speaking).

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`with_print`|Specify whether you want to display the value as quickly as possible (`True`), or if you want to manually write the `print()` function or use the displayed value for something else (`False`).|`True`|

## Returns

- **value type(s):** integer
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** no (by default)

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

# Loading the largest dataset prepared in English
bot.prepared_datasets.english.load_prepared_dataset("high")

# Displaying the number of examples in the respective dataset in the console.
bot.trainer.show_number_of_examples()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_