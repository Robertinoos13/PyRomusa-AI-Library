# `bot.storage.load_from_file()`

## Description

Loads a chatbot from a `.json` file, given its name and location (the folder where it is stored). This function is useful when you have a previously trained chatbot and simply want to generate text with it, without the complexities of training.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`file_name`|The file is loaded/searched for, using the value of this parameter as its name.|`str = None`|
|`file_location`|Specify the path to the folder from where you want to load the chatbot.|`str`|

## Returns

no return values excepted

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

# Loading a pretrained chatbot from a specific folder from the disk (no_name_chatbot.json)
bot.storage.load_from_file(
    file_name="no_name_chatbot",
    file_location="C:\Users\Robert\Desktop\My_Chatbots_Collection"
)

# We use the chatbot to generate text based on a prompt.
print(bot.reply_at("Hello chatbot, how are you?"))
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_