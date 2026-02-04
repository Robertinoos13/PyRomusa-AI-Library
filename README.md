# `PyRomusa AI` 🤖

**`PyRomusa AI`** is a lightweight Python library for creating simple AI chatbots with minimal code.  
It is designed for learning purposes, rapid prototyping, and experimentation with basic AI concepts.

---

## Quick Navigation 🌐

This README.md file seems a bit long, right? 

Well, just click on the section (the blue text) below that interests you and you'll be taken directly there! 👇

- [Key Features 🔑](#key-features-) 
    - Are you new and still don't know what you can do and what capabilities `PyRomusa AI` has? Discover what you can do with this and what capabilities `PyRomusa AI` has.
- [Repository Structure 📁](#repository-structure-)
    - Are you new at this repository? Learn a little about the structure of this repository to find what you need.
- [Version Types Explained](#version-types-explained)
    -  Here you will find several versions of `PyRomusa AI`, each placed in a specific category, depending on how stable it is, how much effort has been put into fixing bugs, and what the respective version was released for.
- [Complete Code Example Using PyRomusa_AI](#complete-code-example-using-pyromusa_ai)
    - Do you want to see what code using the `PyRomusa AI` library would look like or do you want some ready-to-copy-paste code to see how it works? Well, this is the section you should come to.
- [About Prepared Datasets 🗄️](#about-prepared-datasets-️)
    - Did you know that you can use ready-to-use training datasets to save time creating input-output examples of a chatbot from scratch? Find here all available datasets, their specifications, and a complete example script with loading a dataset.
- [About Reply Engines](#about-reply-engines)
    - Does your chatbot seem to not understand the prompt you wrote or is writing extremely unclearly? This can probably be solved by changing the engine. Click here if you want to learn more about these engines.
- [Contact us 📩🌐](#contact-us-)
    - Do you want to talk to the person/team that created this library called `PyRomusa AI`? Here you will find all the available possibilities to contact us!
- [More ➕](#more-) 
    - Still haven't found what you need? You'll probably find it here.

---

## Key Features 🔑
- Create a chatbot in just a few lines of Python  
- Simple training process (no heavy frameworks involved)  
- Multiple version types: Stable, Beta, and Experimental  
- Beginner-friendly and easy to understand  
- No high-end GPU required

---

## Repository Structure 📁
All versions of the library are stored inside the `📁 versions/` folder.

`📁 versions/`
- `📁 BETA versions/` 
    - 📁 _PyRomusa_AI_ - v0.0.X
- `📁 EXPERIMENTAL versions/` 
    - 📁 _PyRomusa_AI_ - vXYZ
- `📁 STABLE versions/` 
    - 📁 _PyRomusa_AI_ - v0.X.Y




Each version folder contains:
- A full `🐍PyRomusa_AI.py` file 
- A dedicated `📄README.md` for that version  

---

`📁 tutorials/` - This is a folder where all sorts of tutorials will be written to use the library.

`📁 important updates/` - This folder will provide a more detailed description of all the important updates that `PyRomusa AI` has had so far.

---

## Version Types Explained
### BETA 🤖🛠️
- Still in development  
- May contain bugs, incomplete features, or small issues  

### STABLE 😁👍
- Recommended for normal usage  
- Fully functional, tested, and considered complete  

### EXPERIMENTAL 🧪🔬
- Radical changes and experimental ideas  
- Not intended for production use  

---

## Complete Code Example Using PyRomusa_AI

```python
"""
This code works correctly with the following versions:
BETA - v0.0.2
STABLE - v0.1.0, v0.1.1, v0.2.0
EXPERIMENTAL - v001
"""

from PyRomusa_AI import Chatbot

# Create a chatbot named "RomusaBot"
bot = Chatbot(chatbot_name="RomusaBot")

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
bot.trainer.start()

# Generate a response to a user input
print(bot.reply_at("Hello chatbot!"))
```

---
## About **Prepared Datasets** 🗄️

Did you know that from `PyRomusa AI` you can load a ready-made training dataset to the model? Well, here's an example below:
``` python
from PyRomusa_AI import Chatbot

# 1. Create your chatbot
bot = Chatbot(chatbot_name="MyChatbot")

# 2. Load a prepared dataset (in this example, you load the smallest default dataset in Romanian)
bot.prepared_datasets.romanian(dataset_name="low")

# 3. Start training
bot.trainer.start()

# 4. Enjoy to use the chatbot (Salut! = Hello!)
print(bot.reply_at(prompt="Salut!"))

```

---

### Info of All Prepared Datasets Available

|Dataset Name|Vocabulary|Number of examples|Word to acces it|Language|Naturalness|Focus on same questions|Planned to be updated|Avaiable in|
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**Default Romanian Dataset: LOW-END**|3625|250|'low'|Romanian|Critically Low|No Effort|NO ❌|**BETA v0.0.1** or newer|
|**Default Romanian Dataset: MID-RANGE**|8242|500|'mid'|Romanian|Critically Low|No Effort|NO ❌|**BETA v0.0.1** or newer|
|**Default Romanian Dataset: HIGH-END**|11581|1000|'high'|Romanian|Critically Low|No Effort|NO ❌|**BETA v0.0.1** or newer|
|**High Quality, Very Low Quantity Romanian Dataset**|496|50|'high-quality-very-low-quantity'|Romanian|Very High|Very Low|NO ❌|**STABLE v0.1.1** or newer|
|**High Quality, Low Quantity Romanian Dataset**|874|100|'high-quality-low-quantity'|Romanian|High|Very Low|NO ❌|**EXPERIMENTAL v001** or newer|
|**Teacher for PyRomusa AI**|397|110|'pyromusa-ai-teacher'|Romanian|Very High|High|YES 👍|**STABLE v0.2.0** or newer|

_(Some values ​​in the `"Vocabulary"` and `"Number of examples"` columns may be approximate.)_

#### Explanation for Each Column

- _Dataset Name_ - **The dataset name will be written here so that each dataset is unique.**

- _Vocabulary_ - **This is where you will write the total number of different words in the dataset.** It is important for the chatbot to have a diverse vocabulary from different domains to talk about more things.

- _Number of examples_ - **This is where you will put the total number of input-output examples that the dataset has.** It is important to have a high number, because it is said that this way you have a better chance of answering more prompts correctly (theoretically speaking...).

- _Word to acces it_ - **Here we will put a recommended option to access the dataset in the `bot.prepared_datasets. ... ` function, putting it in `dataset_name` variable.** It is important to know how to access a specific dataset in your code.

- _Language_ - **This will be the language that most of the dataset examples are in**. It's important to understand what the chatbot is saying.

- _Naturalness_ - **This represents who the input/output examples  are made by and how.** Here only certain terms will be used, depending on each situation:

    - **No Effort** - The examples in the dataset are 100% AI-generated and not a single one is human-made.
    - **Critically Low** - The examples in the dataset are 99% generated with AI, but about 1% are human-made
    - **Very Low** - The examples in the dataset are 80% generated with AI, but about 20% are human-made
    - **Low** - The examples in the dataset are 60% generated with AI, but about 40% are human-made
    - **Balanced** - The examples in the dataset are 50% generated with AI, but about 50% are human-made
    - **High** - The examples in the dataset are 20% generated with AI, but about 80% are human-made
    - **Very High** - The examples in the dataset are 100% human-made, but probability some information in the examples in the dataset is not correct.
    - **Perfectly** - The examples in the dataset are 100% human-made, and also has verified information

        _(By the way: The datasets that are mostly human-made, the examples from them were added progressively, thus the chatbot "learns" from mistakes.)_
    
- _Focus on same questions_ - **Here you will find out how much focus was placed on the chatbot that has this dataset to recognize the same question, but written in a different form by the user.** It is important to know how much patience you need to have for the chatbot to understand what you are saying, so that it does not fallback or write something difficult to understand. Here you can find the following values:

    - **No Effort** - worst value
    - **Very Low**
    - **Low**
    - **Balanced**
    - **High**
    - **Very High** - best value

- _Planned to be updated_ - **This column will have only one of the 3 values: YES, NO or MAYBE.** This column shows whether the prepared dataset will be updated in the future. If YES, the dataset specifications vary depending on the version of `PyRomusa AI`.

- _Avaiable In_ - **Here you will find in which oldest version this dataset started appearing in.** It is important to know which version to look for in the `versions/` folder if you want to use a specific dataset.
---

## About **Reply Engines** 
**Did you know that you can change the logic in which the chatbot will generate a response?** Well, that's a new concept in the `STABLE 0.2.0` release!

**But why was this new concept added?** Well, it **was observed that with a changed logic for generating responses, the chatbot responds more chaotically, more stably, or more precisely to a certain length of the prompt**, so that's how the concept of engines was born: _to optimize the goal of your chatbot._

### Engines available in the latest version of `PyRomusa AI`:

|Engine Name|Advantages|Disadvantages|
|:---------:|:---------|:------------|
|  stable   |In general, it writes more correctly in terms of word order, and the chatbot's response is also much easier to read and understand.|High chances of not understanding an extremely short prompt (e.g. a word or three), even if it has it as an example in training, also returning a fairly easy fallback message.|
|  chaos    |Makes more of an effort to understand a message, so the chances of returning an automatic fallback message are lower.|In general, he writes some strange and quite difficult to understand messages, often not knowing what the chatbot meant. It can also write too many or too few words, thus compounding the difficulty of fully understanding what the chatbot meant.|


### Short tutorial/code: **How to use an engine of your choice?**

---

_By the way_: This is a complete tutorial. **If you are only interested in how to select the engine when you want to generate a response, then skip to step 5.**

---

1. First, import the Chatbot from PyRomusa AI

``` python
from PyRomusa_AI import Chatbot
```

2. Create an instance of the chatbot

``` python
bot = Chatbot(chatbot_name="test")
```

3. Add training examples or upload a prepared dataset

``` python
bot.trainer.add_data(
                    training_input_example= "...",
                    training_output_example= "..."
                    )

# AND / OR...

bot.prepared_datasets.romanian.load_prepared_dataset(
                                                    dataset_name="..."
                                                    )
```

4. Start the training

``` python
bot.trainer.start()
```

5. Generate the answer... **choosing the engine you want**
``` python
print(bot.reply_at(
    prompt="Hey Chatbot!",
    engine_name="chaos" # Here you write the name of the desired engine
))
```


---
## Contact us 📩🌐

Do you want to give us a new idea for functionality for `PyRomusa AI`, have you detected a bug in a particular version, want to ask us something, give us feedback, need help, a tutorial from `📁tutorials/` is not cleary or just want to say hello? Anything friendly message and/or about `PyRomusa AI` is welcome!

e-mail: pyromusa.ai@gmail.com

---

## More ➕

### 1. When will you be able to install the library with just `pip install PyRomusa_AI` from bash?

An exact date for this has not yet been decided, but it is planned for this to happen in the near future, when `PyRomusa AI` will evolve further and have a minimum community.

---

**Note:** Versions prior to `BETA 0.0.1` were initially released under the name `muri_ai`.
**The project has been renamed to `PyRomusa_AI` to avoid naming conflicts and for better branding.**