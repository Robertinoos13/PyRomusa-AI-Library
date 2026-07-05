# ❗VERY IMPORTANT UPDATE: v0.8.0 -> v0.9.0❗

## What's new?

### 1. New principal object, `RealChatbot()`

#### 1.1. _What is this?_

For the first time in the history of `PyRomusa AI`, a second main object has been added as `Chatbot()`: `RealChatbot()`. **This is also a type of chatbot, but it is based on real LLM (Large Language Model) technologies.** It is perfect for those who want a real experience of training, response generation and architecture.


#### 1.2. How can I use it?

Here's the good part, first of all: The main functions of `RealChatbot()` are written exactly the same as `Chatbot()`, just with different parameters:
``` python
from PyRomusa_AI import RealChatbot

# Create a chatbot named "RomusaBot"
bot = RealChatbot(
    chatbot_name="RomusaBot",
    d_model = 64 # You will never find a parameter like this in the Chatbot() object.
)

# Add some input/output training data
bot.trainer.add_data(
    "Hello chatbot!",
    "Hello human, how can I help you today?"
)

bot.trainer.add_data(
    "Bye chatbot!",
    "Bye human, see you next time!"
)

# Start the training process
bot.trainer.start(epochs=200) # This is a function with different parameters than Chatbot()

# Generate a response to a user input
print(bot.reply_at("Hello chatbot!", max_new_tokens=55)) # And this has certain different parameters
```
> **ATTENTION:** If `RealChatbot()` has additional parameters than `Chatbot()`, then `Chatbot()` also has certain additional parameters than `RealChatbot()` (e.g. in the `bot.reply_at()` function)

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

---