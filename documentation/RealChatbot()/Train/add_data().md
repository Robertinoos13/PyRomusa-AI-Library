# `bot.trainer.add_data()`

## Description

Add a Q&A-style training example that is already structured and included in the chatbot's training text. This is a useful function when you want your chatbot to learn how to answer specific questions.

## Parameters

|name|description|default value|
|:---:|:---|:--:|
|`training_input_example`|In that example, add a question.|`""`|
|`training_output_example`|In that example, add a answer.|`""`|


## Returns

no return value

## Codes examples

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot(tokenizer_type="word-level")

# Some Q&A personalized examples
bot.trainer.add_data("What’s your favorite color?", "My favorite color is blue because I like the color of the sea.")
bot.trainer.add_data("Do you like cats?", "Yes, I love cats because they are very cute.")
bot.trainer.add_data("What did you eat today?", "I ate pizza today.")
bot.trainer.add_data("What’s your favorite game?", "My favorite game is hide-and-seek.")
bot.trainer.add_data("Where would you like to travel?", "If I could travel, I would travel to America, because I want to see how people live outside of Europe.")


bot.trainer.start(epochs=5)

user_input = "What’s your favorite color?"
print(f"USER: {user_input}")
print(f"BOT:  {bot.reply_at(user_input)}")
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_