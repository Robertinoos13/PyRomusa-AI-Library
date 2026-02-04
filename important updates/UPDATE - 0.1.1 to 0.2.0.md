# ❗BIG UPDATE: 0.1.1 -> 0.2.0❗

## What's new?

### 1. New concept in `PyRomusa AI`: **engines**

#### 1.1. _What is this?_

With this completely new concept in PyRomusa AI with engines, you can now change the logic of generating a chatbot response by choosing an engine.

As engines available in STABLE version 0.2.0, we have:

|Engine Name|Advantages|Disadvantages|
|:---------:|:---------|:------------|
|  stable   |It writes more correctly in terms of word order, and the chatbot's response is also much easier to read and understand.|High chances of not understanding an extremely short prompt (e.g. a word or three), even if it has it as an example in training, also returning a fairly easy fallback message.|
|  chaos    |Makes more of an effort to understand a message, so the chances of returning an automatic fallback message are lower.|In general, he writes some strange and quite difficult to understand messages, often not knowing what the chatbot meant. It can also write too many or too few words, thus compounding the difficulty of fully understanding what the chatbot meant.|

#### 1.2. _Example of selecting an engine_

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot(chatbot_name="test")

bot.prepared_datasets.romanian.load_prepared_dataset(dataset_name="high")
bot.trainer.start()

bot.reply_at(
            prompt="Hey!", # This is where you will write your prompt.
            engine_name="chaos" # Here you select the engine you prefer ('chaos' or 'stable')
            )


# NOTE: 
# - The 'stable' engine is set as the default value 
# - The 'chaos' engine is actually the first logic ever invented in this function (you can find it in older versions).
```

---

### 2. Reorganizing `PyRomusa AI` files for cleaner code

---

#### 2.1. _What exactly is this about?_

The main `PyRomusa AI` code has been separated from the code that contributes to the prepared datasets data (input-output examples)

---

#### 2.2. _OLD STRUCTURE vs NEW STRUCTURE_

---

#### a) OLD STRUCTURE _(berofe)_

`📁PyRomusa AI - vX.Y.Z/`

- `🐍PyRomusa_AI.py`

- `📄README.md`

---

#### b) NEW STRUCTURE _(now)_

`📁PyRomusa_AI - vX.Y.Z/`

 - `📄README.md`

- `📁PyRomusa_AI/`

    - `🐍PyRomusa_AI.py` 

    - `📁Datasets/`

        - more Python files...
   

NOTE: **Basically, you will need at least the `🐍PyRomusa_AI.py` file to use the main functions of `PyRomusa AI`**

---

#### 2.3. What is the reason for this change?
---

The reasons for this change was:

- **before you spent too much time scrolling down to find a code sequence** due to the large number of lines of code (about 4000 lines of code before)
- This was also done **to reduce the memory of the main script** _(from about 500kb -> 20kb)_

---

### 3. Upgrade to chatbot fallback response personalization

#### 3.1. _What is this?_

The term 'fallback message' refers to backup messages in case the chatbot doesn't understand the prompt or doesn't know what to respond with.

**The term 'fallback message' refers to backup messages in case the chatbot doesn't understand the prompt or doesn't know what to respond with.**

**This customization consists of what language to say the fallback messages** (currently available options: English, Romanian, Spanish) **or what to say in case X or Y.**


#### 3.2 Code examples with this new functionality

#### a) Setting messages in a specific language

``` python
from PyRomusa_AI import Chatbot

bot = Chatbot(chatbot_name="test")

bot.prepared_datasets.romanian.load_prepared_dataset(dataset_name="high")
bot.trainer.start()

print(bot.chatbot_name, ": ", bot.reply_at(
                                           prompt="Hello chatbot!", # Here you put the user prompt
                                           engine_name="stable", # Even if it is a default engine, know that any changes related to fallback messages only work in this engine.
                                           fallback_language="english" # Here you put the desired language in which you want the fallback messages to be ('english', 'romanian' or 'spanish')
                                           ))

```
---
#### b) Making fallback messages 100% personalized to your preferences


``` python
from PyRomusa_AI import Chatbot

bot = Chatbot(chatbot_name="test")

bot.prepared_datasets.romanian.load_prepared_dataset(dataset_name="high")
bot.trainer.start()

print(bot.chatbot_name, ": ", bot.reply_at(prompt="Hello chatbot!", 
                                           engine_name="stable",

                                           fallback_language="", # We do this as a free string so we can apply the desired changes, otherwise it won't work

                                           fallback_empty_string_message="Put your message here in case the prompt is empty (has no text at all)",
                                           fallback_no_understanded_message="Put your message here in case the chatbot doesn't understand the prompt",
                                           fallback_not_sure_message="Put your message here for other cases"))

```

---

### 4. New prepared datasets

#### 4.1. _What is this?_

Ok, this is a pretty common update. This update with the prepared datasets adds two new prepared datasets, called:

- **Teacher for PyRomusa AI** - This contains input-output examples to give the chatbot some small knowledge about the PyRomusa AI library. This library is planned to be improved in the future.

- **High Quality, Low Quantity Romanian Dataset** - quantity of input-output examples higher than its previous version, **High Quality, _Very Low_ Quantity Romanian Dataset**.

#### 4.2. You want more info about this new prepared datasets?

**If you want to see the specifications of the prepared datasets**, just look for those specifications in the main README (the first README you encounter when you first enter this repository), in the `About Prepared Datasets` section.

---

### 5. Bug Fixing

A minor update has been fixed:
- Probably, your utf-8, in your Python codes, usually gave an error for rarer letters, which as a native English speaker you don't see all day long, letters like 'ă', 'ț', 'ș', etc. Now this problem has been fixed, you will no longer get errors just for a string with 'weirder' letters.