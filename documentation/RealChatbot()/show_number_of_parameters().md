# `bot.show_number_of_parameters()`

## Description

Displays the total number of chatbot parameters, depending by tehnical chatbot specifications (`d_model`, `num_heads`, `num_layers`, etc.). It is useful to know how demanding the chatbot might be on your hardware and how 'intelligent' it is expected to be.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`with_print`|Use this parameter to specify whether you want to manually write the print() function (True if not, False if yes).|`True`|

## Returns

- **value type(s):** string or integer
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** optional (no by default)

## Codes examples

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot()

# Displays a number in a simple and direct way, without any complications.
bot.show_number_of_parameters()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_