# `bot.trainer.show_relationed_output_with_input_ids()`

## Description

It displays the possible words the chatbot can generate when a specific word is present in the input (this function shows them as words, the human's language). It is a useful function if you want to see what words to expect in the chatbot's output when it encounters a specific word in the prompt.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`with_print`|Specify whether you want to display the value as quickly as possible (`True`), or if you want to manually write the `print()` function or use the displayed value for something else (`False`).|`True`|

## Returns

- **value type(s):** dictionary
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** no (by default)

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

bot.prepared_datasets.english.load_prepared_dataset("high")

# Call this function to start training; otherwise, you will get an AttributeError.
bot.trainer.start()

bot.trainer.show_relationed_output_with_input_words()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_