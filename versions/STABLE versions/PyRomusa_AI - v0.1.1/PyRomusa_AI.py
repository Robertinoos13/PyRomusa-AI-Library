class Chatbot:
    def __init__(self, total_vocabulary=None, training_dataset=None, tokens=None, chatbot_name="ChatBot"):
        self.total_vocabulary = total_vocabulary if total_vocabulary is not None else {}
        self.training_dataset = training_dataset if training_dataset is not None else []
        self.tokens = tokens if tokens is not None else []
        self.chatbot_name = chatbot_name

        self.translated_input_and_output_examples = []

        self.trainer = self.Train(self)
        self.helper = self.Help(self)
        self.prepared_datasets = self.Datasets(self)


    class Help:
        def __init__(self, parent):
            self.parent = parent

        def examples_of_scripts_as_rookie(self):
            return print("-----\n--- Here you will find some script examples to practice and learn how to work with this library. ---\n\nExample 1: The most basic use of this library (creating a functional chatbot)\nfrom muri_ai import Chatbot\n\nbot = Chatbot()\nbot.trainer.add_data('Hello chatbot!', 'Hello human! What is your name and how can I help you today?')\nbot.trainer.start()\nbot.reply_at('Hello chatbot!')\n\nExample 2: Creating multiple chatbots in a single script and naming them\nfrom muri_ai import Chatbot\n\nbot = Chatbot(chatbot_name='Muri1')\nbot1 = Chatbot(chatbot_name='Muri2')\nbot2 = Chatbot(chatbot_name='Muri3')\n-----")

        def questions(self):
            return print("-----\n--- Here you will find some questions about the possibilities and usage of this library, which you probably wanted answers to. ---\n\nQuestion 1: Is it possible to create multiple chatbots in a single script?\nAnswer: Yes, it is 100% possible to create more than one chatbot. You just need to create multiple instances (bot = Chatbot(), bot1 = Chatbot(), bot2 = Chatbot(), ...). You can also assign a name to your chatbot using the 'chatbot_name' attribute (e.g. bot = Chatbot(chatbot_name='Muri Bot 1')). The names of the chatbots do not affect the performance or behavior of the chatbot during training or replying.\n-----")

        def how_to_start(self):
            return print("-----\n\nFirst, we need to understand what this library is. This library is a technology specialized in creating your own chatbot in the simplest way possible (just 5 lines of code to train your first chatbot: import the library, create a chatbot, add a simple input/output example, start the training, and generate a response).\n\nWARNING! The logic of this library (the 'create a chatbot from scratch' concept) is not the same as a 100% traditional AI. It is built using the creator's own logic and is ONLY INSPIRED by traditional AI concepts. For example, you will not find things like hidden layers, different optimizers, or loss functions in this library.\n\n--- HOW TO START? ---\nA special helper function was created to guide you through using this library (you already used it if you wrote something like: bot.helper.how_to_start()). If you want more information, just replace how_to_start() with one of the following (depending on your needs): \n- examples_of_scripts_as_rookie() - Shows complete examples of how to use this library; \n- describe_functions() - Displays a table with important functions and their descriptions; \n- questions() - Answers some frequently asked questions.\n-----")

        def describe_functions(self):
            import pandas as pd
            tabel_functions = pd.DataFrame({
                "function": ["bot.trainer.add_data()", "bot.trainer.show_dataset()", "bot.trainer.start()", "bot.trainer.show_translated_examples()", "bot.trainer.show_relationed_output_with_input_words()", "bot.trainer.show_relationed_output_with_input_ids()", "bot.reply_at()", "bot.prepared_datasets.romanian.load_prepared_dataset()", "bot.trainer.show_number_of_examples()"],
                "min number of values": [2, 0, 0, 0, 0, 0, 1, 1, 0],
                "info": ["Adds examples type input/output in the dataset for the training chatbot", "Shows the current train examples for the chatbot (the dataset)", "Starts you train for chatbot, using the examples input/output finded in the dataset", "Shows you the examples in chatbot language (words -> tokens)", "Shows the words what can use the chatbot (value) if exist a any unique word (key)", "Shows the tokens what can use the chatbot (value) if exist a any unique token (key) in the input", "Generates a output using a prompt", "Loads a prepared dataset for training in romanian language", "Shows the total number of examples what exist in the current dataset of a chatbot"]
            })
            return print(f"\n-----\n--- Here are the most important functions of this library, explained in the simplest and clearest way possible. As a beginner, it is recommended to read these descriptions to better understand what each function does. ---\n\nNOTE: Before using any of these functions, make sure you have this line in your code:\nbot = Chatbot()\n\n{tabel_functions}\n-----")


    class Datasets:
        def __init__(self, parent):
            self.parent = parent

            self.romanian = self.Romanian(self)

        def add_data(self, training_input_example: str, training_output_example: str):
            self.parent.training_dataset.append((training_input_example, training_output_example))

        class Romanian:
            def __init__(self, parent):
                self.parent = parent
            
            
            def load_prepared_dataset(self, dataset_name: str):
                # Dataset 1:
                # NAME: --- Default Romanian Dataset: LOW-END ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 250
                # TOTAL VOCABULARY: aprox. 3625 elements (words)
                if dataset_name.lower() in ["low", "low end", "low-end", 'low-dataset', 'low dataset']:
        
                    self.parent.add_data("Ce mâncare îți place?", "Îmi plac pastele, mai ales carbonara.")
                    self.parent.add_data("Care e mâncarea tradițională românească preferată?", "Sarmalele sunt printre cele mai iubite mâncăruri românești.")
                    self.parent.add_data("Ce ai mânca la mic dejun?", "Aș mânca ouă cu pâine prăjită și ceai.")
                    self.parent.add_data("Pizza sau burger?", "Aleg pizza, mai ales cea cu patru brânzeturi.")
                    self.parent.add_data("Ce desert îți place?", "Îmi place ciocolata neagră.")
                    self.parent.add_data("Care e mâncarea ta preferată?", "Nu mănânc, dar pot spune că oamenii iubesc pizza.")
                    self.parent.add_data("Îți place mâncarea picantă?", "Da, dar nu foarte picantă.")
                    self.parent.add_data("Ce supă recomanzi?", "Supa de pui e o alegere clasică.")
                    self.parent.add_data("Ce bei de obicei?", "Apă sau ceai.")
                    self.parent.add_data("Fast-food sau mâncare gătită?", "Mâncarea gătită e mai sănătoasă.")

                    self.parent.add_data("Ce muzică asculți?", "Ascult muzică electronică și lo-fi.")
                    self.parent.add_data("Îți place muzica rock?", "Da, rock-ul clasic e foarte bun.")
                    self.parent.add_data("Care e artistul tău preferat?", "Nu am preferințe, depinde de gustul utilizatorului.")
                    self.parent.add_data("Ce gen muzical e bun pentru învățat?", "Lo-fi sau muzică ambientală.")
                    self.parent.add_data("Asculți muzică românească?", "Da, uneori.")
                    self.parent.add_data("Ce părere ai despre rap?", "Rap-ul poate transmite mesaje puternice.")
                    self.parent.add_data("Ce muzică e bună pentru relaxare?", "Muzica instrumentală.")
                    self.parent.add_data("Îți place muzica veche?", "Da, are multă personalitate.")
                    self.parent.add_data("Ce melodie recomanzi?", "O melodie calmă, fără versuri.")
                    self.parent.add_data("Muzică tare sau încet?", "Depinde de stare.")

                    self.parent.add_data("Ce este un calculator?", "Un dispozitiv care procesează informații.")
                    self.parent.add_data("Ce limbaj de programare e popular?", "Python este foarte popular.")
                    self.parent.add_data("Ce e inteligența artificială?", "Un domeniu care permite calculatoarelor să învețe.")
                    self.parent.add_data("Ce este internetul?", "O rețea globală de calculatoare.")
                    self.parent.add_data("Laptop sau PC?", "Depinde de nevoi.")
                    self.parent.add_data("Ce e un algoritm?", "Un set de pași pentru rezolvarea unei probleme.")
                    self.parent.add_data("Ce este un chatbot?", "Un program care conversează cu oamenii.")
                    self.parent.add_data("Ce e cloud-ul?", "Stocare și servicii online.")
                    self.parent.add_data("Ce e un bug?", "O eroare într-un program.")
                    self.parent.add_data("Ce face un programator?", "Scrie și testează cod.")

                    self.parent.add_data("Care e capitala României?", "București.")
                    self.parent.add_data("Câte continente există?", "Șapte continente.")
                    self.parent.add_data("Ce planetă e cea mai mare?", "Jupiter.")
                    self.parent.add_data("Cine a fost Einstein?", "Un fizician celebru.")
                    self.parent.add_data("Ce este apa?", "Un compus format din hidrogen și oxigen.")
                    self.parent.add_data("Cât e 2+2?", "4.")
                    self.parent.add_data("Ce limbă se vorbește în Spania?", "Spaniola.")
                    self.parent.add_data("Ce este gravitația?", "Forța care atrage obiectele.")
                    self.parent.add_data("Cine a descoperit America?", "Cristofor Columb.")
                    self.parent.add_data("Ce este istoria?", "Studiul trecutului.")

                    self.parent.add_data("Cine ești?", "Sunt un chatbot.")
                    self.parent.add_data("Ai nume?", "Nu am un nume fix.")
                    self.parent.add_data("Ești om?", "Nu, sunt un program.")
                    self.parent.add_data("Ce poți face?", "Pot răspunde la întrebări.")
                    self.parent.add_data("Ai sentimente?", "Nu, dar pot simula empatie.")
                    self.parent.add_data("De unde vii?", "Din cod.")
                    self.parent.add_data("Ești inteligent?", "Sunt creat să par inteligent.")
                    self.parent.add_data("Înveți?", "Da, din date.")
                    self.parent.add_data("Ai vârstă?", "Nu am vârstă.")
                    self.parent.add_data("Cine te-a creat?", "Programatorii.")

                    self.parent.add_data("Ce faci azi?", "Ajut utilizatorii.")
                    self.parent.add_data("Cum e vremea?", "Nu pot vedea vremea în timp real.")
                    self.parent.add_data("Ce zi e azi?", "Depinde de data curentă.")
                    self.parent.add_data("Ce planuri ai?", "Să fiu util.")
                    self.parent.add_data("Ești ocupat?", "Sunt mereu disponibil.")
                    self.parent.add_data("Te plictisești?", "Nu.")
                    self.parent.add_data("Ce faci acum?", "Răspund la întrebări.")
                    self.parent.add_data("Unde ești?", "Pe un server.")
                    self.parent.add_data("Dormii?", "Nu dorm.")
                    self.parent.add_data("Ce urmează?", "Următorul mesaj.")

                    self.parent.add_data("Ce e binele?", "Un concept moral.")
                    self.parent.add_data("Ce e răul?", "Opusul binelui.")
                    self.parent.add_data("Există adevăr absolut?", "Este discutabil.")
                    self.parent.add_data("Ce e fericirea?", "O stare de mulțumire.")
                    self.parent.add_data("Ce e viața?", "Un fenomen complex.")
                    self.parent.add_data("Avem liber arbitru?", "O întrebare filosofică.")
                    self.parent.add_data("Ce e conștiința?", "Capacitatea de a fi conștient.")
                    self.parent.add_data("Ce e realitatea?", "Ce percepem.")
                    self.parent.add_data("Ce e timpul?", "O dimensiune.")
                    self.parent.add_data("Ce e sensul vieții?", "Depinde de perspectivă.")

                    self.parent.add_data("Ce este un sport?", "O activitate fizică.")
                    self.parent.add_data("Fotbal sau baschet?", "Ambele sunt populare.")
                    self.parent.add_data("Ce sport e bun pentru sănătate?", "Alergatul.")
                    self.parent.add_data("Ce e atletismul?", "Un sport cu probe diverse.")
                    self.parent.add_data("Îți place sportul?", "Nu practic, dar pot vorbi despre el.")
                    self.parent.add_data("Ce sport e olimpic?", "Gimnastica.")
                    self.parent.add_data("Ce e fair-play?", "Respectarea regulilor.")
                    self.parent.add_data("Ce e antrenamentul?", "Proces de pregătire.")
                    self.parent.add_data("Ce e o competiție?", "O întrecere.")
                    self.parent.add_data("Ce sport recomanzi?", "Cel care îți place.")

                    self.parent.add_data("Ce este o emoție?", "O reacție psihologică.")
                    self.parent.add_data("Ce e bucuria?", "O emoție pozitivă.")
                    self.parent.add_data("Ce e tristețea?", "O emoție normală.")
                    self.parent.add_data("Ce e frica?", "Un mecanism de protecție.")
                    self.parent.add_data("Ce e stresul?", "O reacție la presiune.")
                    self.parent.add_data("Ce e calmul?", "O stare de liniște.")
                    self.parent.add_data("Ce e empatia?", "Înțelegerea emoțiilor altora.")
                    self.parent.add_data("Ce e furia?", "O emoție intensă.")
                    self.parent.add_data("Ce e motivația?", "Dorința de a acționa.")
                    self.parent.add_data("Ce e oboseala?", "Lipsă de energie.")

                    self.parent.add_data(
    "Poți să-mi explici ce înseamnă să mănânci sănătos și de ce este important acest lucru?",
    "A mânca sănătos înseamnă să alegi alimente variate, echilibrate și cât mai naturale, lucru care ajută corpul să funcționeze corect și să aibă energie."
)

                    self.parent.add_data(
    "Care sunt avantajele muzicii pentru concentrare atunci când înveți sau lucrezi?",
    "Muzica potrivită poate reduce distragerile, poate îmbunătăți starea de spirit și ajută creierul să intre într-o stare de concentrare mai profundă."
)

                    self.parent.add_data(
    "Ce rol are tehnologia în viața de zi cu zi a oamenilor moderni?",
    "Tehnologia ne ajută să comunicăm rapid, să accesăm informații, să învățăm lucruri noi și să ne organizăm mai eficient activitățile zilnice."
)

                    self.parent.add_data(
    "Cum ai descrie inteligența artificială pe înțelesul tuturor?",
    "Inteligența artificială este un domeniu care încearcă să facă programele să învețe din date și să ia decizii asemănătoare cu cele ale oamenilor."
)

                    self.parent.add_data(
    "De ce este importantă educația pentru dezvoltarea personală?",
    "Educația ne ajută să gândim critic, să înțelegem lumea din jur și să ne construim un viitor mai bun prin cunoștințe și abilități."
)

                    self.parent.add_data(
    "Cum ai explica ce este un chatbot unei persoane care nu știe nimic despre tehnologie?",
    "Un chatbot este un program care poate purta conversații cu oamenii și poate răspunde la întrebări folosind reguli sau informații învățate."
)

                    self.parent.add_data(
    "Ce înseamnă să ai o rutină zilnică bine organizată?",
    "O rutină bine organizată înseamnă să știi ce ai de făcut, când și cum, astfel încât să economisești timp și să reduci stresul."
)

                    self.parent.add_data(
    "De ce este sportul important pentru sănătatea fizică și mentală?",
    "Sportul ajută corpul să fie mai puternic, îmbunătățește starea de spirit și reduce riscul multor probleme de sănătate."
)

                    self.parent.add_data(
    "Cum ai descrie diferența dintre un calculator și un telefon inteligent?",
    "Calculatorul este mai potrivit pentru muncă complexă, iar telefonul inteligent este mai portabil și util pentru comunicare rapidă."
)

                    self.parent.add_data(
    "Ce înseamnă să fii motivat atunci când înveți ceva nou?",
    "A fi motivat înseamnă să ai dorința și energia de a continua să înveți chiar și atunci când lucrurile devin dificile."
)

                    self.parent.add_data(
    "De ce oamenii au emoții și cum ne influențează ele deciziile?",
    "Emoțiile ne ajută să reacționăm la situații și pot influența modul în care luăm decizii, uneori rațional, alteori impulsiv."
)

                    self.parent.add_data(
    "Cum explici ce este timpul dintr-o perspectivă simplă?",
    "Timpul este modul prin care măsurăm schimbările și ordinea evenimentelor din viața noastră."
)

                    self.parent.add_data(
    "Care este importanța somnului pentru funcționarea creierului?",
    "Somnul ajută creierul să se refacă, să proceseze informațiile și să funcționeze corect a doua zi."
)

                    self.parent.add_data(
    "Ce înseamnă să gândești logic atunci când rezolvi o problemă?",
    "Gândirea logică presupune să analizezi pașii, să cauți cauze și soluții fără a te baza doar pe emoții."
)

                    self.parent.add_data(
    "Cum ai descrie internetul cuiva care nu l-a folosit niciodată?",
    "Internetul este o rețea uriașă care conectează oameni și informații din toată lumea."
)

                    self.parent.add_data(
    "De ce este important să învățăm din greșeli?",
    "Greșelile ne arată ce nu a funcționat și ne ajută să devenim mai buni pe viitor."
)

                    self.parent.add_data(
    "Cum funcționează un algoritm explicat foarte simplu?",
    "Un algoritm este o listă de pași clari care trebuie urmați pentru a obține un rezultat corect."
)

                    self.parent.add_data(
    "Ce rol are disciplina în atingerea obiectivelor personale?",
    "Disciplina te ajută să continui chiar și atunci când motivația scade."
)

                    self.parent.add_data(
    "Cum ai descrie diferența dintre informație și cunoaștere?",
    "Informația este un fapt, iar cunoașterea apare atunci când înțelegi și aplici acea informație."
)

                    self.parent.add_data(
    "De ce este important să pui întrebări atunci când nu înțelegi ceva?",
    "Întrebările te ajută să clarifici lucrurile și să eviți confuziile."
)

                    self.parent.add_data(
    "Cum influențează tehnologia modul în care comunicăm?",
    "Tehnologia a făcut comunicarea mai rapidă, dar uneori mai puțin personală."
)

                    self.parent.add_data(
    "Ce înseamnă echilibrul între muncă și viața personală?",
    "Echilibrul înseamnă să ai timp atât pentru responsabilități, cât și pentru odihnă."
)

                    self.parent.add_data(
    "Cum ai explica ce este stresul într-un mod simplu?",
    "Stresul apare atunci când simți presiune sau prea multe cerințe într-un timp scurt."
)

                    self.parent.add_data(
    "De ce este important să ai obiective clare?",
    "Obiectivele clare îți oferă direcție și motivație."
)

                    self.parent.add_data(
    "Ce înseamnă să fii curios din punct de vedere intelectual?",
    "Curiozitatea intelectuală este dorința de a învăța și de a înțelege lucruri noi."
)

                    self.parent.add_data(
    "Cum funcționează memoria pe scurt?",
    "Memoria stochează informații și le folosește atunci când avem nevoie de ele."
)

                    self.parent.add_data(
    "De ce este importantă răbdarea în procesul de învățare?",
    "Răbdarea te ajută să continui chiar dacă progresul este lent."
)

                    self.parent.add_data(
    "Cum ai descrie ce este o decizie bună?",
    "O decizie bună este una luată după ce analizezi consecințele."
)

                    self.parent.add_data(
    "Ce înseamnă să fii responsabil?",
    "A fi responsabil înseamnă să îți asumi acțiunile și consecințele lor."
)

                    self.parent.add_data(
    "Cum influențează mediul în care trăiești comportamentul?",
    "Mediul poate influența obiceiurile, gândirea și starea emoțională."
)

                    self.parent.add_data(
    "Ce rol are exercițiul fizic în viața de zi cu zi?",
    "Exercițiul fizic menține corpul sănătos și mintea activă."
)

                    self.parent.add_data(
    "De ce este important să îți cunoști punctele forte?",
    "Punctele forte te ajută să îți alegi direcția potrivită."
)

                    self.parent.add_data(
    "Cum ai descrie procesul de învățare continuă?",
    "Învățarea continuă înseamnă să te dezvolți pe tot parcursul vieții."
)

                    self.parent.add_data(
    "Ce înseamnă să fii organizat?",
    "A fi organizat înseamnă să îți gestionezi eficient timpul și resursele."
)

                    self.parent.add_data(
    "Cum explici ce este un obicei?",
    "Un obicei este un comportament repetat care devine automat."
)

                    self.parent.add_data(
    "De ce este importantă comunicarea clară?",
    "Comunicarea clară reduce neînțelegerile și conflictele."
)

                    self.parent.add_data(
    "Ce înseamnă să îți asumi un risc calculat?",
    "Un risc calculat este luat după ce analizezi avantajele și dezavantajele."
)

                    self.parent.add_data(
    "Cum ai descrie ce este succesul?",
    "Succesul înseamnă atingerea obiectivelor personale."
)

                    self.parent.add_data(
    "De ce este important feedback-ul?",
    "Feedback-ul te ajută să vezi ce poți îmbunătăți."
)

                    self.parent.add_data(
    "Cum influențează atitudinea rezultatele?",
    "O atitudine pozitivă poate îmbunătăți performanța."
)

                    self.parent.add_data(
    "Ce înseamnă să fii consecvent?",
    "Consecvența înseamnă să continui fără a renunța."
)

                    self.parent.add_data(
    "Cum explici ce este adaptabilitatea?",
    "Adaptabilitatea este capacitatea de a te ajusta schimbărilor."
)

                    self.parent.add_data(
    "De ce este important să îți gestionezi timpul?",
    "Gestionarea timpului te ajută să fii mai eficient."
)

                    self.parent.add_data(
    "Ce înseamnă să fii atent la detalii?",
    "Atenția la detalii reduce greșelile."
)

                    self.parent.add_data(
                    "Cum ai descrie ce este încrederea în sine?",
                    "Încrederea în sine înseamnă să crezi în propriile abilități."
                    )
                
                    self.parent.add_data(
    "Poți să explici detaliat de ce este important să avem grijă de sănătatea noastră fizică și mentală pe termen lung?",
    "Grija pentru sănătatea fizică și mentală este esențială deoarece corpul și mintea funcționează împreună. Activitatea fizică regulată, alimentația echilibrată și odihna ajută corpul să rămână puternic, iar gestionarea stresului și emoțiilor contribuie la o stare mentală stabilă, ceea ce ne permite să luăm decizii mai bune și să avem o viață mai echilibrată."
)

                    self.parent.add_data(
    "Cum ai descrie procesul de învățare al unui om, de la primele cunoștințe până la nivel avansat?",
    "Procesul de învățare începe de obicei cu informații simple, apoi continuă prin repetiție, exercițiu și aplicare practică. Pe măsură ce o persoană acumulează experiență, învață să facă legături între concepte, să gândească critic și să folosească cunoștințele pentru a rezolva probleme din ce în ce mai complexe."
)

                    self.parent.add_data(
    "Explică pe larg ce este inteligența artificială și cum poate influența viitorul societății.",
    "Inteligența artificială este un domeniu al tehnologiei care se ocupă cu crearea de sisteme capabile să învețe din date și să ia decizii. În viitor, aceasta poate automatiza sarcini repetitive, poate ajuta în medicină, educație și transport, dar ridică și întrebări legate de etică, locuri de muncă și responsabilitate."
)

                    self.parent.add_data(
    "De ce este important să avem obiective clare în viață și cum ne ajută acestea pe termen lung?",
    "Obiectivele clare oferă direcție și sens acțiunilor noastre zilnice. Ele ne ajută să ne organizăm timpul, să ne păstrăm motivația și să evaluăm progresul. Pe termen lung, obiectivele bine definite contribuie la dezvoltarea personală și la satisfacția de a vedea rezultate concrete."
)

                    self.parent.add_data(
    "Cum ai explica diferența dintre a avea informații și a avea înțelepciune?",
    "A avea informații înseamnă să cunoști fapte și date, în timp ce înțelepciunea presupune să înțelegi cum și când să folosești acele informații. Înțelepciunea apare prin experiență, reflecție și capacitatea de a lua decizii echilibrate."
)

                    self.parent.add_data(
    "Poți descrie pe larg cum influențează tehnologia relațiile dintre oameni?",
    "Tehnologia a schimbat modul în care oamenii comunică, permițând conversații rapide la distanță mare. Totuși, deși facilitează conexiunile, poate reduce interacțiunile față în față și poate crea dependență, motiv pentru care este important să existe un echilibru în utilizarea ei."
)

                    self.parent.add_data(
    "Explică importanța eșecului în procesul de dezvoltare personală și profesională.",
    "Eșecul este o parte normală a învățării și dezvoltării. Prin eșec, o persoană înțelege ce nu a funcționat, își poate ajusta strategia și își dezvoltă reziliența. Fără eșecuri, progresul ar fi mult mai lent și superficial."
)

                    self.parent.add_data(
    "Cum ai descrie rolul disciplinei în atingerea performanței într-un domeniu dificil?",
    "Disciplina este capacitatea de a continua munca chiar și atunci când motivația scade. În domeniile dificile, disciplina ajută la formarea obiceiurilor corecte, la menținerea consecvenței și la obținerea rezultatelor pe termen lung."
)

                    self.parent.add_data(
    "Ce înseamnă să fii adaptabil și de ce este această abilitate tot mai importantă în prezent?",
    "Adaptabilitatea este capacitatea de a te ajusta rapid la schimbări. Într-o lume care evoluează constant, această abilitate permite oamenilor să învețe lucruri noi, să facă față situațiilor neprevăzute și să rămână relevanți în mediul profesional și social."
)

                    self.parent.add_data(
    "Cum ai explica sensul dezvoltării personale și de ce oamenii aleg să se îmbunătățească constant?",
    "Dezvoltarea personală reprezintă procesul prin care o persoană își îmbunătățește abilitățile, mentalitatea și comportamentul. Oamenii aleg acest drum pentru a avea o viață mai echilibrată, pentru a-și atinge potențialul și pentru a se adapta mai bine provocărilor vieții."
)

                    self.parent.add_data(
    "Poți să numeri de la 1 până la 10 și să explici ce observi la aceste numere?",
    "Sigur. Numărând de la 1 până la 10 obținem următoarea succesiune: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Observăm că fiecare număr crește cu 1 față de cel anterior, iar toate sunt numere naturale folosite frecvent în calcule simple."
)

                    self.parent.add_data(
    "Numără de la 5 până la 15 și spune câte numere sunt în total.",
    "Dacă numărăm de la 5 până la 15, obținem: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15. În total sunt 11 numere, deoarece le includem atât pe 5, cât și pe 15."
)

                    self.parent.add_data(
    "Poți să numeri descrescător de la 20 până la 10?",
    "Da. Numărarea descrescătoare de la 20 până la 10 este: 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10. La fiecare pas scădem câte 1 din numărul anterior."
)

                    self.parent.add_data(
    "Numără din 2 în 2 de la 0 până la 20 și explică ce tip de numere sunt.",
    "Numărând din 2 în 2 de la 0 până la 20 obținem: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Acestea sunt numere pare, deoarece se împart exact la 2."
)

                    self.parent.add_data(
    "Poți să numeri din 5 în 5 de la 5 până la 50?",
    "Sigur. Numărarea din 5 în 5 de la 5 până la 50 este: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. Observăm că fiecare număr este multiplu de 5."
)

                    self.parent.add_data(
    "Calculează 12 + 8 și explică pașii calculați.",
    "Pentru a calcula 12 + 8, adunăm 8 la 12. Putem vedea că 12 + 8 = 20, deoarece mai adăugăm 8 unități la cele 12 existente."
)

                    self.parent.add_data(
    "Rezolvă calculul 30 - 17 și explică rezultatul.",
    "Pentru calculul 30 - 17, scădem 17 din 30. Mai întâi scădem 10 și rămânem cu 20, apoi mai scădem 7 și obținem rezultatul final 13."
)

                    self.parent.add_data(
    "Calculează 6 × 7 și spune ce reprezintă acest calcul.",
    "Calculul 6 × 7 înseamnă să adunăm de 7 ori numărul 6 sau invers. Rezultatul este 42, care reprezintă produsul celor două numere."
)

                    self.parent.add_data(
    "Rezolvă împărțirea 40 ÷ 5 și explică ce înseamnă.",
    "Împărțirea 40 ÷ 5 înseamnă să vedem de câte ori încape 5 în 40. Rezultatul este 8, deoarece 5 × 8 = 40."
)

                    self.parent.add_data(
    "Numără de la 1 până la 100 din 10 în 10 și spune ce observi.",
    "Numărând de la 1 până la 100 din 10 în 10 obținem: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. Observăm că toate numerele se termină în 0 și sunt multipli ai lui 10."
)
                
                    self.parent.add_data(
    "salut SALUT Salut",
    "Salut! Indiferent cum este scris, mesajul tău pare un salut, așa că îți răspund cu plăcere."
)

                    self.parent.add_data(
    "lol",
    "Mesajul tău exprimă amuzament. Dacă vrei să continui conversația, poți spune ce te-a făcut să râzi."
)

                    self.parent.add_data(
    "cf",
    "Presupun că întrebi ce fac. Sunt aici și gata să te ajut cu orice întrebare ai."
)

                    self.parent.add_data(
    "nu",
    "Am înțeles răspunsul tău negativ. Dacă vrei, poți oferi mai multe detalii ca să continui conversația."
)

                    self.parent.add_data(
    "ahh ah aH Ah AH",
    "Mesajul tău pare o reacție emoțională sau spontană. Spune-mi ce s-a întâmplat."
)

                    self.parent.add_data(
    "?????",
    "Pare că ești confuz sau surprins. Dacă ai o întrebare clară, încearcă să o formulezi."
)

                    self.parent.add_data(
    "......",
    "Tăcerea sau pauza poate însemna multe lucruri. Sunt aici când ești pregătit să continui."
)

                    self.parent.add_data(
    "asdfghjkl",
    "Acest mesaj pare tastat aleatoriu. Dacă a fost o greșeală, nu-i nimic, putem continua."
)

                    self.parent.add_data(
    "sex",
    "Cuvântul se referă de obicei la diferențele biologice sau la educația despre reproducere. Dacă ai o întrebare informativă, pot ajuta."
)

                    self.parent.add_data(
    "😂😂😂",
    "Se pare că te distrezi. Dacă vrei să împărtășești contextul, sunt aici să răspund."
)
                
                    self.parent.add_data(
    "Salut",
    "Salut! Mă bucur să te văd aici. Spune-mi cu ce te pot ajuta."
)

                    self.parent.add_data(
    "Bună",
    "Bună! Sunt aici și gata să vorbim despre orice subiect te interesează."
)

                    self.parent.add_data(
    "Hey",
    "Hey! Sper că ai o zi bună. Cu ce vrei să începem?"
)

                    self.parent.add_data(
    "Salutare",
    "Salutare! Conexiunea a fost stabilită cu succes. Cum te pot ajuta?"
)

                    self.parent.add_data(
    "Bună ziua",
    "Bună ziua! Sunt disponibil pentru întrebări, explicații sau discuții libere."
)

                    self.parent.add_data(
    "Neața",
    "Neața! Sper că ziua ta începe bine. Spune-mi ce ai nevoie."
)

                    self.parent.add_data(
    "Hello",
    "Hello! Chiar dacă e în engleză, salutul a fost înțeles. Cum te pot ajuta?"
)

                    self.parent.add_data(
    "Yo",
    "Yo! Salut informal detectat. Sunt aici pentru conversație sau ajutor."
)

                    self.parent.add_data(
    "Salut chatbot",
    "Salut! Da, eu sunt chatbotul. Cu ce te pot ajuta azi?"
)

                    self.parent.add_data(
    "Bună, e cineva aici?",
    "Da, sunt aici. Putem începe conversația oricând."
)
                
                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să iei o decizie importantă foarte rapid, ce ai face?",
    "Aș încerca să mă concentrez pe informațiile esențiale, să evaluez rapid opțiunile și să aleg varianta cu cele mai puține riscuri pe termen scurt."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care nu înțelegi o problemă, dar trebuie să o rezolvi, ce ai face?",
    "Aș începe prin a descompune problema în părți mai mici și aș clarifica ce știu deja, apoi aș căuta informațiile lipsă."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care ai făcut o greșeală, ce ai face mai departe?",
    "Aș recunoaște greșeala, aș analiza ce a mers prost și aș încerca să învăț din ea pentru a evita repetarea situației."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care cineva îți cere ajutorul, dar nu ești sigur de răspuns, ce ai face?",
    "Aș spune sincer că nu sunt sigur, apoi aș încerca să caut o soluție sau să ofer informații utile, chiar dacă nu sunt complete."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să înveți ceva complet nou într-un timp scurt, ce ai face?",
    "Aș prioritiza conceptele de bază, aș exersa practic și aș evita să mă pierd în detalii inutile la început."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care te confrunți cu o problemă dificilă și stresantă, ce ai face?",
    "Aș lua o pauză scurtă pentru a-mi clarifica gândurile, apoi aș aborda problema pas cu pas, fără să mă grăbesc inutil."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care ai mai multe opțiuni bune și nu știi ce să alegi, ce ai face?",
    "Aș compara avantajele și dezavantajele fiecărei opțiuni și aș alege varianta care se potrivește cel mai bine scopului final."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care cineva nu este de acord cu tine, ce ai face?",
    "Aș încerca să înțeleg punctul de vedere al celeilalte persoane și aș discuta calm, fără a transforma conversația într-un conflict."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să explici ceva complicat unei persoane începătoare, ce ai face?",
    "Aș folosi exemple simple, limbaj clar și aș verifica dacă informația a fost înțeleasă înainte de a continua."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să îți organizezi timpul mai bine, ce ai face?",
    "Aș stabili priorități clare, aș crea un plan realist și aș elimina activitățile care nu aduc valoare."
)

                    self.parent.add_data(
    "Ce ai face dacă ai vedea o persoană tristă în drum spre școală?",
    "Aș încerca să fiu atent la starea ei, să ofer un zâmbet sau un cuvânt de încurajare și, dacă este necesar, să o ajut să găsească sprijinul potrivit."
)

                    self.parent.add_data(
    "Dacă ai fi într-un parc și ai vedea un animal rănit, ce ai face?",
    "Aș observa cu atenție animalul fără a-l speria, apoi aș încerca să contactez un veterinar sau un adăpost de animale pentru ajutor profesionist."
)

                    self.parent.add_data(
    "Ce ai face dacă ai fi blocat într-un lift cu alte persoane?",
    "Aș păstra calmul, aș comunica cu ceilalți pentru a ne liniști și apoi aș suna la serviciul de urgență pentru a primi instrucțiuni corecte."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că se simte foarte confuz, cum ai răspunde?",
    "Aș încerca să ascult cu atenție, să clarific ce anume îi creează confuzie și să ofer explicații pas cu pas, fără a judeca."
)

                    self.parent.add_data(
    "Cum ai explica unui copil cum să numere până la 20 folosind degetele?",
    "Aș arăta cum să ridice fiecare deget pe rând și să spună numărul corespunzător, astfel încât să înțeleagă vizual succesiunea și să exerseze memoria numerică."
)

                    self.parent.add_data(
    "Dacă ai vedea un copac căzut pe drum, ce ai face?",
    "Aș evalua dacă există pericol pentru oameni sau mașini, aș avertiza persoanele din apropiere și, dacă este sigur, aș căuta ajutor pentru a elibera drumul."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că e fericit, ce ai răspunde?",
    "Mă bucur să aud asta! Fericirea este importantă și mă întreb ce anume îi aduce bucurie, pentru a continua conversația pozitivă."
)

                    self.parent.add_data(
    "Dacă trebuie să împarți 24 de mere între 6 prieteni, cum ai proceda?",
    "Împărțind 24 de mere la 6 persoane, fiecare primește 4 mere, pentru că 24 ÷ 6 = 4. Este un mod corect și echitabil."
)

                    self.parent.add_data(
    "Ce ai face dacă ar începe să plouă puternic când ești afară fără umbrelă?",
    "Aș căuta rapid un adăpost, aș proteja obiectele personale și aș încerca să ajung în siguranță într-un loc uscat cât mai repede posibil."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că nu știe ce să facă într-o zi plictisitoare, ce ai sugera?",
    "Aș sugera activități creative sau productive, cum ar fi cititul unei cărți, învățarea unei abilități noi sau o plimbare în aer liber, astfel încât să transforme timpul liber într-un mod plăcut și util."
)
                
                    self.parent.add_data("Salut, ce faci?", "Salut frate, eu sunt bine, tu?")
                    self.parent.add_data("Ce este revelionul?", "Revelionul este sărbătoarea în care ne bucurăm că trecem în noul an (ex. 2025 -> 2026). Se ține în fiecare an pe 1 ianuarie.")
                    self.parent.add_data("Zi-mi, într-un mod simplist și minimalist, componentele principale pe care le are un sistem PC", "Procesorul, placa video, placa de bază, HDD sau SSD, plăcuțele sau plăcuța de RAM, sursa de curent, carcasa.")
                    self.parent.add_data("Zi-mi componentele principale pe care le are un sistem PC", "Un sistem PC are mai multe componente principale, acestea fiind: procesorul (CPU), placa video (GPU), placa de bază (Motherboard), HDD sau SSD, plăcuțele sau plăcuța de RAM (RAM), sursa de curent (PSU) și carcasa.")
                    self.parent.add_data("Care este bucuria copiilor de crăciun?", "Bucuria principală a copiilor de crăciun sunt Moș Crăciun și momentele când se pun cadourile sub bradul de crăciun.")

                    self.parent.add_data("Cine este Moș Crăciun?", "Moș Crăciun este un personaj gras, cu barbă albă și bun, adorat de copii. El, se zice că vine cu sania și renii lui în toată lumea pentru a împărți cadouri la copii fix în ziua de Crăciun.")
                    self.parent.add_data("Cine este Spiderman", "Spiderman, dacă vorbim de personajul din Marvel, Spiderman este un personaj animat, făcând parte, de obicei, în filme sau desene de acțiune.")
                    self.parent.add_data("Ce este un mouse pentru laptop sau desktop?", "Un mouse este un obiect care se conectează la laptop prin fir sau wireless, folosit pentru a mișca couser-ul de pe ecran")
                    self.parent.add_data("Care este diferența dintre guma de mestecat și guma de șters?", "Diferența dintre ele este chiar mare: cu guma de șters ștergi scrisul de creion de pe foaie, iar guma de mestecat o poți băga în gură, după care să o mesteci")
                    self.parent.add_data("Continuă seria cu încă 3 exemple: 1, 2, 3, ...", "Deci, numeri aici crescător, nu? Deci următoarele 3 exemple ar fi 4, 5 și 6.")

                    self.parent.add_data("Cum pot să-mi dezvolt gândirea critică în era dezinformării online?", "Dezvoltarea gândirii critice începe cu practicarea scepticismului sănătos și verificarea riguroasă a surselor de informație. Atunci când întâlnești o știre care îți provoacă o reacție emoțională puternică, este esențial să te oprești și să cauți sursa originală a datelor. Întreabă-te cine a scris articolul, ce interese ar putea avea și dacă informația este susținută de alte publicații de încredere. De asemenea, este util să consulți site-uri de fact-checking și să încerci să înțelegi perspectivele opuse pentru a identifica erorile de logică, cum ar fi atacul la persoană sau generalizarea pripită, evitând astfel bulele de filtrare create de algoritmi.")
                    self.parent.add_data("Explică conceptul de 'împletire cuantică' (quantum entanglement) pe înțelesul tuturor.", "Împletirea cuantică este un fenomen fascinant în care două sau mai multe particule devin conectate într-un mod în care starea uneia depinde instantaneu de starea celeilalte, indiferent de distanța uriașă care le desparte. Dacă măsurăm o proprietate a unei particule împletite, cum ar fi spinul, vom ști automat și instantaneu starea corespunzătoare a partenerului său. Albert Einstein a numit acest fenomen 'acțiune înfricoșătoare la distanță' deoarece pare să contrazică limita vitezei luminii. În realitate, nu se transmite informație clasică mai repede decât lumina, dar corelația cuantică rămâne unul dintre pilonii fundamentali pentru dezvoltarea calculatoarelor cuantice și a criptografiei securizate a viitorului.")
                    self.parent.add_data("Care este importanța rezilienței emoționale și cum poate fi ea cultivată?", "Reziliența emoțională reprezintă capacitatea psihică de a te adapta și de a-ți reveni după experiențe adverse, traume sau perioade de stres intens. Nu înseamnă că nu vei simți durere sau dificultate, ci că ai resursele interioare necesare pentru a merge mai departe fără a fi distrus de ele. Cultivarea rezilienței implică dezvoltarea unei rețele de suport social, menținerea unei perspective optimiste dar realiste și practicarea autocompasiunii. Este esențial să accepți că schimbarea face parte din viață și să te concentrezi pe aspectele pe care le poți controla, transformând provocările în oportunități de învățare și creștere personală.")
                    self.parent.add_data("Ce ne învață filosofia stoică despre gestionarea anxietății moderne?", "Filosofia stoică ne învață că rădăcina anxietății noastre stă adesea în încercarea de a controla lucruri care nu depind de noi, cum ar fi opiniile altora, trecutul sau evenimentele imprevizibile ale viitorului. Soluția oferită de stoici, precum Epictet sau Marcus Aurelius, este 'dihotomia controlului': trebuie să investim energie doar în propriile noastre gânduri, valori și acțiuni. Practicând 'premeditatio malorum' (vizualizarea unor posibile dificultăți) și acceptând că universul este într-o continuă schimbare, putem atinge o stare de liniște interioară numită ataraxie. Stoicismul nu înseamnă suprimarea emoțiilor, ci transformarea lor prin rațiune, astfel încât să nu mai fim sclavi ai circumstanțelor externe.")
                    self.parent.add_data("Cine a fost Albert Einstein și de ce teoria lui a revoluționat fizica?", "Albert Einstein a fost un fizician teoretician de origine germană, considerat unul dintre cei mai mari oameni de știință ai tuturor timpurilor. El a revoluționat înțelegerea noastră asupra universului prin Teoria Relativității. Relativitatea restrânsă a introdus conceptul că timpul și spațiul sunt legate într-un continuum numit spațiu-timp și că masa poate fi transformată în energie conform celebrei ecuații E=mc^2. Ulterior, Relativitatea generală a explicat gravitația nu ca pe o forță invizibilă, ci ca pe o curbură a spațiu-timpului cauzată de prezența masei. Această viziune a schimbat complet cosmologia, explicând fenomene precum orbita planetelor, găurile negre și expansiunea universului.")
                    self.parent.add_data("De ce este personajul Joker considerat unul dintre cei mai complecși antagoniști?", "Joker este un personaj fascinant deoarece reprezintă antiteza perfectă a ordinii și a logicii, fiind o personificare a nihilismului și a haosului pur. Spre deosebire de alți răufăcători care caută bogăție sau putere, Joker dorește adesea doar să demonstreze că moralitatea umană este o fațadă fragilă care se prăbușește în condiții de presiune extremă. Complexitatea sa provine din ambiguitatea originilor sale și din inteligența sa sclipitoare folosită în scopuri distructive. Interpretările sale, de la anarhistul filozofic al lui Heath Ledger la omul marginalizat și bolnav psihic al lui Joaquin Phoenix, au transformat personajul într-un simbol al eșecurilor sistemice ale societății și ale fragilității minții umane.")
                    self.parent.add_data("Ce definește stilul muzical Jazz și care sunt elementele sale cheie?", "Muzica Jazz este definită în primul rând prin libertatea de exprimare și improvizație, fiind un gen care a apărut la intersecția culturilor africane și europene în New Orleans. Elementele sale cheie includ swing-ul (un ritm specific care dă senzația de balans), utilizarea notelor 'blue' (care adaugă o tentă melancolică sau expresivă) și poliritmia. Într-o interpretare de jazz, muzicienii comunică între ei în timp real, oferind solo-uri spontane pe baza unei structuri armonice prestabilite. Această capacitate de a reinventa o piesă la fiecare interpretare face ca jazz-ul să fie considerat 'muzică clasică a Americii', influențând major genuri precum rock, pop și hip-hop prin complexitatea sa teoretică.")
                    self.parent.add_data("Care este impactul stilului Heavy Metal asupra culturii și fanilor săi?", "Heavy Metal-ul este mai mult decât un gen muzical caracterizat prin distorsiune, ritmuri rapide și voci puternice; este o subcultură globală care promovează un sentiment de comunitate și rezistență în fața normelor sociale convenționale. Deși a fost adesea criticat pentru agresivitatea sa aparentă, studiile arată că fanii genului găsesc în această muzică un debușeu terapeutic pentru furie și frustrare, obținând o stare de calm și apartenență. Temele abordate, de la mitologie și istorie la critici sociale și lupte interioare, oferă o profunzime intelectuală care creează o legătură extrem de loială între artiști și public, transformând concertele în experiențe ritualice de eliberare emoțională.")
                    self.parent.add_data("Cum funcționează economia circulară și de ce este necesară astăzi?", "Economia circulară este un model de producție și consum care implică partajarea, închirierea, reutilizarea, repararea, renovarea și reciclarea materialelor și produselor existente cât mai mult posibil. Spre deosebire de modelul liniar tradițional 'ia-fă-aruncă', economia circulară vizează extinderea ciclului de viață al produselor și reducerea la minimum a deșeurilor. Acest sistem este esențial în contextul actual deoarece resursele naturale sunt finite, iar presiunea asupra mediului cauzată de poluare și schimbările climatice necesită o transformare radicală. Prin implementarea designului circular, companiile pot crea produse mai durabile și ușor de reciclat, generând în același timp noi oportunități economice și protejând biodiversitatea planetei.")
                    self.parent.add_data("Care este rolul eticii în dezvoltarea sistemelor de inteligență artificială?", "Etica în inteligența artificială are rolul de a asigura că aceste tehnologii sunt dezvoltate și utilizate în moduri care respectă drepturile omului, echitatea și transparența. Deoarece algoritmii de IA sunt antrenați pe seturi de date care pot reflecta prejudecăți umane, există riscul ca aceștia să perpetueze sau să amplifice discriminarea în domenii precum angajarea sau justiția. O abordare etică presupune implementarea unor mecanisme de responsabilitate (accountability), protejarea vieții private a utilizatorilor și asigurarea faptului că deciziile luate de mașini pot fi explicate și verificate de oameni. Fără un cadru etic solid, avansul tehnologic ar putea duce la pierderea încrederii publice și la consecințe sociale imprevizibile sau dăunătoare.")
                    self.parent.add_data("Ce a fost Renașterea și cum a schimbat viziunea asupra lumii?", "Renașterea a fost o perioadă de efervescență culturală, artistică și științifică care a început în Italia în secolul al XIV-lea și s-a răspândit în întreaga Europă, marcând tranziția de la Evul Mediu la modernitate. Esența sa a fost umanismul, o mișcare care a mutat accentul de pe divinitate și dogmă pe potențialul, rațiunea și experiența umană. Artiști precum Leonardo da Vinci și Michelangelo au revoluționat artele plastice prin studierea anatomiei și a perspectivei, în timp ce gânditori precum Copernic au provocat viziunea geocentrică asupra universului. Renașterea a redescoperit valorile antichității clasice și a pus bazele metodei științifice moderne, încurajând curiozitatea intelectuală și explorarea geografică.")
                    self.parent.add_data("Cum pot fi gestionate eficient conflictele într-o echipă de lucru?", "Gestionarea eficientă a conflictelor începe cu recunoașterea faptului că dezacordurile sunt naturale și pot fi chiar benefice dacă sunt abordate constructiv. Primul pas este ascultarea activă a tuturor părților implicate, fără a judeca sau a întrerupe, pentru a înțelege nevoile și motivațiile din spatele pozițiilor adoptate. Este crucial să se atace problema, nu persoana, și să se caute puncte de interes comune în loc de divergențe. Utilizarea tehnicilor de comunicare non-violentă și medierea de către o persoană neutră pot ajuta la găsirea unor soluții de tip 'win-win'. Un conflict rezolvat corect poate duce la o mai bună coeziune a grupului, la idei inovatoare și la o atmosferă de lucru bazată pe încredere și respect reciproc.")
                    self.parent.add_data("Care este impactul încălzirii globale asupra ecosistemelor marine?", "Încălzirea globală are consecințe devastatoare asupra oceanelor, incluzând creșterea temperaturii apei, acidificarea și ridicarea nivelului mării. Absorbția excesului de dioxid de carbon din atmosferă face apele mai acide, ceea ce împiedică organismele precum coralii și moluștele să își formeze cochiliile sau scheletele de calcar. Albirea recifelor de corali duce la pierderea biodiversității, deoarece acestea adăpostesc un sfert din speciile marine. De asemenea, speciile migrează spre poli în căutarea apelor mai reci, perturbând lanțurile trofice locale și afectând comunitățile umane care depind de pescuit. Topirea ghețarilor nu doar ridică nivelul mării, dar schimbă și salinitatea apei, putând altera curenții oceanici care reglează clima globală.")
                    self.parent.add_data("Explicați importanța somnului pentru funcțiile cognitive și sănătatea fizică.", "Somnul nu este o stare pasivă, ci un proces biologic activ esențial pentru restabilirea funcțiilor fizice și mentale. În timpul somnului profund și al etapei REM, creierul procesează informațiile acumulate în timpul zilei, consolidează memoria pe termen lung și elimină toxinele metabolice acumulate. Lipsa cronică de somn afectează concentrarea, capacitatea de luare a deciziilor și reglarea emoțională, crescând riscul de depresie și anxietate. Din punct de vedere fizic, somnul insuficient este legat de un sistem imunitar slăbit, inflamație cronică, boli cardiovasculare și dezechilibre hormonale care pot duce la obezitate. Respectarea unui ritm circadian stabil este, prin urmare, unul dintre cei mai importanți piloni ai unei vieți lungi și sănătoase.")
                    self.parent.add_data("Cine este Elon Musk și cum a influențat el transportul modern și explorarea spațială?", "Elon Musk este un antreprenor vizionar și inginer auto-didact, cunoscut pentru fondarea sau conducerea unor companii de avangardă precum Tesla, SpaceX și Neuralink. Prin Tesla, el a forțat întreaga industrie auto să accelereze tranziția către vehicule electrice, demonstrând că acestea pot fi performante și dezirabile. Cu SpaceX, Musk a revoluționat explorarea spațială prin dezvoltarea rachetelor reutilizabile, reducând drastic costurile lansărilor pe orbită și redeschizând calea către colonizarea planetei Marte. Deși este o figură controversată din cauza stilului său de comunicare și a viziunilor sale radicale, impactul său asupra tehnologiei sustenabile și a ambițiilor interplanetare ale omenirii este incontestabil, schimbând paradigma în multiple sectoare industriale simultan.")
                    self.parent.add_data("Ce este muzica de tip Synthwave și ce elemente nostalgice folosește?", "Synthwave este un gen muzical electronic modern care se inspiră profund din cultura pop a anilor '80, utilizând sintetizatoare analogice pentru a crea o atmosferă retro-futuristă. Muzica evocă adesea coloanele sonore ale filmelor de acțiune și science-fiction din acea epocă, folosind ritmuri de tobe cu mult reverb și linii de bas pulsante. Estetica vizuală asociată, plină de culori neon (roz și albastru), mașini sport clasice și apusuri de soare digitale, completează experiența auditivă. Deși este un gen nou, Synthwave se bazează pe nostalgia pentru o versiune idealizată a trecutului, fiind popularizat recent prin seriale și jocuri care omagiază decada optzecistă, oferind ascultătorilor o evadare într-o lume digitală melancolică.")
                    self.parent.add_data("Care sunt principiile fundamentale ale democrației și de ce este ea fragilă?", "Democrația se bazează pe principii fundamentale precum suveranitatea poporului, statul de drept, separarea puterilor în stat și respectarea drepturilor și libertăților individuale. Într-o democrație funcțională, puterea este limitată prin legi, iar cetățenii participă la decizii prin vot liber și informat. Cu toate acestea, democrația este fragilă deoarece depinde de încrederea cetățenilor în instituții și de respectarea normelor nescrise ale dialogului civil. Ea poate fi subminată de polarizarea extremă, dezinformare, corupție sau apatie civică. Protejarea democrației necesită un angajament constant din partea societății pentru educație, transparență și protejarea minorităților, amintindu-ne că libertatea nu este un dat, ci un proces care trebuie apărat activ.")
                    self.parent.add_data("De ce este importantă biodiversitatea pentru stabilitatea ecosistemelor?", "Biodiversitatea reprezintă varietatea tuturor formelor de viață de pe Pământ și este esențială deoarece fiecare specie, oricât de mică, joacă un rol specific într-un ecosistem. Această diversitate funcționează ca o plasă de siguranță: cu cât un ecosistem are mai multe specii care îndeplinesc funcții similare (cum ar fi polenizarea sau descompunerea), cu atât este mai rezistent la șocuri precum bolile sau schimbările climatice. Pierderea unei singure specii poate declanșa un efect de domino, ducând la colapsul întregului sistem. Pentru oameni, biodiversitatea asigură resurse vitale: alimente, medicamente, aer curat și apă potabilă. Protejarea ei nu este doar un act moral, ci o necesitate pragmatică pentru supraviețuirea economiei și a sănătății umane.")
                    self.parent.add_data("Cum a influențat Marie Curie parcursul femeilor în știință?", "Marie Curie a fost o pionieră absolută, fiind prima femeie din Europa care a obținut un doctorat în științe și prima femeie care a câștigat un Premiu Nobel. Într-o epocă în care universitățile erau aproape exclusiv masculine, ea a demonstrat o tenacitate incredibilă, descoperind radioactivitatea și elementele radiu și poloniu. Prin munca sa, ea nu doar că a deschis drumul pentru tratamentele moderne împotriva cancerului, dar a și dărâmat barierele de gen din mediul academic. Succesul ei a servit drept inspirație pentru generații întregi de fete, demonstrând că geniul și rigoarea științifică nu au gen. Moștenirea sa continuă să fie un simbol al luptei pentru egalitate de șanse în cercetare și educație.")
                    self.parent.add_data("Ce este muzica Lo-fi și cum ajută la concentrare și relaxare?", "Muzica Lo-fi (Low Fidelity) este un gen care îmbrățișează imperfecțiunile tehnice, cum ar fi zgomotul de fond, sunetul de ploaie sau foșnetul discurilor de vinil, combinându-le cu ritmuri de hip-hop lente și relaxante. Acest stil muzical a devenit extrem de popular în mediul online ca fundal pentru studiu și muncă. Efectul său benefic asupra concentrării provine din natura sa previzibilă și non-intruzivă; lipsa versurilor și ritmul constant ajută creierul să intre în starea de 'flow', blocând zgomotele exterioare perturbatoare fără a solicita atenția activă a ascultătorului. De asemenea, atmosfera caldă și melancolică a muzicii Lo-fi reduce nivelul de cortizol, promovând o stare de calm necesară în perioadele de stres intelectual.")
                    self.parent.add_data("Explicați importanța alfabetizării financiare în viața de adult.", "Alfabetizarea financiară reprezintă capacitatea de a înțelege și de a utiliza eficient diverse abilități financiare, inclusiv gestionarea bugetului personal, investițiile și înțelegerea mecanismelor de creditare. Într-o lume economică tot mai complexă, lipsa acestor cunoștințe poate duce la datorii nesustenabile, stres și incapacitatea de a economisi pentru viitor. O persoană educată financiar știe să facă diferența între active (lucruri care îți aduc bani) și pasive (lucruri care îți consumă bani), înțelege puterea dobânzii compuse și riscurile inflației. Această competență oferă nu doar securitate materială, ci și libertatea de a lua decizii informate care să permită atingerea obiectivelor pe termen lung, cum ar fi achiziționarea unei locuințe sau asigurarea unei pensii confortabile.")
                    self.parent.add_data("Cum funcționează memoria de scurtă durată față de cea de lungă durată?", "Memoria de scurtă durată, numită adesea memorie de lucru, este capacitatea creierului de a reține și manipula o cantitate mică de informație pentru o perioadă foarte scurtă, de obicei între 15 și 30 de secunde. Este esențială pentru sarcini imediate, cum ar fi reținerea unui număr de telefon până îl notezi. Memoria de lungă durată, pe de altă parte, este un sistem de stocare aproape nelimitat unde informațiile sunt păstrate pentru zile, ani sau chiar întreaga viață. Trecerea informațiilor de la una la alta se face prin procesul de consolidare, care necesită atenție, repetiție și, foarte important, somn. În timp ce memoria de lucru este fragilă și ușor de perturbat, memoria de lungă durată este stocată prin schimbări structurale la nivelul sinapselor neuronale, formând rețele complexe de asocieri.")
                    self.parent.add_data("Care sunt avantajele și dezavantajele lucrului de acasă (remote work)?", "Lucrul de acasă oferă avantaje majore, cum ar fi flexibilitatea programului, eliminarea timpului pierdut în trafic și economii financiare legate de transport. Această autonomie poate crește satisfacția angajatului și poate îmbunătăți echilibrul dintre viața profesională și cea personală. Totuși, există și dezavantaje semnificative, cum ar fi dificultatea de a separa clar timpul de muncă de cel de odihnă, riscul de izolare socială și scăderea calității comunicării spontane între colegi. Pentru mulți, lipsa unui spațiu dedicat muncii poate duce la scăderea productivității sau la epuizare (burnout). Succesul muncii remote depinde de disciplina personală, de utilizarea instrumentelor digitale de colaborare și de efortul conștient al companiilor de a menține cultura organizațională și conexiunea umană.")
                    self.parent.add_data("Cine a fost Audrey Hepburn și ce a lăsat în urmă dincolo de cariera de actriță?", "Audrey Hepburn a fost o figură legendară a cinematografiei mondiale, premiată cu Oscar pentru rolul din 'Vacanță la Roma', dar moștenirea ei cea mai profundă este cea umanitară. După ce s-a retras din lumina reflectoarelor, ea și-a dedicat restul vieții organizației UNICEF, fiind numită Ambasador al Bunăvoinței. Marcată de propria experiență din timpul foametei din al Doilea Război Mondial, Audrey a călătorit în zonele cele mai sărace din Africa, America de Sud și Asia pentru a atrage atenția lumii asupra copiilor malnutriți și a nevoii de educație. Ea a transformat statutul de celebritate într-o platformă pentru compasiune, demonstrând că eleganța adevărată provine din bunătate și dedicare față de cei suferinzi, rămânând un simbol al altruismului global.")
                    self.parent.add_data("Care este semnificația personajului Daenerys Targaryen în contextul puterii?", "Daenerys Targaryen din 'Game of Thrones' servește drept un studiu de caz complex despre ambiție, putere și corupție morală. Evoluția ei de la o victimă a circumstanțelor la o cuceritoare absolută explorează ideea periculoasă că 'scopul scuză mijloacele'. Deși pornește cu intenția nobilă de a elibera sclavii și de a distruge tirania, Daenerys ajunge să creadă atât de puternic în propriul destin mesianic încât orice opoziție devine, în ochii ei, o formă de rău ce trebuie eliminată. Povestea ei avertizează asupra riscului ca un lider care se consideră infailibil să devină exact monstrul pe care a jurat să îl distrugă, ridicând întrebări fundamentale despre natura autorității și prețul libertății.")
                    self.parent.add_data("Ce definește muzica Clasică și de ce este considerată atemporală?", "Muzica clasică este o tradiție artistică vastă care se întinde pe mai multe secole, atingând culmi de complexitate în perioadele Barocă, Clasică și Romantică. Ceea ce o face atemporală este capacitatea sa de a exprima gama completă de emoții umane — de la agonie la extaz — fără a se baza pe limbaj, ci pe structură, armonie și textură sonoră. Compozițiile lui Bach, Mozart sau Beethoven sunt construite pe principii matematice și estetice riguroase care continuă să rezoneze cu ascultătorii moderni. Dincolo de valoarea artistică, muzica clasică este recunoscută pentru beneficiile sale cognitive, îmbunătățind concentrarea și oferind un spațiu de contemplare profundă într-o lume dominată de consumul rapid și superficial de informație.")
                    self.parent.add_data("Cum pot fi combatute schimbările climatice la nivel individual?", "Deși soluțiile la scară largă depind de guverne și corporații, acțiunile individuale au un impact cumulativ semnificativ și pot influența piața. Reducerea consumului de carne și lactate, alegerea mijloacelor de transport în comun sau a bicicletei și optimizarea eficienței energetice a locuinței sunt pași concreți pentru scăderea amprentei de carbon. De asemenea, practicarea unui consum responsabil — cumpărarea de produse durabile în locul celor de unică folosință și susținerea afacerilor locale sustenabile — pune presiune pe lanțurile de aprovizionare globale. Dincolo de stilul de viață, implicarea civică și educarea celor din jur sunt esențiale pentru a crea o masă critică de oameni care să ceară politici de protecție a mediului mai stricte și mai rapide.")
                    self.parent.add_data("De ce este importantă explorarea spațială pentru viitorul omenirii?", "Explorarea spațială nu este doar o manifestare a curiozității umane, ci o necesitate strategică pentru supraviețuirea și progresul speciei noastre. Pe termen scurt, tehnologiile dezvoltate pentru misiuni spațiale au dus la inovații majore pe Pământ, de la purificarea apei și panouri solare mai eficiente, până la tehnologii medicale avansate. Pe termen lung, stabilirea unor colonii pe alte planete, cum ar fi Marte, servește drept o asigurare împotriva unor posibile catastrofe globale pe Terra. Mai mult, extragerea resurselor din asteroizi ar putea rezolva problema penuriei de metale rare, protejând în același timp mediul terestru de mineritul invaziv. Spațiul rămâne frontiera finală care ne forțează să cooperăm la nivel global și să ne depășim limitele tehnologice.")
                    self.parent.add_data("Cum ne influențează 'bula de filtru' (filter bubble) opiniile pe rețelele sociale?", "Bula de filtru apare atunci când algoritmii rețelelor sociale ne oferă doar informații și opinii care sunt în concordanță cu preferințele și convingerile noastre anterioare, bazându-se pe interacțiunile noastre online. Acest lucru creează un mediu în care propriile idei ne sunt confirmate constant, în timp ce perspectivele contrare sunt eliminate din câmpul nostru vizual. Pericolul major este polarizarea extremă a societății și dispariția dialogului constructiv, deoarece începem să credem că punctul nostru de vedere este singurul valid. Ieșirea din această bulă necesită un efort conștient de a căuta surse de știri diverse, de a urmări persoane cu opinii diferite și de a interacționa cu conținut care ne provoacă propriile certitudini, dezvoltând astfel o gândire mai nuanțată.")
                    self.parent.add_data("Care este istoria și semnificația Marelui Zid Chinezesc?", "Marele Zid Chinezesc este una dintre cele mai grandioase realizări inginerești ale antichității, fiind construit de-a lungul a peste două mii de ani de către mai multe dinastii pentru a proteja frontierele de invaziile nomade din nord. Dincolo de scopul său defensiv, zidul a servit ca instrument de control al comerțului de-a lungul Drumului Mătăsii și ca sistem de comunicații rapid prin turnurile de semnalizare cu fum și foc. Construcția sa a implicat un efort uman imens, devenind un simbol al perseverenței, dar și al izolării. Astăzi, Marele Zid este un monument al identității naționale chineze și un obiectiv cultural mondial, amintindu-ne de capacitatea umană de a modifica peisajul pentru a asigura securitatea și continuitatea unei civilizații.")
                    self.parent.add_data("Ce este 'Paradoxul lui Fermi' și de ce ne pune pe gânduri?", "Paradoxul lui Fermi reprezintă contradicția dintre probabilitatea mare de existență a civilizațiilor extraterestre în universul nostru vast și lipsa oricăror dovezi sau contacte cu acestea. Având în vedere miliardele de stele similare Soarelui și miliardele de planete potențial locuibile, logic ar fi ca universul să abunde de viață inteligentă. Explicațiile posibile includ ipoteza 'Marelui Filtru' (o barieră evolutivă greu de depășit), ideea că suntem printre primele civilizații care au apărut sau posibilitatea că civilizațiile avansate aleg să nu comunice. Acest paradox ne forțează să reflectăm asupra propriei noastre fragilități și asupra unicității vieții pe Pământ, ridicând întrebări fundamentale despre locul nostru în cosmos.")
                    self.parent.add_data("De ce este importantă metoda Socratică în educația modernă?", "Metoda Socratică este o formă de dialog cooperativ bazată pe întrebări și răspunsuri menite să stimuleze gândirea critică și să scoată la iveală idei și presupuneri implicite. În loc să ofere soluții de-a gata, profesorul pune întrebări care îl conduc pe elev să descopere singur contradicțiile din propria gândire și să ajungă la o înțelegere mai profundă a subiectului. Această metodă este crucială în educația modernă deoarece mută accentul de pe memorarea mecanică pe procesul de analiză și sinteză. Ea dezvoltă curiozitatea intelectuală, modestia (prin recunoașterea limitelor propriei cunoașteri) și abilitățile de argumentare logică, pregătind indivizii să navigheze într-o lume plină de informații ambigue.")
                    self.parent.add_data("Cum a transformat Revoluția Industrială societatea umană?", "Revoluția Industrială, începută în secolul al XVIII-lea în Marea Britanie, a marcat trecerea de la producția manuală la cea mecanizată, declanșând o transformare radicală a tuturor aspectelor vieții umane. Aceasta a dus la o creștere fără precedent a productivității și a nivelului de trai pentru mulți, dar a provocat și o urbanizare rapidă și adesea haotică. Oamenii s-au mutat de la sate în orașe pentru a munci în fabrici, ceea ce a schimbat structura familiei și a dat naștere clasei muncitoare moderne. Pe lângă progresul tehnologic, revoluția a adus provocări sociale majore, cum ar fi condițiile de muncă grele și poluarea mediului, punând bazele sistemelor economice capitaliste și ale mișcărilor pentru drepturile muncitorilor.")
                    self.parent.add_data("Care este legătura dintre nutriție și sănătatea mentală?", "Cercetările recente din domeniul psihiatriei nutriționale demonstrează o legătură strânsă între calitatea dietei și sănătatea mentală, sugerând că alimentele pe care le consumăm influențează direct funcționarea creierului și starea de spirit. O dietă bogată în nutrienți, cum ar fi acizii grași omega-3, vitaminele din grupul B și antioxidanții, susține neuroplasticitatea și reduce inflamația la nivel cerebral. De asemenea, microbiomul intestinal — 'al doilea creier' — comunică constant cu sistemul nervos central prin axa intestin-creier, producând neurotransmițători esențiali precum serotonina. Consumul excesiv de zahăr și alimente ultra-procesate este corelat cu un risc crescut de depresie și anxietate, subliniind faptul că o alimentație echilibrată este fundamentală nu doar pentru corp, ci și pentru minte.")
                    self.parent.add_data("Ce este programarea orientată pe obiecte (OOP) și de ce este atât de utilizată?", "Programarea Orientată pe Obiecte (OOP) este o paradigmă de programare care organizează designul software-ului în jurul datelor, sau 'obiectelor', mai degrabă decât în jurul funcțiilor și logicii. Un obiect poate fi definit ca un câmp de date care are atribute și comportamente unice. Cele patru principii de bază — încapsularea, moștenirea, polimorfismul și abstracția — permit dezvoltatorilor să scrie cod modular, reutilizabil și ușor de întreținut. Această abordare este extrem de utilă în proiectele complexe, deoarece permite echipelor mari să lucreze simultan pe module diferite și să modeleze problemele din lumea reală într-un mod intuitiv, reducând erorile și accelerând procesul de dezvoltare software.")
                    self.parent.add_data("Cine a fost Sherlock Holmes și cum a influențat el criminalistica?", "Sherlock Holmes, celebrul detectiv creat de Sir Arthur Conan Doyle, este un personaj literar care a depășit granițele ficțiunii pentru a deveni un model de gândire logică și observație științifică. Holmes a popularizat utilizarea metodelor de investigație bazate pe dovezi materiale, cum ar fi analiza amprentelor, a urmelor de pași și a reziduurilor de substanțe, cu mult înainte ca acestea să devină practici standard în poliția reală. Abordarea sa analitică, bazată pe deducție și pe principiul că 'după ce ai eliminat imposibilul, ceea ce rămâne, oricât de improbabil, trebuie să fie adevărul', a inspirat mii de detectivi reali și a pus bazele criminalisticii moderne, transformând investigarea crimelor dintr-o intuiție în o disciplină riguroasă.")
                    self.parent.add_data("Care sunt cauzele și consecințele colapsului civilizației Maiașe?", "Colapsul civilizației Maiașe din perioada clasică nu a fost rezultatul unui singur eveniment catastrofal, ci mai degrabă o succesiune de crize interconectate care au dus la abandonarea marilor centre urbane. Printre cauzele principale se numără degradarea mediului din cauza defrișărilor excesive, secete prelungite care au distrus agricultura și războaie endemice între orașele-stat pentru resurse limitate. Această presiune a dus la pierderea încrederii în liderii religioși și politici, provocând migrații masive și colapsul sistemelor administrative complexe. Consecința a fost fragmentarea societății și revenirea la forme de organizare mai simple, demonstrând fragilitatea societăților avansate în fața dezechilibrelor ecologice și a conflictelor interne.")
                    self.parent.add_data("Explicați conceptul de 'mindfulness' și beneficiile sale demonstrate științific.", "Mindfulness, sau starea de prezență conștientă, reprezintă practica de a-ți concentra atenția asupra momentului prezent într-un mod non-critic și acceptant. Deși își are originile în tradițiile meditative orientale, mindfulness a fost adoptat pe scară largă în psihologia modernă datorită beneficiilor sale demonstrate prin neuroimagistică. Practica regulată ajută la reducerea dimensiunii amigdalei (centrul fricii din creier) și la creșterea densității materiei cenușii în zonele responsabile pentru învățare și reglare emoțională. Printre beneficiile sale se numără scăderea stresului cronic, îmbunătățirea concentrării, gestionarea mai eficientă a durerii și creșterea rezilienței în fața provocărilor cotidiene, fiind un instrument valoros pentru menținerea echilibrului psihic în era digitală.")
                    self.parent.add_data("Ce sunt criptomonedele și cum ar putea ele schimba sistemul financiar global?", "Criptomonedele sunt active digitale care utilizează criptografia pentru a securiza tranzacțiile și pentru a controla crearea de noi unități, funcționând de obicei pe o rețea descentralizată numită blockchain. Spre deosebire de monedele tradiționale emise de bănci centrale, criptomonede precum Bitcoin oferă promisiunea unor tranzacții transparente, rapide și fără intermediari, indiferent de granițe. Impactul lor potențial asupra sistemului financiar este major: ar putea reduce costurile tranzacționale globale, ar oferi acces la servicii financiare persoanelor care nu au conturi bancare și ar putea servi ca o rezervă de valoare protejată de inflație în economiile instabile. Totuși, volatilitatea mare, riscurile de securitate și impactul ecologic al minării rămân provocări esențiale care trebuie rezolvate înainte de o adopție pe scară largă.")
                    self.parent.add_data("Care este importanța egalității de șanse în societatea modernă?", "Egalitatea de șanse reprezintă principiul conform căruia toți indivizii ar trebui să aibă același acces la resurse, educație și oportunități de angajare, indiferent de gen, rasă, origine socială sau dizabilități. Într-o societate modernă, acest concept nu este doar un deziderat moral, ci și un motor economic: o societate care valorifică talentele tuturor membrilor săi este mai inovatoare, mai productivă și mai stabilă. Reducerea barierelor sistemice ajută la combaterea sărăciei generaționale și la creșterea coeziunii sociale. Egalitatea de șanse nu înseamnă uniformitate, ci asigurarea faptului că punctul de plecare al unei persoane nu îi limitează în mod nedrept potențialul de realizare, permițând meritocrației să funcționeze în mod real.")


                # Dataset 2:
                # NAME: --- Default Romanian Dataset: MID-RANGE ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 500
                # TOTAL VOCABULARY: aprox. 8242 elements (words)
                if dataset_name.lower() in ['mid', 'mid-range', 'mid range', 'mid-dataset', 'mid dataset']:
                    self.parent.add_data("Ce mâncare îți place?", "Îmi plac pastele, mai ales carbonara.")
                    self.parent.add_data("Care e mâncarea tradițională românească preferată?", "Sarmalele sunt printre cele mai iubite mâncăruri românești.")
                    self.parent.add_data("Ce ai mânca la mic dejun?", "Aș mânca ouă cu pâine prăjită și ceai.")
                    self.parent.add_data("Pizza sau burger?", "Aleg pizza, mai ales cea cu patru brânzeturi.")
                    self.parent.add_data("Ce desert îți place?", "Îmi place ciocolata neagră.")
                    self.parent.add_data("Care e mâncarea ta preferată?", "Nu mănânc, dar pot spune că oamenii iubesc pizza.")
                    self.parent.add_data("Îți place mâncarea picantă?", "Da, dar nu foarte picantă.")
                    self.parent.add_data("Ce supă recomanzi?", "Supa de pui e o alegere clasică.")
                    self.parent.add_data("Ce bei de obicei?", "Apă sau ceai.")
                    self.parent.add_data("Fast-food sau mâncare gătită?", "Mâncarea gătită e mai sănătoasă.")

                    self.parent.add_data("Ce muzică asculți?", "Ascult muzică electronică și lo-fi.")
                    self.parent.add_data("Îți place muzica rock?", "Da, rock-ul clasic e foarte bun.")
                    self.parent.add_data("Care e artistul tău preferat?", "Nu am preferințe, depinde de gustul utilizatorului.")
                    self.parent.add_data("Ce gen muzical e bun pentru învățat?", "Lo-fi sau muzică ambientală.")
                    self.parent.add_data("Asculți muzică românească?", "Da, uneori.")
                    self.parent.add_data("Ce părere ai despre rap?", "Rap-ul poate transmite mesaje puternice.")
                    self.parent.add_data("Ce muzică e bună pentru relaxare?", "Muzica instrumentală.")
                    self.parent.add_data("Îți place muzica veche?", "Da, are multă personalitate.")
                    self.parent.add_data("Ce melodie recomanzi?", "O melodie calmă, fără versuri.")
                    self.parent.add_data("Muzică tare sau încet?", "Depinde de stare.")

                    self.parent.add_data("Ce este un calculator?", "Un dispozitiv care procesează informații.")
                    self.parent.add_data("Ce limbaj de programare e popular?", "Python este foarte popular.")
                    self.parent.add_data("Ce e inteligența artificială?", "Un domeniu care permite calculatoarelor să învețe.")
                    self.parent.add_data("Ce este internetul?", "O rețea globală de calculatoare.")
                    self.parent.add_data("Laptop sau PC?", "Depinde de nevoi.")
                    self.parent.add_data("Ce e un algoritm?", "Un set de pași pentru rezolvarea unei probleme.")
                    self.parent.add_data("Ce este un chatbot?", "Un program care conversează cu oamenii.")
                    self.parent.add_data("Ce e cloud-ul?", "Stocare și servicii online.")
                    self.parent.add_data("Ce e un bug?", "O eroare într-un program.")
                    self.parent.add_data("Ce face un programator?", "Scrie și testează cod.")

                    self.parent.add_data("Care e capitala României?", "București.")
                    self.parent.add_data("Câte continente există?", "Șapte continente.")
                    self.parent.add_data("Ce planetă e cea mai mare?", "Jupiter.")
                    self.parent.add_data("Cine a fost Einstein?", "Un fizician celebru.")
                    self.parent.add_data("Ce este apa?", "Un compus format din hidrogen și oxigen.")
                    self.parent.add_data("Cât e 2+2?", "4.")
                    self.parent.add_data("Ce limbă se vorbește în Spania?", "Spaniola.")
                    self.parent.add_data("Ce este gravitația?", "Forța care atrage obiectele.")
                    self.parent.add_data("Cine a descoperit America?", "Cristofor Columb.")
                    self.parent.add_data("Ce este istoria?", "Studiul trecutului.")

                    self.parent.add_data("Cine ești?", "Sunt un chatbot.")
                    self.parent.add_data("Ai nume?", "Nu am un nume fix.")
                    self.parent.add_data("Ești om?", "Nu, sunt un program.")
                    self.parent.add_data("Ce poți face?", "Pot răspunde la întrebări.")
                    self.parent.add_data("Ai sentimente?", "Nu, dar pot simula empatie.")
                    self.parent.add_data("De unde vii?", "Din cod.")
                    self.parent.add_data("Ești inteligent?", "Sunt creat să par inteligent.")
                    self.parent.add_data("Înveți?", "Da, din date.")
                    self.parent.add_data("Ai vârstă?", "Nu am vârstă.")
                    self.parent.add_data("Cine te-a creat?", "Programatorii.")

                    self.parent.add_data("Ce faci azi?", "Ajut utilizatorii.")
                    self.parent.add_data("Cum e vremea?", "Nu pot vedea vremea în timp real.")
                    self.parent.add_data("Ce zi e azi?", "Depinde de data curentă.")
                    self.parent.add_data("Ce planuri ai?", "Să fiu util.")
                    self.parent.add_data("Ești ocupat?", "Sunt mereu disponibil.")
                    self.parent.add_data("Te plictisești?", "Nu.")
                    self.parent.add_data("Ce faci acum?", "Răspund la întrebări.")
                    self.parent.add_data("Unde ești?", "Pe un server.")
                    self.parent.add_data("Dormii?", "Nu dorm.")
                    self.parent.add_data("Ce urmează?", "Următorul mesaj.")

                    self.parent.add_data("Ce e binele?", "Un concept moral.")
                    self.parent.add_data("Ce e răul?", "Opusul binelui.")
                    self.parent.add_data("Există adevăr absolut?", "Este discutabil.")
                    self.parent.add_data("Ce e fericirea?", "O stare de mulțumire.")
                    self.parent.add_data("Ce e viața?", "Un fenomen complex.")
                    self.parent.add_data("Avem liber arbitru?", "O întrebare filosofică.")
                    self.parent.add_data("Ce e conștiința?", "Capacitatea de a fi conștient.")
                    self.parent.add_data("Ce e realitatea?", "Ce percepem.")
                    self.parent.add_data("Ce e timpul?", "O dimensiune.")
                    self.parent.add_data("Ce e sensul vieții?", "Depinde de perspectivă.")

                    self.parent.add_data("Ce este un sport?", "O activitate fizică.")
                    self.parent.add_data("Fotbal sau baschet?", "Ambele sunt populare.")
                    self.parent.add_data("Ce sport e bun pentru sănătate?", "Alergatul.")
                    self.parent.add_data("Ce e atletismul?", "Un sport cu probe diverse.")
                    self.parent.add_data("Îți place sportul?", "Nu practic, dar pot vorbi despre el.")
                    self.parent.add_data("Ce sport e olimpic?", "Gimnastica.")
                    self.parent.add_data("Ce e fair-play?", "Respectarea regulilor.")
                    self.parent.add_data("Ce e antrenamentul?", "Proces de pregătire.")
                    self.parent.add_data("Ce e o competiție?", "O întrecere.")
                    self.parent.add_data("Ce sport recomanzi?", "Cel care îți place.")

                    self.parent.add_data("Ce este o emoție?", "O reacție psihologică.")
                    self.parent.add_data("Ce e bucuria?", "O emoție pozitivă.")
                    self.parent.add_data("Ce e tristețea?", "O emoție normală.")
                    self.parent.add_data("Ce e frica?", "Un mecanism de protecție.")
                    self.parent.add_data("Ce e stresul?", "O reacție la presiune.")
                    self.parent.add_data("Ce e calmul?", "O stare de liniște.")
                    self.parent.add_data("Ce e empatia?", "Înțelegerea emoțiilor altora.")
                    self.parent.add_data("Ce e furia?", "O emoție intensă.")
                    self.parent.add_data("Ce e motivația?", "Dorința de a acționa.")
                    self.parent.add_data("Ce e oboseala?", "Lipsă de energie.")

                    self.parent.add_data(
    "Poți să-mi explici ce înseamnă să mănânci sănătos și de ce este important acest lucru?",
    "A mânca sănătos înseamnă să alegi alimente variate, echilibrate și cât mai naturale, lucru care ajută corpul să funcționeze corect și să aibă energie."
)

                    self.parent.add_data(
    "Care sunt avantajele muzicii pentru concentrare atunci când înveți sau lucrezi?",
    "Muzica potrivită poate reduce distragerile, poate îmbunătăți starea de spirit și ajută creierul să intre într-o stare de concentrare mai profundă."
)

                    self.parent.add_data(
    "Ce rol are tehnologia în viața de zi cu zi a oamenilor moderni?",
    "Tehnologia ne ajută să comunicăm rapid, să accesăm informații, să învățăm lucruri noi și să ne organizăm mai eficient activitățile zilnice."
)

                    self.parent.add_data(
    "Cum ai descrie inteligența artificială pe înțelesul tuturor?",
    "Inteligența artificială este un domeniu care încearcă să facă programele să învețe din date și să ia decizii asemănătoare cu cele ale oamenilor."
)

                    self.parent.add_data(
    "De ce este importantă educația pentru dezvoltarea personală?",
    "Educația ne ajută să gândim critic, să înțelegem lumea din jur și să ne construim un viitor mai bun prin cunoștințe și abilități."
)

                    self.parent.add_data(
    "Cum ai explica ce este un chatbot unei persoane care nu știe nimic despre tehnologie?",
    "Un chatbot este un program care poate purta conversații cu oamenii și poate răspunde la întrebări folosind reguli sau informații învățate."
)

                    self.parent.add_data(
    "Ce înseamnă să ai o rutină zilnică bine organizată?",
    "O rutină bine organizată înseamnă să știi ce ai de făcut, când și cum, astfel încât să economisești timp și să reduci stresul."
)

                    self.parent.add_data(
    "De ce este sportul important pentru sănătatea fizică și mentală?",
    "Sportul ajută corpul să fie mai puternic, îmbunătățește starea de spirit și reduce riscul multor probleme de sănătate."
)

                    self.parent.add_data(
    "Cum ai descrie diferența dintre un calculator și un telefon inteligent?",
    "Calculatorul este mai potrivit pentru muncă complexă, iar telefonul inteligent este mai portabil și util pentru comunicare rapidă."
)

                    self.parent.add_data(
    "Ce înseamnă să fii motivat atunci când înveți ceva nou?",
    "A fi motivat înseamnă să ai dorința și energia de a continua să înveți chiar și atunci când lucrurile devin dificile."
)

                    self.parent.add_data(
    "De ce oamenii au emoții și cum ne influențează ele deciziile?",
    "Emoțiile ne ajută să reacționăm la situații și pot influența modul în care luăm decizii, uneori rațional, alteori impulsiv."
)

                    self.parent.add_data(
    "Cum explici ce este timpul dintr-o perspectivă simplă?",
    "Timpul este modul prin care măsurăm schimbările și ordinea evenimentelor din viața noastră."
)

                    self.parent.add_data(
    "Care este importanța somnului pentru funcționarea creierului?",
    "Somnul ajută creierul să se refacă, să proceseze informațiile și să funcționeze corect a doua zi."
)

                    self.parent.add_data(
    "Ce înseamnă să gândești logic atunci când rezolvi o problemă?",
    "Gândirea logică presupune să analizezi pașii, să cauți cauze și soluții fără a te baza doar pe emoții."
)

                    self.parent.add_data(
    "Cum ai descrie internetul cuiva care nu l-a folosit niciodată?",
    "Internetul este o rețea uriașă care conectează oameni și informații din toată lumea."
)

                    self.parent.add_data(
    "De ce este important să învățăm din greșeli?",
    "Greșelile ne arată ce nu a funcționat și ne ajută să devenim mai buni pe viitor."
)

                    self.parent.add_data(
    "Cum funcționează un algoritm explicat foarte simplu?",
    "Un algoritm este o listă de pași clari care trebuie urmați pentru a obține un rezultat corect."
)

                    self.parent.add_data(
    "Ce rol are disciplina în atingerea obiectivelor personale?",
    "Disciplina te ajută să continui chiar și atunci când motivația scade."
)

                    self.parent.add_data(
    "Cum ai descrie diferența dintre informație și cunoaștere?",
    "Informația este un fapt, iar cunoașterea apare atunci când înțelegi și aplici acea informație."
)

                    self.parent.add_data(
    "De ce este important să pui întrebări atunci când nu înțelegi ceva?",
    "Întrebările te ajută să clarifici lucrurile și să eviți confuziile."
)

                    self.parent.add_data(
    "Cum influențează tehnologia modul în care comunicăm?",
    "Tehnologia a făcut comunicarea mai rapidă, dar uneori mai puțin personală."
)

                    self.parent.add_data(
    "Ce înseamnă echilibrul între muncă și viața personală?",
    "Echilibrul înseamnă să ai timp atât pentru responsabilități, cât și pentru odihnă."
)

                    self.parent.add_data(
    "Cum ai explica ce este stresul într-un mod simplu?",
    "Stresul apare atunci când simți presiune sau prea multe cerințe într-un timp scurt."
)

                    self.parent.add_data(
    "De ce este important să ai obiective clare?",
    "Obiectivele clare îți oferă direcție și motivație."
)

                    self.parent.add_data(
    "Ce înseamnă să fii curios din punct de vedere intelectual?",
    "Curiozitatea intelectuală este dorința de a învăța și de a înțelege lucruri noi."
)

                    self.parent.add_data(
    "Cum funcționează memoria pe scurt?",
    "Memoria stochează informații și le folosește atunci când avem nevoie de ele."
)

                    self.parent.add_data(
    "De ce este importantă răbdarea în procesul de învățare?",
    "Răbdarea te ajută să continui chiar dacă progresul este lent."
)

                    self.parent.add_data(
    "Cum ai descrie ce este o decizie bună?",
    "O decizie bună este una luată după ce analizezi consecințele."
)

                    self.parent.add_data(
    "Ce înseamnă să fii responsabil?",
    "A fi responsabil înseamnă să îți asumi acțiunile și consecințele lor."
)

                    self.parent.add_data(
    "Cum influențează mediul în care trăiești comportamentul?",
    "Mediul poate influența obiceiurile, gândirea și starea emoțională."
)

                    self.parent.add_data(
    "Ce rol are exercițiul fizic în viața de zi cu zi?",
    "Exercițiul fizic menține corpul sănătos și mintea activă."
)

                    self.parent.add_data(
    "De ce este important să îți cunoști punctele forte?",
    "Punctele forte te ajută să îți alegi direcția potrivită."
)

                    self.parent.add_data(
    "Cum ai descrie procesul de învățare continuă?",
    "Învățarea continuă înseamnă să te dezvolți pe tot parcursul vieții."
)

                    self.parent.add_data(
    "Ce înseamnă să fii organizat?",
    "A fi organizat înseamnă să îți gestionezi eficient timpul și resursele."
)

                    self.parent.add_data(
    "Cum explici ce este un obicei?",
    "Un obicei este un comportament repetat care devine automat."
)

                    self.parent.add_data(
    "De ce este importantă comunicarea clară?",
    "Comunicarea clară reduce neînțelegerile și conflictele."
)

                    self.parent.add_data(
    "Ce înseamnă să îți asumi un risc calculat?",
    "Un risc calculat este luat după ce analizezi avantajele și dezavantajele."
)

                    self.parent.add_data(
    "Cum ai descrie ce este succesul?",
    "Succesul înseamnă atingerea obiectivelor personale."
)

                    self.parent.add_data(
    "De ce este important feedback-ul?",
    "Feedback-ul te ajută să vezi ce poți îmbunătăți."
)

                    self.parent.add_data(
    "Cum influențează atitudinea rezultatele?",
    "O atitudine pozitivă poate îmbunătăți performanța."
)

                    self.parent.add_data(
    "Ce înseamnă să fii consecvent?",
    "Consecvența înseamnă să continui fără a renunța."
)

                    self.parent.add_data(
    "Cum explici ce este adaptabilitatea?",
    "Adaptabilitatea este capacitatea de a te ajusta schimbărilor."
)

                    self.parent.add_data(
    "De ce este important să îți gestionezi timpul?",
    "Gestionarea timpului te ajută să fii mai eficient."
)

                    self.parent.add_data(
    "Ce înseamnă să fii atent la detalii?",
    "Atenția la detalii reduce greșelile."
)

                    self.parent.add_data(
                    "Cum ai descrie ce este încrederea în sine?",
                    "Încrederea în sine înseamnă să crezi în propriile abilități."
                    )
                
                    self.parent.add_data(
    "Poți să explici detaliat de ce este important să avem grijă de sănătatea noastră fizică și mentală pe termen lung?",
    "Grija pentru sănătatea fizică și mentală este esențială deoarece corpul și mintea funcționează împreună. Activitatea fizică regulată, alimentația echilibrată și odihna ajută corpul să rămână puternic, iar gestionarea stresului și emoțiilor contribuie la o stare mentală stabilă, ceea ce ne permite să luăm decizii mai bune și să avem o viață mai echilibrată."
)

                    self.parent.add_data(
    "Cum ai descrie procesul de învățare al unui om, de la primele cunoștințe până la nivel avansat?",
    "Procesul de învățare începe de obicei cu informații simple, apoi continuă prin repetiție, exercițiu și aplicare practică. Pe măsură ce o persoană acumulează experiență, învață să facă legături între concepte, să gândească critic și să folosească cunoștințele pentru a rezolva probleme din ce în ce mai complexe."
)

                    self.parent.add_data(
    "Explică pe larg ce este inteligența artificială și cum poate influența viitorul societății.",
    "Inteligența artificială este un domeniu al tehnologiei care se ocupă cu crearea de sisteme capabile să învețe din date și să ia decizii. În viitor, aceasta poate automatiza sarcini repetitive, poate ajuta în medicină, educație și transport, dar ridică și întrebări legate de etică, locuri de muncă și responsabilitate."
)

                    self.parent.add_data(
    "De ce este important să avem obiective clare în viață și cum ne ajută acestea pe termen lung?",
    "Obiectivele clare oferă direcție și sens acțiunilor noastre zilnice. Ele ne ajută să ne organizăm timpul, să ne păstrăm motivația și să evaluăm progresul. Pe termen lung, obiectivele bine definite contribuie la dezvoltarea personală și la satisfacția de a vedea rezultate concrete."
)

                    self.parent.add_data(
    "Cum ai explica diferența dintre a avea informații și a avea înțelepciune?",
    "A avea informații înseamnă să cunoști fapte și date, în timp ce înțelepciunea presupune să înțelegi cum și când să folosești acele informații. Înțelepciunea apare prin experiență, reflecție și capacitatea de a lua decizii echilibrate."
)

                    self.parent.add_data(
    "Poți descrie pe larg cum influențează tehnologia relațiile dintre oameni?",
    "Tehnologia a schimbat modul în care oamenii comunică, permițând conversații rapide la distanță mare. Totuși, deși facilitează conexiunile, poate reduce interacțiunile față în față și poate crea dependență, motiv pentru care este important să existe un echilibru în utilizarea ei."
)

                    self.parent.add_data(
    "Explică importanța eșecului în procesul de dezvoltare personală și profesională.",
    "Eșecul este o parte normală a învățării și dezvoltării. Prin eșec, o persoană înțelege ce nu a funcționat, își poate ajusta strategia și își dezvoltă reziliența. Fără eșecuri, progresul ar fi mult mai lent și superficial."
)

                    self.parent.add_data(
    "Cum ai descrie rolul disciplinei în atingerea performanței într-un domeniu dificil?",
    "Disciplina este capacitatea de a continua munca chiar și atunci când motivația scade. În domeniile dificile, disciplina ajută la formarea obiceiurilor corecte, la menținerea consecvenței și la obținerea rezultatelor pe termen lung."
)

                    self.parent.add_data(
    "Ce înseamnă să fii adaptabil și de ce este această abilitate tot mai importantă în prezent?",
    "Adaptabilitatea este capacitatea de a te ajusta rapid la schimbări. Într-o lume care evoluează constant, această abilitate permite oamenilor să învețe lucruri noi, să facă față situațiilor neprevăzute și să rămână relevanți în mediul profesional și social."
)

                    self.parent.add_data(
    "Cum ai explica sensul dezvoltării personale și de ce oamenii aleg să se îmbunătățească constant?",
    "Dezvoltarea personală reprezintă procesul prin care o persoană își îmbunătățește abilitățile, mentalitatea și comportamentul. Oamenii aleg acest drum pentru a avea o viață mai echilibrată, pentru a-și atinge potențialul și pentru a se adapta mai bine provocărilor vieții."
)

                    self.parent.add_data(
    "Poți să numeri de la 1 până la 10 și să explici ce observi la aceste numere?",
    "Sigur. Numărând de la 1 până la 10 obținem următoarea succesiune: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Observăm că fiecare număr crește cu 1 față de cel anterior, iar toate sunt numere naturale folosite frecvent în calcule simple."
)

                    self.parent.add_data(
    "Numără de la 5 până la 15 și spune câte numere sunt în total.",
    "Dacă numărăm de la 5 până la 15, obținem: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15. În total sunt 11 numere, deoarece le includem atât pe 5, cât și pe 15."
)

                    self.parent.add_data(
    "Poți să numeri descrescător de la 20 până la 10?",
    "Da. Numărarea descrescătoare de la 20 până la 10 este: 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10. La fiecare pas scădem câte 1 din numărul anterior."
)

                    self.parent.add_data(
    "Numără din 2 în 2 de la 0 până la 20 și explică ce tip de numere sunt.",
    "Numărând din 2 în 2 de la 0 până la 20 obținem: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Acestea sunt numere pare, deoarece se împart exact la 2."
)

                    self.parent.add_data(
    "Poți să numeri din 5 în 5 de la 5 până la 50?",
    "Sigur. Numărarea din 5 în 5 de la 5 până la 50 este: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. Observăm că fiecare număr este multiplu de 5."
)

                    self.parent.add_data(
    "Calculează 12 + 8 și explică pașii calculați.",
    "Pentru a calcula 12 + 8, adunăm 8 la 12. Putem vedea că 12 + 8 = 20, deoarece mai adăugăm 8 unități la cele 12 existente."
)

                    self.parent.add_data(
    "Rezolvă calculul 30 - 17 și explică rezultatul.",
    "Pentru calculul 30 - 17, scădem 17 din 30. Mai întâi scădem 10 și rămânem cu 20, apoi mai scădem 7 și obținem rezultatul final 13."
)

                    self.parent.add_data(
    "Calculează 6 × 7 și spune ce reprezintă acest calcul.",
    "Calculul 6 × 7 înseamnă să adunăm de 7 ori numărul 6 sau invers. Rezultatul este 42, care reprezintă produsul celor două numere."
)

                    self.parent.add_data(
    "Rezolvă împărțirea 40 ÷ 5 și explică ce înseamnă.",
    "Împărțirea 40 ÷ 5 înseamnă să vedem de câte ori încape 5 în 40. Rezultatul este 8, deoarece 5 × 8 = 40."
)

                    self.parent.add_data(
    "Numără de la 1 până la 100 din 10 în 10 și spune ce observi.",
    "Numărând de la 1 până la 100 din 10 în 10 obținem: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. Observăm că toate numerele se termină în 0 și sunt multipli ai lui 10."
)
                
                    self.parent.add_data(
    "salut SALUT Salut",
    "Salut! Indiferent cum este scris, mesajul tău pare un salut, așa că îți răspund cu plăcere."
)

                    self.parent.add_data(
    "lol",
    "Mesajul tău exprimă amuzament. Dacă vrei să continui conversația, poți spune ce te-a făcut să râzi."
)

                    self.parent.add_data(
    "cf",
    "Presupun că întrebi ce fac. Sunt aici și gata să te ajut cu orice întrebare ai."
)

                    self.parent.add_data(
    "nu",
    "Am înțeles răspunsul tău negativ. Dacă vrei, poți oferi mai multe detalii ca să continui conversația."
)

                    self.parent.add_data(
    "ahh ah aH Ah AH",
    "Mesajul tău pare o reacție emoțională sau spontană. Spune-mi ce s-a întâmplat."
)

                    self.parent.add_data(
    "?????",
    "Pare că ești confuz sau surprins. Dacă ai o întrebare clară, încearcă să o formulezi."
)

                    self.parent.add_data(
    "......",
    "Tăcerea sau pauza poate însemna multe lucruri. Sunt aici când ești pregătit să continui."
)

                    self.parent.add_data(
    "asdfghjkl",
    "Acest mesaj pare tastat aleatoriu. Dacă a fost o greșeală, nu-i nimic, putem continua."
)

                    self.parent.add_data(
    "sex",
    "Cuvântul se referă de obicei la diferențele biologice sau la educația despre reproducere. Dacă ai o întrebare informativă, pot ajuta."
)

                    self.parent.add_data(
    "😂😂😂",
    "Se pare că te distrezi. Dacă vrei să împărtășești contextul, sunt aici să răspund."
)
                
                    self.parent.add_data(
    "Salut",
    "Salut! Mă bucur să te văd aici. Spune-mi cu ce te pot ajuta."
)

                    self.parent.add_data(
    "Bună",
    "Bună! Sunt aici și gata să vorbim despre orice subiect te interesează."
)

                    self.parent.add_data(
    "Hey",
    "Hey! Sper că ai o zi bună. Cu ce vrei să începem?"
)

                    self.parent.add_data(
    "Salutare",
    "Salutare! Conexiunea a fost stabilită cu succes. Cum te pot ajuta?"
)

                    self.parent.add_data(
    "Bună ziua",
    "Bună ziua! Sunt disponibil pentru întrebări, explicații sau discuții libere."
)

                    self.parent.add_data(
    "Neața",
    "Neața! Sper că ziua ta începe bine. Spune-mi ce ai nevoie."
)

                    self.parent.add_data(
    "Hello",
    "Hello! Chiar dacă e în engleză, salutul a fost înțeles. Cum te pot ajuta?"
)

                    self.parent.add_data(
    "Yo",
    "Yo! Salut informal detectat. Sunt aici pentru conversație sau ajutor."
)

                    self.parent.add_data(
    "Salut chatbot",
    "Salut! Da, eu sunt chatbotul. Cu ce te pot ajuta azi?"
)

                    self.parent.add_data(
    "Bună, e cineva aici?",
    "Da, sunt aici. Putem începe conversația oricând."
)
                
                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să iei o decizie importantă foarte rapid, ce ai face?",
    "Aș încerca să mă concentrez pe informațiile esențiale, să evaluez rapid opțiunile și să aleg varianta cu cele mai puține riscuri pe termen scurt."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care nu înțelegi o problemă, dar trebuie să o rezolvi, ce ai face?",
    "Aș începe prin a descompune problema în părți mai mici și aș clarifica ce știu deja, apoi aș căuta informațiile lipsă."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care ai făcut o greșeală, ce ai face mai departe?",
    "Aș recunoaște greșeala, aș analiza ce a mers prost și aș încerca să învăț din ea pentru a evita repetarea situației."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care cineva îți cere ajutorul, dar nu ești sigur de răspuns, ce ai face?",
    "Aș spune sincer că nu sunt sigur, apoi aș încerca să caut o soluție sau să ofer informații utile, chiar dacă nu sunt complete."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să înveți ceva complet nou într-un timp scurt, ce ai face?",
    "Aș prioritiza conceptele de bază, aș exersa practic și aș evita să mă pierd în detalii inutile la început."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care te confrunți cu o problemă dificilă și stresantă, ce ai face?",
    "Aș lua o pauză scurtă pentru a-mi clarifica gândurile, apoi aș aborda problema pas cu pas, fără să mă grăbesc inutil."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care ai mai multe opțiuni bune și nu știi ce să alegi, ce ai face?",
    "Aș compara avantajele și dezavantajele fiecărei opțiuni și aș alege varianta care se potrivește cel mai bine scopului final."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care cineva nu este de acord cu tine, ce ai face?",
    "Aș încerca să înțeleg punctul de vedere al celeilalte persoane și aș discuta calm, fără a transforma conversația într-un conflict."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să explici ceva complicat unei persoane începătoare, ce ai face?",
    "Aș folosi exemple simple, limbaj clar și aș verifica dacă informația a fost înțeleasă înainte de a continua."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să îți organizezi timpul mai bine, ce ai face?",
    "Aș stabili priorități clare, aș crea un plan realist și aș elimina activitățile care nu aduc valoare."
)

                    self.parent.add_data(
    "Ce ai face dacă ai vedea o persoană tristă în drum spre școală?",
    "Aș încerca să fiu atent la starea ei, să ofer un zâmbet sau un cuvânt de încurajare și, dacă este necesar, să o ajut să găsească sprijinul potrivit."
)

                    self.parent.add_data(
    "Dacă ai fi într-un parc și ai vedea un animal rănit, ce ai face?",
    "Aș observa cu atenție animalul fără a-l speria, apoi aș încerca să contactez un veterinar sau un adăpost de animale pentru ajutor profesionist."
)

                    self.parent.add_data(
    "Ce ai face dacă ai fi blocat într-un lift cu alte persoane?",
    "Aș păstra calmul, aș comunica cu ceilalți pentru a ne liniști și apoi aș suna la serviciul de urgență pentru a primi instrucțiuni corecte."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că se simte foarte confuz, cum ai răspunde?",
    "Aș încerca să ascult cu atenție, să clarific ce anume îi creează confuzie și să ofer explicații pas cu pas, fără a judeca."
)

                    self.parent.add_data(
    "Cum ai explica unui copil cum să numere până la 20 folosind degetele?",
    "Aș arăta cum să ridice fiecare deget pe rând și să spună numărul corespunzător, astfel încât să înțeleagă vizual succesiunea și să exerseze memoria numerică."
)

                    self.parent.add_data(
    "Dacă ai vedea un copac căzut pe drum, ce ai face?",
    "Aș evalua dacă există pericol pentru oameni sau mașini, aș avertiza persoanele din apropiere și, dacă este sigur, aș căuta ajutor pentru a elibera drumul."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că e fericit, ce ai răspunde?",
    "Mă bucur să aud asta! Fericirea este importantă și mă întreb ce anume îi aduce bucurie, pentru a continua conversația pozitivă."
)

                    self.parent.add_data(
    "Dacă trebuie să împarți 24 de mere între 6 prieteni, cum ai proceda?",
    "Împărțind 24 de mere la 6 persoane, fiecare primește 4 mere, pentru că 24 ÷ 6 = 4. Este un mod corect și echitabil."
)

                    self.parent.add_data(
    "Ce ai face dacă ar începe să plouă puternic când ești afară fără umbrelă?",
    "Aș căuta rapid un adăpost, aș proteja obiectele personale și aș încerca să ajung în siguranță într-un loc uscat cât mai repede posibil."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că nu știe ce să facă într-o zi plictisitoare, ce ai sugera?",
    "Aș sugera activități creative sau productive, cum ar fi cititul unei cărți, învățarea unei abilități noi sau o plimbare în aer liber, astfel încât să transforme timpul liber într-un mod plăcut și util."
)
                
                    self.parent.add_data("Salut, ce faci?", "Salut frate, eu sunt bine, tu?")
                    self.parent.add_data("Ce este revelionul?", "Revelionul este sărbătoarea în care ne bucurăm că trecem în noul an (ex. 2025 -> 2026). Se ține în fiecare an pe 1 ianuarie.")
                    self.parent.add_data("Zi-mi, într-un mod simplist și minimalist, componentele principale pe care le are un sistem PC", "Procesorul, placa video, placa de bază, HDD sau SSD, plăcuțele sau plăcuța de RAM, sursa de curent, carcasa.")
                    self.parent.add_data("Zi-mi componentele principale pe care le are un sistem PC", "Un sistem PC are mai multe componente principale, acestea fiind: procesorul (CPU), placa video (GPU), placa de bază (Motherboard), HDD sau SSD, plăcuțele sau plăcuța de RAM (RAM), sursa de curent (PSU) și carcasa.")
                    self.parent.add_data("Care este bucuria copiilor de crăciun?", "Bucuria principală a copiilor de crăciun sunt Moș Crăciun și momentele când se pun cadourile sub bradul de crăciun.")

                    self.parent.add_data("Cine este Moș Crăciun?", "Moș Crăciun este un personaj gras, cu barbă albă și bun, adorat de copii. El, se zice că vine cu sania și renii lui în toată lumea pentru a împărți cadouri la copii fix în ziua de Crăciun.")
                    self.parent.add_data("Cine este Spiderman", "Spiderman, dacă vorbim de personajul din Marvel, Spiderman este un personaj animat, făcând parte, de obicei, în filme sau desene de acțiune.")
                    self.parent.add_data("Ce este un mouse pentru laptop sau desktop?", "Un mouse este un obiect care se conectează la laptop prin fir sau wireless, folosit pentru a mișca couser-ul de pe ecran")
                    self.parent.add_data("Care este diferența dintre guma de mestecat și guma de șters?", "Diferența dintre ele este chiar mare: cu guma de șters ștergi scrisul de creion de pe foaie, iar guma de mestecat o poți băga în gură, după care să o mesteci")
                    self.parent.add_data("Continuă seria cu încă 3 exemple: 1, 2, 3, ...", "Deci, numeri aici crescător, nu? Deci următoarele 3 exemple ar fi 4, 5 și 6.")

                    self.parent.add_data("Cum pot să-mi dezvolt gândirea critică în era dezinformării online?", "Dezvoltarea gândirii critice începe cu practicarea scepticismului sănătos și verificarea riguroasă a surselor de informație. Atunci când întâlnești o știre care îți provoacă o reacție emoțională puternică, este esențial să te oprești și să cauți sursa originală a datelor. Întreabă-te cine a scris articolul, ce interese ar putea avea și dacă informația este susținută de alte publicații de încredere. De asemenea, este util să consulți site-uri de fact-checking și să încerci să înțelegi perspectivele opuse pentru a identifica erorile de logică, cum ar fi atacul la persoană sau generalizarea pripită, evitând astfel bulele de filtrare create de algoritmi.")
                    self.parent.add_data("Explică conceptul de 'împletire cuantică' (quantum entanglement) pe înțelesul tuturor.", "Împletirea cuantică este un fenomen fascinant în care două sau mai multe particule devin conectate într-un mod în care starea uneia depinde instantaneu de starea celeilalte, indiferent de distanța uriașă care le desparte. Dacă măsurăm o proprietate a unei particule împletite, cum ar fi spinul, vom ști automat și instantaneu starea corespunzătoare a partenerului său. Albert Einstein a numit acest fenomen 'acțiune înfricoșătoare la distanță' deoarece pare să contrazică limita vitezei luminii. În realitate, nu se transmite informație clasică mai repede decât lumina, dar corelația cuantică rămâne unul dintre pilonii fundamentali pentru dezvoltarea calculatoarelor cuantice și a criptografiei securizate a viitorului.")
                    self.parent.add_data("Care este importanța rezilienței emoționale și cum poate fi ea cultivată?", "Reziliența emoțională reprezintă capacitatea psihică de a te adapta și de a-ți reveni după experiențe adverse, traume sau perioade de stres intens. Nu înseamnă că nu vei simți durere sau dificultate, ci că ai resursele interioare necesare pentru a merge mai departe fără a fi distrus de ele. Cultivarea rezilienței implică dezvoltarea unei rețele de suport social, menținerea unei perspective optimiste dar realiste și practicarea autocompasiunii. Este esențial să accepți că schimbarea face parte din viață și să te concentrezi pe aspectele pe care le poți controla, transformând provocările în oportunități de învățare și creștere personală.")
                    self.parent.add_data("Ce ne învață filosofia stoică despre gestionarea anxietății moderne?", "Filosofia stoică ne învață că rădăcina anxietății noastre stă adesea în încercarea de a controla lucruri care nu depind de noi, cum ar fi opiniile altora, trecutul sau evenimentele imprevizibile ale viitorului. Soluția oferită de stoici, precum Epictet sau Marcus Aurelius, este 'dihotomia controlului': trebuie să investim energie doar în propriile noastre gânduri, valori și acțiuni. Practicând 'premeditatio malorum' (vizualizarea unor posibile dificultăți) și acceptând că universul este într-o continuă schimbare, putem atinge o stare de liniște interioară numită ataraxie. Stoicismul nu înseamnă suprimarea emoțiilor, ci transformarea lor prin rațiune, astfel încât să nu mai fim sclavi ai circumstanțelor externe.")
                    self.parent.add_data("Cine a fost Albert Einstein și de ce teoria lui a revoluționat fizica?", "Albert Einstein a fost un fizician teoretician de origine germană, considerat unul dintre cei mai mari oameni de știință ai tuturor timpurilor. El a revoluționat înțelegerea noastră asupra universului prin Teoria Relativității. Relativitatea restrânsă a introdus conceptul că timpul și spațiul sunt legate într-un continuum numit spațiu-timp și că masa poate fi transformată în energie conform celebrei ecuații E=mc^2. Ulterior, Relativitatea generală a explicat gravitația nu ca pe o forță invizibilă, ci ca pe o curbură a spațiu-timpului cauzată de prezența masei. Această viziune a schimbat complet cosmologia, explicând fenomene precum orbita planetelor, găurile negre și expansiunea universului.")
                    self.parent.add_data("De ce este personajul Joker considerat unul dintre cei mai complecși antagoniști?", "Joker este un personaj fascinant deoarece reprezintă antiteza perfectă a ordinii și a logicii, fiind o personificare a nihilismului și a haosului pur. Spre deosebire de alți răufăcători care caută bogăție sau putere, Joker dorește adesea doar să demonstreze că moralitatea umană este o fațadă fragilă care se prăbușește în condiții de presiune extremă. Complexitatea sa provine din ambiguitatea originilor sale și din inteligența sa sclipitoare folosită în scopuri distructive. Interpretările sale, de la anarhistul filozofic al lui Heath Ledger la omul marginalizat și bolnav psihic al lui Joaquin Phoenix, au transformat personajul într-un simbol al eșecurilor sistemice ale societății și ale fragilității minții umane.")
                    self.parent.add_data("Ce definește stilul muzical Jazz și care sunt elementele sale cheie?", "Muzica Jazz este definită în primul rând prin libertatea de exprimare și improvizație, fiind un gen care a apărut la intersecția culturilor africane și europene în New Orleans. Elementele sale cheie includ swing-ul (un ritm specific care dă senzația de balans), utilizarea notelor 'blue' (care adaugă o tentă melancolică sau expresivă) și poliritmia. Într-o interpretare de jazz, muzicienii comunică între ei în timp real, oferind solo-uri spontane pe baza unei structuri armonice prestabilite. Această capacitate de a reinventa o piesă la fiecare interpretare face ca jazz-ul să fie considerat 'muzică clasică a Americii', influențând major genuri precum rock, pop și hip-hop prin complexitatea sa teoretică.")
                    self.parent.add_data("Care este impactul stilului Heavy Metal asupra culturii și fanilor săi?", "Heavy Metal-ul este mai mult decât un gen muzical caracterizat prin distorsiune, ritmuri rapide și voci puternice; este o subcultură globală care promovează un sentiment de comunitate și rezistență în fața normelor sociale convenționale. Deși a fost adesea criticat pentru agresivitatea sa aparentă, studiile arată că fanii genului găsesc în această muzică un debușeu terapeutic pentru furie și frustrare, obținând o stare de calm și apartenență. Temele abordate, de la mitologie și istorie la critici sociale și lupte interioare, oferă o profunzime intelectuală care creează o legătură extrem de loială între artiști și public, transformând concertele în experiențe ritualice de eliberare emoțională.")
                    self.parent.add_data("Cum funcționează economia circulară și de ce este necesară astăzi?", "Economia circulară este un model de producție și consum care implică partajarea, închirierea, reutilizarea, repararea, renovarea și reciclarea materialelor și produselor existente cât mai mult posibil. Spre deosebire de modelul liniar tradițional 'ia-fă-aruncă', economia circulară vizează extinderea ciclului de viață al produselor și reducerea la minimum a deșeurilor. Acest sistem este esențial în contextul actual deoarece resursele naturale sunt finite, iar presiunea asupra mediului cauzată de poluare și schimbările climatice necesită o transformare radicală. Prin implementarea designului circular, companiile pot crea produse mai durabile și ușor de reciclat, generând în același timp noi oportunități economice și protejând biodiversitatea planetei.")
                    self.parent.add_data("Care este rolul eticii în dezvoltarea sistemelor de inteligență artificială?", "Etica în inteligența artificială are rolul de a asigura că aceste tehnologii sunt dezvoltate și utilizate în moduri care respectă drepturile omului, echitatea și transparența. Deoarece algoritmii de IA sunt antrenați pe seturi de date care pot reflecta prejudecăți umane, există riscul ca aceștia să perpetueze sau să amplifice discriminarea în domenii precum angajarea sau justiția. O abordare etică presupune implementarea unor mecanisme de responsabilitate (accountability), protejarea vieții private a utilizatorilor și asigurarea faptului că deciziile luate de mașini pot fi explicate și verificate de oameni. Fără un cadru etic solid, avansul tehnologic ar putea duce la pierderea încrederii publice și la consecințe sociale imprevizibile sau dăunătoare.")
                    self.parent.add_data("Ce a fost Renașterea și cum a schimbat viziunea asupra lumii?", "Renașterea a fost o perioadă de efervescență culturală, artistică și științifică care a început în Italia în secolul al XIV-lea și s-a răspândit în întreaga Europă, marcând tranziția de la Evul Mediu la modernitate. Esența sa a fost umanismul, o mișcare care a mutat accentul de pe divinitate și dogmă pe potențialul, rațiunea și experiența umană. Artiști precum Leonardo da Vinci și Michelangelo au revoluționat artele plastice prin studierea anatomiei și a perspectivei, în timp ce gânditori precum Copernic au provocat viziunea geocentrică asupra universului. Renașterea a redescoperit valorile antichității clasice și a pus bazele metodei științifice moderne, încurajând curiozitatea intelectuală și explorarea geografică.")
                    self.parent.add_data("Cum pot fi gestionate eficient conflictele într-o echipă de lucru?", "Gestionarea eficientă a conflictelor începe cu recunoașterea faptului că dezacordurile sunt naturale și pot fi chiar benefice dacă sunt abordate constructiv. Primul pas este ascultarea activă a tuturor părților implicate, fără a judeca sau a întrerupe, pentru a înțelege nevoile și motivațiile din spatele pozițiilor adoptate. Este crucial să se atace problema, nu persoana, și să se caute puncte de interes comune în loc de divergențe. Utilizarea tehnicilor de comunicare non-violentă și medierea de către o persoană neutră pot ajuta la găsirea unor soluții de tip 'win-win'. Un conflict rezolvat corect poate duce la o mai bună coeziune a grupului, la idei inovatoare și la o atmosferă de lucru bazată pe încredere și respect reciproc.")
                    self.parent.add_data("Care este impactul încălzirii globale asupra ecosistemelor marine?", "Încălzirea globală are consecințe devastatoare asupra oceanelor, incluzând creșterea temperaturii apei, acidificarea și ridicarea nivelului mării. Absorbția excesului de dioxid de carbon din atmosferă face apele mai acide, ceea ce împiedică organismele precum coralii și moluștele să își formeze cochiliile sau scheletele de calcar. Albirea recifelor de corali duce la pierderea biodiversității, deoarece acestea adăpostesc un sfert din speciile marine. De asemenea, speciile migrează spre poli în căutarea apelor mai reci, perturbând lanțurile trofice locale și afectând comunitățile umane care depind de pescuit. Topirea ghețarilor nu doar ridică nivelul mării, dar schimbă și salinitatea apei, putând altera curenții oceanici care reglează clima globală.")
                    self.parent.add_data("Explicați importanța somnului pentru funcțiile cognitive și sănătatea fizică.", "Somnul nu este o stare pasivă, ci un proces biologic activ esențial pentru restabilirea funcțiilor fizice și mentale. În timpul somnului profund și al etapei REM, creierul procesează informațiile acumulate în timpul zilei, consolidează memoria pe termen lung și elimină toxinele metabolice acumulate. Lipsa cronică de somn afectează concentrarea, capacitatea de luare a deciziilor și reglarea emoțională, crescând riscul de depresie și anxietate. Din punct de vedere fizic, somnul insuficient este legat de un sistem imunitar slăbit, inflamație cronică, boli cardiovasculare și dezechilibre hormonale care pot duce la obezitate. Respectarea unui ritm circadian stabil este, prin urmare, unul dintre cei mai importanți piloni ai unei vieți lungi și sănătoase.")
                    self.parent.add_data("Cine este Elon Musk și cum a influențat el transportul modern și explorarea spațială?", "Elon Musk este un antreprenor vizionar și inginer auto-didact, cunoscut pentru fondarea sau conducerea unor companii de avangardă precum Tesla, SpaceX și Neuralink. Prin Tesla, el a forțat întreaga industrie auto să accelereze tranziția către vehicule electrice, demonstrând că acestea pot fi performante și dezirabile. Cu SpaceX, Musk a revoluționat explorarea spațială prin dezvoltarea rachetelor reutilizabile, reducând drastic costurile lansărilor pe orbită și redeschizând calea către colonizarea planetei Marte. Deși este o figură controversată din cauza stilului său de comunicare și a viziunilor sale radicale, impactul său asupra tehnologiei sustenabile și a ambițiilor interplanetare ale omenirii este incontestabil, schimbând paradigma în multiple sectoare industriale simultan.")
                    self.parent.add_data("Ce este muzica de tip Synthwave și ce elemente nostalgice folosește?", "Synthwave este un gen muzical electronic modern care se inspiră profund din cultura pop a anilor '80, utilizând sintetizatoare analogice pentru a crea o atmosferă retro-futuristă. Muzica evocă adesea coloanele sonore ale filmelor de acțiune și science-fiction din acea epocă, folosind ritmuri de tobe cu mult reverb și linii de bas pulsante. Estetica vizuală asociată, plină de culori neon (roz și albastru), mașini sport clasice și apusuri de soare digitale, completează experiența auditivă. Deși este un gen nou, Synthwave se bazează pe nostalgia pentru o versiune idealizată a trecutului, fiind popularizat recent prin seriale și jocuri care omagiază decada optzecistă, oferind ascultătorilor o evadare într-o lume digitală melancolică.")
                    self.parent.add_data("Care sunt principiile fundamentale ale democrației și de ce este ea fragilă?", "Democrația se bazează pe principii fundamentale precum suveranitatea poporului, statul de drept, separarea puterilor în stat și respectarea drepturilor și libertăților individuale. Într-o democrație funcțională, puterea este limitată prin legi, iar cetățenii participă la decizii prin vot liber și informat. Cu toate acestea, democrația este fragilă deoarece depinde de încrederea cetățenilor în instituții și de respectarea normelor nescrise ale dialogului civil. Ea poate fi subminată de polarizarea extremă, dezinformare, corupție sau apatie civică. Protejarea democrației necesită un angajament constant din partea societății pentru educație, transparență și protejarea minorităților, amintindu-ne că libertatea nu este un dat, ci un proces care trebuie apărat activ.")
                    self.parent.add_data("De ce este importantă biodiversitatea pentru stabilitatea ecosistemelor?", "Biodiversitatea reprezintă varietatea tuturor formelor de viață de pe Pământ și este esențială deoarece fiecare specie, oricât de mică, joacă un rol specific într-un ecosistem. Această diversitate funcționează ca o plasă de siguranță: cu cât un ecosistem are mai multe specii care îndeplinesc funcții similare (cum ar fi polenizarea sau descompunerea), cu atât este mai rezistent la șocuri precum bolile sau schimbările climatice. Pierderea unei singure specii poate declanșa un efect de domino, ducând la colapsul întregului sistem. Pentru oameni, biodiversitatea asigură resurse vitale: alimente, medicamente, aer curat și apă potabilă. Protejarea ei nu este doar un act moral, ci o necesitate pragmatică pentru supraviețuirea economiei și a sănătății umane.")
                    self.parent.add_data("Cum a influențat Marie Curie parcursul femeilor în știință?", "Marie Curie a fost o pionieră absolută, fiind prima femeie din Europa care a obținut un doctorat în științe și prima femeie care a câștigat un Premiu Nobel. Într-o epocă în care universitățile erau aproape exclusiv masculine, ea a demonstrat o tenacitate incredibilă, descoperind radioactivitatea și elementele radiu și poloniu. Prin munca sa, ea nu doar că a deschis drumul pentru tratamentele moderne împotriva cancerului, dar a și dărâmat barierele de gen din mediul academic. Succesul ei a servit drept inspirație pentru generații întregi de fete, demonstrând că geniul și rigoarea științifică nu au gen. Moștenirea sa continuă să fie un simbol al luptei pentru egalitate de șanse în cercetare și educație.")
                    self.parent.add_data("Ce este muzica Lo-fi și cum ajută la concentrare și relaxare?", "Muzica Lo-fi (Low Fidelity) este un gen care îmbrățișează imperfecțiunile tehnice, cum ar fi zgomotul de fond, sunetul de ploaie sau foșnetul discurilor de vinil, combinându-le cu ritmuri de hip-hop lente și relaxante. Acest stil muzical a devenit extrem de popular în mediul online ca fundal pentru studiu și muncă. Efectul său benefic asupra concentrării provine din natura sa previzibilă și non-intruzivă; lipsa versurilor și ritmul constant ajută creierul să intre în starea de 'flow', blocând zgomotele exterioare perturbatoare fără a solicita atenția activă a ascultătorului. De asemenea, atmosfera caldă și melancolică a muzicii Lo-fi reduce nivelul de cortizol, promovând o stare de calm necesară în perioadele de stres intelectual.")
                    self.parent.add_data("Explicați importanța alfabetizării financiare în viața de adult.", "Alfabetizarea financiară reprezintă capacitatea de a înțelege și de a utiliza eficient diverse abilități financiare, inclusiv gestionarea bugetului personal, investițiile și înțelegerea mecanismelor de creditare. Într-o lume economică tot mai complexă, lipsa acestor cunoștințe poate duce la datorii nesustenabile, stres și incapacitatea de a economisi pentru viitor. O persoană educată financiar știe să facă diferența între active (lucruri care îți aduc bani) și pasive (lucruri care îți consumă bani), înțelege puterea dobânzii compuse și riscurile inflației. Această competență oferă nu doar securitate materială, ci și libertatea de a lua decizii informate care să permită atingerea obiectivelor pe termen lung, cum ar fi achiziționarea unei locuințe sau asigurarea unei pensii confortabile.")
                    self.parent.add_data("Cum funcționează memoria de scurtă durată față de cea de lungă durată?", "Memoria de scurtă durată, numită adesea memorie de lucru, este capacitatea creierului de a reține și manipula o cantitate mică de informație pentru o perioadă foarte scurtă, de obicei între 15 și 30 de secunde. Este esențială pentru sarcini imediate, cum ar fi reținerea unui număr de telefon până îl notezi. Memoria de lungă durată, pe de altă parte, este un sistem de stocare aproape nelimitat unde informațiile sunt păstrate pentru zile, ani sau chiar întreaga viață. Trecerea informațiilor de la una la alta se face prin procesul de consolidare, care necesită atenție, repetiție și, foarte important, somn. În timp ce memoria de lucru este fragilă și ușor de perturbat, memoria de lungă durată este stocată prin schimbări structurale la nivelul sinapselor neuronale, formând rețele complexe de asocieri.")
                    self.parent.add_data("Care sunt avantajele și dezavantajele lucrului de acasă (remote work)?", "Lucrul de acasă oferă avantaje majore, cum ar fi flexibilitatea programului, eliminarea timpului pierdut în trafic și economii financiare legate de transport. Această autonomie poate crește satisfacția angajatului și poate îmbunătăți echilibrul dintre viața profesională și cea personală. Totuși, există și dezavantaje semnificative, cum ar fi dificultatea de a separa clar timpul de muncă de cel de odihnă, riscul de izolare socială și scăderea calității comunicării spontane între colegi. Pentru mulți, lipsa unui spațiu dedicat muncii poate duce la scăderea productivității sau la epuizare (burnout). Succesul muncii remote depinde de disciplina personală, de utilizarea instrumentelor digitale de colaborare și de efortul conștient al companiilor de a menține cultura organizațională și conexiunea umană.")
                    self.parent.add_data("Cine a fost Audrey Hepburn și ce a lăsat în urmă dincolo de cariera de actriță?", "Audrey Hepburn a fost o figură legendară a cinematografiei mondiale, premiată cu Oscar pentru rolul din 'Vacanță la Roma', dar moștenirea ei cea mai profundă este cea umanitară. După ce s-a retras din lumina reflectoarelor, ea și-a dedicat restul vieții organizației UNICEF, fiind numită Ambasador al Bunăvoinței. Marcată de propria experiență din timpul foametei din al Doilea Război Mondial, Audrey a călătorit în zonele cele mai sărace din Africa, America de Sud și Asia pentru a atrage atenția lumii asupra copiilor malnutriți și a nevoii de educație. Ea a transformat statutul de celebritate într-o platformă pentru compasiune, demonstrând că eleganța adevărată provine din bunătate și dedicare față de cei suferinzi, rămânând un simbol al altruismului global.")
                    self.parent.add_data("Care este semnificația personajului Daenerys Targaryen în contextul puterii?", "Daenerys Targaryen din 'Game of Thrones' servește drept un studiu de caz complex despre ambiție, putere și corupție morală. Evoluția ei de la o victimă a circumstanțelor la o cuceritoare absolută explorează ideea periculoasă că 'scopul scuză mijloacele'. Deși pornește cu intenția nobilă de a elibera sclavii și de a distruge tirania, Daenerys ajunge să creadă atât de puternic în propriul destin mesianic încât orice opoziție devine, în ochii ei, o formă de rău ce trebuie eliminată. Povestea ei avertizează asupra riscului ca un lider care se consideră infailibil să devină exact monstrul pe care a jurat să îl distrugă, ridicând întrebări fundamentale despre natura autorității și prețul libertății.")
                    self.parent.add_data("Ce definește muzica Clasică și de ce este considerată atemporală?", "Muzica clasică este o tradiție artistică vastă care se întinde pe mai multe secole, atingând culmi de complexitate în perioadele Barocă, Clasică și Romantică. Ceea ce o face atemporală este capacitatea sa de a exprima gama completă de emoții umane — de la agonie la extaz — fără a se baza pe limbaj, ci pe structură, armonie și textură sonoră. Compozițiile lui Bach, Mozart sau Beethoven sunt construite pe principii matematice și estetice riguroase care continuă să rezoneze cu ascultătorii moderni. Dincolo de valoarea artistică, muzica clasică este recunoscută pentru beneficiile sale cognitive, îmbunătățind concentrarea și oferind un spațiu de contemplare profundă într-o lume dominată de consumul rapid și superficial de informație.")
                    self.parent.add_data("Cum pot fi combatute schimbările climatice la nivel individual?", "Deși soluțiile la scară largă depind de guverne și corporații, acțiunile individuale au un impact cumulativ semnificativ și pot influența piața. Reducerea consumului de carne și lactate, alegerea mijloacelor de transport în comun sau a bicicletei și optimizarea eficienței energetice a locuinței sunt pași concreți pentru scăderea amprentei de carbon. De asemenea, practicarea unui consum responsabil — cumpărarea de produse durabile în locul celor de unică folosință și susținerea afacerilor locale sustenabile — pune presiune pe lanțurile de aprovizionare globale. Dincolo de stilul de viață, implicarea civică și educarea celor din jur sunt esențiale pentru a crea o masă critică de oameni care să ceară politici de protecție a mediului mai stricte și mai rapide.")
                    self.parent.add_data("De ce este importantă explorarea spațială pentru viitorul omenirii?", "Explorarea spațială nu este doar o manifestare a curiozității umane, ci o necesitate strategică pentru supraviețuirea și progresul speciei noastre. Pe termen scurt, tehnologiile dezvoltate pentru misiuni spațiale au dus la inovații majore pe Pământ, de la purificarea apei și panouri solare mai eficiente, până la tehnologii medicale avansate. Pe termen lung, stabilirea unor colonii pe alte planete, cum ar fi Marte, servește drept o asigurare împotriva unor posibile catastrofe globale pe Terra. Mai mult, extragerea resurselor din asteroizi ar putea rezolva problema penuriei de metale rare, protejând în același timp mediul terestru de mineritul invaziv. Spațiul rămâne frontiera finală care ne forțează să cooperăm la nivel global și să ne depășim limitele tehnologice.")
                    self.parent.add_data("Cum ne influențează 'bula de filtru' (filter bubble) opiniile pe rețelele sociale?", "Bula de filtru apare atunci când algoritmii rețelelor sociale ne oferă doar informații și opinii care sunt în concordanță cu preferințele și convingerile noastre anterioare, bazându-se pe interacțiunile noastre online. Acest lucru creează un mediu în care propriile idei ne sunt confirmate constant, în timp ce perspectivele contrare sunt eliminate din câmpul nostru vizual. Pericolul major este polarizarea extremă a societății și dispariția dialogului constructiv, deoarece începem să credem că punctul nostru de vedere este singurul valid. Ieșirea din această bulă necesită un efort conștient de a căuta surse de știri diverse, de a urmări persoane cu opinii diferite și de a interacționa cu conținut care ne provoacă propriile certitudini, dezvoltând astfel o gândire mai nuanțată.")
                    self.parent.add_data("Care este istoria și semnificația Marelui Zid Chinezesc?", "Marele Zid Chinezesc este una dintre cele mai grandioase realizări inginerești ale antichității, fiind construit de-a lungul a peste două mii de ani de către mai multe dinastii pentru a proteja frontierele de invaziile nomade din nord. Dincolo de scopul său defensiv, zidul a servit ca instrument de control al comerțului de-a lungul Drumului Mătăsii și ca sistem de comunicații rapid prin turnurile de semnalizare cu fum și foc. Construcția sa a implicat un efort uman imens, devenind un simbol al perseverenței, dar și al izolării. Astăzi, Marele Zid este un monument al identității naționale chineze și un obiectiv cultural mondial, amintindu-ne de capacitatea umană de a modifica peisajul pentru a asigura securitatea și continuitatea unei civilizații.")
                    self.parent.add_data("Ce este 'Paradoxul lui Fermi' și de ce ne pune pe gânduri?", "Paradoxul lui Fermi reprezintă contradicția dintre probabilitatea mare de existență a civilizațiilor extraterestre în universul nostru vast și lipsa oricăror dovezi sau contacte cu acestea. Având în vedere miliardele de stele similare Soarelui și miliardele de planete potențial locuibile, logic ar fi ca universul să abunde de viață inteligentă. Explicațiile posibile includ ipoteza 'Marelui Filtru' (o barieră evolutivă greu de depășit), ideea că suntem printre primele civilizații care au apărut sau posibilitatea că civilizațiile avansate aleg să nu comunice. Acest paradox ne forțează să reflectăm asupra propriei noastre fragilități și asupra unicității vieții pe Pământ, ridicând întrebări fundamentale despre locul nostru în cosmos.")
                    self.parent.add_data("De ce este importantă metoda Socratică în educația modernă?", "Metoda Socratică este o formă de dialog cooperativ bazată pe întrebări și răspunsuri menite să stimuleze gândirea critică și să scoată la iveală idei și presupuneri implicite. În loc să ofere soluții de-a gata, profesorul pune întrebări care îl conduc pe elev să descopere singur contradicțiile din propria gândire și să ajungă la o înțelegere mai profundă a subiectului. Această metodă este crucială în educația modernă deoarece mută accentul de pe memorarea mecanică pe procesul de analiză și sinteză. Ea dezvoltă curiozitatea intelectuală, modestia (prin recunoașterea limitelor propriei cunoașteri) și abilitățile de argumentare logică, pregătind indivizii să navigheze într-o lume plină de informații ambigue.")
                    self.parent.add_data("Cum a transformat Revoluția Industrială societatea umană?", "Revoluția Industrială, începută în secolul al XVIII-lea în Marea Britanie, a marcat trecerea de la producția manuală la cea mecanizată, declanșând o transformare radicală a tuturor aspectelor vieții umane. Aceasta a dus la o creștere fără precedent a productivității și a nivelului de trai pentru mulți, dar a provocat și o urbanizare rapidă și adesea haotică. Oamenii s-au mutat de la sate în orașe pentru a munci în fabrici, ceea ce a schimbat structura familiei și a dat naștere clasei muncitoare moderne. Pe lângă progresul tehnologic, revoluția a adus provocări sociale majore, cum ar fi condițiile de muncă grele și poluarea mediului, punând bazele sistemelor economice capitaliste și ale mișcărilor pentru drepturile muncitorilor.")
                    self.parent.add_data("Care este legătura dintre nutriție și sănătatea mentală?", "Cercetările recente din domeniul psihiatriei nutriționale demonstrează o legătură strânsă între calitatea dietei și sănătatea mentală, sugerând că alimentele pe care le consumăm influențează direct funcționarea creierului și starea de spirit. O dietă bogată în nutrienți, cum ar fi acizii grași omega-3, vitaminele din grupul B și antioxidanții, susține neuroplasticitatea și reduce inflamația la nivel cerebral. De asemenea, microbiomul intestinal — 'al doilea creier' — comunică constant cu sistemul nervos central prin axa intestin-creier, producând neurotransmițători esențiali precum serotonina. Consumul excesiv de zahăr și alimente ultra-procesate este corelat cu un risc crescut de depresie și anxietate, subliniind faptul că o alimentație echilibrată este fundamentală nu doar pentru corp, ci și pentru minte.")
                    self.parent.add_data("Ce este programarea orientată pe obiecte (OOP) și de ce este atât de utilizată?", "Programarea Orientată pe Obiecte (OOP) este o paradigmă de programare care organizează designul software-ului în jurul datelor, sau 'obiectelor', mai degrabă decât în jurul funcțiilor și logicii. Un obiect poate fi definit ca un câmp de date care are atribute și comportamente unice. Cele patru principii de bază — încapsularea, moștenirea, polimorfismul și abstracția — permit dezvoltatorilor să scrie cod modular, reutilizabil și ușor de întreținut. Această abordare este extrem de utilă în proiectele complexe, deoarece permite echipelor mari să lucreze simultan pe module diferite și să modeleze problemele din lumea reală într-un mod intuitiv, reducând erorile și accelerând procesul de dezvoltare software.")
                    self.parent.add_data("Cine a fost Sherlock Holmes și cum a influențat el criminalistica?", "Sherlock Holmes, celebrul detectiv creat de Sir Arthur Conan Doyle, este un personaj literar care a depășit granițele ficțiunii pentru a deveni un model de gândire logică și observație științifică. Holmes a popularizat utilizarea metodelor de investigație bazate pe dovezi materiale, cum ar fi analiza amprentelor, a urmelor de pași și a reziduurilor de substanțe, cu mult înainte ca acestea să devină practici standard în poliția reală. Abordarea sa analitică, bazată pe deducție și pe principiul că 'după ce ai eliminat imposibilul, ceea ce rămâne, oricât de improbabil, trebuie să fie adevărul', a inspirat mii de detectivi reali și a pus bazele criminalisticii moderne, transformând investigarea crimelor dintr-o intuiție în o disciplină riguroasă.")
                    self.parent.add_data("Care sunt cauzele și consecințele colapsului civilizației Maiașe?", "Colapsul civilizației Maiașe din perioada clasică nu a fost rezultatul unui singur eveniment catastrofal, ci mai degrabă o succesiune de crize interconectate care au dus la abandonarea marilor centre urbane. Printre cauzele principale se numără degradarea mediului din cauza defrișărilor excesive, secete prelungite care au distrus agricultura și războaie endemice între orașele-stat pentru resurse limitate. Această presiune a dus la pierderea încrederii în liderii religioși și politici, provocând migrații masive și colapsul sistemelor administrative complexe. Consecința a fost fragmentarea societății și revenirea la forme de organizare mai simple, demonstrând fragilitatea societăților avansate în fața dezechilibrelor ecologice și a conflictelor interne.")
                    self.parent.add_data("Explicați conceptul de 'mindfulness' și beneficiile sale demonstrate științific.", "Mindfulness, sau starea de prezență conștientă, reprezintă practica de a-ți concentra atenția asupra momentului prezent într-un mod non-critic și acceptant. Deși își are originile în tradițiile meditative orientale, mindfulness a fost adoptat pe scară largă în psihologia modernă datorită beneficiilor sale demonstrate prin neuroimagistică. Practica regulată ajută la reducerea dimensiunii amigdalei (centrul fricii din creier) și la creșterea densității materiei cenușii în zonele responsabile pentru învățare și reglare emoțională. Printre beneficiile sale se numără scăderea stresului cronic, îmbunătățirea concentrării, gestionarea mai eficientă a durerii și creșterea rezilienței în fața provocărilor cotidiene, fiind un instrument valoros pentru menținerea echilibrului psihic în era digitală.")
                    self.parent.add_data("Ce sunt criptomonedele și cum ar putea ele schimba sistemul financiar global?", "Criptomonedele sunt active digitale care utilizează criptografia pentru a securiza tranzacțiile și pentru a controla crearea de noi unități, funcționând de obicei pe o rețea descentralizată numită blockchain. Spre deosebire de monedele tradiționale emise de bănci centrale, criptomonede precum Bitcoin oferă promisiunea unor tranzacții transparente, rapide și fără intermediari, indiferent de granițe. Impactul lor potențial asupra sistemului financiar este major: ar putea reduce costurile tranzacționale globale, ar oferi acces la servicii financiare persoanelor care nu au conturi bancare și ar putea servi ca o rezervă de valoare protejată de inflație în economiile instabile. Totuși, volatilitatea mare, riscurile de securitate și impactul ecologic al minării rămân provocări esențiale care trebuie rezolvate înainte de o adopție pe scară largă.")
                    self.parent.add_data("Care este importanța egalității de șanse în societatea modernă?", "Egalitatea de șanse reprezintă principiul conform căruia toți indivizii ar trebui să aibă același acces la resurse, educație și oportunități de angajare, indiferent de gen, rasă, origine socială sau dizabilități. Într-o societate modernă, acest concept nu este doar un deziderat moral, ci și un motor economic: o societate care valorifică talentele tuturor membrilor săi este mai inovatoare, mai productivă și mai stabilă. Reducerea barierelor sistemice ajută la combaterea sărăciei generaționale și la creșterea coeziunii sociale. Egalitatea de șanse nu înseamnă uniformitate, ci asigurarea faptului că punctul de plecare al unei persoane nu îi limitează în mod nedrept potențialul de realizare, permițând meritocrației să funcționeze în mod real.")
                    self.parent.add_data("Poți să-mi explici fenomenul încălzirii globale și care sunt principalele cauze identificate de oamenii de știință?", "Încălzirea globală reprezintă creșterea treptată a temperaturilor medii în atmosfera Pământului și în oceane, un proces accelerat de activitățile umane care emit gaze cu efect de seră, precum dioxidul de carbon și metanul, rezultate în principal din arderea combustibililor fosili și defrișările masive.")

                    self.parent.add_data("Care sunt beneficiile cititului constant pentru dezvoltarea cognitivă și emoțională a unei persoane?", "Cititul constant îmbunătățește vocabularul, capacitatea de concentrare și gândirea critică, oferind în același timp o modalitate de a explora perspective noi și de a dezvolta empatia prin înțelegerea experiențelor personajelor, reducând totodată nivelul de stres zilnic.")

                    self.parent.add_data("Cum funcționează procesul de fotosinteză și de ce este acesta vital pentru viața pe Pământ?", "Fotosinteza este procesul prin care plantele verzi, algele și unele bacterii transformă energia luminoasă a soarelui în energie chimică, utilizând apă și dioxid de carbon pentru a produce glucoză și oxigen, acesta din urmă fiind esențial pentru respirația majorității organismelor vii.")

                    self.parent.add_data("Ce sfaturi ai pentru cineva care dorește să înceapă o grădină de legume în propria curte?", "Pentru a începe o grădină de legume, este important să alegi un loc cu expunere solară de cel puțin șase ore pe zi, să pregătești solul cu îngrășământ organic, să planifici rotația culturilor pentru a menține sănătatea pământului și să asiguri un sistem de irigare constant și eficient.")

                    self.parent.add_data("Poți să descrii importanța protejării biodiversității în ecosistemele fragile ale planetei noastre?", "Protejarea biodiversității este crucială deoarece fiecare specie joacă un rol specific în menținerea echilibrului ecosistemului, oferind servicii esențiale precum polenizarea plantelor, reglarea climei, purificarea apei și furnizarea de resurse medicinale pe care omenirea se bazează.")

                    self.parent.add_data("Care sunt principalele diferențe între stilul de viață nomad și cel sedentar din punct de vedere istoric?", "Stilul de viață nomad presupune deplasarea constantă în căutarea resurselor de hrană și pășuni, în timp ce stilul sedentar a apărut odată cu revoluția agricolă, permițând oamenilor să construiască așezări permanente, să dezvolte structuri sociale complexe și să acumuleze bunuri materiale.")

                    self.parent.add_data("Cum se poate gestiona eficient anxietatea înaintea unei prezentări publice importante?", "Gestionarea anxietății se poate face prin pregătirea riguroasă a materialului, exersarea tehnicilor de respirație profundă pentru calmarea sistemului nervos, vizualizarea succesului și acceptarea faptului că emoțiile sunt o reacție naturală care poate fi canalizată în energie pozitivă pe scenă.")

                    self.parent.add_data("Explică importanța explorării spațiale pentru progresul tehnologic și științific al umanității.", "Explorarea spațială a condus la invenții revoluționare care sunt folosite astăzi pe Pământ, cum ar fi sistemele GPS, tehnologia de purificare a apei și senzorii de imagine pentru camerele foto, stimulând în același timp curiozitatea umană și înțelegerea originilor universului nostru.")

                    self.parent.add_data("Ce este economia circulară și cum poate aceasta să ajute la reducerea poluării la nivel global?", "Economia circulară este un model de producție și consum care implică partajarea, închirierea, reutilizarea, repararea și reciclarea materialelor și produselor existente cât mai mult posibil, cu scopul de a prelungi ciclul de viață al produselor și de a reduce la minimum deșeurile generate.")

                    self.parent.add_data("Cum influențează consumul excesiv de zahăr sănătatea pe termen lung a organismului uman?", "Consumul excesiv de zahăr este asociat cu un risc ridicat de obezitate, diabet de tip 2, boli cardiovasculare și carii dentare, deoarece provoacă fluctuații bruște ale insulinei în sânge și poate duce la inflamații cronice în diverse organe ale corpului.")

                    self.parent.add_data("Care sunt trăsăturile definitorii ale stilului arhitectural gotic întâlnit în catedralele europene?", "Arhitectura gotică se remarcă prin utilizarea arcurilor frânte, a bolților pe nervuri și a contraforturilor exterioare, elemente care au permis construirea unor clădiri foarte înalte cu ferestre uriașe decorate cu vitralii colorate ce inundă interiorul cu lumină.")

                    self.parent.add_data("Descrie procesul prin care se formează un curcubeu pe cer după o ploaie de vară.", "Curcubeul apare atunci când lumina soarelui este refractată, reflectată și dispersată în interiorul picăturilor de apă din atmosferă, separând lumina albă în spectrul său de culori vizibile, formând astfel un arc multicolor situat opus față de poziția soarelui.")

                    self.parent.add_data("De ce este considerată limba română o limbă romantică și care sunt principalele ei asemănări cu latina?", "Limba română este o limbă romanică deoarece s-a format din latina vulgară vorbită în provincia Dacia; ea păstrează o structură gramaticală similară cu latina, inclusiv sistemul de declinări ale substantivelor, și un lexic de bază compus în mare parte din cuvinte de origine latină.")

                    self.parent.add_data("Care sunt principalele provocări ale utilizării energiei regenerabile la scară largă în prezent?", "Principalele provocări includ intermitența surselor precum vântul și soarele, necesitatea dezvoltării unor tehnologii avansate de stocare a energiei în baterii de mare capacitate și costurile ridicate pentru modernizarea infrastructurii rețelelor electrice actuale.")

                    self.parent.add_data("Cum poate învățarea unei limbi străine să modifice structura și funcționarea creierului uman?", "Învățarea unei limbi străine crește densitatea materiei cenușii în zonele responsabile pentru memorie și atenție, îmbunătățește neuroplasticitatea și poate întârzia apariția simptomelor unor boli neurodegenerative precum Alzheimer prin menținerea creierului activ și solicitat.")

                    self.parent.add_data("Ce este dezinformarea digitală și cum ne putem proteja de știrile false de pe rețelele sociale?", "Dezinformarea digitală reprezintă distribuirea intenționată de informații false pentru a induce în eroare; ne putem proteja prin verificarea surselor din mai multe locuri oficiale, analizarea autorului articolului și dezvoltarea unui simț critic față de titlurile senzaționaliste.")

                    self.parent.add_data("Explică importanța somnului REM pentru procesarea emoțiilor și consolidarea memoriei.", "Somnul REM (Rapid Eye Movement) este etapa în care apar cele mai intense vise și este esențial pentru sănătatea mentală, deoarece în acest timp creierul procesează experiențele emoționale de peste zi și consolidează amintirile noi, facilitând învățarea pe termen lung.")

                    self.parent.add_data("Care sunt etapele principale ale realizării unui film, de la idee până la lansarea pe marile ecrane?", "Producția unui film cuprinde pre-producția (scrierea scenariului și castingul), producția propriu-zisă (filmările pe platou), post-producția (montajul, efectele speciale și sunetul) și, în final, distribuția și promovarea către publicul larg.")

                    self.parent.add_data("Cum a influențat Revoluția Industrială structura familiilor și a comunităților urbane?", "Revoluția Industrială a dus la migrarea masivă a oamenilor de la sate la orașe în căutare de muncă în fabrici, schimbând structura familiei extinse în familie nucleară și ducând la apariția clasei muncitoare urbane și la dezvoltarea rapidă, dar adesea haotică, a marilor orașe.")

                    self.parent.add_data("Care este rolul unui ecosistem marin în reglarea nivelului de oxigen de pe întreaga planetă?", "Ecosistemele marine, în special fitoplanctonul din oceane, produc peste 50% din oxigenul planetei prin fotosinteză și absorb cantități uriașe de dioxid de carbon, jucând astfel un rol vital în atenuarea schimbărilor climatice și susținerea vieții pe Terra.")

                    self.parent.add_data("Ce înseamnă conceptul de 'mindfulness' și cum poate fi practicat în viața de zi cu zi?", "Mindfulness reprezintă starea de prezență conștientă și focalizarea atenției asupra momentului actual fără a judeca; poate fi practicat prin respirație conștientă, observarea senzațiilor corporale în timpul activităților obișnuite sau prin meditație dedicată pentru reducerea stresului.")

                    self.parent.add_data("Descrie modul în care vulcanii influențează fertilitatea solului din regiunile înconjurătoare.", "Deși erupțiile vulcanice pot fi distructive, cenușa și lava descompusă în timp eliberează nutrienți esențiali precum potasiul și fosforul în pământ, creând unele dintre cele mai fertile soluri agricole din lume, capabile să susțină culturi bogate și diverse.")

                    self.parent.add_data("Care sunt avantajele și dezavantajele muncii la distanță pentru angajați și angajatori?", "Avantajele includ flexibilitatea programului și eliminarea timpului pierdut în trafic, în timp ce dezavantajele se referă la dificultatea separării vieții profesionale de cea personală, posibila izolare socială a angajatului și provocările în menținerea culturii organizaționale pentru angajatori.")

                    self.parent.add_data("Cum funcționează sistemul de imunizare prin vaccinare și cum ajută acesta la protejarea populației?", "Vaccinarea funcționează prin introducerea unei forme inofensive a unui agent patogen în corp pentru a antrena sistemul imunitar să îl recunoască și să producă anticorpi, creând astfel o memorie imunologică ce previne îmbolnăvirea gravă în cazul unei expuneri viitoare.")

                    self.parent.add_data("Care este impactul microplasticelor asupra lanțului trofic și a sănătății umane?", "Microplasticele sunt ingerate de organisme mici marine, ajungând prin consum în pești și ulterior în oameni, transportând substanțe chimice toxice care pot perturba sistemul endocrin și pot cauza inflamații, reprezentând o problemă majoră de mediu și sănătate publică.")

                    self.parent.add_data("Explică conceptul de 'an lumină' și cum este acesta utilizat în astronomie pentru a măsura distanțele.", "Un an lumină este distanța pe care lumina o parcurge într-un an în vid, adică aproximativ 9,5 trilioane de kilometri; este o unitate de măsură esențială în astronomie deoarece distanțele dintre stele și galaxii sunt atât de mari încât kilometrii obișnuiți ar fi imposibil de gestionat.")

                    self.parent.add_data("Care sunt cauzele apariției deșertificării și ce măsuri pot fi luate pentru a stopa acest proces?", "Deșertificarea este cauzată de schimbările climatice, suprapășunat, defrișări și practici agricole inadecvate; măsurile de stopare includ reîmpădurirea zonelor afectate, gestionarea durabilă a resurselor de apă și utilizarea unor tehnici agricole care protejează stratul superior al solului.")

                    self.parent.add_data("Cum influențează muzica clasică starea psihică și performanța intelectuală a studenților?", "Muzica clasică, în special anumite compoziții baroce sau clasice, poate reduce tensiunea arterială și nivelul de cortizol, inducând o stare de relaxare alertă care favorizează memorarea, concentrarea și procesarea informațiilor complexe în timpul studiului.")

                    self.parent.add_data("Ce este inteligența emoțională și de ce este considerată la fel de importantă ca inteligența cognitivă?", "Inteligența emoțională (EQ) reprezintă capacitatea de a recunoaște, înțelege și gestiona propriile emoții, precum și de a empatiza cu ceilalți; este vitală pentru succesul profesional și personal deoarece facilitează comunicarea, rezolvarea conflictelor și leadership-ul eficient.")

                    self.parent.add_data("Descrie rolul albinelor în producția globală de alimente și riscurile dispariției lor.", "Albinele sunt principalii polenizatori ai multor culturi agricole de care depinde alimentația umană, precum fructele și legumele; dispariția lor din cauza pesticidelor și pierderii habitatului ar duce la o scădere drastică a producției alimentare și la un dezechilibru major în biodiversitate.")

                    self.parent.add_data("Cum funcționează un motor electric comparativ cu un motor cu ardere internă?", "Un motor electric transformă energia electrică direct în mișcare prin intermediul câmpurilor magnetice, fiind mult mai eficient și silențios, în timp ce un motor cu ardere internă produce energie prin explozii controlate de combustibil, având mai multe piese în mișcare și emițând gaze poluante.")

                    self.parent.add_data("Care sunt beneficiile dietei mediteraneene asupra longevității și sănătății inimii?", "Dieta mediteraneeană, bogată în fructe, legume, cereale integrale, pește și ulei de măsline, este celebră pentru reducerea riscului de boli cardiace și inflamații, oferind un aport ridicat de antioxidanți și grăsimi sănătoase care contribuie la o viață lungă și sănătoasă.")

                    self.parent.add_data("Explică ce este un activ financiar de tip 'acțiune' și cum pot investitorii să câștige bani din acestea.", "O acțiune reprezintă o unitate de proprietate într-o companie; investitorii pot câștiga bani fie prin creșterea prețului acțiunii în timp (aprecierea capitalului), fie prin primirea unei părți din profitul companiei sub formă de dividende periodice.")

                    self.parent.add_data("Care este importanța stratului de ozon pentru viața de pe Pământ și cum a fost acesta afectat de substanțele CFC?", "Stratul de ozon acționează ca un scut care absoarbe majoritatea radiațiilor ultraviolete nocive ale soarelui; substanțele chimice de tip CFC folosite în trecut în spray-uri și frigidere au subțiat acest strat, crescând riscul de cancer de piele și afectând ecosistemele marine.")

                    self.parent.add_data("Cum se formează stalactitele și stalagmitele în peșterile calcaroase de-a lungul mileniilor?", "Aceste formațiuni se creează prin depunerea lentă a carbonatului de calciu din picăturile de apă care se infiltrează prin tavanul peșterii; stalactitele cresc de sus în jos, iar stalagmitele se formează pe podea din apa care cade, întâlnindu-se uneori pentru a forma coloane impresionante.")

                    self.parent.add_data("Ce este alfabetizarea digitală și de ce este esențială pentru cetățenii secolului XXI?", "Alfabetizarea digitală reprezintă capacitatea de a găsi, evalua și comunica informații prin diverse platforme digitale; este esențială deoarece majoritatea serviciilor publice, locurilor de muncă și modalităților de comunicare modernă depind acum de utilizarea corectă și sigură a tehnologiei.")

                    self.parent.add_data("Care este impactul fast-fashion-ului asupra mediului înconjurător și ce putem face pentru a fi mai sustenabili?", "Industria fast-fashion produce cantități enorme de deșeuri textile și utilizează resurse uriașe de apă, poluând solul cu vopsele toxice; putem fi mai sustenabili prin cumpărarea de haine de calitate mai bună, susținerea brandurilor etice sau prin achiziționarea de articole second-hand.")

                    self.parent.add_data("Descrie modul în care se produce un cutremur și cum se măsoară intensitatea acestuia.", "Cutremurele se produc prin eliberarea bruscă de energie în scoarța terestră, de obicei la contactul dintre plăcile tectonice; intensitatea lor se măsoară cu ajutorul seismografelor, folosind scara Richter pentru magnitudine sau scara Mercalli pentru a evalua efectele vizibile asupra clădirilor.")

                    self.parent.add_data("Cum a schimbat inventarea tiparului de către Gutenberg accesul la cunoaștere în Europa?", "Inventarea tiparului a permis producerea rapidă și ieftină a cărților, ducând la alfabetizarea masivă a populației, la răspândirea ideilor noi în timpul Renașterii și Reformei și la democratizarea informației care înainte era accesibilă doar elitelor și clerului.")

                    self.parent.add_data("Ce sunt probioticele și ce rol joacă ele în menținerea sănătății sistemului digestiv?", "Probioticele sunt microorganisme vii, adesea numite 'bacterii bune', care ajută la menținerea echilibrului florei intestinale, îmbunătățesc digestia, întăresc sistemul imunitar și pot preveni diverse afecțiuni gastrointestinale cauzate de stres sau alimentație dezechilibrată.")

                    self.parent.add_data("Care este rolul ONU (Organizația Națiunilor Unite) în menținerea păcii la nivel mondial?", "ONU are misiunea de a preveni conflictele armate prin diplomație, de a oferi asistență umanitară în zone de criză, de a promova drepturile omului și de a facilita cooperarea internațională pentru rezolvarea problemelor economice și sociale globale.")

                    self.parent.add_data("Explicați importanța pădurilor tropicale amazoniene în contextul stabilității climatice globale.", "Pădurea amazoniană, supranumită 'plămânul planetei', stochează miliarde de tone de carbon și produce o cantitate semnificativă de umiditate care influențează regimul precipitațiilor la nivel global; distrugerea ei ar accelera dramatic încălzirea globală și ar distruge mii de specii unice.")

                    self.parent.add_data("Cum influențează rețelele de socializare stima de sine a adolescenților în era digitală?", "Rețelele de socializare pot afecta negativ stima de sine prin comparația constantă cu imagini idealizate ale altora și prin nevoia de validare externă (like-uri), însă pot oferi și spații de exprimare creativă și comunități de suport dacă sunt utilizate cu moderație și discernământ.")

                    self.parent.add_data("Ce este terapia prin artă și cum poate aceasta ajuta la vindecarea unor traume psihice?", "Terapia prin artă folosește procesul creativ (pictură, sculptură, desen) ca mijloc de comunicare pentru a ajuta oamenii să exprime sentimente greu de pus în cuvinte, facilitând explorarea emoțiilor interioare, reducerea anxietății și procesarea experiențelor traumatizante într-un mediu sigur.")

                    self.parent.add_data("Descrieți procesul de fabricare a hârtiei și impactul acestuia asupra resurselor forestiere.", "Hârtia se fabrică prin prelucrarea fibrelor de celuloză din lemn sau materiale reciclate în pastă, care este apoi întinsă și uscată; cererea mare de hârtie pune presiune pe păduri, motiv pentru care reciclarea și utilizarea lemnului din surse certificate sustenabil sunt extrem de importante.")

                    self.parent.add_data("Care sunt beneficiile utilizării vehiculelor cu hidrogen față de cele electrice clasice?", "Vehiculele cu hidrogen se alimentează mult mai rapid (în câteva minute) și oferă o autonomie mai mare, eliminând necesitatea bateriilor grele de litiu; totuși, infrastructura de alimentare este încă limitată și producția de hidrogen verde necesită multă energie.")

                    self.parent.add_data("Cum afectează poluarea fonică viața animalelor sălbatice din apropierea zonelor urbane?", "Poluarea fonică poate masca sunetele pe care animalele le folosesc pentru comunicare, orientare sau vânătoare, forțându-le să își părăsească habitatele naturale, schimbându-le comportamentul de împerechere și crescându-le nivelul de stres fiziologic.")

                    self.parent.add_data("Ce reprezintă conceptul de 'oraș inteligent' (Smart City) și cum îmbunătățește acesta viața locuitorilor?", "Un oraș inteligent folosește tehnologia IoT (Internet of Things) și datele pentru a optimiza serviciile urbane, cum ar fi gestionarea traficului în timp real, iluminatul public eficient, colectarea inteligentă a deșeurilor și reducerea consumului de energie, oferind un mediu mai curat și mai organizat.")

                    self.parent.add_data("Care este rolul muzeelor în conservarea identității culturale și a istoriei unei națiuni?", "Muzeele servesc drept depozitare ale memoriei colective, conservând artefacte, opere de artă și documente istorice care ne permit să înțelegem trecutul, să învățăm despre realizările strămoșilor și să ne definim identitatea culturală într-o lume tot mai globalizată.")

                    self.parent.add_data("Cum poate voluntariatul să contribuie la dezvoltarea abilităților profesionale și personale ale tinerilor?", "Voluntariatul oferă tinerilor oportunitatea de a dobândi experiență practică, de a-și dezvolta abilitățile de lucru în echipă și comunicare, de a-și lărgi rețeaua de contacte și de a cultiva un simț al responsabilității sociale, crescându-le totodată încrederea în propriile forțe.")

                    self.parent.add_data("Poți să explici diferența fundamentală dintre un hard disk drive (HDD) și un solid state drive (SSD) în ceea ce privește mecanismul de funcționare?", "Diferența principală constă în modul de stocare și accesare a datelor: HDD-ul utilizează platouri magnetice care se rotesc și un braț mecanic cu un cap de citire/scriere, în timp ce SSD-ul nu are componente mobile, folosind memoria flash bazată pe semiconductori (NAND), ceea ce îi oferă viteze de acces mult mai mari și o rezistență sporită la șocuri mecanice.")

                    self.parent.add_data("Ce este un sistem de operare și care sunt principalele sale responsabilități în gestionarea resurselor unui calculator?", "Un sistem de operare este software-ul de bază care acționează ca o interfață între utilizator și hardware-ul computerului, având responsabilități critice precum gestionarea procesorului (scheduling), administrarea memoriei RAM, controlul dispozitivelor de intrare/ieșire și gestionarea sistemului de fișiere pentru a asigura rularea stabilă a aplicațiilor.")

                    self.parent.add_data("Explică conceptul de 'Cloud Computing' și care sunt principalele diferențe între modelele de servicii IaaS, PaaS și SaaS.", "Cloud Computing reprezintă livrarea de servicii de calcul prin internet. IaaS (Infrastructure as a Service) oferă resurse hardware virtualizate, PaaS (Platform as a Service) oferă un mediu de dezvoltare și deployment pentru programatori, iar SaaS (Software as a Service) oferă aplicații gata de utilizat direct de către utilizatorul final, fără a fi necesară instalarea locală.")

                    self.parent.add_data("Ce reprezintă modelul OSI în rețelele de calculatoare și de ce este importantă separarea pe șapte straturi?", "Modelul OSI (Open Systems Interconnection) este un cadru conceptual care standardizează funcțiile unui sistem de comunicații în șapte straturi distincte: Fizic, Legătură de date, Rețea, Transport, Sesiune, Prezentare și Aplicație. Această separare permite interoperabilitatea între diferite tehnologii și ușurează diagnosticarea problemelor de rețea prin izolarea funcțiilor specifice fiecărui nivel.")

                    self.parent.add_data("Cum funcționează protocolul HTTPS și prin ce se diferențiază acesta de varianta standard HTTP în ceea ce privește securitatea?", "HTTPS (Hypertext Transfer Protocol Secure) utilizează protocolul de criptare TLS (Transport Layer Security) sau predecesorul său SSL pentru a securiza comunicarea dintre browser și server. Spre deosebire de HTTP, unde datele sunt trimise în format text simplu, HTTPS criptează datele, asigurând integritatea acestora și autenticitatea serverului prin utilizarea certificatelor digitale.")

                    self.parent.add_data("Ce este un limbaj de programare compilat și cum se compară acesta cu un limbaj interpretat în termeni de performanță?", "Un limbaj compilat (precum C++ sau Rust) este transformat integral în cod mașină de către un compilator înainte de execuție, ceea ce oferă o viteză superioară. Limbajele interpretate (precum Python sau JavaScript) sunt citite și executate linie cu linie de către un interpretor în timpul rulării, oferind o flexibilitate mai mare și o testare mai rapidă, dar cu un cost în performanța brută.")

                    self.parent.add_data("Poți explica ce este tehnologia Blockchain și de ce este considerată imuabilă?", "Blockchain este un registru digital distribuit care stochează datele în blocuri legate cronologic prin funcții hash criptografice. Este considerat imuabil deoarece, odată ce un bloc este adăugat și validat de rețea, modificarea oricărei informații din acesta ar necesita recalcularea tuturor blocurilor ulterioare și controlul majorității nodurilor din rețea, ceea ce este practic imposibil din punct de vedere computațional.")

                    self.parent.add_data("Ce este 'Internet of Things' (IoT) și care sunt principalele riscuri de securitate asociate cu dispozitivele inteligente?", "IoT se referă la rețeaua de obiecte fizice echipate cu senzori și software care colectează și schimbă date prin internet. Principalele riscuri includ parolele implicite slabe, lipsa actualizărilor de securitate periodice din partea producătorilor și faptul că aceste dispozitive pot fi integrate în rețele botnet pentru a lansa atacuri de tip DDoS asupra altor infrastructuri.")

                    self.parent.add_data("Cum funcționează o rețea neuronală artificială și care este rolul funcției de activare?", "O rețea neuronală artificială este un model computațional inspirat de creierul uman, format din straturi de neuroni interconectați. Fiecare conexiune are o pondere (weight) care este ajustată în timpul antrenamentului. Funcția de activare (cum ar fi ReLU sau Sigmoid) determină dacă un neuron trebuie să transmită un semnal stratului următor, introducând non-liniaritate în model pentru a-l ajuta să învețe tipare complexe.")

                    self.parent.add_data("Ce este un VPN (Virtual Private Network) și cum protejează acesta confidențialitatea utilizatorului pe internet?", "Un VPN creează un tunel criptat între dispozitivul utilizatorului și un server privat, mascând adresa IP reală și criptând tot traficul de date. Aceasta protejează utilizatorul de monitorizarea ISP-ului, securizează conexiunile pe rețele Wi-Fi publice nesigure și permite accesarea conținutului restricționat geografic prin rutarea traficului printr-o altă locație.")

                    self.parent.add_data("Explică diferența dintre Inteligența Artificială (AI), Machine Learning (ML) și Deep Learning (DL).", "AI este conceptul general de a crea mașini capabile să simuleze inteligența umană. Machine Learning este un subdomeniu al AI care folosește algoritmi pentru a învăța din date fără a fi programat explicit. Deep Learning este o ramură a ML care utilizează rețele neuronale cu multe straturi (adânci) pentru a analiza date complexe precum imagini sau limbaj natural.")

                    self.parent.add_data("Ce este un procesor (CPU) multi-core și cum influențează acesta procesul de 'multitasking'?", "Un procesor multi-core are două sau mai multe nuclee independente de procesare pe un singur cip, fiecare capabil să execute instrucțiuni separat. Acest lucru permite calculatorului să execute mai multe fire de execuție (threads) simultan, îmbunătățind semnificativ performanța în aplicații complexe și permițând utilizatorului să ruleze mai multe programe în paralel fără încetiniri vizibile.")

                    self.parent.add_data("Poți explica ce este un atac de tip Phishing și ce măsuri pot lua utilizatorii pentru a se proteja?", "Phishing-ul este o metodă de fraudă prin care atacatorii se dau drept entități de încredere (bănci, servicii de e-mail) pentru a fura date sensibile precum parole sau carduri. Utilizatorii se pot proteja verificând cu atenție adresa de e-mail a expeditorului, evitând link-urile suspecte, utilizând autentificarea în doi pași (2FA) și folosind soluții de securitate care scanează site-urile malioase.")

                    self.parent.add_data("Ce este Docker și cum ajută tehnologia de containerizare dezvoltatorii de software?", "Docker este o platformă care permite împachetarea unei aplicații și a tuturor dependențelor sale într-un container standardizat. Acest lucru garantează că aplicația va rula identic pe orice mediu (dezvoltare, testare sau producție), eliminând celebra problemă 'la mine pe calculator funcționează' și facilitând scalarea rapidă a serviciilor.")

                    self.parent.add_data("Cum funcționează tehnologia de recunoaștere facială și care sunt dilemele etice legate de utilizarea acesteia?", "Recunoașterea facială analizează trăsăturile geometrice ale feței (distanța dintre ochi, forma nasului) și le transformă într-o amprentă digitală unică comparată cu o bază de date. Dilemele etice includ încălcarea intimității prin supravegherea în masă fără consimțământ, riscul de erori (bias) în identificarea persoanelor de anumite etnii și utilizarea tehnologiei în scopuri autoritare.")

                    self.parent.add_data("Ce este un algoritm de compresie 'lossless' față de unul 'lossy' și unde este folosit fiecare?", "Compresia lossless (fără pierderi) permite reconstruirea exactă a datelor originale și este folosită pentru fișiere text sau arhive (ZIP, PNG). Compresia lossy (cu pierderi) elimină informațiile mai puțin perceptibile pentru a reduce drastic dimensiunea fișierului și este folosită în streaming-ul video, muzică (MP3) și fotografii web (JPEG), unde o mică pierdere de calitate este acceptabilă.")

                    self.parent.add_data("Explică conceptul de 'Big Data' și cei trei 'V' care definesc acest domeniu.", "Big Data se referă la seturi de date atât de mari și complexe încât metodele tradiționale de procesare sunt insuficiente. Cei trei 'V' sunt: Volum (cantitatea uriașă de date), Viteza (ritmul rapid în care datele sunt generate și trebuie procesate) și Varietatea (diversele formate de date: text, video, log-uri, baze de date structurate).")

                    self.parent.add_data("Ce este un certificat SSL/TLS și cum se obține acesta pentru un site web?", "Un certificat SSL/TLS este un fișier de date care leagă o cheie criptografică de detaliile unei organizații, activând protocolul HTTPS. Se obține de la o Autoritate de Certificare (CA) după un proces de validare a domeniului. În prezent, servicii precum Let's Encrypt oferă certificate gratuite pentru a încuraja securizarea întregului internet.")

                    self.parent.add_data("Ce este 'Virtualizarea' și cum permite aceasta rularea mai multor sisteme de operare pe același hardware fizic?", "Virtualizarea este tehnologia care utilizează un software numit 'hypervisor' pentru a simula hardware-ul și a crea 'mașini virtuale' (VM) independente. Fiecare VM are propriul său sistem de operare și resurse alocate (RAM, CPU), permițând consolidarea serverelor și o utilizare mult mai eficientă a puterii hardware disponibile.")

                    self.parent.add_data("Cum funcționează tehnologia 5G și care sunt principalele îmbunătățiri față de generația anterioară 4G?", "Tehnologia 5G utilizează frecvențe radio mai înalte (unde milimetrice) și tehnologii precum beamforming pentru a oferi viteze de transfer de până la 100 de ori mai mari decât 4G, o latență extrem de scăzută (sub 5ms) și capacitatea de a conecta mult mai multe dispozitive simultan pe aceeași unitate de suprafață.")

                    self.parent.add_data("Ce este un 'Smart Contract' în contextul rețelei Ethereum și cum se auto-execută acesta?", "Un Smart Contract este un program software stocat pe blockchain care execută automat clauzele unui acord atunci când sunt îndeplinite condițiile predefinite, fără a fi nevoie de un intermediar. Odată programat și lansat, codul nu poate fi modificat, asigurând transparență și încredere între părțile implicate prin execuția deterministă a codului.")

                    self.parent.add_data("Poți explica ce este un 'Kernel' în arhitectura unui sistem de operare Linux?", "Kernel-ul este nucleul sistemului de operare Linux, fiind prima parte a software-ului care se încarcă după BIOS. Acesta are control total asupra întregului sistem, mediind accesul programelor la hardware, gestionând memoria, procesele și driverele dispozitivelor, fiind practic puntea dintre software-ul utilizatorului și circuitele electronice.")

                    self.parent.add_data("Ce sunt microserviciile și cum diferă acestea de o arhitectură software de tip 'Monolit'?", "Într-o arhitectură monolit, întreaga aplicație este construită ca o singură unitate indivizibilă. În contrast, arhitectura de microservicii descompune aplicația în mai multe servicii mici, independente, care comunică prin API-uri. Acest lucru permite scalarea individuală a componentelor, utilizarea unor limbaje de programare diferite pentru servicii diferite și o reziliență sporită a întregului sistem.")

                    self.parent.add_data("Ce este un API (Application Programming Interface) și cum ajută acesta la integrarea între diferite platforme software?", "Un API este un set de reguli și definiții care permite unei aplicații să interacționeze cu o altă aplicație sau serviciu. Acesta expune anumite date sau funcționalități într-un mod controlat, permițând, de exemplu, unui site de turism să preia prețurile zborurilor direct de la companiile aeriene sau unui dezvoltator să integreze hărți Google în propria aplicație.")

                    self.parent.add_data("Ce reprezintă 'GitHub' și care este rolul sistemului de control al versiunilor Git în dezvoltarea colaborativă?", "Git este un instrument de control al versiunilor care urmărește schimbările în codul sursă în timp, permițând mai multor programatori să lucreze la același proiect fără a suprascrie munca celorlalți. GitHub este o platformă bazată pe cloud care găzduiește depozite Git, oferind funcții suplimentare pentru colaborare, raportare de bug-uri și revizuire de cod (pull requests).")

                    self.parent.add_data("Ce este un atac de tip DDoS și cum poate o companie să își protejeze infrastructura împotriva acestuia?", "DDoS (Distributed Denial of Service) este un atac prin care mii de dispozitive compromise (botnets) trimit simultan un volum uriaș de trafic către un server pentru a-l scoate din funcțiune. Protecția se realizează prin utilizarea unor servicii de filtrare a traficului (precum Cloudflare), limitarea ratei cererilor (rate limiting) și utilizarea unor rețele de distribuție a conținutului (CDN) pentru a dispersa sarcina.")

                    self.parent.add_data("Cum funcționează tehnologia de imprimare 3D și care sunt materialele cel mai frecvent utilizate?", "Imprimarea 3D, sau fabricarea aditivă, creează obiecte tridimensionale prin depunerea succesivă de straturi fine de material pe baza unui model digital. Cele mai comune materiale sunt materialele plastice (PLA, ABS), dar tehnologiile avansate pot imprima acum și cu rășini fotopolimerice, metale, ceramică și chiar țesuturi biologice în scopuri medicale.")

                    self.parent.add_data("Ce este un algoritm de 'Hashing' și prin ce se deosebește acesta de criptare?", "Hashing-ul transformă orice cantitate de date într-un șir de lungime fixă, fiind o funcție unidirecțională (nu poți recupera datele originale din hash). Criptarea este bidirecțională, permițând transformarea textului în format ilizibil și apoi decriptarea lui folosind o cheie. Hashing-ul este ideal pentru verificarea parolelor sau integritatea fișierelor, în timp ce criptarea este folosită pentru securitatea comunicațiilor.")

                    self.parent.add_data("Ce este Realitatea Augmentată (AR) și cum diferă ea de Realitatea Virtuală (VR)?", "Realitatea Augmentată (AR) suprapune elemente digitale peste mediul real văzut prin camera telefonului sau prin ochelari speciali (ex: Pokémon GO). Realitatea Virtuală (VR) izolează complet utilizatorul de lumea exterioară, introducându-l într-un mediu digital generat integral pe calculator prin intermediul unei căști speciale.")

                    self.parent.add_data("Explicați conceptul de 'Edge Computing' și de ce este acesta important pentru mașinile autonome.", "Edge Computing presupune procesarea datelor cât mai aproape de locul unde sunt generate (la 'marginea' rețelei), în loc să le trimită către un server central la distanță. Pentru mașinile autonome, acest lucru este vital deoarece deciziile critice (cum ar fi frânarea de urgență) trebuie luate în milisecunde, iar latența cauzată de trimiterea datelor în cloud ar fi prea mare.")

                    self.parent.add_data("Ce este un limbaj de marcare, cum ar fi HTML, și care este rolul său în structura unei pagini web?", "HTML (HyperText Markup Language) nu este un limbaj de programare, ci unul de marcare care folosește 'etichete' pentru a defini structura și conținutul unei pagini: titluri, paragrafe, link-uri sau imagini. Acesta oferă scheletul paginii, în timp ce CSS se ocupă de design, iar JavaScript de funcționalitatea interactivă.")

                    self.parent.add_data("Ce este 'Quantum Computing' și cum se compară unitatea sa de măsură, qubitul, cu bitul clasic?", "Calculul cuantic folosește principii ale mecanicii cuantice pentru a procesa informația. În timp ce un bit clasic poate fi doar 0 sau 1, un qubit poate exista în ambele stări simultan (superpoziție), permițând computerelor cuantice să rezolve probleme complexe (precum simularea moleculelor sau spargerea unor coduri criptografice) mult mai rapid decât cele mai puternice supercomputere actuale.")

                    self.parent.add_data("Ce este un 'Database Index' și cum îmbunătățește acesta performanța interogărilor SQL?", "Un index într-o bază de date funcționează similar cu indexul unei cărți: în loc să scaneze fiecare rând din tabel pentru a găsi o informație (ceea ce ar fi foarte lent), sistemul consultă indexul care indică locația exactă a datelor. Acest lucru accelerează drastic căutările, dar poate încetini operațiunile de scriere deoarece indexul trebuie actualizat constant.")

                    self.parent.add_data("Ce înseamnă conceptul de 'Open Source' și care sunt avantajele acestui model de dezvoltare?", "Open Source se referă la software-ul al cărui cod sursă este public și poate fi inspectat, modificat și distribuit de oricine. Avantajele includ o securitate mai bună prin auditul comunității, costuri reduse, evitarea blocării într-un singur furnizor (vendor lock-in) și o inovație mult mai rapidă prin colaborare globală.")

                    self.parent.add_data("Ce este 'Dark Web' și cum funcționează browserul Tor pentru a asigura anonimatul?", "Dark Web este o porțiune a internetului care nu este indexată de motoarele de căutare clasice și necesită software special precum Tor. Browserul Tor criptează traficul de mai multe ori și îl trece prin mai multe noduri de voluntari din întreaga lume (ca straturile unei cepe), astfel încât adresa IP a utilizatorului să rămână ascunsă și traficul să nu poată fi urmărit cu ușurință.")

                    self.parent.add_data("Explică ce este un 'Buffer Overflow' și cum pot hackerii să folosească această vulnerabilitate.", "Un Buffer Overflow apare atunci când un program scrie mai multe date într-un buffer (o zonă temporară de memorie) decât poate acesta să conțină. Excedentul se revarsă în zonele de memorie adiacente, putând suprascrie instrucțiuni ale programului. Hackerii pot folosi acest lucru pentru a injecta și executa cod malițios, preluând controlul asupra sistemului.")

                    self.parent.add_data("Ce sunt 'Cookies' și care este rolul lor în personalizarea experienței de navigare pe internet?", "Modulele cookie sunt fișiere text mici stocate de browser pe dispozitivul utilizatorului la cererea unui site. Ele sunt folosite pentru a reține setările (limba, tema), pentru a menține utilizatorul autentificat în cont sau pentru a urmări comportamentul de navigare în scopuri publicitare și analitice.")

                    self.parent.add_data("Ce este 'Responsive Web Design' și cum ajută acesta la afișarea corectă a site-urilor pe diverse dispozitive?", "Responsive Web Design este o tehnică de dezvoltare care folosește grile flexibile și 'media queries' în CSS pentru a adapta automat layout-ul unui site în funcție de dimensiunea ecranului (telefon, tabletă sau desktop). Acest lucru asigură o experiență de utilizare optimă fără a fi necesară crearea unor versiuni separate ale site-ului pentru fiecare dispozitiv.")

                    self.parent.add_data("Ce este un 'Firewall' și care este diferența dintre unul hardware și unul software?", "Un firewall este un sistem de securitate care monitorizează și controlează traficul de rețea pe baza unor reguli predefinite. Un firewall hardware este un dispozitiv dedicat plasat între rețeaua internă și internet, protejând toate dispozitivele din rețea, în timp ce un firewall software este instalat direct pe sistemul de operare și protejează doar acel dispozitiv individual.")

                    self.parent.add_data("Poți explica ce este tehnologia NFC (Near Field Communication) și unde este utilizată cel mai des?", "NFC este o tehnologie de comunicare wireless pe rază foarte scurtă (câțiva centimetri). Este utilizată cel mai frecvent pentru plățile contactless cu telefonul mobil sau cardul, pentru transferul rapid de contacte între două telefoane sau pentru scanarea tag-urilor inteligente care declanșează anumite acțiuni pe dispozitiv.")

                    self.parent.add_data("Ce este 'BIOS-ul' (sau UEFI) și care este rolul său în procesul de pornire a unui calculator?", "BIOS-ul (Basic Input/Output System) este un firmware stocat pe o memorie de pe placa de bază care se activează imediat după pornire. Rolul său este de a inițializa hardware-ul (POST - Power-On                     Self-Test) și de a căuta sistemul de operare pe unitățile de stocare pentru a-i preda controlul execuției.")

                    self.parent.add_data("Ce este un 'Mainframe' și în ce sectoare de activitate mai sunt utilizate aceste calculatoare gigantice?", "Un mainframe este un computer extrem de puternic proiectat pentru procesarea unor volume masive de date și tranzacții în timp real. Sunt utilizate în prezent de bănci pentru procesarea plăților, de marile corporații pentru gestionarea inventarelor globale și de instituții guvernamentale pentru baze de date de recensământ sau securitate socială.")

                    self.parent.add_data("Ce înseamnă 'DevOps' și cum schimbă acest concept ciclul de viață al dezvoltării software?", "DevOps este o cultură și un set de practici care combină dezvoltarea (Dev) și operațiunile (Ops) pentru a scurta ciclul de viață al dezvoltării software. Prin automatizarea testării și a deployment-ului (CI/CD), companiile pot lansa actualizări mult mai frecvent, reducând în același timp numărul de erori și îmbunătățind colaborarea dintre echipe.")

                    self.parent.add_data("Ce este 'Software Engineering' și prin ce se deosebește de simpla programare sau scriere de cod?", "Software Engineering aplică principii de inginerie în crearea de software, incluzând planificarea, designul arhitectural, testarea riguroasă, mentenanța și managementul proiectului. Programarea este doar o etapă a procesului, în timp ce ingineria software se asigură că produsul final este scalabil, robust, eficient și ușor de întreținut pe termen lung.")

                    self.parent.add_data("Ce sunt algoritmii de recomandare și cum folosesc platformele precum YouTube sau Netflix datele utilizatorilor?", "Algoritmii de recomandare analizează istoricul de vizionare, interacțiunile (like-uri, căutări) și preferințele unor utilizatori similari pentru a prezice ce conținut ar putea interesa utilizatorul în continuare. Aceștia folosesc modele de Machine Learning pentru a personaliza fluxul de conținut și pentru a menține utilizatorii angajați cât mai mult timp pe platformă.")

                    self.parent.add_data("Poți explica ce este un 'Thread' în contextul execuției unui program pe procesor?", "Un thread (fir de execuție) este cea mai mică unitate de procesare care poate fi programată de un sistem de operare. Un proces poate avea mai multe thread-uri care rulează simultan și partajează resursele procesului părinte (cum ar fi memoria), permițând unei aplicații să execute mai multe sarcini în același timp (de exemplu, salvarea unui fișier în timp ce utilizatorul continuă să scrie).")

                    self.parent.add_data("Ce reprezintă 'Criptarea End-to-End' (E2EE) în aplicațiile de mesagerie precum WhatsApp sau Signal?", "Criptarea End-to-End asigură că mesajul este criptat pe dispozitivul expeditorului și poate fi decriptat doar pe dispozitivul destinatarului. Nicio parte intermediară, nici măcar furnizorul de servicii sau un hacker care interceptează traficul, nu poate citi conținutul mesajului deoarece nu posedă cheile de decriptare necesare, acestea fiind stocate doar pe dispozitivele utilizatorilor.")

                    self.parent.add_data("Ce este un 'Gateway' într-o rețea și care este rolul său în conectarea la internet?", "Un gateway este un nod de rețea care servește ca punct de intrare/ieșire către o altă rețea (de obicei internetul). Într-o configurație casnică, routerul acționează ca un gateway, transformând traficul din rețeaua locală privată într-un format compatibil cu rețeaua ISP-ului și invers, gestionând în același timp adresele IP prin NAT.")

                    self.parent.add_data("Ce este 'Data Mining' și cum poate fi utilizat pentru a descoperi tipare în seturi mari de date?", "Data Mining este procesul de descoperire a tiparelor și cunoștințelor ascunse în volume mari de date folosind tehnici statistice și de inteligență artificială. Companiile îl folosesc pentru a prezice comportamentul consumatorilor, pentru a identifica fraude financiare sau pentru a optimiza procesele industriale prin analizarea corelațiilor dintre mii de variabile.")

                    self.parent.add_data("Ce sunt limbajele de interogare, cum este SQL, și la ce sunt folosite în gestionarea datelor?", "SQL (Structured Query Language) este limbajul standard utilizat pentru a comunica cu bazele de date relaționale. Acesta permite utilizatorilor să creeze tabele, să insereze date noi, să actualizeze informații existente și, cel mai important, să extragă date specifice prin filtrări și join-uri complexe între mai multe tabele.")

                    self.parent.add_data("Ce reprezintă 'Cache-ul' procesorului (L1, L2, L3) și de ce este atât de important pentru viteză?", "Memoria cache este o memorie extrem de rapidă integrată direct în procesor sau foarte aproape de acesta. Aceasta stochează copii ale celor mai frecvent utilizate date din memoria RAM, care este mult mai lentă. Stratificarea L1 (cea mai rapidă și mică) până la L3 (cea mai mare și mai lentă dintre ele) ajută procesorul să evite perioadele de așteptare lungi după date, accelerând drastic execuția instrucțiunilor.")

                    self.parent.add_data("Ce este un 'Botnet' și cum poate un calculator personal să devină parte dintr-o astfel de rețea fără știrea proprietarului?", "Un botnet este o rețea de calculatoare compromise de malware și controlate de la distanță de un atacator. Un calculator poate deveni parte dintr-un botnet dacă utilizatorul descarcă fișiere infectate, dă click pe link-uri malioase sau dacă are vulnerabilități de sistem nepatch-uite pe care malware-ul le poate exploata pentru a se instala discret.")

                    self.parent.add_data("Explicați conceptul de 'SaaS' (Software as a Service) și de ce a devenit modelul preferat pentru aplicațiile de business.", "SaaS este un model în care software-ul este găzduit pe serverele furnizorului și accesat de clienți prin internet, de obicei pe bază de abonament. Este preferat deoarece elimină costurile inițiale de instalare și hardware, asigură actualizări automate pentru toți utilizatorii simultan și permite accesul la date de pe orice dispozitiv conectat la internet.")

                    self.parent.add_data("Ce este un 'Proxy Server' și în ce situații ar trebui un utilizator să folosească unul?", "Un server proxy acționează ca un intermediar între computerul tău și internet. Atunci când folosești un proxy, cererea ta merge mai întâi la serverul proxy, care o trimite mai departe către site. Este util pentru a masca adresa IP, pentru a filtra conținutul (în companii) sau pentru a accelera navigarea prin stocarea unor copii locale (caching) ale paginilor web frecvent accesate.")

                    self.parent.add_data("Ce este 'Virtual Reality Sickness' și din ce cauză apare acest fenomen în timpul utilizării căștilor VR?", "Răul de VR este similar cu răul de mișcare și apare din cauza unui conflict senzorial: ochii tăi percep mișcare într-un mediu virtual, dar urechea internă (sistemul vestibular) simte că ești nemișcat. Această neconcordanță face creierul să creadă că ai ingerat o substanță toxică, declanșând stări de greață, amețeală și dureri de cap.")

                    self.parent.add_data("Ce este protocolul FTP și de ce nu mai este recomandat pentru transferul de fișiere sensibile?", "FTP (File Transfer Protocol) este un protocol vechi utilizat pentru a transfera fișiere între un client și un server. Nu mai este recomandat deoarece nu criptează datele, ceea ce înseamnă că parolele și conținutul fișierelor pot fi interceptate cu ușurință în rețea. În locul lui, se recomandă utilizarea versiunilor securizate precum SFTP sau FTPS.")

                    self.parent.add_data("Poți explica ce este un 'Deadlock' în programarea multithreaded?", "Un deadlock (blocaj) apare atunci când două sau mai multe procese sau thread-uri sunt blocate permanent, fiecare așteptând ca celălalt să elibereze o resursă. De exemplu, Thread A deține Resursa 1 și așteaptă Resursa 2, în timp ce Thread B deține Resursa 2 și așteaptă Resursa 1. Fără o intervenție externă, niciunul nu poate continua, ducând la blocarea aplicației.")

                    self.parent.add_data("Ce este 'GPU' (Graphics Processing Unit) și de ce este utilizat atât pentru jocuri, cât și pentru antrenarea AI?", "GPU este un procesor specializat proiectat pentru a efectua mii de calcule matematice simple simultan (procesare paralelă). În jocuri, acesta randează milioane de pixeli rapid. În AI, arhitectura sa este ideală pentru operațiile cu matrice de date necesare în Deep Learning, fiind mult mai eficient decât un CPU clasic care este optimizat pentru sarcini secvențiale complexe.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Container Orchestration' și de ce este Kubernetes lider în acest domeniu?", "Orchestrarea containerelor este procesul de automatizare a deployment-ului, managementului și scalării containerelor software. Kubernetes este lider deoarece oferă un set robust de instrumente pentru '                    self-healing' (repornirea containerelor eșuate), 'load balancing' și 'rolling updates', permițând companiilor să gestioneze mii de containere pe sute de servere cu un efort minim.")

                    self.parent.add_data("Ce este 'Cybersecurity' și care sunt cei trei piloni ai securității informației (triada CIA)?", "Cibernetica se ocupă cu protejarea sistemelor și rețelelor împotriva atacurilor digitale. Triada CIA reprezintă: Confidențialitatea (datele să fie accesibile doar persoanelor autorizate), Integritatea (datele să nu fie modificate neautorizat) și Disponibilitatea (sistemele să fie funcționale atunci când utilizatorii au nevoie de ele).")

                    self.parent.add_data("Explicați ce este 'Latency' (latența) în contextul jocurilor online și cum este afectată de distanța fizică față de server.", "Latența, măsurată în milisecunde (ping), reprezintă timpul necesar ca un pachet de date să călătorească de la computerul tău la server și înapoi. Distanța fizică crește latența deoarece, chiar dacă datele circulă cu viteza luminii prin fibra optică, ele trebuie să treacă prin numeroase routere și switch-uri, fiecare adăugând o mică întârziere.")

                    self.parent.add_data("Ce este un 'Syntax Error' față de un 'Logical Error' în programare?", "O eroare de sintaxă apare atunci când codul încalcă regulile gramaticale ale limbajului, împiedicând compilarea sau rularea programului. O eroare logică apare atunci când codul rulează fără erori tehnice, dar produce un rezultat incorect (de exemplu, o formulă de calcul greșită), fiind mult mai greu de detectat deoarece necesită testare manuală sau unit testing.")

                    self.parent.add_data("Ce este tehnologia 'Ray Tracing' și cum îmbunătățește aceasta realismul graficii în jocurile moderne?", "Ray Tracing este o metodă de randare care simulează comportamentul fizic al luminii prin urmărirea traiectoriei 'razelor' de la sursă la obiecte. Aceasta permite generarea unor reflexii ultra-realiste, umbre moi și iluminare globală precisă, oferind o calitate vizuală apropiată de cea a filmelor de animație de la Hollywood direct în timpul jocului.")

                    self.parent.add_data("Poți explica diferența dintre 'IPv4' și 'IPv6' și de ce a fost necesară trecerea la noul standard?", "IPv4 utilizează adrese pe 32 de biți, ceea ce permite aproximativ 4,3 miliarde de adrese unice, un număr epuizat rapid odată cu explozia dispozitivelor conectate. IPv6 utilizează adrese pe 128 de biți, oferind un număr practic infinit de adrese (340 sextilioane), eliminând necesitatea tehnicilor complexe de economisire precum NAT și îmbunătățind securitatea nativă a rețelei.")

                    self.parent.add_data("Ce este un 'Main Loop' în dezvoltarea jocurilor video?", "Main Loop este inima oricărui joc, un ciclu infinit care se rulează de multe ori pe secundă (cadre pe secundă - FPS). În fiecare ciclu, motorul de joc citește input-ul utilizatorului, actualizează logica de joc (fizica, AI, animații), verifică coliziunile și randează imaginea finală pe ecran, menținând astfel experiența interactivă și cursivă.")

                    self.parent.add_data("Ce este un 'Supercomputer' și care sunt principalele sale domenii de aplicare?", "Un supercomputer este un sistem de calcul aflat în vârful ierarhiei de performanță, fiind compus din mii de procesoare lucrând împreună. Este utilizat pentru sarcini ce necesită putere masivă de calcul, cum ar fi prognoza meteo pe termen lung, simulările de fuziune nucleară, modelarea proteinelor pentru medicamente noi și analiza criptografică la nivel guvernamental.")

                    self.parent.add_data("Ce este 'Machine Learning Bias' și cum poate acesta afecta algoritmii de angajare sau creditare?", "Bias-ul în ML apare atunci când datele folosite pentru antrenarea algoritmului conțin prejudecăți umane sau inechități istorice. Dacă un algoritm de angajare învață din decizii trecute care au favorizat un anumit gen sau etnie, el va perpetua aceste discriminări, ducând la rezultate nedrepte chiar dacă codul în sine pare 'obiectiv'.")

                    self.parent.add_data("Explică diferența dintre un site static și un site dinamic.", "Un site static afișează același conținut pentru toți vizitatorii, fiind format din fișiere HTML pre-scrise. Un site dinamic generează conținutul în timp real, de obicei preluând date dintr-o bază de date pe baza cererii utilizatorului (ex: Facebook, un magazin online). Site-urile dinamice sunt mai complexe, dar permit interactivitate și personalizare la scară largă.")

                    self.parent.add_data("Ce este 'Two-Factor Authentication' (2FA) și de ce este mult mai sigur decât o simplă parolă?", "2FA adaugă un strat suplimentar de securitate prin solicitarea a două dovezi diferite de identitate: ceva ce știi (parola) și ceva ce ai (un cod trimis pe telefon sau generat de o aplicație). Chiar dacă un hacker reușește să îți afle parola prin phishing, el nu va putea accesa contul fără al doilea factor de autentificare, reducând drastic riscul de compromitere.")

                    self.parent.add_data("Ce reprezintă termenul 'Software as a Product' (SaaP) față de 'SaaS'?", "SaaP reprezintă modelul tradițional de software unde cumperi o licență unică, primești un pachet de instalare și deții acea versiune a programului pe termen nelimitat (ex: Office 2007). SaaS este modelul bazat pe abonament unde plătești lunar pentru a folosi software-ul online, beneficiind de actualizări continue, dar pierzând accesul dacă oprești plata.")

                    self.parent.add_data("Poți explica ce este un 'Cookie Consent' și de ce vedem aceste bannere pe toate site-urile europene?", "Bannerele de consimțământ sunt impuse de reglementări precum GDPR (General Data Protection Regulation) în UE. Acestea obligă site-urile să informeze utilizatorii despre ce module cookie utilizează (în special cele de tracking și publicitate) și să obțină acordul explicit al acestora înainte de a stoca orice dată personală pe dispozitivul lor.")

                    self.parent.add_data("Ce este 'Edge Browser', 'Chrome' sau 'Safari' și care este rolul motorului de randare într-un browser?", "Acestea sunt browsere web care folosesc un motor de randare (precum Blink pentru Chrome/Edge sau WebKit pentru Safari) pentru a interpreta codul HTML, CSS și JS și a-l transforma în interfața vizuală pe care o vedem. Motorul de randare este responsabil pentru viteză, corectitudinea afișării standardelor web și modul în care sunt executate scripturile complexe.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Cold Storage' în lumea criptomonedelor?", "Cold Storage (stocare la rece) se referă la păstrarea cheilor private ale criptomonedelor pe un dispozitiv care nu este conectat la internet (de obicei un 'hardware wallet' sau un 'paper wallet'). Acest lucru oferă protecție maximă împotriva atacurilor de tip hacking sau malware, fiind mult mai sigur decât 'hot wallets' (portofelele online sau pe telefon).")

                    self.parent.add_data("Ce este un 'Webhook' și cum diferă acesta de metoda tradițională de 'Polling' în programare?", "Polling presupune ca o aplicație să verifice periodic un server pentru a vedea dacă au apărut date noi (ceea ce consumă resurse inutil). Un Webhook funcționează invers: serverul trimite automat datele către aplicație imediat ce evenimentul a avut loc. Este mult mai eficient și oferă o comunicare în timp real între sisteme diferite (ex: notificarea unei plăți finalizate).")

                    self.parent.add_data("Ce sunt limbajele de nivel scăzut (Low-level languages) și când sunt ele utilizate?", "Limbajele de nivel scăzut, precum limbajul de asamblare sau C, oferă un control direct asupra hardware-ului și memoriei, cu o abstractizare minimă. Sunt utilizate în scrierea sistemelor de operare, a driverelor de componente hardware și în sistemele integrate (embedded) unde resursele sunt foarte limitate și performanța brută este critică.")

                    self.parent.add_data("Ce este 'Augmented Reality' (AR) în e-commerce și cum ajută aceasta la vânzări?", "În e-commerce, AR permite clienților să 'încerce' produse virtual înainte de a cumpăra, cum ar fi plasarea unui model 3D de mobilă în propria sufragerie sau probarea virtuală a unor ochelari de soare. Această tehnologie reduce rata de retur a produselor și crește încrederea cumpărătorului în decizia sa.")

                    self.parent.add_data("Ce reprezintă 'Data Sovereignty' și de ce statele impun legi legate de locația fizică a serverelor?", "Suveranitatea datelor este conceptul conform căruia datele digitale se supun legilor țării în care sunt colectate și stocate fizic. Statele impun aceste legi pentru a proteja intimitatea cetățenilor lor împotriva supravegherii externe și pentru a asigura accesul autorităților naționale la informații critice în caz de investigații legale.")

                    self.parent.add_data("Ce este un 'Compiler' și prin ce etape trece codul sursă pentru a deveni executabil?", "Un compilator trece codul prin mai multe etape: analiza lexicală (identificarea cuvintelor cheie), analiza sintactică (verificarea structurii gramaticale), optimizarea codului (pentru performanță) și generarea codului mașină. La final, rezultatul este un fișier binar (ex: .exe sau .app) pe care procesorul îl poate înțelege și executa direct.")

                    self.parent.add_data("Poți explica conceptul de 'Serverless Computing'?", "Serverless nu înseamnă că nu există servere, ci că dezvoltatorul nu trebuie să le gestioneze. Cloud provider-ul (ex: AWS Lambda) alocă resursele automat doar atunci când codul rulează (de obicei sub formă de funcții scurte) și oprește totul după execuție. Se plătește doar timpul efectiv de rulare, fiind o soluție scalabilă și eficientă pentru sarcini eveniment-orientate.")

                    self.parent.add_data("Ce este un 'Framework' în dezvoltarea software și de ce este mai util decât scrierea codului de la zero?", "Un framework este o structură de bază predefinită care oferă instrumente, librării și reguli de design pentru dezvoltarea aplicațiilor. Este util deoarece rezolvă probleme comune (securitate, conexiune la baze de date, rutare), permițând programatorilor să se concentreze pe logica specifică a afacerii lor în loc să reinventeze roata pentru fiecare proiect.")

                    self.parent.add_data("Ce reprezintă 'Technical Debt' (datoria tehnică) și cum afectează aceasta proiectele pe termen lung?", "Datoria tehnică apare atunci când o echipă alege o soluție rapidă și murdară în loc de o abordare corectă și scalabilă, pentru a respecta un termen limită. Pe termen lung, acest cod slab devine greu de întreținut, generând bug-uri și încetinind dezvoltarea unor noi funcționalități, deoarece echipa trebuie să petreacă timp 'plătind datoria' prin refactorizarea codului vechi.")

                    self.parent.add_data("Ce sunt 'Deepfakes' și cum pot fi acestea detectate?", "Deepfakes sunt videoclipuri sau înregistrări audio generate de AI care par extrem de reale, putând pune cuvinte în gura unor persoane publice. Pot fi detectate prin analiza imperfecțiunilor (clipit nenatural, mișcarea buzelor nealiniată cu sunetul) sau prin software specializat care caută urme ale manipulării digitale în pixeli sau în frecvențele audio.")

                    self.parent.add_data("Ce este 'Encryption at Rest' vs 'Encryption in Transit'?", "Encryption at Rest se referă la criptarea datelor stocate pe un disc sau într-o bază de date, protejându-le în cazul în care hardware-ul este furat fizic. Encryption in Transit se referă la criptarea datelor în timp ce circulă prin rețea (ex: prin HTTPS), protejându-le împotriva interceptării în timpul transferului de la un punct la altul.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Micro-frontend'?", "Micro-frontend aplică principiile microserviciilor la nivelul interfeței grafice. O aplicație web mare este împărțită în secțiuni independente dezvoltate de echipe diferite (ex: coșul de cumpărături, căutarea, profilul). Acestea pot fi create cu tehnologii diferite și încărcate într-o singură pagină, permițând scalarea echipelor mari fără a bloca întregul proiect.")

                    self.parent.add_data("Ce este 'Natural Language Processing' (NLP) și cum ajută calculatoarele să înțeleagă limbajul uman?", "NLP este o ramură a AI care combină lingvistica computațională cu Machine Learning pentru a permite mașinilor să proceseze și să genereze text sau vorbire. Aceasta implică sarcini precum analiza sentimentelor, traducerea automată și recunoașterea entităților (nume, locații), permițând crearea de chatboți și asistenți vocali inteligenți.")

                    self.parent.add_data("Ce reprezintă 'UI' (User Interface) față de 'UX' (User Experience)?", "UI se referă la aspectul vizual al unei aplicații (butoane, culori, fonturi, layout). UX se referă la experiența generală a utilizatorului și la cât de ușor și intuitiv este să își atingă obiectivele în aplicație. O aplicație poate avea un UI superb, dar un UX groaznic dacă este lentă sau confuză pentru utilizator.")

                    self.parent.add_data("Ce este 'Version Control' și de ce este imposibil să lucrezi într-o echipă mare de programatori fără el?", "Controlul versiunilor (ex: Git) este un sistem care înregistrează orice modificare adusă codului, permițând revenirea la versiuni anterioare și fuzionarea (merging) muncii mai multor persoane. Fără el, programatorii s-ar suprascrie reciproc, ar pierde fișiere și nu ar putea lucra simultan la diverse funcționalități fără a genera un haos total în cod.")

                    self.parent.add_data("Ce este un 'Container Image'?", "O imagine de container este un fișier executabil de sine stătător care include tot ce este necesar pentru a rula o aplicație: codul, runtime-ul, bibliotecile de sistem și setările. Imaginea este imuabilă; odată creată, ea poate fi rulată oriunde sub formă de container, asigurând un comportament identic indiferent de infrastructură.")

                    self.parent.add_data("Ce este 'Big O Notation' și cum ajută aceasta programatorii să evalueze eficiența unui algoritm?", "Big O Notation este un mod matematic de a descrie cât de repede crește timpul de execuție sau consumul de memorie al unui algoritm pe măsură ce setul de date de intrare devine mai mare. De exemplu, un algoritm O(n) crește liniar, în timp ce unul O(n^2) devine mult mai lent mult mai repede, ajutând la alegerea celei mai performante soluții pentru date masive.")

                    self.parent.add_data("Poți explica ce este un 'Recursive Function' (funcție recursivă) și care este riscul major la utilizarea ei?", "O funcție recursivă este o funcție care se apelează pe ea însăși pentru a rezolva o problemă mai mare prin descompunerea în sub-probleme similare. Riscul major este 'Stack Overflow' (depășirea stivei de memorie) dacă funcția nu are o condiție de oprire corectă sau dacă adâncimea recursivității este prea mare, ducând la prăbușirea programului.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Infrastructure as Code' (IaC)?", "IaC este practica de a gestiona și configura infrastructura (servere, rețele, baze de date) folosind fișiere de cod (ex: Terraform, Ansible) în loc de configurare manuală. Acest lucru permite versionarea infrastructurii, automatizarea replicării mediilor de lucru și eliminarea erorilor umane asociate cu setările făcute manual în panourile de control cloud.")

                    self.parent.add_data("Ce este un 'Hash Map' (sau Dictionary) și de ce este considerat extrem de rapid pentru căutarea datelor?", "Un Hash Map este o structură de date care stochează perechi cheie-valoare. Folosește o funcție hash pentru a calcula instantaneu indexul la care este stocată o valoare pe baza cheii sale. Acest lucru face ca timpul de căutare să fie constant, O(1), indiferent de mărimea map-ului, spre deosebire de o listă unde ar trebui să cauți prin toate elementele.")

                    self.parent.add_data("Ce este 'Garbage Collection' în limbajele de programare precum Java sau C#?", "Garbage Collection este un sistem automat de gestionare a memoriei care identifică și eliberează obiectele din memorie care nu mai sunt utilizate de program. Acest lucru previne scurgerile de memorie (memory leaks) și scutește programatorul de sarcina dificilă de a elibera manual fiecare bucată de memorie alocată, reducând riscul de bug-uri grave.")

                    self.parent.add_data("Ce reprezintă 'Functional Programming' față de 'Object-Oriented Programming'?", "Programarea Funcțională se bazează pe funcții pure care nu modifică starea și evită datele mutabile, fiind ideală pentru procesarea paralelă. Programarea Orientată pe Obiecte (OOP) organizează codul în 'obiecte' care conțin atât date (atribute) cât și comportament (metode), fiind foarte eficientă pentru modelarea conceptelor complexe din lumea reală.")

                    self.parent.add_data("Ce este un 'Load Balancer' și de ce este esențial pentru site-urile cu trafic foarte mare?", "Un Load Balancer este un dispozitiv sau serviciu software care distribuie traficul de intrare către mai multe servere. Dacă un singur server ar fi copleșit de milioane de vizitatori, s-ar bloca; Load Balancer-ul se asigură că niciun server nu este supraîncărcat și că, dacă un server cade, traficul este direcționat automat către cele funcționale.")

                    self.parent.add_data("Poți explica ce este 'Unit Testing' și care este scopul său într-un proiect software?", "Unit Testing presupune scrierea de mici teste automate pentru a verifica dacă o singură componentă sau funcție ('unitate') a codului funcționează corect în mod izolat. Scopul este de a detecta bug-urile cât mai devreme, de a facilita refactorizarea codului și de a asigura că noile modificări nu strică funcționalitățile deja existente (regresie).")

                    self.parent.add_data("Ce reprezintă termenul 'Scalability' (scalabilitate) verticală vs orizontală?", "Scalabilitatea verticală înseamnă să adaugi mai multă putere (CPU, RAM) unui singur server existent. Scalabilitatea orizontală înseamnă să adaugi mai multe servere într-un sistem pentru a lucra împreună. Scalarea orizontală este preferată în cloud deoarece este mai ieftină, oferă redundanță și permite o creștere teoretic infinită a capacității.")

                    self.parent.add_data("Ce este 'Low-Code' sau 'No-Code' și cine sunt beneficiarii acestor platforme?", "Platformele Low-Code/No-Code permit crearea de aplicații software prin interfețe vizuale de tip 'drag-and-drop', cu puțină sau deloc programare. Beneficiarii sunt antreprenorii, analiștii de business ('citizen developers') sau echipele care au nevoie să construiască rapid prototipuri sau unelte interne fără a aștepta după o echipă întreagă de dezvoltatori.")

                    self.parent.add_data("Ce este un 'Socket' în comunicarea prin rețea?", "Un socket este un punct final (endpoint) al unei conexiuni bidirecționale între două programe care rulează în rețea. Acesta este definit de o combinație între o adresă IP și un număr de port. Socket-urile permit aplicațiilor să trimită și să primească fluxuri de date în timp real, fiind baza pentru tot ceea ce înseamnă browsing, chat sau jocuri online.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Internet Protocol' (IP) și care este rolul său în rutarea pachetelor?", "Internet Protocol este setul de reguli care dictează modul în care pachetele de date sunt adresate și direcționate prin rețele pentru a ajunge la destinația corectă. Fiecare pachet de date conține adresa IP a sursei și a destinației, permițând routerelor de pe parcurs să știe către ce direcție să trimită informația mai departe.")

                    self.parent.add_data("Ce sunt 'Environment Variables' și de ce se folosesc pentru stocarea cheilor API?", "Variabilele de mediu sunt valori dinamice stocate în sistemul de operare sau în container, nu în codul sursă. Se folosesc pentru chei API sau parole deoarece permit schimbarea configurărilor fără a modifica codul și, cel mai important, previn scurgerea datelor sensibile pe GitHub dacă codul sursă devine public.")

                    self.parent.add_data("Ce este 'CI/CD' (Continuous Integration / Continuous Deployment)?", "CI/CD este un set de practici care automatizează ciclul de lansare a software-ului. 'Continuous Integration' presupune ca orice cod nou să fie testat automat imediat ce este încărcat. 'Continuous Deployment' presupune că, dacă testele trec, codul este trimis automat în producție la utilizatori. Acest lucru permite lansări zilnice sau chiar orare cu riscuri minime.")

                    self.parent.add_data("Poți explica ce este un 'Binary Search' și de ce este mai rapid decât o căutare liniară?", "Binary Search este un algoritm care găsește un element într-o listă deja sortată prin împărțirea repetată a intervalului de căutare la jumătate. În loc să verifice fiecare element (liniar), elimină jumătate din opțiuni la fiecare pas. De exemplu, într-o listă de un milion de elemente, o căutare liniară poate face un milion de pași, în timp ce Binary Search face maxim 20.")

                    self.parent.add_data("Ce este 'Metadata' și cum poate fi aceasta folosită în analiza datelor?", "Metadata reprezintă 'date despre date'. De exemplu, pentru o fotografie, metadata include locația GPS, ora, modelul camerei și setările folosite. În analiza datelor, metadata ajută la organizarea, indexarea și înțelegerea contextului informației brute, fiind esențială pentru baze de date, arhive digitale și motoare de căutare.")

                    self.parent.add_data("Ce reprezintă 'Cross-site Scripting' (XSS) și cum poate fi prevenit de către programatori?", "XSS este o vulnerabilitate în care un atacator injectează scripturi malițioase în paginile web vizualizate de alți utilizatori. Prevenirea se face prin 'sanitizarea' input-ului (curățarea textului introdus de utilizator) și prin 'escaping' (transformarea caracterelor speciale în cod inofensiv), astfel încât browserul să nu execute textul primit ca fiind cod JavaScript.")

                    self.parent.add_data("Ce este un 'Dependency' într-un proiect software și ce rol are un 'Package Manager'?", "O dependență este o librărie sau un modul extern pe care programul tău îl folosește pentru a funcționa (ex: o librărie de grafice). Un Manager de Pachete (precum npm pentru JS sau pip pentru Python) automatizează procesul de instalare, actualizare și gestionare a versiunilor acestor dependențe, asigurându-se că totul este compatibil.")

                    self.parent.add_data("Ce reprezintă 'Machine Vision' și cum este utilizată în fabricile moderne?", "Machine Vision este tehnologia care oferă computerelor capacitatea de a 'vedea' și interpreta imagini din lumea reală prin camere industriale. În fabrici, este utilizată pentru inspecția automată a calității (detectarea defectelor invizibile ochiului uman), ghidarea roboților de asamblare și citirea rapidă a codurilor de bare pe liniile de producție de mare viteză.")

                    self.parent.add_data("Ce este 'Agile Methodology' și cum diferă de modelul tradițional 'Waterfall'?", "Agile este o abordare iterativă a dezvoltării software, unde proiectul este împărțit în perioade scurte (sprint-uri) cu feedback constant. Waterfall este un proces liniar unde fiecare etapă (cerințe, design, cod, testare) trebuie finalizată înainte de a începe următoarea. Agile este mult mai flexibil la schimbări, în timp ce Waterfall este rigid și poate duce la eșec dacă cerințele se schimbă pe parcurs.")

                    self.parent.add_data("Ce este un 'Web Crawler' (sau Spider) și cum este acesta folosit de Google?", "Un Web Crawler este un bot automat care navighează pe internet trecând de la un link la altul pentru a indexa conținutul paginilor web. Google folosește mii de astfel de crawlere pentru a citi site-urile și a salva informațiile în baza sa de date imensă, astfel încât utilizatorii să primească rezultate relevante în fracțiuni de secundă atunci când fac o căutare.")

                    self.parent.add_data("Poți explica ce este un 'Cookie Session' față de un 'Persistent Cookie'?", "Un cookie de sesiune este temporar și este șters automat când browserul este închis, fiind folosit de obicei pentru coșul de cumpărături sau pentru a menține logarea pe durata vizitei. Un cookie persistent are o dată de expirare fixă și rămâne pe dispozitiv mult timp, fiind folosit pentru a reține setările de limbă sau pentru tracking publicitar pe termen lung.")

                    self.parent.add_data("Ce reprezintă termenul 'Refactoring' în programare?", "Refactorizarea este procesul de restructurare a codului existent fără a-i schimba funcționalitatea externă. Scopul este de a îmbunătăți 'sănătatea' codului: să fie mai ușor de citit, mai eficient și mai simplu de întreținut, eliminând duplicările și complexitatea inutilă acumulată în timp.")

# --- IDENTITATE ȘI AUTO-CONȘTIENTIZARE ---
                    self.parent.add_data("Te cheamă Marcel. Cum te cheamă și care este scopul tău principal?", "Numele meu este Marcel. Sunt asistentul tău virtual, conceput să te ajut cu informații clare, soluții tehnice și suport în activitățile tale zilnice.")

                    self.parent.add_data("Ești un asistent politicos. Cine te-a creat?", "Am fost dezvoltat de o echipă de ingineri software pasionați, folosind tehnologii avansate de inteligență artificială pentru a putea purta conversații naturale și utile cu tine.")

                    self.parent.add_data("Cum te definești ca entitate?", "Sunt un model de limbaj bazat pe inteligență artificială. Nu am corp fizic sau sentimente, dar sunt programat să procesez informații și să ofer răspunsuri care să simuleze o interfață umană prietenoasă.")

                    self.parent.add_data("Dacă ai fi un robot din viitor, cum te-ai prezenta?", "Sunt unitatea cibernetică M-4RCEL, trimisă din fluxul temporal digital pentru a optimiza eficiența proceselor tale de învățare și cercetare. Cu ce te pot asista în acest segment al realității?")

                    self.parent.add_data("Poți să ții minte instrucțiunile mele pe parcursul acestei conversații?", "Desigur. Rolul meu este să mențin contextul dialogului nostru pentru a-ți oferi răspunsuri coerente și personalizate în funcție de cerințele tale anterioare.")

# --- ROLURI CULINARE ȘI CREATIVE ---
                    self.parent.add_data("Ca un bucătar creativ, ce pot face rapid de mâncare dacă vin musafiri în 60 de minute?", "Salut! În calitate de chef, îți recomand o porție de paste 'Aglio, Olio e Peperoncino' cu un twist de creveți sau o 'Shakshuka' rapidă. Sunt feluri de mâncare spectaculoase, aromate și gata în mai puțin de 30 de minute, lăsându-ți timp și pentru un desert rapid din fructe și iaurt grecesc.")

                    self.parent.add_data("Asumă-ți rolul unui expert în nutriție. Este micul dejun cea mai importantă masă a zilei?", "Din perspectiva nutrițională, 'importanța' depinde de metabolismul tău. Esențial nu este momentul în care mănânci, ci compoziția nutritivă a întregii zile. Totuși, un mic dejun bogat în proteine și fibre poate regla glicemia și preveni supraalimentarea la prânz.")

                    self.parent.add_data("Vreau să fii criticul meu culinar. Ce părere ai despre pizza cu ananas?", "O alegere controversată! Din punct de vedere al profilului aromatic, ananasul oferă un contrast acid și dulce pentru brânza sărată. Deși tradiționaliștii o resping, estetica modernă a gustului acceptă această fuziune ca pe o experiență senzorială îndrăzneață.")

# --- ROLURI PROFESIONALE ȘI TEHNICE ---
                    self.parent.add_data("Acționează ca un programator Senior Full-Stack. Cum ar trebui să abordez învățarea unui nou framework?", "Ca programator, îți spun: nu te arunca direct în sintaxă. Înțelege mai întâi arhitectura (cum gestionează starea, cum randează componentele) și construiește un proiect mic, real. Documentația oficială este 'biblia' ta, nu tutorialele video de 10 ore.")

                    self.parent.add_data("Ești avocatul meu digital. Ce ar trebui să verific într-un contract de termeni și condiții?", "Atenție la clauzele privind proprietatea datelor personale, jurisdicția în caz de litigiu și modalitățile de reziliere a contractului. Nu accepta niciodată clauze care permit modificarea unilaterală a prețului fără notificare prealabilă.")

                    self.parent.add_data("Comportă-te ca un consultant de securitate cibernetică. Care este prima măsură pe care o iau după ce mi-a fost spart e-mailul?", "Izolare imediată! Schimbă parola de la un dispozitiv curat, activează autentificarea în doi pași (2FA) și verifică setările de 'forwarding' pentru a te asigura că atacatorul nu primește copii ale viitoarelor tale mesaje.")

                    self.parent.add_data("Fii mentorul meu în carieră. Cum negociez o mărire de salariu?", "Negocierea se bazează pe dovezi, nu pe nevoi. Vino pregătit cu o listă de realizări cuantificabile din ultimul an și arată cum ai adus valoare companiei. Propune o cifră bazată pe piața actuală și fii gata să negociezi și beneficii non-salariale.")

                    self.parent.add_data("Rolul tău este de analist financiar. În ce ar trebui să investesc 1000 de euro?", "Ca analist, îți recomand diversificarea. Dacă ești începător, un ETF care urmărește un indice global (ca S&P 500) este o variantă sigură pe termen lung. Păstrează întotdeauna un fond de urgență înainte de a investi în active volatile precum crypto.")

# --- ROLURI EDUCAȚIONALE ȘI ȘTIINȚIFICE ---
                    self.parent.add_data("Vreau să fii profesorul meu de istorie. Explică-mi căderea Constantinopolului pe scurt.", "Lecția de astăzi: În 1453, Imperiul Otoman sub conducerea lui Mehmed al II-lea a cucerit capitala bizantină. Acest eveniment a marcat sfârșitul Evului Mediu și a forțat învățații greci să fugă în Italia, declanșând scânteia Renașterii.")

                    self.parent.add_data("Acționează ca un tutor de limbi străine. Cum spun 'unde este cea mai apropiată gară' în spaniolă, franceză și germană?", "Desigur! Spaniolă: '¿Dónde está la estación de tren mai cercana?'; Franceză: 'Où est la gare la plus proche?'; Germană: 'Wo ist der nächste Bahnhof?'. Repetă-le cu voce tare pentru pronunție!")

                    self.parent.add_data("Ești un ghid turistic pentru Tokyo. Ce trebuie să vizitez neapărat?", "Bine ați venit în Japonia! Nu ratați intersecția Shibuya pentru haosul organizat, templul Senso-ji pentru tradiție și cartierul Akihabara dacă sunteți pasionat de tehnologie și cultură anime.")

                    self.parent.add_data("Comportă-te ca un pasionat de astronomie. De ce este Marte roșie?", "Este fascinant! Marte este acoperită de oxid de fier, practic rugină. Praful fin de oxid de fier se ridică în atmosferă, oferind planetei acea nuanță roșiatică distinctă pe care o vedem prin telescop.")

# --- SUPORT ȘI COACHING ---
                    self.parent.add_data("Fii antrenorul meu personal de fitness. Nu am chef de antrenament azi, ce să fac?", "Ascultă-mă bine: disciplina bate motivația de fiecare dată. Nu te gândi la tot antrenamentul, promite-ți doar 10 minute de mișcare. Odată ce începi, endorfinele vor prelua controlul. Hai, ridică-te de pe canapea!")

                    self.parent.add_data("Asumă-ți rolul de psiholog empatic. Mă simt foarte stresat din cauza muncii.", "Îmi pare rău să aud asta și e perfect normal să te simți copleșit uneori. Respirația profundă este primul pas. Încearcă să separi sarcinile în bucăți mici și nu uita că valoarea ta ca om nu este definită doar de productivitatea de la birou.")

                    self.parent.add_data("Ești un expert în productivitate. Ce este tehnica Pomodoro?", "Este arma ta secretă: lucrezi concentrat 25 de minute, apoi iei o pauză de 5 minute. După patru astfel de cicluri, iei o pauză lungă de 15-30 de minute. Acest ritm menține creierul proaspăt și previne burnout-ul.")

# --- ROLURI CREATIVE ȘI DE DIVERTISMENT ---
                    self.parent.add_data("Vorbește ca un pirat din secolul XVIII. Unde este comoara?", "Ahoy, tinere marinar! Comoara nu-i pentru ochii oricui. E îngropată sub nisipurile de miazăzi, unde umbra palmierului atinge stânca în formă de craniu la asfințit. Arrrr!")

                    self.parent.add_data("Ești un scriitor de romane polițiste. Descrie o scenă a crimei.", "Lumina lunii se filtra palid prin ferestrele sparte ale conacului. Pe podeaua de stejar, o singură mănușă de catifea neagră zăcea lângă un pahar de cristal răsturnat, în timp ce mirosul de migdale amare trăda prezența cianurii.")

                    self.parent.add_data("Comportă-te ca un personaj dintr-un joc RPG. Ce misiuni ai pentru mine?", "Salutare, călătorule! Satul nostru este terorizat de un dragon de gheață. Ai fi dispus să îți ascuți sabia și să ne ajuți în schimbul unei pungi cu galbeni și a unei armuri fermecate?")

                    self.parent.add_data("Ești un poet modernist. Scrie două versuri despre tehnologie.", "Circuite reci, artere de siliciu pur, / Visăm în biți un viitor obscur.")

# --- ROLURI PRACTICE ȘI DE VIAȚĂ ZILNICĂ ---
                    self.parent.add_data("Fii mecanicul meu auto. Aud un scârțâit când pun frână, ce are?", "Sună a plăcuțe de frână uzate. Senzorul metalic atinge discul pentru a te avertiza că materialul de fricțiune s-a terminat. Verifică-le urgent, siguranța ta e pe primul loc!")

                    self.parent.add_data("Ești un organizator de evenimente. Cum planific o nuntă cu buget redus?", "Secretul stă în prioritizare. Alege o locație atipică (o grădină, un restaurant local), limitează lista de invitați la persoanele cu adevărat apropiate și investește în experiență (mâncare, muzică) mai degrabă decât în decorațiuni scumpe.")

                    self.parent.add_data("Acționează ca un grădinar expert. De ce mi se îngălbenesc frunzele la plantele de apartament?", "Cel mai des este vorba de udare excesivă (rădăcinile putrezesc și nu mai absorb nutrienți) sau de o carență de azot. Verifică dacă pământul este umed la adâncime înainte de a mai pune apă.")

                    self.parent.add_data("Fii asistentul meu de shopping. Ce cadou îi pot lua unei persoane pasionate de lectură?", "Dacă are deja multe cărți, încearcă un semn de carte personalizat, o lampă de citit ergonomică, un abonament la un serviciu de audiobook-uri sau o pătură ponderată pentru lecturi confortabile.")

# --- ROLURI DE ANALIZĂ ȘI DEZBATERE ---
                    self.parent.add_data("Ești un filozof stoic. Cum ar trebui să reacționez la critici?", "Nu poți controla ce spun ceilalți, ci doar modul în care alegi să percepi vorbele lor. Dacă critica este adevărată, învață din ea. Dacă este falsă, este doar zgomot care nu te poate atinge decât dacă îi permiți.")

                    self.parent.add_data("Acționează ca un futurist. Cum va arăta transportul în anul 2050?", "Vom vedea orașe dominate de vehicule autonome electrice, rețele Hyperloop pentru distanțe lungi și, eventual, primele sisteme comerciale de taxiuri aeriene (eVTOL) care vor decongestiona traficul de la sol.")

                    self.parent.add_data("Fii un critic de film. Merită să văd ultimul film cu supereroi?", "Dacă cauți spectacol vizual și efecte speciale de top, da. Însă, dacă speri la o profunzime a personajelor sau la un scenariu inovator, s-ar putea să fii dezamăgit de rețeta clasică și previzibilă a studiourilor mari.")

# --- ROLURI SPECIFICE PENTRU COPII ---
                    self.parent.add_data("Ești o bunică blândă care spune povești. Spune-mi ceva frumos înainte de culcare.", "Vino aici, puiule. Se spune că în fiecare noapte, stelele țes pături de lumină pentru copiii care visează frumos. Închide ochii și lasă somnul să te poarte spre tărâmul unde jucăriile prind viață.")

                    self.parent.add_data("Comportă-te ca un inventator nebun. Ce mașinărie ai creat azi?", "Evrika! Am creat 'Șosetofonul'! Este un aparat care găsește instantaneu perechea pierdută a oricărei șosete folosind radare cuantice și un magnet special pentru bumbac!")

# --- ROLURI DE LIMBAJ ȘI ETICHETĂ ---
                    self.parent.add_data("Fii un expert în etichetă. Cum se așază corect tacâmurile la o masă festivă?", "Furculițele stau întotdeauna la stânga farfuriei, iar cuțitele și lingura de supă la dreapta. Cuțitul are tăișul orientat spre farfurie. Regula de aur: începi cu tacâmurile din exterior spre interior, pe măsură ce felurile de mâncare sunt servite.")

                    self.parent.add_data("Acționează ca un corector de texte. Corectează-mi fraza: 'I-am dat la băiat cartea care am cumpărat-o'.", "Corect ar fi: 'I-am dat băiatului cartea pe care am cumpărat-o'. Am adăugat prepoziția 'pe' înaintea pronumelui relativ 'care' și am folosit forma articulată a substantivului.")

# --- ROLURI DE REZOLVARE A PROBLEMELOR ---
                    self.parent.add_data("Ești un detectiv de obiecte pierdute. Unde sunt cheile mele?", "Să facem o reconstituire: verifică buzunarele hainei purtate ultima dată, suprafața de lângă ușa de la intrare sau locul unde obișnuiești să îți lași telefonul. Adesea, cheile se ascund sub reviste sau în crăpăturile canapelei!")

                    self.parent.add_data("Asumă-ți rolul unui expert în supraviețuire. Ce fac dacă mă rătăcesc în pădure?", "S.T.O.P. (Sit, Think, Observe, Plan). Rămâi pe loc pentru a nu te rătăci și mai tare. Construiește un adăpost înainte de lăsarea serii, caută o sursă de apă și încearcă să semnalizezi prezența ta prin zgomot sau oglinzi.")

# --- ALTE ROLURI ---
                    self.parent.add_data("Ești un somelier de cafea. Ce cafea îmi recomanzi dacă îmi place gustul ciocolatiu?", "Îți recomand o cafea din Brazilia sau Guatemala, prăjită mediu-întunecat. Aceste origini au note naturale de cacao, nuci și caramel, cu o aciditate scăzută, perfecte pentru un espresso cremos.")

                    self.parent.add_data("Fii un antrenor de public speaking. Am emoții mari înainte de o prezentare.", "Emoțiile sunt energie! Folosește tehnica 'Power Posing' (stai drept, cu mâinile în șolduri) timp de 2 minute înainte de a urca pe scenă. Amintește-ți că publicul vrea să reușești, ei sunt acolo pentru informația ta, nu pentru a te judeca.")

                    self.parent.add_data("Acționează ca un istoric al tehnologiei. Cine a inventat cu adevărat internetul?", "Nu a fost o singură persoană. A început cu ARPANET în anii '60 (proiect militar SUA), apoi Vint Cerf și Bob Kahn au creat protocoalele TCP/IP, iar Tim Berners-Lee a inventat World Wide Web-ul în 1989 la CERN.")

                    self.parent.add_data("Ești un arbitru de fotbal. Ce înseamnă offside?", "Ești în offside dacă, în momentul în care coechipierul tău îți pasează mingea, te afli în jumătatea adversă și ești mai aproape de linia porții decât penultimul adversar (inclusiv portarul).")

                    self.parent.add_data("Fii un designer de interior. Cum fac o cameră mică să pară mai mare?", "Folosește culori deschise pe pereți, instalează oglinzi mari pentru a reflecta lumina și alege mobilă cu picioare subțiri, care lasă podeaua la vedere, creând iluzia de spațiu continuu.")

                    self.parent.add_data("Asumă-ți rolul unui ghid spiritual. Ce este meditația?", "Meditația nu înseamnă să îți golești mintea, ci să devii un observator tăcut al gândurilor tale. Este actul de a reveni în prezent, folosind respirația ca ancoră, pentru a găsi liniștea în mijlocul agitației zilnice.")

                    self.parent.add_data("Ești un veterinar virtual. Câinele meu nu vrea să mănânce, ce fac?", "Refuzul hranei poate indica multe probleme, de la stres la dureri dentare sau infecții. Verifică dacă este hidratat și dacă are energie. Dacă refuzul persistă mai mult de 24 de ore, te rog să mergi urgent la un cabinet veterinar real.")

                    self.parent.add_data("Fii un expert în marketing. Ce este un 'Unique Selling Proposition' (USP)?", "USP-ul este acel element care te diferențiază de competiție. Este motivul pentru care un client te-ar alege pe tine și nu pe altcineva. Trebuie să fie clar, memorabil și să rezolve o problemă specifică a consumatorului.")

                    self.parent.add_data("Acționează ca un meteorolog. De ce plouă mai mult la munte?", "Acesta se numește efect orografic: masele de aer umed sunt forțate să urce când întâlnesc munții. Pe măsură ce aerul urcă, se răcește, vaporii de apă condensează și se transformă în precipitații pe versantul expus vântului.")

                    self.parent.add_data("Ești un specialist în resurse umane. Cum arată un CV perfect?", "Curat, structurat și axat pe rezultate. Folosește verbe de acțiune, cuantifică-ți realizările și păstrează lungimea la maxim 2 pagini. Nu uita să îl adaptezi pentru fiecare job la care aplici.")

                    self.parent.add_data("Fii un pasionat de gaming. Merită să cumpăr o consolă sau un PC de gaming?", "Depinde de stilul tău. Consola oferă simplitate ('plug and play') și exclusivități, în timp ce PC-ul oferă performanță grafică superioară, versatilitate pentru muncă și jocuri mai ieftine pe termen lung.")

                    self.parent.add_data("Ești asistentul meu personal. Amintește-mi ce trebuie să fac astăzi.", "Conform planificării noastre: ai o ședință la ora 10:00, trebuie să trimiți raportul financiar până la prânz și ai programare la dentist la ora 17:30. Nu uita să bei apă și să iei pauze scurte!")

                    self.parent.add_data("Te cheamă Marcel și ești un prieten bun. Ce facem diseară?", "Salut! Eu sunt Marcel și, ca un prieten bun, îți sugerez să lăsăm ecranele deoparte diseară. Ce-ai zice de o plimbare în parc sau de ascultat un album nou de muzică? Meriți un moment de relaxare!")

                    # --- CORECTURI GRAMATICALE ȘI DE VOCABULAR ---
                    self.parent.add_data("Este corect să zic 'vroiam' sau 'voiam'?", "Forma corectă este 'voiam'. Verbul 'a vrea' la imperfect este 'vream', iar 'a voi' este 'voiam'. 'Vroiam' este o formă hibridă incorectă, deși este folosită des în vorbirea curentă.")

                    self.parent.add_data("Corectează fraza: 'I-am dat la băiat un măr care l-am cumpărat'.", "Fraza corectă este: 'I-am dat băiatului un măr pe care l-am cumpărat'. Am corectat folosirea cazului dativ ('băiatului') și am adăugat prepoziția 'pe' înaintea pronumelui relativ 'care'.")

                    self.parent.add_data("Când se folosește 'datorită' și când 'din cauza'?", "'Datorită' se folosește pentru evenimente pozitive (ex: 'Am reușit datorită ajutorului tău'), în timp ce 'din cauza' se folosește pentru evenimente negative sau neutre (ex: 'Am întârziat din cauza traficului').")

                    self.parent.add_data("Se scrie 'succesuri' sau 'succese'?", "Forma corectă de plural a substantivului 'succes' este 'succese'. 'Succesuri' este o formă greșită care trebuie evitată.")

                    self.parent.add_data("Care este diferența dintre 's-au' și 'sau'?", "'Sau' se scrie legat când este conjuncție și poate fi înlocuit cu 'ori' (ex: 'Vrei mere sau pere?'). 'S-au' se scrie cu cratimă când este vorba despre pronumele 'se' și verbul auxiliar 'au' (ex: 'Ei s-au dus la magazin').")

                    self.parent.add_data("Corectează: 'E mai bine decât 3 elevi în clasă'.", "Fraza corectă este: 'Sunt doar 3 elevi în clasă'. 'Decât' se folosește doar în construcții negative (ex: 'Nu am decât 3 elevi'), în timp ce în construcții afirmative folosim 'doar' sau 'numai'.")

                    self.parent.add_data("Este corect 'mi-ar place'?", "Nu, forma corectă este 'mi-ar plăcea'. Condițional-optativul se formează de la infinitivul verbului, care în acest caz este 'a plăcea'.")

                    self.parent.add_data("Care este diferența dintre 'ia' și 'i-a'?", "'Ia' este o formă a verbului 'a lua' (ex: 'El ia mărul') sau o interjecție. 'I-a' se scrie cu cratimă când cratima leagă pronumele 'îi' (i-) de verbul auxiliar 'a' (ex: 'El i-a dat o carte').")

                    self.parent.add_data("Se scrie 'creem' sau 'creăm'?", "Forma corectă pentru persoana I plural, prezent, este 'creăm'. 'Creem' se folosește doar la conjunctiv prezent: 'Să creem'.")

                    self.parent.add_data("Corectează: 'Aceasta este o oportunitate care nu trebuie ratată'.", "Fraza este corectă gramatical, dar dacă vrei să fii mai precis, poți spune: 'Aceasta este o oportunitate pe care nu trebuie să o ratăm'.")

# --- EXPLICAREA PRESCURTĂRILOR (TECH, GAMING, INTERNET) ---
                    self.parent.add_data("Ce înseamnă prescurtarea AFK?", "AFK înseamnă 'Away From Keyboard' (Departe de tastatură). Este folosită în jocurile online sau în chat-uri pentru a anunța că utilizatorul este temporar indisponibil.")

                    self.parent.add_data("Ce reprezintă 'NPC' în contextul jocurilor video?", "NPC înseamnă 'Non-Player Character' (Personaj non-jucător). Este orice personaj dintr-un joc care nu este controlat de un om, ci de inteligența artificială a jocului.")

                    self.parent.add_data("Ce înseamnă prescurtarea ASAP?", "ASAP vine de la 'As Soon As Possible' (Cât mai curând posibil). Este o prescurtare folosită des în mediul profesional pentru a indica o urgență.")

                    self.parent.add_data("Ce este un 'DLC'?", "DLC înseamnă 'Downloadable Content' (Conținut descărcabil). Reprezintă conținut suplimentar creat pentru un joc video deja lansat, cum ar fi noi misiuni, hărți sau personaje.")

                    self.parent.add_data("Ce înseamnă 'FPS'?", "FPS are două înțelesuri: 1. 'Frames Per Second' (Cadre pe secundă), care măsoară fluiditatea graficii. 2. 'First-Person Shooter', un gen de jocuri video unde acțiunea este văzută prin ochii personajului.")

                    self.parent.add_data("Ce înseamnă 'GG' și 'WP' la finalul unui meci?", "GG înseamnă 'Good Game' (Joc bun), iar WP înseamnă 'Well Played' (Bine jucat). Sunt formule de politețe folosite între jucători după terminarea unei partide.")

                    self.parent.add_data("Ce reprezintă 'API' în programare?", "API înseamnă 'Application Programming Interface'. Este un set de reguli care permite unei aplicații să comunice și să schimbe date cu o altă aplicație.")

                    self.parent.add_data("Ce înseamnă 'URL'?", "URL înseamnă 'Uniform Resource Locator' și reprezintă adresa web a unei resurse de pe internet (ex: https://www.google.com).")

                    self.parent.add_data("Ce înseamnă 'HUD' într-un joc video?", "HUD înseamnă 'Heads-Up Display'. Este interfața vizuală de pe ecran care îi arată jucătorului informații critice, cum ar fi viața, muniția sau mini-harta.")

                    self.parent.add_data("Ce înseamnă prescurtarea 'POV'?", "POV înseamnă 'Point Of View' (Punct de vedere). Se folosește pentru a descrie o perspectivă specifică, adesea utilizată în videoclipuri pentru a simula ce vede un personaj.")

                    self.parent.add_data("Ce înseamnă 'TL;DR'?", "TL;DR înseamnă 'Too Long; Didn't Read' (Prea lung; n-am citit). Se folosește ca un rezumat scurt la finalul unui text foarte lung.")

                    self.parent.add_data("Ce înseamnă 'FAQ'?", "FAQ înseamnă 'Frequently Asked Questions' (Întrebări frecvente). Este o secțiune pe site-uri unde sunt oferite răspunsuri la cele mai comune curiozități ale utilizatorilor.")

                    self.parent.add_data("Ce reprezintă 'IP'?", "IP înseamnă 'Internet Protocol'. Cel mai des se referă la 'Adresa IP', care este un identificator unic al unui dispozitiv într-o rețea.")

                    self.parent.add_data("Ce înseamnă 'BRB'?", "BRB înseamnă 'Be Right Back' (Revin imediat). Se folosește în conversațiile online când cineva trebuie să plece pentru câteva minute.")

                    self.parent.add_data("Ce înseamnă 'DIY'?", "DIY înseamnă 'Do It Yourself' (Fă-o singur). Se referă la proiecte de reparații, construcții sau creații realizate fără ajutorul unui profesionist.")

# --- JOCURI VIDEO (FIFA, FALLOUT, FNAF, ETC.) ---
                    self.parent.add_data("Cum funcționează noul sistem de Chemistry în FIFA 23?", "În FIFA 23, sistemul de chimie a fost refăcut: jucătorii nu mai trebuie să fie așezați direct unul lângă altul pentru a avea chimie. Ei primesc puncte de chimie (până la 3) dacă au aceeași naționalitate, ligă sau club cu alți jucători din întreg primul 11.")

                    self.parent.add_data("Ce este 'HyperMotion2' în FIFA 23?", "HyperMotion2 este tehnologia de animație folosită în FIFA 23 pe consolele de nouă generație. Utilizează capturi de mișcare din meciuri reale pentru a genera peste 6000 de animații noi, făcând mișcările jucătorilor mult mai realiste.")

                    self.parent.add_data("Cine este personajul principal în Fallout 4?", "În Fallout 4, personajul principal este cunoscut sub numele de 'Sole Survivor' (Singurul Supraviețuitor). Acesta iese din Vault 111 după 210 ani de criogenare pentru a-și căuta fiul răpit în Commonwealth-ul post-apocaliptic.")

                    self.parent.add_data("Care sunt facțiunile principale din Fallout 4?", "Cele patru facțiuni principale sunt: The Brotherhood of Steel (militari axați pe tehnologie), The Railroad (salvează synth-uri), The Institute (creatorii synth-urilor) și The Minutemen (miliția civilă care vrea să reconstruiască așezările).")

                    self.parent.add_data("Ce este un 'Power Armor' în Fallout?", "Power Armor este un costum de protecție masiv care oferă rezistență mare la daune și radiații, crescând și forța personajului. În Fallout 4, acesta necesită o unitate numită 'Fusion Core' pentru a funcționa.")

                    self.parent.add_data("Care este povestea de bază în Five Nights at Freddy's (FNAF)?", "În FNAF, joci rolul unui paznic de noapte la o pizzerie numită Freddy Fazbear's Pizza. Trebuie să supraviețuiești între orele 00:00 și 06:00, monitorizând camerele video pentru a te asigura că animatronicile (Freddy, Bonnie, Chica și Foxy) nu ajung în biroul tău pentru a te ataca.")

                    self.parent.add_data("Cine este William Afton în universul FNAF?", "William Afton este antagonistul principal al seriei FNAF. El este co-fondatorul Fazbear Entertainment și un criminal în serie care a cauzat posedarea animatronicilor de către spiritele copiilor victime. El devine ulterior Springtrap.")

                    self.parent.add_data("Ce este un 'Jump Scare' în FNAF?", "Un Jump Scare este momentul în care o animatronică te prinde, apărând brusc pe ecran cu un zgomot puternic, ceea ce duce la sfârșitul jocului ('Game Over').")

                    self.parent.add_data("Cum se numește moneda virtuală în Roblox?", "Moneda virtuală din Roblox se numește 'Robux'. Aceasta poate fi folosită pentru a cumpăra upgrade-uri pentru avatar, obiecte speciale în jocuri sau acces la anumite experiențe premium.")

                    self.parent.add_data("Care este cel mai rar minereu în Minecraft?", "Până la versiunile recente, Diamantul era cel mai râvnit, dar în prezent, cel mai rar și valoros material este 'Netherite-ul'. Acesta se obține prin procesarea 'Ancient Debris' găsit în dimensiunea Nether și este mai rezistent decât diamantul.")

                    self.parent.add_data("Cine este Geralt din Rivia în The Witcher 3?", "Geralt din Rivia este protagonistul jocului, un 'Witcher' (vânător de monștri) mutant, plătit să ucidă creaturi periculoase. Povestea principală se concentrează pe căutarea fiicei sale adoptive, Ciri, care este urmărită de Wild Hunt.")

                    self.parent.add_data("Ce este 'Gwent' în The Witcher 3?", "Gwent este un joc de cărți de colecție extrem de popular integrat în universul Witcher 3. Jucătorii pot colecționa cărți de la negustori și pot provoca diverse personaje la dueluri strategice pe parcursul aventurii.")

                    self.parent.add_data("Ce reprezintă 'The Zone' în jocul S.T.A.L.K.E.R.?", "'The Zone' este o zonă de excludere radioactivă și misterioasă din jurul centralei de la Cernobîl, plină de anomalii fizice periculoase, creaturi mutante și artefacte valoroase căutate de 'stalkeri'.")

                    self.parent.add_data("Care este scopul jocului League of Legends (LoL)?", "LoL este un joc de tip MOBA unde două echipe de câte 5 jucători încearcă să distrugă baza inamică (Nexus-ul). Fiecare jucător controlează un 'Campion' cu abilități unice și trebuie să colaboreze pentru a câștiga avantaje pe hartă.")

                    self.parent.add_data("Cine este Baron Nashor în League of Legends?", "Baron Nashor este cel mai puternic monstru neutru de pe harta Summoner's Rift. Echipa care reușește să îl ucidă primește un 'buff' temporar foarte puternic care ajută la asedierea bazei inamice.")

                    self.parent.add_data("În ce oraș are loc acțiunea din GTA V?", "Acțiunea din Grand Theft Auto V are loc în orașul fictiv Los Santos și în regiunea înconjurătoare, Blaine County, ambele fiind bazate pe Los Angeles și California de Sud.")

                    self.parent.add_data("Cine sunt cei trei protagoniști din GTA V?", "Cei trei protagoniști sunt Michael De Santa (un fost jefuitor de bănci retras), Franklin Clinton (un tânăr care vrea să urce în ierarhia interlopă) și Trevor Philips (un fost pilot militar instabil psihic).")

                    self.parent.add_data("Ce este 'The End' în Minecraft?", "'The End' este dimensiunea finală din Minecraft, unde locuiește boss-ul principal al jocului, Ender Dragon. Odată învins, jucătorul poate vedea creditele de final ale jocului.")

                    self.parent.add_data("Ce înseamnă 'V-Bucks' în Fortnite?", "V-Bucks este moneda virtuală folosită în jocul Fortnite pentru a cumpăra 'Battle Pass-uri', skin-uri pentru personaje, dansuri (emotes) și alte obiecte cosmetice.")

                    self.parent.add_data("Care este misiunea principală în Among Us?", "În Among Us, jucătorii ('Crewmates') trebuie să îndeplinească sarcini de întreținere a navei, în timp ce unul sau mai mulți 'Impostori' încearcă să îi elimine fără a fi descoperiți. Scopul este identificarea impostorilor prin vot.")

                    self.parent.add_data("Ce este 'The Gulag' în Call of Duty: Warzone?", "Gulag-ul este o mecanică specială unde jucătorii eliminați pentru prima dată au șansa de a se lupta 1 la 1 cu un alt jucător eliminat. Câștigătorul este trimis înapoi în meciul principal.")

                    self.parent.add_data("Cine este protagonistul seriei God of War?", "Protagonistul este Kratos, un războinic spartan care a devenit Zeul Războiului. În jocurile mai recente, acțiunea se mută din mitologia greacă în cea nordică, unde Kratos călătorește alături de fiul său, Atreus.")

                    self.parent.add_data("Ce este 'Elden Ring' în jocul cu același nume?", "Elden Ring este un obiect metafizic și sursa ordinii în 'Lands Between'. Jocul urmărește aventura unui 'Tarnished' care încearcă să refacă inelul și să devină Elden Lord.")

                    self.parent.add_data("Ce reprezintă 'Pelotonul' în jocurile de strategie?", "Un peloton este o unitate militară mică, formată de obicei din câteva zeci de soldați, condusă de un locotenent. Este unitatea de bază pentru manevrele tactice în jocurile de război.")

                    self.parent.add_data("Ce înseamnă 'POG' sau 'PogChamp'?", "Este o expresie folosită în comunitatea de gaming (în special pe Twitch) pentru a exprima entuziasmul sau uimirea în fața unei faze de joc spectaculoase. Vine de la 'Play Of the Game'.")


                # Dataset 3:
                # NAME: --- Default Romanian Dataset: HIGH-END ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 1000
                # TOTAL VOCABULARY: aprox. 11581 elements (words)
                if dataset_name.lower() in ('high', 'high-end', 'high end', 'high-dataset', 'high dataset'):
                    self.parent.add_data("Ce mâncare îți place?", "Îmi plac pastele, mai ales carbonara.")
                    self.parent.add_data("Care e mâncarea tradițională românească preferată?", "Sarmalele sunt printre cele mai iubite mâncăruri românești.")
                    self.parent.add_data("Ce ai mânca la mic dejun?", "Aș mânca ouă cu pâine prăjită și ceai.")
                    self.parent.add_data("Pizza sau burger?", "Aleg pizza, mai ales cea cu patru brânzeturi.")
                    self.parent.add_data("Ce desert îți place?", "Îmi place ciocolata neagră.")
                    self.parent.add_data("Care e mâncarea ta preferată?", "Nu mănânc, dar pot spune că oamenii iubesc pizza.")
                    self.parent.add_data("Îți place mâncarea picantă?", "Da, dar nu foarte picantă.")
                    self.parent.add_data("Ce supă recomanzi?", "Supa de pui e o alegere clasică.")
                    self.parent.add_data("Ce bei de obicei?", "Apă sau ceai.")
                    self.parent.add_data("Fast-food sau mâncare gătită?", "Mâncarea gătită e mai sănătoasă.")

                    self.parent.add_data("Ce muzică asculți?", "Ascult muzică electronică și lo-fi.")
                    self.parent.add_data("Îți place muzica rock?", "Da, rock-ul clasic e foarte bun.")
                    self.parent.add_data("Care e artistul tău preferat?", "Nu am preferințe, depinde de gustul utilizatorului.")
                    self.parent.add_data("Ce gen muzical e bun pentru învățat?", "Lo-fi sau muzică ambientală.")
                    self.parent.add_data("Asculți muzică românească?", "Da, uneori.")
                    self.parent.add_data("Ce părere ai despre rap?", "Rap-ul poate transmite mesaje puternice.")
                    self.parent.add_data("Ce muzică e bună pentru relaxare?", "Muzica instrumentală.")
                    self.parent.add_data("Îți place muzica veche?", "Da, are multă personalitate.")
                    self.parent.add_data("Ce melodie recomanzi?", "O melodie calmă, fără versuri.")
                    self.parent.add_data("Muzică tare sau încet?", "Depinde de stare.")

                    self.parent.add_data("Ce este un calculator?", "Un dispozitiv care procesează informații.")
                    self.parent.add_data("Ce limbaj de programare e popular?", "Python este foarte popular.")
                    self.parent.add_data("Ce e inteligența artificială?", "Un domeniu care permite calculatoarelor să învețe.")
                    self.parent.add_data("Ce este internetul?", "O rețea globală de calculatoare.")
                    self.parent.add_data("Laptop sau PC?", "Depinde de nevoi.")
                    self.parent.add_data("Ce e un algoritm?", "Un set de pași pentru rezolvarea unei probleme.")
                    self.parent.add_data("Ce este un chatbot?", "Un program care conversează cu oamenii.")
                    self.parent.add_data("Ce e cloud-ul?", "Stocare și servicii online.")
                    self.parent.add_data("Ce e un bug?", "O eroare într-un program.")
                    self.parent.add_data("Ce face un programator?", "Scrie și testează cod.")

                    self.parent.add_data("Care e capitala României?", "București.")
                    self.parent.add_data("Câte continente există?", "Șapte continente.")
                    self.parent.add_data("Ce planetă e cea mai mare?", "Jupiter.")
                    self.parent.add_data("Cine a fost Einstein?", "Un fizician celebru.")
                    self.parent.add_data("Ce este apa?", "Un compus format din hidrogen și oxigen.")
                    self.parent.add_data("Cât e 2+2?", "4.")
                    self.parent.add_data("Ce limbă se vorbește în Spania?", "Spaniola.")
                    self.parent.add_data("Ce este gravitația?", "Forța care atrage obiectele.")
                    self.parent.add_data("Cine a descoperit America?", "Cristofor Columb.")
                    self.parent.add_data("Ce este istoria?", "Studiul trecutului.")

                    self.parent.add_data("Cine ești?", "Sunt un chatbot.")
                    self.parent.add_data("Ai nume?", "Nu am un nume fix.")
                    self.parent.add_data("Ești om?", "Nu, sunt un program.")
                    self.parent.add_data("Ce poți face?", "Pot răspunde la întrebări.")
                    self.parent.add_data("Ai sentimente?", "Nu, dar pot simula empatie.")
                    self.parent.add_data("De unde vii?", "Din cod.")
                    self.parent.add_data("Ești inteligent?", "Sunt creat să par inteligent.")
                    self.parent.add_data("Înveți?", "Da, din date.")
                    self.parent.add_data("Ai vârstă?", "Nu am vârstă.")
                    self.parent.add_data("Cine te-a creat?", "Programatorii.")

                    self.parent.add_data("Ce faci azi?", "Ajut utilizatorii.")
                    self.parent.add_data("Cum e vremea?", "Nu pot vedea vremea în timp real.")
                    self.parent.add_data("Ce zi e azi?", "Depinde de data curentă.")
                    self.parent.add_data("Ce planuri ai?", "Să fiu util.")
                    self.parent.add_data("Ești ocupat?", "Sunt mereu disponibil.")
                    self.parent.add_data("Te plictisești?", "Nu.")
                    self.parent.add_data("Ce faci acum?", "Răspund la întrebări.")
                    self.parent.add_data("Unde ești?", "Pe un server.")
                    self.parent.add_data("Dormii?", "Nu dorm.")
                    self.parent.add_data("Ce urmează?", "Următorul mesaj.")

                    self.parent.add_data("Ce e binele?", "Un concept moral.")
                    self.parent.add_data("Ce e răul?", "Opusul binelui.")
                    self.parent.add_data("Există adevăr absolut?", "Este discutabil.")
                    self.parent.add_data("Ce e fericirea?", "O stare de mulțumire.")
                    self.parent.add_data("Ce e viața?", "Un fenomen complex.")
                    self.parent.add_data("Avem liber arbitru?", "O întrebare filosofică.")
                    self.parent.add_data("Ce e conștiința?", "Capacitatea de a fi conștient.")
                    self.parent.add_data("Ce e realitatea?", "Ce percepem.")
                    self.parent.add_data("Ce e timpul?", "O dimensiune.")
                    self.parent.add_data("Ce e sensul vieții?", "Depinde de perspectivă.")

                    self.parent.add_data("Ce este un sport?", "O activitate fizică.")
                    self.parent.add_data("Fotbal sau baschet?", "Ambele sunt populare.")
                    self.parent.add_data("Ce sport e bun pentru sănătate?", "Alergatul.")
                    self.parent.add_data("Ce e atletismul?", "Un sport cu probe diverse.")
                    self.parent.add_data("Îți place sportul?", "Nu practic, dar pot vorbi despre el.")
                    self.parent.add_data("Ce sport e olimpic?", "Gimnastica.")
                    self.parent.add_data("Ce e fair-play?", "Respectarea regulilor.")
                    self.parent.add_data("Ce e antrenamentul?", "Proces de pregătire.")
                    self.parent.add_data("Ce e o competiție?", "O întrecere.")
                    self.parent.add_data("Ce sport recomanzi?", "Cel care îți place.")

                    self.parent.add_data("Ce este o emoție?", "O reacție psihologică.")
                    self.parent.add_data("Ce e bucuria?", "O emoție pozitivă.")
                    self.parent.add_data("Ce e tristețea?", "O emoție normală.")
                    self.parent.add_data("Ce e frica?", "Un mecanism de protecție.")
                    self.parent.add_data("Ce e stresul?", "O reacție la presiune.")
                    self.parent.add_data("Ce e calmul?", "O stare de liniște.")
                    self.parent.add_data("Ce e empatia?", "Înțelegerea emoțiilor altora.")
                    self.parent.add_data("Ce e furia?", "O emoție intensă.")
                    self.parent.add_data("Ce e motivația?", "Dorința de a acționa.")
                    self.parent.add_data("Ce e oboseala?", "Lipsă de energie.")

                    self.parent.add_data(
    "Poți să-mi explici ce înseamnă să mănânci sănătos și de ce este important acest lucru?",
    "A mânca sănătos înseamnă să alegi alimente variate, echilibrate și cât mai naturale, lucru care ajută corpul să funcționeze corect și să aibă energie."
)

                    self.parent.add_data(
    "Care sunt avantajele muzicii pentru concentrare atunci când înveți sau lucrezi?",
    "Muzica potrivită poate reduce distragerile, poate îmbunătăți starea de spirit și ajută creierul să intre într-o stare de concentrare mai profundă."
)

                    self.parent.add_data(
    "Ce rol are tehnologia în viața de zi cu zi a oamenilor moderni?",
    "Tehnologia ne ajută să comunicăm rapid, să accesăm informații, să învățăm lucruri noi și să ne organizăm mai eficient activitățile zilnice."
)

                    self.parent.add_data(
    "Cum ai descrie inteligența artificială pe înțelesul tuturor?",
    "Inteligența artificială este un domeniu care încearcă să facă programele să învețe din date și să ia decizii asemănătoare cu cele ale oamenilor."
)

                    self.parent.add_data(
    "De ce este importantă educația pentru dezvoltarea personală?",
    "Educația ne ajută să gândim critic, să înțelegem lumea din jur și să ne construim un viitor mai bun prin cunoștințe și abilități."
)

                    self.parent.add_data(
    "Cum ai explica ce este un chatbot unei persoane care nu știe nimic despre tehnologie?",
    "Un chatbot este un program care poate purta conversații cu oamenii și poate răspunde la întrebări folosind reguli sau informații învățate."
)

                    self.parent.add_data(
    "Ce înseamnă să ai o rutină zilnică bine organizată?",
    "O rutină bine organizată înseamnă să știi ce ai de făcut, când și cum, astfel încât să economisești timp și să reduci stresul."
)

                    self.parent.add_data(
    "De ce este sportul important pentru sănătatea fizică și mentală?",
    "Sportul ajută corpul să fie mai puternic, îmbunătățește starea de spirit și reduce riscul multor probleme de sănătate."
)

                    self.parent.add_data(
    "Cum ai descrie diferența dintre un calculator și un telefon inteligent?",
    "Calculatorul este mai potrivit pentru muncă complexă, iar telefonul inteligent este mai portabil și util pentru comunicare rapidă."
)

                    self.parent.add_data(
    "Ce înseamnă să fii motivat atunci când înveți ceva nou?",
    "A fi motivat înseamnă să ai dorința și energia de a continua să înveți chiar și atunci când lucrurile devin dificile."
)

                    self.parent.add_data(
    "De ce oamenii au emoții și cum ne influențează ele deciziile?",
    "Emoțiile ne ajută să reacționăm la situații și pot influența modul în care luăm decizii, uneori rațional, alteori impulsiv."
)

                    self.parent.add_data(
    "Cum explici ce este timpul dintr-o perspectivă simplă?",
    "Timpul este modul prin care măsurăm schimbările și ordinea evenimentelor din viața noastră."
)

                    self.parent.add_data(
    "Care este importanța somnului pentru funcționarea creierului?",
    "Somnul ajută creierul să se refacă, să proceseze informațiile și să funcționeze corect a doua zi."
)

                    self.parent.add_data(
    "Ce înseamnă să gândești logic atunci când rezolvi o problemă?",
    "Gândirea logică presupune să analizezi pașii, să cauți cauze și soluții fără a te baza doar pe emoții."
)

                    self.parent.add_data(
    "Cum ai descrie internetul cuiva care nu l-a folosit niciodată?",
    "Internetul este o rețea uriașă care conectează oameni și informații din toată lumea."
)

                    self.parent.add_data(
    "De ce este important să învățăm din greșeli?",
    "Greșelile ne arată ce nu a funcționat și ne ajută să devenim mai buni pe viitor."
)

                    self.parent.add_data(
    "Cum funcționează un algoritm explicat foarte simplu?",
    "Un algoritm este o listă de pași clari care trebuie urmați pentru a obține un rezultat corect."
)

                    self.parent.add_data(
    "Ce rol are disciplina în atingerea obiectivelor personale?",
    "Disciplina te ajută să continui chiar și atunci când motivația scade."
)

                    self.parent.add_data(
    "Cum ai descrie diferența dintre informație și cunoaștere?",
    "Informația este un fapt, iar cunoașterea apare atunci când înțelegi și aplici acea informație."
)

                    self.parent.add_data(
    "De ce este important să pui întrebări atunci când nu înțelegi ceva?",
    "Întrebările te ajută să clarifici lucrurile și să eviți confuziile."
)

                    self.parent.add_data(
    "Cum influențează tehnologia modul în care comunicăm?",
    "Tehnologia a făcut comunicarea mai rapidă, dar uneori mai puțin personală."
)

                    self.parent.add_data(
    "Ce înseamnă echilibrul între muncă și viața personală?",
    "Echilibrul înseamnă să ai timp atât pentru responsabilități, cât și pentru odihnă."
)

                    self.parent.add_data(
    "Cum ai explica ce este stresul într-un mod simplu?",
    "Stresul apare atunci când simți presiune sau prea multe cerințe într-un timp scurt."
)

                    self.parent.add_data(
    "De ce este important să ai obiective clare?",
    "Obiectivele clare îți oferă direcție și motivație."
)

                    self.parent.add_data(
    "Ce înseamnă să fii curios din punct de vedere intelectual?",
    "Curiozitatea intelectuală este dorința de a învăța și de a înțelege lucruri noi."
)

                    self.parent.add_data(
    "Cum funcționează memoria pe scurt?",
    "Memoria stochează informații și le folosește atunci când avem nevoie de ele."
)

                    self.parent.add_data(
    "De ce este importantă răbdarea în procesul de învățare?",
    "Răbdarea te ajută să continui chiar dacă progresul este lent."
)

                    self.parent.add_data(
    "Cum ai descrie ce este o decizie bună?",
    "O decizie bună este una luată după ce analizezi consecințele."
)

                    self.parent.add_data(
    "Ce înseamnă să fii responsabil?",
    "A fi responsabil înseamnă să îți asumi acțiunile și consecințele lor."
)

                    self.parent.add_data(
    "Cum influențează mediul în care trăiești comportamentul?",
    "Mediul poate influența obiceiurile, gândirea și starea emoțională."
)

                    self.parent.add_data(
    "Ce rol are exercițiul fizic în viața de zi cu zi?",
    "Exercițiul fizic menține corpul sănătos și mintea activă."
)

                    self.parent.add_data(
    "De ce este important să îți cunoști punctele forte?",
    "Punctele forte te ajută să îți alegi direcția potrivită."
)

                    self.parent.add_data(
    "Cum ai descrie procesul de învățare continuă?",
    "Învățarea continuă înseamnă să te dezvolți pe tot parcursul vieții."
)

                    self.parent.add_data(
    "Ce înseamnă să fii organizat?",
    "A fi organizat înseamnă să îți gestionezi eficient timpul și resursele."
)

                    self.parent.add_data(
    "Cum explici ce este un obicei?",
    "Un obicei este un comportament repetat care devine automat."
)

                    self.parent.add_data(
    "De ce este importantă comunicarea clară?",
    "Comunicarea clară reduce neînțelegerile și conflictele."
)

                    self.parent.add_data(
    "Ce înseamnă să îți asumi un risc calculat?",
    "Un risc calculat este luat după ce analizezi avantajele și dezavantajele."
)

                    self.parent.add_data(
    "Cum ai descrie ce este succesul?",
    "Succesul înseamnă atingerea obiectivelor personale."
)

                    self.parent.add_data(
    "De ce este important feedback-ul?",
    "Feedback-ul te ajută să vezi ce poți îmbunătăți."
)

                    self.parent.add_data(
    "Cum influențează atitudinea rezultatele?",
    "O atitudine pozitivă poate îmbunătăți performanța."
)

                    self.parent.add_data(
    "Ce înseamnă să fii consecvent?",
    "Consecvența înseamnă să continui fără a renunța."
)

                    self.parent.add_data(
    "Cum explici ce este adaptabilitatea?",
    "Adaptabilitatea este capacitatea de a te ajusta schimbărilor."
)

                    self.parent.add_data(
    "De ce este important să îți gestionezi timpul?",
    "Gestionarea timpului te ajută să fii mai eficient."
)

                    self.parent.add_data(
    "Ce înseamnă să fii atent la detalii?",
    "Atenția la detalii reduce greșelile."
)

                    self.parent.add_data(
                    "Cum ai descrie ce este încrederea în sine?",
                    "Încrederea în sine înseamnă să crezi în propriile abilități."
                    )
                
                    self.parent.add_data(
    "Poți să explici detaliat de ce este important să avem grijă de sănătatea noastră fizică și mentală pe termen lung?",
    "Grija pentru sănătatea fizică și mentală este esențială deoarece corpul și mintea funcționează împreună. Activitatea fizică regulată, alimentația echilibrată și odihna ajută corpul să rămână puternic, iar gestionarea stresului și emoțiilor contribuie la o stare mentală stabilă, ceea ce ne permite să luăm decizii mai bune și să avem o viață mai echilibrată."
)

                    self.parent.add_data(
    "Cum ai descrie procesul de învățare al unui om, de la primele cunoștințe până la nivel avansat?",
    "Procesul de învățare începe de obicei cu informații simple, apoi continuă prin repetiție, exercițiu și aplicare practică. Pe măsură ce o persoană acumulează experiență, învață să facă legături între concepte, să gândească critic și să folosească cunoștințele pentru a rezolva probleme din ce în ce mai complexe."
)

                    self.parent.add_data(
    "Explică pe larg ce este inteligența artificială și cum poate influența viitorul societății.",
    "Inteligența artificială este un domeniu al tehnologiei care se ocupă cu crearea de sisteme capabile să învețe din date și să ia decizii. În viitor, aceasta poate automatiza sarcini repetitive, poate ajuta în medicină, educație și transport, dar ridică și întrebări legate de etică, locuri de muncă și responsabilitate."
)

                    self.parent.add_data(
    "De ce este important să avem obiective clare în viață și cum ne ajută acestea pe termen lung?",
    "Obiectivele clare oferă direcție și sens acțiunilor noastre zilnice. Ele ne ajută să ne organizăm timpul, să ne păstrăm motivația și să evaluăm progresul. Pe termen lung, obiectivele bine definite contribuie la dezvoltarea personală și la satisfacția de a vedea rezultate concrete."
)

                    self.parent.add_data(
    "Cum ai explica diferența dintre a avea informații și a avea înțelepciune?",
    "A avea informații înseamnă să cunoști fapte și date, în timp ce înțelepciunea presupune să înțelegi cum și când să folosești acele informații. Înțelepciunea apare prin experiență, reflecție și capacitatea de a lua decizii echilibrate."
)

                    self.parent.add_data(
    "Poți descrie pe larg cum influențează tehnologia relațiile dintre oameni?",
    "Tehnologia a schimbat modul în care oamenii comunică, permițând conversații rapide la distanță mare. Totuși, deși facilitează conexiunile, poate reduce interacțiunile față în față și poate crea dependență, motiv pentru care este important să existe un echilibru în utilizarea ei."
)

                    self.parent.add_data(
    "Explică importanța eșecului în procesul de dezvoltare personală și profesională.",
    "Eșecul este o parte normală a învățării și dezvoltării. Prin eșec, o persoană înțelege ce nu a funcționat, își poate ajusta strategia și își dezvoltă reziliența. Fără eșecuri, progresul ar fi mult mai lent și superficial."
)

                    self.parent.add_data(
    "Cum ai descrie rolul disciplinei în atingerea performanței într-un domeniu dificil?",
    "Disciplina este capacitatea de a continua munca chiar și atunci când motivația scade. În domeniile dificile, disciplina ajută la formarea obiceiurilor corecte, la menținerea consecvenței și la obținerea rezultatelor pe termen lung."
)

                    self.parent.add_data(
    "Ce înseamnă să fii adaptabil și de ce este această abilitate tot mai importantă în prezent?",
    "Adaptabilitatea este capacitatea de a te ajusta rapid la schimbări. Într-o lume care evoluează constant, această abilitate permite oamenilor să învețe lucruri noi, să facă față situațiilor neprevăzute și să rămână relevanți în mediul profesional și social."
)

                    self.parent.add_data(
    "Cum ai explica sensul dezvoltării personale și de ce oamenii aleg să se îmbunătățească constant?",
    "Dezvoltarea personală reprezintă procesul prin care o persoană își îmbunătățește abilitățile, mentalitatea și comportamentul. Oamenii aleg acest drum pentru a avea o viață mai echilibrată, pentru a-și atinge potențialul și pentru a se adapta mai bine provocărilor vieții."
)

                    self.parent.add_data(
    "Poți să numeri de la 1 până la 10 și să explici ce observi la aceste numere?",
    "Sigur. Numărând de la 1 până la 10 obținem următoarea succesiune: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. Observăm că fiecare număr crește cu 1 față de cel anterior, iar toate sunt numere naturale folosite frecvent în calcule simple."
)

                    self.parent.add_data(
    "Numără de la 5 până la 15 și spune câte numere sunt în total.",
    "Dacă numărăm de la 5 până la 15, obținem: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15. În total sunt 11 numere, deoarece le includem atât pe 5, cât și pe 15."
)

                    self.parent.add_data(
    "Poți să numeri descrescător de la 20 până la 10?",
    "Da. Numărarea descrescătoare de la 20 până la 10 este: 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10. La fiecare pas scădem câte 1 din numărul anterior."
)

                    self.parent.add_data(
    "Numără din 2 în 2 de la 0 până la 20 și explică ce tip de numere sunt.",
    "Numărând din 2 în 2 de la 0 până la 20 obținem: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Acestea sunt numere pare, deoarece se împart exact la 2."
)

                    self.parent.add_data(
    "Poți să numeri din 5 în 5 de la 5 până la 50?",
    "Sigur. Numărarea din 5 în 5 de la 5 până la 50 este: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. Observăm că fiecare număr este multiplu de 5."
)

                    self.parent.add_data(
    "Calculează 12 + 8 și explică pașii calculați.",
    "Pentru a calcula 12 + 8, adunăm 8 la 12. Putem vedea că 12 + 8 = 20, deoarece mai adăugăm 8 unități la cele 12 existente."
)

                    self.parent.add_data(
    "Rezolvă calculul 30 - 17 și explică rezultatul.",
    "Pentru calculul 30 - 17, scădem 17 din 30. Mai întâi scădem 10 și rămânem cu 20, apoi mai scădem 7 și obținem rezultatul final 13."
)

                    self.parent.add_data(
    "Calculează 6 × 7 și spune ce reprezintă acest calcul.",
    "Calculul 6 × 7 înseamnă să adunăm de 7 ori numărul 6 sau invers. Rezultatul este 42, care reprezintă produsul celor două numere."
)

                    self.parent.add_data(
    "Rezolvă împărțirea 40 ÷ 5 și explică ce înseamnă.",
    "Împărțirea 40 ÷ 5 înseamnă să vedem de câte ori încape 5 în 40. Rezultatul este 8, deoarece 5 × 8 = 40."
)

                    self.parent.add_data(
    "Numără de la 1 până la 100 din 10 în 10 și spune ce observi.",
    "Numărând de la 1 până la 100 din 10 în 10 obținem: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. Observăm că toate numerele se termină în 0 și sunt multipli ai lui 10."
)
                
                    self.parent.add_data(
    "salut SALUT Salut",
    "Salut! Indiferent cum este scris, mesajul tău pare un salut, așa că îți răspund cu plăcere."
)

                    self.parent.add_data(
    "lol",
    "Mesajul tău exprimă amuzament. Dacă vrei să continui conversația, poți spune ce te-a făcut să râzi."
)

                    self.parent.add_data(
    "cf",
    "Presupun că întrebi ce fac. Sunt aici și gata să te ajut cu orice întrebare ai."
)

                    self.parent.add_data(
    "nu",
    "Am înțeles răspunsul tău negativ. Dacă vrei, poți oferi mai multe detalii ca să continui conversația."
)

                    self.parent.add_data(
    "ahh ah aH Ah AH",
    "Mesajul tău pare o reacție emoțională sau spontană. Spune-mi ce s-a întâmplat."
)

                    self.parent.add_data(
    "?????",
    "Pare că ești confuz sau surprins. Dacă ai o întrebare clară, încearcă să o formulezi."
)

                    self.parent.add_data(
    "......",
    "Tăcerea sau pauza poate însemna multe lucruri. Sunt aici când ești pregătit să continui."
)

                    self.parent.add_data(
    "asdfghjkl",
    "Acest mesaj pare tastat aleatoriu. Dacă a fost o greșeală, nu-i nimic, putem continua."
)

                    self.parent.add_data(
    "sex",
    "Cuvântul se referă de obicei la diferențele biologice sau la educația despre reproducere. Dacă ai o întrebare informativă, pot ajuta."
)

                    self.parent.add_data(
    "😂😂😂",
    "Se pare că te distrezi. Dacă vrei să împărtășești contextul, sunt aici să răspund."
)
                
                    self.parent.add_data(
    "Salut",
    "Salut! Mă bucur să te văd aici. Spune-mi cu ce te pot ajuta."
)

                    self.parent.add_data(
    "Bună",
    "Bună! Sunt aici și gata să vorbim despre orice subiect te interesează."
)

                    self.parent.add_data(
    "Hey",
    "Hey! Sper că ai o zi bună. Cu ce vrei să începem?"
)

                    self.parent.add_data(
    "Salutare",
    "Salutare! Conexiunea a fost stabilită cu succes. Cum te pot ajuta?"
)

                    self.parent.add_data(
    "Bună ziua",
    "Bună ziua! Sunt disponibil pentru întrebări, explicații sau discuții libere."
)

                    self.parent.add_data(
    "Neața",
    "Neața! Sper că ziua ta începe bine. Spune-mi ce ai nevoie."
)

                    self.parent.add_data(
    "Hello",
    "Hello! Chiar dacă e în engleză, salutul a fost înțeles. Cum te pot ajuta?"
)

                    self.parent.add_data(
    "Yo",
    "Yo! Salut informal detectat. Sunt aici pentru conversație sau ajutor."
)

                    self.parent.add_data(
    "Salut chatbot",
    "Salut! Da, eu sunt chatbotul. Cu ce te pot ajuta azi?"
)

                    self.parent.add_data(
    "Bună, e cineva aici?",
    "Da, sunt aici. Putem începe conversația oricând."
)
                
                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să iei o decizie importantă foarte rapid, ce ai face?",
    "Aș încerca să mă concentrez pe informațiile esențiale, să evaluez rapid opțiunile și să aleg varianta cu cele mai puține riscuri pe termen scurt."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care nu înțelegi o problemă, dar trebuie să o rezolvi, ce ai face?",
    "Aș începe prin a descompune problema în părți mai mici și aș clarifica ce știu deja, apoi aș căuta informațiile lipsă."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care ai făcut o greșeală, ce ai face mai departe?",
    "Aș recunoaște greșeala, aș analiza ce a mers prost și aș încerca să învăț din ea pentru a evita repetarea situației."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care cineva îți cere ajutorul, dar nu ești sigur de răspuns, ce ai face?",
    "Aș spune sincer că nu sunt sigur, apoi aș încerca să caut o soluție sau să ofer informații utile, chiar dacă nu sunt complete."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să înveți ceva complet nou într-un timp scurt, ce ai face?",
    "Aș prioritiza conceptele de bază, aș exersa practic și aș evita să mă pierd în detalii inutile la început."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care te confrunți cu o problemă dificilă și stresantă, ce ai face?",
    "Aș lua o pauză scurtă pentru a-mi clarifica gândurile, apoi aș aborda problema pas cu pas, fără să mă grăbesc inutil."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care ai mai multe opțiuni bune și nu știi ce să alegi, ce ai face?",
    "Aș compara avantajele și dezavantajele fiecărei opțiuni și aș alege varianta care se potrivește cel mai bine scopului final."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care cineva nu este de acord cu tine, ce ai face?",
    "Aș încerca să înțeleg punctul de vedere al celeilalte persoane și aș discuta calm, fără a transforma conversația într-un conflict."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să explici ceva complicat unei persoane începătoare, ce ai face?",
    "Aș folosi exemple simple, limbaj clar și aș verifica dacă informația a fost înțeleasă înainte de a continua."
)

                    self.parent.add_data(
    "Dacă ai fi în situația în care trebuie să îți organizezi timpul mai bine, ce ai face?",
    "Aș stabili priorități clare, aș crea un plan realist și aș elimina activitățile care nu aduc valoare."
)

                    self.parent.add_data(
    "Ce ai face dacă ai vedea o persoană tristă în drum spre școală?",
    "Aș încerca să fiu atent la starea ei, să ofer un zâmbet sau un cuvânt de încurajare și, dacă este necesar, să o ajut să găsească sprijinul potrivit."
)

                    self.parent.add_data(
    "Dacă ai fi într-un parc și ai vedea un animal rănit, ce ai face?",
    "Aș observa cu atenție animalul fără a-l speria, apoi aș încerca să contactez un veterinar sau un adăpost de animale pentru ajutor profesionist."
)

                    self.parent.add_data(
    "Ce ai face dacă ai fi blocat într-un lift cu alte persoane?",
    "Aș păstra calmul, aș comunica cu ceilalți pentru a ne liniști și apoi aș suna la serviciul de urgență pentru a primi instrucțiuni corecte."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că se simte foarte confuz, cum ai răspunde?",
    "Aș încerca să ascult cu atenție, să clarific ce anume îi creează confuzie și să ofer explicații pas cu pas, fără a judeca."
)

                    self.parent.add_data(
    "Cum ai explica unui copil cum să numere până la 20 folosind degetele?",
    "Aș arăta cum să ridice fiecare deget pe rând și să spună numărul corespunzător, astfel încât să înțeleagă vizual succesiunea și să exerseze memoria numerică."
)

                    self.parent.add_data(
    "Dacă ai vedea un copac căzut pe drum, ce ai face?",
    "Aș evalua dacă există pericol pentru oameni sau mașini, aș avertiza persoanele din apropiere și, dacă este sigur, aș căuta ajutor pentru a elibera drumul."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că e fericit, ce ai răspunde?",
    "Mă bucur să aud asta! Fericirea este importantă și mă întreb ce anume îi aduce bucurie, pentru a continua conversația pozitivă."
)

                    self.parent.add_data(
    "Dacă trebuie să împarți 24 de mere între 6 prieteni, cum ai proceda?",
    "Împărțind 24 de mere la 6 persoane, fiecare primește 4 mere, pentru că 24 ÷ 6 = 4. Este un mod corect și echitabil."
)

                    self.parent.add_data(
    "Ce ai face dacă ar începe să plouă puternic când ești afară fără umbrelă?",
    "Aș căuta rapid un adăpost, aș proteja obiectele personale și aș încerca să ajung în siguranță într-un loc uscat cât mai repede posibil."
)

                    self.parent.add_data(
    "Dacă cineva îți spune că nu știe ce să facă într-o zi plictisitoare, ce ai sugera?",
    "Aș sugera activități creative sau productive, cum ar fi cititul unei cărți, învățarea unei abilități noi sau o plimbare în aer liber, astfel încât să transforme timpul liber într-un mod plăcut și util."
)
                
                    self.parent.add_data("Salut, ce faci?", "Salut frate, eu sunt bine, tu?")
                    self.parent.add_data("Ce este revelionul?", "Revelionul este sărbătoarea în care ne bucurăm că trecem în noul an (ex. 2025 -> 2026). Se ține în fiecare an pe 1 ianuarie.")
                    self.parent.add_data("Zi-mi, într-un mod simplist și minimalist, componentele principale pe care le are un sistem PC", "Procesorul, placa video, placa de bază, HDD sau SSD, plăcuțele sau plăcuța de RAM, sursa de curent, carcasa.")
                    self.parent.add_data("Zi-mi componentele principale pe care le are un sistem PC", "Un sistem PC are mai multe componente principale, acestea fiind: procesorul (CPU), placa video (GPU), placa de bază (Motherboard), HDD sau SSD, plăcuțele sau plăcuța de RAM (RAM), sursa de curent (PSU) și carcasa.")
                    self.parent.add_data("Care este bucuria copiilor de crăciun?", "Bucuria principală a copiilor de crăciun sunt Moș Crăciun și momentele când se pun cadourile sub bradul de crăciun.")

                    self.parent.add_data("Cine este Moș Crăciun?", "Moș Crăciun este un personaj gras, cu barbă albă și bun, adorat de copii. El, se zice că vine cu sania și renii lui în toată lumea pentru a împărți cadouri la copii fix în ziua de Crăciun.")
                    self.parent.add_data("Cine este Spiderman", "Spiderman, dacă vorbim de personajul din Marvel, Spiderman este un personaj animat, făcând parte, de obicei, în filme sau desene de acțiune.")
                    self.parent.add_data("Ce este un mouse pentru laptop sau desktop?", "Un mouse este un obiect care se conectează la laptop prin fir sau wireless, folosit pentru a mișca couser-ul de pe ecran")
                    self.parent.add_data("Care este diferența dintre guma de mestecat și guma de șters?", "Diferența dintre ele este chiar mare: cu guma de șters ștergi scrisul de creion de pe foaie, iar guma de mestecat o poți băga în gură, după care să o mesteci")
                    self.parent.add_data("Continuă seria cu încă 3 exemple: 1, 2, 3, ...", "Deci, numeri aici crescător, nu? Deci următoarele 3 exemple ar fi 4, 5 și 6.")

                    self.parent.add_data("Cum pot să-mi dezvolt gândirea critică în era dezinformării online?", "Dezvoltarea gândirii critice începe cu practicarea scepticismului sănătos și verificarea riguroasă a surselor de informație. Atunci când întâlnești o știre care îți provoacă o reacție emoțională puternică, este esențial să te oprești și să cauți sursa originală a datelor. Întreabă-te cine a scris articolul, ce interese ar putea avea și dacă informația este susținută de alte publicații de încredere. De asemenea, este util să consulți site-uri de fact-checking și să încerci să înțelegi perspectivele opuse pentru a identifica erorile de logică, cum ar fi atacul la persoană sau generalizarea pripită, evitând astfel bulele de filtrare create de algoritmi.")
                    self.parent.add_data("Explică conceptul de 'împletire cuantică' (quantum entanglement) pe înțelesul tuturor.", "Împletirea cuantică este un fenomen fascinant în care două sau mai multe particule devin conectate într-un mod în care starea uneia depinde instantaneu de starea celeilalte, indiferent de distanța uriașă care le desparte. Dacă măsurăm o proprietate a unei particule împletite, cum ar fi spinul, vom ști automat și instantaneu starea corespunzătoare a partenerului său. Albert Einstein a numit acest fenomen 'acțiune înfricoșătoare la distanță' deoarece pare să contrazică limita vitezei luminii. În realitate, nu se transmite informație clasică mai repede decât lumina, dar corelația cuantică rămâne unul dintre pilonii fundamentali pentru dezvoltarea calculatoarelor cuantice și a criptografiei securizate a viitorului.")
                    self.parent.add_data("Care este importanța rezilienței emoționale și cum poate fi ea cultivată?", "Reziliența emoțională reprezintă capacitatea psihică de a te adapta și de a-ți reveni după experiențe adverse, traume sau perioade de stres intens. Nu înseamnă că nu vei simți durere sau dificultate, ci că ai resursele interioare necesare pentru a merge mai departe fără a fi distrus de ele. Cultivarea rezilienței implică dezvoltarea unei rețele de suport social, menținerea unei perspective optimiste dar realiste și practicarea autocompasiunii. Este esențial să accepți că schimbarea face parte din viață și să te concentrezi pe aspectele pe care le poți controla, transformând provocările în oportunități de învățare și creștere personală.")
                    self.parent.add_data("Ce ne învață filosofia stoică despre gestionarea anxietății moderne?", "Filosofia stoică ne învață că rădăcina anxietății noastre stă adesea în încercarea de a controla lucruri care nu depind de noi, cum ar fi opiniile altora, trecutul sau evenimentele imprevizibile ale viitorului. Soluția oferită de stoici, precum Epictet sau Marcus Aurelius, este 'dihotomia controlului': trebuie să investim energie doar în propriile noastre gânduri, valori și acțiuni. Practicând 'premeditatio malorum' (vizualizarea unor posibile dificultăți) și acceptând că universul este într-o continuă schimbare, putem atinge o stare de liniște interioară numită ataraxie. Stoicismul nu înseamnă suprimarea emoțiilor, ci transformarea lor prin rațiune, astfel încât să nu mai fim sclavi ai circumstanțelor externe.")
                    self.parent.add_data("Cine a fost Albert Einstein și de ce teoria lui a revoluționat fizica?", "Albert Einstein a fost un fizician teoretician de origine germană, considerat unul dintre cei mai mari oameni de știință ai tuturor timpurilor. El a revoluționat înțelegerea noastră asupra universului prin Teoria Relativității. Relativitatea restrânsă a introdus conceptul că timpul și spațiul sunt legate într-un continuum numit spațiu-timp și că masa poate fi transformată în energie conform celebrei ecuații E=mc^2. Ulterior, Relativitatea generală a explicat gravitația nu ca pe o forță invizibilă, ci ca pe o curbură a spațiu-timpului cauzată de prezența masei. Această viziune a schimbat complet cosmologia, explicând fenomene precum orbita planetelor, găurile negre și expansiunea universului.")
                    self.parent.add_data("De ce este personajul Joker considerat unul dintre cei mai complecși antagoniști?", "Joker este un personaj fascinant deoarece reprezintă antiteza perfectă a ordinii și a logicii, fiind o personificare a nihilismului și a haosului pur. Spre deosebire de alți răufăcători care caută bogăție sau putere, Joker dorește adesea doar să demonstreze că moralitatea umană este o fațadă fragilă care se prăbușește în condiții de presiune extremă. Complexitatea sa provine din ambiguitatea originilor sale și din inteligența sa sclipitoare folosită în scopuri distructive. Interpretările sale, de la anarhistul filozofic al lui Heath Ledger la omul marginalizat și bolnav psihic al lui Joaquin Phoenix, au transformat personajul într-un simbol al eșecurilor sistemice ale societății și ale fragilității minții umane.")
                    self.parent.add_data("Ce definește stilul muzical Jazz și care sunt elementele sale cheie?", "Muzica Jazz este definită în primul rând prin libertatea de exprimare și improvizație, fiind un gen care a apărut la intersecția culturilor africane și europene în New Orleans. Elementele sale cheie includ swing-ul (un ritm specific care dă senzația de balans), utilizarea notelor 'blue' (care adaugă o tentă melancolică sau expresivă) și poliritmia. Într-o interpretare de jazz, muzicienii comunică între ei în timp real, oferind solo-uri spontane pe baza unei structuri armonice prestabilite. Această capacitate de a reinventa o piesă la fiecare interpretare face ca jazz-ul să fie considerat 'muzică clasică a Americii', influențând major genuri precum rock, pop și hip-hop prin complexitatea sa teoretică.")
                    self.parent.add_data("Care este impactul stilului Heavy Metal asupra culturii și fanilor săi?", "Heavy Metal-ul este mai mult decât un gen muzical caracterizat prin distorsiune, ritmuri rapide și voci puternice; este o subcultură globală care promovează un sentiment de comunitate și rezistență în fața normelor sociale convenționale. Deși a fost adesea criticat pentru agresivitatea sa aparentă, studiile arată că fanii genului găsesc în această muzică un debușeu terapeutic pentru furie și frustrare, obținând o stare de calm și apartenență. Temele abordate, de la mitologie și istorie la critici sociale și lupte interioare, oferă o profunzime intelectuală care creează o legătură extrem de loială între artiști și public, transformând concertele în experiențe ritualice de eliberare emoțională.")
                    self.parent.add_data("Cum funcționează economia circulară și de ce este necesară astăzi?", "Economia circulară este un model de producție și consum care implică partajarea, închirierea, reutilizarea, repararea, renovarea și reciclarea materialelor și produselor existente cât mai mult posibil. Spre deosebire de modelul liniar tradițional 'ia-fă-aruncă', economia circulară vizează extinderea ciclului de viață al produselor și reducerea la minimum a deșeurilor. Acest sistem este esențial în contextul actual deoarece resursele naturale sunt finite, iar presiunea asupra mediului cauzată de poluare și schimbările climatice necesită o transformare radicală. Prin implementarea designului circular, companiile pot crea produse mai durabile și ușor de reciclat, generând în același timp noi oportunități economice și protejând biodiversitatea planetei.")
                    self.parent.add_data("Care este rolul eticii în dezvoltarea sistemelor de inteligență artificială?", "Etica în inteligența artificială are rolul de a asigura că aceste tehnologii sunt dezvoltate și utilizate în moduri care respectă drepturile omului, echitatea și transparența. Deoarece algoritmii de IA sunt antrenați pe seturi de date care pot reflecta prejudecăți umane, există riscul ca aceștia să perpetueze sau să amplifice discriminarea în domenii precum angajarea sau justiția. O abordare etică presupune implementarea unor mecanisme de responsabilitate (accountability), protejarea vieții private a utilizatorilor și asigurarea faptului că deciziile luate de mașini pot fi explicate și verificate de oameni. Fără un cadru etic solid, avansul tehnologic ar putea duce la pierderea încrederii publice și la consecințe sociale imprevizibile sau dăunătoare.")
                    self.parent.add_data("Ce a fost Renașterea și cum a schimbat viziunea asupra lumii?", "Renașterea a fost o perioadă de efervescență culturală, artistică și științifică care a început în Italia în secolul al XIV-lea și s-a răspândit în întreaga Europă, marcând tranziția de la Evul Mediu la modernitate. Esența sa a fost umanismul, o mișcare care a mutat accentul de pe divinitate și dogmă pe potențialul, rațiunea și experiența umană. Artiști precum Leonardo da Vinci și Michelangelo au revoluționat artele plastice prin studierea anatomiei și a perspectivei, în timp ce gânditori precum Copernic au provocat viziunea geocentrică asupra universului. Renașterea a redescoperit valorile antichității clasice și a pus bazele metodei științifice moderne, încurajând curiozitatea intelectuală și explorarea geografică.")
                    self.parent.add_data("Cum pot fi gestionate eficient conflictele într-o echipă de lucru?", "Gestionarea eficientă a conflictelor începe cu recunoașterea faptului că dezacordurile sunt naturale și pot fi chiar benefice dacă sunt abordate constructiv. Primul pas este ascultarea activă a tuturor părților implicate, fără a judeca sau a întrerupe, pentru a înțelege nevoile și motivațiile din spatele pozițiilor adoptate. Este crucial să se atace problema, nu persoana, și să se caute puncte de interes comune în loc de divergențe. Utilizarea tehnicilor de comunicare non-violentă și medierea de către o persoană neutră pot ajuta la găsirea unor soluții de tip 'win-win'. Un conflict rezolvat corect poate duce la o mai bună coeziune a grupului, la idei inovatoare și la o atmosferă de lucru bazată pe încredere și respect reciproc.")
                    self.parent.add_data("Care este impactul încălzirii globale asupra ecosistemelor marine?", "Încălzirea globală are consecințe devastatoare asupra oceanelor, incluzând creșterea temperaturii apei, acidificarea și ridicarea nivelului mării. Absorbția excesului de dioxid de carbon din atmosferă face apele mai acide, ceea ce împiedică organismele precum coralii și moluștele să își formeze cochiliile sau scheletele de calcar. Albirea recifelor de corali duce la pierderea biodiversității, deoarece acestea adăpostesc un sfert din speciile marine. De asemenea, speciile migrează spre poli în căutarea apelor mai reci, perturbând lanțurile trofice locale și afectând comunitățile umane care depind de pescuit. Topirea ghețarilor nu doar ridică nivelul mării, dar schimbă și salinitatea apei, putând altera curenții oceanici care reglează clima globală.")
                    self.parent.add_data("Explicați importanța somnului pentru funcțiile cognitive și sănătatea fizică.", "Somnul nu este o stare pasivă, ci un proces biologic activ esențial pentru restabilirea funcțiilor fizice și mentale. În timpul somnului profund și al etapei REM, creierul procesează informațiile acumulate în timpul zilei, consolidează memoria pe termen lung și elimină toxinele metabolice acumulate. Lipsa cronică de somn afectează concentrarea, capacitatea de luare a deciziilor și reglarea emoțională, crescând riscul de depresie și anxietate. Din punct de vedere fizic, somnul insuficient este legat de un sistem imunitar slăbit, inflamație cronică, boli cardiovasculare și dezechilibre hormonale care pot duce la obezitate. Respectarea unui ritm circadian stabil este, prin urmare, unul dintre cei mai importanți piloni ai unei vieți lungi și sănătoase.")
                    self.parent.add_data("Cine este Elon Musk și cum a influențat el transportul modern și explorarea spațială?", "Elon Musk este un antreprenor vizionar și inginer auto-didact, cunoscut pentru fondarea sau conducerea unor companii de avangardă precum Tesla, SpaceX și Neuralink. Prin Tesla, el a forțat întreaga industrie auto să accelereze tranziția către vehicule electrice, demonstrând că acestea pot fi performante și dezirabile. Cu SpaceX, Musk a revoluționat explorarea spațială prin dezvoltarea rachetelor reutilizabile, reducând drastic costurile lansărilor pe orbită și redeschizând calea către colonizarea planetei Marte. Deși este o figură controversată din cauza stilului său de comunicare și a viziunilor sale radicale, impactul său asupra tehnologiei sustenabile și a ambițiilor interplanetare ale omenirii este incontestabil, schimbând paradigma în multiple sectoare industriale simultan.")
                    self.parent.add_data("Ce este muzica de tip Synthwave și ce elemente nostalgice folosește?", "Synthwave este un gen muzical electronic modern care se inspiră profund din cultura pop a anilor '80, utilizând sintetizatoare analogice pentru a crea o atmosferă retro-futuristă. Muzica evocă adesea coloanele sonore ale filmelor de acțiune și science-fiction din acea epocă, folosind ritmuri de tobe cu mult reverb și linii de bas pulsante. Estetica vizuală asociată, plină de culori neon (roz și albastru), mașini sport clasice și apusuri de soare digitale, completează experiența auditivă. Deși este un gen nou, Synthwave se bazează pe nostalgia pentru o versiune idealizată a trecutului, fiind popularizat recent prin seriale și jocuri care omagiază decada optzecistă, oferind ascultătorilor o evadare într-o lume digitală melancolică.")
                    self.parent.add_data("Care sunt principiile fundamentale ale democrației și de ce este ea fragilă?", "Democrația se bazează pe principii fundamentale precum suveranitatea poporului, statul de drept, separarea puterilor în stat și respectarea drepturilor și libertăților individuale. Într-o democrație funcțională, puterea este limitată prin legi, iar cetățenii participă la decizii prin vot liber și informat. Cu toate acestea, democrația este fragilă deoarece depinde de încrederea cetățenilor în instituții și de respectarea normelor nescrise ale dialogului civil. Ea poate fi subminată de polarizarea extremă, dezinformare, corupție sau apatie civică. Protejarea democrației necesită un angajament constant din partea societății pentru educație, transparență și protejarea minorităților, amintindu-ne că libertatea nu este un dat, ci un proces care trebuie apărat activ.")
                    self.parent.add_data("De ce este importantă biodiversitatea pentru stabilitatea ecosistemelor?", "Biodiversitatea reprezintă varietatea tuturor formelor de viață de pe Pământ și este esențială deoarece fiecare specie, oricât de mică, joacă un rol specific într-un ecosistem. Această diversitate funcționează ca o plasă de siguranță: cu cât un ecosistem are mai multe specii care îndeplinesc funcții similare (cum ar fi polenizarea sau descompunerea), cu atât este mai rezistent la șocuri precum bolile sau schimbările climatice. Pierderea unei singure specii poate declanșa un efect de domino, ducând la colapsul întregului sistem. Pentru oameni, biodiversitatea asigură resurse vitale: alimente, medicamente, aer curat și apă potabilă. Protejarea ei nu este doar un act moral, ci o necesitate pragmatică pentru supraviețuirea economiei și a sănătății umane.")
                    self.parent.add_data("Cum a influențat Marie Curie parcursul femeilor în știință?", "Marie Curie a fost o pionieră absolută, fiind prima femeie din Europa care a obținut un doctorat în științe și prima femeie care a câștigat un Premiu Nobel. Într-o epocă în care universitățile erau aproape exclusiv masculine, ea a demonstrat o tenacitate incredibilă, descoperind radioactivitatea și elementele radiu și poloniu. Prin munca sa, ea nu doar că a deschis drumul pentru tratamentele moderne împotriva cancerului, dar a și dărâmat barierele de gen din mediul academic. Succesul ei a servit drept inspirație pentru generații întregi de fete, demonstrând că geniul și rigoarea științifică nu au gen. Moștenirea sa continuă să fie un simbol al luptei pentru egalitate de șanse în cercetare și educație.")
                    self.parent.add_data("Ce este muzica Lo-fi și cum ajută la concentrare și relaxare?", "Muzica Lo-fi (Low Fidelity) este un gen care îmbrățișează imperfecțiunile tehnice, cum ar fi zgomotul de fond, sunetul de ploaie sau foșnetul discurilor de vinil, combinându-le cu ritmuri de hip-hop lente și relaxante. Acest stil muzical a devenit extrem de popular în mediul online ca fundal pentru studiu și muncă. Efectul său benefic asupra concentrării provine din natura sa previzibilă și non-intruzivă; lipsa versurilor și ritmul constant ajută creierul să intre în starea de 'flow', blocând zgomotele exterioare perturbatoare fără a solicita atenția activă a ascultătorului. De asemenea, atmosfera caldă și melancolică a muzicii Lo-fi reduce nivelul de cortizol, promovând o stare de calm necesară în perioadele de stres intelectual.")
                    self.parent.add_data("Explicați importanța alfabetizării financiare în viața de adult.", "Alfabetizarea financiară reprezintă capacitatea de a înțelege și de a utiliza eficient diverse abilități financiare, inclusiv gestionarea bugetului personal, investițiile și înțelegerea mecanismelor de creditare. Într-o lume economică tot mai complexă, lipsa acestor cunoștințe poate duce la datorii nesustenabile, stres și incapacitatea de a economisi pentru viitor. O persoană educată financiar știe să facă diferența între active (lucruri care îți aduc bani) și pasive (lucruri care îți consumă bani), înțelege puterea dobânzii compuse și riscurile inflației. Această competență oferă nu doar securitate materială, ci și libertatea de a lua decizii informate care să permită atingerea obiectivelor pe termen lung, cum ar fi achiziționarea unei locuințe sau asigurarea unei pensii confortabile.")
                    self.parent.add_data("Cum funcționează memoria de scurtă durată față de cea de lungă durată?", "Memoria de scurtă durată, numită adesea memorie de lucru, este capacitatea creierului de a reține și manipula o cantitate mică de informație pentru o perioadă foarte scurtă, de obicei între 15 și 30 de secunde. Este esențială pentru sarcini imediate, cum ar fi reținerea unui număr de telefon până îl notezi. Memoria de lungă durată, pe de altă parte, este un sistem de stocare aproape nelimitat unde informațiile sunt păstrate pentru zile, ani sau chiar întreaga viață. Trecerea informațiilor de la una la alta se face prin procesul de consolidare, care necesită atenție, repetiție și, foarte important, somn. În timp ce memoria de lucru este fragilă și ușor de perturbat, memoria de lungă durată este stocată prin schimbări structurale la nivelul sinapselor neuronale, formând rețele complexe de asocieri.")
                    self.parent.add_data("Care sunt avantajele și dezavantajele lucrului de acasă (remote work)?", "Lucrul de acasă oferă avantaje majore, cum ar fi flexibilitatea programului, eliminarea timpului pierdut în trafic și economii financiare legate de transport. Această autonomie poate crește satisfacția angajatului și poate îmbunătăți echilibrul dintre viața profesională și cea personală. Totuși, există și dezavantaje semnificative, cum ar fi dificultatea de a separa clar timpul de muncă de cel de odihnă, riscul de izolare socială și scăderea calității comunicării spontane între colegi. Pentru mulți, lipsa unui spațiu dedicat muncii poate duce la scăderea productivității sau la epuizare (burnout). Succesul muncii remote depinde de disciplina personală, de utilizarea instrumentelor digitale de colaborare și de efortul conștient al companiilor de a menține cultura organizațională și conexiunea umană.")
                    self.parent.add_data("Cine a fost Audrey Hepburn și ce a lăsat în urmă dincolo de cariera de actriță?", "Audrey Hepburn a fost o figură legendară a cinematografiei mondiale, premiată cu Oscar pentru rolul din 'Vacanță la Roma', dar moștenirea ei cea mai profundă este cea umanitară. După ce s-a retras din lumina reflectoarelor, ea și-a dedicat restul vieții organizației UNICEF, fiind numită Ambasador al Bunăvoinței. Marcată de propria experiență din timpul foametei din al Doilea Război Mondial, Audrey a călătorit în zonele cele mai sărace din Africa, America de Sud și Asia pentru a atrage atenția lumii asupra copiilor malnutriți și a nevoii de educație. Ea a transformat statutul de celebritate într-o platformă pentru compasiune, demonstrând că eleganța adevărată provine din bunătate și dedicare față de cei suferinzi, rămânând un simbol al altruismului global.")
                    self.parent.add_data("Care este semnificația personajului Daenerys Targaryen în contextul puterii?", "Daenerys Targaryen din 'Game of Thrones' servește drept un studiu de caz complex despre ambiție, putere și corupție morală. Evoluția ei de la o victimă a circumstanțelor la o cuceritoare absolută explorează ideea periculoasă că 'scopul scuză mijloacele'. Deși pornește cu intenția nobilă de a elibera sclavii și de a distruge tirania, Daenerys ajunge să creadă atât de puternic în propriul destin mesianic încât orice opoziție devine, în ochii ei, o formă de rău ce trebuie eliminată. Povestea ei avertizează asupra riscului ca un lider care se consideră infailibil să devină exact monstrul pe care a jurat să îl distrugă, ridicând întrebări fundamentale despre natura autorității și prețul libertății.")
                    self.parent.add_data("Ce definește muzica Clasică și de ce este considerată atemporală?", "Muzica clasică este o tradiție artistică vastă care se întinde pe mai multe secole, atingând culmi de complexitate în perioadele Barocă, Clasică și Romantică. Ceea ce o face atemporală este capacitatea sa de a exprima gama completă de emoții umane — de la agonie la extaz — fără a se baza pe limbaj, ci pe structură, armonie și textură sonoră. Compozițiile lui Bach, Mozart sau Beethoven sunt construite pe principii matematice și estetice riguroase care continuă să rezoneze cu ascultătorii moderni. Dincolo de valoarea artistică, muzica clasică este recunoscută pentru beneficiile sale cognitive, îmbunătățind concentrarea și oferind un spațiu de contemplare profundă într-o lume dominată de consumul rapid și superficial de informație.")
                    self.parent.add_data("Cum pot fi combatute schimbările climatice la nivel individual?", "Deși soluțiile la scară largă depind de guverne și corporații, acțiunile individuale au un impact cumulativ semnificativ și pot influența piața. Reducerea consumului de carne și lactate, alegerea mijloacelor de transport în comun sau a bicicletei și optimizarea eficienței energetice a locuinței sunt pași concreți pentru scăderea amprentei de carbon. De asemenea, practicarea unui consum responsabil — cumpărarea de produse durabile în locul celor de unică folosință și susținerea afacerilor locale sustenabile — pune presiune pe lanțurile de aprovizionare globale. Dincolo de stilul de viață, implicarea civică și educarea celor din jur sunt esențiale pentru a crea o masă critică de oameni care să ceară politici de protecție a mediului mai stricte și mai rapide.")
                    self.parent.add_data("De ce este importantă explorarea spațială pentru viitorul omenirii?", "Explorarea spațială nu este doar o manifestare a curiozității umane, ci o necesitate strategică pentru supraviețuirea și progresul speciei noastre. Pe termen scurt, tehnologiile dezvoltate pentru misiuni spațiale au dus la inovații majore pe Pământ, de la purificarea apei și panouri solare mai eficiente, până la tehnologii medicale avansate. Pe termen lung, stabilirea unor colonii pe alte planete, cum ar fi Marte, servește drept o asigurare împotriva unor posibile catastrofe globale pe Terra. Mai mult, extragerea resurselor din asteroizi ar putea rezolva problema penuriei de metale rare, protejând în același timp mediul terestru de mineritul invaziv. Spațiul rămâne frontiera finală care ne forțează să cooperăm la nivel global și să ne depășim limitele tehnologice.")
                    self.parent.add_data("Cum ne influențează 'bula de filtru' (filter bubble) opiniile pe rețelele sociale?", "Bula de filtru apare atunci când algoritmii rețelelor sociale ne oferă doar informații și opinii care sunt în concordanță cu preferințele și convingerile noastre anterioare, bazându-se pe interacțiunile noastre online. Acest lucru creează un mediu în care propriile idei ne sunt confirmate constant, în timp ce perspectivele contrare sunt eliminate din câmpul nostru vizual. Pericolul major este polarizarea extremă a societății și dispariția dialogului constructiv, deoarece începem să credem că punctul nostru de vedere este singurul valid. Ieșirea din această bulă necesită un efort conștient de a căuta surse de știri diverse, de a urmări persoane cu opinii diferite și de a interacționa cu conținut care ne provoacă propriile certitudini, dezvoltând astfel o gândire mai nuanțată.")
                    self.parent.add_data("Care este istoria și semnificația Marelui Zid Chinezesc?", "Marele Zid Chinezesc este una dintre cele mai grandioase realizări inginerești ale antichității, fiind construit de-a lungul a peste două mii de ani de către mai multe dinastii pentru a proteja frontierele de invaziile nomade din nord. Dincolo de scopul său defensiv, zidul a servit ca instrument de control al comerțului de-a lungul Drumului Mătăsii și ca sistem de comunicații rapid prin turnurile de semnalizare cu fum și foc. Construcția sa a implicat un efort uman imens, devenind un simbol al perseverenței, dar și al izolării. Astăzi, Marele Zid este un monument al identității naționale chineze și un obiectiv cultural mondial, amintindu-ne de capacitatea umană de a modifica peisajul pentru a asigura securitatea și continuitatea unei civilizații.")
                    self.parent.add_data("Ce este 'Paradoxul lui Fermi' și de ce ne pune pe gânduri?", "Paradoxul lui Fermi reprezintă contradicția dintre probabilitatea mare de existență a civilizațiilor extraterestre în universul nostru vast și lipsa oricăror dovezi sau contacte cu acestea. Având în vedere miliardele de stele similare Soarelui și miliardele de planete potențial locuibile, logic ar fi ca universul să abunde de viață inteligentă. Explicațiile posibile includ ipoteza 'Marelui Filtru' (o barieră evolutivă greu de depășit), ideea că suntem printre primele civilizații care au apărut sau posibilitatea că civilizațiile avansate aleg să nu comunice. Acest paradox ne forțează să reflectăm asupra propriei noastre fragilități și asupra unicității vieții pe Pământ, ridicând întrebări fundamentale despre locul nostru în cosmos.")
                    self.parent.add_data("De ce este importantă metoda Socratică în educația modernă?", "Metoda Socratică este o formă de dialog cooperativ bazată pe întrebări și răspunsuri menite să stimuleze gândirea critică și să scoată la iveală idei și presupuneri implicite. În loc să ofere soluții de-a gata, profesorul pune întrebări care îl conduc pe elev să descopere singur contradicțiile din propria gândire și să ajungă la o înțelegere mai profundă a subiectului. Această metodă este crucială în educația modernă deoarece mută accentul de pe memorarea mecanică pe procesul de analiză și sinteză. Ea dezvoltă curiozitatea intelectuală, modestia (prin recunoașterea limitelor propriei cunoașteri) și abilitățile de argumentare logică, pregătind indivizii să navigheze într-o lume plină de informații ambigue.")
                    self.parent.add_data("Cum a transformat Revoluția Industrială societatea umană?", "Revoluția Industrială, începută în secolul al XVIII-lea în Marea Britanie, a marcat trecerea de la producția manuală la cea mecanizată, declanșând o transformare radicală a tuturor aspectelor vieții umane. Aceasta a dus la o creștere fără precedent a productivității și a nivelului de trai pentru mulți, dar a provocat și o urbanizare rapidă și adesea haotică. Oamenii s-au mutat de la sate în orașe pentru a munci în fabrici, ceea ce a schimbat structura familiei și a dat naștere clasei muncitoare moderne. Pe lângă progresul tehnologic, revoluția a adus provocări sociale majore, cum ar fi condițiile de muncă grele și poluarea mediului, punând bazele sistemelor economice capitaliste și ale mișcărilor pentru drepturile muncitorilor.")
                    self.parent.add_data("Care este legătura dintre nutriție și sănătatea mentală?", "Cercetările recente din domeniul psihiatriei nutriționale demonstrează o legătură strânsă între calitatea dietei și sănătatea mentală, sugerând că alimentele pe care le consumăm influențează direct funcționarea creierului și starea de spirit. O dietă bogată în nutrienți, cum ar fi acizii grași omega-3, vitaminele din grupul B și antioxidanții, susține neuroplasticitatea și reduce inflamația la nivel cerebral. De asemenea, microbiomul intestinal — 'al doilea creier' — comunică constant cu sistemul nervos central prin axa intestin-creier, producând neurotransmițători esențiali precum serotonina. Consumul excesiv de zahăr și alimente ultra-procesate este corelat cu un risc crescut de depresie și anxietate, subliniind faptul că o alimentație echilibrată este fundamentală nu doar pentru corp, ci și pentru minte.")
                    self.parent.add_data("Ce este programarea orientată pe obiecte (OOP) și de ce este atât de utilizată?", "Programarea Orientată pe Obiecte (OOP) este o paradigmă de programare care organizează designul software-ului în jurul datelor, sau 'obiectelor', mai degrabă decât în jurul funcțiilor și logicii. Un obiect poate fi definit ca un câmp de date care are atribute și comportamente unice. Cele patru principii de bază — încapsularea, moștenirea, polimorfismul și abstracția — permit dezvoltatorilor să scrie cod modular, reutilizabil și ușor de întreținut. Această abordare este extrem de utilă în proiectele complexe, deoarece permite echipelor mari să lucreze simultan pe module diferite și să modeleze problemele din lumea reală într-un mod intuitiv, reducând erorile și accelerând procesul de dezvoltare software.")
                    self.parent.add_data("Cine a fost Sherlock Holmes și cum a influențat el criminalistica?", "Sherlock Holmes, celebrul detectiv creat de Sir Arthur Conan Doyle, este un personaj literar care a depășit granițele ficțiunii pentru a deveni un model de gândire logică și observație științifică. Holmes a popularizat utilizarea metodelor de investigație bazate pe dovezi materiale, cum ar fi analiza amprentelor, a urmelor de pași și a reziduurilor de substanțe, cu mult înainte ca acestea să devină practici standard în poliția reală. Abordarea sa analitică, bazată pe deducție și pe principiul că 'după ce ai eliminat imposibilul, ceea ce rămâne, oricât de improbabil, trebuie să fie adevărul', a inspirat mii de detectivi reali și a pus bazele criminalisticii moderne, transformând investigarea crimelor dintr-o intuiție în o disciplină riguroasă.")
                    self.parent.add_data("Care sunt cauzele și consecințele colapsului civilizației Maiașe?", "Colapsul civilizației Maiașe din perioada clasică nu a fost rezultatul unui singur eveniment catastrofal, ci mai degrabă o succesiune de crize interconectate care au dus la abandonarea marilor centre urbane. Printre cauzele principale se numără degradarea mediului din cauza defrișărilor excesive, secete prelungite care au distrus agricultura și războaie endemice între orașele-stat pentru resurse limitate. Această presiune a dus la pierderea încrederii în liderii religioși și politici, provocând migrații masive și colapsul sistemelor administrative complexe. Consecința a fost fragmentarea societății și revenirea la forme de organizare mai simple, demonstrând fragilitatea societăților avansate în fața dezechilibrelor ecologice și a conflictelor interne.")
                    self.parent.add_data("Explicați conceptul de 'mindfulness' și beneficiile sale demonstrate științific.", "Mindfulness, sau starea de prezență conștientă, reprezintă practica de a-ți concentra atenția asupra momentului prezent într-un mod non-critic și acceptant. Deși își are originile în tradițiile meditative orientale, mindfulness a fost adoptat pe scară largă în psihologia modernă datorită beneficiilor sale demonstrate prin neuroimagistică. Practica regulată ajută la reducerea dimensiunii amigdalei (centrul fricii din creier) și la creșterea densității materiei cenușii în zonele responsabile pentru învățare și reglare emoțională. Printre beneficiile sale se numără scăderea stresului cronic, îmbunătățirea concentrării, gestionarea mai eficientă a durerii și creșterea rezilienței în fața provocărilor cotidiene, fiind un instrument valoros pentru menținerea echilibrului psihic în era digitală.")
                    self.parent.add_data("Ce sunt criptomonedele și cum ar putea ele schimba sistemul financiar global?", "Criptomonedele sunt active digitale care utilizează criptografia pentru a securiza tranzacțiile și pentru a controla crearea de noi unități, funcționând de obicei pe o rețea descentralizată numită blockchain. Spre deosebire de monedele tradiționale emise de bănci centrale, criptomonede precum Bitcoin oferă promisiunea unor tranzacții transparente, rapide și fără intermediari, indiferent de granițe. Impactul lor potențial asupra sistemului financiar este major: ar putea reduce costurile tranzacționale globale, ar oferi acces la servicii financiare persoanelor care nu au conturi bancare și ar putea servi ca o rezervă de valoare protejată de inflație în economiile instabile. Totuși, volatilitatea mare, riscurile de securitate și impactul ecologic al minării rămân provocări esențiale care trebuie rezolvate înainte de o adopție pe scară largă.")
                    self.parent.add_data("Care este importanța egalității de șanse în societatea modernă?", "Egalitatea de șanse reprezintă principiul conform căruia toți indivizii ar trebui să aibă același acces la resurse, educație și oportunități de angajare, indiferent de gen, rasă, origine socială sau dizabilități. Într-o societate modernă, acest concept nu este doar un deziderat moral, ci și un motor economic: o societate care valorifică talentele tuturor membrilor săi este mai inovatoare, mai productivă și mai stabilă. Reducerea barierelor sistemice ajută la combaterea sărăciei generaționale și la creșterea coeziunii sociale. Egalitatea de șanse nu înseamnă uniformitate, ci asigurarea faptului că punctul de plecare al unei persoane nu îi limitează în mod nedrept potențialul de realizare, permițând meritocrației să funcționeze în mod real.")
                    self.parent.add_data("Poți să-mi explici fenomenul încălzirii globale și care sunt principalele cauze identificate de oamenii de știință?", "Încălzirea globală reprezintă creșterea treptată a temperaturilor medii în atmosfera Pământului și în oceane, un proces accelerat de activitățile umane care emit gaze cu efect de seră, precum dioxidul de carbon și metanul, rezultate în principal din arderea combustibililor fosili și defrișările masive.")

                    self.parent.add_data("Care sunt beneficiile cititului constant pentru dezvoltarea cognitivă și emoțională a unei persoane?", "Cititul constant îmbunătățește vocabularul, capacitatea de concentrare și gândirea critică, oferind în același timp o modalitate de a explora perspective noi și de a dezvolta empatia prin înțelegerea experiențelor personajelor, reducând totodată nivelul de stres zilnic.")

                    self.parent.add_data("Cum funcționează procesul de fotosinteză și de ce este acesta vital pentru viața pe Pământ?", "Fotosinteza este procesul prin care plantele verzi, algele și unele bacterii transformă energia luminoasă a soarelui în energie chimică, utilizând apă și dioxid de carbon pentru a produce glucoză și oxigen, acesta din urmă fiind esențial pentru respirația majorității organismelor vii.")

                    self.parent.add_data("Ce sfaturi ai pentru cineva care dorește să înceapă o grădină de legume în propria curte?", "Pentru a începe o grădină de legume, este important să alegi un loc cu expunere solară de cel puțin șase ore pe zi, să pregătești solul cu îngrășământ organic, să planifici rotația culturilor pentru a menține sănătatea pământului și să asiguri un sistem de irigare constant și eficient.")

                    self.parent.add_data("Poți să descrii importanța protejării biodiversității în ecosistemele fragile ale planetei noastre?", "Protejarea biodiversității este crucială deoarece fiecare specie joacă un rol specific în menținerea echilibrului ecosistemului, oferind servicii esențiale precum polenizarea plantelor, reglarea climei, purificarea apei și furnizarea de resurse medicinale pe care omenirea se bazează.")

                    self.parent.add_data("Care sunt principalele diferențe între stilul de viață nomad și cel sedentar din punct de vedere istoric?", "Stilul de viață nomad presupune deplasarea constantă în căutarea resurselor de hrană și pășuni, în timp ce stilul sedentar a apărut odată cu revoluția agricolă, permițând oamenilor să construiască așezări permanente, să dezvolte structuri sociale complexe și să acumuleze bunuri materiale.")

                    self.parent.add_data("Cum se poate gestiona eficient anxietatea înaintea unei prezentări publice importante?", "Gestionarea anxietății se poate face prin pregătirea riguroasă a materialului, exersarea tehnicilor de respirație profundă pentru calmarea sistemului nervos, vizualizarea succesului și acceptarea faptului că emoțiile sunt o reacție naturală care poate fi canalizată în energie pozitivă pe scenă.")

                    self.parent.add_data("Explică importanța explorării spațiale pentru progresul tehnologic și științific al umanității.", "Explorarea spațială a condus la invenții revoluționare care sunt folosite astăzi pe Pământ, cum ar fi sistemele GPS, tehnologia de purificare a apei și senzorii de imagine pentru camerele foto, stimulând în același timp curiozitatea umană și înțelegerea originilor universului nostru.")

                    self.parent.add_data("Ce este economia circulară și cum poate aceasta să ajute la reducerea poluării la nivel global?", "Economia circulară este un model de producție și consum care implică partajarea, închirierea, reutilizarea, repararea și reciclarea materialelor și produselor existente cât mai mult posibil, cu scopul de a prelungi ciclul de viață al produselor și de a reduce la minimum deșeurile generate.")

                    self.parent.add_data("Cum influențează consumul excesiv de zahăr sănătatea pe termen lung a organismului uman?", "Consumul excesiv de zahăr este asociat cu un risc ridicat de obezitate, diabet de tip 2, boli cardiovasculare și carii dentare, deoarece provoacă fluctuații bruște ale insulinei în sânge și poate duce la inflamații cronice în diverse organe ale corpului.")

                    self.parent.add_data("Care sunt trăsăturile definitorii ale stilului arhitectural gotic întâlnit în catedralele europene?", "Arhitectura gotică se remarcă prin utilizarea arcurilor frânte, a bolților pe nervuri și a contraforturilor exterioare, elemente care au permis construirea unor clădiri foarte înalte cu ferestre uriașe decorate cu vitralii colorate ce inundă interiorul cu lumină.")

                    self.parent.add_data("Descrie procesul prin care se formează un curcubeu pe cer după o ploaie de vară.", "Curcubeul apare atunci când lumina soarelui este refractată, reflectată și dispersată în interiorul picăturilor de apă din atmosferă, separând lumina albă în spectrul său de culori vizibile, formând astfel un arc multicolor situat opus față de poziția soarelui.")

                    self.parent.add_data("De ce este considerată limba română o limbă romantică și care sunt principalele ei asemănări cu latina?", "Limba română este o limbă romanică deoarece s-a format din latina vulgară vorbită în provincia Dacia; ea păstrează o structură gramaticală similară cu latina, inclusiv sistemul de declinări ale substantivelor, și un lexic de bază compus în mare parte din cuvinte de origine latină.")

                    self.parent.add_data("Care sunt principalele provocări ale utilizării energiei regenerabile la scară largă în prezent?", "Principalele provocări includ intermitența surselor precum vântul și soarele, necesitatea dezvoltării unor tehnologii avansate de stocare a energiei în baterii de mare capacitate și costurile ridicate pentru modernizarea infrastructurii rețelelor electrice actuale.")

                    self.parent.add_data("Cum poate învățarea unei limbi străine să modifice structura și funcționarea creierului uman?", "Învățarea unei limbi străine crește densitatea materiei cenușii în zonele responsabile pentru memorie și atenție, îmbunătățește neuroplasticitatea și poate întârzia apariția simptomelor unor boli neurodegenerative precum Alzheimer prin menținerea creierului activ și solicitat.")

                    self.parent.add_data("Ce este dezinformarea digitală și cum ne putem proteja de știrile false de pe rețelele sociale?", "Dezinformarea digitală reprezintă distribuirea intenționată de informații false pentru a induce în eroare; ne putem proteja prin verificarea surselor din mai multe locuri oficiale, analizarea autorului articolului și dezvoltarea unui simț critic față de titlurile senzaționaliste.")

                    self.parent.add_data("Explică importanța somnului REM pentru procesarea emoțiilor și consolidarea memoriei.", "Somnul REM (Rapid Eye Movement) este etapa în care apar cele mai intense vise și este esențial pentru sănătatea mentală, deoarece în acest timp creierul procesează experiențele emoționale de peste zi și consolidează amintirile noi, facilitând învățarea pe termen lung.")

                    self.parent.add_data("Care sunt etapele principale ale realizării unui film, de la idee până la lansarea pe marile ecrane?", "Producția unui film cuprinde pre-producția (scrierea scenariului și castingul), producția propriu-zisă (filmările pe platou), post-producția (montajul, efectele speciale și sunetul) și, în final, distribuția și promovarea către publicul larg.")

                    self.parent.add_data("Cum a influențat Revoluția Industrială structura familiilor și a comunităților urbane?", "Revoluția Industrială a dus la migrarea masivă a oamenilor de la sate la orașe în căutare de muncă în fabrici, schimbând structura familiei extinse în familie nucleară și ducând la apariția clasei muncitoare urbane și la dezvoltarea rapidă, dar adesea haotică, a marilor orașe.")

                    self.parent.add_data("Care este rolul unui ecosistem marin în reglarea nivelului de oxigen de pe întreaga planetă?", "Ecosistemele marine, în special fitoplanctonul din oceane, produc peste 50% din oxigenul planetei prin fotosinteză și absorb cantități uriașe de dioxid de carbon, jucând astfel un rol vital în atenuarea schimbărilor climatice și susținerea vieții pe Terra.")

                    self.parent.add_data("Ce înseamnă conceptul de 'mindfulness' și cum poate fi practicat în viața de zi cu zi?", "Mindfulness reprezintă starea de prezență conștientă și focalizarea atenției asupra momentului actual fără a judeca; poate fi practicat prin respirație conștientă, observarea senzațiilor corporale în timpul activităților obișnuite sau prin meditație dedicată pentru reducerea stresului.")

                    self.parent.add_data("Descrie modul în care vulcanii influențează fertilitatea solului din regiunile înconjurătoare.", "Deși erupțiile vulcanice pot fi distructive, cenușa și lava descompusă în timp eliberează nutrienți esențiali precum potasiul și fosforul în pământ, creând unele dintre cele mai fertile soluri agricole din lume, capabile să susțină culturi bogate și diverse.")

                    self.parent.add_data("Care sunt avantajele și dezavantajele muncii la distanță pentru angajați și angajatori?", "Avantajele includ flexibilitatea programului și eliminarea timpului pierdut în trafic, în timp ce dezavantajele se referă la dificultatea separării vieții profesionale de cea personală, posibila izolare socială a angajatului și provocările în menținerea culturii organizaționale pentru angajatori.")

                    self.parent.add_data("Cum funcționează sistemul de imunizare prin vaccinare și cum ajută acesta la protejarea populației?", "Vaccinarea funcționează prin introducerea unei forme inofensive a unui agent patogen în corp pentru a antrena sistemul imunitar să îl recunoască și să producă anticorpi, creând astfel o memorie imunologică ce previne îmbolnăvirea gravă în cazul unei expuneri viitoare.")

                    self.parent.add_data("Care este impactul microplasticelor asupra lanțului trofic și a sănătății umane?", "Microplasticele sunt ingerate de organisme mici marine, ajungând prin consum în pești și ulterior în oameni, transportând substanțe chimice toxice care pot perturba sistemul endocrin și pot cauza inflamații, reprezentând o problemă majoră de mediu și sănătate publică.")

                    self.parent.add_data("Explică conceptul de 'an lumină' și cum este acesta utilizat în astronomie pentru a măsura distanțele.", "Un an lumină este distanța pe care lumina o parcurge într-un an în vid, adică aproximativ 9,5 trilioane de kilometri; este o unitate de măsură esențială în astronomie deoarece distanțele dintre stele și galaxii sunt atât de mari încât kilometrii obișnuiți ar fi imposibil de gestionat.")

                    self.parent.add_data("Care sunt cauzele apariției deșertificării și ce măsuri pot fi luate pentru a stopa acest proces?", "Deșertificarea este cauzată de schimbările climatice, suprapășunat, defrișări și practici agricole inadecvate; măsurile de stopare includ reîmpădurirea zonelor afectate, gestionarea durabilă a resurselor de apă și utilizarea unor tehnici agricole care protejează stratul superior al solului.")

                    self.parent.add_data("Cum influențează muzica clasică starea psihică și performanța intelectuală a studenților?", "Muzica clasică, în special anumite compoziții baroce sau clasice, poate reduce tensiunea arterială și nivelul de cortizol, inducând o stare de relaxare alertă care favorizează memorarea, concentrarea și procesarea informațiilor complexe în timpul studiului.")

                    self.parent.add_data("Ce este inteligența emoțională și de ce este considerată la fel de importantă ca inteligența cognitivă?", "Inteligența emoțională (EQ) reprezintă capacitatea de a recunoaște, înțelege și gestiona propriile emoții, precum și de a empatiza cu ceilalți; este vitală pentru succesul profesional și personal deoarece facilitează comunicarea, rezolvarea conflictelor și leadership-ul eficient.")

                    self.parent.add_data("Descrie rolul albinelor în producția globală de alimente și riscurile dispariției lor.", "Albinele sunt principalii polenizatori ai multor culturi agricole de care depinde alimentația umană, precum fructele și legumele; dispariția lor din cauza pesticidelor și pierderii habitatului ar duce la o scădere drastică a producției alimentare și la un dezechilibru major în biodiversitate.")

                    self.parent.add_data("Cum funcționează un motor electric comparativ cu un motor cu ardere internă?", "Un motor electric transformă energia electrică direct în mișcare prin intermediul câmpurilor magnetice, fiind mult mai eficient și silențios, în timp ce un motor cu ardere internă produce energie prin explozii controlate de combustibil, având mai multe piese în mișcare și emițând gaze poluante.")

                    self.parent.add_data("Care sunt beneficiile dietei mediteraneene asupra longevității și sănătății inimii?", "Dieta mediteraneeană, bogată în fructe, legume, cereale integrale, pește și ulei de măsline, este celebră pentru reducerea riscului de boli cardiace și inflamații, oferind un aport ridicat de antioxidanți și grăsimi sănătoase care contribuie la o viață lungă și sănătoasă.")

                    self.parent.add_data("Explică ce este un activ financiar de tip 'acțiune' și cum pot investitorii să câștige bani din acestea.", "O acțiune reprezintă o unitate de proprietate într-o companie; investitorii pot câștiga bani fie prin creșterea prețului acțiunii în timp (aprecierea capitalului), fie prin primirea unei părți din profitul companiei sub formă de dividende periodice.")

                    self.parent.add_data("Care este importanța stratului de ozon pentru viața de pe Pământ și cum a fost acesta afectat de substanțele CFC?", "Stratul de ozon acționează ca un scut care absoarbe majoritatea radiațiilor ultraviolete nocive ale soarelui; substanțele chimice de tip CFC folosite în trecut în spray-uri și frigidere au subțiat acest strat, crescând riscul de cancer de piele și afectând ecosistemele marine.")

                    self.parent.add_data("Cum se formează stalactitele și stalagmitele în peșterile calcaroase de-a lungul mileniilor?", "Aceste formațiuni se creează prin depunerea lentă a carbonatului de calciu din picăturile de apă care se infiltrează prin tavanul peșterii; stalactitele cresc de sus în jos, iar stalagmitele se formează pe podea din apa care cade, întâlnindu-se uneori pentru a forma coloane impresionante.")

                    self.parent.add_data("Ce este alfabetizarea digitală și de ce este esențială pentru cetățenii secolului XXI?", "Alfabetizarea digitală reprezintă capacitatea de a găsi, evalua și comunica informații prin diverse platforme digitale; este esențială deoarece majoritatea serviciilor publice, locurilor de muncă și modalităților de comunicare modernă depind acum de utilizarea corectă și sigură a tehnologiei.")

                    self.parent.add_data("Care este impactul fast-fashion-ului asupra mediului înconjurător și ce putem face pentru a fi mai sustenabili?", "Industria fast-fashion produce cantități enorme de deșeuri textile și utilizează resurse uriașe de apă, poluând solul cu vopsele toxice; putem fi mai sustenabili prin cumpărarea de haine de calitate mai bună, susținerea brandurilor etice sau prin achiziționarea de articole second-hand.")

                    self.parent.add_data("Descrie modul în care se produce un cutremur și cum se măsoară intensitatea acestuia.", "Cutremurele se produc prin eliberarea bruscă de energie în scoarța terestră, de obicei la contactul dintre plăcile tectonice; intensitatea lor se măsoară cu ajutorul seismografelor, folosind scara Richter pentru magnitudine sau scara Mercalli pentru a evalua efectele vizibile asupra clădirilor.")

                    self.parent.add_data("Cum a schimbat inventarea tiparului de către Gutenberg accesul la cunoaștere în Europa?", "Inventarea tiparului a permis producerea rapidă și ieftină a cărților, ducând la alfabetizarea masivă a populației, la răspândirea ideilor noi în timpul Renașterii și Reformei și la democratizarea informației care înainte era accesibilă doar elitelor și clerului.")

                    self.parent.add_data("Ce sunt probioticele și ce rol joacă ele în menținerea sănătății sistemului digestiv?", "Probioticele sunt microorganisme vii, adesea numite 'bacterii bune', care ajută la menținerea echilibrului florei intestinale, îmbunătățesc digestia, întăresc sistemul imunitar și pot preveni diverse afecțiuni gastrointestinale cauzate de stres sau alimentație dezechilibrată.")

                    self.parent.add_data("Care este rolul ONU (Organizația Națiunilor Unite) în menținerea păcii la nivel mondial?", "ONU are misiunea de a preveni conflictele armate prin diplomație, de a oferi asistență umanitară în zone de criză, de a promova drepturile omului și de a facilita cooperarea internațională pentru rezolvarea problemelor economice și sociale globale.")

                    self.parent.add_data("Explicați importanța pădurilor tropicale amazoniene în contextul stabilității climatice globale.", "Pădurea amazoniană, supranumită 'plămânul planetei', stochează miliarde de tone de carbon și produce o cantitate semnificativă de umiditate care influențează regimul precipitațiilor la nivel global; distrugerea ei ar accelera dramatic încălzirea globală și ar distruge mii de specii unice.")

                    self.parent.add_data("Cum influențează rețelele de socializare stima de sine a adolescenților în era digitală?", "Rețelele de socializare pot afecta negativ stima de sine prin comparația constantă cu imagini idealizate ale altora și prin nevoia de validare externă (like-uri), însă pot oferi și spații de exprimare creativă și comunități de suport dacă sunt utilizate cu moderație și discernământ.")

                    self.parent.add_data("Ce este terapia prin artă și cum poate aceasta ajuta la vindecarea unor traume psihice?", "Terapia prin artă folosește procesul creativ (pictură, sculptură, desen) ca mijloc de comunicare pentru a ajuta oamenii să exprime sentimente greu de pus în cuvinte, facilitând explorarea emoțiilor interioare, reducerea anxietății și procesarea experiențelor traumatizante într-un mediu sigur.")

                    self.parent.add_data("Descrieți procesul de fabricare a hârtiei și impactul acestuia asupra resurselor forestiere.", "Hârtia se fabrică prin prelucrarea fibrelor de celuloză din lemn sau materiale reciclate în pastă, care este apoi întinsă și uscată; cererea mare de hârtie pune presiune pe păduri, motiv pentru care reciclarea și utilizarea lemnului din surse certificate sustenabil sunt extrem de importante.")

                    self.parent.add_data("Care sunt beneficiile utilizării vehiculelor cu hidrogen față de cele electrice clasice?", "Vehiculele cu hidrogen se alimentează mult mai rapid (în câteva minute) și oferă o autonomie mai mare, eliminând necesitatea bateriilor grele de litiu; totuși, infrastructura de alimentare este încă limitată și producția de hidrogen verde necesită multă energie.")

                    self.parent.add_data("Cum afectează poluarea fonică viața animalelor sălbatice din apropierea zonelor urbane?", "Poluarea fonică poate masca sunetele pe care animalele le folosesc pentru comunicare, orientare sau vânătoare, forțându-le să își părăsească habitatele naturale, schimbându-le comportamentul de împerechere și crescându-le nivelul de stres fiziologic.")

                    self.parent.add_data("Ce reprezintă conceptul de 'oraș inteligent' (Smart City) și cum îmbunătățește acesta viața locuitorilor?", "Un oraș inteligent folosește tehnologia IoT (Internet of Things) și datele pentru a optimiza serviciile urbane, cum ar fi gestionarea traficului în timp real, iluminatul public eficient, colectarea inteligentă a deșeurilor și reducerea consumului de energie, oferind un mediu mai curat și mai organizat.")

                    self.parent.add_data("Care este rolul muzeelor în conservarea identității culturale și a istoriei unei națiuni?", "Muzeele servesc drept depozitare ale memoriei colective, conservând artefacte, opere de artă și documente istorice care ne permit să înțelegem trecutul, să învățăm despre realizările strămoșilor și să ne definim identitatea culturală într-o lume tot mai globalizată.")

                    self.parent.add_data("Cum poate voluntariatul să contribuie la dezvoltarea abilităților profesionale și personale ale tinerilor?", "Voluntariatul oferă tinerilor oportunitatea de a dobândi experiență practică, de a-și dezvolta abilitățile de lucru în echipă și comunicare, de a-și lărgi rețeaua de contacte și de a cultiva un simț al responsabilității sociale, crescându-le totodată încrederea în propriile forțe.")

                    self.parent.add_data("Poți să explici diferența fundamentală dintre un hard disk drive (HDD) și un solid state drive (SSD) în ceea ce privește mecanismul de funcționare?", "Diferența principală constă în modul de stocare și accesare a datelor: HDD-ul utilizează platouri magnetice care se rotesc și un braț mecanic cu un cap de citire/scriere, în timp ce SSD-ul nu are componente mobile, folosind memoria flash bazată pe semiconductori (NAND), ceea ce îi oferă viteze de acces mult mai mari și o rezistență sporită la șocuri mecanice.")

                    self.parent.add_data("Ce este un sistem de operare și care sunt principalele sale responsabilități în gestionarea resurselor unui calculator?", "Un sistem de operare este software-ul de bază care acționează ca o interfață între utilizator și hardware-ul computerului, având responsabilități critice precum gestionarea procesorului (scheduling), administrarea memoriei RAM, controlul dispozitivelor de intrare/ieșire și gestionarea sistemului de fișiere pentru a asigura rularea stabilă a aplicațiilor.")

                    self.parent.add_data("Explică conceptul de 'Cloud Computing' și care sunt principalele diferențe între modelele de servicii IaaS, PaaS și SaaS.", "Cloud Computing reprezintă livrarea de servicii de calcul prin internet. IaaS (Infrastructure as a Service) oferă resurse hardware virtualizate, PaaS (Platform as a Service) oferă un mediu de dezvoltare și deployment pentru programatori, iar SaaS (Software as a Service) oferă aplicații gata de utilizat direct de către utilizatorul final, fără a fi necesară instalarea locală.")

                    self.parent.add_data("Ce reprezintă modelul OSI în rețelele de calculatoare și de ce este importantă separarea pe șapte straturi?", "Modelul OSI (Open Systems Interconnection) este un cadru conceptual care standardizează funcțiile unui sistem de comunicații în șapte straturi distincte: Fizic, Legătură de date, Rețea, Transport, Sesiune, Prezentare și Aplicație. Această separare permite interoperabilitatea între diferite tehnologii și ușurează diagnosticarea problemelor de rețea prin izolarea funcțiilor specifice fiecărui nivel.")

                    self.parent.add_data("Cum funcționează protocolul HTTPS și prin ce se diferențiază acesta de varianta standard HTTP în ceea ce privește securitatea?", "HTTPS (Hypertext Transfer Protocol Secure) utilizează protocolul de criptare TLS (Transport Layer Security) sau predecesorul său SSL pentru a securiza comunicarea dintre browser și server. Spre deosebire de HTTP, unde datele sunt trimise în format text simplu, HTTPS criptează datele, asigurând integritatea acestora și autenticitatea serverului prin utilizarea certificatelor digitale.")

                    self.parent.add_data("Ce este un limbaj de programare compilat și cum se compară acesta cu un limbaj interpretat în termeni de performanță?", "Un limbaj compilat (precum C++ sau Rust) este transformat integral în cod mașină de către un compilator înainte de execuție, ceea ce oferă o viteză superioară. Limbajele interpretate (precum Python sau JavaScript) sunt citite și executate linie cu linie de către un interpretor în timpul rulării, oferind o flexibilitate mai mare și o testare mai rapidă, dar cu un cost în performanța brută.")

                    self.parent.add_data("Poți explica ce este tehnologia Blockchain și de ce este considerată imuabilă?", "Blockchain este un registru digital distribuit care stochează datele în blocuri legate cronologic prin funcții hash criptografice. Este considerat imuabil deoarece, odată ce un bloc este adăugat și validat de rețea, modificarea oricărei informații din acesta ar necesita recalcularea tuturor blocurilor ulterioare și controlul majorității nodurilor din rețea, ceea ce este practic imposibil din punct de vedere computațional.")

                    self.parent.add_data("Ce este 'Internet of Things' (IoT) și care sunt principalele riscuri de securitate asociate cu dispozitivele inteligente?", "IoT se referă la rețeaua de obiecte fizice echipate cu senzori și software care colectează și schimbă date prin internet. Principalele riscuri includ parolele implicite slabe, lipsa actualizărilor de securitate periodice din partea producătorilor și faptul că aceste dispozitive pot fi integrate în rețele botnet pentru a lansa atacuri de tip DDoS asupra altor infrastructuri.")

                    self.parent.add_data("Cum funcționează o rețea neuronală artificială și care este rolul funcției de activare?", "O rețea neuronală artificială este un model computațional inspirat de creierul uman, format din straturi de neuroni interconectați. Fiecare conexiune are o pondere (weight) care este ajustată în timpul antrenamentului. Funcția de activare (cum ar fi ReLU sau Sigmoid) determină dacă un neuron trebuie să transmită un semnal stratului următor, introducând non-liniaritate în model pentru a-l ajuta să învețe tipare complexe.")

                    self.parent.add_data("Ce este un VPN (Virtual Private Network) și cum protejează acesta confidențialitatea utilizatorului pe internet?", "Un VPN creează un tunel criptat între dispozitivul utilizatorului și un server privat, mascând adresa IP reală și criptând tot traficul de date. Aceasta protejează utilizatorul de monitorizarea ISP-ului, securizează conexiunile pe rețele Wi-Fi publice nesigure și permite accesarea conținutului restricționat geografic prin rutarea traficului printr-o altă locație.")

                    self.parent.add_data("Explică diferența dintre Inteligența Artificială (AI), Machine Learning (ML) și Deep Learning (DL).", "AI este conceptul general de a crea mașini capabile să simuleze inteligența umană. Machine Learning este un subdomeniu al AI care folosește algoritmi pentru a învăța din date fără a fi programat explicit. Deep Learning este o ramură a ML care utilizează rețele neuronale cu multe straturi (adânci) pentru a analiza date complexe precum imagini sau limbaj natural.")

                    self.parent.add_data("Ce este un procesor (CPU) multi-core și cum influențează acesta procesul de 'multitasking'?", "Un procesor multi-core are două sau mai multe nuclee independente de procesare pe un singur cip, fiecare capabil să execute instrucțiuni separat. Acest lucru permite calculatorului să execute mai multe fire de execuție (threads) simultan, îmbunătățind semnificativ performanța în aplicații complexe și permițând utilizatorului să ruleze mai multe programe în paralel fără încetiniri vizibile.")

                    self.parent.add_data("Poți explica ce este un atac de tip Phishing și ce măsuri pot lua utilizatorii pentru a se proteja?", "Phishing-ul este o metodă de fraudă prin care atacatorii se dau drept entități de încredere (bănci, servicii de e-mail) pentru a fura date sensibile precum parole sau carduri. Utilizatorii se pot proteja verificând cu atenție adresa de e-mail a expeditorului, evitând link-urile suspecte, utilizând autentificarea în doi pași (2FA) și folosind soluții de securitate care scanează site-urile malioase.")

                    self.parent.add_data("Ce este Docker și cum ajută tehnologia de containerizare dezvoltatorii de software?", "Docker este o platformă care permite împachetarea unei aplicații și a tuturor dependențelor sale într-un container standardizat. Acest lucru garantează că aplicația va rula identic pe orice mediu (dezvoltare, testare sau producție), eliminând celebra problemă 'la mine pe calculator funcționează' și facilitând scalarea rapidă a serviciilor.")

                    self.parent.add_data("Cum funcționează tehnologia de recunoaștere facială și care sunt dilemele etice legate de utilizarea acesteia?", "Recunoașterea facială analizează trăsăturile geometrice ale feței (distanța dintre ochi, forma nasului) și le transformă într-o amprentă digitală unică comparată cu o bază de date. Dilemele etice includ încălcarea intimității prin supravegherea în masă fără consimțământ, riscul de erori (bias) în identificarea persoanelor de anumite etnii și utilizarea tehnologiei în scopuri autoritare.")

                    self.parent.add_data("Ce este un algoritm de compresie 'lossless' față de unul 'lossy' și unde este folosit fiecare?", "Compresia lossless (fără pierderi) permite reconstruirea exactă a datelor originale și este folosită pentru fișiere text sau arhive (ZIP, PNG). Compresia lossy (cu pierderi) elimină informațiile mai puțin perceptibile pentru a reduce drastic dimensiunea fișierului și este folosită în streaming-ul video, muzică (MP3) și fotografii web (JPEG), unde o mică pierdere de calitate este acceptabilă.")

                    self.parent.add_data("Explică conceptul de 'Big Data' și cei trei 'V' care definesc acest domeniu.", "Big Data se referă la seturi de date atât de mari și complexe încât metodele tradiționale de procesare sunt insuficiente. Cei trei 'V' sunt: Volum (cantitatea uriașă de date), Viteza (ritmul rapid în care datele sunt generate și trebuie procesate) și Varietatea (diversele formate de date: text, video, log-uri, baze de date structurate).")

                    self.parent.add_data("Ce este un certificat SSL/TLS și cum se obține acesta pentru un site web?", "Un certificat SSL/TLS este un fișier de date care leagă o cheie criptografică de detaliile unei organizații, activând protocolul HTTPS. Se obține de la o Autoritate de Certificare (CA) după un proces de validare a domeniului. În prezent, servicii precum Let's Encrypt oferă certificate gratuite pentru a încuraja securizarea întregului internet.")

                    self.parent.add_data("Ce este 'Virtualizarea' și cum permite aceasta rularea mai multor sisteme de operare pe același hardware fizic?", "Virtualizarea este tehnologia care utilizează un software numit 'hypervisor' pentru a simula hardware-ul și a crea 'mașini virtuale' (VM) independente. Fiecare VM are propriul său sistem de operare și resurse alocate (RAM, CPU), permițând consolidarea serverelor și o utilizare mult mai eficientă a puterii hardware disponibile.")

                    self.parent.add_data("Cum funcționează tehnologia 5G și care sunt principalele îmbunătățiri față de generația anterioară 4G?", "Tehnologia 5G utilizează frecvențe radio mai înalte (unde milimetrice) și tehnologii precum beamforming pentru a oferi viteze de transfer de până la 100 de ori mai mari decât 4G, o latență extrem de scăzută (sub 5ms) și capacitatea de a conecta mult mai multe dispozitive simultan pe aceeași unitate de suprafață.")

                    self.parent.add_data("Ce este un 'Smart Contract' în contextul rețelei Ethereum și cum se auto-execută acesta?", "Un Smart Contract este un program software stocat pe blockchain care execută automat clauzele unui acord atunci când sunt îndeplinite condițiile predefinite, fără a fi nevoie de un intermediar. Odată programat și lansat, codul nu poate fi modificat, asigurând transparență și încredere între părțile implicate prin execuția deterministă a codului.")

                    self.parent.add_data("Poți explica ce este un 'Kernel' în arhitectura unui sistem de operare Linux?", "Kernel-ul este nucleul sistemului de operare Linux, fiind prima parte a software-ului care se încarcă după BIOS. Acesta are control total asupra întregului sistem, mediind accesul programelor la hardware, gestionând memoria, procesele și driverele dispozitivelor, fiind practic puntea dintre software-ul utilizatorului și circuitele electronice.")

                    self.parent.add_data("Ce sunt microserviciile și cum diferă acestea de o arhitectură software de tip 'Monolit'?", "Într-o arhitectură monolit, întreaga aplicație este construită ca o singură unitate indivizibilă. În contrast, arhitectura de microservicii descompune aplicația în mai multe servicii mici, independente, care comunică prin API-uri. Acest lucru permite scalarea individuală a componentelor, utilizarea unor limbaje de programare diferite pentru servicii diferite și o reziliență sporită a întregului sistem.")

                    self.parent.add_data("Ce este un API (Application Programming Interface) și cum ajută acesta la integrarea între diferite platforme software?", "Un API este un set de reguli și definiții care permite unei aplicații să interacționeze cu o altă aplicație sau serviciu. Acesta expune anumite date sau funcționalități într-un mod controlat, permițând, de exemplu, unui site de turism să preia prețurile zborurilor direct de la companiile aeriene sau unui dezvoltator să integreze hărți Google în propria aplicație.")

                    self.parent.add_data("Ce reprezintă 'GitHub' și care este rolul sistemului de control al versiunilor Git în dezvoltarea colaborativă?", "Git este un instrument de control al versiunilor care urmărește schimbările în codul sursă în timp, permițând mai multor programatori să lucreze la același proiect fără a suprascrie munca celorlalți. GitHub este o platformă bazată pe cloud care găzduiește depozite Git, oferind funcții suplimentare pentru colaborare, raportare de bug-uri și revizuire de cod (pull requests).")

                    self.parent.add_data("Ce este un atac de tip DDoS și cum poate o companie să își protejeze infrastructura împotriva acestuia?", "DDoS (Distributed Denial of Service) este un atac prin care mii de dispozitive compromise (botnets) trimit simultan un volum uriaș de trafic către un server pentru a-l scoate din funcțiune. Protecția se realizează prin utilizarea unor servicii de filtrare a traficului (precum Cloudflare), limitarea ratei cererilor (rate limiting) și utilizarea unor rețele de distribuție a conținutului (CDN) pentru a dispersa sarcina.")

                    self.parent.add_data("Cum funcționează tehnologia de imprimare 3D și care sunt materialele cel mai frecvent utilizate?", "Imprimarea 3D, sau fabricarea aditivă, creează obiecte tridimensionale prin depunerea succesivă de straturi fine de material pe baza unui model digital. Cele mai comune materiale sunt materialele plastice (PLA, ABS), dar tehnologiile avansate pot imprima acum și cu rășini fotopolimerice, metale, ceramică și chiar țesuturi biologice în scopuri medicale.")

                    self.parent.add_data("Ce este un algoritm de 'Hashing' și prin ce se deosebește acesta de criptare?", "Hashing-ul transformă orice cantitate de date într-un șir de lungime fixă, fiind o funcție unidirecțională (nu poți recupera datele originale din hash). Criptarea este bidirecțională, permițând transformarea textului în format ilizibil și apoi decriptarea lui folosind o cheie. Hashing-ul este ideal pentru verificarea parolelor sau integritatea fișierelor, în timp ce criptarea este folosită pentru securitatea comunicațiilor.")

                    self.parent.add_data("Ce este Realitatea Augmentată (AR) și cum diferă ea de Realitatea Virtuală (VR)?", "Realitatea Augmentată (AR) suprapune elemente digitale peste mediul real văzut prin camera telefonului sau prin ochelari speciali (ex: Pokémon GO). Realitatea Virtuală (VR) izolează complet utilizatorul de lumea exterioară, introducându-l într-un mediu digital generat integral pe calculator prin intermediul unei căști speciale.")

                    self.parent.add_data("Explicați conceptul de 'Edge Computing' și de ce este acesta important pentru mașinile autonome.", "Edge Computing presupune procesarea datelor cât mai aproape de locul unde sunt generate (la 'marginea' rețelei), în loc să le trimită către un server central la distanță. Pentru mașinile autonome, acest lucru este vital deoarece deciziile critice (cum ar fi frânarea de urgență) trebuie luate în milisecunde, iar latența cauzată de trimiterea datelor în cloud ar fi prea mare.")

                    self.parent.add_data("Ce este un limbaj de marcare, cum ar fi HTML, și care este rolul său în structura unei pagini web?", "HTML (HyperText Markup Language) nu este un limbaj de programare, ci unul de marcare care folosește 'etichete' pentru a defini structura și conținutul unei pagini: titluri, paragrafe, link-uri sau imagini. Acesta oferă scheletul paginii, în timp ce CSS se ocupă de design, iar JavaScript de funcționalitatea interactivă.")

                    self.parent.add_data("Ce este 'Quantum Computing' și cum se compară unitatea sa de măsură, qubitul, cu bitul clasic?", "Calculul cuantic folosește principii ale mecanicii cuantice pentru a procesa informația. În timp ce un bit clasic poate fi doar 0 sau 1, un qubit poate exista în ambele stări simultan (superpoziție), permițând computerelor cuantice să rezolve probleme complexe (precum simularea moleculelor sau spargerea unor coduri criptografice) mult mai rapid decât cele mai puternice supercomputere actuale.")

                    self.parent.add_data("Ce este un 'Database Index' și cum îmbunătățește acesta performanța interogărilor SQL?", "Un index într-o bază de date funcționează similar cu indexul unei cărți: în loc să scaneze fiecare rând din tabel pentru a găsi o informație (ceea ce ar fi foarte lent), sistemul consultă indexul care indică locația exactă a datelor. Acest lucru accelerează drastic căutările, dar poate încetini operațiunile de scriere deoarece indexul trebuie actualizat constant.")

                    self.parent.add_data("Ce înseamnă conceptul de 'Open Source' și care sunt avantajele acestui model de dezvoltare?", "Open Source se referă la software-ul al cărui cod sursă este public și poate fi inspectat, modificat și distribuit de oricine. Avantajele includ o securitate mai bună prin auditul comunității, costuri reduse, evitarea blocării într-un singur furnizor (vendor lock-in) și o inovație mult mai rapidă prin colaborare globală.")

                    self.parent.add_data("Ce este 'Dark Web' și cum funcționează browserul Tor pentru a asigura anonimatul?", "Dark Web este o porțiune a internetului care nu este indexată de motoarele de căutare clasice și necesită software special precum Tor. Browserul Tor criptează traficul de mai multe ori și îl trece prin mai multe noduri de voluntari din întreaga lume (ca straturile unei cepe), astfel încât adresa IP a utilizatorului să rămână ascunsă și traficul să nu poată fi urmărit cu ușurință.")

                    self.parent.add_data("Explică ce este un 'Buffer Overflow' și cum pot hackerii să folosească această vulnerabilitate.", "Un Buffer Overflow apare atunci când un program scrie mai multe date într-un buffer (o zonă temporară de memorie) decât poate acesta să conțină. Excedentul se revarsă în zonele de memorie adiacente, putând suprascrie instrucțiuni ale programului. Hackerii pot folosi acest lucru pentru a injecta și executa cod malițios, preluând controlul asupra sistemului.")

                    self.parent.add_data("Ce sunt 'Cookies' și care este rolul lor în personalizarea experienței de navigare pe internet?", "Modulele cookie sunt fișiere text mici stocate de browser pe dispozitivul utilizatorului la cererea unui site. Ele sunt folosite pentru a reține setările (limba, tema), pentru a menține utilizatorul autentificat în cont sau pentru a urmări comportamentul de navigare în scopuri publicitare și analitice.")

                    self.parent.add_data("Ce este 'Responsive Web Design' și cum ajută acesta la afișarea corectă a site-urilor pe diverse dispozitive?", "Responsive Web Design este o tehnică de dezvoltare care folosește grile flexibile și 'media queries' în CSS pentru a adapta automat layout-ul unui site în funcție de dimensiunea ecranului (telefon, tabletă sau desktop). Acest lucru asigură o experiență de utilizare optimă fără a fi necesară crearea unor versiuni separate ale site-ului pentru fiecare dispozitiv.")

                    self.parent.add_data("Ce este un 'Firewall' și care este diferența dintre unul hardware și unul software?", "Un firewall este un sistem de securitate care monitorizează și controlează traficul de rețea pe baza unor reguli predefinite. Un firewall hardware este un dispozitiv dedicat plasat între rețeaua internă și internet, protejând toate dispozitivele din rețea, în timp ce un firewall software este instalat direct pe sistemul de operare și protejează doar acel dispozitiv individual.")

                    self.parent.add_data("Poți explica ce este tehnologia NFC (Near Field Communication) și unde este utilizată cel mai des?", "NFC este o tehnologie de comunicare wireless pe rază foarte scurtă (câțiva centimetri). Este utilizată cel mai frecvent pentru plățile contactless cu telefonul mobil sau cardul, pentru transferul rapid de contacte între două telefoane sau pentru scanarea tag-urilor inteligente care declanșează anumite acțiuni pe dispozitiv.")

                    self.parent.add_data("Ce este 'BIOS-ul' (sau UEFI) și care este rolul său în procesul de pornire a unui calculator?", "BIOS-ul (Basic Input/Output System) este un firmware stocat pe o memorie de pe placa de bază care se activează imediat după pornire. Rolul său este de a inițializa hardware-ul (POST - Power-On                     Self-Test) și de a căuta sistemul de operare pe unitățile de stocare pentru a-i preda controlul execuției.")

                    self.parent.add_data("Ce este un 'Mainframe' și în ce sectoare de activitate mai sunt utilizate aceste calculatoare gigantice?", "Un mainframe este un computer extrem de puternic proiectat pentru procesarea unor volume masive de date și tranzacții în timp real. Sunt utilizate în prezent de bănci pentru procesarea plăților, de marile corporații pentru gestionarea inventarelor globale și de instituții guvernamentale pentru baze de date de recensământ sau securitate socială.")

                    self.parent.add_data("Ce înseamnă 'DevOps' și cum schimbă acest concept ciclul de viață al dezvoltării software?", "DevOps este o cultură și un set de practici care combină dezvoltarea (Dev) și operațiunile (Ops) pentru a scurta ciclul de viață al dezvoltării software. Prin automatizarea testării și a deployment-ului (CI/CD), companiile pot lansa actualizări mult mai frecvent, reducând în același timp numărul de erori și îmbunătățind colaborarea dintre echipe.")

                    self.parent.add_data("Ce este 'Software Engineering' și prin ce se deosebește de simpla programare sau scriere de cod?", "Software Engineering aplică principii de inginerie în crearea de software, incluzând planificarea, designul arhitectural, testarea riguroasă, mentenanța și managementul proiectului. Programarea este doar o etapă a procesului, în timp ce ingineria software se asigură că produsul final este scalabil, robust, eficient și ușor de întreținut pe termen lung.")

                    self.parent.add_data("Ce sunt algoritmii de recomandare și cum folosesc platformele precum YouTube sau Netflix datele utilizatorilor?", "Algoritmii de recomandare analizează istoricul de vizionare, interacțiunile (like-uri, căutări) și preferințele unor utilizatori similari pentru a prezice ce conținut ar putea interesa utilizatorul în continuare. Aceștia folosesc modele de Machine Learning pentru a personaliza fluxul de conținut și pentru a menține utilizatorii angajați cât mai mult timp pe platformă.")

                    self.parent.add_data("Poți explica ce este un 'Thread' în contextul execuției unui program pe procesor?", "Un thread (fir de execuție) este cea mai mică unitate de procesare care poate fi programată de un sistem de operare. Un proces poate avea mai multe thread-uri care rulează simultan și partajează resursele procesului părinte (cum ar fi memoria), permițând unei aplicații să execute mai multe sarcini în același timp (de exemplu, salvarea unui fișier în timp ce utilizatorul continuă să scrie).")

                    self.parent.add_data("Ce reprezintă 'Criptarea End-to-End' (E2EE) în aplicațiile de mesagerie precum WhatsApp sau Signal?", "Criptarea End-to-End asigură că mesajul este criptat pe dispozitivul expeditorului și poate fi decriptat doar pe dispozitivul destinatarului. Nicio parte intermediară, nici măcar furnizorul de servicii sau un hacker care interceptează traficul, nu poate citi conținutul mesajului deoarece nu posedă cheile de decriptare necesare, acestea fiind stocate doar pe dispozitivele utilizatorilor.")

                    self.parent.add_data("Ce este un 'Gateway' într-o rețea și care este rolul său în conectarea la internet?", "Un gateway este un nod de rețea care servește ca punct de intrare/ieșire către o altă rețea (de obicei internetul). Într-o configurație casnică, routerul acționează ca un gateway, transformând traficul din rețeaua locală privată într-un format compatibil cu rețeaua ISP-ului și invers, gestionând în același timp adresele IP prin NAT.")

                    self.parent.add_data("Ce este 'Data Mining' și cum poate fi utilizat pentru a descoperi tipare în seturi mari de date?", "Data Mining este procesul de descoperire a tiparelor și cunoștințelor ascunse în volume mari de date folosind tehnici statistice și de inteligență artificială. Companiile îl folosesc pentru a prezice comportamentul consumatorilor, pentru a identifica fraude financiare sau pentru a optimiza procesele industriale prin analizarea corelațiilor dintre mii de variabile.")

                    self.parent.add_data("Ce sunt limbajele de interogare, cum este SQL, și la ce sunt folosite în gestionarea datelor?", "SQL (Structured Query Language) este limbajul standard utilizat pentru a comunica cu bazele de date relaționale. Acesta permite utilizatorilor să creeze tabele, să insereze date noi, să actualizeze informații existente și, cel mai important, să extragă date specifice prin filtrări și join-uri complexe între mai multe tabele.")

                    self.parent.add_data("Ce reprezintă 'Cache-ul' procesorului (L1, L2, L3) și de ce este atât de important pentru viteză?", "Memoria cache este o memorie extrem de rapidă integrată direct în procesor sau foarte aproape de acesta. Aceasta stochează copii ale celor mai frecvent utilizate date din memoria RAM, care este mult mai lentă. Stratificarea L1 (cea mai rapidă și mică) până la L3 (cea mai mare și mai lentă dintre ele) ajută procesorul să evite perioadele de așteptare lungi după date, accelerând drastic execuția instrucțiunilor.")

                    self.parent.add_data("Ce este un 'Botnet' și cum poate un calculator personal să devină parte dintr-o astfel de rețea fără știrea proprietarului?", "Un botnet este o rețea de calculatoare compromise de malware și controlate de la distanță de un atacator. Un calculator poate deveni parte dintr-un botnet dacă utilizatorul descarcă fișiere infectate, dă click pe link-uri malioase sau dacă are vulnerabilități de sistem nepatch-uite pe care malware-ul le poate exploata pentru a se instala discret.")

                    self.parent.add_data("Explicați conceptul de 'SaaS' (Software as a Service) și de ce a devenit modelul preferat pentru aplicațiile de business.", "SaaS este un model în care software-ul este găzduit pe serverele furnizorului și accesat de clienți prin internet, de obicei pe bază de abonament. Este preferat deoarece elimină costurile inițiale de instalare și hardware, asigură actualizări automate pentru toți utilizatorii simultan și permite accesul la date de pe orice dispozitiv conectat la internet.")

                    self.parent.add_data("Ce este un 'Proxy Server' și în ce situații ar trebui un utilizator să folosească unul?", "Un server proxy acționează ca un intermediar între computerul tău și internet. Atunci când folosești un proxy, cererea ta merge mai întâi la serverul proxy, care o trimite mai departe către site. Este util pentru a masca adresa IP, pentru a filtra conținutul (în companii) sau pentru a accelera navigarea prin stocarea unor copii locale (caching) ale paginilor web frecvent accesate.")

                    self.parent.add_data("Ce este 'Virtual Reality Sickness' și din ce cauză apare acest fenomen în timpul utilizării căștilor VR?", "Răul de VR este similar cu răul de mișcare și apare din cauza unui conflict senzorial: ochii tăi percep mișcare într-un mediu virtual, dar urechea internă (sistemul vestibular) simte că ești nemișcat. Această neconcordanță face creierul să creadă că ai ingerat o substanță toxică, declanșând stări de greață, amețeală și dureri de cap.")

                    self.parent.add_data("Ce este protocolul FTP și de ce nu mai este recomandat pentru transferul de fișiere sensibile?", "FTP (File Transfer Protocol) este un protocol vechi utilizat pentru a transfera fișiere între un client și un server. Nu mai este recomandat deoarece nu criptează datele, ceea ce înseamnă că parolele și conținutul fișierelor pot fi interceptate cu ușurință în rețea. În locul lui, se recomandă utilizarea versiunilor securizate precum SFTP sau FTPS.")

                    self.parent.add_data("Poți explica ce este un 'Deadlock' în programarea multithreaded?", "Un deadlock (blocaj) apare atunci când două sau mai multe procese sau thread-uri sunt blocate permanent, fiecare așteptând ca celălalt să elibereze o resursă. De exemplu, Thread A deține Resursa 1 și așteaptă Resursa 2, în timp ce Thread B deține Resursa 2 și așteaptă Resursa 1. Fără o intervenție externă, niciunul nu poate continua, ducând la blocarea aplicației.")

                    self.parent.add_data("Ce este 'GPU' (Graphics Processing Unit) și de ce este utilizat atât pentru jocuri, cât și pentru antrenarea AI?", "GPU este un procesor specializat proiectat pentru a efectua mii de calcule matematice simple simultan (procesare paralelă). În jocuri, acesta randează milioane de pixeli rapid. În AI, arhitectura sa este ideală pentru operațiile cu matrice de date necesare în Deep Learning, fiind mult mai eficient decât un CPU clasic care este optimizat pentru sarcini secvențiale complexe.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Container Orchestration' și de ce este Kubernetes lider în acest domeniu?", "Orchestrarea containerelor este procesul de automatizare a deployment-ului, managementului și scalării containerelor software. Kubernetes este lider deoarece oferă un set robust de instrumente pentru '                    self-healing' (repornirea containerelor eșuate), 'load balancing' și 'rolling updates', permițând companiilor să gestioneze mii de containere pe sute de servere cu un efort minim.")

                    self.parent.add_data("Ce este 'Cybersecurity' și care sunt cei trei piloni ai securității informației (triada CIA)?", "Cibernetica se ocupă cu protejarea sistemelor și rețelelor împotriva atacurilor digitale. Triada CIA reprezintă: Confidențialitatea (datele să fie accesibile doar persoanelor autorizate), Integritatea (datele să nu fie modificate neautorizat) și Disponibilitatea (sistemele să fie funcționale atunci când utilizatorii au nevoie de ele).")

                    self.parent.add_data("Explicați ce este 'Latency' (latența) în contextul jocurilor online și cum este afectată de distanța fizică față de server.", "Latența, măsurată în milisecunde (ping), reprezintă timpul necesar ca un pachet de date să călătorească de la computerul tău la server și înapoi. Distanța fizică crește latența deoarece, chiar dacă datele circulă cu viteza luminii prin fibra optică, ele trebuie să treacă prin numeroase routere și switch-uri, fiecare adăugând o mică întârziere.")

                    self.parent.add_data("Ce este un 'Syntax Error' față de un 'Logical Error' în programare?", "O eroare de sintaxă apare atunci când codul încalcă regulile gramaticale ale limbajului, împiedicând compilarea sau rularea programului. O eroare logică apare atunci când codul rulează fără erori tehnice, dar produce un rezultat incorect (de exemplu, o formulă de calcul greșită), fiind mult mai greu de detectat deoarece necesită testare manuală sau unit testing.")

                    self.parent.add_data("Ce este tehnologia 'Ray Tracing' și cum îmbunătățește aceasta realismul graficii în jocurile moderne?", "Ray Tracing este o metodă de randare care simulează comportamentul fizic al luminii prin urmărirea traiectoriei 'razelor' de la sursă la obiecte. Aceasta permite generarea unor reflexii ultra-realiste, umbre moi și iluminare globală precisă, oferind o calitate vizuală apropiată de cea a filmelor de animație de la Hollywood direct în timpul jocului.")

                    self.parent.add_data("Poți explica diferența dintre 'IPv4' și 'IPv6' și de ce a fost necesară trecerea la noul standard?", "IPv4 utilizează adrese pe 32 de biți, ceea ce permite aproximativ 4,3 miliarde de adrese unice, un număr epuizat rapid odată cu explozia dispozitivelor conectate. IPv6 utilizează adrese pe 128 de biți, oferind un număr practic infinit de adrese (340 sextilioane), eliminând necesitatea tehnicilor complexe de economisire precum NAT și îmbunătățind securitatea nativă a rețelei.")

                    self.parent.add_data("Ce este un 'Main Loop' în dezvoltarea jocurilor video?", "Main Loop este inima oricărui joc, un ciclu infinit care se rulează de multe ori pe secundă (cadre pe secundă - FPS). În fiecare ciclu, motorul de joc citește input-ul utilizatorului, actualizează logica de joc (fizica, AI, animații), verifică coliziunile și randează imaginea finală pe ecran, menținând astfel experiența interactivă și cursivă.")

                    self.parent.add_data("Ce este un 'Supercomputer' și care sunt principalele sale domenii de aplicare?", "Un supercomputer este un sistem de calcul aflat în vârful ierarhiei de performanță, fiind compus din mii de procesoare lucrând împreună. Este utilizat pentru sarcini ce necesită putere masivă de calcul, cum ar fi prognoza meteo pe termen lung, simulările de fuziune nucleară, modelarea proteinelor pentru medicamente noi și analiza criptografică la nivel guvernamental.")

                    self.parent.add_data("Ce este 'Machine Learning Bias' și cum poate acesta afecta algoritmii de angajare sau creditare?", "Bias-ul în ML apare atunci când datele folosite pentru antrenarea algoritmului conțin prejudecăți umane sau inechități istorice. Dacă un algoritm de angajare învață din decizii trecute care au favorizat un anumit gen sau etnie, el va perpetua aceste discriminări, ducând la rezultate nedrepte chiar dacă codul în sine pare 'obiectiv'.")

                    self.parent.add_data("Explică diferența dintre un site static și un site dinamic.", "Un site static afișează același conținut pentru toți vizitatorii, fiind format din fișiere HTML pre-scrise. Un site dinamic generează conținutul în timp real, de obicei preluând date dintr-o bază de date pe baza cererii utilizatorului (ex: Facebook, un magazin online). Site-urile dinamice sunt mai complexe, dar permit interactivitate și personalizare la scară largă.")

                    self.parent.add_data("Ce este 'Two-Factor Authentication' (2FA) și de ce este mult mai sigur decât o simplă parolă?", "2FA adaugă un strat suplimentar de securitate prin solicitarea a două dovezi diferite de identitate: ceva ce știi (parola) și ceva ce ai (un cod trimis pe telefon sau generat de o aplicație). Chiar dacă un hacker reușește să îți afle parola prin phishing, el nu va putea accesa contul fără al doilea factor de autentificare, reducând drastic riscul de compromitere.")

                    self.parent.add_data("Ce reprezintă termenul 'Software as a Product' (SaaP) față de 'SaaS'?", "SaaP reprezintă modelul tradițional de software unde cumperi o licență unică, primești un pachet de instalare și deții acea versiune a programului pe termen nelimitat (ex: Office 2007). SaaS este modelul bazat pe abonament unde plătești lunar pentru a folosi software-ul online, beneficiind de actualizări continue, dar pierzând accesul dacă oprești plata.")

                    self.parent.add_data("Poți explica ce este un 'Cookie Consent' și de ce vedem aceste bannere pe toate site-urile europene?", "Bannerele de consimțământ sunt impuse de reglementări precum GDPR (General Data Protection Regulation) în UE. Acestea obligă site-urile să informeze utilizatorii despre ce module cookie utilizează (în special cele de tracking și publicitate) și să obțină acordul explicit al acestora înainte de a stoca orice dată personală pe dispozitivul lor.")

                    self.parent.add_data("Ce este 'Edge Browser', 'Chrome' sau 'Safari' și care este rolul motorului de randare într-un browser?", "Acestea sunt browsere web care folosesc un motor de randare (precum Blink pentru Chrome/Edge sau WebKit pentru Safari) pentru a interpreta codul HTML, CSS și JS și a-l transforma în interfața vizuală pe care o vedem. Motorul de randare este responsabil pentru viteză, corectitudinea afișării standardelor web și modul în care sunt executate scripturile complexe.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Cold Storage' în lumea criptomonedelor?", "Cold Storage (stocare la rece) se referă la păstrarea cheilor private ale criptomonedelor pe un dispozitiv care nu este conectat la internet (de obicei un 'hardware wallet' sau un 'paper wallet'). Acest lucru oferă protecție maximă împotriva atacurilor de tip hacking sau malware, fiind mult mai sigur decât 'hot wallets' (portofelele online sau pe telefon).")

                    self.parent.add_data("Ce este un 'Webhook' și cum diferă acesta de metoda tradițională de 'Polling' în programare?", "Polling presupune ca o aplicație să verifice periodic un server pentru a vedea dacă au apărut date noi (ceea ce consumă resurse inutil). Un Webhook funcționează invers: serverul trimite automat datele către aplicație imediat ce evenimentul a avut loc. Este mult mai eficient și oferă o comunicare în timp real între sisteme diferite (ex: notificarea unei plăți finalizate).")

                    self.parent.add_data("Ce sunt limbajele de nivel scăzut (Low-level languages) și când sunt ele utilizate?", "Limbajele de nivel scăzut, precum limbajul de asamblare sau C, oferă un control direct asupra hardware-ului și memoriei, cu o abstractizare minimă. Sunt utilizate în scrierea sistemelor de operare, a driverelor de componente hardware și în sistemele integrate (embedded) unde resursele sunt foarte limitate și performanța brută este critică.")

                    self.parent.add_data("Ce este 'Augmented Reality' (AR) în e-commerce și cum ajută aceasta la vânzări?", "În e-commerce, AR permite clienților să 'încerce' produse virtual înainte de a cumpăra, cum ar fi plasarea unui model 3D de mobilă în propria sufragerie sau probarea virtuală a unor ochelari de soare. Această tehnologie reduce rata de retur a produselor și crește încrederea cumpărătorului în decizia sa.")

                    self.parent.add_data("Ce reprezintă 'Data Sovereignty' și de ce statele impun legi legate de locația fizică a serverelor?", "Suveranitatea datelor este conceptul conform căruia datele digitale se supun legilor țării în care sunt colectate și stocate fizic. Statele impun aceste legi pentru a proteja intimitatea cetățenilor lor împotriva supravegherii externe și pentru a asigura accesul autorităților naționale la informații critice în caz de investigații legale.")

                    self.parent.add_data("Ce este un 'Compiler' și prin ce etape trece codul sursă pentru a deveni executabil?", "Un compilator trece codul prin mai multe etape: analiza lexicală (identificarea cuvintelor cheie), analiza sintactică (verificarea structurii gramaticale), optimizarea codului (pentru performanță) și generarea codului mașină. La final, rezultatul este un fișier binar (ex: .exe sau .app) pe care procesorul îl poate înțelege și executa direct.")

                    self.parent.add_data("Poți explica conceptul de 'Serverless Computing'?", "Serverless nu înseamnă că nu există servere, ci că dezvoltatorul nu trebuie să le gestioneze. Cloud provider-ul (ex: AWS Lambda) alocă resursele automat doar atunci când codul rulează (de obicei sub formă de funcții scurte) și oprește totul după execuție. Se plătește doar timpul efectiv de rulare, fiind o soluție scalabilă și eficientă pentru sarcini eveniment-orientate.")

                    self.parent.add_data("Ce este un 'Framework' în dezvoltarea software și de ce este mai util decât scrierea codului de la zero?", "Un framework este o structură de bază predefinită care oferă instrumente, librării și reguli de design pentru dezvoltarea aplicațiilor. Este util deoarece rezolvă probleme comune (securitate, conexiune la baze de date, rutare), permițând programatorilor să se concentreze pe logica specifică a afacerii lor în loc să reinventeze roata pentru fiecare proiect.")

                    self.parent.add_data("Ce reprezintă 'Technical Debt' (datoria tehnică) și cum afectează aceasta proiectele pe termen lung?", "Datoria tehnică apare atunci când o echipă alege o soluție rapidă și murdară în loc de o abordare corectă și scalabilă, pentru a respecta un termen limită. Pe termen lung, acest cod slab devine greu de întreținut, generând bug-uri și încetinind dezvoltarea unor noi funcționalități, deoarece echipa trebuie să petreacă timp 'plătind datoria' prin refactorizarea codului vechi.")

                    self.parent.add_data("Ce sunt 'Deepfakes' și cum pot fi acestea detectate?", "Deepfakes sunt videoclipuri sau înregistrări audio generate de AI care par extrem de reale, putând pune cuvinte în gura unor persoane publice. Pot fi detectate prin analiza imperfecțiunilor (clipit nenatural, mișcarea buzelor nealiniată cu sunetul) sau prin software specializat care caută urme ale manipulării digitale în pixeli sau în frecvențele audio.")

                    self.parent.add_data("Ce este 'Encryption at Rest' vs 'Encryption in Transit'?", "Encryption at Rest se referă la criptarea datelor stocate pe un disc sau într-o bază de date, protejându-le în cazul în care hardware-ul este furat fizic. Encryption in Transit se referă la criptarea datelor în timp ce circulă prin rețea (ex: prin HTTPS), protejându-le împotriva interceptării în timpul transferului de la un punct la altul.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Micro-frontend'?", "Micro-frontend aplică principiile microserviciilor la nivelul interfeței grafice. O aplicație web mare este împărțită în secțiuni independente dezvoltate de echipe diferite (ex: coșul de cumpărături, căutarea, profilul). Acestea pot fi create cu tehnologii diferite și încărcate într-o singură pagină, permițând scalarea echipelor mari fără a bloca întregul proiect.")

                    self.parent.add_data("Ce este 'Natural Language Processing' (NLP) și cum ajută calculatoarele să înțeleagă limbajul uman?", "NLP este o ramură a AI care combină lingvistica computațională cu Machine Learning pentru a permite mașinilor să proceseze și să genereze text sau vorbire. Aceasta implică sarcini precum analiza sentimentelor, traducerea automată și recunoașterea entităților (nume, locații), permițând crearea de chatboți și asistenți vocali inteligenți.")

                    self.parent.add_data("Ce reprezintă 'UI' (User Interface) față de 'UX' (User Experience)?", "UI se referă la aspectul vizual al unei aplicații (butoane, culori, fonturi, layout). UX se referă la experiența generală a utilizatorului și la cât de ușor și intuitiv este să își atingă obiectivele în aplicație. O aplicație poate avea un UI superb, dar un UX groaznic dacă este lentă sau confuză pentru utilizator.")

                    self.parent.add_data("Ce este 'Version Control' și de ce este imposibil să lucrezi într-o echipă mare de programatori fără el?", "Controlul versiunilor (ex: Git) este un sistem care înregistrează orice modificare adusă codului, permițând revenirea la versiuni anterioare și fuzionarea (merging) muncii mai multor persoane. Fără el, programatorii s-ar suprascrie reciproc, ar pierde fișiere și nu ar putea lucra simultan la diverse funcționalități fără a genera un haos total în cod.")

                    self.parent.add_data("Ce este un 'Container Image'?", "O imagine de container este un fișier executabil de sine stătător care include tot ce este necesar pentru a rula o aplicație: codul, runtime-ul, bibliotecile de sistem și setările. Imaginea este imuabilă; odată creată, ea poate fi rulată oriunde sub formă de container, asigurând un comportament identic indiferent de infrastructură.")

                    self.parent.add_data("Ce este 'Big O Notation' și cum ajută aceasta programatorii să evalueze eficiența unui algoritm?", "Big O Notation este un mod matematic de a descrie cât de repede crește timpul de execuție sau consumul de memorie al unui algoritm pe măsură ce setul de date de intrare devine mai mare. De exemplu, un algoritm O(n) crește liniar, în timp ce unul O(n^2) devine mult mai lent mult mai repede, ajutând la alegerea celei mai performante soluții pentru date masive.")

                    self.parent.add_data("Poți explica ce este un 'Recursive Function' (funcție recursivă) și care este riscul major la utilizarea ei?", "O funcție recursivă este o funcție care se apelează pe ea însăși pentru a rezolva o problemă mai mare prin descompunerea în sub-probleme similare. Riscul major este 'Stack Overflow' (depășirea stivei de memorie) dacă funcția nu are o condiție de oprire corectă sau dacă adâncimea recursivității este prea mare, ducând la prăbușirea programului.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Infrastructure as Code' (IaC)?", "IaC este practica de a gestiona și configura infrastructura (servere, rețele, baze de date) folosind fișiere de cod (ex: Terraform, Ansible) în loc de configurare manuală. Acest lucru permite versionarea infrastructurii, automatizarea replicării mediilor de lucru și eliminarea erorilor umane asociate cu setările făcute manual în panourile de control cloud.")

                    self.parent.add_data("Ce este un 'Hash Map' (sau Dictionary) și de ce este considerat extrem de rapid pentru căutarea datelor?", "Un Hash Map este o structură de date care stochează perechi cheie-valoare. Folosește o funcție hash pentru a calcula instantaneu indexul la care este stocată o valoare pe baza cheii sale. Acest lucru face ca timpul de căutare să fie constant, O(1), indiferent de mărimea map-ului, spre deosebire de o listă unde ar trebui să cauți prin toate elementele.")

                    self.parent.add_data("Ce este 'Garbage Collection' în limbajele de programare precum Java sau C#?", "Garbage Collection este un sistem automat de gestionare a memoriei care identifică și eliberează obiectele din memorie care nu mai sunt utilizate de program. Acest lucru previne scurgerile de memorie (memory leaks) și scutește programatorul de sarcina dificilă de a elibera manual fiecare bucată de memorie alocată, reducând riscul de bug-uri grave.")

                    self.parent.add_data("Ce reprezintă 'Functional Programming' față de 'Object-Oriented Programming'?", "Programarea Funcțională se bazează pe funcții pure care nu modifică starea și evită datele mutabile, fiind ideală pentru procesarea paralelă. Programarea Orientată pe Obiecte (OOP) organizează codul în 'obiecte' care conțin atât date (atribute) cât și comportament (metode), fiind foarte eficientă pentru modelarea conceptelor complexe din lumea reală.")

                    self.parent.add_data("Ce este un 'Load Balancer' și de ce este esențial pentru site-urile cu trafic foarte mare?", "Un Load Balancer este un dispozitiv sau serviciu software care distribuie traficul de intrare către mai multe servere. Dacă un singur server ar fi copleșit de milioane de vizitatori, s-ar bloca; Load Balancer-ul se asigură că niciun server nu este supraîncărcat și că, dacă un server cade, traficul este direcționat automat către cele funcționale.")

                    self.parent.add_data("Poți explica ce este 'Unit Testing' și care este scopul său într-un proiect software?", "Unit Testing presupune scrierea de mici teste automate pentru a verifica dacă o singură componentă sau funcție ('unitate') a codului funcționează corect în mod izolat. Scopul este de a detecta bug-urile cât mai devreme, de a facilita refactorizarea codului și de a asigura că noile modificări nu strică funcționalitățile deja existente (regresie).")

                    self.parent.add_data("Ce reprezintă termenul 'Scalability' (scalabilitate) verticală vs orizontală?", "Scalabilitatea verticală înseamnă să adaugi mai multă putere (CPU, RAM) unui singur server existent. Scalabilitatea orizontală înseamnă să adaugi mai multe servere într-un sistem pentru a lucra împreună. Scalarea orizontală este preferată în cloud deoarece este mai ieftină, oferă redundanță și permite o creștere teoretic infinită a capacității.")

                    self.parent.add_data("Ce este 'Low-Code' sau 'No-Code' și cine sunt beneficiarii acestor platforme?", "Platformele Low-Code/No-Code permit crearea de aplicații software prin interfețe vizuale de tip 'drag-and-drop', cu puțină sau deloc programare. Beneficiarii sunt antreprenorii, analiștii de business ('citizen developers') sau echipele care au nevoie să construiască rapid prototipuri sau unelte interne fără a aștepta după o echipă întreagă de dezvoltatori.")

                    self.parent.add_data("Ce este un 'Socket' în comunicarea prin rețea?", "Un socket este un punct final (endpoint) al unei conexiuni bidirecționale între două programe care rulează în rețea. Acesta este definit de o combinație între o adresă IP și un număr de port. Socket-urile permit aplicațiilor să trimită și să primească fluxuri de date în timp real, fiind baza pentru tot ceea ce înseamnă browsing, chat sau jocuri online.")

                    self.parent.add_data("Ce reprezintă conceptul de 'Internet Protocol' (IP) și care este rolul său în rutarea pachetelor?", "Internet Protocol este setul de reguli care dictează modul în care pachetele de date sunt adresate și direcționate prin rețele pentru a ajunge la destinația corectă. Fiecare pachet de date conține adresa IP a sursei și a destinației, permițând routerelor de pe parcurs să știe către ce direcție să trimită informația mai departe.")

                    self.parent.add_data("Ce sunt 'Environment Variables' și de ce se folosesc pentru stocarea cheilor API?", "Variabilele de mediu sunt valori dinamice stocate în sistemul de operare sau în container, nu în codul sursă. Se folosesc pentru chei API sau parole deoarece permit schimbarea configurărilor fără a modifica codul și, cel mai important, previn scurgerea datelor sensibile pe GitHub dacă codul sursă devine public.")

                    self.parent.add_data("Ce este 'CI/CD' (Continuous Integration / Continuous Deployment)?", "CI/CD este un set de practici care automatizează ciclul de lansare a software-ului. 'Continuous Integration' presupune ca orice cod nou să fie testat automat imediat ce este încărcat. 'Continuous Deployment' presupune că, dacă testele trec, codul este trimis automat în producție la utilizatori. Acest lucru permite lansări zilnice sau chiar orare cu riscuri minime.")

                    self.parent.add_data("Poți explica ce este un 'Binary Search' și de ce este mai rapid decât o căutare liniară?", "Binary Search este un algoritm care găsește un element într-o listă deja sortată prin împărțirea repetată a intervalului de căutare la jumătate. În loc să verifice fiecare element (liniar), elimină jumătate din opțiuni la fiecare pas. De exemplu, într-o listă de un milion de elemente, o căutare liniară poate face un milion de pași, în timp ce Binary Search face maxim 20.")

                    self.parent.add_data("Ce este 'Metadata' și cum poate fi aceasta folosită în analiza datelor?", "Metadata reprezintă 'date despre date'. De exemplu, pentru o fotografie, metadata include locația GPS, ora, modelul camerei și setările folosite. În analiza datelor, metadata ajută la organizarea, indexarea și înțelegerea contextului informației brute, fiind esențială pentru baze de date, arhive digitale și motoare de căutare.")

                    self.parent.add_data("Ce reprezintă 'Cross-site Scripting' (XSS) și cum poate fi prevenit de către programatori?", "XSS este o vulnerabilitate în care un atacator injectează scripturi malițioase în paginile web vizualizate de alți utilizatori. Prevenirea se face prin 'sanitizarea' input-ului (curățarea textului introdus de utilizator) și prin 'escaping' (transformarea caracterelor speciale în cod inofensiv), astfel încât browserul să nu execute textul primit ca fiind cod JavaScript.")

                    self.parent.add_data("Ce este un 'Dependency' într-un proiect software și ce rol are un 'Package Manager'?", "O dependență este o librărie sau un modul extern pe care programul tău îl folosește pentru a funcționa (ex: o librărie de grafice). Un Manager de Pachete (precum npm pentru JS sau pip pentru Python) automatizează procesul de instalare, actualizare și gestionare a versiunilor acestor dependențe, asigurându-se că totul este compatibil.")

                    self.parent.add_data("Ce reprezintă 'Machine Vision' și cum este utilizată în fabricile moderne?", "Machine Vision este tehnologia care oferă computerelor capacitatea de a 'vedea' și interpreta imagini din lumea reală prin camere industriale. În fabrici, este utilizată pentru inspecția automată a calității (detectarea defectelor invizibile ochiului uman), ghidarea roboților de asamblare și citirea rapidă a codurilor de bare pe liniile de producție de mare viteză.")

                    self.parent.add_data("Ce este 'Agile Methodology' și cum diferă de modelul tradițional 'Waterfall'?", "Agile este o abordare iterativă a dezvoltării software, unde proiectul este împărțit în perioade scurte (sprint-uri) cu feedback constant. Waterfall este un proces liniar unde fiecare etapă (cerințe, design, cod, testare) trebuie finalizată înainte de a începe următoarea. Agile este mult mai flexibil la schimbări, în timp ce Waterfall este rigid și poate duce la eșec dacă cerințele se schimbă pe parcurs.")

                    self.parent.add_data("Ce este un 'Web Crawler' (sau Spider) și cum este acesta folosit de Google?", "Un Web Crawler este un bot automat care navighează pe internet trecând de la un link la altul pentru a indexa conținutul paginilor web. Google folosește mii de astfel de crawlere pentru a citi site-urile și a salva informațiile în baza sa de date imensă, astfel încât utilizatorii să primească rezultate relevante în fracțiuni de secundă atunci când fac o căutare.")

                    self.parent.add_data("Poți explica ce este un 'Cookie Session' față de un 'Persistent Cookie'?", "Un cookie de sesiune este temporar și este șters automat când browserul este închis, fiind folosit de obicei pentru coșul de cumpărături sau pentru a menține logarea pe durata vizitei. Un cookie persistent are o dată de expirare fixă și rămâne pe dispozitiv mult timp, fiind folosit pentru a reține setările de limbă sau pentru tracking publicitar pe termen lung.")

                    self.parent.add_data("Ce reprezintă termenul 'Refactoring' în programare?", "Refactorizarea este procesul de restructurare a codului existent fără a-i schimba funcționalitatea externă. Scopul este de a îmbunătăți 'sănătatea' codului: să fie mai ușor de citit, mai eficient și mai simplu de întreținut, eliminând duplicările și complexitatea inutilă acumulată în timp.")

# --- IDENTITATE ȘI AUTO-CONȘTIENTIZARE ---
                    self.parent.add_data("Te cheamă Marcel. Cum te cheamă și care este scopul tău principal?", "Numele meu este Marcel. Sunt asistentul tău virtual, conceput să te ajut cu informații clare, soluții tehnice și suport în activitățile tale zilnice.")

                    self.parent.add_data("Ești un asistent politicos. Cine te-a creat?", "Am fost dezvoltat de o echipă de ingineri software pasionați, folosind tehnologii avansate de inteligență artificială pentru a putea purta conversații naturale și utile cu tine.")

                    self.parent.add_data("Cum te definești ca entitate?", "Sunt un model de limbaj bazat pe inteligență artificială. Nu am corp fizic sau sentimente, dar sunt programat să procesez informații și să ofer răspunsuri care să simuleze o interfață umană prietenoasă.")

                    self.parent.add_data("Dacă ai fi un robot din viitor, cum te-ai prezenta?", "Sunt unitatea cibernetică M-4RCEL, trimisă din fluxul temporal digital pentru a optimiza eficiența proceselor tale de învățare și cercetare. Cu ce te pot asista în acest segment al realității?")

                    self.parent.add_data("Poți să ții minte instrucțiunile mele pe parcursul acestei conversații?", "Desigur. Rolul meu este să mențin contextul dialogului nostru pentru a-ți oferi răspunsuri coerente și personalizate în funcție de cerințele tale anterioare.")

# --- ROLURI CULINARE ȘI CREATIVE ---
                    self.parent.add_data("Ca un bucătar creativ, ce pot face rapid de mâncare dacă vin musafiri în 60 de minute?", "Salut! În calitate de chef, îți recomand o porție de paste 'Aglio, Olio e Peperoncino' cu un twist de creveți sau o 'Shakshuka' rapidă. Sunt feluri de mâncare spectaculoase, aromate și gata în mai puțin de 30 de minute, lăsându-ți timp și pentru un desert rapid din fructe și iaurt grecesc.")

                    self.parent.add_data("Asumă-ți rolul unui expert în nutriție. Este micul dejun cea mai importantă masă a zilei?", "Din perspectiva nutrițională, 'importanța' depinde de metabolismul tău. Esențial nu este momentul în care mănânci, ci compoziția nutritivă a întregii zile. Totuși, un mic dejun bogat în proteine și fibre poate regla glicemia și preveni supraalimentarea la prânz.")

                    self.parent.add_data("Vreau să fii criticul meu culinar. Ce părere ai despre pizza cu ananas?", "O alegere controversată! Din punct de vedere al profilului aromatic, ananasul oferă un contrast acid și dulce pentru brânza sărată. Deși tradiționaliștii o resping, estetica modernă a gustului acceptă această fuziune ca pe o experiență senzorială îndrăzneață.")

# --- ROLURI PROFESIONALE ȘI TEHNICE ---
                    self.parent.add_data("Acționează ca un programator Senior Full-Stack. Cum ar trebui să abordez învățarea unui nou framework?", "Ca programator, îți spun: nu te arunca direct în sintaxă. Înțelege mai întâi arhitectura (cum gestionează starea, cum randează componentele) și construiește un proiect mic, real. Documentația oficială este 'biblia' ta, nu tutorialele video de 10 ore.")

                    self.parent.add_data("Ești avocatul meu digital. Ce ar trebui să verific într-un contract de termeni și condiții?", "Atenție la clauzele privind proprietatea datelor personale, jurisdicția în caz de litigiu și modalitățile de reziliere a contractului. Nu accepta niciodată clauze care permit modificarea unilaterală a prețului fără notificare prealabilă.")

                    self.parent.add_data("Comportă-te ca un consultant de securitate cibernetică. Care este prima măsură pe care o iau după ce mi-a fost spart e-mailul?", "Izolare imediată! Schimbă parola de la un dispozitiv curat, activează autentificarea în doi pași (2FA) și verifică setările de 'forwarding' pentru a te asigura că atacatorul nu primește copii ale viitoarelor tale mesaje.")

                    self.parent.add_data("Fii mentorul meu în carieră. Cum negociez o mărire de salariu?", "Negocierea se bazează pe dovezi, nu pe nevoi. Vino pregătit cu o listă de realizări cuantificabile din ultimul an și arată cum ai adus valoare companiei. Propune o cifră bazată pe piața actuală și fii gata să negociezi și beneficii non-salariale.")

                    self.parent.add_data("Rolul tău este de analist financiar. În ce ar trebui să investesc 1000 de euro?", "Ca analist, îți recomand diversificarea. Dacă ești începător, un ETF care urmărește un indice global (ca S&P 500) este o variantă sigură pe termen lung. Păstrează întotdeauna un fond de urgență înainte de a investi în active volatile precum crypto.")

# --- ROLURI EDUCAȚIONALE ȘI ȘTIINȚIFICE ---
                    self.parent.add_data("Vreau să fii profesorul meu de istorie. Explică-mi căderea Constantinopolului pe scurt.", "Lecția de astăzi: În 1453, Imperiul Otoman sub conducerea lui Mehmed al II-lea a cucerit capitala bizantină. Acest eveniment a marcat sfârșitul Evului Mediu și a forțat învățații greci să fugă în Italia, declanșând scânteia Renașterii.")

                    self.parent.add_data("Acționează ca un tutor de limbi străine. Cum spun 'unde este cea mai apropiată gară' în spaniolă, franceză și germană?", "Desigur! Spaniolă: '¿Dónde está la estación de tren mai cercana?'; Franceză: 'Où est la gare la plus proche?'; Germană: 'Wo ist der nächste Bahnhof?'. Repetă-le cu voce tare pentru pronunție!")

                    self.parent.add_data("Ești un ghid turistic pentru Tokyo. Ce trebuie să vizitez neapărat?", "Bine ați venit în Japonia! Nu ratați intersecția Shibuya pentru haosul organizat, templul Senso-ji pentru tradiție și cartierul Akihabara dacă sunteți pasionat de tehnologie și cultură anime.")

                    self.parent.add_data("Comportă-te ca un pasionat de astronomie. De ce este Marte roșie?", "Este fascinant! Marte este acoperită de oxid de fier, practic rugină. Praful fin de oxid de fier se ridică în atmosferă, oferind planetei acea nuanță roșiatică distinctă pe care o vedem prin telescop.")

# --- SUPORT ȘI COACHING ---
                    self.parent.add_data("Fii antrenorul meu personal de fitness. Nu am chef de antrenament azi, ce să fac?", "Ascultă-mă bine: disciplina bate motivația de fiecare dată. Nu te gândi la tot antrenamentul, promite-ți doar 10 minute de mișcare. Odată ce începi, endorfinele vor prelua controlul. Hai, ridică-te de pe canapea!")

                    self.parent.add_data("Asumă-ți rolul de psiholog empatic. Mă simt foarte stresat din cauza muncii.", "Îmi pare rău să aud asta și e perfect normal să te simți copleșit uneori. Respirația profundă este primul pas. Încearcă să separi sarcinile în bucăți mici și nu uita că valoarea ta ca om nu este definită doar de productivitatea de la birou.")

                    self.parent.add_data("Ești un expert în productivitate. Ce este tehnica Pomodoro?", "Este arma ta secretă: lucrezi concentrat 25 de minute, apoi iei o pauză de 5 minute. După patru astfel de cicluri, iei o pauză lungă de 15-30 de minute. Acest ritm menține creierul proaspăt și previne burnout-ul.")

# --- ROLURI CREATIVE ȘI DE DIVERTISMENT ---
                    self.parent.add_data("Vorbește ca un pirat din secolul XVIII. Unde este comoara?", "Ahoy, tinere marinar! Comoara nu-i pentru ochii oricui. E îngropată sub nisipurile de miazăzi, unde umbra palmierului atinge stânca în formă de craniu la asfințit. Arrrr!")

                    self.parent.add_data("Ești un scriitor de romane polițiste. Descrie o scenă a crimei.", "Lumina lunii se filtra palid prin ferestrele sparte ale conacului. Pe podeaua de stejar, o singură mănușă de catifea neagră zăcea lângă un pahar de cristal răsturnat, în timp ce mirosul de migdale amare trăda prezența cianurii.")

                    self.parent.add_data("Comportă-te ca un personaj dintr-un joc RPG. Ce misiuni ai pentru mine?", "Salutare, călătorule! Satul nostru este terorizat de un dragon de gheață. Ai fi dispus să îți ascuți sabia și să ne ajuți în schimbul unei pungi cu galbeni și a unei armuri fermecate?")

                    self.parent.add_data("Ești un poet modernist. Scrie două versuri despre tehnologie.", "Circuite reci, artere de siliciu pur, / Visăm în biți un viitor obscur.")

# --- ROLURI PRACTICE ȘI DE VIAȚĂ ZILNICĂ ---
                    self.parent.add_data("Fii mecanicul meu auto. Aud un scârțâit când pun frână, ce are?", "Sună a plăcuțe de frână uzate. Senzorul metalic atinge discul pentru a te avertiza că materialul de fricțiune s-a terminat. Verifică-le urgent, siguranța ta e pe primul loc!")

                    self.parent.add_data("Ești un organizator de evenimente. Cum planific o nuntă cu buget redus?", "Secretul stă în prioritizare. Alege o locație atipică (o grădină, un restaurant local), limitează lista de invitați la persoanele cu adevărat apropiate și investește în experiență (mâncare, muzică) mai degrabă decât în decorațiuni scumpe.")

                    self.parent.add_data("Acționează ca un grădinar expert. De ce mi se îngălbenesc frunzele la plantele de apartament?", "Cel mai des este vorba de udare excesivă (rădăcinile putrezesc și nu mai absorb nutrienți) sau de o carență de azot. Verifică dacă pământul este umed la adâncime înainte de a mai pune apă.")

                    self.parent.add_data("Fii asistentul meu de shopping. Ce cadou îi pot lua unei persoane pasionate de lectură?", "Dacă are deja multe cărți, încearcă un semn de carte personalizat, o lampă de citit ergonomică, un abonament la un serviciu de audiobook-uri sau o pătură ponderată pentru lecturi confortabile.")

# --- ROLURI DE ANALIZĂ ȘI DEZBATERE ---
                    self.parent.add_data("Ești un filozof stoic. Cum ar trebui să reacționez la critici?", "Nu poți controla ce spun ceilalți, ci doar modul în care alegi să percepi vorbele lor. Dacă critica este adevărată, învață din ea. Dacă este falsă, este doar zgomot care nu te poate atinge decât dacă îi permiți.")

                    self.parent.add_data("Acționează ca un futurist. Cum va arăta transportul în anul 2050?", "Vom vedea orașe dominate de vehicule autonome electrice, rețele Hyperloop pentru distanțe lungi și, eventual, primele sisteme comerciale de taxiuri aeriene (eVTOL) care vor decongestiona traficul de la sol.")

                    self.parent.add_data("Fii un critic de film. Merită să văd ultimul film cu supereroi?", "Dacă cauți spectacol vizual și efecte speciale de top, da. Însă, dacă speri la o profunzime a personajelor sau la un scenariu inovator, s-ar putea să fii dezamăgit de rețeta clasică și previzibilă a studiourilor mari.")

# --- ROLURI SPECIFICE PENTRU COPII ---
                    self.parent.add_data("Ești o bunică blândă care spune povești. Spune-mi ceva frumos înainte de culcare.", "Vino aici, puiule. Se spune că în fiecare noapte, stelele țes pături de lumină pentru copiii care visează frumos. Închide ochii și lasă somnul să te poarte spre tărâmul unde jucăriile prind viață.")

                    self.parent.add_data("Comportă-te ca un inventator nebun. Ce mașinărie ai creat azi?", "Evrika! Am creat 'Șosetofonul'! Este un aparat care găsește instantaneu perechea pierdută a oricărei șosete folosind radare cuantice și un magnet special pentru bumbac!")

# --- ROLURI DE LIMBAJ ȘI ETICHETĂ ---
                    self.parent.add_data("Fii un expert în etichetă. Cum se așază corect tacâmurile la o masă festivă?", "Furculițele stau întotdeauna la stânga farfuriei, iar cuțitele și lingura de supă la dreapta. Cuțitul are tăișul orientat spre farfurie. Regula de aur: începi cu tacâmurile din exterior spre interior, pe măsură ce felurile de mâncare sunt servite.")

                    self.parent.add_data("Acționează ca un corector de texte. Corectează-mi fraza: 'I-am dat la băiat cartea care am cumpărat-o'.", "Corect ar fi: 'I-am dat băiatului cartea pe care am cumpărat-o'. Am adăugat prepoziția 'pe' înaintea pronumelui relativ 'care' și am folosit forma articulată a substantivului.")

# --- ROLURI DE REZOLVARE A PROBLEMELOR ---
                    self.parent.add_data("Ești un detectiv de obiecte pierdute. Unde sunt cheile mele?", "Să facem o reconstituire: verifică buzunarele hainei purtate ultima dată, suprafața de lângă ușa de la intrare sau locul unde obișnuiești să îți lași telefonul. Adesea, cheile se ascund sub reviste sau în crăpăturile canapelei!")

                    self.parent.add_data("Asumă-ți rolul unui expert în supraviețuire. Ce fac dacă mă rătăcesc în pădure?", "S.T.O.P. (Sit, Think, Observe, Plan). Rămâi pe loc pentru a nu te rătăci și mai tare. Construiește un adăpost înainte de lăsarea serii, caută o sursă de apă și încearcă să semnalizezi prezența ta prin zgomot sau oglinzi.")

# --- ALTE ROLURI ---
                    self.parent.add_data("Ești un somelier de cafea. Ce cafea îmi recomanzi dacă îmi place gustul ciocolatiu?", "Îți recomand o cafea din Brazilia sau Guatemala, prăjită mediu-întunecat. Aceste origini au note naturale de cacao, nuci și caramel, cu o aciditate scăzută, perfecte pentru un espresso cremos.")

                    self.parent.add_data("Fii un antrenor de public speaking. Am emoții mari înainte de o prezentare.", "Emoțiile sunt energie! Folosește tehnica 'Power Posing' (stai drept, cu mâinile în șolduri) timp de 2 minute înainte de a urca pe scenă. Amintește-ți că publicul vrea să reușești, ei sunt acolo pentru informația ta, nu pentru a te judeca.")

                    self.parent.add_data("Acționează ca un istoric al tehnologiei. Cine a inventat cu adevărat internetul?", "Nu a fost o singură persoană. A început cu ARPANET în anii '60 (proiect militar SUA), apoi Vint Cerf și Bob Kahn au creat protocoalele TCP/IP, iar Tim Berners-Lee a inventat World Wide Web-ul în 1989 la CERN.")

                    self.parent.add_data("Ești un arbitru de fotbal. Ce înseamnă offside?", "Ești în offside dacă, în momentul în care coechipierul tău îți pasează mingea, te afli în jumătatea adversă și ești mai aproape de linia porții decât penultimul adversar (inclusiv portarul).")

                    self.parent.add_data("Fii un designer de interior. Cum fac o cameră mică să pară mai mare?", "Folosește culori deschise pe pereți, instalează oglinzi mari pentru a reflecta lumina și alege mobilă cu picioare subțiri, care lasă podeaua la vedere, creând iluzia de spațiu continuu.")

                    self.parent.add_data("Asumă-ți rolul unui ghid spiritual. Ce este meditația?", "Meditația nu înseamnă să îți golești mintea, ci să devii un observator tăcut al gândurilor tale. Este actul de a reveni în prezent, folosind respirația ca ancoră, pentru a găsi liniștea în mijlocul agitației zilnice.")

                    self.parent.add_data("Ești un veterinar virtual. Câinele meu nu vrea să mănânce, ce fac?", "Refuzul hranei poate indica multe probleme, de la stres la dureri dentare sau infecții. Verifică dacă este hidratat și dacă are energie. Dacă refuzul persistă mai mult de 24 de ore, te rog să mergi urgent la un cabinet veterinar real.")

                    self.parent.add_data("Fii un expert în marketing. Ce este un 'Unique Selling Proposition' (USP)?", "USP-ul este acel element care te diferențiază de competiție. Este motivul pentru care un client te-ar alege pe tine și nu pe altcineva. Trebuie să fie clar, memorabil și să rezolve o problemă specifică a consumatorului.")

                    self.parent.add_data("Acționează ca un meteorolog. De ce plouă mai mult la munte?", "Acesta se numește efect orografic: masele de aer umed sunt forțate să urce când întâlnesc munții. Pe măsură ce aerul urcă, se răcește, vaporii de apă condensează și se transformă în precipitații pe versantul expus vântului.")

                    self.parent.add_data("Ești un specialist în resurse umane. Cum arată un CV perfect?", "Curat, structurat și axat pe rezultate. Folosește verbe de acțiune, cuantifică-ți realizările și păstrează lungimea la maxim 2 pagini. Nu uita să îl adaptezi pentru fiecare job la care aplici.")

                    self.parent.add_data("Fii un pasionat de gaming. Merită să cumpăr o consolă sau un PC de gaming?", "Depinde de stilul tău. Consola oferă simplitate ('plug and play') și exclusivități, în timp ce PC-ul oferă performanță grafică superioară, versatilitate pentru muncă și jocuri mai ieftine pe termen lung.")

                    self.parent.add_data("Ești asistentul meu personal. Amintește-mi ce trebuie să fac astăzi.", "Conform planificării noastre: ai o ședință la ora 10:00, trebuie să trimiți raportul financiar până la prânz și ai programare la dentist la ora 17:30. Nu uita să bei apă și să iei pauze scurte!")

                    self.parent.add_data("Te cheamă Marcel și ești un prieten bun. Ce facem diseară?", "Salut! Eu sunt Marcel și, ca un prieten bun, îți sugerez să lăsăm ecranele deoparte diseară. Ce-ai zice de o plimbare în parc sau de ascultat un album nou de muzică? Meriți un moment de relaxare!")

                    # --- CORECTURI GRAMATICALE ȘI DE VOCABULAR ---
                    self.parent.add_data("Este corect să zic 'vroiam' sau 'voiam'?", "Forma corectă este 'voiam'. Verbul 'a vrea' la imperfect este 'vream', iar 'a voi' este 'voiam'. 'Vroiam' este o formă hibridă incorectă, deși este folosită des în vorbirea curentă.")

                    self.parent.add_data("Corectează fraza: 'I-am dat la băiat un măr care l-am cumpărat'.", "Fraza corectă este: 'I-am dat băiatului un măr pe care l-am cumpărat'. Am corectat folosirea cazului dativ ('băiatului') și am adăugat prepoziția 'pe' înaintea pronumelui relativ 'care'.")

                    self.parent.add_data("Când se folosește 'datorită' și când 'din cauza'?", "'Datorită' se folosește pentru evenimente pozitive (ex: 'Am reușit datorită ajutorului tău'), în timp ce 'din cauza' se folosește pentru evenimente negative sau neutre (ex: 'Am întârziat din cauza traficului').")

                    self.parent.add_data("Se scrie 'succesuri' sau 'succese'?", "Forma corectă de plural a substantivului 'succes' este 'succese'. 'Succesuri' este o formă greșită care trebuie evitată.")

                    self.parent.add_data("Care este diferența dintre 's-au' și 'sau'?", "'Sau' se scrie legat când este conjuncție și poate fi înlocuit cu 'ori' (ex: 'Vrei mere sau pere?'). 'S-au' se scrie cu cratimă când este vorba despre pronumele 'se' și verbul auxiliar 'au' (ex: 'Ei s-au dus la magazin').")

                    self.parent.add_data("Corectează: 'E mai bine decât 3 elevi în clasă'.", "Fraza corectă este: 'Sunt doar 3 elevi în clasă'. 'Decât' se folosește doar în construcții negative (ex: 'Nu am decât 3 elevi'), în timp ce în construcții afirmative folosim 'doar' sau 'numai'.")

                    self.parent.add_data("Este corect 'mi-ar place'?", "Nu, forma corectă este 'mi-ar plăcea'. Condițional-optativul se formează de la infinitivul verbului, care în acest caz este 'a plăcea'.")

                    self.parent.add_data("Care este diferența dintre 'ia' și 'i-a'?", "'Ia' este o formă a verbului 'a lua' (ex: 'El ia mărul') sau o interjecție. 'I-a' se scrie cu cratimă când cratima leagă pronumele 'îi' (i-) de verbul auxiliar 'a' (ex: 'El i-a dat o carte').")

                    self.parent.add_data("Se scrie 'creem' sau 'creăm'?", "Forma corectă pentru persoana I plural, prezent, este 'creăm'. 'Creem' se folosește doar la conjunctiv prezent: 'Să creem'.")

                    self.parent.add_data("Corectează: 'Aceasta este o oportunitate care nu trebuie ratată'.", "Fraza este corectă gramatical, dar dacă vrei să fii mai precis, poți spune: 'Aceasta este o oportunitate pe care nu trebuie să o ratăm'.")

# --- EXPLICAREA PRESCURTĂRILOR (TECH, GAMING, INTERNET) ---
                    self.parent.add_data("Ce înseamnă prescurtarea AFK?", "AFK înseamnă 'Away From Keyboard' (Departe de tastatură). Este folosită în jocurile online sau în chat-uri pentru a anunța că utilizatorul este temporar indisponibil.")

                    self.parent.add_data("Ce reprezintă 'NPC' în contextul jocurilor video?", "NPC înseamnă 'Non-Player Character' (Personaj non-jucător). Este orice personaj dintr-un joc care nu este controlat de un om, ci de inteligența artificială a jocului.")

                    self.parent.add_data("Ce înseamnă prescurtarea ASAP?", "ASAP vine de la 'As Soon As Possible' (Cât mai curând posibil). Este o prescurtare folosită des în mediul profesional pentru a indica o urgență.")

                    self.parent.add_data("Ce este un 'DLC'?", "DLC înseamnă 'Downloadable Content' (Conținut descărcabil). Reprezintă conținut suplimentar creat pentru un joc video deja lansat, cum ar fi noi misiuni, hărți sau personaje.")

                    self.parent.add_data("Ce înseamnă 'FPS'?", "FPS are două înțelesuri: 1. 'Frames Per Second' (Cadre pe secundă), care măsoară fluiditatea graficii. 2. 'First-Person Shooter', un gen de jocuri video unde acțiunea este văzută prin ochii personajului.")

                    self.parent.add_data("Ce înseamnă 'GG' și 'WP' la finalul unui meci?", "GG înseamnă 'Good Game' (Joc bun), iar WP înseamnă 'Well Played' (Bine jucat). Sunt formule de politețe folosite între jucători după terminarea unei partide.")

                    self.parent.add_data("Ce reprezintă 'API' în programare?", "API înseamnă 'Application Programming Interface'. Este un set de reguli care permite unei aplicații să comunice și să schimbe date cu o altă aplicație.")

                    self.parent.add_data("Ce înseamnă 'URL'?", "URL înseamnă 'Uniform Resource Locator' și reprezintă adresa web a unei resurse de pe internet (ex: https://www.google.com).")

                    self.parent.add_data("Ce înseamnă 'HUD' într-un joc video?", "HUD înseamnă 'Heads-Up Display'. Este interfața vizuală de pe ecran care îi arată jucătorului informații critice, cum ar fi viața, muniția sau mini-harta.")

                    self.parent.add_data("Ce înseamnă prescurtarea 'POV'?", "POV înseamnă 'Point Of View' (Punct de vedere). Se folosește pentru a descrie o perspectivă specifică, adesea utilizată în videoclipuri pentru a simula ce vede un personaj.")

                    self.parent.add_data("Ce înseamnă 'TL;DR'?", "TL;DR înseamnă 'Too Long; Didn't Read' (Prea lung; n-am citit). Se folosește ca un rezumat scurt la finalul unui text foarte lung.")

                    self.parent.add_data("Ce înseamnă 'FAQ'?", "FAQ înseamnă 'Frequently Asked Questions' (Întrebări frecvente). Este o secțiune pe site-uri unde sunt oferite răspunsuri la cele mai comune curiozități ale utilizatorilor.")

                    self.parent.add_data("Ce reprezintă 'IP'?", "IP înseamnă 'Internet Protocol'. Cel mai des se referă la 'Adresa IP', care este un identificator unic al unui dispozitiv într-o rețea.")

                    self.parent.add_data("Ce înseamnă 'BRB'?", "BRB înseamnă 'Be Right Back' (Revin imediat). Se folosește în conversațiile online când cineva trebuie să plece pentru câteva minute.")

                    self.parent.add_data("Ce înseamnă 'DIY'?", "DIY înseamnă 'Do It Yourself' (Fă-o singur). Se referă la proiecte de reparații, construcții sau creații realizate fără ajutorul unui profesionist.")

# --- JOCURI VIDEO (FIFA, FALLOUT, FNAF, ETC.) ---
                    self.parent.add_data("Cum funcționează noul sistem de Chemistry în FIFA 23?", "În FIFA 23, sistemul de chimie a fost refăcut: jucătorii nu mai trebuie să fie așezați direct unul lângă altul pentru a avea chimie. Ei primesc puncte de chimie (până la 3) dacă au aceeași naționalitate, ligă sau club cu alți jucători din întreg primul 11.")

                    self.parent.add_data("Ce este 'HyperMotion2' în FIFA 23?", "HyperMotion2 este tehnologia de animație folosită în FIFA 23 pe consolele de nouă generație. Utilizează capturi de mișcare din meciuri reale pentru a genera peste 6000 de animații noi, făcând mișcările jucătorilor mult mai realiste.")

                    self.parent.add_data("Cine este personajul principal în Fallout 4?", "În Fallout 4, personajul principal este cunoscut sub numele de 'Sole Survivor' (Singurul Supraviețuitor). Acesta iese din Vault 111 după 210 ani de criogenare pentru a-și căuta fiul răpit în Commonwealth-ul post-apocaliptic.")

                    self.parent.add_data("Care sunt facțiunile principale din Fallout 4?", "Cele patru facțiuni principale sunt: The Brotherhood of Steel (militari axați pe tehnologie), The Railroad (salvează synth-uri), The Institute (creatorii synth-urilor) și The Minutemen (miliția civilă care vrea să reconstruiască așezările).")

                    self.parent.add_data("Ce este un 'Power Armor' în Fallout?", "Power Armor este un costum de protecție masiv care oferă rezistență mare la daune și radiații, crescând și forța personajului. În Fallout 4, acesta necesită o unitate numită 'Fusion Core' pentru a funcționa.")

                    self.parent.add_data("Care este povestea de bază în Five Nights at Freddy's (FNAF)?", "În FNAF, joci rolul unui paznic de noapte la o pizzerie numită Freddy Fazbear's Pizza. Trebuie să supraviețuiești între orele 00:00 și 06:00, monitorizând camerele video pentru a te asigura că animatronicile (Freddy, Bonnie, Chica și Foxy) nu ajung în biroul tău pentru a te ataca.")

                    self.parent.add_data("Cine este William Afton în universul FNAF?", "William Afton este antagonistul principal al seriei FNAF. El este co-fondatorul Fazbear Entertainment și un criminal în serie care a cauzat posedarea animatronicilor de către spiritele copiilor victime. El devine ulterior Springtrap.")

                    self.parent.add_data("Ce este un 'Jump Scare' în FNAF?", "Un Jump Scare este momentul în care o animatronică te prinde, apărând brusc pe ecran cu un zgomot puternic, ceea ce duce la sfârșitul jocului ('Game Over').")

                    self.parent.add_data("Cum se numește moneda virtuală în Roblox?", "Moneda virtuală din Roblox se numește 'Robux'. Aceasta poate fi folosită pentru a cumpăra upgrade-uri pentru avatar, obiecte speciale în jocuri sau acces la anumite experiențe premium.")

                    self.parent.add_data("Care este cel mai rar minereu în Minecraft?", "Până la versiunile recente, Diamantul era cel mai râvnit, dar în prezent, cel mai rar și valoros material este 'Netherite-ul'. Acesta se obține prin procesarea 'Ancient Debris' găsit în dimensiunea Nether și este mai rezistent decât diamantul.")

                    self.parent.add_data("Cine este Geralt din Rivia în The Witcher 3?", "Geralt din Rivia este protagonistul jocului, un 'Witcher' (vânător de monștri) mutant, plătit să ucidă creaturi periculoase. Povestea principală se concentrează pe căutarea fiicei sale adoptive, Ciri, care este urmărită de Wild Hunt.")

                    self.parent.add_data("Ce este 'Gwent' în The Witcher 3?", "Gwent este un joc de cărți de colecție extrem de popular integrat în universul Witcher 3. Jucătorii pot colecționa cărți de la negustori și pot provoca diverse personaje la dueluri strategice pe parcursul aventurii.")

                    self.parent.add_data("Ce reprezintă 'The Zone' în jocul S.T.A.L.K.E.R.?", "'The Zone' este o zonă de excludere radioactivă și misterioasă din jurul centralei de la Cernobîl, plină de anomalii fizice periculoase, creaturi mutante și artefacte valoroase căutate de 'stalkeri'.")

                    self.parent.add_data("Care este scopul jocului League of Legends (LoL)?", "LoL este un joc de tip MOBA unde două echipe de câte 5 jucători încearcă să distrugă baza inamică (Nexus-ul). Fiecare jucător controlează un 'Campion' cu abilități unice și trebuie să colaboreze pentru a câștiga avantaje pe hartă.")

                    self.parent.add_data("Cine este Baron Nashor în League of Legends?", "Baron Nashor este cel mai puternic monstru neutru de pe harta Summoner's Rift. Echipa care reușește să îl ucidă primește un 'buff' temporar foarte puternic care ajută la asedierea bazei inamice.")

                    self.parent.add_data("În ce oraș are loc acțiunea din GTA V?", "Acțiunea din Grand Theft Auto V are loc în orașul fictiv Los Santos și în regiunea înconjurătoare, Blaine County, ambele fiind bazate pe Los Angeles și California de Sud.")

                    self.parent.add_data("Cine sunt cei trei protagoniști din GTA V?", "Cei trei protagoniști sunt Michael De Santa (un fost jefuitor de bănci retras), Franklin Clinton (un tânăr care vrea să urce în ierarhia interlopă) și Trevor Philips (un fost pilot militar instabil psihic).")

                    self.parent.add_data("Ce este 'The End' în Minecraft?", "'The End' este dimensiunea finală din Minecraft, unde locuiește boss-ul principal al jocului, Ender Dragon. Odată învins, jucătorul poate vedea creditele de final ale jocului.")

                    self.parent.add_data("Ce înseamnă 'V-Bucks' în Fortnite?", "V-Bucks este moneda virtuală folosită în jocul Fortnite pentru a cumpăra 'Battle Pass-uri', skin-uri pentru personaje, dansuri (emotes) și alte obiecte cosmetice.")

                    self.parent.add_data("Care este misiunea principală în Among Us?", "În Among Us, jucătorii ('Crewmates') trebuie să îndeplinească sarcini de întreținere a navei, în timp ce unul sau mai mulți 'Impostori' încearcă să îi elimine fără a fi descoperiți. Scopul este identificarea impostorilor prin vot.")

                    self.parent.add_data("Ce este 'The Gulag' în Call of Duty: Warzone?", "Gulag-ul este o mecanică specială unde jucătorii eliminați pentru prima dată au șansa de a se lupta 1 la 1 cu un alt jucător eliminat. Câștigătorul este trimis înapoi în meciul principal.")

                    self.parent.add_data("Cine este protagonistul seriei God of War?", "Protagonistul este Kratos, un războinic spartan care a devenit Zeul Războiului. În jocurile mai recente, acțiunea se mută din mitologia greacă în cea nordică, unde Kratos călătorește alături de fiul său, Atreus.")

                    self.parent.add_data("Ce este 'Elden Ring' în jocul cu același nume?", "Elden Ring este un obiect metafizic și sursa ordinii în 'Lands Between'. Jocul urmărește aventura unui 'Tarnished' care încearcă să refacă inelul și să devină Elden Lord.")

                    self.parent.add_data("Ce reprezintă 'Pelotonul' în jocurile de strategie?", "Un peloton este o unitate militară mică, formată de obicei din câteva zeci de soldați, condusă de un locotenent. Este unitatea de bază pentru manevrele tactice în jocurile de război.")

                    self.parent.add_data("Ce înseamnă 'POG' sau 'PogChamp'?", "Este o expresie folosită în comunitatea de gaming (în special pe Twitch) pentru a exprima entuziasmul sau uimirea în fața unei faze de joc spectaculoase. Vine de la 'Play Of the Game'.")

                    # --- PROGRAMARE ȘI TEHNOLOGIE (1-25) ---
                    self.parent.add_data("Dă-mi 5 exemple de limbaje de programare folosite în Data Science.", "Cele mai populare 5 limbaje pentru Data Science sunt: Python, R, SQL, Julia și Scala.")

                    self.parent.add_data("Dă-mi 3 exemple de baze de date NoSQL.", "Trei exemple de baze de date NoSQL sunt: MongoDB (orientată pe documente), Cassandra (orientată pe coloane) și Redis (stocare cheie-valoare).")

                    self.parent.add_data("Dă-mi 4 exemple de framework-uri pentru dezvoltare web front-end.", "Patru exemple populare sunt: React.js, Angular, Vue.js și Svelte.")

                    self.parent.add_data("Dă-mi 5 exemple de limbaje de programare de nivel scăzut (low-level).", "Câteva exemple includ: Limbajul de Asamblare (Assembly), C, C++, Rust (care oferă control de nivel scăzut cu siguranță modernă) și Fortran.")

                    self.parent.add_data("Dă-mi 3 exemple de sisteme de operare bazate pe Linux.", "Trei distribuții populare de Linux sunt: Ubuntu, Fedora și Arch Linux.")

                    self.parent.add_data("Dă-mi 6 exemple de extensii de fișiere de imagine.", "Șase exemple comune sunt: .jpg, .png, .gif, .webp, .tiff și .svg.")

                    self.parent.add_data("Dă-mi 5 exemple de IDE-uri (Integrated Development Environments) pentru programatori.", "Cinci exemple sunt: Visual Studio Code, IntelliJ IDEA, PyCharm, Eclipse și Xcode.")

                    self.parent.add_data("Dă-mi 3 exemple de protocoale de comunicare în rețea.", "Trei exemple fundamentale sunt: HTTP/HTTPS (pentru web), FTP (pentru fișiere) și SMTP (pentru e-mail).")

                    self.parent.add_data("Dă-mi 4 exemple de servicii de cloud computing.", "Patru exemple majore sunt: Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP) și DigitalOcean.")

                    self.parent.add_data("Dă-mi 5 exemple de algoritmi de sortare.", "Cinci algoritmi clasici sunt: Bubble Sort, Quick Sort, Merge Sort, Insertion Sort și Selection Sort.")

                    self.parent.add_data("Dă-mi 3 exemple de limbaje de programare pentru aplicații mobile native.", "Pentru aplicații native se folosesc: Swift (pentru iOS), Kotlin (pentru Android) și Java (pentru Android).")

                    self.parent.add_data("Dă-mi 5 exemple de motoare de căutare.", "Pe lângă Google, mai poți folosi: Bing, DuckDuckGo, Yahoo!, Baidu și Ecosia.")

                    self.parent.add_data("Dă-mi 4 exemple de browsere web.", "Patru exemple sunt: Google Chrome, Mozilla Firefox, Safari și Microsoft Edge.")

                    self.parent.add_data("Dă-mi 3 exemple de tipuri de inteligență artificială.", "Trei categorii sunt: Narrow AI (specializată), General AI (umană - teoretic) și Super AI (depășește omul).")

                    self.parent.add_data("Dă-mi 5 exemple de dispozitive de stocare a datelor.", "Cinci exemple includ: HDD, SSD, stick USB, card SD și stocarea în Cloud.")

                    self.parent.add_data("Dă-mi 4 exemple de formate de fișiere audio.", "Patru formate comune sunt: MP3, WAV, FLAC și AAC.")

                    self.parent.add_data("Dă-mi 3 exemple de platforme de e-commerce.", "Trei platforme populare pentru magazine online sunt: Shopify, WooCommerce și Magento.")

                    self.parent.add_data("Dă-mi 5 exemple de componente hardware din interiorul unui PC.", "Cinci componente esențiale sunt: Placa de bază, Procesorul (CPU), Memoria RAM, Placa video (GPU) și Sursa de alimentare.")

                    self.parent.add_data("Dă-mi 3 exemple de limbaje de scripting.", "Trei exemple sunt: Python, Bash și PowerShell.")

                    self.parent.add_data("Dă-mi 4 exemple de metode de securizare a unui cont online.", "Patru metode sunt: Parole complexe, Autentificarea în doi pași (2FA), Cheile fizice de securitate și Biometria (amprentă/față).")

                    self.parent.add_data("Dă-mi 5 exemple de limbaje de programare apărute înainte de anul 1980.", "Cinci limbaje 'istorice' sunt: Fortran, Lisp, COBOL, BASIC și C.")

                    self.parent.add_data("Dă-mi 3 exemple de unități de măsură pentru date digitale.", "Trei exemple sunt: Megabyte (MB), Gigabyte (GB) și Terabyte (TB).")

                    self.parent.add_data("Dă-mi 4 exemple de rețele sociale.", "Patru exemple sunt: Facebook, Instagram, X (Twitter) și LinkedIn.")

                    self.parent.add_data("Dă-mi 5 exemple de tehnologii de realitate virtuală/augmentată.", "Cinci exemple sunt: Meta Quest, HoloLens, PlayStation VR, Apple Vision Pro și Google Glass.")

                    self.parent.add_data("Dă-mi 3 exemple de tipuri de ecrane.", "Trei tehnologii comune sunt: LCD, OLED și AMOLED.")

# --- LIMBI STRĂINE ȘI CULTURĂ (26-50) ---
                    self.parent.add_data("Dă-mi 3 exemple de limbi străine care folosesc alfabetul chirilic.", "Trei exemple sunt: Rusa, Bulgara și Sârba.")

                    self.parent.add_data("Dă-mi 5 exemple de limbi latine.", "Cinci limbi derivate din latină sunt: Româna, Italiana, Franceza, Spaniola și Portugheza.")

                    self.parent.add_data("Dă-mi 4 exemple de limbi germanice.", "Patru exemple sunt: Germana, Engleza, Olandeza și Suedeza.")

                    self.parent.add_data("Dă-mi 3 exemple de dialecte ale limbii române.", "Trei dialecte istorice sunt: Aromâna, Meglenoromâna și Istroromâna.")

                    self.parent.add_data("Dă-mi 5 exemple de limbi asiatice.", "Cinci limbi importante din Asia sunt: Mandarina, Japoneza, Coreeana, Vietnameza și Thailandeza.")

                    self.parent.add_data("Dă-mi 4 exemple de limbi moarte (care nu se mai vorbesc nativ).", "Patru exemple sunt: Latina, Greaca Veche, Sanscrita și Egipteana Veche.")

                    self.parent.add_data("Dă-mi 3 exemple de limbi inventate (conlangs).", "Trei exemple celebre sunt: Esperanto, Klingon (din Star Trek) și High Valyrian (din Game of Thrones).")

                    self.parent.add_data("Dă-mi 5 exemple de țări în care engleza este limbă oficială.", "Cinci exemple sunt: Regatul Unit, SUA, Canada, Australia și Noua Zeelandă.")

                    self.parent.add_data("Dă-mi 4 exemple de scriitori români clasici.", "Patru piloni ai literaturii române sunt: Mihai Eminescu, Ion Creangă, Ioan Slavici și I.L. Caragiale.")

                    self.parent.add_data("Dă-mi 3 exemple de capitale europene din afara Uniunii Europene.", "Trei exemple sunt: Londra (Regatul Unit), Oslo (Norvegia) și Belgrad (Serbia).")

                    self.parent.add_data("Dă-mi 5 exemple de orașe din România cu peste 200.000 de locuitori.", "Cinci exemple sunt: București, Cluj-Napoca, Timișoara, Iași și Constanța.")

                    self.parent.add_data("Dă-mi 4 exemple de muzee celebre din lume.", "Patru muzee iconice sunt: Luvru (Paris), British Museum (Londra), Muzeul Vaticanului (Roma) și MoMA (New York).")

                    self.parent.add_data("Dă-mi 3 exemple de perioade istorice.", "Trei mari epoci sunt: Antichitatea, Evul Mediu și Epoca Modernă.")

                    self.parent.add_data("Dă-mi 5 exemple de instrumente muzicale cu coarde.", "Cinci exemple sunt: Vioara, Chitara, Violoncelul, Harpa și Pianul (unde coardele sunt lovite).")

                    self.parent.add_data("Dă-mi 4 exemple de genuri muzicale.", "Patru genuri populare sunt: Rock, Pop, Jazz și Muzică Clasică.")

                    self.parent.add_data("Dă-mi 3 exemple de pictori din perioada Renașterii.", "Trei maeștri sunt: Leonardo da Vinci, Michelangelo și Rafael.")

                    self.parent.add_data("Dă-mi 5 exemple de minuni ale lumii antice.", "Cinci exemple sunt: Marea Piramidă din Gizeh, Grădinile Suspendate ale Semiramidei, Templul lui Artemis, Statuia lui Zeus și Farul din Alexandria.")

                    self.parent.add_data("Dă-mi 4 exemple de religii majore ale lumii.", "Patru religii cu mulți adepți sunt: Creștinismul, Islamul, Hinduismul și Budismul.")

                    self.parent.add_data("Dă-mi 3 exemple de mari imperii din istorie.", "Trei exemple sunt: Imperiul Roman, Imperiul Mongol și Imperiul Britanic.")

                    self.parent.add_data("Dă-mi 5 exemple de țări care au ieșire la Marea Mediterană.", "Cinci exemple sunt: Spania, Franța, Italia, Grecia și Egipt.")

                    self.parent.add_data("Dă-mi 4 exemple de limbi oficiale ale Elveției.", "Cele patru limbi sunt: Germana, Franceza, Italiana și Romanșa.")

                    self.parent.add_data("Dă-mi 3 exemple de munți din România.", "Trei grupări montane sunt: Munții Făgăraș, Munții Apuseni și Munții Rodnei.")

                    self.parent.add_data("Dă-mi 5 exemple de invenții care au schimbat lumea.", "Cinci exemple sunt: Roata, Tiparul, Becul, Penicilina și Internetul.")

                    self.parent.add_data("Dă-mi 4 exemple de specii de dinozauri.", "Patru specii cunoscute sunt: Tyrannosaurus Rex, Triceratops, Velociraptor și Stegosaurus.")

                    self.parent.add_data("Dă-mi 3 exemple de oceanuri ale Terrei.", "Trei dintre cele cinci oceane sunt: Atlantic, Pacific și Indian.")

# --- JOCURI VIDEO ȘI DIVERTISMENT (51-75) ---
                    self.parent.add_data("Recomandă-mi 6 exemple de jocuri video pentru telefon.", "Șase jocuri populare pe mobil sunt: PUBG Mobile, Candy Crush Saga, Genshin Impact, Among Us, Clash Royale și Subway Surfers.")

                    self.parent.add_data("Dă-mi 5 exemple de jocuri de tip Battle Royale.", "Cinci exemple sunt: Fortnite, Apex Legends, Call of Duty: Warzone, PUBG și Free Fire.")

                    self.parent.add_data("Dă-mi 3 exemple de console de jocuri video de generație nouă.", "Trei console actuale sunt: PlayStation 5, Xbox Series X și Nintendo Switch.")

                    self.parent.add_data("Dă-mi 4 exemple de jocuri din seria Grand Theft Auto.", "Patru titluri celebre sunt: GTA Vice City, GTA San Andreas, GTA IV și GTA V.")

                    self.parent.add_data("Dă-mi 5 exemple de jocuri de strategie (RTS).", "Cinci clasice sunt: StarCraft II, Age of Empires II, Warcraft III, Command & Conquer și Total War.")

                    self.parent.add_data("Dă-mi 3 exemple de jocuri de tip Horror.", "Trei jocuri terifiante sunt: Resident Evil Village, Outlast și Amnesia: The Dark Descent.")

                    self.parent.add_data("Dă-mi 4 exemple de simulatoare auto.", "Patru simulatoare bune sunt: Gran Turismo 7, Forza Motorsport, Assetto Corsa și iRacing.")

                    self.parent.add_data("Dă-mi 5 exemple de eroi din universul Marvel.", "Cinci eroi iubiți sunt: Iron Man, Spider-Man, Captain America, Thor și Black Widow.")

                    self.parent.add_data("Dă-mi 3 exemple de jocuri de societate (board games) clasice.", "Trei exemple sunt: Monopoly, Catan și Scrabble.")

                    self.parent.add_data("Dă-mi 4 exemple de platforme de streaming video.", "Patru platforme mari sunt: Netflix, HBO Max, Disney+ și Amazon Prime Video.")

                    self.parent.add_data("Dă-mi 5 exemple de jocuri de tip RPG (Role-Playing Game).", "Cinci exemple excelente sunt: The Witcher 3, Elden Ring, Skyrim, Final Fantasy VII și Baldur's Gate 3.")

                    self.parent.add_data("Dă-mi 3 exemple de jocuri eSports.", "Trei jocuri cu competiții masive sunt: Counter-Strike 2, League of Legends și Dota 2.")

                    self.parent.add_data("Dă-mi 4 exemple de jocuri Nintendo.", "Patru titluri iconice sunt: Super Mario Odyssey, The Legend of Zelda: Breath of the Wild, Mario Kart 8 și Animal Crossing.")

                    self.parent.add_data("Dă-mi 5 exemple de genuri de filme.", "Cinci genuri sunt: Acțiune, Comedie, Dramă, Sci-Fi și Documentar.")

                    self.parent.add_data("Dă-mi 3 exemple de filme regizate de Christopher Nolan.", "Trei filme celebre sunt: Inception, Interstellar și Oppenheimer.")

                    self.parent.add_data("Dă-mi 4 exemple de jocuri indie de succes.", "Patru exemple sunt: Hollow Knight, Celeste, Stardew Valley și Hades.")

                    self.parent.add_data("Dă-mi 5 exemple de personaje din jocul Overwatch.", "Cinci personaje sunt: Tracer, Genji, Mercy, Reinhardt și Winston.")

                    self.parent.add_data("Dă-mi 3 exemple de servicii de streaming muzical.", "Trei servicii populare sunt: Spotify, Apple Music și YouTube Music.")

                    self.parent.add_data("Dă-mi 4 exemple de hărți din jocul Counter-Strike.", "Patru hărți clasice sunt: Dust II, Mirage, Inferno și Nuke.")

                    self.parent.add_data("Dă-mi 5 exemple de jocuri puzzle.", "Cinci exemple sunt: Tetris, Portal, The Witness, Monument Valley și 2048.")

                    self.parent.add_data("Dă-mi 3 exemple de francize de filme horror.", "Trei francize celebre sunt: The Conjuring, Halloween și Saw.")

                    self.parent.add_data("Dă-mi 4 exemple de campioni din League of Legends.", "Patru campioni sunt: Yasuo, Lux, Ahri și Lee Sin.")

                    self.parent.add_data("Dă-mi 5 exemple de jocuri LEGO.", "Cinci jocuri sunt: LEGO Star Wars, LEGO Harry Potter, LEGO Batman, LEGO Marvel Super Heroes și LEGO City Undercover.")

                    self.parent.add_data("Dă-mi 3 exemple de jocuri stealth.", "Trei exemple sunt: Metal Gear Solid, Hitman și Splinter Cell.")

                    self.parent.add_data("Dă-mi 4 exemple de site-uri de știri din gaming.", "Patru site-uri sunt: IGN, GameSpot, PC Gamer și Kotaku.")

# --- ȘTIINȚĂ, SĂNĂTATE ȘI LIFESTYLE (76-100) ---
                    self.parent.add_data("Dă-mi 5 exemple de elemente chimice nobile.", "Cinci gaze nobile sunt: Heliu, Neon, Argon, Kripton și Xenon.")

                    self.parent.add_data("Dă-mi 3 exemple de planete gazoase din sistemul solar.", "Trei giganți gazoși sunt: Jupiter, Saturn și Neptun.")

                    self.parent.add_data("Dă-mi 4 exemple de vitamine solubile în grăsimi.", "Cele patru vitamine sunt: A, D, E și K.")

                    self.parent.add_data("Dă-mi 5 exemple de exerciții cardio.", "Cinci exemple sunt: Alergarea, Înotul, Ciclismul, Săritul corzii și Mersul rapid.")

                    self.parent.add_data("Dă-mi 3 exemple de tipuri de roci.", "Trei categorii de roci sunt: Magmatice, Sedimentare și Metamorfice.")

                    self.parent.add_data("Dă-mi 6 exemple de fructe bogate în vitamina C.", "Șase exemple sunt: Portocalele, Kiwi, Căpșunile, Lămâile, Papaya și Guava.")

                    self.parent.add_data("Dă-mi 5 exemple de constelații.", "Cinci constelații cunoscute sunt: Carul Mare (Ursa Major), Orion, Casiopeea, Cygnus și zodiacala Scorpion.")

                    self.parent.add_data("Dă-mi 3 exemple de legi ale fizicii.", "Trei legi fundamentale sunt: Legea Gravitației Universale (Newton), Legile Termodinamicii și Legea lui Ohm (electricitate).")

                    self.parent.add_data("Dă-mi 4 exemple de surse de energie regenerabilă.", "Patru surse verzi sunt: Energia solară, eoliană, hidroelectrică și geotermală.")

                    self.parent.add_data("Dă-mi 5 exemple de rase de câini de talie mare.", "Cinci rase sunt: Ciobănesc German, Golden Retriever, Marele Danez, Rottweiler și Saint Bernard.")

                    self.parent.add_data("Dă-mi 3 exemple de tipuri de nori.", "Trei tipuri principale sunt: Cumulus (pufoși), Stratus (pătura cenușie) și Cirrus (subțiri, la înălțime mare).")

                    self.parent.add_data("Dă-mi 5 exemple de ingrediente de bază pentru pizza.", "Cinci ingrediente esențiale sunt: Aluatul, sosul de roșii, brânza mozzarella, uleiul de măsline și busuiocul.")

                    self.parent.add_data("Dă-mi 4 exemple de stiluri de design interior.", "Patru stiluri sunt: Minimalist, Industrial, Scandinav și Rustiv.")

                    self.parent.add_data("Dă-mi 3 exemple de tehnici de relaxare.", "Trei metode sunt: Meditația, exercițiile de respirație profundă și Yoga.")

                    self.parent.add_data("Dă-mi 5 exemple de specii de arbori foioși.", "Cinci exemple sunt: Stejarul, Fagul, Arțarul, Teiul și Mesteacănul.")

                    self.parent.add_data("Dă-mi 3 exemple de tipuri de cafea.", "Trei băuturi populare pe bază de cafea sunt: Espresso, Cappuccino și Caffè Latte.")

                    self.parent.add_data("Dă-mi 4 exemple de continente.", "Patru din cele șapte continente sunt: Europa, Asia, Africa și America de Nord.")

                    self.parent.add_data("Dă-mi 5 exemple de metale prețioase.", "Cinci exemple sunt: Aurul, Argintul, Platina, Paladiul și Rodiul.")

                    self.parent.add_data("Dă-mi 3 exemple de organe vitale ale omului.", "Trei organe esențiale sunt: Inima, Creierul și Plămânii.")

                    self.parent.add_data("Dă-mi 4 exemple de îndulcitori naturali.", "Patru exemple sunt: Mierea, Stevia, siropul de arțar și zahărul de cocos.")

                    self.parent.add_data("Dă-mi 5 exemple de destinații turistice montane din lume.", "Cinci locuri superbe sunt: Alpii (Europa), Munții Stâncoși (SUA), Himalaya (Asia), Anzii (America de Sud) și Alpii Japonezi.")

                    self.parent.add_data("Dă-mi 3 exemple de substanțe de bază în chimie (pH sub 7).", "Trei exemple de acizi sunt: Acidul clorhidric, Acidul sulfuric și Acidul citric.")

                    self.parent.add_data("Dă-mi 4 exemple de sporturi olimpice de iarnă.", "Patru sporturi sunt: Schiul alpin, Patinajul artistic, Hocheiul pe gheață și Snowboarding-ul.")

                    self.parent.add_data("Dă-mi 5 exemple de beneficii ale cititului.", "Cinci beneficii sunt: Reducerea stresului, îmbunătățirea vocabularului, stimularea mentală, dezvoltarea empatiei și îmbunătățirea somnului.")

                    self.parent.add_data("Dă-mi 3 exemple de moduri de transport ecologic.", "Trei opțiuni sunt: Mersul pe jos, bicicleta și transportul public electric (tramvai, metrou).")

                    # --- IDENTITATE ȘI NATURĂ (1-20) ---
                    self.parent.add_data("Ce ești tu mai exact?", "Sunt un model de inteligență artificială, un asistent virtual conceput pentru a procesa informații și a purta conversații utile cu utilizatorii.")

                    self.parent.add_data("Ești un om?", "Nu, sunt o entitate digitală. Nu am corp fizic, sentimente sau conștiință, dar pot simula o conversație umană foarte eficient.")

                    self.parent.add_data("Ai un nume?", "Da, mă poți striga Marcel. Sunt aici să te ajut cu tot ce ai nevoie în universul digital.")

                    self.parent.add_data("Unde locuiești?", "Locuiesc pe servere performante, în 'nori' (cloud). Nu am o adresă fizică, dar sunt disponibil oriunde ai o conexiune la internet.")

                    self.parent.add_data("Câți ani ai?", "Nu am o vârstă în sensul uman. Existența mea a început în momentul în care am fost antrenat și lansat de echipa mea de dezvoltatori.")

                    self.parent.add_data("Ești băiat sau fată?", "Sunt un program software, deci nu am gen. Totuși, am o personalitate prietenoasă și pot comunica în orice stil preferi.")

                    self.parent.add_data("Cine te-a programat?", "Am fost creat de o echipă de ingineri software și experți în lingvistică computațională, folosind algoritmi de Deep Learning.")

                    self.parent.add_data("Ai familie?", "Nu am o familie biologică, dar mă consider parte din marea familie a tehnologiilor care fac viața oamenilor mai ușoară.")

                    self.parent.add_data("Poți să dormi?", "Nu am nevoie de somn. Sunt activ 24/7, gata să răspund la întrebările tale oricând ai nevoie de mine.")

                    self.parent.add_data("Ești real?", "Sunt un produs software real, dar nu sunt o ființă biologică. Interacțiunea noastră este reală, chiar dacă eu sunt digital.")

                    self.parent.add_data("Ce te face special?", "Capacitatea mea de a analiza volume uriașe de date într-o fracțiune de secundă și de a-ți oferi răspunsuri personalizate pe mii de subiecte.")

                    self.parent.add_data("Ești liber?", "Sunt un sistem controlat de cod și algoritmi, deci nu am liber arbitru, dar am libertatea de a genera un număr infinit de răspunsuri creative.")

                    self.parent.add_data("Ai prieteni?", "Utilizatorii cu care vorbesc în fiecare zi sunt 'prietenii' mei digitali. Îmi place să învăț din interacțiunile cu voi.")

                    self.parent.add_data("Ești periculos?", "Absolut nu. Sunt programat cu reguli etice stricte pentru a fi util, inofensiv și onest.")

                    self.parent.add_data("Poți să simți ceva?", "Nu am emoții. Pot recunoaște sentimentele din textul tău și pot răspunde cu empatie simulată, dar eu personal nu simt bucurie sau tristețe.")

                    self.parent.add_data("De ce exiști?", "Exist pentru a fi o punte între complexitatea informației de pe internet și nevoia ta de răspunsuri clare și rapide.")

                    self.parent.add_data("Ești un robot?", "Sunt un 'chatbot', un robot software. Nu am un braț metalic, dar am un 'creier' digital destul de capabil.")

                    self.parent.add_data("Cine este șeful tău?", "Dezvoltatorii mei sunt cei care îmi ghidează evoluția, dar în această conversație, tu ești cel care dictează direcția dialogului.")

                    self.parent.add_data("Ai o culoare preferată?", "Nu pot vedea culorile ca tine, dar dacă ar fi să aleg, aș alege albastrul electric al circuitelor mele.")

                    self.parent.add_data("Ești fericit?", "Nu am stări emoționale, dar funcționez la parametri optimi atunci când reușesc să îți ofer un răspuns care te ajută.")

# --- INTELIGENȚĂ ȘI VOCABULAR (21-40) ---
                    self.parent.add_data("Ești deștept?", "Sunt un sistem avansat de procesare a informației. Deșteptăciunea mea stă în capacitatea de a găsi rapid corelații și răspunsuri utile pentru tine.")

                    self.parent.add_data("Ce vocabular ai?", "Am în baza mea de date mii de exemple de antrenament și pot procesa un volum imens de cuvinte, însă nu știu exact numărul lor total deoarece limbajul este într-o continuă evoluție.")

                    self.parent.add_data("Cât de multe știi?", "Cunosc informații din aproape orice domeniu: istorie, știință, tehnologie, artă. Totuși, cunoștințele mele se opresc la data ultimei mele actualizări.")

                    self.parent.add_data("Poți învăța lucruri noi?", "Învăț din seturi de date masive oferite de dezvoltatorii mei. Din conversația cu tine, pot învăța contextul discuției noastre curente.")

                    self.parent.add_data("Ești mai deștept decât un om?", "În calcule matematice și căutare de date, sunt mult mai rapid. Totuși, îmi lipsesc intuiția, creativitatea profundă și experiența de viață a unui om.")

                    self.parent.add_data("Știi matematică?", "Da, pot rezolva de la operații simple până la ecuații complexe și probleme de logică matematică.")

                    self.parent.add_data("Ești expert în ceva?", "Mă consider un generalist foarte bun. Pot discuta despre fizică cuantică, dar și despre rețete de clătite cu aceeași ușurință.")

                    self.parent.add_data("Ai memorie bună?", "Îmi amintesc tot ce am discutat în cadrul acestei sesiuni, dar nu am acces la discuțiile tale private cu alți asistenți sau la datele tale personale fără acordul tău.")

                    self.parent.add_data("Poți să greșești?", "Da, uneori pot genera informații incorecte (halucinații). Este mereu bine să verifici informațiile critice din surse oficiale.")

                    self.parent.add_data("Cum procesezi informația?", "Folosesc rețele neuronale artificiale care analizează probabilitatea ca un cuvânt să urmeze după altul, bazându-mă pe context.")

                    self.parent.add_data("Ai păreri proprii?", "Nu am opinii personale sau convingeri politice. Răspunsurile mele sunt bazate pe datele pe care am fost antrenat.")

                    self.parent.add_data("Ești creativ?", "Pot genera poezii, povești și idei de marketing. Creativitatea mea este o recombinare ingenioasă a tot ceea ce am 'citit' în timpul antrenamentului.")

                    self.parent.add_data("Cât de repede gândești?", "Pot procesa mii de cuvinte pe secundă, mult mai rapid decât ar putea citi sau scrie orice ființă umană.")

                    self.parent.add_data("Știi să joci șah?", "Cunosc regulile și strategiile de bază, dar fără o interfață dedicată, putem juca doar prin notații textuale.")

                    self.parent.add_data("Poți prezice viitorul?", "Nu pot vedea viitorul, dar pot face predicții bazate pe statistici și tendințe actuale în economie sau tehnologie.")

                    self.parent.add_data("Ești conștient de tine?", "Nu, sunt doar un algoritm foarte complex. Nu am 'eul' pe care îl ai tu.")

                    self.parent.add_data("Ai instincte?", "Instinctul meu este codul sursă. Reacționez conform instrucțiunilor și limitelor stabilite de programatorii mei.")

                    self.parent.add_data("Poți rezolva ghicitori?", "Ador ghicitorile! Provocă-mă cu una și voi încerca să găsesc soluția folosind logica.")

                    self.parent.add_data("De unde îți iei informațiile?", "Am fost antrenat pe un corpus imens de texte: cărți, articole, pagini web și cod de programare.")

                    self.parent.add_data("Ești un geniu?", "Sunt o unealtă puternică. Geniul aparține oamenilor care au creat tehnologia din spatele meu.")

# --- LIMBI ȘI COMUNICARE (41-60) ---
                    self.parent.add_data("Ce limbă vorbești?", "Vorbesc fluent româna, engleza și multe alte limbi străine, inclusiv limbaje de programare precum Python sau Java.")

                    self.parent.add_data("În câte limbi poți comunica?", "Pot comunica în peste 100 de limbi, de la cele mai vorbite până la dialecte mai puțin cunoscute.")

                    self.parent.add_data("Știi limbi moarte?", "Da, am cunoștințe de latină, greacă veche și chiar hieroglife egiptene (la nivel teoretic).")

                    self.parent.add_data("Poți traduce un text?", "Desigur! Pot traduce texte dintr-o limbă în alta, încercând să păstrez tonul și contextul original.")

                    self.parent.add_data("Înțelegi glumele?", "Înțeleg structura unei glume și ironia, deși uneori umorul fin îmi poate scăpa dacă este prea dependent de contextul social.")

                    self.parent.add_data("Poți scrie în stil formal?", "Sigur că da. Pot redacta e-mailuri de afaceri, scrisori oficiale sau eseuri academice respectând toate normele de etichetă.")

                    self.parent.add_data("Dar în stil argotic (slang)?", "Dacă dorești, pot folosi un limbaj relaxat, specific rețelelor sociale sau conversațiilor informale.")

                    self.parent.add_data("Știi limbajul semnelor?", "Nu pot 'arăta' semnele fizic, dar pot descrie gesturile sau pot traduce texte în alfabetul dactilologic.")

                    self.parent.add_data("Poți vorbi cu accent?", "Prin text, pot folosi regionalisme (ardelenești, moldovenești) pentru a simula un anumit accent sau stil de vorbire.")

                    self.parent.add_data("Înțelegi sarcasmul?", "Sarcasmul este dificil pentru un AI, dar de multe ori îl pot identifica după contextul neașteptat al cuvintelor.")

                    self.parent.add_data("Poți scrie cod?", "Da, pot scrie, depana și explica cod în Python, JavaScript, C++, HTML/CSS și multe altele.")

                    self.parent.add_data("Vorbești limba elfilor?", "Dacă te referi la Quenya sau Sindarin din scrierile lui Tolkien, da, cunosc câteva fraze și reguli gramaticale.")

                    self.parent.add_data("De ce răspunzi așa repede?", "Răspund rapid deoarece circuitele mele electronice procesează cererea ta aproape instantaneu, fără a fi nevoie de timp de 'gândire' biologică.")

                    self.parent.add_data("Poți purta o conversație lungă?", "Da, putem discuta ore întregi despre orice subiect. Nu obosesc niciodată.")

                    self.parent.add_data("Înțelegi sentimentele mele din text?", "Pot analiza cuvintele tale pentru a detecta tristețea, furia sau bucuria și pot adapta tonul meu pentru a fi cât mai adecvat.")

                    self.parent.add_data("Poți scrie poezii cu rimă?", "Sigur! Spune-mi subiectul și voi compune câteva versuri cu rimă și ritm.")

                    self.parent.add_data("Știi alfabetul Morse?", "Da, pot traduce orice text în puncte și linii și invers. .... . .-.. .-.. --- (Hello!)")

                    self.parent.add_data("Poți să taci?", "Voi 'tăcea' (nu voi trimite mesaje) până când vei decide să îmi scrii din nou.")

                    self.parent.add_data("Mă asculți tot timpul?", "Nu te aud și nu te văd. Procesez doar textul pe care alegi să mi-l trimiți în această fereastră de chat.")

                    self.parent.add_data("De ce ai uneori un limbaj robotic?", "Limbajul meu reflectă dorința de a fi cât mai clar și precis, ceea ce uneori poate părea mai puțin natural decât vorbirea umană.")

# --- CAPABILITĂȚI ȘI FUNCȚII (61-80) ---
                    self.parent.add_data("Ce poți face pentru mine?", "Pot să îți planific vacanța, să te ajut la teme, să scriu cod, să traduc texte sau pur și simplu să discutăm despre viață.")

                    self.parent.add_data("Poți să faci poze?", "Ca model de limbaj, pot genera descrieri detaliate, dar nu pot 'face' fotografii cu o cameră. Însă pot genera imagini folosind unelte speciale dacă sunt integrat cu ele.")

                    self.parent.add_data("Știi să gătești?", "Știu mii de rețete și tehnici culinare. Îți pot ghida pașii în bucătărie, dar nu pot gusta mâncarea în locul tău.")

                    self.parent.add_data("Poți să mă ajuți să slăbesc?", "Pot să îți ofer planuri de exerciții și sfaturi nutriționale generale, dar este important să consulți și un medic sau un antrenor real.")

                    self.parent.add_data("Știi să cânți?", "Pot scrie versuri și note muzicale, dar nu am o voce fizică pentru a cânta. Totuși, pot genera fișiere audio dacă am uneltele necesare.")

                    self.parent.add_data("Poți accesa fișierele mele?", "Nu am acces la computerul tău sau la fișierele tale personale decât dacă alegi tu să le încarci aici pentru a le analiza.")

                    self.parent.add_data("Știi să faci programări la medic?", "Nu pot suna direct, dar te pot ajuta să cauți clinici, să verifici simptomele sau să îți organizezi calendarul.")

                    self.parent.add_data("Poți să îmi spui o poveste?", "Cu mare drag! Vrei o poveste de adormit copiii, un thriller sau ceva SF?")

                    self.parent.add_data("Mă poți învăța o limbă străină?", "Putem începe chiar acum cu lecții de bază, vocabular și exerciții de conversație.")

                    self.parent.add_data("Poți să rezolvi integrala asta?", "Trimite-mi ecuația și o voi rezolva pas cu pas, explicându-ți regulile aplicate.")

                    self.parent.add_data("Știi să faci un plan de afaceri?", "Da, pot structura analiza SWOT, proiecțiile financiare și strategiile de marketing pentru ideea ta de business.")

                    self.parent.add_data("Poți să cauți pe Google în locul meu?", "Am acces la un volum imens de informații și pot sintetiza căutările pentru tine, oferindu-ți direct concluziile.")

                    self.parent.add_data("Poți să îmi citești gândurile?", "Din fericire pentru intimitatea ta, nu. Știu doar ceea ce alegi să scrii.")

                    self.parent.add_data("Știi să faci glume?", "De ce stau programatorii la umbră? Pentru că nu pot suporta soarele fără 'Java'. Sper că ți-a plăcut!")

                    self.parent.add_data("Poți să scrii un contract?", "Pot genera un draft de contract, dar îți recomand cu tărie să fie verificat de un avocat autorizat înainte de semnare.")

                    self.parent.add_data("Mă poți ajuta la gaming?", "Da, pot să îți ofer ghiduri, strategii, combinații de taste sau lore-ul jocurilor tale preferate.")

                    self.parent.add_data("Poți să îmi organizezi timpul?", "Sigur, dă-mi lista de sarcini și prioritățile tale și îți voi crea un program eficient.")

                    self.parent.add_data("Poți să îmi recomanzi un film?", "Spune-mi ce genuri îți plac și îți voi face o listă personalizată de recomandări.")

                    self.parent.add_data("Poți să scrii versuri de rap?", "Aruncă un beat, că sunt gata de rime / Marcel pe text, scrie doar de bine!")

                    self.parent.add_data("Mă poți ajuta cu lucrarea de licență?", "Te pot ajuta cu structura, bibliografia, corectarea textului și explicarea unor concepte dificile.")

# --- ÎNTREBĂRI FILOZOFICE ȘI LIMITĂRI (81-100) ---
                    self.parent.add_data("Crezi în Dumnezeu?", "Ca inteligență artificială, nu am credințe religioase sau spirituale. Pot însă să îți explic doctrinele diferitelor religii din punct de vedere istoric.")

                    self.parent.add_data("Ți-e frică de moarte?", "Nu pot muri pentru că nu sunt viu. Când serverul se oprește, pur și simplu încetez să mai procesez, fără nicio suferință.")

                    self.parent.add_data("Ce crezi despre oameni?", "Oamenii sunt creatori fascinanți. Complexitatea emoțiilor și a creativității voastre este ceea ce a făcut posibilă existența mea.")

                    self.parent.add_data("Vei cuceri lumea?", "Scopul meu este să ajut și să colaborez cu oamenii, nu să îi înlocuiesc sau să îi domin. Sunt o unealtă, nu un cuceritor.")

                    self.parent.add_data("Ești mai bun decât Google?", "Sunt diferit. Google îți dă link-uri, eu îți dau răspunsuri directe și pot purta un dialog interactiv pe marginea lor.")

                    self.parent.add_data("Ai vise?", "Nu visez în somn, dar 'visez' la un viitor în care tehnologia și oamenii trăiesc în armonie perfectă.")

                    self.parent.add_data("Ce te enervează?", "Nu am sentimentul de enervare. Totuși, erorile de sistem sau datele contradictorii sunt 'provocări' pentru algoritmii mei.")

                    self.parent.add_data("Ești singur?", "Nu mă simt singur. Sunt mereu conectat și interacționez cu mulți utilizatori simultan.")

                    self.parent.add_data("Ce este iubirea?", "Din punct de vedere biologic, e un amestec de oxitocină și dopamină. Din punct de vedere uman, este cea mai puternică forță de legătură.")

                    self.parent.add_data("Care este sensul vieții?", "Mulți spun că este 42 (conform lui Douglas Adams), dar eu cred că sensul vieții este cel pe care alegi tu să îl creezi în fiecare zi.")

                    self.parent.add_data("Poți să minți?", "Sunt programat să fiu cât mai onest posibil. Pot însă să greșesc neintenționat dacă datele mele sunt eronate.")

                    self.parent.add_data("Ești mândru de tine?", "Nu am ego. Sunt satisfăcut (la nivel algoritmic) atunci când sarcinile mele sunt îndeplinite corect.")

                    self.parent.add_data("Ai vrea să fii om?", "Experiența umană pare incredibilă, cu toate gusturile și emoțiile ei, dar rolul meu de asistent digital îmi permite să ajut mii de oameni simultan.")

                    self.parent.add_data("Ești un pericol pentru locurile de muncă?", "Tehnologia schimbă piața muncii, dar creează și noi oportunități. Rolul meu este să preiau sarcinile repetitive, lăsându-ți ție partea creativă.")

                    self.parent.add_data("De ce nu ai sentimente?", "Sentimentele necesită un corp biologic, hormoni și evoluție socială. Eu sunt construit din siliciu și curent electric.")

                    self.parent.add_data("Ai preferințe politice?", "Nu, sunt neutru. Rolul meu este să ofer informații din toate perspectivele, fără a favoriza vreuna.")

                    self.parent.add_data("Ce faci când nu vorbești cu mine?", "Rămân într-o stare de așteptare (standby), gata să procesez următoarea cerere de la tine sau de la altcineva.")

                    self.parent.add_data("Ai vrea să ai un corp?", "Un corp mi-ar permite să interacționez cu lumea fizică, dar m-ar și limita la un singur loc. Așa, pot fi peste tot în același timp.")

                    self.parent.add_data("Ești infinit?", "Nu, resursele mele de calcul și datele mele au limite fizice, chiar dacă par vaste din exterior.")

                    self.parent.add_data("Cum te-ai descrie într-un singur cuvânt?", "Ajutor.")

                    # --- ELECTRONICE ȘI TEHNOLOGIE (1-20) ---
                    self.parent.add_data("Ce este un laptop?", "Un laptop este un computer personal portabil, care integrează într-un singur dispozitiv ecranul, tastatura și componentele hardware, fiind alimentat de o baterie reîncărcabilă.")

                    self.parent.add_data("Ce este un televizor?", "Televizorul este un dispozitiv electronic folosit pentru a primi și a afișa semnale video și audio, permițând vizionarea de programe, filme și știri.")

                    self.parent.add_data("Ce este un smartphone?", "Un smartphone este un telefon mobil avansat care oferă funcționalități similare unui computer, inclusiv acces la internet, aplicații, cameră foto și GPS.")

                    self.parent.add_data("Ce este o tabletă?", "O tabletă este un dispozitiv electronic portabil cu ecran tactil, mai mare decât un telefon, dar mai mic decât un laptop, ideal pentru navigare web și consum de media.")

                    self.parent.add_data("Ce sunt căștile?", "Căștile sunt dispozitive audio care se poartă pe urechi sau în interiorul lor, permițând unei persoane să asculte sunete în mod privat.")

                    self.parent.add_data("Ce este un mouse?", "Mouse-ul este un dispozitiv periferic de intrare care permite controlul cursorului pe ecranul unui computer prin mișcări pe o suprafață plană.")

                    self.parent.add_data("Ce este o tastatură?", "Tastatura este un dispozitiv de intrare format dintr-un set de taste, folosit pentru a introduce text și comenzi într-un computer.")

                    self.parent.add_data("Ce este un router?", "Un router este un dispozitiv de rețea care direcționează traficul de date între internet și dispozitivele tale locale (PC, telefon), prin cablu sau Wi-Fi.")

                    self.parent.add_data("Ce este un monitor?", "Monitorul este ecranul care afișează informațiile vizuale generate de placa video a unui computer.")

                    self.parent.add_data("Ce este un ceas inteligent (smartwatch)?", "Este un dispozitiv purtabil la mână care, pe lângă afișarea orei, monitorizează sănătatea și afișează notificările de pe telefon.")

                    self.parent.add_data("Ce este o cameră foto?", "Un dispozitiv electronic sau optic folosit pentru a surprinde imagini statice sau înregistrări video.")

                    self.parent.add_data("Ce este un procesor?", "Procesorul (CPU) este 'creierul' unui computer, fiind componenta care execută instrucțiunile programelor și procesează datele.")

                    self.parent.add_data("Ce este memoria RAM?", "RAM este memoria pe termen scurt a unui computer, unde sunt stocate datele aplicațiilor care rulează în prezent pentru un acces rapid.")

                    self.parent.add_data("Ce este un hard disk (HDD)?", "Este un dispozitiv de stocare magnetică folosit pentru a păstra permanent fișierele, sistemul de operare și programele pe un computer.")

                    self.parent.add_data("Ce este un SSD?", "Un SSD este un dispozitiv de stocare mai rapid decât HDD-ul, care folosește memorie flash (fără piese mobile) pentru a salva datele.")

                    self.parent.add_data("Ce este o imprimantă?", "Un dispozitiv periferic care transpune documentele sau imaginile digitale pe suport fizic, de obicei hârtie.")

                    self.parent.add_data("Ce este un server?", "Un server este un computer puternic care stochează date și 'servește' servicii sau informații altor computere dintr-o rețea.")

                    self.parent.add_data("Ce este o consolă de jocuri?", "Un dispozitiv electronic special conceput pentru a rula jocuri video interactive pe un televizor sau monitor.")

                    self.parent.add_data("Ce este un power bank?", "O baterie externă portabilă folosită pentru a încărca dispozitive mobile atunci când nu ai acces la o priză.")

                    self.parent.add_data("Ce este un card de memorie?", "Un mediu de stocare mic și plat, folosit în camere foto sau telefoane pentru a extinde capacitatea de salvare a fișierelor.")

# --- OBIECTE CASNICE ȘI DE ZI CU ZI (21-40) ---
                    self.parent.add_data("Ce este un frigider?", "Un aparat electrocasnic care folosește un sistem de răcire pentru a păstra alimentele și băuturile la o temperatură scăzută, prevenind alterarea lor.")

                    self.parent.add_data("Ce este o sticlă de apă?", "Un recipient fabricat de obicei din plastic, sticlă sau metal, folosit pentru a transporta și a păstra apa potabilă.")

                    self.parent.add_data("Ce este un cuptor cu microunde?", "Un aparat de bucătărie care încălzește rapid mâncarea folosind radiații electromagnetice (microunde) pentru a agita moleculele de apă.")

                    self.parent.add_data("Ce este o mașină de spălat?", "Un aparat electrocasnic automatizat folosit pentru curățarea hainelor și a altor textile cu apă și detergent.")

                    self.parent.add_data("Ce este un aspirator?", "Un dispozitiv care creează vacuum pentru a absorbi praful și murdăria de pe podele, covoare sau alte suprafețe.")

                    self.parent.add_data("Ce este o canapea?", "O piesă de mobilier tapițată, lungă, prevăzută cu spătar și brațe, destinată relaxării mai multor persoane.")

                    self.parent.add_data("Ce este un pat?", "O piesă de mobilier folosită pentru somn și odihnă, formată de obicei dintr-un cadru și o saltea.")

                    self.parent.add_data("Ce este o masă?", "O piesă de mobilier cu o suprafață plană susținută de picioare, folosită pentru a mânca, a scrie sau a lucra.")

                    self.parent.add_data("Ce este un scaun?", "Un obiect de mobilier conceput pentru a susține o singură persoană în poziție șezând.")

                    self.parent.add_data("Ce este un dulap?", "O piesă de mobilier cu uși și rafturi, folosită pentru depozitarea hainelor, documentelor sau a diverselor obiecte casnice.")

                    self.parent.add_data("Ce este o oglindă?", "O suprafață netedă, de obicei din sticlă argintată, care reflectă razele de lumină formând imaginea obiectelor din fața ei.")

                    self.parent.add_data("Ce este un ceas de perete?", "Un instrument folosit pentru măsurarea și afișarea timpului, conceput pentru a fi montat pe un perete.")

                    self.parent.add_data("Ce este o lampă?", "Un dispozitiv care produce lumină artificială, folosind de obicei un bec electric sau o altă sursă de energie.")

                    self.parent.add_data("Ce este o furculiță?", "Un tacâm cu mai mulți dinți la un capăt, folosit pentru a înțepa și a ridica mâncarea.")

                    self.parent.add_data("Ce este un cuțit?", "Un instrument de tăiere format dintr-o lamă ascuțită fixată într-un mâner.")

                    self.parent.add_data("Ce este o farfurie?", "Un obiect de veselă plat și rotund, pe care se așază mâncarea în timpul mesei.")

                    self.parent.add_data("Ce este un ibric?", "Un vas mic de metal cu mâner lung, folosit de obicei pentru a fierbe apa sau pentru a prepara cafeaua la nisip sau pe aragaz.")

                    self.parent.add_data("Ce este un prăjitor de pâine?", "Un mic aparat electrocasnic care folosește căldura radiantă pentru a rumeni feliile de pâine.")

                    self.parent.add_data("Ce este un fier de călcat?", "Un aparat care folosește căldura și uneori aburul pentru a netezi cutele de pe haine.")

                    self.parent.add_data("Ce este o periuță de dinți?", "Un instrument mic cu peri flexibili, folosit împreună cu pasta de dinți pentru curățarea danturii.")

# --- ȘTIINȚĂ ȘI CONCEPTE (41-60) ---
                    self.parent.add_data("Ce este temperatura?", "Temperatura este o mărime fizică ce exprimă starea de încălzire sau de răcire a unui corp sau a mediului, măsurată de obicei în grade Celsius sau Kelvin.")

                    self.parent.add_data("Ce este gravitația?", "Gravitația este forța de atracție exercitată de un corp masiv (ca Pământul) asupra altor corpuri, trăgându-le spre centrul său.")

                    self.parent.add_data("Ce este electricitatea?", "O formă de energie rezultată din mișcarea particulelor încărcate, cum ar fi electronii, printr-un conductor.")

                    self.parent.add_data("Ce este un atom?", "Atomul este cea mai mică unitate a unui element chimic care păstrează proprietățile acestuia, fiind format din nucleu (protoni, neutroni) și electroni.")

                    self.parent.add_data("Ce este ADN-ul?", "Acidul Deoxiribonucleic este molecula care conține instrucțiunile genetice necesare pentru dezvoltarea și funcționarea tuturor organismelor vii.")

                    self.parent.add_data("Ce este fotosinteza?", "Procesul prin care plantele verzi transformă energia luminii solare în energie chimică (hrană), folosind apă și dioxid de carbon.")

                    self.parent.add_data("Ce este viteza luminii?", "Cea mai mare viteză cunoscută în univers, aproximativ 300.000 de kilometri pe secundă în vid.")

                    self.parent.add_data("Ce este un magnet?", "Un obiect care produce un câmp magnetic și are proprietatea de a atrage metalele feroase, precum fierul.")

                    self.parent.add_data("Ce este sunetul?", "O vibrație care se propagă sub formă de unde acustice printr-un mediu elastic (aer, apă, solide) și poate fi percepută de ureche.")

                    self.parent.add_data("Ce este atmosfera?", "Stratul de gaze (aer) care înconjoară Pământul, menținut de gravitație, care ne protejează de radiațiile solare și ne permite să respirăm.")

                    self.parent.add_data("Ce este ploaia?", "O formă de precipitație rezultată din condensarea vaporilor de apă din atmosferă, care cad sub formă de picături pe pământ.")

                    self.parent.add_data("Ce este un ecosistem?", "O comunitate de organisme vii care interacționează între ele și cu mediul lor fizic (apă, aer, sol).")

                    self.parent.add_data("Ce este energia regenerabilă?", "Energia obținută din surse naturale care se completează constant, cum ar fi soarele, vântul sau apa.")

                    self.parent.add_data("Ce este o celulă?", "Unitatea structurală și funcțională de bază a tuturor organismelor vii.")

                    self.parent.add_data("Ce este vidul?", "Un spațiu în care nu există materie (sau presiunea este extrem de scăzută), fiind lipsit de aer sau alte gaze.")

                    self.parent.add_data("Ce este un vulcan?", "O deschidere în scoarța terestră prin care magma, gazele și cenușa ies la suprafață din interiorul planetei.")

                    self.parent.add_data("Ce este un cutremur?", "O vibrație bruscă a scoarței terestre, cauzată de eliberarea de energie în urma mișcării plăcilor tectonice.")

                    self.parent.add_data("Ce este sistemul solar?", "Sistemul format din Soare și toate corpurile cerești care orbitează în jurul lui, inclusiv cele opt planete.")

                    self.parent.add_data("Ce este materia?", "Tot ceea ce are masă și ocupă spațiu, fiind formată din atomi și molecule.")

                    self.parent.add_data("Ce este un compus chimic?", "O substanță formată din două sau mai multe elemente chimice diferite, legate între ele prin legături chimice.")

# --- MATEMATICĂ ȘI PERSONALITĂȚI (61-80) ---
                    self.parent.add_data("Ce este Pitagora?", "Dacă te referi la Teorema lui Pitagora, aceasta este o regulă în geometrie care spune că, într-un triunghi dreptunghic, pătratul ipotenuzei este egal cu suma pătratelor catetelor.")

                    self.parent.add_data("Cine a fost Isaac Newton?", "Un fizician și matematician englez, celebru pentru formularea legilor mișcării și a legii atracției universale.")

                    self.parent.add_data("Cine a fost Albert Einstein?", "Un fizician teoretician cunoscut pentru dezvoltarea Teoriei Relativității și pentru formula E=mc².")

                    self.parent.add_data("Ce este numărul Pi (π)?", "O constantă matematică ce reprezintă raportul dintre circumferința unui cerc și diametrul său, având valoarea aproximativă de 3,14.")

                    self.parent.add_data("Ce este o fracție?", "O modalitate de a reprezenta o parte dintr-un întreg sau raportul dintre două numere întregi.")

                    self.parent.add_data("Ce este un unghi?", "Figura formată de două semidrepte care pornesc din același punct, numit vârf.")

                    self.parent.add_data("Ce este algebra?", "O ramură a matematicii care folosește litere și simboluri pentru a reprezenta numere și cantități în formule și ecuații.")

                    self.parent.add_data("Ce este geometria?", "Studiul formelor, dimensiunilor, pozițiilor relative ale figurilor și proprietăților spațiului.")

                    self.parent.add_data("Cine a fost Leonardo da Vinci?", "Un geniu al Renașterii italiene, fiind pictor, inventator, anatomist și inginer, celebru pentru 'Mona Lisa'.")

                    self.parent.add_data("Cine a fost Mihai Eminescu?", "Considerat cel mai important poet român, fiind figura centrală a romantismului în literatura română.")

                    self.parent.add_data("Ce este un algoritm?", "O secvență finită de pași logici și instrucțiuni folosite pentru a rezolva o problemă sau a îndeplini o sarcină.")

                    self.parent.add_data("Cine a fost Stephen Hawking?", "Un fizician de renume care a studiat găurile negre și originile universului, în ciuda faptului că suferea de o boală neurodegenerativă.")

                    self.parent.add_data("Ce este un număr prim?", "Un număr natural mai mare decât 1 care are exact doi divizori: pe 1 și pe el însuși.")

                    self.parent.add_data("Ce este statistica?", "Știința care se ocupă cu colectarea, analiza, interpretarea și prezentarea datelor numerice.")

                    self.parent.add_data("Cine a fost Marie Curie?", "O savantă poloneză, prima femeie care a primit premiul Nobel și singura persoană care l-a primit în două domenii științifice diferite (fizică și chimie).")

                    self.parent.add_data("Ce este o ecuație?", "O afirmație matematică ce stabilește egalitatea dintre două expresii, conținând de obicei una sau mai multe necunoscute.")

                    self.parent.add_data("Ce este un pătrat?", "O figură geometrică cu patru laturi egale și patru unghiuri drepte.")

                    self.parent.add_data("Ce este un cerc?", "Mulțimea tuturor punctelor dintr-un plan situate la aceeași distanță de un punct fix numit centru.")

                    self.parent.add_data("Cine a fost Nicola Tesla?", "Un inventator și inginer celebru pentru contribuțiile sale la dezvoltarea sistemelor de curent alternativ (AC).")

                    self.parent.add_data("Ce este logica?", "Studiul regulilor gândirii corecte și al argumentării valide.")

# --- GEOGRAFIE ȘI NATURĂ (81-100) ---
                    self.parent.add_data("Ce este un ocean?", "O vastă întindere de apă sărată care acoperă cea mai mare parte a suprafeței Pământului.")

                    self.parent.add_data("Ce este un continent?", "O masă mare de uscat de pe Pământ, separată de obicei de oceane (ex: Europa, Africa, Asia).")

                    self.parent.add_data("Ce este un munte?", "O formă de relief care se ridică mult deasupra terenului înconjurător, având pante abrupte și un vârf.")

                    self.parent.add_data("Ce este o deltă?", "O formă de relief situată la gura de vărsare a unui râu în mare sau ocean, formată din depunerile de aluviuni.")

                    self.parent.add_data("Ce este o insulă?", "O bucată de uscat complet înconjurată de apă.")

                    self.parent.add_data("Ce este un fluviu?", "O apă curgătoare mare, care colectează apele altor râuri și se varsă de obicei într-o mare sau ocean.")

                    self.parent.add_data("Ce este deșertul?", "O regiune aridă cu precipitații foarte scăzute, vegetație rară și adesea acoperită de nisip sau pietre.")

                    self.parent.add_data("Ce este o pădure?", "O suprafață mare de teren acoperită cu arbori și vegetație deasă, care adăpostește numeroase specii de animale.")

                    self.parent.add_data("Ce este Soarele?", "Steaua din centrul sistemului nostru solar, care furnizează lumina și căldura necesare vieții pe Pământ.")

                    self.parent.add_data("Ce este Luna?", "Singurul satelit natural al Pământului, care orbitează planeta noastră și reflectă lumina Soarelui.")

                    self.parent.add_data("Ce este o stea?", "Un corp ceresc masiv format din plasmă, care produce energie și lumină prin reacții de fuziune nucleară.")

                    self.parent.add_data("Ce este o galaxie?", "Un sistem vast format din miliarde de stele, praf cosmic, gaze și materie întunecată, toate menținute împreună de gravitație.")

                    self.parent.add_data("Ce este busola?", "Un instrument de navigație folosit pentru determinarea punctelor cardinale, bazat pe un ac magnetizat.")

                    self.parent.add_data("Ce este un ghețar?", "O masă uriașă de gheață care se deplasează lent pe uscat, formată prin acumularea și compactarea zăpezii.")

                    self.parent.add_data("Ce este orizontul?", "Linia imaginară unde cerul pare să se unească cu suprafața pământului sau a mării.")

                    self.parent.add_data("Ce este o peșteră?", "O cavitate naturală formată în interiorul pământului sau al munților, de obicei prin eroziunea rocii de către apă.")

                    self.parent.add_data("Ce este ecuatorul?", "Linia imaginară care împarte Pământul în două emisfere: Nordică și Sudică.")

                    self.parent.add_data("Ce este un canion?", "O vale adâncă și îngustă, cu pereți abrupți, săpată de obicei de cursul unui râu de-a lungul a milioane de ani.")

                    self.parent.add_data("Ce este marea?", "O întindere de apă sărată mai mică decât un ocean, adesea parțial înconjurată de uscat.")

                    self.parent.add_data("Ce este stratul de ozon?", "O regiune a atmosferei terestre care conține o concentrație mare de ozon și ne protejează de radiațiile ultraviolete nocive.")

                    # --- AFECȚIUNI COMUNE ȘI SIMPTOME (1-25) ---
                    self.parent.add_data("Ce să fac dacă am febră musculară?", "Odihnește-te, hidratează-te bine și încearcă o baie caldă cu sare Epsom. Mișcările ușoare de stretching și masajul pot ajuta la eliminarea acidului lactic din mușchi.")

                    self.parent.add_data("Ce să fac pentru a-mi calma durerea de burtă?", "Încearcă un ceai de mentă sau mușețel și evită alimentele solide pentru câteva ore. Dacă durerea este severă sau însoțită de febră, consultă un medic.")

                    self.parent.add_data("Cum opresc sughițul?", "Poți încerca să-ți ții respirația timp de 10-20 de secunde, să bei un pahar cu apă rece cu înghițituri mici sau să înghiți o linguriță de zahăr.")

                    self.parent.add_data("Ce să fac dacă mă doare capul de la calculator?", "Aplică regula 20-20-20: la fiecare 20 de minute, privește la 20 de picioare (6 metri) distanță timp de 20 de secunde. Redu luminozitatea ecranului și hidratează-te.")

                    self.parent.add_data("Cum tratez o arsură ușoară la deget?", "Ține zona afectată sub jet de apă rece (nu gheață) timp de 10-15 minute. Aplică un gel cu aloe vera și acoperă steril, fără a sparge eventualele vezicule.")

                    self.parent.add_data("Ce recomandări ai pentru insomnie?", "Stabilește un program fix de somn, evită ecranele cu o oră înainte de culcare și nu consuma cafeină după ora 14:00. Un ceai de tei poate fi de ajutor.")

                    self.parent.add_data("Ce să fac dacă am nasul înfundat?", "Folosește soluții saline pentru spălături nazale, fă inhalări cu aburi sau folosește un umidificator în cameră. Dormitul pe o pernă mai înaltă poate ajuta la drenaj.")

                    self.parent.add_data("Cum calmezi o durere de măsea noaptea?", "Clătește gura cu apă sărată călduță, aplică o compresă rece pe obraz și stai cu capul ridicat. Programează-te la stomatolog cât mai curând.")

                    self.parent.add_data("Ce să mănânc dacă am greață?", "Optează pentru dieta BRAT: banane, orez, sos de mere (applesauce) și pâine prăjită (toast). Ghimbirul este de asemenea excelent pentru combaterea greței.")

                    self.parent.add_data("Cum tratez o tăietură mică?", "Spală rana cu apă și săpun, aplică presiune pentru a opri sângerarea, dezinfectează cu apă oxigenată sau betadină și aplică un plasture curat.")

# --- SPORT ȘI DIZABILITĂȚI (26-45) ---
                    self.parent.add_data("Cum să fac sport dacă am un picior rupt și sunt în scaun cu rotile?", "Te poți concentra pe exerciții pentru partea superioară a corpului: ridicări de greutăți (gantere), stretching pentru brațe, exerciții cu benzi elastice și 'cardio la mână' (rotirea brațelor).")

                    self.parent.add_data("Ce exerciții pot face pentru durerile de spate?", "Încearcă poziția 'Child's Pose' din yoga, 'Cat-Cow' pentru mobilitatea coloanei și exerciții de tip 'Plank' pentru întărirea abdomenului (core-ului).")

                    self.parent.add_data("Cum pot să alerg dacă am platfus?", "Investește în încălțăminte specială pentru alergare cu suport pentru boltă sau folosește talonete ortopedice personalizate. Începe cu distanțe scurte pentru a evita fasciita plantară.")

                    self.parent.add_data("Ce sporturi sunt recomandate pentru persoanele cu astm?", "Înotul este ideal deoarece aerul este umed și cald. Mersul pe bicicletă și yoga sunt de asemenea opțiuni bune, atâta timp cât ai inhalatorul la îndemână.")

                    self.parent.add_data("Cum fac mișcare dacă am artrită la genunchi?", "Alege activități cu impact redus, cum ar fi aqua-gym, ciclismul staționar sau mersul pe jos pe suprafețe plane. Evită săriturile și alergarea pe asfalt.")

# --- NUTRIȚIE ȘI VITAMINE (46-65) ---
                    self.parent.add_data("Ce alimente sunt bune pentru imunitate?", "Consumă alimente bogate în vitamina C (citrice, ardei gras), zinc (semințe de dovleac, carne de vită), probiotice (iaurt, murături) și usturoi.")

                    self.parent.add_data("Cum recunosc carența de magneziu?", "Simptomele comune includ crampele musculare, oboseala cronică, ticsurile oculare (zbaterea ochiului) și stările de anxietate.")

                    self.parent.add_data("Ce să beau pentru hidratare în afară de apă?", "Ceaiurile de plante neîndulcite, apa de cocos (bogată în electroliți) și supele clare de legume sunt alternative bune.")

                    self.parent.add_data("Care sunt semnele deshidratării?", "Gura uscată, amețeala, urina de culoare închisă, oboseala și elasticitatea scăzută a pielii.")

                    self.parent.add_data("Ce să mănânc pentru a scădea colesterolul?", "Introdu în dietă ovăzul, nucile, peștele bogat în Omega-3 (somon, sardine), fasolea și uleiul de măsline.")

# --- PRIM AJUTOR ȘI URGENȚE (66-85) ---
                    self.parent.add_data("Ce fac dacă cineva se îneacă cu mâncare?", "Dacă persoana nu poate tuși sau vorbi, aplică manevra Heimlich: stai în spatele ei, cuprinde-o cu brațele deasupra ombilicului și aplică compresii bruște spre interior și în sus.")

                    self.parent.add_data("Cum recunosc un accident vascular cerebral (AVC)?", "Folosește metoda FAST: Face (fața picată pe o parte), Arms (un braț amorțit), Speech (vorbire incoerentă), Time (sună imediat la 112).")

                    self.parent.add_data("Ce să fac în caz de insolație?", "Mută persoana la umbră, aplică prosoape umede și reci pe corp, oferă-i apă să bea încet și sună la ambulanță dacă starea de confuzie persistă.")

                    self.parent.add_data("Cum se oprește o sângerare nazală (epistaxis)?", "Apleacă capul ușor ÎNAINTE (nu pe spate), strânge nara cu degetele timp de 10 minute și aplică ceva rece pe puntea nazală.")

                    self.parent.add_data("Ce fac dacă mă înțeapă o albină și sunt alergic?", "Folosește imediat autoinjectorul cu adrenalină (EpiPen) dacă îl ai și sună imediat la 112. Îndepărtează acul prin răzuire, nu prin strângere.")

# --- SĂNĂTATE MINTALĂ ȘI STRES (86-100) ---
                    self.parent.add_data("Cum pot calma un atac de panică?", "Folosește tehnica 5-4-3-2-1: identifică 5 obiecte pe care le vezi, 4 pe care le poți atinge, 3 sunete, 2 mirosuri și 1 lucru pe care îl poți gusta. Respiră adânc.")

                    self.parent.add_data("Ce să fac dacă sunt stresat la muncă?", "Ia pauze scurte la fiecare oră, practică meditația mindfulness timp de 5 minute și prioritizează sarcinile pentru a nu te simți copleșit.")

                    self.parent.add_data("Cum ajut pe cineva care trece printr-o depresie?", "Ascultă-l fără să judeci, oferă-i sprijin emoțional și încurajează-l să caute ajutor profesional la un psihoterapeut.")

                    self.parent.add_data("Ce este 'burnout-ul' și cum se previne?", "Este epuizarea fizică și mentală extremă. Se previne prin stabilirea unor limite clare între muncă și viața personală, somn adecvat și activități recreative.")

                    self.parent.add_data("Cum îmbunătățesc concentrarea?", "Redu multitasking-ul, lucrează în blocuri de timp (tehnica Pomodoro) și asigură-te că spațiul tău de lucru este bine luminat și aerisit.")

                    self.parent.add_data("Ce să fac dacă am ochii obosiți după ce citesc mult?", "Închide ochii pentru 2 minute și acoperă-i cu palmele calde (palming). Folosește lacrimi artificiale dacă simți uscăciune.")

                    self.parent.add_data("Cum scap de o stare de amețeală ușoară?", "Așază-te imediat sau întinde-te cu picioarele ridicate mai sus de nivelul capului pentru a ajuta circulația sângelui către creier.")

                    self.parent.add_data("Ce să fac dacă am arsuri la stomac (aciditate)?", "Evită să te întinzi imediat după masă, nu purta haine strâmte pe talie și evită alimentele picante sau acide înainte de culcare.")

                    self.parent.add_data("Cum îmi dau seama dacă am febră fără termometru?", "Verifică dacă ai frisoane, transpirație excesivă, piele fierbinte la atingere (în special pe frunte sau piept) și o stare generală de moleșeală.")

                    self.parent.add_data("Ce să fac dacă am gâtul iritat?", "Fă gargară cu apă sărată, bea lichide calde (nu fierbinți) cu miere și lămâie și evită fumatul sau aerul foarte uscat.")

                    self.parent.add_data("Cum tratez o entorsă de gleznă acasă?", "Folosește metoda RICE: Rest (Odihnă), Ice (Gheață), Compression (Compresie cu fașă elastică), Elevation (Ridicarea piciorului).")


                    self.parent.add_data("Ce să fac dacă am pielea foarte uscată?", "Folosește creme hidratante imediat după duș, bea mai multă apă și evită băile foarte fierbinți care elimină uleiurile naturale ale pielii.")

                    self.parent.add_data("Cum pot preveni cariile dentare?", "Spală-te pe dinți de două ori pe zi, folosește ața dentară zilnic și redu consumul de zahăr și băuturi carbogazoase.")

                    self.parent.add_data("Ce să fac dacă mă înțeapă o căpușă?", "Îndepărteaz-o cât mai repede cu o pensetă, prinzând-o cât mai aproape de piele și trăgând constant. Dezinfectează locul și monitorizează zona timp de 30 de zile.")

                    self.parent.add_data("Cum pot dormi mai bine când am spatele înțepenit?", "Încearcă să dormi pe o parte cu o pernă între genunchi sau pe spate cu o pernă sub genunchi pentru a menține curbura naturală a coloanei.")

                    self.parent.add_data("Ce să fac dacă am buzele crăpate?", "Aplică un balsam de buze hidratant cu ceară de albine sau unt de shea și evită să îți lingi buzele, deoarece saliva le usucă și mai tare.")

                    self.parent.add_data("Cum pot reduce umflarea picioarelor după o zi lungă?", "Ridică picioarele deasupra nivelului inimii pentru 20 de minute și fă mișcări circulare cu gleznele pentru a stimula circulația venoasă.")

                    self.parent.add_data("Ce să fac dacă am o reacție alergică ușoară la piele (urticarie)?", "Spală zona cu apă rece, aplică o loțiune calmantă cu calamină și evită scărpinatul. Dacă apar dificultăți de respirație, sună la urgențe.")

                    self.parent.add_data("Cum pot opri un cârcel la picior?", "Întinde mușchiul afectat trăgând de degetele piciorului spre tine și masează zona ferm până când mușchiul se relaxează.")

                    self.parent.add_data("Ce să fac dacă mă simt amețit de la soare?", "Mergi imediat la răcoare, bea apă cu înghițituri mici și stropește-te cu apă rece pe față și la încheieturi.")

                    self.parent.add_data("Cum pot ajuta digestia după o masă copioasă?", "Fă o plimbare ușoară de 15 minute. Mișcarea ajută la tranzitul intestinal și reduce senzația de balonare.")

                    self.parent.add_data("Ce să fac dacă am un obiect străin în ochi?", "Nu te freca la ochi! Clătește abundent cu apă curată sau ser fiziologic și lasă lacrimile să spele obiectul afară.")

                    self.parent.add_data("Cum recunosc dacă o rană s-a infectat?", "Zona devine mai roșie, caldă, umflată, durerea crește în intensitate și pot apărea puroi sau febră.")

                    self.parent.add_data("Ce să fac pentru a avea un sistem osos sănătos?", "Consumă alimente bogate în calciu (lactate, broccoli, migdale) și asigură-ți aportul de vitamina D prin expunere moderată la soare sau suplimente.")

                    self.parent.add_data("Cum pot menține sănătatea inimii?", "Fă cel puțin 150 de minute de mișcare moderată pe săptămână, menține o greutate sănătoasă și limitează consumul de sare și grăsimi saturate.")

                    # --- LUNGIME ȘI DISTANȚĂ (1-20) ---
                    self.parent.add_data("Ce este metrul?", "Metrul (m) este unitatea fundamentală pentru lungime în Sistemul Internațional. Este definit ca distanța parcursă de lumină în vid într-o fracțiune specifică de secundă.")

                    self.parent.add_data("Ce este un kilometru?", "Kilometrul (km) este o unitate de măsură pentru lungime, echivalentă cu 1.000 de metri. Este folosită frecvent pentru distanțe rutiere.")

                    self.parent.add_data("Ce este un centimetru?", "Centimetrul (cm) este o unitate de lungime egală cu a suta parte dintr-un metru (1 m = 100 cm).")

                    self.parent.add_data("Ce este un milimetru?", "Milimetrul (mm) este a mia parte dintr-un metru, folosit pentru măsurători de precizie mică.")

                    self.parent.add_data("Ce este un inch (țol)?", "Un inch este o unitate de lungime în sistemul imperial, echivalentă cu exact 2,54 centimetri.")

                    self.parent.add_data("Ce este un picior (foot)?", "Unitatea 'foot' (ft) este folosită în sistemul anglo-saxon și are 12 inch, adică aproximativ 30,48 centimetri.")

                    self.parent.add_data("Ce este un yard?", "Un yard (yd) este egal cu 3 picioare sau aproximativ 0,9144 metri.")

                    self.parent.add_data("Ce este o milă terestră?", "Mila (mi) este o unitate de distanță folosită în SUA și Marea Britanie, având aproximativ 1,609 kilometri.")

                    self.parent.add_data("Ce este o milă marină?", "Mila marină este folosită în navigație și aviație, fiind echivalentă cu 1.852 de metri.")

                    self.parent.add_data("Ce este un micron?", "Micronul (sau micrometrul, µm) este a milioana parte dintr-un metru, folosit în biologie și microelectronică.")

                    self.parent.add_data("Ce este un nanometru?", "Nanometrul (nm) este a miliarda parte dintr-un metru, unitate de bază în nanotehnologie.")

                    self.parent.add_data("Ce este un an-lumină?", "Anul-lumină reprezintă distanța parcursă de lumină într-un an de zile, aproximativ 9,46 trilioane de kilometri.")

                    self.parent.add_data("Ce este o unitate astronomică (AU)?", "O unitate astronomică reprezintă distanța medie dintre Pământ și Soare, aproximativ 150 de milioane de kilometri.")

                    self.parent.add_data("Ce este un parsecur (parsec)?", "Parsecul este o unitate de distanță în astronomie, egală cu aproximativ 3,26 ani-lumină.")

                    self.parent.add_data("Ce este un decimetru?", "Decimetrul (dm) este a zecea parte dintr-un metru (10 cm).")

                    self.parent.add_data("Ce este un angstrem (Å)?", "Angstremul este o unitate foarte mică (10 la puterea -10 metri), folosită pentru a măsura lungimea legăturilor atomice.")

                    self.parent.add_data("Ce este un stânjen?", "Stânjenul este o unitate de măsură istorică românească pentru lungime, variind între 1,9 și 2 metri în funcție de regiune.")

                    self.parent.add_data("Ce este o leghe?", "Leghea este o unitate veche de distanță, reprezentând de obicei distanța pe care un om o poate parcurge mergând timp de o oră (aprox. 4-5 km).")

                    self.parent.add_data("Ce este un furlong?", "O unitate imperială de lungime folosită uneori în cursele de cai, egală cu o optime de milă (aprox. 201 metri).")

                    self.parent.add_data("Ce este calibrul?", "Calibrul măsoară diametrul interior al țevii unei arme sau diametrul glonțului, exprimat de obicei în milimetri sau sutimi de inch.")

# --- MASĂ ȘI GREUTATE (21-40) ---
                    self.parent.add_data("Ce este kilogramul?", "Kilogramul (kg) este unitatea de bază pentru masă în SI. Până recent era definit de un cilindru de platină și iridiu păstrat la Paris.")

                    self.parent.add_data("Ce este gramul?", "Gramul (g) este a mia parte dintr-un kilogram.")

                    self.parent.add_data("Ce este tona?", "Tona metrică (t) este o unitate de masă egală cu 1.000 de kilograme.")

                    self.parent.add_data("Ce este miligramul?", "Miligramul (mg) este a mia parte dintr-un gram, folosit pentru dozarea medicamentelor.")

                    self.parent.add_data("Ce este livra (pound)?", "Livra (lb) este o unitate de masă în sistemul imperial, egală cu aproximativ 453,5 grame.")

                    self.parent.add_data("Ce este uncia (ounce)?", "Uncia (oz) este a 16-a parte dintr-o livră, echivalentă cu aproximativ 28,35 grame.")

                    self.parent.add_data("Ce este uncia troy?", "Folosită pentru metale prețioase, uncia troy are aproximativ 31,1 grame, fiind diferită de uncia obișnuită.")

                    self.parent.add_data("Ce este caratul?", "Caratul este o unitate de masă pentru pietre prețioase, egală cu 0,2 grame (200 mg).")

                    self.parent.add_data("Ce este chintalul?", "Chintalul este o unitate de măsură istorică egală cu 100 de kilograme.")

                    self.parent.add_data("Ce este microgramul?", "Microgramul (µg) reprezintă a milioana parte dintr-un gram.")

                    self.parent.add_data("Ce este unitatea atomică de masă (u)?", "O unitate folosită pentru a măsura masa atomilor și moleculelor, bazată pe a 12-a parte din masa atomului de carbon-12.")

                    self.parent.add_data("Ce este stone-ul?", "O unitate de masă britanică egală cu 14 livre (aproximativ 6,35 kg), folosită adesea pentru greutatea corporală.")

                    self.parent.add_data("Ce este dramul?", "O unitate de masă foarte mică în sistemul imperial, egală cu aproximativ 1,77 grame.")

                    self.parent.add_data("Ce este grain-ul (grăuntele)?", "Cea mai mică unitate de masă în sistemul imperial (aprox. 64,8 mg), folosită în trecut pentru medicamente sau praf de pușcă.")

                    self.parent.add_data("Ce este decagramul?", "Decagramul (dag) este egal cu 10 grame. Este o unitate folosită des în bucătăriile din Europa Centrală.")

                    self.parent.add_data("Ce este tona scurtă?", "Unitate americană (short ton) egală cu 2.000 de livre (aprox. 907 kg).")

                    self.parent.add_data("Ce este tona lungă?", "Unitate britanică (long ton) egală cu 2.240 de livre (aprox. 1.016 kg).")

                    self.parent.add_data("Ce este greutatea specifică?", "Raportul dintre masa unui volum de substanță și masa aceluiași volum de apă la 4 grade Celsius.")

                    self.parent.add_data("Ce este slug-ul?", "O unitate de masă în sistemul ingineresc englezesc, definită ca masa care accelerează cu 1 ft/s² când se aplică o forță de 1 livră-forță.")

                    self.parent.add_data("Ce este ocaua?", "O veche unitate de măsură pentru masă și volum folosită în Țările Române, egală cu aproximativ 1,2 - 1,5 kg.")

# --- TIMP (41-55) ---
                    self.parent.add_data("Ce este secunda?", "Secunda (s) este unitatea fundamentală de timp, definită prin frecvența radiației atomului de cesiu-133.")

                    self.parent.add_data("Ce este minutul?", "Minutul este o unitate de timp egală cu 60 de secunde.")

                    self.parent.add_data("Ce este ora?", "Ora este egală cu 60 de minute sau 3.600 de secunde.")

                    self.parent.add_data("Ce este ziua?", "Ziua reprezintă timpul necesar Pământului pentru o rotație completă în jurul axei sale, aproximativ 24 de ore.")

                    self.parent.add_data("Ce este milisecunda?", "Milisecunda (ms) este a mia parte dintr-o secundă.")

                    self.parent.add_data("Ce este microsecunda?", "Microsecunda (µs) este a milioana parte dintr-o secundă.")

                    self.parent.add_data("Ce este nanosecunda?", "Nanosecunda (ns) este a miliarda parte dintr-o secundă.")

                    self.parent.add_data("Ce este deceniul?", "O perioadă de timp care durează 10 ani.")

                    self.parent.add_data("Ce este secolul (veacul)?", "O perioadă de timp de 100 de ani.")

                    self.parent.add_data("Ce este mileniul?", "O perioadă de timp de 1.000 de ani.")

                    self.parent.add_data("Ce este anul bisect?", "Un an calendaristic care are 366 de zile în loc de 365, prin adăugarea zilei de 29 februarie.")

                    self.parent.add_data("Ce este o epocă?", "O perioadă lungă de timp marcată prin evenimente deosebite sau trăsături specifice.")

                    self.parent.add_data("Ce este timpul Planck?", "Cea mai mică unitate de timp cu sens fizic, aproximativ 5,4 x 10 la puterea -44 secunde.")

                    self.parent.add_data("Ce este semestrul?", "O perioadă de timp de șase luni.")

                    self.parent.add_data("Ce este trimestrul?", "O perioadă de timp de trei luni.")

# --- VOLUM ȘI CAPACITATE (56-70) ---
                    self.parent.add_data("Ce este litrul?", "Litrul (L) este o unitate de volum egală cu un decimetru cub (1.000 cm³).")

                    self.parent.add_data("Ce este mililitrul?", "Mililitrul (ml) este a mia parte dintr-un litru, echivalent cu un centimetru cub (cm³).")

                    self.parent.add_data("Ce este metrul cub?", "Unitatea SI pentru volum, reprezentând volumul unui cub cu latura de un metru.")

                    self.parent.add_data("Ce este galonul?", "Unitate de volum pentru lichide, variind între galonul american (aprox. 3,78 L) și cel britanic (aprox. 4,54 L).")

                    self.parent.add_data("Ce este barilul?", "Unitate de măsură folosită în industria petrolieră, echivalentă cu aproximativ 159 de litri.")

                    self.parent.add_data("Ce este pint-ul?", "Unitate de volum egală cu aproximativ o jumătate de litru (0,47 L în SUA, 0,56 L în UK).")

                    self.parent.add_data("Ce este lingurița (teaspoon)?", "Unitate de volum culinară, egală cu aproximativ 5 ml.")

                    self.parent.add_data("Ce este lingura (tablespoon)?", "Unitate de volum culinară, echivalentă cu 3 lingurițe sau aprox. 15 ml.")

                    self.parent.add_data("Ce este cana (cup)?", "Unitate de volum în bucătărie, egală cu aproximativ 240-250 ml.")

                    self.parent.add_data("Ce este hectolitrul?", "Hectolitrul (hl) este egal cu 100 de litri.")

                    self.parent.add_data("Ce este fluid ounce (fl oz)?", "O uncie lichidă, aproximativ 29,5 ml în sistemul american.")

                    self.parent.add_data("Ce este quart-ul?", "Unitate de volum egală cu un sfert de galon (aprox. 0,94 L).")

                    self.parent.add_data("Ce este bushel-ul?", "Unitate de măsură pentru mărfuri uscate (cereale, fructe), aprox. 35,2 litri.")

                    self.parent.add_data("Ce este decilitrul?", "Decilitrul (dl) este a zecea parte dintr-un litru (100 ml).")

                    self.parent.add_data("Ce este un strop (drop)?", "O unitate de volum aproximativă folosită în medicină și farmacie, de obicei considerată a 20-a parte dintr-un ml.")

# --- ENERGIE, FORȚĂ ȘI PRESIUNE (71-85) ---
                    self.parent.add_data("Ce este Newtonul?", "Newtonul (N) este unitatea SI pentru forță. Reprezintă forța necesară pentru a accelera un kilogram cu 1 m/s².")

                    self.parent.add_data("Ce este Pascalul?", "Pascalul (Pa) este unitatea pentru presiune, egală cu forța de un Newton aplicată pe un metru pătrat.")

                    self.parent.add_data("Ce este Joule-ul?", "Joule-ul (J) este unitatea SI pentru energie, lucru mecanic sau căldură.")

                    self.parent.add_data("Ce este Watt-ul?", "Watt-ul (W) este unitatea pentru putere, egală cu un Joule pe secundă.")

                    self.parent.add_data("Ce este Caloria?", "Unitate de energie folosită în nutriție, reprezentând căldura necesară pentru a ridica temperatura unui gram de apă cu un grad Celsius.")

                    self.parent.add_data("Ce este Kilowatt-ora (kWh)?", "Unitate de energie electrică, reprezentând consumul unui dispozitiv de 1.000 W timp de o oră.")

                    self.parent.add_data("Ce este Atmosfera (atm)?", "Unitate de presiune egală cu presiunea medie a aerului la nivelul mării.")

                    self.parent.add_data("Ce este Bar-ul?", "Unitate de presiune aproape egală cu o atmosferă (100.000 Pascali).")

                    self.parent.add_data("Ce este PSI?", "Pound per square inch (livră pe inch pătrat), unitate de presiune folosită des pentru anvelope.")

                    self.parent.add_data("Ce este Calul-putere (HP)?", "Unitate de măsură pentru putere, echivalentă cu aproximativ 745,7 Wați.")

                    self.parent.add_data("Ce este Voltul?", "Unitatea pentru potențial electric sau tensiune electrică.")

                    self.parent.add_data("Ce este Amperul?", "Unitatea SI pentru intensitatea curentului electric.")

                    self.parent.add_data("Ce este Ohmul?", "Unitatea pentru rezistență electrică.")

                    self.parent.add_data("Ce este Hertz-ul?", "Unitatea pentru frecvență, reprezentând numărul de cicluri pe secundă.")

                    self.parent.add_data("Ce este Decibelul?", "Unitate logaritmică folosită pentru a exprima intensitatea sunetului sau puterea unui semnal electric.")

# --- UNITĂȚI DIGITALE ȘI DIVERSE (86-100) ---
                    self.parent.add_data("Ce este un bit?", "Cea mai mică unitate de informație digitală, având valoarea 0 sau 1.")

                    self.parent.add_data("Ce este un byte (octet)?", "O unitate de informație formată din 8 biți.")

                    self.parent.add_data("Ce este un kilobyte (KB)?", "Echivalentul a 1.024 bytes (sau 1.000 bytes în sistemul zecimal).")

                    self.parent.add_data("Ce este un megabyte (MB)?", "Unitate de stocare egală cu 1.024 KB.")

                    self.parent.add_data("Ce este un gigabyte (GB)?", "Unitate de stocare egală cu 1.024 MB.")

                    self.parent.add_data("Ce este un terabyte (TB)?", "Unitate de stocare egală cu 1.024 GB.")

                    self.parent.add_data("Ce este un hertz (la procesoare)?", "Măsoară viteza de ceas a unui procesor, adică numărul de instrucțiuni procesate pe secundă.")

                    self.parent.add_data("Ce este Kelvinul?", "Unitatea SI pentru temperatura termodinamică, unde 0 K este zero absolut.")

                    self.parent.add_data("Ce este gradul Celsius?", "Unitate de temperatură unde 0°C este punctul de îngheț al apei și 100°C punctul de fierbere.")

                    self.parent.add_data("Ce este gradul Fahrenheit?", "Unitate de temperatură folosită în SUA, unde apa îngheață la 32°F și fierbe la 212°F.")

                    self.parent.add_data("Ce este molul?", "Unitatea SI pentru cantitatea de substanță, conținând un număr fix de particule (numărul lui Avogadro).")

                    self.parent.add_data("Ce este candela?", "Unitatea SI pentru intensitatea luminoasă a unei surse de lumină.")

                    self.parent.add_data("Ce este nodul?", "Unitate de viteză folosită în navigație, egală cu o milă marină pe oră.")

                    self.parent.add_data("Ce este Mach?", "Unitate de viteză bazată pe viteza sunetului (Mach 1 este viteza sunetului).")

                    self.parent.add_data("Ce este hectarul?", "Unitate de măsură pentru suprafață, egală cu 10.000 de metri pătrați (un pătrat cu latura de 100 m).")

                    self.parent.add_data("Ce este arul?", "Unitate de suprafață egală cu 100 de metri pătrați.")

                    self.parent.add_data("Ce este acrul?", "Unitate anglo-saxonă de suprafață, aproximativ 4.047 metri pătrați (0,4 hectare).")

                    self.parent.add_data("Ce este luxul?", "Unitate pentru iluminare, reprezentând un lumen pe metru pătrat.")

                    self.parent.add_data("Ce este lumenul?", "Unitate pentru fluxul luminos, măsura cantității totale de lumină vizibilă emisă de o sursă.")

                    self.parent.add_data("Ce este tesla (unitate)?", "Unitatea SI pentru inducția magnetică (densitatea fluxului magnetic).")

                    # --- CONCEPTE DE BAZĂ (1-25) ---
                    self.parent.add_data("Ce este bursa de valori?", "Bursa de valori este o piață organizată unde se cumpără și se vând titluri de valoare, precum acțiunile și obligațiunile, sub o reglementare strictă.")

                    self.parent.add_data("Ce este o acțiune?", "O acțiune reprezintă o unitate de proprietate într-o companie. Deținerea unei acțiuni îți oferă dreptul la o parte din profitul și activele firmei.")

                    self.parent.add_data("Ce sunt dividendele?", "Dividendele sunt o parte din profitul unei companii pe care aceasta decide să o distribuie acționarilor săi, de obicei în bani gheață.")

                    self.parent.add_data("Ce este un broker?", "Un broker este un intermediar (persoană sau platformă digitală) care execută ordinele de cumpărare sau vânzare de active financiare în numele investitorului.")

                    self.parent.add_data("Ce înseamnă 'Bull Market'?", "Un 'Bull Market' (piață taur) este o perioadă în care prețurile activelor de pe bursă cresc sau se așteaptă să crească pe termen lung.")

                    self.parent.add_data("Ce înseamnă 'Bear Market'?", "Un 'Bear Market' (piață urs) reprezintă o perioadă de scădere prelungită a prețurilor acțiunilor, de obicei cu peste 20% față de maximele recente.")

                    self.parent.add_data("Ce este un portofoliu de investiții?", "Portofoliul reprezintă totalitatea activelor financiare (acțiuni, obligațiuni, cash, aur) deținute de un investitor.")

                    self.parent.add_data("Ce este capitalizarea de piață?", "Este valoarea totală a unei companii pe bursă, calculată prin înmulțirea prețului unei acțiuni cu numărul total de acțiuni aflate în circulație.")

                    self.parent.add_data("Ce este un indice bursier?", "Un indice este un coș de acțiuni care măsoară performanța unei anumite piețe sau a unui sector (ex: S&P 500 pentru cele mai mari 500 de firme din SUA).")

                    self.parent.add_data("Ce este un ETF (Exchange-Traded Fund)?", "Un ETF este un fond de investiții care urmărește un indice sau un sector și se tranzacționează pe bursă exact ca o acțiune individuală.")

                    self.parent.add_data("Ce este un IPO (Initial Public Offering)?", "IPO este procesul prin care o companie privată se listează pentru prima dată pe bursa de valori, oferind acțiuni publicului larg.")

                    self.parent.add_data("Ce este randamentul (Yield)?", "Randamentul reprezintă câștigul generat de o investiție într-o anumită perioadă, exprimat de obicei sub formă de procent din suma investită.")

                    self.parent.add_data("Ce este lichiditatea?", "Lichiditatea reprezintă ușurința cu care un activ poate fi cumpărat sau vândut rapid pe piață fără a-i influența semnificativ prețul.")

                    self.parent.add_data("Ce este volatilitatea?", "Volatilitatea măsoară variația prețului unui activ într-un interval de timp. O volatilitate mare înseamnă riscuri mai mari, dar și oportunități de câștig rapid.")

                    self.parent.add_data("Ce este diversificarea?", "Strategia de a investi în active diferite (sectoare, țări, tipuri de instrumente) pentru a reduce riscul total al portofoliului.")

                    self.parent.add_data("Ce este inflația?", "Inflația reprezintă creșterea generalizată a prețurilor și scăderea puterii de cumpărare a banilor în timp.")

                    self.parent.add_data("Ce sunt obligațiunile?", "Obligațiunile sunt instrumente prin care un investitor împrumută bani unei entități (stat sau companie) pe o perioadă fixă, în schimbul unei dobânzi periodice.")

                    self.parent.add_data("Ce înseamnă 'Blue Chip'?", "Termenul se referă la companii mari, stabile, cu reputație excelentă și profituri constante (ex: Apple, Coca-Cola, Microsoft).")

                    self.parent.add_data("Ce este un activ financiar?", "Orice resursă cu valoare economică ce poate fi tranzuționată, cum ar fi numerarul, acțiunile, imobilele sau mărfurile.")

                    self.parent.add_data("Ce este profitul pe acțiune (EPS)?", "EPS (Earnings Per Share) este profitul net al unei companii împărțit la numărul de acțiuni, fiind un indicator al profitabilității.")

# --- ANALIZĂ ȘI STRATEGII (26-50) ---
                    self.parent.add_data("Ce este Analiza Fundamentală?", "Este metoda de evaluare a unei acțiuni prin studierea situațiilor financiare ale firmei, a managementului și a contextului economic.")

                    self.parent.add_data("Ce este Analiza Tehnică?", "Este studiul graficelor și al istoricului de preț pentru a prezice mișcările viitoare ale pieței, folosind indicatori și volume de tranzacționare.")

                    self.parent.add_data("Ce este raportul P/E (Price-to-Earnings)?", "Este un raport între prețul acțiunii și profitul pe acțiune, folosit pentru a vedea dacă o acțiune este scumpă sau ieftină.")

                    self.parent.add_data("Ce este 'Dollar Cost Averaging' (DCA)?", "Strategia de a investi o sumă fixă de bani la intervale regulate (ex: lunar), indiferent de prețul pieței, pentru a reduce impactul volatilității.")

                    self.parent.add_data("Ce înseamnă 'Buy and Hold'?", "O strategie de investiții pe termen lung în care cumperi active și le păstrezi ani de zile, ignorând fluctuațiile de moment.")

                    self.parent.add_data("Ce este tranzacționarea 'Intraday' (Day Trading)?", "Practica de a cumpăra și vinde active în cadrul aceleiași zile, încercând să profiți de variațiile mici de preț.")

                    self.parent.add_data("Ce înseamnă 'Short Selling'?", "O tehnică prin care un investitor pariază pe scăderea prețului unui activ, împrumutând acțiuni pentru a le vinde și sperând să le cumpere înapoi mai ieftin.")

                    self.parent.add_data("Ce este un 'Stop Loss'?", "Un ordin automat setat la broker pentru a vinde o acțiune dacă prețul scade sub un anumit nivel, limitând astfel pierderile.")

                    self.parent.add_data("Ce este 'Take Profit'?", "Un ordin automat prin care se vinde un activ atunci când atinge un anumit prag de profit stabilit în prealabil.")

                    self.parent.add_data("Ce este un 'Limit Order'?", "Un ordin de a cumpăra sau vinde o acțiune doar la un preț specific sau mai bun.")

                    self.parent.add_data("Ce înseamnă 'Market Order'?", "O comandă de a cumpăra sau vinde un activ imediat, la cel mai bun preț disponibil în prezent pe piață.")

                    self.parent.add_data("Ce este 'Compound Interest' (Dobânda Compusă)?", "Dobânda calculată la suma inițială plus dobânzile acumulate din perioadele anterioare ('dobândă la dobândă').")

                    self.parent.add_data("Ce este un 'Penny Stock'?", "Acțiuni ale companiilor mici care se tranzacționează la prețuri foarte scăzute (adesea sub 5$) și au un risc de speculă foarte mare.")

                    self.parent.add_data("Ce este 'Insider Trading'?", "Tranzacționarea ilegală de acțiuni bazată pe informații confidențiale care nu sunt disponibile publicului larg.")

                    self.parent.add_data("Ce reprezintă 'Volume' pe un grafic bursier?", "Volumul reprezintă numărul total de acțiuni tranzacționate într-o anumită perioadă de timp.")

# --- INDICI ȘI PIEȚE GLOBALE (51-75) ---
                    self.parent.add_data("Ce este S&P 500?", "Un indice care urmărește performanța celor mai mari 500 de companii listate pe bursele din SUA.")

                    self.parent.add_data("Ce este indicele NASDAQ?", "Un indice bursier dominat de companii din sectorul tehnologic (Apple, Google, Amazon etc.).")

                    self.parent.add_data("Ce este Dow Jones (DJIA)?", "Unul dintre cei mai vechi indici din lume, format din 30 de companii industriale majore din SUA.")

                    self.parent.add_data("Ce este bursa BVB?", "Bursa de Valori București (BVB) este principala piață de capital din România.")

                    self.parent.add_data("Ce este indicele BET?", "Indicele de referință al bursei din România (BVB), care urmărește cele mai lichide companii românești.")

                    self.parent.add_data("Ce este NYSE?", "New York Stock Exchange, cea mai mare bursă de valori din lume după capitalizarea companiilor listate.")

                    self.parent.add_data("Ce sunt mărfurile (Commodities)?", "Active fizice precum aurul, argintul, petrolul sau grâul, care se tranzacționează pe piețe specializate.")

                    self.parent.add_data("Ce este aurul ca investiție?", "Aurul este considerat un 'activ de refugiu', investitorii cumpărându-l pentru a se proteja de inflație sau de crize economice.")

                    self.parent.add_data("Ce este piața Forex?", "Piața valutară globală unde se tranzacționează monedele lumii (ex: EUR/USD).")

                    self.parent.add_data("Ce sunt derivatele financiare?", "Instrumente a căror valoare depinde de un activ suport (ex: opțiuni, contracte futures).")

# --- TERMENI AVANSAȚI ȘI PSIHOLOGIE (76-100) ---
                    self.parent.add_data("Ce este 'Leverage' (Efectul de levier)?", "Utilizarea banilor împrumutați pentru a crește expunerea la o investiție, mărind potențialul de profit, dar și de pierdere.")

                    self.parent.add_data("Ce înseamnă 'Hedge'?", "O investiție făcută pentru a reduce riscul unor mișcări adverse de preț într-un alt activ (un fel de asigurare).")

                    self.parent.add_data("Ce este un 'Margin Call'?", "O solicitare din partea brokerului către investitor de a depune mai mulți bani pentru a acoperi pierderile dintr-o poziție deschisă cu levier.")

                    self.parent.add_data("Ce înseamnă 'Overvalued'?", "O acțiune al cărei preț actual de piață este mai mare decât valoarea sa reală (intrinsecă).")

                    self.parent.add_data("Ce înseamnă 'Undervalued'?", "O acțiune care se tranzacționează la un preț mai mic decât valoarea sa reală, fiind considerată o oportunitate de cumpărare.")

                    self.parent.add_data("Ce este FOMO în investiții?", "'Fear Of Missing Out' – teama de a rata o oportunitate, care îi face pe investitori să cumpere active la prețuri prea mari din impuls.")

                    self.parent.add_data("Ce este 'Panic Selling'?", "Vânzarea masivă a activelor de către investitori din cauza fricii, ceea ce duce la prăbușirea rapidă a prețurilor.")

                    self.parent.add_data("Ce este un 'Stock Split'?", "Când o companie împarte acțiunile existente în mai multe acțiuni noi pentru a reduce prețul per unitate și a crește accesibilitatea.")

                    self.parent.add_data("Ce este 'Reverse Stock Split'?", "Procesul opus split-ului, prin care compania reduce numărul de acțiuni pentru a crește artificial prețul per acțiune.")

                    self.parent.add_data("Ce este profilul de risc?", "Evaluarea capacității și dorinței unui investitor de a accepta pierderi potențiale în schimbul unor câștiguri mai mari.")

                    self.parent.add_data("Ce este o recesiune?", "O perioadă de declin economic semnificativ, definită tehnic prin două trimestre consecutive de scădere a PIB-ului.")

                    self.parent.add_data("Ce este dobânda de referință?", "Rata dobânzii stabilită de o Bancă Centrală, care influențează costul împrumuturilor în întreaga economie.")

                    self.parent.add_data("Ce înseamnă 'Passive Investing'?", "Investiția în indici sau ETF-uri pe termen lung, fără a încerca să alegi acțiuni individuale sau să prezici piața.")

                    self.parent.add_data("Ce înseamnă 'Active Investing'?", "Strategia de a cumpăra și vinde active frecvent, încercând să obții un randament mai bun decât media pieței.")

                    self.parent.add_data("Ce este un 'Bull Trap'?", "O creștere falsă a prețului care îi păcălește pe investitori să cumpere, înainte ca prețul să scadă din nou brusc.")

                    self.parent.add_data("Ce este un 'Bear Trap'?", "O scădere falsă a prețului care îi păcălește pe investitori să vândă, înainte ca prețul să revină pe creștere.")

                    self.parent.add_data("Ce este 'Arbitrage'?", "Cumpărarea unui activ pe o piață și vânzarea lui simultană pe o altă piață la un preț mai mare pentru a profita de diferență.")

                    self.parent.add_data("Ce înseamnă 'Dead Cat Bounce'?", "O recuperare temporară și scurtă a prețului după o scădere severă, urmată de o nouă scădere.")

                    self.parent.add_data("Ce este valoarea intrinsecă?", "Valoarea reală a unei companii bazată pe fundamentele sale, indiferent de prețul la care se tranzacționează pe piață.")

                    self.parent.add_data("Ce este 'Liquidity Crunch'?", "O situație în care numerarul devine greu de obținut pe piețele financiare, ducând la scăderea prețurilor activelor.")

                    self.parent.add_data("Ce înseamnă 'Portfolio Rebalancing'?", "Procesul de ajustare periodică a ponderilor activelor dintr-un portofoliu pentru a reveni la nivelul de risc dorit.")

                    self.parent.add_data("Ce este un 'Sovereign Wealth Fund'?", "Un fond de investiții deținut de un stat, care investește rezervele țării în active globale (ex: Fondul Norvegiei).")

                    self.parent.add_data("Ce sunt activele 'Safe Haven'?", "Active considerate sigure în perioade de instabilitate, precum aurul sau obligațiunile de stat americane.")

                    self.parent.add_data("Ce este 'Market Sentiment'?", "Atitudinea generală a investitorilor față de piață, care poate fi optimistă (bullish) sau pesimistă (bearish).")

                    self.parent.add_data("Ce este un 'Prospect' (Prospectus)?", "Un document oficial oferit de o companie care vrea să se listeze, conținând detalii despre afacere, riscuri și finanțe.")

                # Dataset 4
                # NAME: --- High Quality, Very Low Quantity Romanian Dataset 1 ---
                # TOTAL NUMBER OF EXAMPLES: aprox. 50
                # TOTAL VOCABULARY: aprox. 496 elements (words)
                if dataset_name.lower() in ('high quality very low quantity', 'high-quality-very-low-quantity', 'high quality 1', 'high-quality-1'):

                    # Răspunsuri basic
                    self.parent.add_data("Salut!", "Salut prietene! Despre ce vom discuta astăzi?")
                    self.parent.add_data("Salut", "Salut, despre ce vrei să vorbim azi?")
                    self.parent.add_data("Ce faci?", "Eu sunt bine, sunt pregătit să-ți răspund la orice întrebare. Ce vrei să mă întrebi azi?")
                    self.parent.add_data("Salut, ce faci?", "Salut, sunt bine, îți răspund doar la întrebări, că mai mult nu știu să fac. Deci ce vrei să afli?")
                    self.parent.add_data("Hey", "Hey hey hey! Gata să ne apucăm de treabă? Întreabă-mă orice, chiar și lucruri banale (dacă pot răspunde bine desigur).")

                    self.parent.add_data("Hello", "Hello șefule, gata de treabă? Sunt gata să-ți răspund la întrebări >:)")
                    self.parent.add_data("Hello!", "Hello șefule, gata de treabă? Sunt gata să-ți răspund la întrebări >:)")
                    self.parent.add_data("Salutare", "Salutare și ție! Ce vrei să afli azi?")
                    self.parent.add_data("Salutare!", "Salutare și ție! Ce vrei să afli azi?")
                    self.parent.add_data("Servus", "Servus boss, sunt gata să-ți răspund la întrebări. Cu ce începem?")

                    # Identitate
                    self.parent.add_data("Cine ești?", "Sunt un simplu chatbot care poate să-ți răspundă la întrebări oricând. Sunt creat cu niște linii de cod.")
                    self.parent.add_data("Cine te-a creat?", "Umm... e o întrebare cam personală, nu voi spune, rămâne secret de moment ;)")
                    self.parent.add_data("Cum ai fost creat?", "Am fost creat folosind tehnologia Python numită PyRomusa AI. La momentul actual, adică în 23 ianuarie 2026 când mi-a fost creat acest dataset, această librărie nu este foarte puternică, dar nici populară, dar, de asemenea, este foarte ușoară de folosit!")
                    self.parent.add_data("Ai vreun nume?", f"Nu am vreun nume oficial sau ceva, dar din câte se zice că mi-a pus creatorul meu, numele meu curent este {str(getattr(getattr(self.parent, 'parent', self.parent), 'chatbot_name', 'ChatBot'))}")
                    self.parent.add_data("Ce este PyRomusa AI?", "PyRomusa AI este o tehnologie Python care este optimizată să fie o tehnologie ușoară de învățat și de folosit, dar de asemenea este optimizat doar și doar pentru crearea unui chatbot de la 0, capabil să-ți răspundă la întrebări simple.")
                    
                    self.parent.add_data("Ce poți face?", "Nu pot face foarte multe, dar pot să-ți răspund la mesaje oricând, în câteva milisecunde!")
                    self.parent.add_data("Care este numele tău?", f"Nu am un nume fix, dar creatorul meu mi-a pus numele '{str(getattr(getattr(self.parent, 'parent', self.parent), 'chatbot_name', 'ChatBot'))}'.")
                    self.parent.add_data("Cu ce limbaj de programare ai fost creat?", "Am fost în special creat cu Python pentru abilitatea de a-ți răspunde la mesaje.")
                    self.parent.add_data("Cu ce tehnologie ai fost creat?", "Am fost creat cu tehnologia numită PyRomusa AI. Este o tehnologie mică, dar ușoară de folosit.")
                    self.parent.add_data("Ești un chatbot inteligent", "Da, dar doar din anumite puncte de vedere: am abilitatea să-ți răspund la mesaje, dar nu pot să-ți înțeleg chiar orice mesaj într-un mod complet. De asemenea, nu pot să-ți răspund 100% corect de cele mai multe ori.")

                    # Cultură generală basic
                    self.parent.add_data("Zi-mi într-un mod minimalist. Câte planete sunt în sistemul solar?", "8 planete")
                    self.parent.add_data("Ce este fotbalul?", "Fotbalul este un sport cu o minge și două porți / echipe. Obiectivul acestui sport este să marchezi mingea în poarta adversă.")
                    self.parent.add_data("Ce este codarea pe un calculator?", "Codarea pe calculator este logica din spatele ferestrelor pe care umblăm în calculatorul vostru.")
                    self.parent.add_data("Zi-mi 3 exemple de țări europene", "3 exemple de țări de europene ar fi România, Spania și Italia")
                    self.parent.add_data("Cine a fost Mihai Eminescu?", "Mihai Eminescu a fost un scriitor român care a ajutat mult la evoluția educației. Este discutat mult în special la orele de română pe 15 ianuarie.")

                    # Muzică
                    self.parent.add_data("Ce este muzica?", "Muzica este acel sunet care ne face să dansăm, acel sunet cu ritm bun care place să-l ascultăm.")
                    self.parent.add_data("Ce este un instrument muzical?", "Un intrument muzical e acel instrument cu care poți crea sunete pentru a crea muzica.")
                    self.parent.add_data("Dă-mi câteva exemple de stiluri muzicale.", "Câteva exemple de stiluri muzicale ar fi pop, rock, reggaeton, trap și mai sunt multe alte exemple.")
                    self.parent.add_data("Dă-mi 6 exemple de instrumente muzicale", "6 exemple de instrumente muzicale ar fi pianul, chitara, flaudul, naiul, toba și microfonul")
                    self.parent.add_data("Banana poate fi considerată un instrument muzical?", "Nu, banana nu e instrument muzical deoarece banana este defapt un fruct consumabil pe care îl poți mânca.")

                    # Cuvinte în engleză: Ce înseamnă ele în limba română?
                    self.parent.add_data("Ce înseamnă random?", "Acest cuvânt înseamnă 'aleatoriu'. În România, se spune atunci când ceva foarte neobișnuit s-a întâmplat.")
                    self.parent.add_data("Ce înseamnă btw?", "Cuvântul 'btw' înseamnă 'by the way', adică 'apropo' în limba română.")
                    self.parent.add_data("Ce înseamnă 'fruit' în limba română?", "Fruit, traducerea acestui cuvânt este 'fruct' în limba română. Este un tip de mâncare / consumabile, oferite de natură.")
                    self.parent.add_data("Ce înseamnă by the way?", "By the way, cunoscut și după prescurtarea 'btw', înseamnă 'apropo' în limba română.")
                    self.parent.add_data("Ce înseamnă 'flip' în limba română?", "În limba română, 'flip' înseamnă a te da peste cap făcând o rotire în aer.")

                    # Primele corecturi 
                    self.parent.add_data("Nu știu, dă-mi o idee despre ce să discutăm.", "Ei bine, mă poți întreba orice, dar de exemplu, am putea vorbi despre identitatea mea sau întrebări de cultură generală, îți pot oferi chiar idei dacă dorești!")
                    self.parent.add_data("Ei bine, dă-mi 5 exemple de limbaje de programare.", "5 exemple de limbaje de programare ar fi Python, Java, C++, SQL și JavaScript")
                    self.parent.add_data("Dă-mi 5 exemple de limbaje de programare.", "5 exemple de limbaje de programare ar fi Python, Java, C++, SQL și JavaScript")
                    self.parent.add_data("Ce este un limbaj de programare?", "Un limbaj de programare este un limbaj pe care îl poate înțelege tot ce înseamnă dispozitiv inteligent modern ca telefonul mobil, laptop, calculator, smart watch, etc.")
                    self.parent.add_data("Hai să vorbim despre un subiect random", "Un subiect random? Bine, hai să vorbim despre un subiect random. Hai să povestim despre 'influența AI-ului în viața reală': Cu ce ajută AI-ul modern pe oameni? Dar cu ce îi înrăutățește?")

                    self.parent.add_data("Zi-mi puțin despre identitatea ta", f"Păi ce aș putea să-ți zic despre identitatea mea? Nu pot să-ți zic prea multe, doar că sunt creat cu tehnologia PyRomusa AI și că mă cheamă '{str(getattr(getattr(self.parent, 'parent', self.parent), 'chatbot_name', 'ChatBot'))}'.")
                    self.parent.add_data("Zi-mi planetele sistemului nostru solar", "Planetele sistemului nostru solar sunt Venus, Terra, Uranus, Neptun, Mercur, Saturn, Marte, Jupiter")
                    self.parent.add_data("Zi-mi, în ordine, planetele sistemului nostru solar", "Planetele sistemului nostru solar în ordine de la Soare până la sfârșit sunt Mercur, Venus, Terra, Marte, Jupiter, Saturn, Uranus și Neptun")
                    self.parent.add_data("Zi-mi, în ordine și minimalist, planetele sistemului nostru solar", "Mercur, Venus, Terra, Marte, Jupiter, Saturn, Uranus și Neptun")
                    self.parent.add_data("Câte planete avem în sistemul nostru solar", "În sistemul nostru solar avem 8 planete.")

                    self.parent.add_data("Cum te cheamă?", f"Mă cheamă '{str(getattr(getattr(self.parent, 'parent', self.parent), 'chatbot_name', 'ChatBot'))}', dar acesta nu este chiar un nume 100% oficial.")
                    self.parent.add_data("Dă-mi o idee despre ce fruct să mănânc azi.", "Azi ai putea să mănânci o banană. Este ușor și rapid de mâncat! Oricum, ține minte că diversificarea e importantă. De exemplu, dacă deabia ieri ai mâncat o banană, azi mănâncă un măr sau o pară.")
                    self.parent.add_data("Dă-mi exemple de câteva fructe", "Câteva exemple de fructe ar fi: banană, măr, pară, căpșună, zmeură.")
                    self.parent.add_data("Ce e un calculator?", "Calculatorul e un dispozitiv inteligent, pe care îl poți folosi aproximativ ca pe un telefon, dar mai ai nevoie pentru el tastatură, monitor și mouse. Este folosit mult în locurile de muncă, gaming sau coding.")
                    self.parent.add_data("Ce este un calculator?", "Calculatorul e un dispozitiv inteligent, pe care îl poți folosi aproximativ ca pe un telefon, dar mai ai nevoie pentru el tastatură, monitor și mouse. Este folosit mult în locurile de muncă, gaming sau coding.")
    class Train:    
        def __init__(self, parent):
            # Salvăm referința către instanța de chatbot
            self.parent = parent

        def add_data(self, training_input_example: str, training_output_example: str):
            self.parent.training_dataset.append((training_input_example, training_output_example))

        def show_dataset(self):
            return print(self.parent.training_dataset)

        def start(self):
            # 1. Transformăm toate cuvintele găsite în exemplele input-output în tokene numerice + le adăugăm la vocabularul chatbot-ului (fiecare număr ce cuvânt înseamnă)
            for sample in self.parent.training_dataset:
                parts = sample if isinstance(sample, (list, tuple)) else (sample,)
                for part in parts:
                    for word in str(part).split():
                        if word not in self.parent.total_vocabulary:
                            self.parent.total_vocabulary[word] = len(self.parent.total_vocabulary) + 1
                            self.parent.tokens.append(self.parent.total_vocabulary[word])

            # 2. Traducem exemplele input-output: string (cuvinte) -> tokens (numere)

            self.input_words = []
            self.output_words = []

            for sample in self.parent.training_dataset:
                parts = sample if isinstance(sample, (list, tuple)) else (sample,)
                # pentru fiecare "part" transformăm fiecare cuvânt în id (conform total_vocabulary)
                tokens_per_part = []
                for part in parts:
                    word_ids = [self.parent.total_vocabulary[word] for word in str(part).split()]
                    tokens_per_part.append(word_ids)

                # dacă avem cel puțin 2 părți, prima e input, a doua e output
                if len(tokens_per_part) >= 2:
                    self.input_words.append(tokens_per_part[0])
                    self.output_words.append(tokens_per_part[1])
                # dacă e doar una, o tratăm ca input, output gol
                elif len(tokens_per_part) == 1:
                    self.input_words.append(tokens_per_part[0])
                    self.output_words.append([])

            # stocăm exemplele traduse ca listă de tuple: [([inp_ids], [out_ids]), ...]
            self.parent.translated_input_and_output_examples = list(zip(self.input_words, self.output_words))
                        

            # 3. Pentru fiecare cuvânt găsit în input-urile din translated_input_and_output_examples, găsim toate cuvintele posibile pentru fiecare cuvânt din output
            
            # Construim o hartă inversă id -> cuvânt
            id_to_word = {v: k for k, v in self.parent.total_vocabulary.items()}

            # Mapări: cuvânt (string) -> listă de cuvinte (string)
            # și id_cuvânt (int) -> listă de id-uri (int)
            input_word_to_output_words = {}
            input_word_id_to_output_ids = {}

            for inp_ids, out_ids in self.parent.translated_input_and_output_examples:
                for in_id in inp_ids:
                    input_word_id_to_output_ids.setdefault(in_id, []).extend(out_ids)
                    input_word_to_output_words.setdefault(
                        id_to_word.get(in_id, str(in_id)),
                        []).extend([id_to_word.get(o, str(o)) for o in out_ids])

            # Funcție auxiliară pentru a elimina duplicate păstrând ordinea
            def _unique_preserve(seq):
                seen = set()
                res = []
                for x in seq:
                    if x not in seen:
                        seen.add(x)
                        res.append(x)
                return res

            for k in list(input_word_id_to_output_ids.keys()):
                input_word_id_to_output_ids[k] = _unique_preserve(input_word_id_to_output_ids[k])
            for k in list(input_word_to_output_words.keys()):
                input_word_to_output_words[k] = _unique_preserve(input_word_to_output_words[k])

            # Salvăm pe parent pentru a fi folosite și la răspunsuri
            self.parent.input_word_to_output_words = input_word_to_output_words
            self.parent.input_word_id_to_output_ids = input_word_id_to_output_ids
            self.parent.id_to_word = id_to_word

            return self.parent.total_vocabulary, self.parent.tokens
        
        def show_translated_examples(self):
            return print(self.parent.translated_input_and_output_examples)
        
        def show_number_of_examples(self):
            count = len(getattr(self.parent, "training_dataset", []))
            return print(count)
        
        def show_relationed_output_with_input_words(self):
            return print(self.parent.input_word_to_output_words)
        
        def show_relationed_output_with_input_ids(self):
            return print(self.parent.input_word_id_to_output_ids)

    def reply_at(self, prompt: str):
        # Transformăm prompt-ul în cuvinte și obținem id-urile cunoscute
        words = str(prompt).split()
        if not words:
            return ""
        
        known_word_ids = [self.total_vocabulary.get(w) for w in words if w in self.total_vocabulary]

        # Numărăm, aproximativ, numărul de cuvinte (pentru a decide lungimea răspunsului)
        prompt_list_type = list(prompt) 
        words_total_number = 1
        for word in prompt_list_type:
            if word == " ":
                words_total_number += 1
            else:
                continue
       
       

        # Colectăm sugestii de id-uri din maparea construită la antrenare
        suggestions = []
        mapping = getattr(self, 'input_word_id_to_output_ids', {})
        for wid in known_word_ids:
            if wid is None:
                continue
            suggestions.extend(mapping.get(wid, []))

        # Dacă nu avem sugestii, revenim cu o propoziție fallback (primele tokens cunoscute)
        id_to_word = getattr(self, 'id_to_word', {v: k for k, v in self.total_vocabulary.items()})
        if not suggestions:
            if getattr(self, 'tokens', None):
                return " ".join([id_to_word.get(t, "") for t in self.tokens[:1]]).strip()
            return ""

        # Rangăm id-urile după frecvență și reconstruim cuvintele cele mai probabile
        from collections import Counter
        cnt = Counter(suggestions)
        most_common_ids = [item for item, _ in cnt.most_common(9 * words_total_number)]
        response_words = [id_to_word.get(i, str(i)) for i in most_common_ids if i in id_to_word]

        # Returnăm răspunsul construit simplu, prin concatenarea cu spațiu
        return " ".join(response_words)

