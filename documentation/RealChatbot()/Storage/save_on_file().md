# `bot.storage.save_on_file()`

## Description

Save the chatbot to a `.pt` file. This is useful when you want to share the chatbot with others or use it in scripts located in a different path, without needing to train it on the training data again.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`file_name`|Contains the name you want the file in question to have.|`"my_chatbot"`|
|`file_location`|Specify the path to the folder where you want to save the chatbot. Leave this parameter as is (as an empty string) if you want to save the file in the same folder from which this function is called.|`""`|

## Returns

no return value excepted (only a saved file on your disk)

## Codes examples

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot(tokenizer_type="word-level")

# We load a random dataset (Default English Dataset: MID-RANGE) and immediately begin training.
bot.prepared_datasets.english.load_prepared_dataset("mid")
bot.trainer.start(epochs=10, show_loss_every_x_loops=1)

# We save the chatbot to a file in the fastest possible way (without modified parameters) in the folder where the script is running.
bot.storage.save_on_file()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_