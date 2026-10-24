# ❗BIG UPDATE: v0.10.1 -> v0.11.0❗

## What's new?

### 1. Added `semiwords-level` tokenizer on `RealChatbot()` object

#### 1.1. _What is this?_

For more flexibility in customizing the architecture of a chatbot created with the `RealChatbot()` object, instead of learning each character, as of v0.10.0, you can also make your chatbot learn semiwords. The `semiwords-level` tokenizer is the perfect balance between the quality of the responses and flexibility.


#### 1.2. _How to use this new tokenizer (code example)?_

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot(
    tokenizer_type="semiwords-level"
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

### 3. Docstrings for all available functions

#### 3.1. _What is this?_

It is a system where, if you hover your cursor over a specific function—without clicking—it provides a description and displays the function along with every available parameter. This feature works in IDEs like VSCode. Download `PyRomusa AI` and try it out yourself!

---

### 4. Raw text as training example

#### 4.1. _What is this?_

As of this version, the `PyRomusa AI` framework supports two types of training examples: Q&A and raw text. **Raw text is useful when you want to teach your chatbot about a specific subject or how a human language is used, without necessarily focusing on answering a specific, fixed question. It is recommended to use raw text in combination with some Q&A examples.** Without Q&A-style examples, the chatbot cannot correctly answer most questions, as it assumes it should simply continue whatever you have said.

#### 4.2. _How do you correctly add a raw text example?_

``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot()

# This is the 'raw-text' type of training example from the new update.
bot.trainer.add_data("Raw text is a new type of training example for the PyRomusa AI framework, introduced as recently as version v0.11.0, which featured a larger-than-usual update. It is recommended for helping the chatbot better understand how a spoken language works or for learning about a specific subject.", example_type="raw")

# We will also include a Q&A-style example, so that the structure of each training example can be observed.
bot.trainer.add_data("Hello bro, how are you today?", "Hello, I'm fine, thanks!")

# Verification:
bot.trainer.start(1) # Rapid training, to update the training text
bot.show_current_training_text()
```

---

### 5. Timer on training loop

#### 5.1. _What is this?_

Since the `RealChatbot()` object is resource-intensive, and the `bot.trainer.start()` function typically takes the longest to execute among all the object's methods, **you can implement a timer that displays the total time elapsed once the training process is complete.** This is a neat feature for those looking to run a benchmark, or simply for curious users who want to know how long it took to train their own personal chatbot.

#### 5.2. _How to activate this timer?_
``` python
from pyromusa_ai import RealChatbot

bot = RealChatbot()

bot.prepared_datasets.english.load_prepared_dataset("low")

bot.trainer.start(
    epochs=11, 
    show_total_time_of_training_when_ends=True # ! Make sure this parameter is set to True
)

# OPTIONAL: Test your chatbot
print(bot.reply_at("Hello"))
```

The timer should look something like this:
```
[TIMER] Training completed successfully. The process took 107.931 seconds.
```
---

### 6. Censored words system on `RealChatbot()`

#### 6.1. _What is this?_

This system requires a Python dictionary as its value; it replaces any words found in the generated response—if those words exist as keys in the dictionary—with their corresponding key values, before the final output is displayed. This exact system has now been added to the `Chatbot()` object as well. If you are already familiar with this system, then that’s perfect.

#### 6.2. How do I use this system?

``` python
print(bot.reply_at(
    prompt="...",
    censored_words={"bad-word": "[CENSORED WORD]"}
))
```

---

### 7. New parameters added (`weight_decay` & `optimizer_type`) in `bot.trainer.start()` function

#### 7.1. _What is this?_

For those who have used various `PyTorch` optimizers in their projects, you will know what I am talking about. The `optimizer_type` parameter specifies which type of optimizer you wish to use for training the chatbot (accepted values ​​in `v0.11.0`: `"adam"` or `"adamw"`). The `weight_decay` parameter functions exactly the same way as it would when applied to a `PyTorch` optimizer.

Furthermore, thanks to this variety of optimizers available to choose from, I have also changed the default optimizer that runs under the hood of `bot.trainer.start()`: from `Adam` to `AdamW`.

#### 7.2. How can I access these parameters?

``` python
bot.trainer.start(
    weight_decay=0.01
    optimizer_type="adam"
)
```

---
### 8. Specified value type for all parameters available on `bot.trainer.start()` function

#### 8.1. _What is this?_

To ensure optimal performance, each parameter for this function is compatible with only one specific data type _(boolean, float, integer, or string)_. If an incorrect value is provided for a parameter, the function will return an error immediately—before execution even begins—allowing you to correct the mistake right away. This is beneficial because the function generally takes a significant amount of time to run; if an invalid parameter value were to be encountered, say, 80% of the way through the process, the entire operation would fail, resulting in a complete waste of time.

---
### 9. A optional feedback system (with y/n) while you are talking to the chatbot

#### 9.1. _What is this?_

Now, to improve the chatbot's responses, you can provide brief yes/no (y/n) feedback after a response is generated. If you indicate that the generated response is not good (n), then try regenerating it.

#### 9.2. _Parameters available in relation to this system_

``` python
bot.reply_at(
    feedback_mode=False,
    max_allowed_similarity_procent_with_banned_replies=0.8,
    max_attempts_to_regenerate_in_feedback_mode=3
)
```

where:

|parameter name|its description|
|:-|:-:|
|`feedback_mode`|Enable feedback mode. Make sure it is set to True.|
|`max_allowed_similarity_procent_with_banned_replies`|represents the maximum percentage (calculated at the character level) allowed for a final answer, in cases where that percentage of similarity exists with an incorrect answer|
|`max_attempts_to_regenerate_in_feedback_mode`|Maximum number of regenerations. If no response is considered good, the response with the lowest similarity to the incorrect responses is automatically selected.|

---
### 10. Clear separation between special tokens and normal tokens

#### 10.1. _What is this?_

Chatbots can now see special tokens within the structure of the training text in an anonymous way. This means they no longer need to generate special tokens for the end of a sentence on a character-by-character basis; instead, they can generate the token directly, making the generation system more accurate/precise.

---

### 11. Removing unnecessary comments from the code

#### 11.1. _What is this?_

In the source code for the `RealChatbot()` object, some unnecessary comments have been removed. The code is now visually cleaner. In practice, this has no impact whatsoever on performance or the quality of the framework's functions.

---