# ❗IMPORTANT UPDATE: v0.3.0 -> v0.4.0❗

## What's new?

### 1. New Reply Engine: _modern_

#### 1.1. _What is this?_

A new response generation logic has been published: **`modern`**

It comes with improvements over engines like `stable` and `chaos`. The new  engine (`modern`) is the first engine that relies on NumPy to function properly. See its advantages and disadvantages in the main README of the repository.

#### 1.2. _How to use this new reply engine?_


``` python
from PyRomusa_AI import Chatbot

bot = Chatbot()

bot.trainer.add_data(
    training_input_example="Hello",
    training_output_example="Bye"
)
bot.trainer.start()

# Use it in this function
bot.reply_at(
    prompt="Hello"
    engine_name="modern" # here
)

```
---

### 2. Upgrade to the prepared dataset 'Teacher for PyRomusa AI'

#### 2.1. _What is this?_

There's no point in adding too many details here, but you should know that **the vocabulary and number of examples for this prepared dataset (Teacher for PyRomusa AI)  have increased.** Now, theoretically, chatbots with this dataset can respond to more prompts.

#### 2.2. _How to use this prepared dataset (code example)?_

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot(chatbot_name="My Teacher") # Remember that 'chatbot_name' variable is optional to fill in, it does not influence the performance of the chatbot. This is just for personality.

# The most important line of code: Using the prepared dataset 'Teacher for PyRomusa AI' in Romanian.
bot.prepared_datasets.romanian.load_prepared_dataset(dataset_name="pyromusa-ai-teacher")

bot.trainer.start()

# 'Ce este PyRomusa AI?' (Romanian) = 'What is PyRomusa AI?' (English)
print(bot.reply_at("Ce este PyRomusa AI?"))
```