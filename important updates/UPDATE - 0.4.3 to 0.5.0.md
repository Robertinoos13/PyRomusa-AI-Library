# ❗IMPORTANT UPDATE: v0.4.3 -> v0.5.0❗

## What's new?

### 1. Talking chatbots, using the function `bot.reply_with_audio()`



#### 1.1. _What is this?_

Now, using just one function, it is possible to have your chatbot speak the generated response based on your prompt. You can take advantage of this with just one simple function that does all the hard work for you for TTS transformation: `bot.reply_with_audio()`

_This feature is very useful if you have in mind a project where you can talk to your own chatbot as if you were talking to it on the phone!_

<br>

#### 1.2. _How to use this new function?_

It is used exactly like the classic function that is most known: `bot.reply_at()`:



``` python
from PyRomusa_AI import Chatbot

bot = Chatbot()

# Let's stop stressing about personalized training data, we use the largest English dataset available
bot.prepared_datasets.english.load_prepared_dataset("high")

bot.trainer.start()

# The expected part for the talking chatbot
# (Did you know that the bot.reply_with_audio() function also can returns text, even though it's specifically made for a chatbot to speak?)
text = bot.reply_with_audio("Hello Chatbot!", engine_name="modern")

print("BOT: " + text)

```
<br>

#### 1.3. _What is the difference between functions `bot.reply_with_audio()` and `bot.reply_at()`?_

|Property|`bot.reply_with_audio()`|`bot.reply_at()`|
|:--|:-:|:-:|
|**Total number of parameters**|14|9|
|Number of required parameters|1|1|
|**What does it return?**|string + sound|string|

>Did you know that the 9 parameters in function `bot.reply_with_audio()` have the same role and are called exactly the same as in function  `bot.reply_at()`? So the remaining 5 parameters in function `bot.reply_with_audio()` are only related to audio functionality (examples of that 5 parameters would be `audio_engine`, `audio_language`, `elevenlabs_api_key`)
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