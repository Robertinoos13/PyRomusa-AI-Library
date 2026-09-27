# `bot.reply_at()`

## Description

Generate a text response based on the training examples the chatbot was trained on and the prompt received as input. It is a useful function if you want to find out how good your current chatbot actually is at answering questions.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`prompt`|It should contain the user input, as this is the most important parameter for generating responses.|`str`|
|`engine_name`|It contains the name of a Reply Engine, thereby generating a response in a specific way.|`"modern"`|
|`sensitivity`|Controls how much recent conversation context is required before examples with last conversations conditions can be used to generate a reply. Higher values make those examples harder to activate and can also affect how confident the chatbot must be in a prompt-to-example match, and therefore how often it falls back to a default message.|`1`|
|`with_memory`|Specify whether the response to be generated should be influenced by previous conversations.|`True`|
|`max_influenced_memory`|How many recent conversations should influence the response to be generated?|`3`|
|`fallback_language`|Specify the language for the default fallback messages. Leave this string empty if you wish to use custom fallback messages by modifying `fallback_empty_string_message`, `fallback_no_understanded_message`, and `fallback_not_sure_message`.|`"english"`|
|`fallback_empty_string_message`|This message will appear if the chatbot receives an empty prompt.|`""`|
|`fallback_no_understanded_message`|This message will appear if the chatbot does not understand the prompt due to limited vocabulary.|`""`|
|`fallback_not_sure_message`|This message will appear if the chatbot encounters another issue.|`""`|
|`temperature`|It influences how noisy the response is. A lower value yields a more precise, correct response, whereas a higher value may result in an illogical answer or a fallback message more frequently.|`0.0`|
|`show_thinking`|It simulates the chatbot's internal thought process—as if it were talking to itself. It does not affect the quality of the response.|`False`|
|`allow_long_text_thinking`|Allows excessively long text in the console when displaying the "thinking" process.|`True`|
|`show_debug`|It displays the valuable values, so you know which training examples the chatbot is missing.|`False`|
|`new_lines_system`|It allows the chatbot to generate a multi-line response.|`True`|
|`censored_words`|Specify which words the function should not return directly by replacing them with other words. The dictionary key must be the forbidden word, and its value must be the word that will appear in its place.|`{}`|

## Returns

- **value type(s):** string
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** yes

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

# Loading a pretrained chatbot from a specific folder from the disk
bot.storage.load_from_file(file_location="C:\Users\Robert\Desktop\My_Chatbots_Collection")

# Generating a string
print(bot.reply_at("Hello chatbot, how are you?"))
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_