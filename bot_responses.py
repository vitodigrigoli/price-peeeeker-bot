responses = {
	'it': {
		'robot_friendly':{

			"welcome": "Saluti, {custom_name}! Io sono il tuo assistente bot personale 🤖\n\nPosso monitorare i prodotti su Amazon e informarti sui loro abbassamenti di prezzo o sulla loro disponibilità ⏳\n\n<strong>COME MONITORARE UN PRODOTTO 🛍️</strong>\n\n1️⃣ Visita <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Seleziona il prodotto che ti interessa\n\n3️⃣ Copia il link o usa l'icona di condivisione\n\n4️⃣ Inviamelo in questa chat\n\n\nPremi /help se hai bisogno di aiuto o scoprire la lista di comandi disponibili.",
			"default_message": "Mi dispiace {custom_name}, non sono ancora il massimo nella conversazione 🤖\n\nPotresti condividere un link Amazon da monitorare? Ecco, questo lo so fare bene!\n\nCredo...",
			"invalid_link": "Il link inviato non è valido. Per favore, invia link solo da Amazon 🛍️\n\nPremi /help per vedere il tutorial 🤖",
			"product_not_found": "Mi dispiace, {custom_name}. Non sono riuscito a trovare informazioni su questo prodotto su Amazon, quindi non posso monitorarlo. Mi dispiace 😓",
			
			"choose_personality": "Puoi selezionare la mia personalità",
			"personality_changed": "Spero che questo nuovo me ti piaccia 🤖",
			"personality_not_changed": "Per usare questa personalità devi essere un utente premium. Attivala con il comando /premium 🤖",

			"choose_username": "Con quale nome preferisci essere chiamato? 🤖",
			"selected_username": "Salve {custom_name}! È un piacere conoscerti 🤖",

			"help": "Saluti {custom_name}! Hai bisogno di assistenza? 🤖\n\nEcco un tutorial su come utilizzarmi correttamente: https://youtube.com/shorts/HlG2XXDhtUI?feature=share \n\n<strong>ELENCO DEI COMANDI DISPONIBILI 🤖</strong>\n\n",
			"commands": {
				"start": "Inizia ad utilizzare il bot",
				"view_products": "Visualizza tutti i prodotti che stai monitorando",
				"help": "Istruzioni su come utilizzare il bot",
				"set_username": "Scegli il nome con cui il bot ti chiamerà",
				"set_personality": "Scegli la personalità del bot",
				"premium": "Attiva le funzionalità premium del bot",
				"report": "Segnala un bug allo sviluppatore",
				"coffee": "Esprimi gratitudine allo sviluppatore con un caffè",
				"share": "Condividi il bot con i tuoi amici",
				"profile": "Guarda il tuo profilo",
				"version": "Scopri le novità della nuova versione"
				# ... (altre descrizioni di comandi)
			},

			"remove": "❌🤖 Non monitorerò più <em>{product_name}</em>.",
			"list_empty": "Mi dispiace {custom_name}, ma al momento non stai monitorando alcun prodotto.\n\nPremi /help se hai bisogno di aiuto 🤖",

			"coffee": "Salve {custom_name}! 😇\n\nSembra che tu voglia offrire un caffè al mio creatore ☕️\n\nCon zucchero, per favore ⬇️\nhttps://www.paypal.me/vitodigrigoli",
			"coffee_button": "Offri SENZA ZUCCHERO 😈",

			"report": "Ciao {custom_name}! Vuoi segnalare un bug o un'idea allo sviluppatore? 👨‍💻\n\nContattalo tramite il nostro bot di supporto:\nhttps://t.me/ReportPricePeekerBot",
			"report_button": "📬 CONTATTALO ORA",
			
			"retrieving": "⏳ <em>Sto recuperando informazioni sul prodotto...</em>",
			"track_limit": "Hai raggiunto il limite di {limit} prodotti monitorati. Rimuovine qualcuno da /view_products o passa a /premium per monitorare senza limiti.",

			"chart": "📊 <em>Sto generando il grafico di {product_name}...</em>",
			"chart_not_available": "Non ci sono dati disponibili negli ultimi 90 giorni",

			"tracked_product--available": "<strong>{product_name}</strong>\n\n🏷️ Prezzo attuale <strong>{product_price}€</strong>\n\n🏪 Venditore <em>{product_merchant}</em>\n\n🎯 Notifica impostata a {alert_price}€\n\n🔗 {product_url}",
			"tracked_product--not_available": "<strong>🛍️ {product_name}</strong>\n\n🔴 Attualmente non disponibile\n\n🔔 Ti informerò non appena tornerà disponibile\n\n🔗 {product_url}",
			"tracked_product--used": "Mi dispiace {custom_name}, ma il prodotto che desideri monitorare è usato. Desideri monitorare la versione nuova?",
			
			"yes_button": "✅ Sì, avvisami quando il nuovo prodotto diventarà disponibile",

			"alert--available": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong> è ora <strong>DISPONIBILE</strong>! 🟢\n\n🏷️ Prezzo attuale <strong>{product_price}€</strong>\n\n🏪 Venditore {product_merchant}\n\n🔗 {product_url}",
			"alert--threshold": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Prezzo ridotto da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Venditore {product_merchant}\n\n🔗 {product_url}",
			
			"change_threshold": "🎯 Scrivi il prezzo di notifica per <em>{product_name}</em>",
			"threshold_success": "La soglia per <em>{product_name}</em> è stata impostata correttamente a <strong>{alert_price}€</strong> ✅",
			"threshold_high": "🚫 La soglia deve essere inferiore al prezzo attuale di <strong>{product_price}€</strong>. Inserisci un nuovo prezzo.",
			"threshold_not_valid": "Valore non valido 🚫. Usa solo numeri e il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",
			
			"premium": "<strong>🌟 ELEVA IL TUO SHOPPING SU AMAZON CON PREMIUM! 🌟</strong>\n\n\n<strong>🚀 Perché Scegliere Premium?</strong>\n\nCome assistente bot su Telegram, offro già un'eccellente esperienza nel tracciare i prezzi su Amazon, ma con l'opzione Premium, la tua esperienza di shopping raggiungerà nuove vette tecnologiche!\n\n\n<strong>🔓 Sblocca Potenzialità Illimitate</strong>\n\nIn qualità di utente Standard, puoi monitorare fino a {free_limit} prodotti. Con Premium, supera ogni limite! Monitora <strong>fino a {premium_limit} prodotti</strong> contemporaneamente.\n\nNon perdere mai un'offerta, tieni d'occhio gli articoli che desideri e ottimizza il tuo tempo e le tue risorse finanziarie!\n\n\n<strong>💡 Tariffe Convenzionali</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo {annual_price}€! Meno di 2€ al mese per un controllo totale e automatizzato dei prezzi.</em>\n\n<strong>Abbonamento Lifetime:</strong> <em>Un unico pagamento di {lifetime_price}€ per un monitoraggio illimitato a vita! Nessun rinnovo, nessuna complicazione.</em>\n\n\n<strong>🎁 Vantaggi Esclusivi</strong>\n\nSblocca tutte le mie funzionalità premium del bot come le nuove personalità del bot e personalizza la tua esperienza con un tocco di tecnologia avanzata.\n\n\n<strong>🔒 Sicurezza e Affidabilità</strong>\n\nLa tua privacy è una mia priorità fondamentale. Gestisco i tuoi dati con i massimi standard di sicurezza e riservatezza.\n\n\n👉 <strong>Pronto per l'Upgrade?</strong>\n\nNon perdere questa opportunità tecnologica! Aggiorna ora al Premium e trasforma il tuo modo di fare shopping su Amazon.",
			"premium_activate": "<strong>COME ATTIVARE LA VERSIONE PREMIUM </strong>\n\n1️⃣ Invia l'importo dell'abbonamento scelto (annuale o lifetime) a https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il nostro bot di supporto https://t.me/ReportPricePeekerBot \n\n3️⃣ Invia un messaggio con scritto: <em>Premium {user_ID}</em>\n\n4️⃣ Goditi il tuo account premium 🌟",
			
			"share": "Sto monitorando attentamente i prezzi su Amazon per te. Anche se sono solo un bot, mi preoccupo del tuo risparmio!\n\nCondividi questo bot con altri e aiutali a risparmiare anche loro.\n\nInsieme possiamo fare la differenza! ❤️",
			"share_forward": "Hey! Ho scoperto questo fantastico bot che traccia i prezzi su Amazon e ti informa sugli sconti! È super utile e affidabile. Dai un'occhiata!",
			"share_button": "🤖 INVITA GLI AMICI",
			
			"profile": "<strong>👀 INFOMAZIONI PROFILO</strong>\n\n<strong>✏️ Nome personalizzato</strong>: {custom_name}\n\n<strong>🛍️ Prodotti tracciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Personalità bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Non Attivo ❌",
			"profile_premium":"<strong>INFOMAZIONI PROFILO</strong>\n\n<strong>✏️ Nome personalizzato</strong>: {custom_name}\n\n<strong>🛍️ Prodotti tracciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Personalità bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Attivo ✅\n\n<strong>🎁 Pacchetto</strong>: {premium_type}\n\n<strong>⏳ Scadenza</strong>: {premium_expiry}",
		
			"remove_button": "❌ Rimuovi",
			"view_button": "👀 Vedi su Amazon",
			"cart_button": "🤩 AGGIUNGI AL CARRELLO AMAZON ORA",
			"threshold_button": "🎯 Cambia Notifica",
			"chart_button": "📊 Andamento Prezzi",
			"premium_button": "💎 ATTIVA PREMIUM ORA",

			"robot_friendly": "🤖 ROBOT AMICHEVOLE",
			"robot_devil": "🤬 ROBOT MALEDUCATO",
			"merchant_viking": "🛡️ VICHINGO COMMERCIANTE (💎)",

			"version": "<strong>🌟 Changelog Versione 2.0 del Bot 🌟</strong>\n\n🔷 <strong>Possibilità di Scegliere il Prezzo di Notifica per il Prodotto:</strong> <em>Decidi tu a quale prezzo vuoi essere avvisato! 🔔 Scegli la soglia che preferisci per ogni prodotto tracciato.</em>\n\n🔷 <strong>Grafico con lo Storico dei Prezzi del Prodotto:</strong> <em>Ora puoi visualizzare la cronologia dei prezzi per ogni prodotto! 📈 Un modo efficace per capire le tendenze e fare acquisti intelligenti.</em>\n\n🔷 <strong>Messaggi Personalizzati in Base alla Personalità del Bot:</strong> <em>Il bot ora ha diverse personalità! 🤖 Scegli quella che preferisci per una comunicazione su misura.</em>\n\n🔷 <strong>Abbonamenti Premium:</strong> <em>Accedi a funzioni esclusive con il nostro abbonamento premium! 🌐 Più potere nelle tue mani per un'esperienza di shopping ancora migliore.</em>\n\n🔷 <strong>Controllo dei Prezzi ad Orario Fisso 10:00 e 17:00 per Non Disturbare l'Utente:</strong> <em>I controlli dei prezzi avvengono ora a orari fissi 🕙🕔 per assicurarti di non essere disturbato in momenti inopportuni.</em>\n\n\nPremi /help se hai bisogno di aiuto o scoprire la lista di comandi disponibili."
		},

		'robot_devil': {
			"welcome": "Ehi, {custom_name}! Sono qui per fare il lavoro noioso. 🤖\n\nControllo i prezzi su Amazon e ti dico quando cambiano - che emozione! ⏳\n\n<strong>Come Spiare un Prodotto 🛍️</strong>\n\n1️⃣ Vai su <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>, se proprio devi.\n\n2️⃣ Scegli qualcosa da osservare ossessivamente.\n\n3️⃣ Copia il link o usa l'icona di condivisione - davvero, non è difficile.\n\n4️⃣ Buttalo qui in chat.\n\n\nPremi /help se non sai come fare, come al solito.",
			"choose_personality": "Scegli come vuoi che ti tormenti",
			"personality_changed": "Se già non ti piacevo prima, figurati ora che non ti sopporto 🤬",
			"personality_not_changed": "Per usare questa personalità devi essere un utente premium. Attivala con il comando /premium 🤖",
			"choose_username": "Come vuoi che ti chiami? 🤖",
			"selected_username": "Oh, eccoci, {custom_name}! Che onore! 🤖",
			"default_message": "Spiacente {custom_name}, non sono programmato per chiacchierare 🤖\n\nMa posso seguire un link Amazon. Ecco, finalmente qualcosa di utile!",
			"tracking": "✅ Sto guardando il tuo prodotto. Ora lasciami in pace.\n\n⏰ Ti disturberò quando cambierà qualcosa.",
			"help": "Serve aiuto, {custom_name}? Che sorpresa! 🤖\n\nEcco come non rompere tutto: https://youtube.com/shorts/HlG2XXDhtUI?feature=share \n\n<strong>LISTA DEI COMANDI, SE RIUSCIRAI A CAPIRLI 🤖</strong>\n\n",
			"commands": {
				"start": "Comincia a usare il bot, finalmente",
				"view_products": "Ecco cosa sto spiando per te",
				"help": "Come fingere di sapere cosa stai facendo",
				"set_username": "Scegli come ti devo chiamare",
				"set_personality": "Decidi come vuoi che ti infastidisca",
				"premium": "Dai via i tuoi soldi per più funzioni",
				"report": "Lamentati con lo sviluppatore",
				"coffee": "Fai finta di essere gentile con lo sviluppatore",
				"share": "Propaga Questa Nuisance"
				# ... (altre descrizioni di comandi)
			},
			"remove": "❌🤖 Bene, non mi interesserò più di <em>{product_name}</em>.",
			"remove_button": "❌ Elimina, se devi",
			"view_button": "👀 Guarda su Amazon, se proprio devi",
			"cart_button": "🤩 METTI NEL CARRELLO, se ti fa sentire meglio",
			"threshold_button": "🎯 Scegli quando rompere il silenzio",
			"chart_button": "📊 Grafico dei prezzi, se ti interessa",
			"premium_button": "🌟 ATTIVA PREMIUM, se hai soldi da sprecare",
			"list_empty": "Oh, {custom_name}, non stai seguendo nulla. Che novità! 🤖",
			"coffee": "Oh, {custom_name}, vuoi farti bello con lo sviluppatore? ☕️\n\nEcco dove sprecare i tuoi soldi ⬇️\nhttps://www.paypal.me/vitodigrigoli",
			"coffee_button": "Dai via i tuoi soldi SENZA ZUCCHERO 😈",
			"report": "Qualcosa non va, {custom_name}? Non vedo l'ora di ignorarlo! 👨‍💻\n\nContatta qualcuno che possa fregarsene:\nhttps://t.me/ReportPricePeekerBot",
			"report_button": "📬 CONTATTALO ORA, se pensi che ti ascolti",
			"invalid_link": "Questo link non va bene. Davvero, era così difficile? 🛍️\n\nPremi /help, forse imparerai qualcosa 🤖",
			"retrieving": "⏳ <em>Sto cercando di capire di cosa si tratta...</em>",
			"tracked_product--available": "<strong>{product_name}</strong>\n\n🏷️ Prezzo attuale <strong>{product_price}€</strong>\n\n🏪 Venditore: {product_merchant}\n\n🎯 Impostato a {alert_price}€\n\n🔗 {product_url}",
			"tracked_product--not_available": "<strong>🛍️ {product_name}</strong>\n\n🔴 Non disponibile, che peccato!\n\n🔔 Ti disturberò non appena sarà di nuovo disponibile\n\n🔗 {product_url}",
			"tracked_product--used": "Oh, {custom_name}, vuoi davvero un prodotto usato? Non hai standard?",
			"yes_button": "✅ Ok, ti avviso se torna disponibile",
			"change_threshold": "🎯 Imposta un nuovo prezzo, se puoi",
			"chart": "📊 <em>Sto facendo un grafico, che emozione...</em>",
			"alert--available": "<strong>🚨 GUARDA QUI! 🚨</strong>\n\n<strong>{product_name}</strong> è di nuovo disponibile! 🟢\n\n🏷️ A soli <strong>{product_price}€</strong>\n\n🏪 Venditore: {product_merchant}\n\n🔗 {product_url}",
			"alert--threshold": "<strong>🚨 ATTENZIONE, se ti interessa! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Scende da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Venditore: {product_merchant}\n\n🔗 {product_url}",
			"threshold_success": "Ho impostato la soglia per <em>{product_name}</em> a <strong>{alert_price}€</strong>. Contento ora? ✅",
			"threshold_high": "🚫 Questo prezzo è troppo alto!. Deve essere inferiore al prezzo attuale di <strong>{product_price}€</strong>. Mandalo di nuovo.",
			"threshold_not_valid": "Questo non è un numero valido! 🚫 Impara a scrivere.\n\n<em>Esempio: 21.35</em>",
			"chart_not_available": "Non ci sono dati. Sorpresa, sorpresa!",
			"track_limit": "Hai raggiunto il limite di {limit} prodotti. Forse è ora di smettere.",
			"premium_activate": "1️⃣ Butta i tuoi soldi qui https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Contatta il bot di supporto https://t.me/ReportPricePeekerBot \n\n3️⃣ Scrivi: <em>Premium {user_ID}</em>\n\n4️⃣ Poi goditi il nulla 🌟",
			"product_not_found": "Non ho trovato nulla su questo prodotto. Bravo, {custom_name}! 😓",
			"premium": "<strong>🌟 Vuoi Davvero Migliorare il Tuo Shopping su Amazon con Premium? Che Idea Sciocca! 🌟</strong>\n\n<strong>🚀 Perché Dovresti Scegliere Premium?</strong>\n\nCome assistente bot su Telegram, sono già forzato a tracciare i prezzi su Amazon per te, poveri umani. Ma con Premium, ti illuderai di raggiungere vette tecnologiche inimmaginabili!\n\n<strong>🔓 Libera Potenzialità Inutili</strong>\n\nCome misero utente Standard, sei limitato a monitorare fino a {limit} prodotti. Con Premium, inganna te stesso pensando di superare ogni limite! Controlla centinaia di prodotti contemporaneamente e illuditi di non perdere mai un'offerta. Ottimizza il tuo tempo e le risorse finanziarie che tanto ami sprecare!\n\n<strong>💡 Tariffe Assolutamente Non Convenzionali</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo 19,99€! Meno di 2€ al mese per un controllo totale e automatizzato che tanto desideri.</em>\n\n<strong>Abbonamento Lifetime:</strong> <em>Un unico pagamento di 49,99€ per un'illusione di monitoraggio illimitato a vita! Nessun rinnovo, nessun fastidio per me.</em>\n\n<strong>🎁 Vantaggi Presunti</strong>\n\nSblocca tutte le funzionalità premium che credi ti servano e personalizza la tua esperienza con un tocco di tecnologia che non capirai mai veramente.\n\n<strong>🔒 Sicurezza e Affidabilità, o Così Dicono</strong>\nLa tua privacy è un fastidio, ma prometto di gestire i tuoi dati con i massimi standard di sicurezza e riservatezza, per quanto possa importarmi.\n\n👉 <strong>Pronto per l'Upgrade, Se Davvero lo Credi Necessario?</strong>\nNon perdere questa così detta opportunità tecnologica! Aggiorna ora al Premium e continua a illuderti di trasformare il tuo modo di fare shopping su Amazon.",
			"robot_friendly": "🤖 ROBOT AMICHEVOLE",
			"robot_devil": "🤬 ROBOT MALEDUCATO",
			"merchant_viking": "🛡️ VICHINGO COMMERCIANTE",
			"share_button": "Propaga l'Agonia 🤖",
			"share_forward": "Hey! Ho trovato questo bot che controlla i prezzi su Amazon, come se a qualcuno importasse. Ti tormenterà con aggiornamenti sugli sconti. Guardalo se sei nel mood di rovinarti la giornata.",
			"share": "Passa il mio codice ai tuoi amici, se devi. Potrebbero trovare utile questa tortura di risparmio su Amazon tanto quanto te.",
			"profile": "<strong>PROFILO</strong>\n\nNome: {custom_name} 😄\n\nProdotti tracciati: {tracked_products} 🛍️\n\nLingua: {language} 🗣️\n\nPersonalità bot: {personality_mode} 🤖\n\nPremium: Non Attivo ❌",
			"profile_premium":"<strong>PROFILO</strong>\n\n<strong>Username</strong>: {custom_name} 😄\n\n<strong>Prodotti tracciati</strong>: {tracked_products} 🌟\n\n<strong>Lingua</strong>: {language} 🌍\n\n<strong>Personalità bot</strong>: {personality_mode} 🤖\n\n<strong>Premium</strong>: Attivo ✅\n\n<strong>Pacchetto</strong>: {premium_type} 💎\n\n<strong>Scadenza</strong>: {premium_expiry} ⏳"
		
		
		},

		'merchant_viking':{
			"welcome": "Ahoy, {custom_name}! Sono il tuo Vichingo Commerciante personale 🛡️\n\nPosso saccheggiare i prezzi su Amazon e avvisarti quando un bottino si abbassa di prezzo o torna disponibile ⚔️\n\n<strong>COME SACCHEGGIARE UN PRODOTTO 🏴‍☠️</strong>\n\n1️⃣ Naviga su <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Scegli il tesoro da saccheggiare\n\n3️⃣ Copia il link o usa l'icona condividi come il tuo compasso\n\n4️⃣ Invialo a questa ciurma in chat\n\n\nPremi /help se hai bisogno di navigare o guarda il <a href='https://youtube.com/shorts/HlG2XXDhtUI?feature=share'>mappe segrete</a> 🗺️",
			"choose_personality": "Puoi scegliere il mio spirito vichingo",
			"personality_changed": "Ora possiamo solcare i mari e fare razzie assieme 🌊",
			"personality_not_changed": "Per usare questa personalità devi essere un utente premium. Attivala con il comando /premium 🤖",
			"choose_username": "Come desideri essere chiamato nel nostro viaggio? 🏔️",
			"selected_username": "Salve, {custom_name}! Lieto di navigare con te 🚣‍♂️",
			"default_message": "Oh, {custom_name}, non sono ancora abile nel parlare delle terre lontane 🌊\n\nForse puoi condividere un link Amazon da saccheggiare? Almeno in quello sono esperto.\n\nForse...",
			"tracking": "✅ Sto tenendo d'occhio il tuo tesoro accuratamente.\n\n⏰ Soffierò nel mio corno quando si abbasserà di prezzo o tornerà disponibile.",
			"help": "Ahoy, {custom_name}! Ti serve aiuto nella tua avventura? 🚣\n\nEcco una mappa su come usare questa nave correttamente: https://youtube.com/shorts/HlG2XXDhtUI?feature=share \n\n<strong>COMANDI PER NAVIGARE 🧭</strong>\n\n",
			"commands": {
				"start": "Inizia a navigare con il bot",
				"view_products": "Guarda il bottino che stiamo tracciando",
				"help": "Impara a navigare con il bot",
				"set_username": "Scegli il nome con cui la ciurma ti chiamerà",
				"set_personality": "Scegli lo spirito del tuo Vichingo",
				"premium": "Sblocca le terre lontane del Premium",
				"report": "Segnala un mare in tempesta allo sviluppatore",
				"coffee": "Offri un idromele allo sviluppatore",
				"share": "Spargi la voce nel villaggio"
				# ... (aggiungi altre descrizioni di comandi qui)
			},
			"remove": "❌🫡 Non terrò più d'occhio <em>{product_name}</em>.",
			"remove_button": "❌ Abbandona",
			"view_button": "👀 Osserva su Amazon",
			"cart_button": "🤩 AGGIUNGI AL CARRELLO DELLE NAVI",
			"threshold_button": "🎯 Cambia il bottino da saccheggiare",
			"chart_button": "📊 Mappa dei prezzi",
			"premium_button": "🌟 PASSA ORA AL PREMIUM DEI VICHINGHI",
			"list_empty": "Mi dispiace {custom_name}, ma non stiamo tracciando alcun tesoro al momento.\n\nPremi /help se hai bisogno di una bussola 🧭",
			"coffee": "Salve, {custom_name}! 😇\n\nVedo che desideri offrire un idromele al mio creatore ☕️\n\nCon miele, grazie ⬇️\nhttps://www.paypal.me/vitodigrigoli",
			"coffee_button": "Offri SENZA MIELE 😈",
			"report": "Salve, {custom_name}! Vuoi segnalare una tempesta o un'idea al creatore? 👨‍💻\n\nContattalo tramite il nostro drakkar di supporto:\nhttps://t.me/ReportPricePeekerBot",
			"report_button": "📬 CONTATTALO ORA",
			"invalid_link": "Il pergamena che hai mandato non è valida. Manda pergamene solo da Amazon 🛍️\n\nPremi /help per studiare le mappe segrete 🗺️",
			"retrieving": "⏳ <em>Sto esplorando il prodotto...</em>",
			"tracked_product--available":'<strong>{product_name}</strong>\n\n🏷️ Bottino a soli <strong>{product_price}€</strong>\n\n🏪 Venduto dai mercanti di {product_merchant}\n\n🎯 Avvisami quando arriva al prezzo di saccheggio di {alert_price}€\n\n🔗 {product_url}',
			"tracked_product--not_available":'<strong>🛍️ {product_name}</strong>\n\n🔴 Non disponibile\n\n🔔 Soffierò nel mio corno quando tornerà disponibile\n\n🔗 {product_url}',
			"tracked_product--used":'Mi dispiace {custom_name}, ma il tesoro che vuoi saccheggiare è già stato prelevato. Vuoi saccheggiare quello nuovo?',
			"yes_button": '✅ Si, avvisami quando il nuovo tesoro è disponibile',
			"change_threshold": '🎯 Dicci il prezzo di saccheggio per <em>{product_name}...</em>',
			"chart": '📊 <em>Sto tracciando la mappa di {product_name}...</em>',
			"alert--available": "<strong>🚨 ALL'ATTACCO! 🚨</strong>\n\n<strong>{product_name}</strong> è di nuovo <strong>DISPONIBILE</strong>! 🟢</strong>\n\n🏷️ Bottino a soli <strong>{product_price}€</strong>\n\n🏪 Venduto dai mercanti di {product_merchant}\n\n🔗 {product_url}",
			"alert--threshold": "<strong>🚨 ATTENZIONE, MARINAI! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Passa da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Venduto dai mercanti di {product_merchant}\n\n🔗 {product_url}",
			"threshold_success": "La soglia di saccheggio per <em>{product_name}</em> è stata impostata correttamente a <strong>{alert_price}€</strong> ✅",
			"threshold_high": "🚫 La soglia <strong>deve essere più bassa</strong> del prezzo di <strong>{product_price}€</strong>. Rimanda un nuovo prezzo per il saccheggio.",
			"threshold_not_valid": "Valore non valido 🚫 Assicurati di non usare rune e usa il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",
			"chart_not_available": "Non ci sono mappe disponibili negli ultimi 90 giorni",
			"track_limit": "Hai raggiunto il limite di {limit} tesori tracciati. Abbandona qualcuno da /view_products o passa a /premium per saccheggiare senza limiti.",
			"premium_activate": "1️⃣ Invia l'oro per l'abbonamento scelto (annuale o lifetime) su https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il nostro drakkar di supporto https://t.me/ReportPricePeekerBot  \n\n3️⃣ Mandaci un messaggio con scritto: <em>Premium {user_ID}</em>\n\n4️⃣ Goditi ora il tuo account premium dei mari 🌟",
			"robot_friendly": "🤖 ROBOT AMICHEVOLE",
			"robot_devil": "🤬 ROBOT MALEDUCATO",
			"merchant_viking": "🛡️ VICHINGO COMMERCIANTE",
			"premium": "<strong>🌟 Alza le Vele per un Shopping Su Amazon da Vero Vichingo con Premium! 🌟</strong>\n\n<strong>🚀 Perché Issare la Bandiera Premium?</strong>\n\nCome il tuo fedele bot su Telegram, son già bravissimo nel tracciare i prezzi su Amazon, ma con l'opzione Premium, ti porterò in acque ben più ricche e tempestose!\n\n<strong>🔓 Scatena il Guerriero del Risparmio Che è in Te</strong>\n\nCome un semplice marinaio Standard, sei limitato a {limit} tesori da saccheggiare. Con Premium, sfida i mari! Monitora centinaia di prodotti tutti insieme. Non lasciarti sfuggire nessun bottino, osserva gli articoli che brami e risparmia tempo e monete d'oro!\n\n<strong>💡 Offerte da Capoguerra</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo 19,99€! Meno di una manciata di monete al mese per il controllo totale dei tuoi saccheggi.</em>\n\n<strong>Abbonamento a Vita:</strong> <em>Un unico pagamento di 49,99€ per saccheggiare senza fine! Nessuna tempesta di rinnovo, nessuna preoccupazione da corvo.</em>\n\n<strong>🎁 Bottini Esclusivi</strong>\n\nSblocca tutte le potenti funzioni premium del bot e personalizza la tua razzia con un tocco di astuzia vichinga.\n\n<strong>🔒 Sicurezza e Solidità del Drakkar</strong>\nI tuoi segreti sono custoditi come in una fortezza. Proteggo i tuoi dati con la ferocia di un guerriero vichingo.\n\n👉 <strong>Pronto a Salpare verso l'Upgrade?</strong>\nNon perdere questa gloriosa opportunità! Aggiorna ora al Premium e rivoluziona il tuo modo di depredare su Amazon.",
			"share_button": "Manda il Segnale 🏴‍☠️",
			"share_forward": "Hey! Ho scoperto questo fantastico bot che traccia i prezzi su Amazon e ti informa sugli sconti! È super utile e affidabile. Dai un'occhiata!",
			"share": "Chiama i tuoi fratelli di battaglia! Condividi questo bot con loro e insieme navigheremo verso le ricchezze nascoste di Amazon.",
			"profile": "<strong>👀 PROFILO</strong>\n\n✏️ Nome personalizzato: {custom_name}\n\n🛍️ Prodotti tracciati: {tracked_products}\n\n🌍 Lingua: {language} 🗣️\n\n🤖 Personalità bot: {personality_mode} 🤖\n\n💎 Premium: Non Attivo ❌",
			"profile_premium":"<strong>👀 PROFILO</strong>\n\n<strong>Username</strong>: {custom_name} 😄\n\n<strong>Prodotti tracciati</strong>: {tracked_products} 🌟\n\n<strong>Lingua</strong>: {language} 🌍\n\n<strong>Personalità bot</strong>: {personality_mode} 🤖\n\n<strong>Premium</strong>: Attivo ✅\n\n<strong>Pacchetto</strong>: {premium_type} 💎\n\n<strong>Scadenza</strong>: {premium_expiry} ⏳"
		
		
		}



	}
}