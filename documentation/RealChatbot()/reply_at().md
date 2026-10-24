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
|`censored_words`|Specify which words should be replaced (the dictionary key name) and with what (the key value).|`{}`|
|`feedback_mode`|If set to True, it allows you to indicate whether the response is good (y) or not (n) after each generation.|`False`|
|`max_allowed_similarity_procent_with_banned_replies`|Set a maximum percentage for the similarity between the response to be returned and the responses prohibited by the user in their feedback. If the calculated similarity exceeds the value of this parameter, a regeneration is attempted.|`0.8`|
|`max_attempts_to_regenerate_in_feedback_mode`|Represents the maximum number of consecutive times a regeneration can occur because the response is considered incorrect.|`3`|

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

_**last updated for `PyRomusa AI` version:** 0.11.0_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_