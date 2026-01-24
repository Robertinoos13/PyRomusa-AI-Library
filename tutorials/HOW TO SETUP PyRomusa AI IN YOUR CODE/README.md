# ❓ How to setup PyRomusa AI in your code? ❓

**NOTE:** This is an explanatory markdown file in the form of a text tutorial to answer the question you chose (_How to setup PyRomusa AI in your code?_).

---

## 1. Select the library version you want from the PyRomusa AI library repository on GitHub.

To select the library version, **you need to browse the** `versions` **folder and select a version type** (selecting a folder):
- `BETA versions` - Here you will find versions that are probably not perfect from a functional point of view. You have the chance to find bugs or errors of any kind here.

- `EXPERIMENTAL versions` - The versions in this folder are the most unstable of all. All versions that appear here are created with a focus on testing new ideas, functions or logic with radical changes. For experimental versions, there is not much focus on fixing bugs, only the bare minimum for a functional new concept.

- `STABLE versions` - Here you will find the most stable versions of all. Here, you will rarely encounter bugs or other errors of any kind. In the long run, these are the most recommended versions.


Once you've selected the version type, find the more specific version you want to use.

>Want a version recommendation? Try this tutorial with the newest version in STABLE (e.g. v1.00.1 on January 25, 2026)

---

## 2. Install or copy paste all the library code into a Python file (.py)

Once you have selected the PyRomusa AI version (that is a folder), **go to the only Python code in that folder, which is called 'PyRomusa_AI.py'. Access its code** and you have 2 options:

a) **Copy the code:**

1. Copy all the code from that script (Ctrl + C)
2. Go to your IDE and create a folder
3. In that folder you created, create 2 more Python scripts, in which:
``` 
    Your Folder/

        *script 1* - Here you paste (Ctrl + V) the version code of the     
        PyRomusa AI library that you selected in the previous step

        *script 2* - Here you will use the PyRomusa AI functions you need
```

Real example (with names):

        AI Library Folder/

            PyRomusa_AI.py
            practice_PyRomusa.py

---

b) **Install the library code directly:**

1. Install the script directly from GitHub
2. Most likely, your browser places the installed files in a folder called 'Downloads' or something similar. Go there, select the downloaded file with a single click and press the key combination Ctrl + X.
3. Put it in a new folder (with Ctrl + V) and open it in your IDE
4. Also, put your Python file (i.e. in the new folder from step 3) where you want to use PyRomusa AI.

---

## 3. Use PyRomusa AI directly in your code!
This is the final step, where you just write your code in script 2 (the script where you will use PyRomusa AI technologies). Run the code below. If it works, you don't need to do anything else, just take advantage of PyRomusa AI's capabilities. Enjoy!

``` python
"""
By the way, for the script to work 100%, make sure that the file where you pasted the PyRomusa AI library code is exactly named 'PyRomusa_AI'.
"""

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

**tutorial last updated:** 24th January 2026

_(Remember: the more outdated the file, the greater the chances that this tutorial will not be 100% functional.)_