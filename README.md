# `PyRomusa AI` 🤖

**Have you ever imagined training your own chatbot that doesn't even have any existing vocabulary, 100% with your own examples type question-answer, without requiring very good hardware?** Well, `PyRomusa AI` will give you this possibility!

**`PyRomusa AI`** is a lightweight Python framework for creating simple AI chatbots with minimal code.



![PyRomusa AI logo](images/PyRomusa_AI_logo.png)

---
## Quick Navigation 🌐

This `📄README.md` file seems a bit long, right? 

Well, just click on the section (the blue text) below that interests you and you'll be taken directly there! 👇

- [Complete Code Example Using `PyRomusa AI`](#complete-code-example-using-pyromusa_ai)
    - Do you want to see what code using the `PyRomusa AI` library would look like or do you want some ready-to-copy-paste code to see how it works? Well, this is the section you should come to.

- [Why should I use `PyRomusa AI`? 🤔](#why-should-i-use-pyromusa-ai-)
    - Do you want a reason to use `PyRomusa AI` or still don't understand what `PyRomusa AI` is? You could find this information right here

- [How to download `PyRomusa AI` directly from GitHub?](#how-to-download-pyromusa-ai-directly-from-github)
    - Are you ready to install PyRomusa AI directly from GitHub, on your hardware, and use PyRomusa AI? Here's a tutorial on how to install it from scratch.
- [Key Features 🔑](#key-features-) 
    - Are you new and still don't know what you can do and what capabilities `PyRomusa AI` has? Discover what you can do with this and what capabilities `PyRomusa AI` has.

- [Repository Structure 📁](#repository-structure-)
    - Are you new at this repository? Learn a little about the structure of this repository to find what you need.

- [Version Types Explained](#version-types-explained)
    -  Here you will find several versions of `PyRomusa AI`, each placed in a specific category, depending on how stable it is, how much effort has been put into fixing bugs, and what the respective version was released for.

- [About Prepared Datasets 🗄️](#about-prepared-datasets-️)
    - Did you know that you can use ready-to-use training datasets to save time creating input-output examples of a chatbot from scratch? Find here all available datasets, their specifications, and a complete example script with loading a dataset.

- [About Reply Engines](#about-reply-engines)
    - Does your chatbot seem to not understand the prompt you wrote or is writing extremely unclearly? This can probably be solved by changing the engine. Click here if you want to learn more about these engines.

- [Contact me 📩🌐](#contact-me-)
    - Do you want to talk to the person that created this library called `PyRomusa AI`? Here you will find all the available possibilities to contact me!

- [More ➕](#more-) 
    - Still haven't found what you need? You'll probably find it here.

- [Credits ⭐](#credits-)
    - Curious about what libraries and frameworks were used to create PyRomusa AI? Here you will find the answer + the main purpose of each
    
- [Notes](#notes)
    - There are some small things you should consider. Come here if you want to know these important things

---

## Complete Code Example Using `PyRomusa AI`

```python
"""
This code works correctly with the following versions:
BETA - v0.0.2
STABLE - v0.1.0, v0.1.1, v0.2.0, v0.3.0, v0.4.0, v0.4.1, v0.4.2, v0.4.3, v0.5.0
EXPERIMENTAL - v001, v002, v003
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
## Why should I use `PyRomusa AI`? 🤔
### 1. Framework with a single goal: **creating chatbots from scratch**
- It is a framework optimized only for creating chatbots from scratch, with your own input-output training examples.
- It has functions specifically for creating a chatbot, without unnecessary functions

### 2. It is a small and new python framework
- Not much is known about this framework yet, and since it is a very young framework, it receives updates quite frequently. Any feedback and suggestions [sent via email or TikTok](#contact-me-) are welcome!

- It is not yet a framework that can be installed in the form of `pip install PyRomusa_AI` in the console, but it is planned to be able to install in this form when there is a minimum community and/or when it will be necessary to make the major update to the STABLE version v0.9.X

### 3. A fast framework
- The response generation time + training time in a single code run are generally much shorter than other major frameworks.

- **Want to see the real speed of the framework? Try the `🐍 benchmark.py` script**: It creates an instance of a chatbot, loads all available datasets, starts training, and responds to 10 prompts using the `modern` reply engine (works on PyRomusa AI STABLE v0.4.1 or newer).

### 4. A framework a little... different from others
- **`PyRomusa AI` comes with some more special concepts**: _[Reply Engines](#about-reply-engines) and [Prepared Datasets](#about-prepared-datasets-️)_
- It does not use some concepts from traditional AI, such as loss functions or hidden layers

### 5. Focused on being easy to learn and use
- The syntax of this framework has been made as easy and logical as possible.
- Even though [the learning resources for this framework](#1-what-methods-do-i-have-to-learn-to-use-pyromusa-ai), available in February 2026, are not very advanced and detailed, at least they are diversified directly by the creator.
---
## How to download `PyRomusa AI` directly from GitHub?

### **This can be done by 2 methods:**

---
### **a) The clasic method**

1. Make sure you have Python and pip installed (`PyRomusa AI` works with Python 3.8+).
2. Open a terminal on Windows, macOS, or Linux, open your command line or terminal.
3. Install `PyRomusa AI` directly from GitHub, writing this in your terminal:
``` bash
pip install git+https://github.com/Robertinoos13/PyRomusa-AI-Library.git#subdirectory=pyromusa-ai
```
> This command tells pip to clone the repository and install the package automatically. You don’t need to download anything manually.

**4. Test the installation**

Open Python in your terminal and try:
``` python
from pyromusa_ai import Chatbot

bot = Chatbot()
bot.trainer.show_number_of_examples()
```
>If no errors appear, PyRomusa AI is installed and ready to use.

>_(**How do you open Python in your terminal? Just type the word** `python` **before you type the python code**, then you have the option to type whatever Python code you want.)_

**5. Load a prepared dataset (optional):**
```
bot.prepared_datasets.romanian.load_prepared_dataset("low")
```

> This loads a Romanian dataset into your chatbot for training or testing.

---

### **b) The manual method**
Did you know that to install older versions of PyRomusa AI, the most stable installation method is this? **If you want to install older versions, then trust this method.**

1. Go to one of these folders: `📁 all versions/` or `📁 pyromusa-ai`
2. If you chose to go to folder `📁 all versions/`, then select a version type, the exact version, and look for file `🐍PyRomusa_AI.py`. If you went the other way, look for the `🐍core.py` file.
3. Once you've found one of the Python files, install it or copy all of its contents to a Python file you created on your hardware.

    > By the way, if you made it to step 3, make sure the Python file I told you about is in the same folder as the python file where you will use the `PyRomusa AI` functionalities. We will talk more about this in step 4.

4. In order to use `PyRomusa AI` in your code, the 2 Python files must be in the same folder, with a structure something like this:
    ```
    |- 📁Your Folder/
    |----- 🐍PyRomusa_AI.py
    |----- 🐍you_code.py
    |----- 📁Datasets/
    |--------- 🐍other python files
    ```

    Where:
    |Name|Description|
    |:--:|:----------|
    |`📁Your Folder/`|The folder where your Python code should be located where you want to use `PyRomusa AI` + the main framework code|
    |`🐍PyRomusa_AI.py`|The main code of the `PyRomusa AI` framework|
    |`🐍you_code.py`|Your code, where you will use `PyRomusa AI`|
    |`📁Datasets/`|This is a folder with several optional Python files that `🐍PyRomusa_AI.py` needs to function fully and smoothly.|

    > Did you know that `PyRomusa AI` uses several optional Python files that it needs to function fully and error-free? Well, they are found in the repository in a folder called `Datasets/`

---
## Key Features 🔑
- Create a chatbot in just a few lines of Python  
- Simple training process (no heavy frameworks involved)  
- Multiple version types: Stable, Beta, and Experimental  
- Beginner-friendly and easy to understand  
- No high-end GPU required

---

## Repository Structure 📁
All versions of `PyRomusa AI` from all time are stored inside the `📁 all versions/` folder.

```
|-📁 all versions/
|
|----📁 BETA versions/ 
|--------📁 _PyRomusa_AI_ - v0.0.X
|
|----📁 EXPERIMENTAL versions/
|--------📁 _PyRomusa_AI_ - vXYZ
|
|----📁 STABLE versions/ 
|--------📁 _PyRomusa_AI_ - v0.X.Y
```



Each version folder contains:
- A full `🐍PyRomusa_AI.py` file 
- A dedicated `📄README.md` for that version  

---
`📁 pyromusa-ai` - This is the newest stable version of `PyRomusa AI`. Its structure is optimized so that you can install it with `pip install` from your terminal. [Click on this text to learn how](#a-the-clasic-method)

`📁 tutorials/` - This is a folder where all sorts of tutorials will be written to use the library.

`📁 important updates/` - This folder will provide a more detailed description of all the important updates that `PyRomusa AI` has had so far.

`📁 images/` - In this folder you will find all the images that the repository usually uses in README.md files.

`🐍 benchmark.py` - A stress-free, ready-made script that uses `PyRomusa AI` to test the runtime on your hardware.

`📁 ISSUE_TEMPLATE` - Do you want a standard template to start a discussion about a bug or a new feature? Then you will find them in this folder

`📄 CONTRIBUTING.md` - A file where you can find details on how to contribute to `PyRomusa AI`

`📄 CODE_OF_CONDUCT.md` - Some rules you should respect if you want to join the community

`📄 SECURITY.md` - Here you will find out what you should do if you are using `PyRomusa AI`, but the output shows something that shouldn't be happening.

`📄 PULL_REQUEST_TEMPLATE.md` - What should your pull request describe and what should you check before making it public? Find out here

---

## Version Types Explained
As this repository has various versions of `PyRomusa AI` that are older, newer, or more buggy, they have been grouped into 3 categories, placed in the `📁 all versions/` folder:

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

## About **Prepared Datasets** 🗄️

Did you know that from `PyRomusa AI` you can load a ready-made training dataset to the model? Well, here's an example below:
``` python
from PyRomusa_AI import Chatbot

# 1. Create your chatbot
bot = Chatbot(chatbot_name="MyChatbot")

# 2. Load a prepared dataset (in this example, you load the smallest default dataset in Romanian)
bot.prepared_datasets.romanian.load_prepared_dataset(dataset_name="low")

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
|**Teacher for PyRomusa AI**|_397_ - _784_|_110_ - _250_|'pyromusa-ai-teacher'|Romanian|Very High|High|YES 👍|**STABLE v0.2.0** or newer|
|**Default English Dataset: LOW-END**|949|250|'low'|English|No Effort|Balanced|NO ❌|**STABLE v0.4.1** or newer|
|**Default English Dataset: MID-RANGE**|1713|500|'mid'|English|No Effort|Balanced|NO ❌|**STABLE v0.4.1** or newer|
|**Default English Dataset: HIGH-END**|3100|1000|'high'|English|No Effort|Balanced|NO ❌|**STABLE v0.4.1** or newer|

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
|  `stable` |In general, it writes more correctly in terms of word order, and the chatbot's response is also much easier to read and understand.|High chances of not understanding an extremely short prompt (e.g. a word or two), even if it has it as an example in training, also returning a fairly easy fallback message.|
|  `chaos`  |Makes more of an effort to understand a message, so the chances of returning an automatic fallback message are lower.|In general, he writes some strange and quite difficult to understand messages, often not knowing what the chatbot meant. It can also write too many or too few words, thus compounding the difficulty of fully understanding what the chatbot meant.|
| `modern`  |It is the first engine based on NumPy. It doesn't matter if you write letters with diacritics or accents or not, the chatbot will still understand. It can now return a generated answer to a one-word prompt, without returning a fallback message, as we encounter, completely the opposite, in the `stable` engine.|In general, the response generation time is longer than in other available engines (`chaos`, `stable`).|


### Short tutorial/code: **How to use an engine of your choice?**

---

_By the way_: This is a complete tutorial. **If you are only interested in how to select the engine when you want to generate a response, then skip to step 5.**

---
``` python
# 1. First, import the Chatbot from PyRomusa AI
from PyRomusa_AI import Chatbot


# 2. Create an instance of the chatbot
bot = Chatbot(chatbot_name="test")


# 3. Add training examples or upload a prepared dataset
bot.trainer.add_data(
                    training_input_example= "...",
                    training_output_example= "..."
                    )

        # AND / OR...

bot.prepared_datasets.romanian.load_prepared_dataset(
                                                    dataset_name="..."
                                                    )
# 4. Start the training
bot.trainer.start()

# 5. Generate the answer... **choosing the engine you want**
print(bot.reply_at(
    prompt="Hey Chatbot!",
    engine_name="chaos" # Here you write the name of the desired engine
))
```


---
## Contact me 📩🌐

Do you want to give me a new idea for functionality for `PyRomusa AI`, have you detected a bug in a particular version, want to ask me something, give me feedback, need help, a tutorial from `📁tutorials/` is not cleary or just want to say hello? Anything friendly message and/or about `PyRomusa AI` is welcome!

- e-mail: pyromusa.ai@gmail.com

- TikTok: [@pyromusa_ai](https://www.tiktok.com/@pyromusa_ai?is_from_webapp=1&sender_device=pc)

---

## More ➕

### 1. What methods do I have to learn to use `PyRomusa AI`?

At the moment _(February 19, 2026)_, these PyRomusa AI learning options are quite limited, but you have the following methods:

1. Find random codes through this repository
    - In almost every README.md there is a piece of code where `PyRomusa AI` is used. Look at these and get inspired

2. Watch videos about `PyRomusa AI`, specifically on the TikTok account [@pyromusa_ai](https://www.tiktok.com/@pyromusa_ai?is_from_webapp=1&sender_device=pc)
    - Sometimes, videos are posted on this TikTok account just about `PyRomusa AI`: from updates and little jokes to code and tutorials. Scroll through the videos here and find what you want.

3. Look in the `📁 tutorials/` folder in this repository

    - This folder, at the moment, does not have a code tutorial, but only a few text guides to solve problems like 'Why can't I load a prepared dataset?' or 'How do I setup PyRomusa AI in my code?', but it is planned to include code tutorials here in the future.

4. Use the prepared dataset 'Teacher for PyRomusa AI'

    - Yes, you can load this prepared dataset for your chatbot in your code, and then ask it questions. This dataset has input-output examples, specifically designed to answer your questions about PyRomusa AI. Indeed, it can't answer every question because of the poor vocabulary specifications and the number of examples, but it can answer basic questions. (By the way, you need to know Romanian to use it)


5. Install `PyRomusa AI` & Run the code:
```python
from PyRomusa_AI import Chatbot

# Create a chatbot
bot = Chatbot()

# Get help
bot.helper.how_to_start()
```
---
## **Credits ⭐**

PyRomusa AI uses several other external Python libraries to function properly and completely. In this table below, you will find each external library used and its most important purpose in `PyRomusa AI`:

|Library name|Objective|Name/Link of the repo in GitHub|
|:---:|:---:|:---:|
|`numpy`|The logic behind the 'modern' reply engine|[numpy](https://github.com/numpy/numpy)|
|`pandas`|To create tables (dataframes) for some functions in `bot.helper. ...`|[pandas](https://github.com/pandas-dev/pandas)|
|`pyrospeak`|For talking chatbots (TTS transformation)|[PyroSpeak-Library](https://github.com/Robertinoos13/PyroSpeak-Library)|

<br><br>

Thank you for creating these Python frameworks/libraries 🙏

---

## **Notes:** 
- Versions prior to `BETA 0.0.1` were initially released under the name `muri_ai`.
**The project has been renamed to `PyRomusa_AI` to avoid naming conflicts and for better branding.**

- Do you notice that the codes in this repository that use `PyRomusa AI`, you often find `from PyRomusa_AI import Chatbot`, and sometimes you also find `from pyromusa_ai import Chatbot`? **Well, know that if you install `PyRomusa AI` via `pip install ...`, in your code you will use `pyromusa_ai`, AND if you install it manually from the repository and do not change its name, then you will use `PyRomusa_AI`**

- **Some information in this repository may be incorrect or outdated.** Please manually verify the information you want before taking it 100% into account. If you do find incorrect or outdated information, please [contact me.](#contact-me-)

---

<br>

Did you find the functionalities interesting, did it help you a lot in a project of yours, or do you think `PyRomusa AI` has potential? Then leave a ⭐ so I know this information, so I know what you think about `PyRomusa AI` at the moment.