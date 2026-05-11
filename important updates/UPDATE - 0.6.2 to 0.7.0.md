# ❗IMPORTANT UPDATE: v0.6.2 -> v0.7.0❗

## What's new?

### 1. New Reply Engine: `optimized`

#### 1.1. _What is this?_

What is a Reply Engine? Its role is to generate output based on a prompt in a certain way. Find out more details in the main README of the repository

#### 1.2. How to use this new Reply Engine?

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot()

# Modify the value of the parameter 'engine_name' 
print(bot.reply_at("prompt", engine_name="optimized"))
```

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

### 3. Saving your chatbot in a `.json` file

#### 3.1. _What is this?_
This is the most interesting update in this new version. Now you don't need to rewrite the code of a chatbot from 0 all the time, because now your chatbot can become a file that you can use later or in other code.

#### 3.2. _So what functions are related to this new functionality?_

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot()

# Save your chatbot
bot.storage.save_on_file(
    file_location="C:/where/to/save",
    file_name="file_name_here"
)

# Load your chatbot
bot.storage.load_from_file(
    file_location="C:/from/where/to/load",
    file_name="file_name_here"
)

```

#### 3.3. _What are the mandatory parameters to fill in?_
|parameter|`save_on_file()`|`load_from_file()`|
|:---:|:---:|:---:|
|`file_location`|no|yes|
|`file_name`|no|no|

> the `file_location` parameter only needs to know the location of the folder where the file representing the chatbot is located, and the `file_name` parameter (in the case of the `load_from_file()` function) represents the fixed name of the file in the folder selected with `file_location`

---

### 4. The file structure of this framework has changed.

#### 4.1. _What is this?_
The framework needs certain files to function. Now, to make the framework code cleaner, some code segments have been moved into multiple files.

#### 4.2. _Now what is the current structure and what files do I need at a minimum?_


```
|- 📁pyromusa-ai/
|---- 📁Reply Engines 🟥
|---- 🐍core.py 🟥
|---- 📁Datasets 🟩
|---- 🐍errors.py 🟩
```

> Where: <br> 🟥 - Mandatory file/folder <br> 🟩 - No mandatory file/folder

> Notice: <br> **As a new thing in the structure, we only have the `📁Reply Engines` folder, which contains the code of all Reply Engines in an orderly manner.** It is a very important folder for the optimal functioning of the framework. Without its existence, from v0.7.0, chatbots would not be able to generate replies based on a prompt.

---

### 5. More functions on `bot.helper.describe_functions()`

#### 5.1. _What is this?_
The `bot.helper.describe_functions()` function returns a table with the most important functions of the framework. Now, in this table, you can find more functions than in the previous version (v0.6.2)

---