# ❓ Why don't work to load a dataset for my chatbot in my code? ❓

**NOTE:** This is an explanatory markdown file in the form of a text tutorial to answer the question you chose (_Why don't work to load a dataset for my chatbot in my code?_).

---

## First of all, we need to know that there can be several main reasons, including:


### a) You modified the source code
It also happens that we, humans, do things in the past that we no longer remember at the moment.

Now, you could:
1. Go to the `all versions/` folder from this repository
2. Reinstall your respective version of `PyRomusa AI` to bring your code back to 'factory settings', replacing the old code with the new one.

---

### b) You tried a newer version of PyRomusa AI from the repository
If you have installed EXPERIMENTAL version `v001` or newer, **please know that from this version the main code of the PyRomusa AI library has begun to be separated from the code of the prepared datasets**, thus organizing it like this:

---

`📁PyRomusa_AI - vX.Y.Z/` — The main folder containing everything for that version of the library (full library code + README.md)

 - `📄README.md` — Documentation for this specific version 

- `📁PyRomusa_AI/` — The secondary folder, which only has all the code that contributes to the 100% functional PyRomusa AI

    - `🐍PyRomusa_AI.py` — **PyRomusa AI library main code** of this version  

    - `📁Datasets/` - Folder with some optional code for the main library code (`🐍PyRomusa_AI.py`) for ready-made data to train your chatbot

        - more Python files **with prepared datasets code**...

---

**And what is the conclusion to point b)?**

- You most likely also did not install the `📁Datasets/` folder, which is important if you want to use ready-made training data _(prepared datasets)_.

- You probably didn't follow the exact order of the folder, especially the part with the most important files (`🐍PyRomusa_AI.py` + everything contained in `📁Datasets/`).

- Another possible minor mistake would be that you changed the name of the `📁Datasets/` folder **AND/OR** changed the names of the Python files in `📁Datasets/`

**Recommendation:**
My recommendation is to install the important Python files (`🐍PyRomusa_AI.py` + all files from `📁Datasets/`) and manually arrange them in your IDE/computer exactly as you see them in this repository (same names, same structure):

---

- `📁PyRomusa_AI/` — These 2 things should be part of the same folder if you don't want to modify an `import` from `🐍PyRomusa_AI.py` in a more complicated way.

    - `🐍my_script.py` - This is a file added by you, this is the script where you need functions from `🐍PyRomusa_AI.py`

    - `🐍PyRomusa_AI.py` — **PyRomusa AI library main code** of this version  

    - `📁Datasets/` - Folder with some optional code for the main library code (`🐍PyRomusa_AI.py`) for ready-made data to train your chatbot

        - more Python files **with prepared datasets code _(for this files you need to fix your problem)_**...

---
### c) Do you get a module error when trying to load a dataset?

Do you have this error?
```
MINOR ERROR: Could not import dataset '...' module. Reason: attempted relative import with no known parent package
```

Yes, this error is specific to those who have manually installed the project files, even if you followed the correct structure.

To resolve this error, you need to follow a few steps:
1. Go to the project's main file (named `core.py` or `PyRomusa_AI.py`, depending on where you installed it)

2. Locate the `Datasets()` object within the type of chatbot you are using (`RealChatbot()` or `Chatbot()`)

3. Find the prepared dataset you want to use and modify this line:
    ``` python
    from .Datasets import ...
    ```
    with:

    ``` python
    from Datasets import ...
    ```

---
### d) Maybe there is even a version where you can't load a prepared dataset?

It's possible, but the chances are low, because in each version the datasets you have available for training a chatbot have been uploaded to test each function before the official publication of the version on GitHub.

If you actually encounter versions where you actually have this problem, please let us know!

> Until then, try using PyRomusa AI, but a different version


---
### e) Try the `pip` official version

Maybe you’re still using the old, 100% manual method for installing files—unaware that `PyRomusa AI` can now be installed much more easily via `pip install ...`? Well, press the `Win + R` key combination, type `cmd`, and run this command:

``` bash
pip install pyromusa-ai
```

Importing it into your Python code will look something like this:

``` python
import pyromusa_ai
```

This would be the most stable method at the moment. This way, you can use the prepared datasets without any issues (generally speaking).

---

### f) Did you find out that you actually have another problem?

If you have another problem, describe it in as much detail as possible to pyromusa.ai@gmail.com, also providing minimal details such as:
- On which version did you encounter the problem?
- What code did you write exactly (copy-paste here)?
- What appears in the console when you run your code?

---


**tutorial last updated:** 20th Octomber 2026

_(Remember: the more outdated the file, the greater the chances that this tutorial will not be 100% functional.)_