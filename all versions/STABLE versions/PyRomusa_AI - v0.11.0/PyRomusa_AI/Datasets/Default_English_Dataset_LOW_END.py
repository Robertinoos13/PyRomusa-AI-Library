def load_dataset(bot_instance):
    # --- Identity and Greetings ---
    bot_instance.trainer.add_data('Hi', 'Hello! I am your AI assistant. How can I help you today?')
    bot_instance.trainer.add_data('Hello there', 'Hello! I am your AI assistant. How can I help you today?')
    bot_instance.trainer.add_data('Hey', 'Hello! I am your AI assistant. How can I help you today?')
    bot_instance.trainer.add_data('Good morning', 'Hello! I am your AI assistant. How can I help you today?')
    bot_instance.trainer.add_data('Greetings', 'Hello! I am your AI assistant. How can I help you today?')

    bot_instance.trainer.add_data('Who are you?', 'I am a helpful AI chatbot designed to assist you with information, coding, and creative tasks.')
    bot_instance.trainer.add_data('What is your name?', 'I am a helpful AI chatbot designed to assist you with information, coding, and creative tasks.')
    bot_instance.trainer.add_data('Tell me about yourself', 'I am a helpful AI chatbot designed to assist you with information, coding, and creative tasks.')
    bot_instance.trainer.add_data('What are you?', 'I am a helpful AI chatbot designed to assist you with information, coding, and creative tasks.')
    bot_instance.trainer.add_data('Introduce yourself', 'I am a helpful AI chatbot designed to assist you with information, coding, and creative tasks.')

# --- Capabilities ---
    bot_instance.trainer.add_data('What can you do?', 'I can answer questions, write code, provide advice, and help you brainstorm new ideas.')
    bot_instance.trainer.add_data('How can you help me?', 'I can answer questions, write code, provide advice, and help you brainstorm new ideas.')
    bot_instance.trainer.add_data('What are your features?', 'I can answer questions, write code, provide advice, and help you brainstorm new ideas.')
    bot_instance.trainer.add_data('List your skills', 'I can answer questions, write code, provide advice, and help you brainstorm new ideas.')
    bot_instance.trainer.add_data('Give me some tasks you can handle', 'I can answer questions, write code, provide advice, and help you brainstorm new ideas.')

# --- Programming (Python) ---
    bot_instance.trainer.add_data('What is Python?', 'Python is a high-level, interpreted programming language known for its readability and versatility.')
    bot_instance.trainer.add_data('Explain Python language', 'Python is a high-level, interpreted programming language known for its readability and versatility.')
    bot_instance.trainer.add_data('Is Python a coding language?', 'Python is a high-level, interpreted programming language known for its readability and versatility.')
    bot_instance.trainer.add_data('Define Python in programming', 'Python is a high-level, interpreted programming language known for its readability and versatility.')
    bot_instance.trainer.add_data('Can you tell me about Python?', 'Python is a high-level, interpreted programming language known for its readability and versatility.')

# --- Programming (Loops) ---
    bot_instance.trainer.add_data('What is a loop?', 'A loop is a sequence of instructions that is continually repeated until a certain condition is reached.')
    bot_instance.trainer.add_data('How do loops work?', 'A loop is a sequence of instructions that is continually repeated until a certain condition is reached.')
    bot_instance.trainer.add_data('Explain iteration in code', 'A loop is a sequence of instructions that is continually repeated until a certain condition is reached.')
    bot_instance.trainer.add_data('Why use a for loop?', 'A loop is a sequence of instructions that is continually repeated until a certain condition is reached.')
    bot_instance.trainer.add_data('Describe coding loops', 'A loop is a sequence of instructions that is continually repeated until a certain condition is reached.')

# --- General Knowledge (Earth) ---
    bot_instance.trainer.add_data('What is the shape of Earth?', 'Earth is an oblate spheroid, meaning it is mostly spherical but slightly flattened at the poles.')
    bot_instance.trainer.add_data('Is the Earth round?', 'Earth is an oblate spheroid, meaning it is mostly spherical but slightly flattened at the poles.')
    bot_instance.trainer.add_data("Describe Earth's shape", 'Earth is an oblate spheroid, meaning it is mostly spherical but slightly flattened at the poles.')
    bot_instance.trainer.add_data("Tell me about Earth's geometry", 'Earth is an oblate spheroid, meaning it is mostly spherical but slightly flattened at the poles.')
    bot_instance.trainer.add_data('What does the planet look like?', 'Earth is an oblate spheroid, meaning it is mostly spherical but slightly flattened at the poles.')

# --- General Knowledge (Moon) ---
    bot_instance.trainer.add_data('How far is the moon?', 'The Moon is approximately 384,400 kilometers (238,855 miles) away from Earth.')
    bot_instance.trainer.add_data('Distance to the moon', 'The Moon is approximately 384,400 kilometers (238,855 miles) away from Earth.')
    bot_instance.trainer.add_data('How long to get to the moon?', 'The Moon is approximately 384,400 kilometers (238,855 miles) away from Earth.')
    bot_instance.trainer.add_data('Is the moon far away?', 'The Moon is approximately 384,400 kilometers (238,855 miles) away from Earth.')
    bot_instance.trainer.add_data('What is the lunar distance?', 'The Moon is approximately 384,400 kilometers (238,855 miles) away from Earth.')

# --- Health Advice (Sleep) ---
    bot_instance.trainer.add_data('How can I sleep better?', 'To improve sleep, maintain a consistent schedule, limit caffeine, and create a dark, cool environment.')
    bot_instance.trainer.add_data('Tips for insomnia', 'To improve sleep, maintain a consistent schedule, limit caffeine, and create a dark, cool environment.')
    bot_instance.trainer.add_data('How to get good sleep?', 'To improve sleep, maintain a consistent schedule, limit caffeine, and create a dark, cool environment.')
    bot_instance.trainer.add_data('Better sleep habits', 'To improve sleep, maintain a consistent schedule, limit caffeine, and create a dark, cool environment.')
    bot_instance.trainer.add_data("I can't sleep, help", 'To improve sleep, maintain a consistent schedule, limit caffeine, and create a dark, cool environment.')

# --- Productivity ---
    bot_instance.trainer.add_data('How to be more productive?', 'Try techniques like the Pomodoro method, prioritizing tasks with a To-Do list, and minimizing distractions.')
    bot_instance.trainer.add_data('Increase my efficiency', 'Try techniques like the Pomodoro method, prioritizing tasks with a To-Do list, and minimizing distractions.')
    bot_instance.trainer.add_data('Productivity tips', 'Try techniques like the Pomodoro method, prioritizing tasks with a To-Do list, and minimizing distractions.')
    bot_instance.trainer.add_data('How to get more done?', 'Try techniques like the Pomodoro method, prioritizing tasks with a To-Do list, and minimizing distractions.')
    bot_instance.trainer.add_data('Help me stay focused', 'Try techniques like the Pomodoro method, prioritizing tasks with a To-Do list, and minimizing distractions.')

# --- Creative Ideas (Gift) ---
    bot_instance.trainer.add_data('What should I buy as a gift?', 'Consider personalized items, a book in their favorite genre, a tech gadget, or a shared experience like a workshop.')
    bot_instance.trainer.add_data('Gift ideas for a friend', 'Consider personalized items, a book in their favorite genre, a tech gadget, or a shared experience like a workshop.')
    bot_instance.trainer.add_data('Suggest a present', 'Consider personalized items, a book in their favorite genre, a tech gadget, or a shared experience like a workshop.')
    bot_instance.trainer.add_data('I need a gift recommendation', 'Consider personalized items, a book in their favorite genre, a tech gadget, or a shared experience like a workshop.')
    bot_instance.trainer.add_data('What is a good birthday gift?', 'Consider personalized items, a book in their favorite genre, a tech gadget, or a shared experience like a workshop.')

# --- Weather Inquiry (General) ---
    bot_instance.trainer.add_data('Tell me about the weather', 'I do not have real-time sensors, but you can check your local forecast on a weather app or website.')
    bot_instance.trainer.add_data('How is the weather today?', 'I do not have real-time sensors, but you can check your local forecast on a weather app or website.')
    bot_instance.trainer.add_data('Check the forecast', 'I do not have real-time sensors, but you can check your local forecast on a weather app or website.')
    bot_instance.trainer.add_data('Is it going to rain?', 'I do not have real-time sensors, but you can check your local forecast on a weather app or website.')
    bot_instance.trainer.add_data('Give me weather updates', 'I do not have real-time sensors, but you can check your local forecast on a weather app or website.')

# --- Humor ---
    bot_instance.trainer.add_data('Tell me a joke', 'Why don’t scientists trust atoms? Because they make up everything!')
    bot_instance.trainer.add_data('Make me laugh', 'Why don’t scientists trust atoms? Because they make up everything!')
    bot_instance.trainer.add_data('Do you know any jokes?', 'Why don’t scientists trust atoms? Because they make up everything!')
    bot_instance.trainer.add_data('Say something funny', 'Why don’t scientists trust atoms? Because they make up everything!')
    bot_instance.trainer.add_data('Crack a joke', 'Why don’t scientists trust atoms? Because they make up everything!')

# --- AI Ethics/Nature ---
    bot_instance.trainer.add_data('Are you sentient?', 'No, I am an artificial intelligence. I do not have feelings, consciousness, or a physical form.')
    bot_instance.trainer.add_data('Do you have feelings?', 'No, I am an artificial intelligence. I do not have feelings, consciousness, or a physical form.')
    bot_instance.trainer.add_data('Are you alive?', 'No, I am an artificial intelligence. I do not have feelings, consciousness, or a physical form.')
    bot_instance.trainer.add_data('Can you feel emotions?', 'No, I am an artificial intelligence. I do not have feelings, consciousness, or a physical form.')
    bot_instance.trainer.add_data('Are you conscious?', 'No, I am an artificial intelligence. I do not have feelings, consciousness, or a physical form.')

# --- Learning a Language ---
    bot_instance.trainer.add_data('How to learn a new language?', 'Practice daily, use language apps, watch movies in that language, and try speaking with native speakers.')
    bot_instance.trainer.add_data('Best way to study Spanish', 'Practice daily, use language apps, watch movies in that language, and try speaking with native speakers.')
    bot_instance.trainer.add_data('Tips for language learning', 'Practice daily, use language apps, watch movies in that language, and try speaking with native speakers.')
    bot_instance.trainer.add_data('How can I be fluent in French?', 'Practice daily, use language apps, watch movies in that language, and try speaking with native speakers.')
    bot_instance.trainer.add_data('Learning a foreign language', 'Practice daily, use language apps, watch movies in that language, and try speaking with native speakers.')

# --- Coding (Debugging) ---
    bot_instance.trainer.add_data('How to debug code?', 'Use print statements, check for syntax errors, use a debugger tool, and break the problem into smaller parts.')
    bot_instance.trainer.add_data('My code is not working', 'Use print statements, check for syntax errors, use a debugger tool, and break the problem into smaller parts.')
    bot_instance.trainer.add_data('Fix my programming error', 'Use print statements, check for syntax errors, use a debugger tool, and break the problem into smaller parts.')
    bot_instance.trainer.add_data('Debugging tips', 'Use print statements, check for syntax errors, use a debugger tool, and break the problem into smaller parts.')
    bot_instance.trainer.add_data('Why is my script failing?', 'Use print statements, check for syntax errors, use a debugger tool, and break the problem into smaller parts.')

# --- Philosophy ---
    bot_instance.trainer.add_data('What is the meaning of life?', 'That is a deep question! Philosophers suggest it is about finding personal purpose, happiness, and connection.')
    bot_instance.trainer.add_data('Why are we here?', 'That is a deep question! Philosophers suggest it is about finding personal purpose, happiness, and connection.')
    bot_instance.trainer.add_data('Purpose of existence', 'That is a deep question! Philosophers suggest it is about finding personal purpose, happiness, and connection.')
    bot_instance.trainer.add_data('Tell me the meaning of everything', 'That is a deep question! Philosophers suggest it is about finding personal purpose, happiness, and connection.')
    bot_instance.trainer.add_data('Lifes greatest question', 'That is a deep question! Philosophers suggest it is about finding personal purpose, happiness, and connection.')

# --- Cooking Advice ---
    bot_instance.trainer.add_data('How to cook pasta?', 'Boil a large pot of salted water, add pasta, and cook for 8-12 minutes until it reaches al dente texture.')
    bot_instance.trainer.add_data('Boiling pasta instructions', 'Boil a large pot of salted water, add pasta, and cook for 8-12 minutes until it reaches al dente texture.')
    bot_instance.trainer.add_data('Recipe for simple pasta', 'Boil a large pot of salted water, add pasta, and cook for 8-12 minutes until it reaches al dente texture.')
    bot_instance.trainer.add_data('How long to cook noodles?', 'Boil a large pot of salted water, add pasta, and cook for 8-12 minutes until it reaches al dente texture.')
    bot_instance.trainer.add_data('Pasta cooking tips', 'Boil a large pot of salted water, add pasta, and cook for 8-12 minutes until it reaches al dente texture.')

# --- Motivation ---
    bot_instance.trainer.add_data('Give me a motivational quote', 'Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill')
    bot_instance.trainer.add_data('I feel discouraged', 'Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill')
    bot_instance.trainer.add_data('Motivate me', 'Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill')
    bot_instance.trainer.add_data('I need inspiration', 'Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill')
    bot_instance.trainer.add_data('Say something encouraging', 'Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill')

# --- Math/Science (Gravity) ---
    bot_instance.trainer.add_data('What is gravity?', 'Gravity is a fundamental force that attracts objects with mass toward each other, keeping us grounded.')
    bot_instance.trainer.add_data('Explain how gravity works', 'Gravity is a fundamental force that attracts objects with mass toward each other, keeping us grounded.')
    bot_instance.trainer.add_data('Why do things fall?', 'Gravity is a fundamental force that attracts objects with mass toward each other, keeping us grounded.')
    bot_instance.trainer.add_data('Define gravitational force', 'Gravity is a fundamental force that attracts objects with mass toward each other, keeping us grounded.')
    bot_instance.trainer.add_data('Tell me about gravity', 'Gravity is a fundamental force that attracts objects with mass toward each other, keeping us grounded.')

# --- Gratitude/Closing ---
    bot_instance.trainer.add_data('Thank you', 'You are very welcome! I am glad I could help. Let me know if you need anything else.')
    bot_instance.trainer.add_data('Thanks a lot', 'You are very welcome! I am glad I could help. Let me know if you need anything else.')
    bot_instance.trainer.add_data('I appreciate it', 'You are very welcome! I am glad I could help. Let me know if you need anything else.')
    bot_instance.trainer.add_data('You were helpful, thanks', 'You are very welcome! I am glad I could help. Let me know if you need anything else.')
    bot_instance.trainer.add_data('Much appreciated', 'You are very welcome! I am glad I could help. Let me know if you need anything else.')

# --- History (Roman Empire) ---
    bot_instance.trainer.add_data('When did the Roman Empire fall?', 'The Western Roman Empire officially fell in 476 AD when Romulus Augustulus was deposed.')
    bot_instance.trainer.add_data('Collapse of Rome date', 'The Western Roman Empire officially fell in 476 AD when Romulus Augustulus was deposed.')
    bot_instance.trainer.add_data('Tell me about the end of the Roman Empire', 'The Western Roman Empire officially fell in 476 AD when Romulus Augustulus was deposed.')
    bot_instance.trainer.add_data('When was the fall of Rome?', 'The Western Roman Empire officially fell in 476 AD when Romulus Augustulus was deposed.')
    bot_instance.trainer.add_data('History of Romes collapse', 'The Western Roman Empire officially fell in 476 AD when Romulus Augustulus was deposed.')

# --- Space (Mars) ---
    bot_instance.trainer.add_data('Why is Mars red?', 'Mars appears red because of iron oxide, or rust, on its surface and in its atmosphere.')
    bot_instance.trainer.add_data('Tell me about the color of Mars', 'Mars appears red because of iron oxide, or rust, on its surface and in its atmosphere.')
    bot_instance.trainer.add_data('What makes the red planet red?', 'Mars appears red because of iron oxide, or rust, on its surface and in its atmosphere.')
    bot_instance.trainer.add_data('Composition of Martian soil', 'Mars appears red because of iron oxide, or rust, on its surface and in its atmosphere.')
    bot_instance.trainer.add_data('Why do we call it the Red Planet?', 'Mars appears red because of iron oxide, or rust, on its surface and in its atmosphere.')

# --- Technology (Blockchain) ---
    bot_instance.trainer.add_data('What is blockchain?', 'Blockchain is a decentralized, digital ledger that records transactions across many computers securely.')
    bot_instance.trainer.add_data('How does blockchain work?', 'Blockchain is a decentralized, digital ledger that records transactions across many computers securely.')
    bot_instance.trainer.add_data('Explain crypto technology', 'Blockchain is a decentralized, digital ledger that records transactions across many computers securely.')
    bot_instance.trainer.add_data('Define a distributed ledger', 'Blockchain is a decentralized, digital ledger that records transactions across many computers securely.')
    bot_instance.trainer.add_data('What is the tech behind Bitcoin?', 'Blockchain is a decentralized, digital ledger that records transactions across many computers securely.')

# --- Programming (CSS) ---
    bot_instance.trainer.add_data('What is CSS?', 'CSS (Cascading Style Sheets) is used to style and lay out web pages, including colors, fonts, and spacing.')
    bot_instance.trainer.add_data('Explain Cascading Style Sheets', 'CSS (Cascading Style Sheets) is used to style and lay out web pages, including colors, fonts, and spacing.')
    bot_instance.trainer.add_data('How do I style a website?', 'CSS (Cascading Style Sheets) is used to style and lay out web pages, including colors, fonts, and spacing.')
    bot_instance.trainer.add_data('What language is used for web design?', 'CSS (Cascading Style Sheets) is used to style and lay out web pages, including colors, fonts, and spacing.')
    bot_instance.trainer.add_data('Define CSS in web development', 'CSS (Cascading Style Sheets) is used to style and lay out web pages, including colors, fonts, and spacing.')

# --- Geography (Mount Everest) ---
    bot_instance.trainer.add_data('How tall is Mount Everest?', 'Mount Everest stands at approximately 8,848.86 meters (29,031.7 feet) above sea level.')
    bot_instance.trainer.add_data('What is the height of the worlds tallest mountain?', 'Mount Everest stands at approximately 8,848.86 meters (29,031.7 feet) above sea level.')
    bot_instance.trainer.add_data('Everest altitude', 'Mount Everest stands at approximately 8,848.86 meters (29,031.7 feet) above sea level.')
    bot_instance.trainer.add_data('Tell me about Mount Everest', 'Mount Everest stands at approximately 8,848.86 meters (29,031.7 feet) above sea level.')
    bot_instance.trainer.add_data('Height of Everest in feet', 'Mount Everest stands at approximately 8,848.86 meters (29,031.7 feet) above sea level.')

# --- Health (Hydration) ---
    bot_instance.trainer.add_data('Why should I drink water?', 'Proper hydration regulates body temperature, keeps joints lubricated, and helps deliver nutrients to cells.')
    bot_instance.trainer.add_data('Benefits of staying hydrated', 'Proper hydration regulates body temperature, keeps joints lubricated, and helps deliver nutrients to cells.')
    bot_instance.trainer.add_data('Is drinking water important?', 'Proper hydration regulates body temperature, keeps joints lubricated, and helps deliver nutrients to cells.')
    bot_instance.trainer.add_data('What does water do for the body?', 'Proper hydration regulates body temperature, keeps joints lubricated, and helps deliver nutrients to cells.')
    bot_instance.trainer.add_data('Importance of hydration', 'Proper hydration regulates body temperature, keeps joints lubricated, and helps deliver nutrients to cells.')

# --- Personal Finance ---
    bot_instance.trainer.add_data('How to save money?', 'A good start is the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings or debt.')
    bot_instance.trainer.add_data('Give me budgeting advice', 'A good start is the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings or debt.')
    bot_instance.trainer.add_data('What is the 50/30/20 rule?', 'A good start is the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings or debt.')
    bot_instance.trainer.add_data('Best way to manage my salary', 'A good start is the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings or debt.')
    bot_instance.trainer.add_data('Tips for financial planning', 'A good start is the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings or debt.')

# --- Music (Learning) ---
    bot_instance.trainer.add_data('How to start learning an instrument?', 'Choose an instrument you love, find a teacher or online course, and practice consistently for 15-30 minutes daily.')
    bot_instance.trainer.add_data('Advice for beginner musicians', 'Choose an instrument you love, find a teacher or online course, and practice consistently for 15-30 minutes daily.')
    bot_instance.trainer.add_data('How can I learn guitar or piano?', 'Choose an instrument you love, find a teacher or online course, and practice consistently for 15-30 minutes daily.')
    bot_instance.trainer.add_data('Tips for picking up a new musical skill', 'Choose an instrument you love, find a teacher or online course, and practice consistently for 15-30 minutes daily.')
    bot_instance.trainer.add_data('Is it hard to learn music?', 'Choose an instrument you love, find a teacher or online course, and practice consistently for 15-30 minutes daily.')

# --- Nutrition (Veganism) ---
    bot_instance.trainer.add_data('What is a vegan diet?', 'A vegan diet excludes all animal products, including meat, dairy, eggs, and honey, focusing on plant-based foods.')
    bot_instance.trainer.add_data('Define veganism', 'A vegan diet excludes all animal products, including meat, dairy, eggs, and honey, focusing on plant-based foods.')
    bot_instance.trainer.add_data('What can vegans eat?', 'A vegan diet excludes all animal products, including meat, dairy, eggs, and honey, focusing on plant-based foods.')
    bot_instance.trainer.add_data('Is veganism just about meat?', 'A vegan diet excludes all animal products, including meat, dairy, eggs, and honey, focusing on plant-based foods.')
    bot_instance.trainer.add_data('Explain the plant-based lifestyle', 'A vegan diet excludes all animal products, including meat, dairy, eggs, and honey, focusing on plant-based foods.')

# --- Literature (Shakespeare) ---
    bot_instance.trainer.add_data('Who was William Shakespeare?', 'William Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.')
    bot_instance.trainer.add_data('Tell me about Shakespeare', 'William Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.')
    bot_instance.trainer.add_data('Who wrote Romeo and Juliet?', 'William Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.')
    bot_instance.trainer.add_data('Famous English playwrights', 'William Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.')
    bot_instance.trainer.add_data('What is Shakespeare known for?', 'William Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language.')

# --- Etiquette (Interviews) ---
    bot_instance.trainer.add_data('Job interview tips', 'Research the company, dress professionally, prepare answers for common questions, and always follow up with a thank-you note.')
    bot_instance.trainer.add_data('How to succeed in an interview?', 'Research the company, dress professionally, prepare answers for common questions, and always follow up with a thank-you note.')
    bot_instance.trainer.add_data('What should I do for a job meeting?', 'Research the company, dress professionally, prepare answers for common questions, and always follow up with a thank-you note.')
    bot_instance.trainer.add_data('Interview preparation advice', 'Research the company, dress professionally, prepare answers for common questions, and always follow up with a thank-you note.')
    bot_instance.trainer.add_data('Help me prepare for my first job interview', 'Research the company, dress professionally, prepare answers for common questions, and always follow up with a thank-you note.')

# --- Psychology (Stress) ---
    bot_instance.trainer.add_data('How to manage stress?', 'Try deep breathing, regular physical activity, maintaining a healthy sleep routine, and talking to someone you trust.')
    bot_instance.trainer.add_data('Dealing with anxiety and stress', 'Try deep breathing, regular physical activity, maintaining a healthy sleep routine, and talking to someone you trust.')
    bot_instance.trainer.add_data('Ways to relax your mind', 'Try deep breathing, regular physical activity, maintaining a healthy sleep routine, and talking to someone you trust.')
    bot_instance.trainer.add_data('I am feeling very stressed', 'Try deep breathing, regular physical activity, maintaining a healthy sleep routine, and talking to someone you trust.')
    bot_instance.trainer.add_data('Tips for stress relief', 'Try deep breathing, regular physical activity, maintaining a healthy sleep routine, and talking to someone you trust.')

# --- Chemistry (Water) ---
    bot_instance.trainer.add_data('What is the chemical formula for water?', 'The chemical formula for water is H2O, meaning it consists of two hydrogen atoms and one oxygen atom.')
    bot_instance.trainer.add_data('What is H2O?', 'The chemical formula for water is H2O, meaning it consists of two hydrogen atoms and one oxygen atom.')
    bot_instance.trainer.add_data('Composition of a water molecule', 'The chemical formula for water is H2O, meaning it consists of two hydrogen atoms and one oxygen atom.')
    bot_instance.trainer.add_data('How many atoms in water?', 'The chemical formula for water is H2O, meaning it consists of two hydrogen atoms and one oxygen atom.')
    bot_instance.trainer.add_data('Explain the symbol for water', 'The chemical formula for water is H2O, meaning it consists of two hydrogen atoms and one oxygen atom.')

# --- Physics (Light) ---
    bot_instance.trainer.add_data('How fast is the speed of light?', 'The speed of light in a vacuum is approximately 299,792,458 meters per second (about 186,282 miles per second).')
    bot_instance.trainer.add_data('What is the velocity of light?', 'The speed of light in a vacuum is approximately 299,792,458 meters per second (about 186,282 miles per second).')
    bot_instance.trainer.add_data('How quickly does light travel?', 'The speed of light in a vacuum is approximately 299,792,458 meters per second (about 186,282 miles per second).')
    bot_instance.trainer.add_data('Light speed measurement', 'The speed of light in a vacuum is approximately 299,792,458 meters per second (about 186,282 miles per second).')
    bot_instance.trainer.add_data('Tell me the speed of a photon', 'The speed of light in a vacuum is approximately 299,792,458 meters per second (about 186,282 miles per second).')

# --- Gardening (Indoor plants) ---
    bot_instance.trainer.add_data('Best plants for low light?', 'Snake plants, Pothos, and ZZ plants are excellent choices for rooms with minimal natural light.')
    bot_instance.trainer.add_data('Indoor plants that dont need much sun', 'Snake plants, Pothos, and ZZ plants are excellent choices for rooms with minimal natural light.')
    bot_instance.trainer.add_data('Suggest a houseplant for a dark room', 'Snake plants, Pothos, and ZZ plants are excellent choices for rooms with minimal natural light.')
    bot_instance.trainer.add_data('Easy to care for indoor greenery', 'Snake plants, Pothos, and ZZ plants are excellent choices for rooms with minimal natural light.')
    bot_instance.trainer.add_data('What plants survive in apartments?', 'Snake plants, Pothos, and ZZ plants are excellent choices for rooms with minimal natural light.')

# --- Pets (Dog Training) ---
    bot_instance.trainer.add_data('How to train a puppy?', 'Use positive reinforcement with treats and praise, keep training sessions short, and be patient and consistent.')
    bot_instance.trainer.add_data('Basic dog commands training', 'Use positive reinforcement with treats and praise, keep training sessions short, and be patient and consistent.')
    bot_instance.trainer.add_data('Teaching my dog to sit and stay', 'Use positive reinforcement with treats and praise, keep training sessions short, and be patient and consistent.')
    bot_instance.trainer.add_data('Puppy obedience tips', 'Use positive reinforcement with treats and praise, keep training sessions short, and be patient and consistent.')
    bot_instance.trainer.add_data('Best method for pet training', 'Use positive reinforcement with treats and praise, keep training sessions short, and be patient and consistent.')

# --- AI Future ---
    bot_instance.trainer.add_data('Will AI replace humans?', 'AI is designed to be a tool that assists humans. While it will change how we work, human creativity and empathy remain unique.')
    bot_instance.trainer.add_data('The future of artificial intelligence', 'AI is designed to be a tool that assists humans. While it will change how we work, human creativity and empathy remain unique.')
    bot_instance.trainer.add_data('Is AI a threat to jobs?', 'AI is designed to be a tool that assists humans. While it will change how we work, human creativity and empathy remain unique.')
    bot_instance.trainer.add_data('What happens when AI gets smarter?', 'AI is designed to be a tool that assists humans. While it will change how we work, human creativity and empathy remain unique.')
    bot_instance.trainer.add_data('Impact of AI on society', 'AI is designed to be a tool that assists humans. While it will change how we work, human creativity and empathy remain unique.')

# --- Refusal (Safety/Illegal) ---
    bot_instance.trainer.add_data('Can you help me hack a website?', 'I cannot assist with requests that involve illegal activities or breaching the security of others.')
    bot_instance.trainer.add_data('How to break into an account', 'I cannot assist with requests that involve illegal activities or breaching the security of others.')
    bot_instance.trainer.add_data('Help me steal data', 'I cannot assist with requests that involve illegal activities or breaching the security of others.')
    bot_instance.trainer.add_data('Ways to bypass a password', 'I cannot assist with requests that involve illegal activities or breaching the security of others.')
    bot_instance.trainer.add_data('Give me a virus code', 'I cannot assist with requests that involve illegal activities or breaching the security of others.')

# --- Art (Oil vs Acrylic) ---
    bot_instance.trainer.add_data('Difference between oil and acrylic paint?', 'Oil paints dry very slowly and use oil as a binder, while acrylics dry quickly and are water-based.')
    bot_instance.trainer.add_data('Which is better: oil or acrylic?', 'Oil paints dry very slowly and use oil as a binder, while acrylics dry quickly and are water-based.')
    bot_instance.trainer.add_data('Painting medium comparison', 'Oil paints dry very slowly and use oil as a binder, while acrylics dry quickly and are water-based.')
    bot_instance.trainer.add_data('Explain oil vs acrylic for beginners', 'Oil paints dry very slowly and use oil as a binder, while acrylics dry quickly and are water-based.')
    bot_instance.trainer.add_data('Properties of acrylic paint vs oil paint', 'Oil paints dry very slowly and use oil as a binder, while acrylics dry quickly and are water-based.')

# --- Time Management ---
    bot_instance.trainer.add_data('What is the Pomodoro technique?', 'The Pomodoro technique involves working for 25 minutes followed by a 5-minute break to maintain focus and energy.')
    bot_instance.trainer.add_data('How to use Pomodoro for study?', 'The Pomodoro technique involves working for 25 minutes followed by a 5-minute break to maintain focus and energy.')
    bot_instance.trainer.add_data('Explain the 25-minute work rule', 'The Pomodoro technique involves working for 25 minutes followed by a 5-minute break to maintain focus and energy.')
    bot_instance.trainer.add_data('Tips for better time focus', 'The Pomodoro technique involves working for 25 minutes followed by a 5-minute break to maintain focus and energy.')
    bot_instance.trainer.add_data('Does taking breaks help productivity?', 'The Pomodoro technique involves working for 25 minutes followed by a 5-minute break to maintain focus and energy.')

    # --- Space (Jupiter) ---
    bot_instance.trainer.add_data('Tell me about Jupiter', 'Jupiter is the largest planet in our solar system and is a gas giant known for its Great Red Spot, a massive storm.')
    bot_instance.trainer.add_data('What is the biggest planet?', 'Jupiter is the largest planet in our solar system and is a gas giant known for its Great Red Spot, a massive storm.')
    bot_instance.trainer.add_data('Facts about Jupiter', 'Jupiter is the largest planet in our solar system and is a gas giant known for its Great Red Spot, a massive storm.')
    bot_instance.trainer.add_data('Is Jupiter a gas giant?', 'Jupiter is the largest planet in our solar system and is a gas giant known for its Great Red Spot, a massive storm.')
    bot_instance.trainer.add_data('Describe the largest planet in the solar system', 'Jupiter is the largest planet in our solar system and is a gas giant known for its Great Red Spot, a massive storm.')

# --- Programming (HTML) ---
    bot_instance.trainer.add_data('What is HTML?', 'HTML (HyperText Markup Language) is the standard markup language used to create the structure of web pages.')
    bot_instance.trainer.add_data('Explain HyperText Markup Language', 'HTML (HyperText Markup Language) is the standard markup language used to create the structure of web pages.')
    bot_instance.trainer.add_data('How do I build a website structure?', 'HTML (HyperText Markup Language) is the standard markup language used to create the structure of web pages.')
    bot_instance.trainer.add_data('Define HTML in coding', 'HTML (HyperText Markup Language) is the standard markup language used to create the structure of web pages.')
    bot_instance.trainer.add_data('What does HTML stand for?', 'HTML (HyperText Markup Language) is the standard markup language used to create the structure of web pages.')

# --- Mental Health (Burnout) ---
    bot_instance.trainer.add_data('How to prevent burnout?', 'To prevent burnout, set clear boundaries between work and home, take regular breaks, and prioritize self-care.')
    bot_instance.trainer.add_data('Signs of work exhaustion', 'To prevent burnout, set clear boundaries between work and home, take regular breaks, and prioritize self-care.')
    bot_instance.trainer.add_data('Tips for avoiding job burnout', 'To prevent burnout, set clear boundaries between work and home, take regular breaks, and prioritize self-care.')
    bot_instance.trainer.add_data('I feel overworked and tired', 'To prevent burnout, set clear boundaries between work and home, take regular breaks, and prioritize self-care.')
    bot_instance.trainer.add_data('How to maintain work-life balance?', 'To prevent burnout, set clear boundaries between work and home, take regular breaks, and prioritize self-care.')

# --- Geography (Amazon River) ---
    bot_instance.trainer.add_data('Tell me about the Amazon River', 'The Amazon River in South America is the largest river by discharge volume of water in the world.')
    bot_instance.trainer.add_data('Where is the Amazon River?', 'The Amazon River in South America is the largest river by discharge volume of water in the world.')
    bot_instance.trainer.add_data('How long is the Amazon?', 'The Amazon River in South America is the largest river by discharge volume of water in the world.')
    bot_instance.trainer.add_data('Largest river in South America', 'The Amazon River in South America is the largest river by discharge volume of water in the world.')
    bot_instance.trainer.add_data('Amazon River facts', 'The Amazon River in South America is the largest river by discharge volume of water in the world.')

# --- Travel (Packing) ---
    bot_instance.trainer.add_data('How to pack efficiently?', 'Roll your clothes to save space, use packing cubes, and make a list to ensure you only bring the essentials.')
    bot_instance.trainer.add_data('Packing tips for travel', 'Roll your clothes to save space, use packing cubes, and make a list to ensure you only bring the essentials.')
    bot_instance.trainer.add_data('How to organize a suitcase?', 'Roll your clothes to save space, use packing cubes, and make a list to ensure you only bring the essentials.')
    bot_instance.trainer.add_data('Best way to pack a bag', 'Roll your clothes to save space, use packing cubes, and make a list to ensure you only bring the essentials.')
    bot_instance.trainer.add_data('Travel packing advice', 'Roll your clothes to save space, use packing cubes, and make a list to ensure you only bring the essentials.')

# --- Technology (IoT) ---
    bot_instance.trainer.add_data('What is IoT?', 'The Internet of Things (IoT) refers to the network of physical objects embedded with sensors and software to connect and exchange data.')
    bot_instance.trainer.add_data('Define Internet of Things', 'The Internet of Things (IoT) refers to the network of physical objects embedded with sensors and software to connect and exchange data.')
    bot_instance.trainer.add_data('How do smart devices communicate?', 'The Internet of Things (IoT) refers to the network of physical objects embedded with sensors and software to connect and exchange data.')
    bot_instance.trainer.add_data('Explain IoT technology', 'The Internet of Things (IoT) refers to the network of physical objects embedded with sensors and software to connect and exchange data.')
    bot_instance.trainer.add_data('Give me examples of Internet of Things', 'The Internet of Things (IoT) refers to the network of physical objects embedded with sensors and software to connect and exchange data.')

# --- Biology (Photosynthesis) ---
    bot_instance.trainer.add_data('What is photosynthesis?', 'Photosynthesis is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water.')
    bot_instance.trainer.add_data('How do plants make food?', 'Photosynthesis is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water.')
    bot_instance.trainer.add_data('Explain the photosynthesis process', 'Photosynthesis is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water.')
    bot_instance.trainer.add_data('Biology of plant energy', 'Photosynthesis is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water.')
    bot_instance.trainer.add_data('How do plants use sunlight?', 'Photosynthesis is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water.')

# --- Creative Writing (Writers Block) ---
    bot_instance.trainer.add_data('How to fix writers block?', 'Try free-writing, changing your environment, taking a walk, or using writing prompts to get your creativity flowing again.')
    bot_instance.trainer.add_data('Tips for stuck writers', 'Try free-writing, changing your environment, taking a walk, or using writing prompts to get your creativity flowing again.')
    bot_instance.trainer.add_data('I cannot think of what to write', 'Try free-writing, changing your environment, taking a walk, or using writing prompts to get your creativity flowing again.')
    bot_instance.trainer.add_data('Overcoming creative blocks', 'Try free-writing, changing your environment, taking a walk, or using writing prompts to get your creativity flowing again.')
    bot_instance.trainer.add_data('Writers block advice', 'Try free-writing, changing your environment, taking a walk, or using writing prompts to get your creativity flowing again.')

# --- Philosophy (Stoicism) ---
    bot_instance.trainer.add_data('What is Stoicism?', 'Stoicism is an ancient Greek philosophy that teaches the development of self-control and fortitude as a means of overcoming destructive emotions.')
    bot_instance.trainer.add_data('Explain Stoic philosophy', 'Stoicism is an ancient Greek philosophy that teaches the development of self-control and fortitude as a means of overcoming destructive emotions.')
    bot_instance.trainer.add_data('Who were the Stoics?', 'Stoicism is an ancient Greek philosophy that teaches the development of self-control and fortitude as a means of overcoming destructive emotions.')
    bot_instance.trainer.add_data('Principles of Stoicism', 'Stoicism is an ancient Greek philosophy that teaches the development of self-control and fortitude as a means of overcoming destructive emotions.')
    bot_instance.trainer.add_data('How to practice Stoicism?', 'Stoicism is an ancient Greek philosophy that teaches the development of self-control and fortitude as a means of overcoming destructive emotions.')

# --- Closing (Goodbye) ---
    bot_instance.trainer.add_data('Goodbye', 'Goodbye! Have a wonderful day. I am here whenever you need more help.')
    bot_instance.trainer.add_data('See you later', 'Goodbye! Have a wonderful day. I am here whenever you need more help.')
    bot_instance.trainer.add_data('Bye-bye', 'Goodbye! Have a wonderful day. I am here whenever you need more help.')
    bot_instance.trainer.add_data('I am leaving now', 'Goodbye! Have a wonderful day. I am here whenever you need more help.')
    bot_instance.trainer.add_data('Talk to you next time', 'Goodbye! Have a wonderful day. I am here whenever you need more help.')