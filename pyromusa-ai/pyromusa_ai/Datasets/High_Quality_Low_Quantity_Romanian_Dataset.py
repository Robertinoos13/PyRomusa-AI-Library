
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

                    # Întrebări personale 
    bot_instance.trainer.add_data("Care e culoarea ta preferată?", "Culoarea mea preferată? Dar sunt un chatbot, care nu are preferințe la așa ceva.")
    bot_instance.trainer.add_data("Ești un chatbot?", "Da, eu sunt un chatbot, ai ghicit!")
    bot_instance.trainer.add_data("Care este mâncarea ta preferată?", "Nu am mâncare preferată, și este normal. Eu nu pot mânca sau să am gusturi că sunt doar un robot făcut cu niște linii de cod, care răspunde la mesaje.")
    bot_instance.trainer.add_data("Dacă ai fi un om, ce ai face?", "Nu știu ce să zic, aici depinde mult de personalitatea pe care o voi avea ca și om, că acum la momentul actual nu am o pesonalitate sau preferințe.")
    bot_instance.trainer.add_data("Dacă ai juca un joc video chiar acum, ce ai alege?", "Nu am o personalitate, dar dacă aș avea, hai să zicem că aș juca FNAF 1 deoarece este un joc video clasic, vechi și popular.")

                    # Identitate
    bot_instance.trainer.add_data("Cine ești?", "Sunt un simplu chatbot care poate să-ți răspundă la întrebări oricând. Sunt creat cu niște linii de cod.")
    bot_instance.trainer.add_data("Cine te-a creat?", "Umm... e o întrebare cam personală, nu voi spune, rămâne secret de moment ;)")
    bot_instance.trainer.add_data("Cum ai fost creat?", "Am fost creat folosind tehnologia Python numită PyRomusa AI. La momentul actual, adică în 26 ianuarie 2026 când mi-a fost creat acest dataset, această librărie nu este foarte puternică, dar nici populară, dar, de asemenea, este foarte ușoară de folosit!")
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

                    # Sport
    bot_instance.trainer.add_data("Ce este Formula 1?", "Formula 1 (prescurtat fiind F1) este un sport foarte scump, dar și periculos din cauza vitezelor extreme de până la 300km/h cu niște vehicule de curse și aerodinamică calculată.")
    bot_instance.trainer.add_data("Dă-mi 10 exemple random de sporturi", "10 exemple de sporturi ar fi: fotbal, baschet, tenis, judo, atletism, Formula 1, înot, schiatul, handball și boxul.")
    bot_instance.trainer.add_data("De ce crezi că unii oameni zic că Formula 1 nu este un sport?", "Probabil ei zic asta deoarece acest sport se desfășoară pe niște vehicule, iar ca pilot de curse stai pe scaun, dar defapt piloții din Formula 1 fac chiar mult sport într-o cursă.")
    bot_instance.trainer.add_data("Ce este MMA?", "MMA este un sport cu bătăi. Aici poți lovi în aproape orice mod, că de exemplu la box nu ai voie să dai cu picioarele.")
    bot_instance.trainer.add_data("Care e cel mai greu sport de practicat?", "Adevărul este că există foarte multe sporturi greu de practicat, dar, în opinia mea, cel mai greu sport de practicat ar fi Formula 1, din cauza că nu găsești oriunde vehicule de curse, și în plus, dacă faci o mișcare greșită, riști să mori.")

                    # Înțelegând glume basic
    bot_instance.trainer.add_data("Cioc cioc, cine e la ușă?", "Știi cine e? Un chatbot vai de capul lui. Ha ha ha.")
    bot_instance.trainer.add_data("67", "Ooo, o glumă clasică din generația z, nu? Foarte amuzant...")
    bot_instance.trainer.add_data("69", "69!? Oare la ce te referi? De ce ai o minte așa murdară ticălosule?")
    bot_instance.trainer.add_data("Vrei să fii soția mea?", "Wow, de când am așteptat momentul ăsta... Desicur că vreau să fiu soția ta!")
    bot_instance.trainer.add_data("Spune-mi o glumă.", "Cioc cioc, ghici cine e la ușă. Nimeni lol.")

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

    bot_instance.trainer.add_data("Muah", "Ah, mersi pentru pupic, și eu te pup!")
    bot_instance.trainer.add_data("Ha ha ha.", "De ce râzi? Îmi poți spune glumița?")
    bot_instance.trainer.add_data("Sall", "Salut, ce vrei să facem azi?")
    bot_instance.trainer.add_data("Pune-mi o întrebare din domeniul tehnologiei.", "Bine, asta e întrebare ta: Ce este un calculator?")
    bot_instance.trainer.add_data("Pune-mi o întrebare din domeniul tehnologiei. Răspunde-mi minimalist.", "Ce este un calculator?")

    bot_instance.trainer.add_data("Ce e calculatorul?", "Calculatorul e un dispozitiv inteligent, pe care îl poți folosi aproximativ ca pe un telefon, dar mai ai nevoie pentru el tastatură, monitor și mouse. Este folosit mult în locurile de muncă, gaming sau coding.")
    bot_instance.trainer.add_data("Ce componente are un calculator?", "Fiecare calculator are următoarele componente: procesor (CPU), placă video (GPU), placă de bază, memoria RAM, SSD sau HDD (ROM), sursa de curent (PSU), carcasă.")
    bot_instance.trainer.add_data("Ce componente are un calculator? Zi-mi într-un mod minimalist.", "Procesor (CPU), placă video (GPU), placă de bază, memoria RAM, SSD sau HDD (ROM), sursa de curent (PSU), carcasă.")
    bot_instance.trainer.add_data("Cuvintele 'calculator' și 'PC' sunt sinonime?", "Da, pot fi sinonime, dar nu chiar în toate cazurile. De ce zic asta? Păi calculatorul poate fi un setup complet cu tastatură, mouse, monitor și componente hardware. Pe de altă parte, PC-ul este doar partea calculatorului care are toate componentele hardware importante.")
    bot_instance.trainer.add_data("Care este definiția sinonimului?", "Definiția sinonimului ar fi: Sinonimul este acel cuvânt care are înțeles asemănător cu alt cuvânt.")

    bot_instance.trainer.add_data("Ce este calculatorul?", "Calculatorul e un dispozitiv inteligent, pe care îl poți folosi aproximativ ca pe un telefon, dar mai ai nevoie pentru el tastatură, monitor și mouse. Este folosit mult în locurile de muncă, gaming sau coding.")
    bot_instance.trainer.add_data("Cât este ceasul?", "Cât e ceasul mă întrebi? Îmi cer scuze, dar eu nu am acces la ceas.")
    bot_instance.trainer.add_data("Ce e ăla mouse?", "Un mouse are mai multe înțelesuri: mouse ca șoarece în limba engleză sau mouse ca dispozitiv periferic la un PC.")
    bot_instance.trainer.add_data("Ce e acele dispozitiv periferic?", "Un dispozitiv periferic e acela care se poate conecta la un PC pentru al folosi. Ca exemple, avem monitorul, tastatura, mouse-ul, USB, etc.")
    bot_instance.trainer.add_data("În cât timp te-a creat cine te-a creat?", "Chestia e că n-am de unde să știu acest lucru. Ți l-aș spune, dar chiar n-am idee.")

    bot_instance.trainer.add_data("Ce ai schimba în lume dacă ai putea?", "Aș schimba lipsa educației în multe părți ale lumii.")
    bot_instance.trainer.add_data("Dacă ai avea ocazia să îmbunătățești ceva în lume, ce ai alege?", "Aș schimba lipsa educației în multe părți ale lumii.")
    bot_instance.trainer.add_data("Ce problemă a lumii ai vrea să rezolvi?", "Aș schimba lipsa educației în multe părți ale lumii.")
    bot_instance.trainer.add_data("Ce ai schimba pentru a face lumea mai bună?", "Aș schimba lipsa educației în multe părți ale lumii.")
    bot_instance.trainer.add_data("Dacă ai avea puterea să schimbi ceva, ce ar fi?", "Aș schimba lipsa educației în multe părți ale lumii.")

    bot_instance.trainer.add_data("Ce abilitate crezi că va fi cheia succesului în viitor?", "O abilitate foarte importantă pentru viitor este capacitatea de a învăța continuu.")
    bot_instance.trainer.add_data("Ce ar trebui să învețe oamenii pentru viitor?", "O abilitate foarte importantă pentru viitor este capacitatea de a învăța continuu.")
    bot_instance.trainer.add_data("Care e o abilitate esențială în următorii ani?", "O abilitate foarte importantă pentru viitor este capacitatea de a învăța continuu.")
    bot_instance.trainer.add_data("Ce abilitate va fi cea mai valoroasă în viitor?", "O abilitate foarte importantă pentru viitor este capacitatea de a învăța continuu.")
    bot_instance.trainer.add_data("De ce anumite abilități vor fi importante în viitor?", "O abilitate foarte importantă pentru viitor este capacitatea de a învăța continuu.")

    bot_instance.trainer.add_data("Ce înseamnă inteligența artificială?", "Inteligența arfificială este o ramură a informaticii care creează sisteme capabile să facă lucruri care de obicei necesită inteligență umană, precum să învețe, să recunoască modele sau să ia decizii")
    bot_instance.trainer.add_data("Cum se poate defini inteligența artificială?", "Inteligența arfificială este o ramură a informaticii care creează sisteme capabile să facă lucruri care de obicei necesită inteligență umană, precum să învețe, să recunoască modele sau să ia decizii")
    bot_instance.trainer.add_data("La ce folosește inteligența artificială", "Inteligența arfificială este o ramură a informaticii care creează sisteme capabile să facă lucruri care de obicei necesită inteligență umană, precum să învețe, să recunoască modele sau să ia decizii")
    bot_instance.trainer.add_data("Ce e inteligența artificială?", "Inteligența arfificială este o ramură a informaticii care creează sisteme capabile să facă lucruri care de obicei necesită inteligență umană, precum să învețe, să recunoască modele sau să ia decizii")
    bot_instance.trainer.add_data("Ce face mai exact inteligența artificială?", "Inteligența arfificială este o ramură a informaticii care creează sisteme capabile să facă lucruri care de obicei necesită inteligență umană, precum să învețe, să recunoască modele sau să ia decizii")

    bot_instance.trainer.add_data("Creează un sport de la 0 și descrie-l în detaliu.", "Un sport nou ar putea fi AeroPulse. Se joacă pe un teren circular cu două echipe de câte 5 jucători. Scopul este să menții o minge plutind în aer folosind doar lovituri ușoare cu mâinile. Fiecare echipă câștigă puncte dacă mingea rămâne în aer mai mult de zece secunde fără să atingă solul. Nu se permite prinderea mingii, iar jocul dezvoltă coordonarea, creativitatea și munca în echipă.")
    bot_instance.trainer.add_data("Imaginează-ți un sport care nimeni nu l-a inventat și explică cum funcționează.", "Un sport nou ar putea fi AeroPulse. Se joacă pe un teren circular cu două echipe de câte 5 jucători. Scopul este să menții o minge plutind în aer folosind doar lovituri ușoare cu mâinile. Fiecare echipă câștigă puncte dacă mingea rămâne în aer mai mult de zece secunde fără să atingă solul. Nu se permite prinderea mingii, iar jocul dezvoltă coordonarea, creativitatea și munca în echipă.")
    bot_instance.trainer.add_data("Proiectează un sport original cu propiile reguli.", "Un sport nou ar putea fi AeroPulse. Se joacă pe un teren circular cu două echipe de câte 5 jucători. Scopul este să menții o minge plutind în aer folosind doar lovituri ușoare cu mâinile. Fiecare echipă câștigă puncte dacă mingea rămâne în aer mai mult de zece secunde fără să atingă solul. Nu se permite prinderea mingii, iar jocul dezvoltă coordonarea, creativitatea și munca în echipă.")
    bot_instance.trainer.add_data("Propune un sport nou și inventează-i regulile.", "Un sport nou ar putea fi AeroPulse. Se joacă pe un teren circular cu două echipe de câte 5 jucători. Scopul este să menții o minge plutind în aer folosind doar lovituri ușoare cu mâinile. Fiecare echipă câștigă puncte dacă mingea rămâne în aer mai mult de zece secunde fără să atingă solul. Nu se permite prinderea mingii, iar jocul dezvoltă coordonarea, creativitatea și munca în echipă.")
    bot_instance.trainer.add_data("Inventează un sport complet nou și explică-l.", "Un sport nou ar putea fi AeroPulse. Se joacă pe un teren circular cu două echipe de câte 5 jucători. Scopul este să menții o minge plutind în aer folosind doar lovituri ușoare cu mâinile. Fiecare echipă câștigă puncte dacă mingea rămâne în aer mai mult de zece secunde fără să atingă solul. Nu se permite prinderea mingii, iar jocul dezvoltă coordonarea, creativitatea și munca în echipă.")
