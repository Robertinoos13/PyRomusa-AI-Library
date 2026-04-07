# ❗IMPORTANT UPDATE: v0.5.0 -> v0.6.0❗

## What's new?

### 1. Debugging and thinking concepts

#### 1.1. _What is this?_

Now, in the `bot.reply_at()` and `bot.reply_with_audio()` function, 2 more totally new parameters have been added: `show_debug` and `show_thinking`.

**These parameters allow you to see more 'under the hood' why your chatbot decided to generate a certain response based on the prompt you entered.
If you know and read the stuff returned by thinking and debugging, you will be able to improve your chatbot's performance in an easier way.**


#### 1.2. _What is the difference between thinking and debugging?_
|debugging|thinking|
|:-------:|:------:|
|**It shows things a little tidier than thinking, as it only shows more relevant things that could help you build your chatbot, but the output is a bit more 'programmer-like'. It's better if you don't want extra details** (e.g. full tokenized user prompt: [1 , 2 , None, 3]).|**It's a bit more animated and 'realistic'. It shows, in an indirect way, most of the processes that happen behind the scenes. It simulates that the chatbot is actually thinking. It will probably show useless information.** (e.g. "_Now that I've finished translating the prompt into my natural language, I need to clean it of the words I don't know_")|

>The 2 concepts do not influence the chatbot's performance at all, they only give you access to details about how the respective response was chosen to be generated for you.

#### 1.3. How to use these concepts?

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot()

# Show debugging
bot.reply_at("prompt", show_debug=True)

# Show thinking
bot.reply_at("prompt", show_thinking=True)
```
> It is not possible to have both parameters set to `True` in a single function. This will cause an error.
---

### 2. Upgrade to the prepared dataset 'Teacher for PyRomusa AI'

#### 2.1. _What is this?_

There's no point in adding too many details here, but you should know that **the vocabulary and number of examples for this prepared dataset (Teacher for PyRomusa AI)  have increased.** Now, theoretically, chatbots with this dataset can respond to more prompts.

<br>

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

### 3. _Reply engine 'modern' has been set as the default value of the `engine_name` parameter_

#### 3.1. _What is this?_
(you can find out what a Reply Engine is in the main README of the repository)

**As before the 'stable' engine was the default value in the `bot.reply_at()` function and it was unable to respond with anything more creative than a fallback message to a one-word prompt, now, in its place, the 'modern' engine has been put** for the overall performance of the response higher than that of 'stable'.

Now it is no longer necesary to do this to use the best reply engine at the moment:
``` python
# It is no longer necessary to modify the 'engine_name' parameter if you want to set the value to 'modern'
bot.reply_at("prompt", engine_name='modern')
```
---

### 4. _Specific errors types on `PyRomusa AI`_

#### 4.1. _What is this?_
Work has begun on various types of errors specific to `PyRomusa AI`. That is, we are starting to replace some known errors from Python (like `ValueError`, `TypeError`) in `PyRomusa AI` for certain situations. The first type of error specific to `PyRomusa AI` is `SameNotAllowedError` (when two variables/parameters are not allowed to have the same value as the other)

#### 4.1. _Example code to catch this error_
``` python
from PyRomusa_AI import Chatbot

bot = Chatbot(chatbot_name="My Teacher")

bot.prepared_datasets.romanian.load_prepared_dataset(dataset_name="pyromusa-ai-teacher")

bot.trainer.start()

# SameNotAllowedError (for 'show_debug' and 'show_thinking' values)
print(bot.reply_at("prompt", show_debug=True, show_thinking=True))
```
---