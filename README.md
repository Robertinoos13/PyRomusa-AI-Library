# PyRomusa_AI 🤖

**PyRomusa_AI** is a lightweight Python library for creating simple AI chatbots with minimal code.  
It is designed for learning purposes, rapid prototyping, and experimentation with basic AI concepts.

---


## Key Features 🔑
- Create a chatbot in just a few lines of Python  
- Simple training process (no heavy frameworks involved)  
- Multiple version types: Stable, Beta, and Experimental  
- Beginner-friendly and easy to understand  

---

## Repository Structure 📁
All versions of the library are stored inside the `versions/` folder.

`versions/`
- `BETA versions/` - _PyRomusa_AI_ - 0.X.0
- `EXPERIMENTAL versions/` - _PyRomusa_AI_ - 0.0.X
- `STABLE versions/` - _PyRomusa_AI_ - X.Y.Z




Each version folder contains:
- A full `PyRomusa_AI.py` file  
- A dedicated `README.md` for that version  

---

`tutorials/` - This is a folder where all sorts of tutorials will be written to use the library.


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
BETA - v0.11.0
STABLE - v1.00.00, v1.00.1
EXPERIMENTAL - (no versions available at the moment)
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
## About Prepared Datasets 🗄️

Did you know that from PyRomusa AI you can load a ready-made training dataset to the model? Well, here's an example below:
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

|Dataset Name|Vocabulary|Number of examples|Word to acces it|Language|Quality|
|---|:---:|:---:|:---:|:---:|:---:|
|**Default Romanian Dataset: LOW-END**|3625|250|'low'|Romanian|Critically Low|
|**Default Romanian Dataset: MID-RANGE**|8242|500|'mid'|Romanian|Critically Low|
|**Default Romanian Dataset: HIGH-END**|11581|1000|'high'|Romanian|Critically Low|
|**High Quality, Very Low Quantity Romanian Dataset**|496|50|'high-quality-very-low-quantity'|Romanian|Very High|

_(Some values ​​in the `"Vocabulary"` and `"Number of examples"` columns may be approximate.)_

#### Explanation for Each Column

- _Dataset Name_ - **The dataset name will be written here so that each dataset is unique.**

- _Vocabulary_ - **This is where you will write the total number of different words in the dataset.** It is important for the chatbot to have a diverse vocabulary from different domains to talk about more things.

- _Number of examples_ - **This is where you will put the total number of input-output examples that the dataset has.** It is important to have a high number, because it is said that this way you have a better chance of answering more prompts correctly (theoretically speaking...).

- _Word to acces it_ - **Here we will put a recommended option to access the dataset in the `bot.prepared_datasets. ... ` function, putting it in `dataset_name` variable.** It is important to know how to access a specific dataset in your code.

- _Language_ - **This will be the language that most of the dataset examples are in**. It's important to understand what the chatbot is saying.

- _Quality_ - **This represents who the input/output examples  are made by and how.** Here only certain terms will be used, depending on each situation:

    - **No Effort** - The examples in the dataset are 100% AI-generated and not a single one is human-made.
    - **Critically Low** - The examples in the dataset are 99% generated with AI, but about 1% are human-made
    - **Very Low** - The examples in the dataset are 80% generated with AI, but about 20% are human-made
    - **Low** - The examples in the dataset are 60% generated with AI, but about 40% are human-made
    - **Balanced** - The examples in the dataset are 50% generated with AI, but about 50% are human-made
    - **High** - The examples in the dataset are 20% generated with AI, but about 80% are human-made
    - **Very High** - The examples in the dataset are 100% human-made, but probability some information in the examples in the dataset is not correct.
    - **Perfectly** - The examples in the dataset are 100% human-made, and also has verified information

    By the way: The datasets that are mostly human-made, the examples from them were added progressively, thus the chatbot "learns" from mistakes.
---

**Note:** Versions prior to `BETA 0.10.0` were initially released under the name `muri_ai`.
**The project has been renamed to `PyRomusa_AI` to avoid naming conflicts and for better branding.**