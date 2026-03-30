"""
PyRomusa AI benchmark:
- Load all available prepared datasets 
- Respond to 10 different prompts using the most advanced and powerful Reply Engine: modern

NOTES:
- This code was made and put in this repository to test the runtime on your hardware, where the most stressful code is run, where the PyRomusa AI framework is used.
- This benchmark works 100% with PyRomusa AI version: STABLE v0.4.1 or newer
- The chatbot's responses can be completely wrong, illogical, or strange. Ignore them, the more important thing is the runtime of this code.
- This code can be modified if you wish (e.g. add more training data with the bot.trainer.add_data() function, change the reply engine from 'modern' to 'stable', remove the loading of a specific prepared dataset, etc.)
"""

"""
ModuleError, even if you installed PyRomusa AI via 'pip install ...'?
Try this line of code instead of the one below (lowercase):

from pyromusa_ai import Chatbot
"""

from PyRomusa_AI import Chatbot


bot = Chatbot(chatbot_name="bechmark bot")

# Loading all Romanian prepared datasets
bot.prepared_datasets.romanian.load_prepared_dataset('low')
bot.prepared_datasets.romanian.load_prepared_dataset('mid')
bot.prepared_datasets.romanian.load_prepared_dataset('high')
bot.prepared_datasets.romanian.load_prepared_dataset('pyromusa-ai-teacher')
bot.prepared_datasets.romanian.load_prepared_dataset('high-quality-very-low-quantity')
bot.prepared_datasets.romanian.load_prepared_dataset('high-quality-low-quantity')

# Loading all English prepared datasets
bot.prepared_datasets.english.load_prepared_dataset('low')
bot.prepared_datasets.english.load_prepared_dataset('mid')
bot.prepared_datasets.english.load_prepared_dataset('high')

# Starting chatbot training
bot.trainer.start()

# List of all the prompts that our chatbot will respond to
prompts = [
    "Salut, cine ești?",
    "Hello, who are you?",
    "Pe ce planetă suntem?",
    "What is Terra?",
    "Ce este inteligența emoțională?",
    "You have a name?",
    "Vrei să fii prietenul meu?",
    "Do you want to be my friend",
    "Câte planete avem în sistemul solar?",
    "Ce e PyRomusa AI?",
    "What is PyRomusa AI?",
]

# This is where the chatbot starts responding to each prompt written in the 'prompts' list.
for input in prompts:
    print(
    bot.reply_at(
        prompt=input,
        engine_name="modern" # Want even more speed? 
                             # Change the reply engine from 'modern' to 'stable' or 'chaos'
    )
    )
