"""
(Official code example using PyRomusa AI from 'PyRomusa-AI-Library' repository on github)

- SCRIPT OBJECTIVE:              Write your own training examples and test the LLM with a prompt
- SUCESSFULLY TESTED IN VERSION: v0.9.1

NOTE:
- Too little data can lead to the chatbot learning the structure of the dataset instead of its content.

"""

from pyromusa_ai import RealChatbot

# --- We create an LLM instance with default settings ---
bot = RealChatbot()

# --- Add your own question-and-answer examples like this: ---
# (first: input example | second: output example)
bot.trainer.add_data("Write the number backwards: 20268", "86202")
bot.trainer.add_data("Count from 1 to 10", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
bot.trainer.add_data("The opposite of right?", "left")
bot.trainer.add_data("The opposite of left?", "right")
bot.trainer.add_data("The opposite of girl?", "boy")
bot.trainer.add_data("The opposite of boy?", "girl")
# ...

# --- Let's start training the chatbot ---
bot.trainer.start()

# Enter here your prompt
PROMPT = "Count from 1 to 10"

# Generate the answer
print(bot.reply_at(prompt=PROMPT))
