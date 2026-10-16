# ❓ How to setup PyRomusa AI in your code? ❓

**NOTE:** This is an explanatory markdown file in the form of a text tutorial to answer the question you chose (_How to setup PyRomusa AI in your code?_).

---

## 1. Install with a command or copy paste all the library code into a Python file (.py)

### **This can be done by 3 methods:**

---
### **a) The clasic method** _(install with a command)_

1. Open a terminal on Windows, macOS, or Linux, open your command line (`Win + R`, then write `cmd` and press `Enter`) or terminal.

2. Install `PyRomusa AI` directly from `PyPI`, writing this in your terminal:
``` bash
pip install pyromusa-ai
```
**3. Test the installation**

Try to run this code:
``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

bot.prepared_datasets.romanian.load_prepared_dataset("low")
bot.trainer.show_number_of_examples()
```
>If no errors appear, PyRomusa AI is installed and ready to use.

---

### **b) The GitHub method**  _(install with a command)_

1. Make sure you have Python and pip installed (`PyRomusa AI` works with Python 3.10+).
2. Open a terminal on Windows, macOS, or Linux, open your command line or terminal.
3. Install `PyRomusa AI` directly from GitHub, writing this in your terminal:
``` bash
pip install git+https://github.com/Robertinoos13/PyRomusa-AI-Library.git#subdirectory=src
```
> This command tells pip to clone the repository and install the package automatically. You don’t need to download anything manually.

**4. Test the installation**

Try to run this code:
``` python
from pyromusa_ai import Chatbot

bot = Chatbot()

bot.prepared_datasets.romanian.load_prepared_dataset("low")
bot.trainer.show_number_of_examples()
```
>If no errors appear, PyRomusa AI is installed and ready to use.

---

### **c) The manual method** _(copy-paste all necesarry content)_
Did you know that to install older versions of PyRomusa AI, the most stable installation method is this? **If you want to install older versions, then trust this method.**

1. Go to one of these folders: `📁 all versions/` or `📁 src/`
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
    |----- 📁Reply_Engines/
    |--------- 🐍other python files
    ```

    Where:
    |Name|Description|
    |:--:|:----------|
    |`📁Your Folder/`|The folder where your Python code should be located where you want to use `PyRomusa AI` + the main framework code|
    |`🐍PyRomusa_AI.py`|The main code of the `PyRomusa AI` framework|
    |`🐍you_code.py`|Your code, where you will use `PyRomusa AI`|
    |`📁Datasets/`|This is a folder with several optional Python files that `🐍PyRomusa_AI.py` needs to function fully.|
    |`📁Reply_Engines/`|The folder and its contents, from v0.7.0, are very important for generating responses based on prompts. This is a required folder.|

    > Did you know that `PyRomusa AI` uses several optional Python files that it needs to function fully and error-free? Well, they are found in the repository in a folder called `Datasets/`

---

## 2. Use `PyRomusa AI` directly in your code!
This is the final step, where you just write your code in script 2 _(the script where you will use PyRomusa AI technologies)_. Run the code below. If it works, you don't need to do anything else, just take advantage of PyRomusa AI's capabilities. Enjoy!

``` python
from pyromusa_ai import Chatbot

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

**tutorial last updated:** 16th Octomber 2026

_(Remember: the more outdated the file, the greater the chances that this tutorial will not be 100% functional.)_