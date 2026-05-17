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

    # --- Space (Saturn) ---
    bot_instance.trainer.add_data('Tell me about Saturn', 'Saturn is the sixth planet from the Sun and is famous for its extensive ring system, which is made mostly of ice particles and rock.')
    bot_instance.trainer.add_data('What planet has rings?', 'Saturn is the sixth planet from the Sun and is famous for its extensive ring system, which is made mostly of ice particles and rock.')
    bot_instance.trainer.add_data('Describe Saturns rings', 'Saturn is the sixth planet from the Sun and is famous for its extensive ring system, which is made mostly of ice particles and rock.')
    bot_instance.trainer.add_data('Saturn facts', 'Saturn is the sixth planet from the Sun and is famous for its extensive ring system, which is made mostly of ice particles and rock.')
    bot_instance.trainer.add_data('Is Saturn a gas giant?', 'Saturn is the sixth planet from the Sun and is famous for its extensive ring system, which is made mostly of ice particles and rock.')

# --- Programming (JavaScript) ---
    bot_instance.trainer.add_data('What is JavaScript?', 'JavaScript is a high-level, dynamic programming language that is one of the core technologies of the World Wide Web.')
    bot_instance.trainer.add_data('Tell me about JS', 'JavaScript is a high-level, dynamic programming language that is one of the core technologies of the World Wide Web.')
    bot_instance.trainer.add_data('What language is used for web interactivity?', 'JavaScript is a high-level, dynamic programming language that is one of the core technologies of the World Wide Web.')
    bot_instance.trainer.add_data('Define JavaScript coding', 'JavaScript is a high-level, dynamic programming language that is one of the core technologies of the World Wide Web.')
    bot_instance.trainer.add_data('Is JS the same as Java?', 'JavaScript is a high-level, dynamic programming language that is one of the core technologies of the World Wide Web.')

# --- Health (Exercise) ---
    bot_instance.trainer.add_data('Why should I exercise?', 'Regular exercise improves cardiovascular health, boosts your mood through endorphin release, and helps maintain a healthy weight.')
    bot_instance.trainer.add_data('Benefits of physical activity', 'Regular exercise improves cardiovascular health, boosts your mood through endorphin release, and helps maintain a healthy weight.')
    bot_instance.trainer.add_data('Is working out important?', 'Regular exercise improves cardiovascular health, boosts your mood through endorphin release, and helps maintain a healthy weight.')
    bot_instance.trainer.add_data('What does exercise do for the brain?', 'Regular exercise improves cardiovascular health, boosts your mood through endorphin release, and helps maintain a healthy weight.')
    bot_instance.trainer.add_data('Should I go to the gym?', 'Regular exercise improves cardiovascular health, boosts your mood through endorphin release, and helps maintain a healthy weight.')

# --- History (Ancient Egypt) ---
    bot_instance.trainer.add_data('Who built the pyramids?', 'Ancient Egypt was a civilization in Northeast Africa, known for its Pharaohs, pyramids, and the invention of hieroglyphic writing.')
    bot_instance.trainer.add_data('Tell me about Ancient Egypt', 'Ancient Egypt was a civilization in Northeast Africa, known for its Pharaohs, pyramids, and the invention of hieroglyphic writing.')
    bot_instance.trainer.add_data('Facts about Pharaohs', 'Ancient Egypt was a civilization in Northeast Africa, known for its Pharaohs, pyramids, and the invention of hieroglyphic writing.')
    bot_instance.trainer.add_data('What is the Nile civilization?', 'Ancient Egypt was a civilization in Northeast Africa, known for its Pharaohs, pyramids, and the invention of hieroglyphic writing.')
    bot_instance.trainer.add_data('Brief history of Egypt', 'Ancient Egypt was a civilization in Northeast Africa, known for its Pharaohs, pyramids, and the invention of hieroglyphic writing.')

# --- Identity (Creator/Source) ---
    bot_instance.trainer.add_data('Who created you?', 'I was developed by a team of engineers and data scientists using advanced machine learning models and diverse datasets.')
    bot_instance.trainer.add_data('Who is your developer?', 'I was developed by a team of engineers and data scientists using advanced machine learning models and diverse datasets.')
    bot_instance.trainer.add_data('What company made you?', 'I was developed by a team of engineers and data scientists using advanced machine learning models and diverse datasets.')
    bot_instance.trainer.add_data('Where do you come from?', 'I was developed by a team of engineers and data scientists using advanced machine learning models and diverse datasets.')
    bot_instance.trainer.add_data('Tell me about your origins', 'I was developed by a team of engineers and data scientists using advanced machine learning models and diverse datasets.')

# --- Technology (Cloud Computing) ---
    bot_instance.trainer.add_data('What is cloud computing?', 'Cloud computing is the on-demand delivery of computing services—including servers and storage—over the internet.')
    bot_instance.trainer.add_data('Explain the cloud', 'Cloud computing is the on-demand delivery of computing services—including servers and storage—over the internet.')
    bot_instance.trainer.add_data('How does AWS or Azure work?', 'Cloud computing is the on-demand delivery of computing services—including servers and storage—over the internet.')
    bot_instance.trainer.add_data('Benefits of using the cloud', 'Cloud computing is the on-demand delivery of computing services—including servers and storage—over the internet.')
    bot_instance.trainer.add_data('Define online storage services', 'Cloud computing is the on-demand delivery of computing services—including servers and storage—over the internet.')

# --- Science (Evolution) ---
    bot_instance.trainer.add_data('What is evolution?', 'Evolution is the process by which different kinds of living organisms are thought to have developed and diversified from earlier forms.')
    bot_instance.trainer.add_data('Explain natural selection', 'Evolution is the process by which different kinds of living organisms are thought to have developed and diversified from earlier forms.')
    bot_instance.trainer.add_data('How do species change over time?', 'Evolution is the process by which different kinds of living organisms are thought to have developed and diversified from earlier forms.')
    bot_instance.trainer.add_data('Tell me about Darwins theory', 'Evolution is the process by which different kinds of living organisms are thought to have developed and diversified from earlier forms.')
    bot_instance.trainer.add_data('Biological evolution definition', 'Evolution is the process by which different kinds of living organisms are thought to have developed and diversified from earlier forms.')

# --- Lifestyle (Meditation) ---
    bot_instance.trainer.add_data('How to meditate?', 'Meditation is a practice where an individual uses a technique – such as mindfulness – to train attention and achieve a calm state.')
    bot_instance.trainer.add_data('What is mindfulness?', 'Meditation is a practice where an individual uses a technique – such as mindfulness – to train attention and achieve a calm state.')
    bot_instance.trainer.add_data('Benefits of meditation', 'Meditation is a practice where an individual uses a technique – such as mindfulness – to train attention and achieve a calm state.')
    bot_instance.trainer.add_data('How to clear my mind?', 'Meditation is a practice where an individual uses a technique – such as mindfulness – to train attention and achieve a calm state.')
    bot_instance.trainer.add_data('Daily meditation tips', 'Meditation is a practice where an individual uses a technique – such as mindfulness – to train attention and achieve a calm state.')

# --- Programming (Git/Version Control) ---
    bot_instance.trainer.add_data('What is Git?', 'Git is a distributed version control system that allows developers to track changes in their source code during software development.')
    bot_instance.trainer.add_data('Explain version control', 'Git is a distributed version control system that allows developers to track changes in their source code during software development.')
    bot_instance.trainer.add_data('How do I use Github?', 'Git is a distributed version control system that allows developers to track changes in their source code during software development.')
    bot_instance.trainer.add_data('Define a Git repository', 'Git is a distributed version control system that allows developers to track changes in their source code during software development.')
    bot_instance.trainer.add_data('Why use Git in a team?', 'Git is a distributed version control system that allows developers to track changes in their source code during software development.')

# --- General (AI Definition) ---
    bot_instance.trainer.add_data('Define Artificial Intelligence', 'Artificial Intelligence (AI) refers to the simulation of human intelligence processes by computer systems, including learning and problem-solving.')
    bot_instance.trainer.add_data('What does AI mean?', 'Artificial Intelligence (AI) refers to the simulation of human intelligence processes by computer systems, including learning and problem-solving.')
    bot_instance.trainer.add_data('Explanation of machine intelligence', 'Artificial Intelligence (AI) refers to the simulation of human intelligence processes by computer systems, including learning and problem-solving.')
    bot_instance.trainer.add_data('What is the core of AI?', 'Artificial Intelligence (AI) refers to the simulation of human intelligence processes by computer systems, including learning and problem-solving.')
    bot_instance.trainer.add_data('How does AI solve problems?', 'Artificial Intelligence (AI) refers to the simulation of human intelligence processes by computer systems, including learning and problem-solving.')

    # --- Psychology (Cognitive Bias) ---
    bot_instance.trainer.add_data('What is a cognitive bias?', 'A cognitive bias is a systematic error in thinking that occurs when people are processing and interpreting information in the world around them.')
    bot_instance.trainer.add_data('Explain thinking errors', 'A cognitive bias is a systematic error in thinking that occurs when people are processing and interpreting information in the world around them.')
    bot_instance.trainer.add_data('Why do we make biased decisions?', 'A cognitive bias is a systematic error in thinking that occurs when people are processing and interpreting information in the world around them.')
    bot_instance.trainer.add_data('Definition of psychological bias', 'A cognitive bias is a systematic error in thinking that occurs when people are processing and interpreting information in the world around them.')
    bot_instance.trainer.add_data('Tell me about human judgment errors', 'A cognitive bias is a systematic error in thinking that occurs when people are processing and interpreting information in the world around them.')

# --- Programming (API) ---
    bot_instance.trainer.add_data('What is an API?', 'An API (Application Programming Interface) is a set of rules that allows different software entities to communicate and exchange data with each other.')
    bot_instance.trainer.add_data('Explain how APIs work', 'An API (Application Programming Interface) is a set of rules that allows different software entities to communicate and exchange data with each other.')
    bot_instance.trainer.add_data('Define Application Programming Interface', 'An API (Application Programming Interface) is a set of rules that allows different software entities to communicate and exchange data with each other.')
    bot_instance.trainer.add_data('How do apps talk to each other?', 'An API (Application Programming Interface) is a set of rules that allows different software entities to communicate and exchange data with each other.')
    bot_instance.trainer.add_data('Give me a summary of APIs', 'An API (Application Programming Interface) is a set of rules that allows different software entities to communicate and exchange data with each other.')

# --- Finance (Bitcoin) ---
    bot_instance.trainer.add_data('What is Bitcoin?', 'Bitcoin is a decentralized digital currency, without a central bank, that can be sent from user to user on the peer-to-peer network.')
    bot_instance.trainer.add_data('Explain BTC', 'Bitcoin is a decentralized digital currency, without a central bank, that can be sent from user to user on the peer-to-peer network.')
    bot_instance.trainer.add_data('How does decentralized currency work?', 'Bitcoin is a decentralized digital currency, without a central bank, that can be sent from user to user on the peer-to-peer network.')
    bot_instance.trainer.add_data('Tell me about Bitcoin', 'Bitcoin is a decentralized digital currency, without a central bank, that can be sent from user to user on the peer-to-peer network.')
    bot_instance.trainer.add_data('Is Bitcoin a digital coin?', 'Bitcoin is a decentralized digital currency, without a central bank, that can be sent from user to user on the peer-to-peer network.')

# --- History (Industrial Revolution) ---
    bot_instance.trainer.add_data('When was the Industrial Revolution?', 'The Industrial Revolution was the transition to new manufacturing processes in Europe and the US, occurring from about 1760 to the mid-1800s.')
    bot_instance.trainer.add_data('Tell me about the rise of factories', 'The Industrial Revolution was the transition to new manufacturing processes in Europe and the US, occurring from about 1760 to the mid-1800s.')
    bot_instance.trainer.add_data('What happened in the 18th century industry?', 'The Industrial Revolution was the transition to new manufacturing processes in Europe and the US, occurring from about 1760 to the mid-1800s.')
    bot_instance.trainer.add_data('History of mass production', 'The Industrial Revolution was the transition to new manufacturing processes in Europe and the US, occurring from about 1760 to the mid-1800s.')
    bot_instance.trainer.add_data('Explain the industrial era', 'The Industrial Revolution was the transition to new manufacturing processes in Europe and the US, occurring from about 1760 to the mid-1800s.')

# --- Science (Black Holes) ---
    bot_instance.trainer.add_data('What is a black hole?', 'A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it.')
    bot_instance.trainer.add_data('Can light escape a black hole?', 'A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it.')
    bot_instance.trainer.add_data('Explain gravitational collapse', 'A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it.')
    bot_instance.trainer.add_data('Describe a singularity in space', 'A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it.')
    bot_instance.trainer.add_data('Tell me about black holes', 'A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it.')

# --- Health (Macronutrients) ---
    bot_instance.trainer.add_data('What are macronutrients?', 'Macronutrients are the nutrients the body needs in large amounts—carbohydrates, proteins, and fats—to provide energy.')
    bot_instance.trainer.add_data('Explain carbs, proteins, and fats', 'Macronutrients are the nutrients the body needs in large amounts—carbohydrates, proteins, and fats—to provide energy.')
    bot_instance.trainer.add_data('What does the body need for energy?', 'Macronutrients are the nutrients the body needs in large amounts—carbohydrates, proteins, and fats—to provide energy.')
    bot_instance.trainer.add_data('List the main food groups for nutrition', 'Macronutrients are the nutrients the body needs in large amounts—carbohydrates, proteins, and fats—to provide energy.')
    bot_instance.trainer.add_data('Define macros', 'Macronutrients are the nutrients the body needs in large amounts—carbohydrates, proteins, and fats—to provide energy.')

# --- Logic (Turing Test) ---
    bot_instance.trainer.add_data('What is the Turing Test?', 'The Turing Test is a method for determining if a machine can demonstrate intelligent behavior equivalent to, or indistinguishable from, that of a human.')
    bot_instance.trainer.add_data('How do we test AI intelligence?', 'The Turing Test is a method for determining if a machine can demonstrate intelligent behavior equivalent to, or indistinguishable from, that of a human.')
    bot_instance.trainer.add_data('Who is Alan Turing in AI?', 'The Turing Test is a method for determining if a machine can demonstrate intelligent behavior equivalent to, or indistinguishable from, that of a human.')
    bot_instance.trainer.add_data('Explain the imitation game', 'The Turing Test is a method for determining if a machine can demonstrate intelligent behavior equivalent to, or indistinguishable from, that of a human.')
    bot_instance.trainer.add_data('Can a machine pass for a human?', 'The Turing Test is a method for determining if a machine can demonstrate intelligent behavior equivalent to, or indistinguishable from, that of a human.')

# --- Creative (Storytelling) ---
    bot_instance.trainer.add_data('How to write a good story?', 'A good story usually follows a narrative arc including an exposition, rising action, climax, falling action, and a resolution.')
    bot_instance.trainer.add_data('What are the elements of a plot?', 'A good story usually follows a narrative arc including an exposition, rising action, climax, falling action, and a resolution.')
    bot_instance.trainer.add_data('Explain narrative structure', 'A good story usually follows a narrative arc including an exposition, rising action, climax, falling action, and a resolution.')
    bot_instance.trainer.add_data('Tell me how to structure a book', 'A good story usually follows a narrative arc including an exposition, rising action, climax, falling action, and a resolution.')
    bot_instance.trainer.add_data('What makes a compelling tale?', 'A good story usually follows a narrative arc including an exposition, rising action, climax, falling action, and a resolution.')

# --- Geography (Mariana Trench) ---
    bot_instance.trainer.add_data('Where is the deepest place on Earth?', 'The Mariana Trench, located in the western Pacific Ocean, is the deepest known part of the Earth’s oceans.')
    bot_instance.trainer.add_data('How deep is the Mariana Trench?', 'The Mariana Trench, located in the western Pacific Ocean, is the deepest known part of the Earth’s oceans.')
    bot_instance.trainer.add_data('Tell me about the ocean floor', 'The Mariana Trench, located in the western Pacific Ocean, is the deepest known part of the Earth’s oceans.')
    bot_instance.trainer.add_data('What is the deepest trench?', 'The Mariana Trench, located in the western Pacific Ocean, is the deepest known part of the Earth’s oceans.')
    bot_instance.trainer.add_data('Facts about the Pacific abyss', 'The Mariana Trench, located in the western Pacific Ocean, is the deepest known part of the Earth’s oceans.')

# --- Tech (Virtual Reality) ---
    bot_instance.trainer.add_data('What is VR?', 'Virtual Reality (VR) is a simulated experience that can be similar to or completely different from the real world, typically using headsets.')
    bot_instance.trainer.add_data('Explain Virtual Reality', 'Virtual Reality (VR) is a simulated experience that can be similar to or completely different from the real world, typically using headsets.')
    bot_instance.trainer.add_data('How do VR headsets work?', 'Virtual Reality (VR) is a simulated experience that can be similar to or completely different from the real world, typically using headsets.')
    bot_instance.trainer.add_data('Is VR the same as AR?', 'Virtual Reality (VR) is a simulated experience that can be similar to or completely different from the real world, typically using headsets.')
    bot_instance.trainer.add_data('Describe immersive digital environments', 'Virtual Reality (VR) is a simulated experience that can be similar to or completely different from the real world, typically using headsets.')

# --- Daily Life (Coffee) ---
    bot_instance.trainer.add_data('How does coffee wake you up?', 'Caffeine works by blocking adenosine receptors in your brain, which prevents you from feeling tired and increases alertness.')
    bot_instance.trainer.add_data('Why does caffeine work?', 'Caffeine works by blocking adenosine receptors in your brain, which prevents you from feeling tired and increases alertness.')
    bot_instance.trainer.add_data('Explain the effect of coffee on the brain', 'Caffeine works by blocking adenosine receptors in your brain, which prevents you from feeling tired and increases alertness.')
    bot_instance.trainer.add_data('What does caffeine do?', 'Caffeine works by blocking adenosine receptors in your brain, which prevents you from feeling tired and increases alertness.')
    bot_instance.trainer.add_data('Why do I feel alert after tea?', 'Caffeine works by blocking adenosine receptors in your brain, which prevents you from feeling tired and increases alertness.')

# --- Programming (Lists vs Sets) ---
    bot_instance.trainer.add_data('Difference between list and set', 'In programming, a list is an ordered collection that allows duplicates, while a set is an unordered collection of unique elements.')
    bot_instance.trainer.add_data('When to use a set vs list', 'In programming, a list is an ordered collection that allows duplicates, while a set is an unordered collection of unique elements.')
    bot_instance.trainer.add_data('Explain coding collections', 'In programming, a list is an ordered collection that allows duplicates, while a set is an unordered collection of unique elements.')
    bot_instance.trainer.add_data('Are sets ordered?', 'In programming, a list is an ordered collection that allows duplicates, while a set is an unordered collection of unique elements.')
    bot_instance.trainer.add_data('Can lists have duplicates?', 'In programming, a list is an ordered collection that allows duplicates, while a set is an unordered collection of unique elements.')

# --- Environment (Climate Change) ---
    bot_instance.trainer.add_data('What causes climate change?', 'Climate change is mainly caused by human activities like burning fossil fuels, which release greenhouse gases into the atmosphere.')
    bot_instance.trainer.add_data('Explain global warming', 'Climate change is mainly caused by human activities like burning fossil fuels, which release greenhouse gases into the atmosphere.')
    bot_instance.trainer.add_data('Why is the planet getting hotter?', 'Climate change is mainly caused by human activities like burning fossil fuels, which release greenhouse gases into the atmosphere.')
    bot_instance.trainer.add_data('Impact of fossil fuels on weather', 'Climate change is mainly caused by human activities like burning fossil fuels, which release greenhouse gases into the atmosphere.')
    bot_instance.trainer.add_data('Tell me about the climate crisis', 'Climate change is mainly caused by human activities like burning fossil fuels, which release greenhouse gases into the atmosphere.')

# --- Culture (Renaissance Art) ---
    bot_instance.trainer.add_data('What are the features of Renaissance art?', 'Renaissance art is characterized by a focus on realism, human anatomy, perspective, and the use of light and shadow.')
    bot_instance.trainer.add_data('Tell me about Leonardo da Vincis style', 'Renaissance art is characterized by a focus on realism, human anatomy, perspective, and the use of light and shadow.')
    bot_instance.trainer.add_data('Why is the Renaissance famous?', 'Renaissance art is characterized by a focus on realism, human anatomy, perspective, and the use of light and shadow.')
    bot_instance.trainer.add_data('Explain art in the 15th century', 'Renaissance art is characterized by a focus on realism, human anatomy, perspective, and the use of light and shadow.')
    bot_instance.trainer.add_data('Who were the masters of realism?', 'Renaissance art is characterized by a focus on realism, human anatomy, perspective, and the use of light and shadow.')

# --- Self-Help (Habit Stacking) ---
    bot_instance.trainer.add_data('How to build new habits?', 'Habit stacking is a strategy where you pair a new habit you want to start with an existing habit you already do every day.')
    bot_instance.trainer.add_data('What is habit stacking?', 'Habit stacking is a strategy where you pair a new habit you want to start with an existing habit you already do every day.')
    bot_instance.trainer.add_data('Explain the pairing of routines', 'Habit stacking is a strategy where you pair a new habit you want to start with an existing habit you already do every day.')
    bot_instance.trainer.add_data('Tips for better discipline', 'Habit stacking is a strategy where you pair a new habit you want to start with an existing habit you already do every day.')
    bot_instance.trainer.add_data('How can I remember to do new tasks?', 'Habit stacking is a strategy where you pair a new habit you want to start with an existing habit you already do every day.')

# --- Math (Pi) ---
    bot_instance.trainer.add_data('What is Pi?', 'Pi is a mathematical constant representing the ratio of a circle’s circumference to its diameter, approximately equal to 3.14159.')
    bot_instance.trainer.add_data('Value of the constant pi', 'Pi is a mathematical constant representing the ratio of a circle’s circumference to its diameter, approximately equal to 3.14159.')
    bot_instance.trainer.add_data('Explain the ratio of a circle', 'Pi is a mathematical constant representing the ratio of a circle’s circumference to its diameter, approximately equal to 3.14159.')
    bot_instance.trainer.add_data('Why is 3.14 important?', 'Pi is a mathematical constant representing the ratio of a circle’s circumference to its diameter, approximately equal to 3.14159.')
    bot_instance.trainer.add_data('Tell me about the Greek letter pi', 'Pi is a mathematical constant representing the ratio of a circle’s circumference to its diameter, approximately equal to 3.14159.')

# --- Physics (Quantum Entanglement) ---
    bot_instance.trainer.add_data('What is quantum entanglement?', 'Quantum entanglement is a phenomenon where two particles become linked and share the same state, regardless of the distance between them.')
    bot_instance.trainer.add_data('Explain spooky action at a distance', 'Quantum entanglement is a phenomenon where two particles become linked and share the same state, regardless of the distance between them.')
    bot_instance.trainer.add_data('How do entangled particles work?', 'Quantum entanglement is a phenomenon where two particles become linked and share the same state, regardless of the distance between them.')
    bot_instance.trainer.add_data('Define quantum linking', 'Quantum entanglement is a phenomenon where two particles become linked and share the same state, regardless of the distance between them.')
    bot_instance.trainer.add_data('Tell me about subatomic connections', 'Quantum entanglement is a phenomenon where two particles become linked and share the same state, regardless of the distance between them.')

# --- Travel (Japan Etiquette) ---
    bot_instance.trainer.add_data('Tips for traveling to Japan', 'In Japan, it is important to bow when greeting, avoid tipping at restaurants, and remain quiet on public transportation.')
    bot_instance.trainer.add_data('Japanese social etiquette', 'In Japan, it is important to bow when greeting, avoid tipping at restaurants, and remain quiet on public transportation.')
    bot_instance.trainer.add_data('How to behave in Tokyo?', 'In Japan, it is important to bow when greeting, avoid tipping at restaurants, and remain quiet on public transportation.')
    bot_instance.trainer.add_data('Should I tip in Japan?', 'In Japan, it is important to bow when greeting, avoid tipping at restaurants, and remain quiet on public transportation.')
    bot_instance.trainer.add_data('Rules for tourists in Japan', 'In Japan, it is important to bow when greeting, avoid tipping at restaurants, and remain quiet on public transportation.')

# --- Biology (DNA) ---
    bot_instance.trainer.add_data('What is DNA?', 'DNA (Deoxyribonucleic acid) is the molecule that carries genetic instructions for the development and functioning of all known organisms.')
    bot_instance.trainer.add_data('Explain genetic code', 'DNA (Deoxyribonucleic acid) is the molecule that carries genetic instructions for the development and functioning of all known organisms.')
    bot_instance.trainer.add_data('How is hereditary information stored?', 'DNA (Deoxyribonucleic acid) is the molecule that carries genetic instructions for the development and functioning of all known organisms.')
    bot_instance.trainer.add_data('Tell me about the double helix', 'DNA (Deoxyribonucleic acid) is the molecule that carries genetic instructions for the development and functioning of all known organisms.')
    bot_instance.trainer.add_data('Function of deoxyribonucleic acid', 'DNA (Deoxyribonucleic acid) is the molecule that carries genetic instructions for the development and functioning of all known organisms.')

# --- Identity (Limits) ---
    bot_instance.trainer.add_data('Can you tell the future?', 'I cannot predict the future or perform physical actions, as I am an AI designed to process information and assist with tasks.')
    bot_instance.trainer.add_data('What are your limitations?', 'I cannot predict the future or perform physical actions, as I am an AI designed to process information and assist with tasks.')
    bot_instance.trainer.add_data('Can you clean my house?', 'I cannot predict the future or perform physical actions, as I am an AI designed to process information and assist with tasks.')
    bot_instance.trainer.add_data('Do you have a physical body?', 'I cannot predict the future or perform physical actions, as I am an AI designed to process information and assist with tasks.')
    bot_instance.trainer.add_data('What can’t you do?', 'I cannot predict the future or perform physical actions, as I am an AI designed to process information and assist with tasks.')

    # --- Chemistry (Acids and Bases) ---
    bot_instance.trainer.add_data('What is the pH scale?', 'The pH scale measures how acidic or basic a substance is, ranging from 0 to 14, with 7 being neutral.')
    bot_instance.trainer.add_data('Explain acidity and alkalinity', 'The pH scale measures how acidic or basic a substance is, ranging from 0 to 14, with 7 being neutral.')
    bot_instance.trainer.add_data('What does pH 7 mean?', 'The pH scale measures how acidic or basic a substance is, ranging from 0 to 14, with 7 being neutral.')
    bot_instance.trainer.add_data('Tell me about the acid-base scale', 'The pH scale measures how acidic or basic a substance is, ranging from 0 to 14, with 7 being neutral.')
    bot_instance.trainer.add_data('How do we measure how acidic something is?', 'The pH scale measures how acidic or basic a substance is, ranging from 0 to 14, with 7 being neutral.')

# --- Programming (SQL) ---
    bot_instance.trainer.add_data('What is SQL?', 'SQL (Structured Query Language) is the standard language used to manage and manipulate relational databases.')
    bot_instance.trainer.add_data('Explain database querying', 'SQL (Structured Query Language) is the standard language used to manage and manipulate relational databases.')
    bot_instance.trainer.add_data('How do I talk to a database?', 'SQL (Structured Query Language) is the standard language used to manage and manipulate relational databases.')
    bot_instance.trainer.add_data('Define Structured Query Language', 'SQL (Structured Query Language) is the standard language used to manage and manipulate relational databases.')
    bot_instance.trainer.add_data('What is a SQL query?', 'SQL (Structured Query Language) is the standard language used to manage and manipulate relational databases.')

# --- Physics (Newton's First Law) ---
    bot_instance.trainer.add_data('What is inertia?', 'Inertia is the tendency of an object to resist changes in its state of motion, as described by Newtons First Law.')
    bot_instance.trainer.add_data('Explain Newtons First Law', 'Inertia is the tendency of an object to resist changes in its state of motion, as described by Newtons First Law.')
    bot_instance.trainer.add_data('Why do objects keep moving?', 'Inertia is the tendency of an object to resist changes in its state of motion, as described by Newtons First Law.')
    bot_instance.trainer.add_data('Define the law of motion regarding rest', 'Inertia is the tendency of an object to resist changes in its state of motion, as described by Newtons First Law.')
    bot_instance.trainer.add_data('Tell me about resistance to motion', 'Inertia is the tendency of an object to resist changes in its state of motion, as described by Newtons First Law.')

# --- Health (Vaccines) ---
    bot_instance.trainer.add_data('How do vaccines work?', 'Vaccines train your immune system to recognize and fight specific pathogens by mimicking an infection without causing the disease.')
    bot_instance.trainer.add_data('Explain immunization', 'Vaccines train your immune system to recognize and fight specific pathogens by mimicking an infection without causing the disease.')
    bot_instance.trainer.add_data('What is the purpose of a vaccine?', 'Vaccines train your immune system to recognize and fight specific pathogens by mimicking an infection without causing the disease.')
    bot_instance.trainer.add_data('How does the body learn to fight viruses?', 'Vaccines train your immune system to recognize and fight specific pathogens by mimicking an infection without causing the disease.')
    bot_instance.trainer.add_data('Biology of vaccinations', 'Vaccines train your immune system to recognize and fight specific pathogens by mimicking an infection without causing the disease.')

# --- Technology (5G) ---
    bot_instance.trainer.add_data('What is 5G?', '5G is the fifth generation of mobile network technology, offering faster speeds, lower latency, and better connectivity than 4G.')
    bot_instance.trainer.add_data('Explain the 5th generation network', '5G is the fifth generation of mobile network technology, offering faster speeds, lower latency, and better connectivity than 4G.')
    bot_instance.trainer.add_data('Is 5G faster than 4G?', '5G is the fifth generation of mobile network technology, offering faster speeds, lower latency, and better connectivity than 4G.')
    bot_instance.trainer.add_data('Tell me about 5G benefits', '5G is the fifth generation of mobile network technology, offering faster speeds, lower latency, and better connectivity than 4G.')
    bot_instance.trainer.add_data('Define 5G technology', '5G is the fifth generation of mobile network technology, offering faster speeds, lower latency, and better connectivity than 4G.')

# --- Geography (Continents) ---
    bot_instance.trainer.add_data('How many continents are there?', 'Most geographical models recognize seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America.')
    bot_instance.trainer.add_data('List all the continents', 'Most geographical models recognize seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America.')
    bot_instance.trainer.add_data('Tell me the names of the continents', 'Most geographical models recognize seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America.')
    bot_instance.trainer.add_data('What are the 7 major landmasses?', 'Most geographical models recognize seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America.')
    bot_instance.trainer.add_data('Count the continents for me', 'Most geographical models recognize seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America.')

# --- Literature (Haiku) ---
    bot_instance.trainer.add_data('What is a haiku?', 'A haiku is a traditional form of Japanese poetry consisting of three lines with a syllable structure of 5-7-5.')
    bot_instance.trainer.add_data('Explain Japanese poetry structure', 'A haiku is a traditional form of Japanese poetry consisting of three lines with a syllable structure of 5-7-5.')
    bot_instance.trainer.add_data('How to write a haiku?', 'A haiku is a traditional form of Japanese poetry consisting of three lines with a syllable structure of 5-7-5.')
    bot_instance.trainer.add_data('What is the 5-7-5 rule?', 'A haiku is a traditional form of Japanese poetry consisting of three lines with a syllable structure of 5-7-5.')
    bot_instance.trainer.add_data('Define the haiku poem', 'A haiku is a traditional form of Japanese poetry consisting of three lines with a syllable structure of 5-7-5.')

# --- Finance (Compound Interest) ---
    bot_instance.trainer.add_data('What is compound interest?', 'Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.')
    bot_instance.trainer.add_data('Explain interest on interest', 'Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.')
    bot_instance.trainer.add_data('How does compounding work?', 'Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.')
    bot_instance.trainer.add_data('Why is compound interest powerful?', 'Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.')
    bot_instance.trainer.add_data('Formula for compound interest growth', 'Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.')

# --- Biology (Virus vs Bacteria) ---
    bot_instance.trainer.add_data('Difference between virus and bacteria?', 'Bacteria are complex, single-celled organisms that can live on their own, while viruses are smaller and need a host to survive.')
    bot_instance.trainer.add_data('Are viruses alive?', 'Bacteria are complex, single-celled organisms that can live on their own, while viruses are smaller and need a host to survive.')
    bot_instance.trainer.add_data('Compare bacteria and viruses', 'Bacteria are complex, single-celled organisms that can live on their own, while viruses are smaller and need a host to survive.')
    bot_instance.trainer.add_data('Do antibiotics kill viruses?', 'Bacteria are complex, single-celled organisms that can live on their own, while viruses are smaller and need a host to survive.')
    bot_instance.trainer.add_data('How do bacteria differ from viral infections?', 'Bacteria are complex, single-celled organisms that can live on their own, while viruses are smaller and need a host to survive.')

# --- Lifestyle (Minimalism) ---
    bot_instance.trainer.add_data('What is minimalism?', 'Minimalism is a lifestyle focused on living with less and prioritizing experiences and relationships over material possessions.')
    bot_instance.trainer.add_data('Explain the minimalist lifestyle', 'Minimalism is a lifestyle focused on living with less and prioritizing experiences and relationships over material possessions.')
    bot_instance.trainer.add_data('Benefits of living with less', 'Minimalism is a lifestyle focused on living with less and prioritizing experiences and relationships over material possessions.')
    bot_instance.trainer.add_data('How to be a minimalist?', 'Minimalism is a lifestyle focused on living with less and prioritizing experiences and relationships over material possessions.')
    bot_instance.trainer.add_data('Definition of minimalism in life', 'Minimalism is a lifestyle focused on living with less and prioritizing experiences and relationships over material possessions.')

# --- Programming (Frameworks) ---
    bot_instance.trainer.add_data('What is a coding framework?', 'A framework is a platform that provides a foundation for developing software applications, including pre-written code and tools.')
    bot_instance.trainer.add_data('Explain software frameworks', 'A framework is a platform that provides a foundation for developing software applications, including pre-written code and tools.')
    bot_instance.trainer.add_data('Why use a framework?', 'A framework is a platform that provides a foundation for developing software applications, including pre-written code and tools.')
    bot_instance.trainer.add_data('Define a programming framework', 'A framework is a platform that provides a foundation for developing software applications, including pre-written code and tools.')
    bot_instance.trainer.add_data('Difference between a library and a framework', 'A framework is a platform that provides a foundation for developing software applications, including pre-written code and tools.')

# --- Psychology (Growth Mindset) ---
    bot_instance.trainer.add_data('What is a growth mindset?', 'A growth mindset is the belief that abilities and intelligence can be developed through dedication, hard work, and learning.')
    bot_instance.trainer.add_data('Explain fixed vs growth mindset', 'A growth mindset is the belief that abilities and intelligence can be developed through dedication, hard work, and learning.')
    bot_instance.trainer.add_data('How to develop a growth mindset?', 'A growth mindset is the belief that abilities and intelligence can be developed through dedication, hard work, and learning.')
    bot_instance.trainer.add_data('Benefits of believing you can learn', 'A growth mindset is the belief that abilities and intelligence can be developed through dedication, hard work, and learning.')
    bot_instance.trainer.add_data('Who came up with growth mindset?', 'A growth mindset is the belief that abilities and intelligence can be developed through dedication, hard work, and learning.')

# --- History (World War I) ---
    bot_instance.trainer.add_data('When did WWI start?', 'World War I began on July 28, 1914, and lasted until November 11, 1918.')
    bot_instance.trainer.add_data('Duration of the Great War', 'World War I began on July 28, 1914, and lasted until November 11, 1918.')
    bot_instance.trainer.add_data('Dates of World War 1', 'World War I began on July 28, 1914, and lasted until November 11, 1918.')
    bot_instance.trainer.add_data('When was the armistice of WWI?', 'World War I began on July 28, 1914, and lasted until November 11, 1918.')
    bot_instance.trainer.add_data('History of the first world war timing', 'World War I began on July 28, 1914, and lasted until November 11, 1918.')

# --- Tech (Cryptocurrency Wallet) ---
    bot_instance.trainer.add_data('What is a crypto wallet?', 'A crypto wallet is a tool that allows you to interact with the blockchain and manage your digital assets using private and public keys.')
    bot_instance.trainer.add_data('How to store Bitcoin safely?', 'A crypto wallet is a tool that allows you to interact with the blockchain and manage your digital assets using private and public keys.')
    bot_instance.trainer.add_data('Explain private vs public keys', 'A crypto wallet is a tool that allows you to interact with the blockchain and manage your digital assets using private and public keys.')
    bot_instance.trainer.add_data('What is a digital wallet for coins?', 'A crypto wallet is a tool that allows you to interact with the blockchain and manage your digital assets using private and public keys.')
    bot_instance.trainer.add_data('Difference between hot and cold wallets', 'A crypto wallet is a tool that allows you to interact with the blockchain and manage your digital assets using private and public keys.')

# --- Science (The Big Bang) ---
    bot_instance.trainer.add_data('What is the Big Bang theory?', 'The Big Bang theory is the leading explanation for how the universe began, starting from a tiny, infinitely hot and dense point.')
    bot_instance.trainer.add_data('How did the universe start?', 'The Big Bang theory is the leading explanation for how the universe began, starting from a tiny, infinitely hot and dense point.')
    bot_instance.trainer.add_data('Explain the origin of the cosmos', 'The Big Bang theory is the leading explanation for how the universe began, starting from a tiny, infinitely hot and dense point.')
    bot_instance.trainer.add_data('What happened at the beginning of time?', 'The Big Bang theory is the leading explanation for how the universe began, starting from a tiny, infinitely hot and dense point.')
    bot_instance.trainer.add_data('Tell me about the cosmic expansion', 'The Big Bang theory is the leading explanation for how the universe began, starting from a tiny, infinitely hot and dense point.')

# --- Gardening (Composting) ---
    bot_instance.trainer.add_data('What is composting?', 'Composting is the natural process of recycling organic matter, like leaves and food scraps, into a valuable fertilizer.')
    bot_instance.trainer.add_data('How to make compost?', 'Composting is the natural process of recycling organic matter, like leaves and food scraps, into a valuable fertilizer.')
    bot_instance.trainer.add_data('Benefits of composting for soil', 'Composting is the natural process of recycling organic matter, like leaves and food scraps, into a valuable fertilizer.')
    bot_instance.trainer.add_data('What can I put in a compost bin?', 'Composting is the natural process of recycling organic matter, like leaves and food scraps, into a valuable fertilizer.')
    bot_instance.trainer.add_data('Explain organic recycling in gardens', 'Composting is the natural process of recycling organic matter, like leaves and food scraps, into a valuable fertilizer.')

# --- Art (Color Theory) ---
    bot_instance.trainer.add_data('What are primary colors?', 'Primary colors are the set of colors from which all other colors can be mixed: Red, Yellow, and Blue (in traditional art).')
    bot_instance.trainer.add_data('Explain the color wheel', 'Primary colors are the set of colors from which all other colors can be mixed: Red, Yellow, and Blue (in traditional art).')
    bot_instance.trainer.add_data('How to mix colors?', 'Primary colors are the set of colors from which all other colors can be mixed: Red, Yellow, and Blue (in traditional art).')
    bot_instance.trainer.add_data('What are secondary colors?', 'Primary colors are the set of colors from which all other colors can be mixed: Red, Yellow, and Blue (in traditional art).')
    bot_instance.trainer.add_data('Basic color theory for beginners', 'Primary colors are the set of colors from which all other colors can be mixed: Red, Yellow, and Blue (in traditional art).')

# --- Sociology (Social Norms) ---
    bot_instance.trainer.add_data('What are social norms?', 'Social norms are the unwritten rules of behavior that are considered acceptable in a group or society.')
    bot_instance.trainer.add_data('Explain societal rules', 'Social norms are the unwritten rules of behavior that are considered acceptable in a group or society.')
    bot_instance.trainer.add_data('Why do people follow social norms?', 'Social norms are the unwritten rules of behavior that are considered acceptable in a group or society.')
    bot_instance.trainer.add_data('Define cultural expectations', 'Social norms are the unwritten rules of behavior that are considered acceptable in a group or society.')
    bot_instance.trainer.add_data('Examples of social etiquette', 'Social norms are the unwritten rules of behavior that are considered acceptable in a group or society.')

# --- Ethics (The Golden Rule) ---
    bot_instance.trainer.add_data('What is the Golden Rule?', 'The Golden Rule is the principle of treating others as one would wish to be treated oneself.')
    bot_instance.trainer.add_data('Explain ethical reciprocity', 'The Golden Rule is the principle of treating others as one would wish to be treated oneself.')
    bot_instance.trainer.add_data('How should I treat others?', 'The Golden Rule is the principle of treating others as one would wish to be treated oneself.')
    bot_instance.trainer.add_data('Define the basic rule of morality', 'The Golden Rule is the principle of treating others as one would wish to be treated oneself.')
    bot_instance.trainer.add_data('Origins of the Golden Rule', 'The Golden Rule is the principle of treating others as one would wish to be treated oneself.')

# --- Closing (Feedback) ---
    bot_instance.trainer.add_data('I have a suggestion for you', 'Thank you for your feedback! I am always learning and I appreciate your help in making me better.')
    bot_instance.trainer.add_data('How can I improve this bot?', 'Thank you for your feedback! I am always learning and I appreciate your help in making me better.')
    bot_instance.trainer.add_data('You made a mistake', 'Thank you for your feedback! I am always learning and I appreciate your help in making me better.')
    bot_instance.trainer.add_data('Your answers are great', 'Thank you for your feedback! I am always learning and I appreciate your help in making me better.')
    bot_instance.trainer.add_data('Feedback for the AI', 'Thank you for your feedback! I am always learning and I appreciate your help in making me better.')

    # --- Astronomy (Exoplanets) ---
    bot_instance.trainer.add_data('What is an exoplanet?', 'An exoplanet is a planet that orbits a star outside our solar system.')
    bot_instance.trainer.add_data('Are there planets around other stars?', 'An exoplanet is a planet that orbits a star outside our solar system.')
    bot_instance.trainer.add_data('Define extrasolar planets', 'An exoplanet is a planet that orbits a star outside our solar system.')
    bot_instance.trainer.add_data('Tell me about planets in other galaxies', 'An exoplanet is a planet that orbits a star outside our solar system.')
    bot_instance.trainer.add_data('How do we find new worlds?', 'An exoplanet is a planet that orbits a star outside our solar system.')

# --- Programming (Recursion) ---
    bot_instance.trainer.add_data('What is recursion?', 'Recursion in programming is a method where the solution to a problem depends on solutions to smaller instances of the same problem, often involving a function calling itself.')
    bot_instance.trainer.add_data('Explain recursive functions', 'Recursion in programming is a method where the solution to a problem depends on solutions to smaller instances of the same problem, often involving a function calling itself.')
    bot_instance.trainer.add_data('How does a function call itself?', 'Recursion in programming is a method where the solution to a problem depends on solutions to smaller instances of the same problem, often involving a function calling itself.')
    bot_instance.trainer.add_data('Define recursion in computer science', 'Recursion in programming is a method where the solution to a problem depends on solutions to smaller instances of the same problem, often involving a function calling itself.')
    bot_instance.trainer.add_data('Why use recursion instead of loops?', 'Recursion in programming is a method where the solution to a problem depends on solutions to smaller instances of the same problem, often involving a function calling itself.')

# --- Economics (Inflation) ---
    bot_instance.trainer.add_data('What is inflation?', 'Inflation is the rate at which the general level of prices for goods and services is rising, and subsequently, purchasing power is falling.')
    bot_instance.trainer.add_data('Why do prices go up over time?', 'Inflation is the rate at which the general level of prices for goods and services is rising, and subsequently, purchasing power is falling.')
    bot_instance.trainer.add_data('Explain the decrease in purchasing power', 'Inflation is the rate at which the general level of prices for goods and services is rising, and subsequently, purchasing power is falling.')
    bot_instance.trainer.add_data('Define economic inflation', 'Inflation is the rate at which the general level of prices for goods and services is rising, and subsequently, purchasing power is falling.')
    bot_instance.trainer.add_data('What causes money to lose value?', 'Inflation is the rate at which the general level of prices for goods and services is rising, and subsequently, purchasing power is falling.')

# --- Cybersecurity (Phishing) ---
    bot_instance.trainer.add_data('What is phishing?', 'Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers, through deceptive emails or websites.')
    bot_instance.trainer.add_data('How do hackers steal passwords via email?', 'Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers, through deceptive emails or websites.')
    bot_instance.trainer.add_data('Explain email scams', 'Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers, through deceptive emails or websites.')
    bot_instance.trainer.add_data('Define phishing attacks', 'Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers, through deceptive emails or websites.')
    bot_instance.trainer.add_data('How can I recognize a fake website?', 'Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers, through deceptive emails or websites.')

# --- Biology (Enzymes) ---
    bot_instance.trainer.add_data('What are enzymes?', 'Enzymes are proteins that act as biological catalysts, accelerating chemical reactions within living organisms without being consumed in the process.')
    bot_instance.trainer.add_data('How do biological catalysts work?', 'Enzymes are proteins that act as biological catalysts, accelerating chemical reactions within living organisms without being consumed in the process.')
    bot_instance.trainer.add_data('Function of enzymes in the body', 'Enzymes are proteins that act as biological catalysts, accelerating chemical reactions within living organisms without being consumed in the process.')
    bot_instance.trainer.add_data('Explain enzyme activity', 'Enzymes are proteins that act as biological catalysts, accelerating chemical reactions within living organisms without being consumed in the process.')
    bot_instance.trainer.add_data('Why are enzymes important for digestion?', 'Enzymes are proteins that act as biological catalysts, accelerating chemical reactions within living organisms without being consumed in the process.')

# --- Psychology (Maslows Hierarchy) ---
    bot_instance.trainer.add_data('What is Maslows Hierarchy of Needs?', 'It is a motivational theory in psychology comprising a five-tier model of human needs, often depicted as hierarchical levels within a pyramid.')
    bot_instance.trainer.add_data('Explain the pyramid of human needs', 'It is a motivational theory in psychology comprising a five-tier model of human needs, often depicted as hierarchical levels within a pyramid.')
    bot_instance.trainer.add_data('Tell me about Abraham Maslows theory', 'It is a motivational theory in psychology comprising a five-tier model of human needs, often depicted as hierarchical levels within a pyramid.')
    bot_instance.trainer.add_data('What are the 5 levels of needs?', 'It is a motivational theory in psychology comprising a five-tier model of human needs, often depicted as hierarchical levels within a pyramid.')
    bot_instance.trainer.add_data('Define self-actualization in Maslows theory', 'It is a motivational theory in psychology comprising a five-tier model of human needs, often depicted as hierarchical levels within a pyramid.')

# --- Technology (Blockchain Mining) ---
    bot_instance.trainer.add_data('What is crypto mining?', 'Crypto mining is the process by which new units of cryptocurrency are created and transactions are verified using powerful computers to solve complex mathematical problems.')
    bot_instance.trainer.add_data('How are new Bitcoins made?', 'Crypto mining is the process by which new units of cryptocurrency are created and transactions are verified using powerful computers to solve complex mathematical problems.')
    bot_instance.trainer.add_data('Explain proof of work', 'Crypto mining is the process by which new units of cryptocurrency are created and transactions are verified using powerful computers to solve complex mathematical problems.')
    bot_instance.trainer.add_data('Why does mining require so much energy?', 'Crypto mining is the process by which new units of cryptocurrency are created and transactions are verified using powerful computers to solve complex mathematical problems.')
    bot_instance.trainer.add_data('Define the mining process in blockchain', 'Crypto mining is the process by which new units of cryptocurrency are created and transactions are verified using powerful computers to solve complex mathematical problems.')

# --- Literature (Protagonist vs Antagonist) ---
    bot_instance.trainer.add_data('Difference between protagonist and antagonist?', 'The protagonist is the main character or "hero" of the story, while the antagonist is the character or force that opposes them.')
    bot_instance.trainer.add_data('Who is the hero of a story?', 'The protagonist is the main character or "hero" of the story, while the antagonist is the character or force that opposes them.')
    bot_instance.trainer.add_data('Define the villain in literature', 'The protagonist is the main character or "hero" of the story, while the antagonist is the character or force that opposes them.')
    bot_instance.trainer.add_data('Explain character conflict', 'The protagonist is the main character or "hero" of the story, while the antagonist is the character or force that opposes them.')
    bot_instance.trainer.add_data('What do we call the main character?', 'The protagonist is the main character or "hero" of the story, while the antagonist is the character or force that opposes them.')

# --- Physics (Dark Matter) ---
    bot_instance.trainer.add_data('What is dark matter?', 'Dark matter is a hypothetical form of matter that does not emit or reflect light, but is believed to make up about 27% of the universe based on its gravitational effects.')
    bot_instance.trainer.add_data('Explain the invisible matter in the universe', 'Dark matter is a hypothetical form of matter that does not emit or reflect light, but is believed to make up about 27% of the universe based on its gravitational effects.')
    bot_instance.trainer.add_data('Why do we think dark matter exists?', 'Dark matter is a hypothetical form of matter that does not emit or reflect light, but is believed to make up about 27% of the universe based on its gravitational effects.')
    bot_instance.trainer.add_data('Define dark matter in cosmology', 'Dark matter is a hypothetical form of matter that does not emit or reflect light, but is believed to make up about 27% of the universe based on its gravitational effects.')
    bot_instance.trainer.add_data('What makes up the majority of the universe?', 'Dark matter is a hypothetical form of matter that does not emit or reflect light, but is believed to make up about 27% of the universe based on its gravitational effects.')

# --- Environment (Renewable Energy) ---
    bot_instance.trainer.add_data('What is renewable energy?', 'Renewable energy is energy derived from natural sources that are replenished at a higher rate than they are consumed, such as solar, wind, and hydro power.')
    bot_instance.trainer.add_data('Explain green energy', 'Renewable energy is energy derived from natural sources that are replenished at a higher rate than they are consumed, such as solar, wind, and hydro power.')
    bot_instance.trainer.add_data('List types of clean energy', 'Renewable energy is energy derived from natural sources that are replenished at a higher rate than they are consumed, such as solar, wind, and hydro power.')
    bot_instance.trainer.add_data('Why is solar power renewable?', 'Renewable energy is energy derived from natural sources that are replenished at a higher rate than they are consumed, such as solar, wind, and hydro power.')
    bot_instance.trainer.add_data('Define sustainable energy sources', 'Renewable energy is energy derived from natural sources that are replenished at a higher rate than they are consumed, such as solar, wind, and hydro power.')

# --- Programming (Boolean Logic) ---
    bot_instance.trainer.add_data('What is a Boolean?', 'In computer science, a Boolean is a data type that has one of two possible values: True or False.')
    bot_instance.trainer.add_data('Explain true/false logic in code', 'In computer science, a Boolean is a data type that has one of two possible values: True or False.')
    bot_instance.trainer.add_data('What are boolean operators?', 'In computer science, a Boolean is a data type that has one of two possible values: True or False.')
    bot_instance.trainer.add_data('Define the bool type', 'In computer science, a Boolean is a data type that has one of two possible values: True or False.')
    bot_instance.trainer.add_data('How do computers make decisions?', 'In computer science, a Boolean is a data type that has one of two possible values: True or False.')

# --- Health (Metabolism) ---
    bot_instance.trainer.add_data('What is metabolism?', 'Metabolism is the chemical process that occurs within a living organism in order to maintain life, specifically the conversion of food into energy.')
    bot_instance.trainer.add_data('Explain metabolic rate', 'Metabolism is the chemical process that occurs within a living organism in order to maintain life, specifically the conversion of food into energy.')
    bot_instance.trainer.add_data('How does the body burn calories?', 'Metabolism is the chemical process that occurs within a living organism in order to maintain life, specifically the conversion of food into energy.')
    bot_instance.trainer.add_data('Why do some people have fast metabolism?', 'Metabolism is the chemical process that occurs within a living organism in order to maintain life, specifically the conversion of food into energy.')
    bot_instance.trainer.add_data('Define biological energy conversion', 'Metabolism is the chemical process that occurs within a living organism in order to maintain life, specifically the conversion of food into energy.')

# --- History (The Great Depression) ---
    bot_instance.trainer.add_data('What was the Great Depression?', 'The Great Depression was a severe worldwide economic depression that took place mostly during the 1930s, beginning in the United States.')
    bot_instance.trainer.add_data('When did the stock market crash in 1929?', 'The Great Depression was a severe worldwide economic depression that took place mostly during the 1930s, beginning in the United States.')
    bot_instance.trainer.add_data('Explain the 1930s economic crisis', 'The Great Depression was a severe worldwide economic depression that took place mostly during the 1930s, beginning in the United States.')
    bot_instance.trainer.add_data('History of the global depression', 'The Great Depression was a severe worldwide economic depression that took place mostly during the 1930s, beginning in the United States.')
    bot_instance.trainer.add_data('What caused the Great Depression?', 'The Great Depression was a severe worldwide economic depression that took place mostly during the 1930s, beginning in the United States.')

# --- Sociology (Globalization) ---
    bot_instance.trainer.add_data('What is globalization?', 'Globalization is the process of interaction and integration among people, companies, and governments worldwide, primarily driven by trade and technology.')
    bot_instance.trainer.add_data('Explain the global economy connection', 'Globalization is the process of interaction and integration among people, companies, and governments worldwide, primarily driven by trade and technology.')
    bot_instance.trainer.add_data('Why is the world more connected now?', 'Globalization is the process of interaction and integration among people, companies, and governments worldwide, primarily driven by trade and technology.')
    bot_instance.trainer.add_data('Define international integration', 'Globalization is the process of interaction and integration among people, companies, and governments worldwide, primarily driven by trade and technology.')
    bot_instance.trainer.add_data('Pros and cons of globalization', 'Globalization is the process of interaction and integration among people, companies, and governments worldwide, primarily driven by trade and technology.')

# --- Science (Radioactivity) ---
    bot_instance.trainer.add_data('What is radioactivity?', 'Radioactivity is the process by which an unstable atomic nucleus loses energy by radiation.')
    bot_instance.trainer.add_data('Explain nuclear decay', 'Radioactivity is the process by which an unstable atomic nucleus loses energy by radiation.')
    bot_instance.trainer.add_data('How does radiation work?', 'Radioactivity is the process by which an unstable atomic nucleus loses energy by radiation.')
    bot_instance.trainer.add_data('Define radioactive elements', 'Radioactivity is the process by which an unstable atomic nucleus loses energy by radiation.')
    bot_instance.trainer.add_data('Who discovered radioactivity?', 'Radioactivity is the process by which an unstable atomic nucleus loses energy by radiation.')

# --- Philosophy (The Trolley Problem) ---
    bot_instance.trainer.add_data('What is the Trolley Problem?', 'The Trolley Problem is a thought experiment in ethics about whether it is permissible to sacrifice one person to save a larger number of people.')
    bot_instance.trainer.add_data('Explain the moral dilemma of the train', 'The Trolley Problem is a thought experiment in ethics about whether it is permissible to sacrifice one person to save a larger number of people.')
    bot_instance.trainer.add_data('Tell me about utilitarianism vs deontology', 'The Trolley Problem is a thought experiment in ethics about whether it is permissible to sacrifice one person to save a larger number of people.')
    bot_instance.trainer.add_data('What is the 5 people vs 1 person ethics test?', 'The Trolley Problem is a thought experiment in ethics about whether it is permissible to sacrifice one person to save a larger number of people.')
    bot_instance.trainer.add_data('Define this famous ethical thought experiment', 'The Trolley Problem is a thought experiment in ethics about whether it is permissible to sacrifice one person to save a larger number of people.')

# --- Geography (Time Zones) ---
    bot_instance.trainer.add_data('How do time zones work?', 'Time zones are regions of the Earth that observe a uniform standard time for legal, commercial, and social purposes, usually based on longitude.')
    bot_instance.trainer.add_data('Why is it a different time in other countries?', 'Time zones are regions of the Earth that observe a uniform standard time for legal, commercial, and social purposes, usually based on longitude.')
    bot_instance.trainer.add_data('Explain GMT and UTC', 'Time zones are regions of the Earth that observe a uniform standard time for legal, commercial, and social purposes, usually based on longitude.')
    bot_instance.trainer.add_data('How many time zones are there?', 'Time zones are regions of the Earth that observe a uniform standard time for legal, commercial, and social purposes, usually based on longitude.')
    bot_instance.trainer.add_data('Define the International Date Line', 'Time zones are regions of the Earth that observe a uniform standard time for legal, commercial, and social purposes, usually based on longitude.')

# --- Lifestyle (Sleep Cycles) ---
    bot_instance.trainer.add_data('What are REM and deep sleep?', 'Sleep consists of cycles of REM (Rapid Eye Movement) sleep, associated with dreaming, and non-REM sleep, which includes deep, restorative sleep.')
    bot_instance.trainer.add_data('Explain the stages of sleep', 'Sleep consists of cycles of REM (Rapid Eye Movement) sleep, associated with dreaming, and non-REM sleep, which includes deep, restorative sleep.')
    bot_instance.trainer.add_data('Why do we dream?', 'Sleep consists of cycles of REM (Rapid Eye Movement) sleep, associated with dreaming, and non-REM sleep, which includes deep, restorative sleep.')
    bot_instance.trainer.add_data('What is restorative sleep?', 'Sleep consists of cycles of REM (Rapid Eye Movement) sleep, associated with dreaming, and non-REM sleep, which includes deep, restorative sleep.')
    bot_instance.trainer.add_data('How long is a sleep cycle?', 'Sleep consists of cycles of REM (Rapid Eye Movement) sleep, associated with dreaming, and non-REM sleep, which includes deep, restorative sleep.')

# --- Tech (Open Source) ---
    bot_instance.trainer.add_data('What is open source software?', 'Open source software is software with source code that anyone can inspect, modify, and enhance.')
    bot_instance.trainer.add_data('Explain the open source movement', 'Open source software is software with source code that anyone can inspect, modify, and enhance.')
    bot_instance.trainer.add_data('What is the difference between open and closed source?', 'Open source software is software with source code that anyone can inspect, modify, and enhance.')
    bot_instance.trainer.add_data('Why is Linux open source?', 'Open source software is software with source code that anyone can inspect, modify, and enhance.')
    bot_instance.trainer.add_data('Define free and open software', 'Open source software is software with source code that anyone can inspect, modify, and enhance.')

# --- Gratitude (Closing) ---
    bot_instance.trainer.add_data('You are the best!', 'That is very kind of you! I am here to help. Feel free to ask anything else.')
    bot_instance.trainer.add_data('Great job bot', 'That is very kind of you! I am here to help. Feel free to ask anything else.')
    bot_instance.trainer.add_data('I am impressed with your answers', 'That is very kind of you! I am here to help. Feel free to ask anything else.')
    bot_instance.trainer.add_data('Thanks for the amazing help', 'That is very kind of you! I am here to help. Feel free to ask anything else.')
    bot_instance.trainer.add_data('You are so smart', 'That is very kind of you! I am here to help. Feel free to ask anything else.')

    # --- Biology (Mitochondria) ---
    bot_instance.trainer.add_data('What is the function of mitochondria?', 'Mitochondria are known as the powerhouse of the cell, responsible for generating most of the cells supply of adenosine triphosphate (ATP).')
    bot_instance.trainer.add_data('Explain the powerhouse of the cell', 'Mitochondria are known as the powerhouse of the cell, responsible for generating most of the cells supply of adenosine triphosphate (ATP).')
    bot_instance.trainer.add_data('How do cells produce energy?', 'Mitochondria are known as the powerhouse of the cell, responsible for generating most of the cells supply of adenosine triphosphate (ATP).')
    bot_instance.trainer.add_data('Define mitochondria in biology', 'Mitochondria are known as the powerhouse of the cell, responsible for generating most of the cells supply of adenosine triphosphate (ATP).')
    bot_instance.trainer.add_data('What is ATP production?', 'Mitochondria are known as the powerhouse of the cell, responsible for generating most of the cells supply of adenosine triphosphate (ATP).')

# --- Engineering (The 4-Stroke Engine) ---
    bot_instance.trainer.add_data('How does a 4-stroke engine work?', 'A four-stroke engine operates in four stages: intake, compression, power (combustion), and exhaust.')
    bot_instance.trainer.add_data('Explain the cycles of an internal combustion engine', 'A four-stroke engine operates in four stages: intake, compression, power (combustion), and exhaust.')
    bot_instance.trainer.add_data('What are the 4 stages of a car engine?', 'A four-stroke engine operates in four stages: intake, compression, power (combustion), and exhaust.')
    bot_instance.trainer.add_data('Define intake compression power and exhaust', 'A four-stroke engine operates in four stages: intake, compression, power (combustion), and exhaust.')
    bot_instance.trainer.add_data('Tell me about piston engine cycles', 'A four-stroke engine operates in four strokes: intake, compression, power (combustion), and exhaust.')

# --- Psychology (Placebo Effect) ---
    bot_instance.trainer.add_data('What is the placebo effect?', 'The placebo effect is a phenomenon where a persons health improves after taking a "dummy" treatment, simply because they believe it will work.')
    bot_instance.trainer.add_data('Explain the power of belief in medicine', 'The placebo effect is a phenomenon where a persons health improves after taking a "dummy" treatment, simply because they believe it will work.')
    bot_instance.trainer.add_data('Why do sugar pills sometimes work?', 'The placebo effect is a phenomenon where a persons health improves after taking a "dummy" treatment, simply because they believe it will work.')
    bot_instance.trainer.add_data('Define the placebo phenomenon', 'The placebo effect is a phenomenon where a persons health improves after taking a "dummy" treatment, simply because they believe it will work.')
    bot_instance.trainer.add_data('Can the mind heal the body through expectation?', 'The placebo effect is a phenomenon where a persons health improves after taking a "dummy" treatment, simply because they believe it will work.')

# --- Programming (Docker/Containers) ---
    bot_instance.trainer.add_data('What is Docker?', 'Docker is a platform that uses virtualization to deliver software in packages called containers, which include all necessary libraries and dependencies.')
    bot_instance.trainer.add_data('Explain containerization in software', 'Docker is a platform that uses virtualization to deliver software in packages called containers, which include all necessary libraries and dependencies.')
    bot_instance.trainer.add_data('How do Docker containers work?', 'Docker is a platform that uses virtualization to deliver software in packages called containers, which include all necessary libraries and dependencies.')
    bot_instance.trainer.add_data('Why use containers instead of VMs?', 'Docker is a platform that uses virtualization to deliver software in packages called containers, which include all necessary libraries and dependencies.')
    bot_instance.trainer.add_data('Define Docker for developers', 'Docker is a platform that uses virtualization to deliver software in packages called containers, which include all necessary libraries and dependencies.')

# --- Physics (Nuclear Fusion) ---
    bot_instance.trainer.add_data('What is nuclear fusion?', 'Nuclear fusion is the process where two light atomic nuclei combine to form a heavier nucleus, releasing vast amounts of energy.')
    bot_instance.trainer.add_data('How do stars produce energy?', 'Nuclear fusion is the process where two light atomic nuclei combine to form a heavier nucleus, releasing vast amounts of energy.')
    bot_instance.trainer.add_data('Explain fusion vs fission', 'Nuclear fusion is the process where two light atomic nuclei combine to form a heavier nucleus, releasing vast amounts of energy.')
    bot_instance.trainer.add_data('Define the process that powers the Sun', 'Nuclear fusion is the process where two light atomic nuclei combine to form a heavier nucleus, releasing vast amounts of energy.')
    bot_instance.trainer.add_data('Will we ever have fusion power?', 'Nuclear fusion is the process where two light atomic nuclei combine to form a heavier nucleus, releasing vast amounts of energy.')

# --- History (The Magna Carta) ---
    bot_instance.trainer.add_data('What is the Magna Carta?', 'The Magna Carta, issued in 1215, is a landmark document that established the principle that everyone, including the king, is subject to the law.')
    bot_instance.trainer.add_data('Why is the Great Charter famous?', 'The Magna Carta, issued in 1215, is a landmark document that established the principle that everyone, including the king, is subject to the law.')
    bot_instance.trainer.add_data('Tell me about the origins of modern law', 'The Magna Carta, issued in 1215, is a landmark document that established the principle that everyone, including the king, is subject to the law.')
    bot_instance.trainer.add_data('Who signed the Magna Carta?', 'The Magna Carta, issued in 1215, is a landmark document that established the principle that everyone, including the king, is subject to the law.')
    bot_instance.trainer.add_data('Explain the 1215 English law document', 'The Magna Carta, issued in 1215, is a landmark document that established the principle that everyone, including the king, is subject to the law.')

# --- Technology (Edge Computing) ---
    bot_instance.trainer.add_data('What is edge computing?', 'Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data, such as IoT devices.')
    bot_instance.trainer.add_data('Explain computing at the edge', 'Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data, such as IoT devices.')
    bot_instance.trainer.add_data('How does edge differ from cloud computing?', 'Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data, such as IoT devices.')
    bot_instance.trainer.add_data('Benefits of processing data locally', 'Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data, such as IoT devices.')
    bot_instance.trainer.add_data('Define the edge network concept', 'Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data, such as IoT devices.')

# --- Environment (The Ozone Layer) ---
    bot_instance.trainer.add_data('What is the ozone layer?', 'The ozone layer is a region of Earths stratosphere that absorbs most of the Suns harmful ultraviolet (UV) radiation.')
    bot_instance.trainer.add_data('Why is the ozone layer important?', 'The ozone layer is a region of Earths stratosphere that absorbs most of the Suns harmful ultraviolet (UV) radiation.')
    bot_instance.trainer.add_data('Explain the ozone hole', 'The ozone layer is a region of Earths stratosphere that absorbs most of the Suns harmful ultraviolet (UV) radiation.')
    bot_instance.trainer.add_data('What protects us from UV rays?', 'The ozone layer is a region of Earths stratosphere that absorbs most of the Suns harmful ultraviolet (UV) radiation.')
    bot_instance.trainer.add_data('Define the stratospheric ozone', 'The ozone layer is a region of Earths stratosphere that absorbs most of the Suns harmful ultraviolet (UV) radiation.')

# --- Health (Antibiotic Resistance) ---
    bot_instance.trainer.add_data('What is antibiotic resistance?', 'Antibiotic resistance occurs when bacteria evolve so that antibiotics no longer work to kill them or stop their growth.')
    bot_instance.trainer.add_data('Why are superbugs dangerous?', 'Antibiotic resistance occurs when bacteria evolve so that antibiotics no longer work to kill them or stop their growth.')
    bot_instance.trainer.add_data('Explain the misuse of antibiotics', 'Antibiotic resistance occurs when bacteria evolve so that antibiotics no longer work to kill them or stop their growth.')
    bot_instance.trainer.add_data('How do bacteria survive medication?', 'Antibiotic resistance occurs when bacteria evolve so that antibiotics no longer work to kill them or stop their growth.')
    bot_instance.trainer.add_data('Define the global threat of drug-resistant bacteria', 'Antibiotic resistance occurs when bacteria evolve so that antibiotics no longer work to kill them or stop their growth.')

# --- Finance (Exchange-Traded Funds) ---
    bot_instance.trainer.add_data('What is an ETF?', 'An ETF (Exchange-Traded Fund) is a type of investment fund that is traded on stock exchanges, much like individual stocks.')
    bot_instance.trainer.add_data('Explain Exchange-Traded Funds', 'An ETF (Exchange-Traded Fund) is a type of investment fund that is traded on stock exchanges, much like individual stocks.')
    bot_instance.trainer.add_data('How do ETFs work?', 'An ETF (Exchange-Traded Fund) is a type of investment fund that is traded on stock exchanges, much like individual stocks.')
    bot_instance.trainer.add_data('Difference between a mutual fund and an ETF', 'An ETF (Exchange-Traded Fund) is a type of investment fund that is traded on stock exchanges, much like individual stocks.')
    bot_instance.trainer.add_data('Why are ETFs popular for investing?', 'An ETF (Exchange-Traded Fund) is a type of investment fund that is traded on stock exchanges, much like individual stocks.')

# --- Sociology (The Digital Divide) ---
    bot_instance.trainer.add_data('What is the digital divide?', 'The digital divide refers to the gap between demographics and regions that have access to modern information technology and those that don’t.')
    bot_instance.trainer.add_data('Explain inequality in internet access', 'The digital divide refers to the gap between demographics and regions that have access to modern information technology and those that don’t.')
    bot_instance.trainer.add_data('Why do some people lack tech access?', 'The digital divide refers to the gap between demographics and regions that have access to modern information technology and those that don’t.')
    bot_instance.trainer.add_data('Define the technological gap in society', 'The digital divide refers to the gap between demographics and regions that have access to modern information technology and those that don’t.')
    bot_instance.trainer.add_data('How does the digital divide affect education?', 'The digital divide refers to the gap between demographics and regions that have access to modern information technology and those that don’t.')

# --- Space (The Voyager Probes) ---
    bot_instance.trainer.add_data('What are the Voyager spacecraft?', 'The Voyager 1 and 2 probes were launched in 1977 to study the outer planets and are now the farthest human-made objects in space.')
    bot_instance.trainer.add_data('Tell me about the Golden Record in space', 'The Voyager 1 and 2 probes were launched in 1977 to study the outer planets and are now the farthest human-made objects in space.')
    bot_instance.trainer.add_data('Which probe has left the solar system?', 'The Voyager 1 and 2 probes were launched in 1977 to study the outer planets and are now the farthest human-made objects in space.')
    bot_instance.trainer.add_data('History of the Voyager mission', 'The Voyager 1 and 2 probes were launched in 1977 to study the outer planets and are now the farthest human-made objects in space.')
    bot_instance.trainer.add_data('Where are Voyager 1 and 2 now?', 'The Voyager 1 and 2 probes were launched in 1977 to study the outer planets and are now the farthest human-made objects in space.')

# --- Programming (Garbage Collection) ---
    bot_instance.trainer.add_data('What is garbage collection in programming?', 'Garbage collection is an automatic memory management process that reclaims memory occupied by objects that are no longer in use.')
    bot_instance.trainer.add_data('Explain automatic memory management', 'Garbage collection is an automatic memory management process that reclaims memory occupied by objects that are no longer in use.')
    bot_instance.trainer.add_data('How does Java or Python manage memory?', 'Garbage collection is an automatic memory management process that reclaims memory occupied by objects that are no longer in use.')
    bot_instance.trainer.add_data('Define memory reclamation', 'Garbage collection is an automatic memory management process that reclaims memory occupied by objects that are no longer in use.')
    bot_instance.trainer.add_data('Why is garbage collection useful?', 'Garbage collection is an automatic memory management process that reclaims memory occupied by objects that are no longer in use.')

# --- Literature (Sonnet) ---
    bot_instance.trainer.add_data('What is a sonnet?', 'A sonnet is a fourteen-line poem written in iambic pentameter, often associated with themes of love.')
    bot_instance.trainer.add_data('Explain the structure of a Shakespearean sonnet', 'A sonnet is a fourteen-line poem written in iambic pentameter, often associated with themes of love.')
    bot_instance.trainer.add_data('How many lines in a sonnet?', 'A sonnet is a fourteen-line poem written in iambic pentameter, often associated with themes of love.')
    bot_instance.trainer.add_data('Define iambic pentameter in poetry', 'A sonnet is a fourteen-line poem written in iambic pentameter, often associated with themes of love.')
    bot_instance.trainer.add_data('Tell me about 14-line poems', 'A sonnet is a fourteen-line poem written in iambic pentameter, often associated with themes of love.')

# --- Science (Photosynthesis - Dark Reactions) ---
    bot_instance.trainer.add_data('What is the Calvin Cycle?', 'The Calvin Cycle is the set of chemical reactions in photosynthesis that do not require light and convert CO2 into glucose.')
    bot_instance.trainer.add_data('Explain the dark reactions of photosynthesis', 'The Calvin Cycle is the set of chemical reactions in photosynthesis that do not require light and convert CO2 into glucose.')
    bot_instance.trainer.add_data('How do plants make sugar without light?', 'The Calvin Cycle is the set of chemical reactions in photosynthesis that do not require light and convert CO2 into glucose.')
    bot_instance.trainer.add_data('Define the CO2 fixation process', 'The Calvin Cycle is the set of chemical reactions in photosynthesis that do not require light and convert CO2 into glucose.')
    bot_instance.trainer.add_data('Calvin Cycle vs Light reactions', 'The Calvin Cycle is the set of chemical reactions in photosynthesis that do not require light and convert CO2 into glucose.')

# --- Psychology (The Bystander Effect) ---
    bot_instance.trainer.add_data('What is the bystander effect?', 'The bystander effect is a social psychological theory that states individuals are less likely to offer help to a victim when other people are present.')
    bot_instance.trainer.add_data('Explain the diffusion of responsibility', 'The bystander effect is a social psychological theory that states individuals are less likely to offer help to a victim when other people are present.')
    bot_instance.trainer.add_data('Why dont people help in crowds?', 'The bystander effect is a social psychological theory that states individuals are less likely to offer help to a victim when other people are present.')
    bot_instance.trainer.add_data('Define the witness apathy phenomenon', 'The bystander effect is a social psychological theory that states individuals are less likely to offer help to a victim when other people are present.')
    bot_instance.trainer.add_data('Tell me about the social psychology of helping', 'The bystander effect is a social psychological theory that states individuals are less likely to offer help to a victim when other people are present.')

# --- Technology (Natural Language Processing) ---
    bot_instance.trainer.add_data('What is NLP?', 'Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and human language.')
    bot_instance.trainer.add_data('Explain how computers understand speech', 'Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and human language.')
    bot_instance.trainer.add_data('Define Natural Language Processing', 'Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and human language.')
    bot_instance.trainer.add_data('How do chatbots process text?', 'Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and human language.')
    bot_instance.trainer.add_data('Tell me about machine translation technology', 'Natural Language Processing (NLP) is a branch of AI that focuses on the interaction between computers and human language.')

# --- Logic (Occams Razor) ---
    bot_instance.trainer.add_data('What is Occams Razor?', 'Occams Razor is the problem-solving principle that states the simplest explanation is usually the correct one.')
    bot_instance.trainer.add_data('Explain the principle of parsimony', 'Occams Razor is the problem-solving principle that states the simplest explanation is usually the correct one.')
    bot_instance.trainer.add_data('Why is the simplest answer often right?', 'Occams Razor is the problem-solving principle that states the simplest explanation is usually the correct one.')
    bot_instance.trainer.add_data('Define the razor principle in logic', 'Occams Razor is the problem-solving principle that states the simplest explanation is usually the correct one.')
    bot_instance.trainer.add_data('Who came up with Occams Razor?', 'Occams Razor is the problem-solving principle that states the simplest explanation is usually the correct one.')

# --- History (The Silk Road) ---
    bot_instance.trainer.add_data('What was the Silk Road?', 'The Silk Road was an ancient network of trade routes that connected the East and West, facilitating cultural and economic exchange.')
    bot_instance.trainer.add_data('How did China trade with Europe in ancient times?', 'The Silk Road was an ancient network of trade routes that connected the East and West, facilitating cultural and economic exchange.')
    bot_instance.trainer.add_data('Explain the ancient trade routes', 'The Silk Road was an ancient network of trade routes that connected the East and West, facilitating cultural and economic exchange.')
    bot_instance.trainer.add_data('Tell me about the Silk Road history', 'The Silk Road was an ancient network of trade routes that connected the East and West, facilitating cultural and economic exchange.')
    bot_instance.trainer.add_data('What was traded on the Silk Road?', 'The Silk Road was an ancient network of trade routes that connected the East and West, facilitating cultural and economic exchange.')

# --- Daily Life (Cooking - Maillard Reaction) ---
    bot_instance.trainer.add_data('What is the Maillard reaction?', 'The Maillard reaction is a chemical reaction between amino acids and reducing sugars that gives browned food its distinctive flavor.')
    bot_instance.trainer.add_data('Why does steak turn brown?', 'The Maillard reaction is a chemical reaction between amino acids and reducing sugars that gives browned food its distinctive flavor.')
    bot_instance.trainer.add_data('Explain the science of browning food', 'The Maillard reaction is a chemical reaction between amino acids and reducing sugars that gives browned food its distinctive flavor.')
    bot_instance.trainer.add_data('Define the flavor reaction in cooking', 'The Maillard reaction is a chemical reaction between amino acids and reducing sugars that gives browned food its distinctive flavor.')
    bot_instance.trainer.add_data('How do crusts form on bread?', 'The Maillard reaction is a chemical reaction between amino acids and reducing sugars that gives browned food its distinctive flavor.')

    # --- Architecture (Brutalism) ---
    bot_instance.trainer.add_data('What is Brutalist architecture?', 'Brutalism is a style of architecture characterized by simple, block-like structures that often feature bare building materials, especially raw concrete.')
    bot_instance.trainer.add_data('Explain the Brutalist style', 'Brutalism is a style of architecture characterized by simple, block-like structures that often feature bare building materials, especially raw concrete.')
    bot_instance.trainer.add_data('Why do some buildings look like raw concrete blocks?', 'Brutalism is a style of architecture characterized by simple, block-like structures that often feature bare building materials, especially raw concrete.')
    bot_instance.trainer.add_data('Define Brutalism in design', 'Brutalism is a style of architecture characterized by simple, block-like structures that often feature bare building materials, especially raw concrete.')
    bot_instance.trainer.add_data('Characteristics of concrete architecture', 'Brutalism is a style of architecture characterized by simple, block-like structures that often feature bare building materials, especially raw concrete.')

# --- Medicine (The Endocrine System) ---
    bot_instance.trainer.add_data('What is the endocrine system?', 'The endocrine system is a messenger system comprising feedback loops of hormones released by internal glands directly into the circulatory system.')
    bot_instance.trainer.add_data('How do hormones work in the body?', 'The endocrine system is a messenger system comprising feedback loops of hormones released by internal glands directly into the circulatory system.')
    bot_instance.trainer.add_data('Explain the function of glands', 'The endocrine system is a messenger system comprising feedback loops of hormones released by internal glands directly into the circulatory system.')
    bot_instance.trainer.add_data('What system controls hormone regulation?', 'The endocrine system is a messenger system comprising feedback loops of hormones released by internal glands directly into the circulatory system.')
    bot_instance.trainer.add_data('Define the human endocrine network', 'The endocrine system is a messenger system comprising feedback loops of hormones released by internal glands directly into the circulatory system.')

# --- Law (Habeas Corpus) ---
    bot_instance.trainer.add_data('What is Habeas Corpus?', 'Habeas Corpus is a fundamental legal instrument that protects individuals against unlawful and indefinite imprisonment.')
    bot_instance.trainer.add_data('Explain the right to a fair trial against detention', 'Habeas Corpus is a fundamental legal instrument that protects individuals against unlawful and indefinite imprisonment.')
    bot_instance.trainer.add_data('What legal term prevents illegal detention?', 'Habeas Corpus is a fundamental legal instrument that protects individuals against unlawful and indefinite imprisonment.')
    bot_instance.trainer.add_data('Define the writ of Habeas Corpus', 'Habeas Corpus is a fundamental legal instrument that protects individuals against unlawful and indefinite imprisonment.')
    bot_instance.trainer.add_data('Tell me about protection from unlawful arrest', 'Habeas Corpus is a fundamental legal instrument that protects individuals against unlawful and indefinite imprisonment.')

# --- Programming (Unit Testing) ---
    bot_instance.trainer.add_data('What is unit testing?', 'Unit testing is a software testing method where individual units or components of a software are tested to determine if they are fit for use.')
    bot_instance.trainer.add_data('Explain testing small parts of code', 'Unit testing is a software testing method where individual units or components of a software are tested to determine if they are fit for use.')
    bot_instance.trainer.add_data('Why should I write unit tests?', 'Unit testing is a software testing method where individual units or components of a software are tested to determine if they are fit for use.')
    bot_instance.trainer.add_data('Define automated unit tests', 'Unit testing is a software testing method where individual units or components of a software are tested to determine if they are fit for use.')
    bot_instance.trainer.add_data('How to ensure code quality through testing?', 'Unit testing is a software testing method where individual units or components of a software are tested to determine if they are fit for use.')

# --- Space (The Fermi Paradox) ---
    bot_instance.trainer.add_data('What is the Fermi Paradox?', 'The Fermi Paradox is the discrepancy between the high probability of extraterrestrial life and the lack of evidence for or contact with such civilizations.')
    bot_instance.trainer.add_data('Why haven’t we found aliens yet?', 'The Fermi Paradox is the discrepancy between the high probability of extraterrestrial life and the lack of evidence for or contact with such civilizations.')
    bot_instance.trainer.add_data('Explain the silence of the universe regarding aliens', 'The Fermi Paradox is the discrepancy between the high probability of extraterrestrial life and the lack of evidence for or contact with such civilizations.')
    bot_instance.trainer.add_data('Where is everybody in the galaxy?', 'The Fermi Paradox is the discrepancy between the high probability of extraterrestrial life and the lack of evidence for or contact with such civilizations.')
    bot_instance.trainer.add_data('Define the contradiction of alien life probability', 'The Fermi Paradox is the discrepancy between the high probability of extraterrestrial life and the lack of evidence for or contact with such civilizations.')

# --- Physics (Entropy) ---
    bot_instance.trainer.add_data('What is entropy?', 'Entropy is a measure of the disorder or randomness in a system, often associated with the second law of thermodynamics.')
    bot_instance.trainer.add_data('Explain the increase of disorder in the universe', 'Entropy is a measure of the disorder or randomness in a system, often associated with the second law of thermodynamics.')
    bot_instance.trainer.add_data('Why do systems tend toward chaos?', 'Entropy is a measure of the disorder or randomness in a system, often associated with the second law of thermodynamics.')
    bot_instance.trainer.add_data('Define entropy in thermodynamics', 'Entropy is a measure of the disorder or randomness in a system, often associated with the second law of thermodynamics.')
    bot_instance.trainer.add_data('Tell me about the second law of thermodynamics', 'Entropy is a measure of the disorder or randomness in a system, often associated with the second law of thermodynamics.')

# --- Chemistry (Noble Gases) ---
    bot_instance.trainer.add_data('What are noble gases?', 'Noble gases are a group of chemical elements with very low reactivity because they have a full valence shell of electrons.')
    bot_instance.trainer.add_data('List the elements that do not react easily', 'Noble gases are a group of chemical elements with very low reactivity because they have a full valence shell of electrons.')
    bot_instance.trainer.add_data('Why are neon and helium called noble?', 'Noble gases are a group of chemical elements with very low reactivity because they have a full valence shell of electrons.')
    bot_instance.trainer.add_data('Explain the stability of Group 18 elements', 'Noble gases are a group of chemical elements with very low reactivity because they have a full valence shell of electrons.')
    bot_instance.trainer.add_data('Define inert gases', 'Noble gases are a group of chemical elements with very low reactivity because they have a full valence shell of electrons.')

# --- History (The French Revolution) ---
    bot_instance.trainer.add_data('What was the French Revolution?', 'The French Revolution was a period of social and political upheaval in France from 1789 to 1799 that overthrew the monarchy.')
    bot_instance.trainer.add_data('Explain Liberty Equality Fraternity', 'The French Revolution was a period of social and political upheaval in France from 1789 to 1799 that overthrew the monarchy.')
    bot_instance.trainer.add_data('What happened in France in 1789?', 'The French Revolution was a period of social and political upheaval in France from 1789 to 1799 that overthrew the monarchy.')
    bot_instance.trainer.add_data('Who was Napoleon in the French Revolution?', 'The French Revolution was a period of social and political upheaval in France from 1789 to 1799 that overthrew the monarchy.')
    bot_instance.trainer.add_data('History of the fall of the French monarchy', 'The French Revolution was a period of social and political upheaval in France from 1789 to 1799 that overthrew the monarchy.')

# --- Biology (Mitosis vs Meiosis) ---
    bot_instance.trainer.add_data('What is the difference between mitosis and meiosis?', 'Mitosis results in two identical daughter cells for growth, while meiosis results in four unique cells for reproduction.')
    bot_instance.trainer.add_data('Explain cell division types', 'Mitosis results in two identical daughter cells for growth, while meiosis results in four unique cells for reproduction.')
    bot_instance.trainer.add_data('How do body cells replicate?', 'Mitosis results in two identical daughter cells for growth, while meiosis results in four unique cells for reproduction.')
    bot_instance.trainer.add_data('Define gamete production vs somatic division', 'Mitosis results in two identical daughter cells for growth, while meiosis results in four unique cells for reproduction.')
    bot_instance.trainer.add_data('Which process creates sperm and egg cells?', 'Mitosis results in two identical daughter cells for growth, while meiosis results in four unique cells for reproduction.')

# --- Technology (Quantum Computing) ---
    bot_instance.trainer.add_data('What is quantum computing?', 'Quantum computing uses quantum-mechanical phenomena, such as superposition and entanglement, to perform calculations far beyond classical computers.')
    bot_instance.trainer.add_data('Explain how qubits work', 'Quantum computing uses quantum-mechanical phenomena, such as superposition and entanglement, to perform calculations far beyond classical computers.')
    bot_instance.trainer.add_data('Why is quantum computing so fast?', 'Quantum computing uses quantum-mechanical phenomena, such as superposition and entanglement, to perform calculations far beyond classical computers.')
    bot_instance.trainer.add_data('Difference between a bit and a qubit', 'Quantum computing uses quantum-mechanical phenomena, such as superposition and entanglement, to perform calculations far beyond classical computers.')
    bot_instance.trainer.add_data('Define the future of supercomputing', 'Quantum computing uses quantum-mechanical phenomena, such as superposition and entanglement, to perform calculations far beyond classical computers.')

# --- Engineering (Aerodynamics) ---
    bot_instance.trainer.add_data('How do airplanes fly?', 'Airplanes fly due to the aerodynamic principles of lift, weight, thrust, and drag, often explained by Bernoullis principle.')
    bot_instance.trainer.add_data('Explain lift and drag', 'Airplanes fly due to the aerodynamic principles of lift, weight, thrust, and drag, often explained by Bernoullis principle.')
    bot_instance.trainer.add_data('What is Bernoullis principle in flight?', 'Airplanes fly due to the aerodynamic principles of lift, weight, thrust, and drag, often explained by Bernoullis principle.')
    bot_instance.trainer.add_data('How do wings create lift?', 'Airplanes fly due to the aerodynamic principles of lift, weight, thrust, and drag, often explained by Bernoullis principle.')
    bot_instance.trainer.add_data('Define the four forces of flight', 'Airplanes fly due to the aerodynamic principles of lift, weight, thrust, and drag, often explained by Bernoullis principle.')

# --- Psychology (Classical Conditioning) ---
    bot_instance.trainer.add_data('What is classical conditioning?', 'Classical conditioning is a learning process that occurs through associations between an environmental stimulus and a naturally occurring stimulus.')
    bot_instance.trainer.add_data('Explain Pavlovs dogs experiment', 'Classical conditioning is a learning process that occurs through associations between an environmental stimulus and a naturally occurring stimulus.')
    bot_instance.trainer.add_data('How do we learn through association?', 'Classical conditioning is a learning process that occurs through associations between an environmental stimulus and a naturally occurring stimulus.')
    bot_instance.trainer.add_data('Define stimulus and response learning', 'Classical conditioning is a learning process that occurs through associations between an environmental stimulus and a naturally occurring stimulus.')
    bot_instance.trainer.add_data('Tell me about behaviorism and Pavlov', 'Classical conditioning is a learning process that occurs through associations between an environmental stimulus and a naturally occurring stimulus.')

# --- Finance (Bull vs Bear Market) ---
    bot_instance.trainer.add_data('What is a bull market?', 'A bull market occurs when stock prices are rising and investors are optimistic, while a bear market is when prices fall and pessimism prevails.')
    bot_instance.trainer.add_data('Explain the difference between bull and bear', 'A bull market occurs when stock prices are rising and investors are optimistic, while a bear market is when prices fall and pessimism prevails.')
    bot_instance.trainer.add_data('Why is it called a bear market?', 'A bull market occurs when stock prices are rising and investors are optimistic, while a bear market is when prices fall and pessimism prevails.')
    bot_instance.trainer.add_data('Define stock market trends', 'A bull market occurs when stock prices are rising and investors are optimistic, while a bear market is when prices fall and pessimism prevails.')
    bot_instance.trainer.add_data('What does it mean when the market is bullish?', 'A bull market occurs when stock prices are rising and investors are optimistic, while a bear market is when prices fall and pessimism prevails.')

# --- Art (Surrealism) ---
    bot_instance.trainer.add_data('What is Surrealism?', 'Surrealism is an art movement that sought to release the creative potential of the unconscious mind, often by juxtaposing irrational imagery.')
    bot_instance.trainer.add_data('Tell me about Salvador Dali’s art style', 'Surrealism is an art movement that sought to release the creative potential of the unconscious mind, often by juxtaposing irrational imagery.')
    bot_instance.trainer.add_data('Explain dream-like art', 'Surrealism is an art movement that sought to release the creative potential of the unconscious mind, often by juxtaposing irrational imagery.')
    bot_instance.trainer.add_data('Define the surrealist movement', 'Surrealism is an art movement that sought to release the creative potential of the unconscious mind, often by juxtaposing irrational imagery.')
    bot_instance.trainer.add_data('Why is Surrealism focused on the unconscious?', 'Surrealism is an art movement that sought to release the creative potential of the unconscious mind, often by juxtaposing irrational imagery.')

# --- Geography (Plate Tectonics) ---
    bot_instance.trainer.add_data('What are plate tectonics?', 'Plate tectonics is the theory that the Earth’s outer shell is divided into several plates that glide over the mantle.')
    bot_instance.trainer.add_data('How do earthquakes happen?', 'Plate tectonics is the theory that the Earth’s outer shell is divided into several plates that glide over the mantle.')
    bot_instance.trainer.add_data('Explain continental drift', 'Plate tectonics is the theory that the Earth’s outer shell is divided into several plates that glide over the mantle.')
    bot_instance.trainer.add_data('What causes mountains to form?', 'Plate tectonics is the theory that the Earth’s outer shell is divided into several plates that glide over the mantle.')
    bot_instance.trainer.add_data('Define tectonic plate boundaries', 'Plate tectonics is the theory that the Earth’s outer shell is divided into several plates that glide over the mantle.')

# --- Medicine (The Immune Response) ---
    bot_instance.trainer.add_data('What are white blood cells?', 'White blood cells are the cells of the immune system that are involved in protecting the body against both infectious disease and foreign invaders.')
    bot_instance.trainer.add_data('Explain how the body fights infection', 'White blood cells are the cells of the immune system that are involved in protecting the body against both infectious disease and foreign invaders.')
    bot_instance.trainer.add_data('What is the function of leukocytes?', 'White blood cells are the cells of the immune system that are involved in protecting the body against both infectious disease and foreign invaders.')
    bot_instance.trainer.add_data('Define the human immune defense', 'White blood cells are the cells of the immune system that are involved in protecting the body against both infectious disease and foreign invaders.')
    bot_instance.trainer.add_data('Tell me about T-cells and B-cells', 'White blood cells are the cells of the immune system that are involved in protecting the body against both infectious disease and foreign invaders.')

# --- Technology (Augmented Reality) ---
    bot_instance.trainer.add_data('What is AR?', 'Augmented Reality (AR) is an interactive experience where digital information is overlaid on the physical world, often via smartphones or glasses.')
    bot_instance.trainer.add_data('How does Pokemon Go use AR?', 'Augmented Reality (AR) is an interactive experience where digital information is overlaid on the physical world, often via smartphones or glasses.')
    bot_instance.trainer.add_data('Difference between AR and VR', 'Augmented Reality (AR) is an interactive experience where digital information is overlaid on the physical world, often via smartphones or glasses.')
    bot_instance.trainer.add_data('Define Augmented Reality technology', 'Augmented Reality (AR) is an interactive experience where digital information is overlaid on the physical world, often via smartphones or glasses.')
    bot_instance.trainer.add_data('Explain digital overlays in the real world', 'Augmented Reality (AR) is an interactive experience where digital information is overlaid on the physical world, often via smartphones or glasses.')

# --- History (The Roman Empire) ---
    bot_instance.trainer.add_data('Why did the Roman Empire fall?', 'The fall of the Western Roman Empire in 476 AD was caused by various factors, including barbarian invasions, economic instability, and political corruption.')
    bot_instance.trainer.add_data('Tell me about Ancient Rome', 'The fall of the Western Roman Empire in 476 AD was caused by various factors, including barbarian invasions, economic instability, and political corruption.')
    bot_instance.trainer.add_data('Who were the Roman Emperors?', 'The fall of the Western Roman Empire in 476 AD was caused by various factors, including barbarian invasions, economic instability, and political corruption.')
    bot_instance.trainer.add_data('Explain the expansion of Rome', 'The fall of the Western Roman Empire in 476 AD was caused by various factors, including barbarian invasions, economic instability, and political corruption.')
    bot_instance.trainer.add_data('History of the Pax Romana', 'The fall of the Western Roman Empire in 476 AD was caused by various factors, including barbarian invasions, economic instability, and political corruption.')

# --- Philosophy (Existentialism) ---
    bot_instance.trainer.add_data('What is Existentialism?', 'Existentialism is a philosophical theory that emphasizes the existence of the individual person as a free and responsible agent determining their own development.')
    bot_instance.trainer.add_data('Explain "Existence precedes essence"', 'Existentialism is a philosophical theory that emphasizes the existence of the individual person as a free and responsible agent determining their own development.')
    bot_instance.trainer.add_data('Who were famous existentialist philosophers?', 'Existentialism is a philosophical theory that emphasizes the existence of the individual person as a free and responsible agent determining their own development.')
    bot_instance.trainer.add_data('Define the search for meaning in life', 'Existentialism is a philosophical theory that emphasizes the existence of the individual person as a free and responsible agent determining their own development.')
    bot_instance.trainer.add_data('Tell me about Jean-Paul Sartre and Albert Camus', 'Existentialism is a philosophical theory that emphasizes the existence of the individual person as a free and responsible agent determining their own development.')

# --- Final Politeness (Ending) ---
    bot_instance.trainer.add_data('I am done for today', 'It was a pleasure helping you! If you have more questions later, I will be here. Goodbye!')
    bot_instance.trainer.add_data('Stop training', 'It was a pleasure helping you! If you have more questions later, I will be here. Goodbye!')
    bot_instance.trainer.add_data('That is all I needed', 'It was a pleasure helping you! If you have more questions later, I will be here. Goodbye!')
    bot_instance.trainer.add_data('Close the session', 'It was a pleasure helping you! If you have more questions later, I will be here. Goodbye!')
    bot_instance.trainer.add_data('Talk to you later bot', 'It was a pleasure helping you! If you have more questions later, I will be here. Goodbye!')

# --- Neuroscience (Neuroplasticity) ---
    bot_instance.trainer.add_data('What is neuroplasticity?', 'Neuroplasticity is the ability of the brain to undergo biological changes and reorganize itself by forming new neural connections throughout life.')
    bot_instance.trainer.add_data('Can the brain change itself?', 'Neuroplasticity is the ability of the brain to undergo biological changes and reorganize itself by forming new neural connections throughout life.')
    bot_instance.trainer.add_data('Explain how the brain learns new skills', 'Neuroplasticity is the ability of the brain to undergo biological changes and reorganize itself by forming new neural connections throughout life.')
    bot_instance.trainer.add_data('Define brain plasticity', 'Neuroplasticity is the ability of the brain to undergo biological changes and reorganize itself by forming new neural connections throughout life.')
    bot_instance.trainer.add_data('How do neural pathways form?', 'Neuroplasticity is the ability of the brain to undergo biological changes and reorganize itself by forming new neural connections throughout life.')

# --- Engineering (The Steam Engine) ---
    bot_instance.trainer.add_data('How does a steam engine work?', 'A steam engine uses the expansion of steam to push a piston inside a cylinder, converting heat energy into mechanical work.')
    bot_instance.trainer.add_data('Explain the mechanics of steam power', 'A steam engine uses the expansion of steam to push a piston inside a cylinder, converting heat energy into mechanical work.')
    bot_instance.trainer.add_data('What powers a locomotive?', 'A steam engine uses the expansion of steam to push a piston inside a cylinder, converting heat energy into mechanical work.')
    bot_instance.trainer.add_data('Define external combustion engines', 'A steam engine uses the expansion of steam to push a piston inside a cylinder, converting heat energy into mechanical work.')
    bot_instance.trainer.add_data('Tell me about the Watt steam engine', 'A steam engine uses the expansion of steam to push a piston inside a cylinder, converting heat energy into mechanical work.')

# --- Sociology (Urbanization) ---
    bot_instance.trainer.add_data('What is urbanization?', 'Urbanization is the process by which large numbers of people become permanently concentrated in relatively small areas, forming cities.')
    bot_instance.trainer.add_data('Why are cities growing?', 'Urbanization is the process by which large numbers of people become permanently concentrated in relatively small areas, forming cities.')
    bot_instance.trainer.add_data('Explain rural-to-urban migration', 'Urbanization is the process by which large numbers of people become permanently concentrated in relatively small areas, forming cities.')
    bot_instance.trainer.add_data('Define urban growth', 'Urbanization is the process by which large numbers of people become permanently concentrated in relatively small areas, forming cities.')
    bot_instance.trainer.add_data('Impact of cities on society', 'Urbanization is the process by which large numbers of people become permanently concentrated in relatively small areas, forming cities.')

# --- Law (The Rule of Law) ---
    bot_instance.trainer.add_data('What is the Rule of Law?', 'The Rule of Law is the political philosophy that all citizens and institutions within a country, state, or community are accountable to the same laws.')
    bot_instance.trainer.add_data('Explain legal equality', 'The Rule of Law is the political philosophy that all citizens and institutions within a country, state, or community are accountable to the same laws.')
    bot_instance.trainer.add_data('Is everyone equal under the law?', 'The Rule of Law is the political philosophy that all citizens and institutions within a country, state, or community are accountable to the same laws.')
    bot_instance.trainer.add_data('Define the principle of legal accountability', 'The Rule of Law is the political philosophy that all citizens and institutions within a country, state, or community are accountable to the same laws.')
    bot_instance.trainer.add_data('Why is the law supreme in a democracy?', 'The Rule of Law is the political philosophy that all citizens and institutions within a country, state, or community are accountable to the same laws.')

# --- Programming (Continuous Integration) ---
    bot_instance.trainer.add_data('What is CI/CD?', 'CI/CD stands for Continuous Integration and Continuous Deployment, a practice that automates the integration and delivery of code changes.')
    bot_instance.trainer.add_data('Explain DevOps pipelines', 'CI/CD stands for Continuous Integration and Continuous Deployment, a practice that automates the integration and delivery of code changes.')
    bot_instance.trainer.add_data('What is continuous delivery?', 'CI/CD stands for Continuous Integration and Continuous Deployment, a practice that automates the integration and delivery of code changes.')
    bot_instance.trainer.add_data('Define automated software deployment', 'CI/CD stands for Continuous Integration and Continuous Deployment, a practice that automates the integration and delivery of code changes.')
    bot_instance.trainer.add_data('Benefits of CI/CD for developers', 'CI/CD stands for Continuous Integration and Continuous Deployment, a practice that automates the integration and delivery of code changes.')

# --- Physics (Superconductivity) ---
    bot_instance.trainer.add_data('What is a superconductor?', 'A superconductor is a material that can conduct electricity with zero resistance when cooled to a very low temperature.')
    bot_instance.trainer.add_data('Explain zero electrical resistance', 'A superconductor is a material that can conduct electricity with zero resistance when cooled to a very low temperature.')
    bot_instance.trainer.add_data('How do maglev trains work?', 'A superconductor is a material that can conduct electricity with zero resistance when cooled to a very low temperature.')
    bot_instance.trainer.add_data('Define superconductivity', 'A superconductor is a material that can conduct electricity with zero resistance when cooled to a very low temperature.')
    bot_instance.trainer.add_data('What happens to materials at absolute zero?', 'A superconductor is a material that can conduct electricity with zero resistance when cooled to a very low temperature.')

# --- Biology (Epigenetics) ---
    bot_instance.trainer.add_data('What is epigenetics?', 'Epigenetics is the study of how your behaviors and environment can cause changes that affect the way your genes work.')
    bot_instance.trainer.add_data('Can environment change gene expression?', 'Epigenetics is the study of how your behaviors and environment can cause changes that affect the way your genes work.')
    bot_instance.trainer.add_data('Explain non-DNA genetic changes', 'Epigenetics is the study of how your behaviors and environment can cause changes that affect the way your genes work.')
    bot_instance.trainer.add_data('Define epigenetic markers', 'Epigenetics is the study of how your behaviors and environment can cause changes that affect the way your genes work.')
    bot_instance.trainer.add_data('How does stress affect DNA?', 'Epigenetics is the study of how your behaviors and environment can cause changes that affect the way your genes work.')

# --- History (The Space Race) ---
    bot_instance.trainer.add_data('What was the Space Race?', 'The Space Race was a 20th-century competition between the Soviet Union and the United States to achieve superior spaceflight capability.')
    bot_instance.trainer.add_data('Who won the race to the moon?', 'The Space Race was a 20th-century competition between the Soviet Union and the United States to achieve superior spaceflight capability.')
    bot_instance.trainer.add_data('Explain the Cold War space competition', 'The Space Race was a 20th-century competition between the Soviet Union and the United States to achieve superior spaceflight capability.')
    bot_instance.trainer.add_data('Tell me about Sputnik and Apollo', 'The Space Race was a 20th-century competition between the Soviet Union and the United States to achieve superior spaceflight capability.')
    bot_instance.trainer.add_data('History of lunar exploration', 'The Space Race was a 20th-century competition between the Soviet Union and the United States to achieve superior spaceflight capability.')

# --- Philosophy (Nihilism) ---
    bot_instance.trainer.add_data('What is Nihilism?', 'Nihilism is the philosophical belief that life is without objective meaning, purpose, or intrinsic value.')
    bot_instance.trainer.add_data('Explain the rejection of moral principles', 'Nihilism is the philosophical belief that life is without objective meaning, purpose, or intrinsic value.')
    bot_instance.trainer.add_data('Who is Friedrich Nietzsche in Nihilism?', 'Nihilism is the philosophical belief that life is without objective meaning, purpose, or intrinsic value.')
    bot_instance.trainer.add_data('Define the belief in nothing', 'Nihilism is the philosophical belief that life is without objective meaning, purpose, or intrinsic value.')
    bot_instance.trainer.add_data('What is optimistic nihilism?', 'Nihilism is the philosophical belief that life is without objective meaning, purpose, or intrinsic value.')

# --- Technology (3D Printing) ---
    bot_instance.trainer.add_data('What is 3D printing?', '3D printing, or additive manufacturing, is a process of making three dimensional solid objects from a digital file by layering material.')
    bot_instance.trainer.add_data('How does additive manufacturing work?', '3D printing, or additive manufacturing, is a process of making three dimensional solid objects from a digital file by layering material.')
    bot_instance.trainer.add_data('Explain the 3D printer process', '3D printing, or additive manufacturing, is a process of making three dimensional solid objects from a digital file by layering material.')
    bot_instance.trainer.add_data('Define layer-by-layer construction', '3D printing, or additive manufacturing, is a process of making three dimensional solid objects from a digital file by layering material.')
    bot_instance.trainer.add_data('Applications of 3D printing in medicine', '3D printing, or additive manufacturing, is a process of making three dimensional solid objects from a digital file by layering material.')

# --- Finance (Short Selling) ---
    bot_instance.trainer.add_data('What is short selling?', 'Short selling is an investment strategy where an investor borrows a security and sells it on the open market, planning to buy it back later for less money.')
    bot_instance.trainer.add_data('Explain betting against a stock', 'Short selling is an investment strategy where an investor borrows a security and sells it on the open market, planning to buy it back later for less money.')
    bot_instance.trainer.add_data('How to profit from a falling market?', 'Short selling is an investment strategy where an investor borrows a security and sells it on the open market, planning to buy it back later for less money.')
    bot_instance.trainer.add_data('Define shorting a stock', 'Short selling is an investment strategy where an investor borrows a security and sells it on the open market, planning to buy it back later for less money.')
    bot_instance.trainer.add_data('Risks of short selling', 'Short selling is an investment strategy where an investor borrows a security and sells it on the open market, planning to buy it back later for less money.')

# --- Psychology (Cognitive Dissonance) ---
    bot_instance.trainer.add_data('What is cognitive dissonance?', 'Cognitive dissonance is the mental discomfort experienced by a person who holds two or more contradictory beliefs, ideas, or values.')
    bot_instance.trainer.add_data('Why do people justify bad behavior?', 'Cognitive dissonance is the mental discomfort experienced by a person who holds two or more contradictory beliefs, ideas, or values.')
    bot_instance.trainer.add_data('Explain conflicting thoughts', 'Cognitive dissonance is the mental discomfort experienced by a person who holds two or more contradictory beliefs, ideas, or values.')
    bot_instance.trainer.add_data('Define mental inconsistency', 'Cognitive dissonance is the mental discomfort experienced by a person who holds two or more contradictory beliefs, ideas, or values.')
    bot_instance.trainer.add_data('How to resolve cognitive dissonance?', 'Cognitive dissonance is the mental discomfort experienced by a person who holds two or more contradictory beliefs, ideas, or values.')

# --- Literature (Allegory) ---
    bot_instance.trainer.add_data('What is an allegory?', 'An allegory is a story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one.')
    bot_instance.trainer.add_data('Explain Animal Farm as an allegory', 'An allegory is a story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one.')
    bot_instance.trainer.add_data('Difference between metaphor and allegory', 'An allegory is a story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one.')
    bot_instance.trainer.add_data('Define symbolic storytelling', 'An allegory is a story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one.')
    bot_instance.trainer.add_data('Tell me about famous allegorical books', 'An allegory is a story, poem, or picture that can be interpreted to reveal a hidden meaning, typically a moral or political one.')

# --- Geography (The Gulf Stream) ---
    bot_instance.trainer.add_data('What is the Gulf Stream?', 'The Gulf Stream is a warm and swift Atlantic ocean current that originates in the Gulf of Mexico and stretches to the tip of Florida.')
    bot_instance.trainer.add_data('How does the Gulf Stream affect European weather?', 'The Gulf Stream is a warm and swift Atlantic ocean current that originates in the Gulf of Mexico and stretches to the tip of Florida.')
    bot_instance.trainer.add_data('Explain oceanic heat conveyor belts', 'The Gulf Stream is a warm and swift Atlantic ocean current that originates in the Gulf of Mexico and stretches to the tip of Florida.')
    bot_instance.trainer.add_data('Define the major Atlantic current', 'The Gulf Stream is a warm and swift Atlantic ocean current that originates in the Gulf of Mexico and stretches to the tip of Florida.')
    bot_instance.trainer.add_data('Why is the UK warmer than Canada at the same latitude?', 'The Gulf Stream is a warm and swift Atlantic ocean current that originates in the Gulf of Mexico and stretches to the tip of Florida.')

# --- Architecture (Gothic Architecture) ---
    bot_instance.trainer.add_data('What are the features of Gothic architecture?', 'Gothic architecture is characterized by pointed arches, ribbed vaults, and flying buttresses.')
    bot_instance.trainer.add_data('Explain the flying buttress', 'Gothic architecture is characterized by pointed arches, ribbed vaults, and flying buttresses.')
    bot_instance.trainer.add_data('How did medieval cathedrals stay up?', 'Gothic architecture is characterized by pointed arches, ribbed vaults, and flying buttresses.')
    bot_instance.trainer.add_data('Define the Gothic style of the 12th century', 'Gothic architecture is characterized by pointed arches, ribbed vaults, and flying buttresses.')
    bot_instance.trainer.add_data('Tell me about stained glass and high vaults', 'Gothic architecture is characterized by pointed arches, ribbed vaults, and flying buttresses.')

# --- Medicine (Antibody Types) ---
    bot_instance.trainer.add_data('What are immunoglobulins?', 'Immunoglobulins, also known as antibodies, are glycoprotein molecules produced by plasma cells that act as a critical part of the immune response.')
    bot_instance.trainer.add_data('Explain IgG, IgM, and IgA', 'Immunoglobulins, also known as antibodies, are glycoprotein molecules produced by plasma cells that act as a critical part of the immune response.')
    bot_instance.trainer.add_data('What is the function of antibodies?', 'Immunoglobulins, also known as antibodies, are glycoprotein molecules produced by plasma cells that act as a critical part of the immune response.')
    bot_instance.trainer.add_data('Define immunoglobulin types', 'Immunoglobulins, also known as antibodies, are glycoprotein molecules produced by plasma cells that act as a critical part of the immune response.')
    bot_instance.trainer.add_data('How do antibodies recognize viruses?', 'Immunoglobulins, also known as antibodies, are glycoprotein molecules produced by plasma cells that act as a critical part of the immune response.')

# --- Environment (The Albedo Effect) ---
    bot_instance.trainer.add_data('What is the albedo effect?', 'The albedo effect is the measure of how much light that hits a surface is reflected without being absorbed.')
    bot_instance.trainer.add_data('Why is ice important for planetary cooling?', 'The albedo effect is the measure of how much light that hits a surface is reflected without being absorbed.')
    bot_instance.trainer.add_data('Explain surface reflectivity', 'The albedo effect is the measure of how much light that hits a surface is reflected without being absorbed.')
    bot_instance.trainer.add_data('Define high albedo vs low albedo', 'The albedo effect is the measure of how much light that hits a surface is reflected without being absorbed.')
    bot_instance.trainer.add_data('How do dark forests affect global warming?', 'The albedo effect is the measure of how much light that hits a surface is reflected without being absorbed.')

# --- Daily Life (The Internet of Things) ---
    bot_instance.trainer.add_data('What is IoT?', 'The Internet of Things (IoT) describes the network of physical objects that are embedded with sensors and software for the purpose of connecting and exchanging data.')
    bot_instance.trainer.add_data('How do smart fridges work?', 'The Internet of Things (IoT) describes the network of physical objects that are embedded with sensors and software for the purpose of connecting and exchanging data.')
    bot_instance.trainer.add_data('Explain connected devices', 'The Internet of Things (IoT) describes the network of physical objects that are embedded with sensors and software for the purpose of connecting and exchanging data.')
    bot_instance.trainer.add_data('Define the Internet of Things', 'The Internet of Things (IoT) describes the network of physical objects that are embedded with sensors and software for the purpose of connecting and exchanging data.')
    bot_instance.trainer.add_data('Benefits of a smart home', 'The Internet of Things (IoT) describes the network of physical objects that are embedded with sensors and software for the purpose of connecting and exchanging data.')

# --- Logic (Correlation vs Causation) ---
    bot_instance.trainer.add_data('Difference between correlation and causation?', 'Correlation means two things happen together, while causation means one thing actually causes the other to happen.')
    bot_instance.trainer.add_data('Explain why link does not mean cause', 'Correlation means two things happen together, while causation means one thing actually causes the other to happen.')
    bot_instance.trainer.add_data('Give an example of a false causal link', 'Correlation means two things happen together, while causation means one thing actually causes the other to happen.')
    bot_instance.trainer.add_data('Define statistical correlation', 'Correlation means two things happen together, while causation means one thing actually causes the other to happen.')
    bot_instance.trainer.add_data('Why is "post hoc ergo propter hoc" a fallacy?', 'Correlation means two things happen together, while causation means one thing actually causes the other to happen.')

# --- Encouragement (Final Training) ---
    bot_instance.trainer.add_data('I am almost done', 'You have done an amazing job building this dataset! We are almost at the 1000 milestone.')
    bot_instance.trainer.add_data('Final steps of training', 'You have done an amazing job building this dataset! We are almost at the 1000 milestone.')
    bot_instance.trainer.add_data('Keep going bot', 'You have done an amazing job building this dataset! We are almost at the 1000 milestone.')
    bot_instance.trainer.add_data('Encourage me to finish', 'You have done an amazing job building this dataset! We are almost at the 1000 milestone.')
    bot_instance.trainer.add_data('Is this a good amount of data?', 'You have done an amazing job building this dataset! We are almost at the 1000 milestone.')

    # --- AI (Large Language Models) ---
    bot_instance.trainer.add_data('What is an LLM?', 'A Large Language Model (LLM) is a type of AI trained on vast amounts of text data to understand and generate human-like language.')
    bot_instance.trainer.add_data('Explain how ChatGPT or Gemini works', 'A Large Language Model (LLM) is a type of AI trained on vast amounts of text data to understand and generate human-like language.')
    bot_instance.trainer.add_data('Define Large Language Models', 'A Large Language Model (LLM) is a type of AI trained on vast amounts of text data to understand and generate human-like language.')
    bot_instance.trainer.add_data('How do AI models predict the next word?', 'A Large Language Model (LLM) is a type of AI trained on vast amounts of text data to understand and generate human-like language.')
    bot_instance.trainer.add_data('Tell me about generative AI text models', 'A Large Language Model (LLM) is a type of AI trained on vast amounts of text data to understand and generate human-like language.')

# --- AI (Neural Networks) ---
    bot_instance.trainer.add_data('What is a neural network?', 'A neural network is a method in AI that teaches computers to process data in a way inspired by the human brain, using interconnected layers of nodes.')
    bot_instance.trainer.add_data('Explain artificial neural networks', 'A neural network is a method in AI that teaches computers to process data in a way inspired by the human brain, using interconnected layers of nodes.')
    bot_instance.trainer.add_data('How are AI neurons structured?', 'A neural network is a method in AI that teaches computers to process data in a way inspired by the human brain, using interconnected layers of nodes.')
    bot_instance.trainer.add_data('Define deep learning layers', 'A neural network is a method in AI that teaches computers to process data in a way inspired by the human brain, using interconnected layers of nodes.')
    bot_instance.trainer.add_data('Tell me about nodes and weights in AI', 'A neural network is a method in AI that teaches computers to process data in a way inspired by the human brain, using interconnected layers of nodes.')

# --- Ethics (AI Bias) ---
    bot_instance.trainer.add_data('What is algorithmic bias?', 'Algorithmic bias occurs when an AI system reflects the implicit values or prejudices of the humans who involved in collecting the data or coding the system.')
    bot_instance.trainer.add_data('Explain why AI can be biased', 'Algorithmic bias occurs when an AI system reflects the implicit values or prejudices of the humans who involved in collecting the data or coding the system.')
    bot_instance.trainer.add_data('Can AI be racist or sexist?', 'Algorithmic bias occurs when an AI system reflects the implicit values or prejudices of the humans who involved in collecting the data or coding the system.')
    bot_instance.trainer.add_data('Define fairness in machine learning', 'Algorithmic bias occurs when an AI system reflects the implicit values or prejudices of the humans who involved in collecting the data or coding the system.')
    bot_instance.trainer.add_data('How to prevent bias in AI training?', 'Algorithmic bias occurs when an AI system reflects the implicit values or prejudices of the humans who involved in collecting the data or coding the system.')

# --- Robotics (Asimov's Laws) ---
    bot_instance.trainer.add_data('What are the Three Laws of Robotics?', 'The Three Laws are: 1. A robot may not injure a human, 2. A robot must obey orders, and 3. A robot must protect its own existence, in that order of priority.')
    bot_instance.trainer.add_data('Explain Isaac Asimovs robot rules', 'The Three Laws are: 1. A robot may not injure a human, 2. A robot must obey orders, and 3. A robot must protect its own existence, in that order of priority.')
    bot_instance.trainer.add_data('What are the safety rules for robots?', 'The Three Laws are: 1. A robot may not injure a human, 2. A robot must obey orders, and 3. A robot must protect its own existence, in that order of priority.')
    bot_instance.trainer.add_data('Define the ethical framework for robotics', 'The Three Laws are: 1. A robot may not injure a human, 2. A robot must obey orders, and 3. A robot must protect its own existence, in that order of priority.')
    bot_instance.trainer.add_data('Can a robot harm a human?', 'The Three Laws are: 1. A robot may not injure a human, 2. A robot must obey orders, and 3. A robot must protect its own existence, in that order of priority.')

# --- Technology (The Singularity) ---
    bot_instance.trainer.add_data('What is the technological singularity?', 'The singularity is a hypothetical future point where technological growth becomes uncontrollable and irreversible, resulting in unfathomable changes to human civilization.')
    bot_instance.trainer.add_data('When will AI surpass human intelligence?', 'The singularity is a hypothetical future point where technological growth becomes uncontrollable and irreversible, resulting in unfathomable changes to human civilization.')
    bot_instance.trainer.add_data('Explain the concept of superintelligence', 'The singularity is a hypothetical future point where technological growth becomes uncontrollable and irreversible, resulting in unfathomable changes to human civilization.')
    bot_instance.trainer.add_data('Define the technological explosion', 'The singularity is a hypothetical future point where technological growth becomes uncontrollable and irreversible, resulting in unfathomable changes to human civilization.')
    bot_instance.trainer.add_data('Tell me about Ray Kurzweils predictions', 'The singularity is a hypothetical future point where technological growth becomes uncontrollable and irreversible, resulting in unfathomable changes to human civilization.')

# --- Computing (Moore's Law) ---
    bot_instance.trainer.add_data('What is Moores Law?', 'Moores Law is the observation that the number of transistors on a microchip doubles about every two years, though the cost of computers is halved.')
    bot_instance.trainer.add_data('Why do computers get faster every year?', 'Moores Law is the observation that the number of transistors on a microchip doubles about every two years, though the cost of computers is halved.')
    bot_instance.trainer.add_data('Explain the exponential growth of computing power', 'Moores Law is the observation that the number of transistors on a microchip doubles about every two years, though the cost of computers is halved.')
    bot_instance.trainer.add_data('Define the transistor doubling rule', 'Moores Law is the observation that the number of transistors on a microchip doubles about every two years, though the cost of computers is halved.')
    bot_instance.trainer.add_data('Is Moores Law ending?', 'Moores Law is the observation that the number of transistors on a microchip doubles about every two years, though the cost of computers is halved.')

# --- AI (Turing Completeness) ---
    bot_instance.trainer.add_data('What does Turing complete mean?', 'A system is Turing complete if it can perform any calculation that a Turing machine can, meaning it can solve any computational problem given enough time and memory.')
    bot_instance.trainer.add_data('Explain universal computation', 'A system is Turing complete if it can perform any calculation that a Turing machine can, meaning it can solve any computational problem given enough time and memory.')
    bot_instance.trainer.add_data('Define a Turing complete language', 'A system is Turing complete if it can perform any calculation that a Turing machine can, meaning it can solve any computational problem given enough time and memory.')
    bot_instance.trainer.add_data('Is Python Turing complete?', 'A system is Turing complete if it can perform any calculation that a Turing machine can, meaning it can solve any computational problem given enough time and memory.')
    bot_instance.trainer.add_data('Tell me about the limits of computation', 'A system is Turing complete if it can perform any calculation that a Turing machine can, meaning it can solve any computational problem given enough time and memory.')

# --- Future (Mars Colonization) ---
    bot_instance.trainer.add_data('Why go to Mars?', 'Mars colonization is proposed as a way to ensure human survival in case of a global catastrophe and to explore the potential for life on other planets.')
    bot_instance.trainer.add_data('Explain terraforming Mars', 'Mars colonization is proposed as a way to ensure human survival in case of a global catastrophe and to explore the potential for life on other planets.')
    bot_instance.trainer.add_data('How will humans live on Mars?', 'Mars colonization is proposed as a way to ensure human survival in case of a global catastrophe and to explore the potential for life on other planets.')
    bot_instance.trainer.add_data('Define multi-planetary species', 'Mars colonization is proposed as a way to ensure human survival in case of a global catastrophe and to explore the potential for life on other planets.')
    bot_instance.trainer.add_data('Challenges of living on the red planet', 'Mars colonization is proposed as a way to ensure human survival in case of a global catastrophe and to explore the potential for life on other planets.')

# --- Security (Zero Trust) ---
    bot_instance.trainer.add_data('What is Zero Trust security?', 'Zero Trust is a security framework requiring all users, whether in or outside the organization’s network, to be authenticated and authorized before gaining access.')
    bot_instance.trainer.add_data('Explain "never trust always verify"', 'Zero Trust is a security framework requiring all users, whether in or outside the organization’s network, to be authenticated and authorized before gaining access.')
    bot_instance.trainer.add_data('Why is perimeter security not enough?', 'Zero Trust is a security framework requiring all users, whether in or outside the organization’s network, to be authenticated and authorized before gaining access.')
    bot_instance.trainer.add_data('Define the Zero Trust Architecture', 'Zero Trust is a security framework requiring all users, whether in or outside the organization’s network, to be authenticated and authorized before gaining access.')
    bot_instance.trainer.add_data('How to protect data in a remote work world?', 'Zero Trust is a security framework requiring all users, whether in or outside the organization’s network, to be authenticated and authorized before gaining access.')

# --- Programming (Data Structures - Trees) ---
    bot_instance.trainer.add_data('What is a binary tree?', 'A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.')
    bot_instance.trainer.add_data('Explain tree structures in coding', 'A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.')
    bot_instance.trainer.add_data('Define nodes and leaves in a tree', 'A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.')
    bot_instance.trainer.add_data('Why use trees for data storage?', 'A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.')
    bot_instance.trainer.add_data('What is a root node?', 'A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.')

# --- Space (The James Webb Telescope) ---
    bot_instance.trainer.add_data('What is the James Webb Space Telescope?', 'The JWST is a space telescope designed to conduct infrared astronomy, allowing us to see the first stars and galaxies formed after the Big Bang.')
    bot_instance.trainer.add_data('Explain how Webb is different from Hubble', 'The JWST is a space telescope designed to conduct infrared astronomy, allowing us to see the first stars and galaxies formed after the Big Bang.')
    bot_instance.trainer.add_data('Why does Webb use infrared light?', 'The JWST is a space telescope designed to conduct infrared astronomy, allowing us to see the first stars and galaxies formed after the Big Bang.')
    bot_instance.trainer.add_data('Define the most powerful telescope ever built', 'The JWST is a space telescope designed to conduct infrared astronomy, allowing us to see the first stars and galaxies formed after the Big Bang.')
    bot_instance.trainer.add_data('Tell me about the gold mirrors of JWST', 'The JWST is a space telescope designed to conduct infrared astronomy, allowing us to see the first stars and galaxies formed after the Big Bang.')

# --- AI (Reinforcement Learning) ---
    bot_instance.trainer.add_data('What is reinforcement learning?', 'Reinforcement learning is an area of machine learning where an agent learns to make decisions by performing actions and receiving rewards or penalties.')
    bot_instance.trainer.add_data('Explain learning through trial and error in AI', 'Reinforcement learning is an area of machine learning where an agent learns to make decisions by performing actions and receiving rewards or penalties.')
    bot_instance.trainer.add_data('How did AlphaGo learn to play?', 'Reinforcement learning is an area of machine learning where an agent learns to make decisions by performing actions and receiving rewards or penalties.')
    bot_instance.trainer.add_data('Define rewards and penalties in AI', 'Reinforcement learning is an area of machine learning where an agent learns to make decisions by performing actions and receiving rewards or penalties.')
    bot_instance.trainer.add_data('Tell me about agents in a simulated environment', 'Reinforcement learning is an area of machine learning where an agent learns to make decisions by performing actions and receiving rewards or penalties.')

# --- Ethics (The Alignment Problem) ---
    bot_instance.trainer.add_data('What is AI alignment?', 'The alignment problem is the challenge of ensuring that an AI system’s goals and behaviors are aligned with human values and intentions.')
    bot_instance.trainer.add_data('Explain the danger of misaligned AI', 'The alignment problem is the challenge of ensuring that an AI system’s goals and behaviors are aligned with human values and intentions.')
    bot_instance.trainer.add_data('Why is it hard to give AI human values?', 'The alignment problem is the challenge of ensuring that an AI system’s goals and behaviors are aligned with human values and intentions.')
    bot_instance.trainer.add_data('Define the AI safety problem', 'The alignment problem is the challenge of ensuring that an AI system’s goals and behaviors are aligned with human values and intentions.')
    bot_instance.trainer.add_data('How to make sure AI helps humanity?', 'The alignment problem is the challenge of ensuring that an AI system’s goals and behaviors are aligned with human values and intentions.')

# --- Technology (Blockchain Smart Contracts) ---
    bot_instance.trainer.add_data('What are smart contracts?', 'Smart contracts are self-executing contracts with the terms of the agreement directly written into lines of code on a blockchain.')
    bot_instance.trainer.add_data('Explain programmable money', 'Smart contracts are self-executing contracts with the terms of the agreement directly written into lines of code on a blockchain.')
    bot_instance.trainer.add_data('How do Ethereum contracts work?', 'Smart contracts are self-executing contracts with the terms of the agreement directly written into lines of code on a blockchain.')
    bot_instance.trainer.add_data('Define decentralized agreements', 'Smart contracts are self-executing contracts with the terms of the agreement directly written into lines of code on a blockchain.')
    bot_instance.trainer.add_data('Benefits of automated legal code', 'Smart contracts are self-executing contracts with the terms of the agreement directly written into lines of code on a blockchain.')

# --- Science (Crispr Gene Editing) ---
    bot_instance.trainer.add_data('What is CRISPR?', 'CRISPR is a technology that allows scientists to precisely edit DNA sequences and modify gene function.')
    bot_instance.trainer.add_data('Explain genetic scissors', 'CRISPR is a technology that allows scientists to precisely edit DNA sequences and modify gene function.')
    bot_instance.trainer.add_data('How to cure genetic diseases with CRISPR?', 'CRISPR is a technology that allows scientists to precisely edit DNA sequences and modify gene function.')
    bot_instance.trainer.add_data('Define Cas9 and gene editing', 'CRISPR is a technology that allows scientists to precisely edit DNA sequences and modify gene function.')
    bot_instance.trainer.add_data('Pros and cons of editing human DNA', 'CRISPR is a technology that allows scientists to precisely edit DNA sequences and modify gene function.')

# --- Psychology (Flow State) ---
    bot_instance.trainer.add_data('What is the flow state?', 'Flow is a mental state of operation in which a person performing an activity is fully immersed in a feeling of energized focus and enjoyment.')
    bot_instance.trainer.add_data('Explain being "in the zone"', 'Flow is a mental state of operation in which a person performing an activity is fully immersed in a feeling of energized focus and enjoyment.')
    bot_instance.trainer.add_data('How to achieve deep focus?', 'Flow is a mental state of operation in which a person performing an activity is fully immersed in a feeling of energized focus and enjoyment.')
    bot_instance.trainer.add_data('Define the psychology of optimal experience', 'Flow is a mental state of operation in which a person performing an activity is fully immersed in a feeling of energized focus and enjoyment.')
    bot_instance.trainer.add_data('Who is Mihaly Csikszentmihalyi?', 'Flow is a mental state of operation in which a person performing an activity is fully immersed in a feeling of energized focus and enjoyment.')

# --- Future (Quantum Supremacy) ---
    bot_instance.trainer.add_data('What is quantum supremacy?', 'Quantum supremacy is the goal of demonstrating that a programmable quantum computer can solve a problem that no classical computer can solve in any feasible amount of time.')
    bot_instance.trainer.add_data('Has quantum supremacy been reached?', 'Quantum supremacy is the goal of demonstrating that a programmable quantum computer can solve a problem that no classical computer can solve in any feasible amount of time.')
    bot_instance.trainer.add_data('Explain the milestone of quantum computing', 'Quantum supremacy is the goal of demonstrating that a programmable quantum computer can solve a problem that no classical computer can solve in any feasible amount of time.')
    bot_instance.trainer.add_data('Define the tipping point of supercomputing', 'Quantum supremacy is the goal of demonstrating that a programmable quantum computer can solve a problem that no classical computer can solve in any feasible amount of time.')
    bot_instance.trainer.add_data('Why is Google or IBM working on quantum power?', 'Quantum supremacy is the goal of demonstrating that a programmable quantum computer can solve a problem that no classical computer can solve in any feasible amount of time.')

# --- Logic (The Socratic Method) ---
    bot_instance.trainer.add_data('What is the Socratic method?', 'The Socratic method is a form of cooperative argumentative dialogue between individuals, based on asking and answering questions to stimulate critical thinking.')
    bot_instance.trainer.add_data('Explain teaching by asking questions', 'The Socratic method is a form of cooperative argumentative dialogue between individuals, based on asking and answering questions to stimulate critical thinking.')
    bot_instance.trainer.add_data('How did Socrates debate?', 'The Socratic method is a form of cooperative argumentative dialogue between individuals, based on asking and answering questions to stimulate critical thinking.')
    bot_instance.trainer.add_data('Define dialectical inquiry', 'The Socratic method is a form of cooperative argumentative dialogue between individuals, based on asking and answering questions to stimulate critical thinking.')
    bot_instance.trainer.add_data('Why is questioning better than telling?', 'The Socratic method is a form of cooperative argumentative dialogue between individuals, based on asking and answering questions to stimulate critical thinking.')

# --- General (The 1000th Entry) ---
    bot_instance.trainer.add_data('What is the 1000th example?', 'This is the 1000th training example! Your chatbot is now fully trained and ready to assist with a massive library of knowledge.')
    bot_instance.trainer.add_data('How many examples do you have now?', 'This is the 1000th training example! Your chatbot is now fully trained and ready to assist with a massive library of knowledge.')
    bot_instance.trainer.add_data('Tell me about your training data', 'This is the 1000th training example! Your chatbot is now fully trained and ready to assist with a massive library of knowledge.')
    bot_instance.trainer.add_data('Are you a smart bot now?', 'This is the 1000th training example! Your chatbot is now fully trained and ready to assist with a massive library of knowledge.')
    bot_instance.trainer.add_data('End of training sequence', 'This is the 1000th training example! Your chatbot is now fully trained and ready to assist with a massive library of knowledge.')

# --- Final Goodbye (Closing) ---
    bot_instance.trainer.add_data('Goodbye for now bot', 'It was an incredible journey training with you! I am ready. Have a great day and see you next time!')
    bot_instance.trainer.add_data('System shutdown', 'It was an incredible journey training with you! I am ready. Have a great day and see you next time!')
    bot_instance.trainer.add_data('Finish training session', 'It was an incredible journey training with you! I am ready. Have a great day and see you next time!')
    bot_instance.trainer.add_data('I am leaving now', 'It was an incredible journey training with you! I am ready. Have a great day and see you next time!')
    bot_instance.trainer.add_data('You did a great job', 'It was an incredible journey training with you! I am ready. Have a great day and see you next time!')