"""
(Official code example using PyRomusa AI from 'PyRomusa-AI-Library' repository on github)

- SCRIPT OBJECTIVE:              Loading a prepared dataset in English and immediately testing the chatbot after training
- SUCESSFULLY TESTED IN VERSION: v0.9.1

NOTE:
- The AI ​​model, being trained on only 1K Q&A examples and its architecture being very small, it is normal not to understand what it says

"""

from pyromusa_ai import RealChatbot

# --- 1. Create a RealChatbot instance (LLM) ---
bot = RealChatbot(
    d_model=64,
    num_heads=8,
    num_layers=4,
    max_len=512
)

# --- 2. Loading the largest English-language prepared dataset available ---
bot.prepared_datasets.english.load_prepared_dataset("high")

# --- 3. Starting training to train our chatbot ---
bot.trainer.start(epochs=5, show_loss_every_x_epochs=1)

# --- 4. Conversational loop ---
while True:

    user_input = input("USER: ")

    if user_input.lower() in ("pa", "bb", "exit"):
        break

    else:
        print("BOT: " + str(bot.reply_at(
            prompt=user_input,
            temperature=0.55 # higher temperature = more chaos
        )))