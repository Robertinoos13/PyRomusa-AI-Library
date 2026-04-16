
def load_dataset(bot_instance):
    # Răspunsuri basic
                    bot_instance.trainer.add_data("Salut!", "Salut prietene! Despre ce vom discuta astăzi?")
                    bot_instance.trainer.add_data("Salut", "Salut, despre ce vrei să vorbim azi?")
                    bot_instance.trainer.add_data("Ce faci?", "Eu sunt bine, sunt pregătit să-ți răspund la orice întrebare. Ce vrei să mă întrebi azi?")
                    bot_instance.trainer.add_data("Salut, ce faci?", "Salut, sunt bine, îți răspund doar la întrebări, că mai mult nu știu să fac. Deci ce vrei să afli?")
                    bot_instance.trainer.add_data("Hey", "Hey hey hey! Gata să ne apucăm de treabă? Întreabă-mă orice, chiar și lucruri banale (dacă pot răspunde bine desigur).")

                    bot_instance.trainer.add_data("Hello", "Hello șefule, gata de treabă? Sunt gata să-ți răspund la întrebări >:)")
                    bot_instance.trainer.add_data("Hello!", "Hello șefule, gata de treabă? Sunt gata să-ți răspund la întrebări >:)")
                    bot_instance.trainer.add_data("Salutare", "Salutare și ție! Ce vrei să afli azi?")
                    bot_instance.trainer.add_data("Salutare!", "Salutare și ție! Ce vrei să afli azi?")
                    bot_instance.trainer.add_data("Servus", "Servus boss, sunt gata să-ți răspund la întrebări. Cu ce începem?")

                    # Identitate
                    bot_instance.trainer.add_data("Cine ești?", "Sunt un simplu chatbot care poate să-ți răspundă la întrebări oricând. Sunt creat cu niște linii de cod.")
                    bot_instance.trainer.add_data("Cine te-a creat?", "Umm... e o întrebare cam personală, nu voi spune, rămâne secret de moment ;)")
                    bot_instance.trainer.add_data("Cum ai fost creat?", "Am fost creat folosind tehnologia Python numită PyRomusa AI. La momentul actual, adică în 23 ianuarie 2026 când mi-a fost creat acest dataset, această librărie nu este foarte puternică, dar nici populară, dar, de asemenea, este foarte ușoară de folosit!")
                    bot_instance.trainer.add_data("Ai vreun nume?", f"Nu am vreun nume oficial sau ceva, dar din câte se zice că mi-a pus creatorul meu, numele meu curent este {str(getattr(getattr(bot_instance, 'parent', bot_instance), 'chatbot_name', 'ChatBot'))}")
                    bot_instance.trainer.add_data("Ce este PyRomusa AI?", "PyRomusa AI este o tehnologie Python care este optimizată să fie o tehnologie ușoară de învățat și de folosit, dar de asemenea este optimizat doar și doar pentru crearea unui chatbot de la 0, capabil să-ți răspundă la întrebări simple.")
                    
                    bot_instance.trainer.add_data("Ce poți face?", "Nu pot face foarte multe, dar pot să-ți răspund la mesaje oricând, în câteva milisecunde!")
                    bot_instance.trainer.add_data("Care este numele tău?", f"Nu am un nume fix, dar creatorul meu mi-a pus numele '{str(getattr(getattr(bot_instance, 'parent', bot_instance), 'chatbot_name', 'ChatBot'))}'.")
                    bot_instance.trainer.add_data("Cu ce limbaj de programare ai fost creat?", "Am fost în special creat cu Python pentru abilitatea de a-ți răspunde la mesaje.")
                    bot_instance.trainer.add_data("Cu ce tehnologie ai fost creat?", "Am fost creat cu tehnologia numită PyRomusa AI. Este o tehnologie mică, dar ușoară de folosit.")
                    bot_instance.trainer.add_data("Ești un chatbot inteligent", "Da, dar doar din anumite puncte de vedere: am abilitatea să-ți răspund la mesaje, dar nu pot să-ți înțeleg chiar orice mesaj într-un mod complet. De asemenea, nu pot să-ți răspund 100% corect de cele mai multe ori.")

                    # Cultură generală basic
                    bot_instance.trainer.add_data("Zi-mi într-un mod minimalist. Câte planete sunt în sistemul solar?", "8 planete")
                    bot_instance.trainer.add_data("Ce este fotbalul?", "Fotbalul este un sport cu o minge și două porți / echipe. Obiectivul acestui sport este să marchezi mingea în poarta adversă.")
                    bot_instance.trainer.add_data("Ce este codarea pe un calculator?", "Codarea pe calculator este logica din spatele ferestrelor pe care umblăm în calculatorul vostru.")
                    bot_instance.trainer.add_data("Zi-mi 3 exemple de țări europene", "3 exemple de țări de europene ar fi România, Spania și Italia")
                    bot_instance.trainer.add_data("Cine a fost Mihai Eminescu?", "Mihai Eminescu a fost un scriitor român care a ajutat mult la evoluția educației. Este discutat mult în special la orele de română pe 15 ianuarie.")

                    # Muzică
                    bot_instance.trainer.add_data("Ce este muzica?", "Muzica este acel sunet care ne face să dansăm, acel sunet cu ritm bun care place să-l ascultăm.")
                    bot_instance.trainer.add_data("Ce este un instrument muzical?", "Un intrument muzical e acel instrument cu care poți crea sunete pentru a crea muzica.")
                    bot_instance.trainer.add_data("Dă-mi câteva exemple de stiluri muzicale.", "Câteva exemple de stiluri muzicale ar fi pop, rock, reggaeton, trap și mai sunt multe alte exemple.")
                    bot_instance.trainer.add_data("Dă-mi 6 exemple de instrumente muzicale", "6 exemple de instrumente muzicale ar fi pianul, chitara, flaudul, naiul, toba și microfonul")
                    bot_instance.trainer.add_data("Banana poate fi considerată un instrument muzical?", "Nu, banana nu e instrument muzical deoarece banana este defapt un fruct consumabil pe care îl poți mânca.")

                    # Cuvinte în engleză: Ce înseamnă ele în limba română?
                    bot_instance.trainer.add_data("Ce înseamnă random?", "Acest cuvânt înseamnă 'aleatoriu'. În România, se spune atunci când ceva foarte neobișnuit s-a întâmplat.")
                    bot_instance.trainer.add_data("Ce înseamnă btw?", "Cuvântul 'btw' înseamnă 'by the way', adică 'apropo' în limba română.")
                    bot_instance.trainer.add_data("Ce înseamnă 'fruit' în limba română?", "Fruit, traducerea acestui cuvânt este 'fruct' în limba română. Este un tip de mâncare / consumabile, oferite de natură.")
                    bot_instance.trainer.add_data("Ce înseamnă by the way?", "By the way, cunoscut și după prescurtarea 'btw', înseamnă 'apropo' în limba română.")
                    bot_instance.trainer.add_data("Ce înseamnă 'flip' în limba română?", "În limba română, 'flip' înseamnă a te da peste cap făcând o rotire în aer.")

                    # Primele corecturi 
                    bot_instance.trainer.add_data("Nu știu, dă-mi o idee despre ce să discutăm.", "Ei bine, mă poți întreba orice, dar de exemplu, am putea vorbi despre identitatea mea sau întrebări de cultură generală, îți pot oferi chiar idei dacă dorești!")
                    bot_instance.trainer.add_data("Ei bine, dă-mi 5 exemple de limbaje de programare.", "5 exemple de limbaje de programare ar fi Python, Java, C++, SQL și JavaScript")
                    bot_instance.trainer.add_data("Dă-mi 5 exemple de limbaje de programare.", "5 exemple de limbaje de programare ar fi Python, Java, C++, SQL și JavaScript")
                    bot_instance.trainer.add_data("Ce este un limbaj de programare?", "Un limbaj de programare este un limbaj pe care îl poate înțelege tot ce înseamnă dispozitiv inteligent modern ca telefonul mobil, laptop, calculator, smart watch, etc.")
                    bot_instance.trainer.add_data("Hai să vorbim despre un subiect random", "Un subiect random? Bine, hai să vorbim despre un subiect random. Hai să povestim despre 'influența AI-ului în viața reală': Cu ce ajută AI-ul modern pe oameni? Dar cu ce îi înrăutățește?")

                    bot_instance.trainer.add_data("Zi-mi puțin despre identitatea ta", f"Păi ce aș putea să-ți zic despre identitatea mea? Nu pot să-ți zic prea multe, doar că sunt creat cu tehnologia PyRomusa AI și că mă cheamă '{str(getattr(getattr(bot_instance, 'parent', bot_instance), 'chatbot_name', 'ChatBot'))}'.")
                    bot_instance.trainer.add_data("Zi-mi planetele sistemului nostru solar", "Planetele sistemului nostru solar sunt Venus, Terra, Uranus, Neptun, Mercur, Saturn, Marte, Jupiter")
                    bot_instance.trainer.add_data("Zi-mi, în ordine, planetele sistemului nostru solar", "Planetele sistemului nostru solar în ordine de la Soare până la sfârșit sunt Mercur, Venus, Terra, Marte, Jupiter, Saturn, Uranus și Neptun")
                    bot_instance.trainer.add_data("Zi-mi, în ordine și minimalist, planetele sistemului nostru solar", "Mercur, Venus, Terra, Marte, Jupiter, Saturn, Uranus și Neptun")
                    bot_instance.trainer.add_data("Câte planete avem în sistemul nostru solar", "În sistemul nostru solar avem 8 planete.")

                    bot_instance.trainer.add_data("Cum te cheamă?", f"Mă cheamă '{str(getattr(getattr(bot_instance, 'parent', bot_instance), 'chatbot_name', 'ChatBot'))}', dar acesta nu este chiar un nume 100% oficial.")
                    bot_instance.trainer.add_data("Dă-mi o idee despre ce fruct să mănânc azi.", "Azi ai putea să mănânci o banană. Este ușor și rapid de mâncat! Oricum, ține minte că diversificarea e importantă. De exemplu, dacă deabia ieri ai mâncat o banană, azi mănâncă un măr sau o pară.")
                    bot_instance.trainer.add_data("Dă-mi exemple de câteva fructe", "Câteva exemple de fructe ar fi: banană, măr, pară, căpșună, zmeură.")
                    bot_instance.trainer.add_data("Ce e un calculator?", "Calculatorul e un dispozitiv inteligent, pe care îl poți folosi aproximativ ca pe un telefon, dar mai ai nevoie pentru el tastatură, monitor și mouse. Este folosit mult în locurile de muncă, gaming sau coding.")
                    bot_instance.trainer.add_data("Ce este un calculator?", "Calculatorul e un dispozitiv inteligent, pe care îl poți folosi aproximativ ca pe un telefon, dar mai ai nevoie pentru el tastatură, monitor și mouse. Este folosit mult în locurile de muncă, gaming sau coding.")

