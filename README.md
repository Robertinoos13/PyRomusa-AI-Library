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
STABLE - v1.00.00
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

**Note:** Versions prior to `BETA 0.10.0` were initially released under the name `muri_ai`.
**The project has been renamed to `PyRomusa_AI` to avoid naming conflicts and for better branding.**