# `bot.trainer.show_translated_examples()`

## Description

It displays approximate translations of training examples in terms of words/tokens. This is a useful feature if you want to see roughly how the chatbot perceives a training example (in tokens).

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`with_print`|Specify whether you want to display the value as quickly as possible (`True`), or if you want to manually write the `print()` function or use the displayed value for something else (`False`).|`True`|

## Returns

- **value type(s):** list
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** no (by default)

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

bot.prepared_datasets.english.load_prepared_dataset("high")

bot.trainer.start()

bot.trainer.show_translated_examples()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_