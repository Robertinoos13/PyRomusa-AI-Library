# ❗IMPORTANT UPDATE: v0.9.1 -> v0.10.0❗

## What's new?

### 1. Added `word-level` tokenizer on `RealChatbot()` object

#### 1.1. _What is this?_

For more flexibility in customizing the architecture of a chatbot created with the `RealChatbot()` object, instead of learning each character, as of v0.10.0, you can also make your chatbot learn directly from whole words. The `word-level` tokenizer provides more spelling accuracy when generating if you have few training examples and a shorter training time, and besides the advantages, the disadvantage would be that it is much more sensitive in case the user writes a prompt with misspelled words.


#### 1.2. _How to use this new tokenizer (code example)?_

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot(
    tokenizer_type="word-level" # Be sure to use 'char-level' if you want other option
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

---

### 3. Bug fixed when loading a chatbot from a `.pt` file

#### 3.1. _What is this?_

To establish the experience with `PyRomusa AI`, we have fixed a bug related to training a pretrained model loaded from a file: now you can provide your chatbot with new training examples (similar to fine-tuning), while keeping the process from last time without major issues

---

### 4. Corrected parameter name `learn_late` -> `learn_rate`

#### 4.1. _What is this?_

A small spelling error has been corrected in the parameter name found in the `bot.trainer.start()` function, the `RealChatbot()` object.

---

### 5. Added auto checkpoint/ask to stop while training

#### 5.1. _What is this?_

To have flexible training on the `RealChatbot()` object, you can now save the 100% automatic chatbot process periodically to a file and set the `bot.trainer.start()` function to periodically ask you to stop training on demand.

#### 5.2. _How to use these functionalities (code example)?_

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot()

# We are loading the largest English dataset available for training (write "low" if you want the shortest English dataset)
bot.prepared_datasets.english.load_prepared_dataset("high")

bot.trainer.start(
    epochs=20,

    # 1. Checkpoint configurations available
    auto_checkpoint_every_x_epochs=2,
    checkpoint_file_name="my_test_checkpoint",
    checkpoint_file_location="C:/enter/here/your/path/optionally",

    # 2. Stop training configurations available
    ask_to_stop_every_x_epochs=5
)

```

---