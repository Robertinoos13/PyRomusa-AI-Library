# `bot.trainer.show_dataset()`

## Description

Displays a list of all uploaded chatbot training examples (one example = `{}`). This is a useful function if you want to see the types of questions the chatbot can answer correctly.

## Parameters

no parameters required


## Returns

- **value type(s):** list
- **number of values returned per call:** 1
- **It needs an additional `print()` function:** no

## Codes examples

``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

# Some Q&A personalized examples
bot.trainer.add_data("What’s your favorite color?", "My favorite color is blue because I like the color of the sea.")
bot.trainer.add_data("Do you like cats?", "Yes, I love cats because they are very cute.")
bot.trainer.add_data("What did you eat today?", "I ate pizza today.")
bot.trainer.add_data("What’s your favorite game?", "My favorite game is hide-and-seek.")
bot.trainer.add_data("Where would you like to travel?", "If I could travel, I would travel to America, because I want to see how people live outside of Europe.")

# We display the loaded training data in the console.
bot.trainer.show_dataset()
```

---

_**last updated for `PyRomusa AI` version:** 0.10.1_

_(Keep in mind: an older version means this documentation is more likely not to be 100% accurate for the latest available version.)_