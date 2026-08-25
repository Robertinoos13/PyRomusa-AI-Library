"""
(Official code example using PyRomusa AI from 'PyRomusa-AI-Library' repository on github)

- SCRIPT OBJECTIVE:              Direct comparison: How does a chatbot trained with word-level vs char-level, trained on the same dataset, respond?
- SUCESSFULLY TESTED IN VERSION: v0.10.0

NOTE:
- The word-level chatbot seems better in practice because it doesn't have to write words letter by letter, 
but directly generates the whole word, meaning more orthographically correct speech.

"""

from pyromusa_ai import RealChatbot

# --- 1. We create 2 chatbots with modified tokenizer ---
word_bot = RealChatbot(tokenizer_type="word-level")
char_bot = RealChatbot(tokenizer_type="char-level")

# --- 2. Loading the largest English-language prepared dataset available for both chatbots ---
word_bot.prepared_datasets.english.load_prepared_dataset("high")
char_bot.prepared_datasets.english.load_prepared_dataset("high")

# --- 3. Starting training to train our chatbots ---
print("\nTraining the word level chatbot...")
word_bot.trainer.start(epochs=5, show_loss_every_x_epochs=1)
print("\nTraining the char level chatbot...")
char_bot.trainer.start(epochs=5, show_loss_every_x_epochs=1)

# --- 4. Conversational loop ---
while True:
    print("\n")

    user_input = input("USER: ")

    if user_input.lower() in ("pa", "bb", "exit"): # NOTE: Write one of this words on user_input to exit from conversational loop
        break

    else:
        print("WORD-BOT: " + str(word_bot.reply_at(
            prompt=user_input,
            temperature=0.55
        )))

        print("CHAR-BOT: " + str(char_bot.reply_at(
            prompt=user_input,
            temperature=0.55
        )))
