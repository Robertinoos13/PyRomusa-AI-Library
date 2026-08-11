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