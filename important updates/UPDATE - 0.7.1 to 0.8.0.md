# ❗IMPORTANT UPDATE: v0.7.1 -> v0.8.0❗

## What's new?

### 1. New Reply Engine: `unsmarty`

#### 1.1. _What is this?_

What is a Reply Engine? Its role is to generate output based on a prompt in a certain way. Find out more details in the main README of the repository

#### 1.2. How to use this new Reply Engine?

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot()

# Modify the value of the parameter 'engine_name' 
print(bot.reply_at("prompt", engine_name="unsmarty"))
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

---

### 3. Memory quantity upgrade

#### 3.1. _What is this?_

This is the chatbots conversation storage system. In older versions (`0.7.1 >=`), only the last conversation could be stored. Now, for more flexibility, the entire conversation from that session can be stored.

---

### 4. Censored words system

#### 4.1. _What is this?_

Maybe your chatbot has learned some bad/vulgar words and you don't want it to say them in its output? Well, now they can be replaced with other words on request, using the 'censored_words' parameter.

#### 4.2. _How I can replace that bad/vulgar words? (code)_

Well, you can use this system using the `censored_words` parameter in the `bot.reply_at()` function.

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot(chatbot_name="Mr. Censored")

# Add training examples and train it
bot.trainer.add_data(
    "How I am for you?",
    "You are a bad guy for me, sorry"
)

bot.trainer.start()

print(bot.reply_at( 
    prompt="How I am for you?"
    censored_words={"bad": "[CENSORED]"}
))
# EXCEPTED OUTPUT: You are a [CENSORED] guy for me, sorry

```

---

### 5. Ability to generate a message in more lines

#### 5.1. _What is this?_
Previously, chatbots would simply generate a single-line response. Now, chatbots can generate a multi-line response if they have learned to do so in their training examples.

#### 5.2. _How can I teach my chatbot to write a multi-line response?_

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot(chatbot_name="Mr. Multi-Line")

bot.trainer.add_data(
    "Count for me from 1 to 5, placing each digit one under the other.",
    "1 \n2 \n3 \n4 \n5" # NOTE: '\n' was used to teach the chatbot to generate a multi-line response
)

```

---

### 6. More parameters in `bot.reply_at()`

#### 6.1. _What is this?_
The parameters in this function help us customize our output more. Now there are more parameters you can use depending on your preferences and goal.

#### 6.2. _What are the new parameters added in this version?_
``` python
bot.reply_at(
    max_influenced_memory=3,
    new_lines_system=True,
    censored_words={}
)
```

#### 6.3. _Parameter description_

|parameter|value type|description|
|:-|:-:|:-|
|`max_influenced_memory`|integer|Represents the number of recent conversations that influence the generation of the current response|
|`new_lines_system`|boolean|'Tells' the function whether chatbots are allowed to generate multi-line messages|
|`censored_words`|dictionary|Contains all the words that your chatbot is not allowed to say directly. **The dictionary key is the banned word, and the value of that key will be displayed instead of the key if applicable.**|

---

### 7. Updated `bot.helper.questions()`

#### 7.1. What is this?

Now, with the new update, some of the information returned by this function has been updated to be up to date.

---