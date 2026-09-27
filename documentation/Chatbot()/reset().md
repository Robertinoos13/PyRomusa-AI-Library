# `bot.reset()`

## Description

Resets the entire chatbot process to factory settings (training, process, etc.). This is useful if you want to reset the chatbot process within a single code run.

## Parameters

no parameters required

## Returns

no return values

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot(chatbot_name="My Offline Bot")

# Reset to factory settings (chatbot_name = "My Offline Bot" -> chatbot_name = "")
bot.reset()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_