# `bot.reply_at()`

## Description

Generate a text response based on the training examples the chatbot was trained on and the prompt received as input. It is a useful function if you want to find out how good your current chatbot actually is at answering questions.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`prompt`|It should contain the user input, as this is the most important parameter for generating responses.|`str`|
|`max_new_tokens`|Limit the chatbot to generating only a specific number of tokens per function call.|`150`|
|`temperature`|It influences how chaotic the generated response is. A lower value yields more precision, while a higher value results in more randomness.|`0.8`|
|`auto_write_prompt_on_default_QA_formating`|The prompt is rewritten in the format the chatbot understands best, ensuring the most accurate response.|`True`|

## Returns

- **value type(s):** string
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** yes

## Codes examples

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot()

# Loading a pretrained chatbot from the same folder with this script (my_chatbot.pt)
bot.storage.load_from_file()

# Generating a string
print(bot.reply_at("Hello chatbot, how are you?"))
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_