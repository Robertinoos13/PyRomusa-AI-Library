# `bot.storage.save_on_file()`

## Description

Save the chatbot to a `.json` file. This is useful when you want to share the chatbot with others or use it in scripts located in a different path, without needing to train it on the training data again.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`file_name`|Contains the name you want the file in question to have.|`"no_name_chatbot"`|
|`file_location`|Specify the path to the folder where you want to save the chatbot.|`str = None`|

## Returns

no return value excepted (only a saved file on your disk)

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

# We load a specific dataset (Default English Dataset: MID-RANGE) and immediately begin training.
bot.prepared_datasets.english.load_prepared_dataset("mid")
bot.trainer.start()

# We save the chatbot to a file in a specific folder from the disk.
bot.storage.save_on_file(
    file_name="my_chatbot",
    file_location="C:\Users\Robert\Desktop\My_Chatbots_Collection"
)
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_