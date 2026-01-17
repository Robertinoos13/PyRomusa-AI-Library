# muri_ai 🤖

**muri_ai** is a lightweight Python library for creating simple AI chatbots with minimal code.  
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
- `BETA versions/` - muri_ai - 0.X.0
- `EXPERIMENTAL versions/` - muri_ai 0.0.X
- `STABLE versions/` - muri_ai - X.Y.Z


Each version folder contains:
- A full `muri_ai.py` file  
- A dedicated `README.md` for that version  

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

## Complete Code Example Using muri_ai

```python
"""
This code works correctly with the following versions:
BETA - 0.11.0
STABLE - (no versions available at the moment)
EXPERIMENTAL - (no versions available at the moment)
"""

from muri_ai import Chatbot

# Create a chatbot named "MuriBot"
bot = Chatbot(chatbot_name="MuriBot")

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


