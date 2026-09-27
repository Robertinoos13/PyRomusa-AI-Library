# `bot.reset()`

## Description

Resets the entire chatbot process to factory settings (training, specifications, etc.). This is useful if you want to reset the chatbot process within a single code run.

## Parameters

no parameters required

## Returns

no return values

## Codes examples

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot(d_model=512)

# Reset to factory settings (d_model = 512 -> d_model = 32)
bot.reset()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_