responses = {
	'it': {
		'robot_friendly':{

			"welcome": "Saluti, {custom_name}! Io sono il tuo assistente bot personale 🤖\n\nPosso monitorare i prodotti su Amazon e informarti sui loro abbassamenti di prezzo o sulla loro disponibilità ⏳\n\n<strong>COME MONITORARE UN PRODOTTO 🛍️</strong>\n\n1️⃣ Visita <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Seleziona il prodotto che ti interessa\n\n3️⃣ Copia il link o usa l'icona di condivisione\n\n4️⃣ Inviamelo in questa chat\n\n\nPremi /help se hai bisogno di aiuto o se vuoi scoprire la lista dei comandi disponibili.",
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
				"help": "Impara a utilizzare il bot",
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

			"tracked_product--available": "<strong>{product_name}</strong>\n\n🏷️ Prezzo attuale <strong>{product_price}€</strong>\n\n🏪 Venduto da <em>{product_merchant}</em>\n\n🎯 Notifica impostata a {alert_price}€\n\n🔗 {product_url}",
			"tracked_product--not_available": "<strong>{product_name}</strong>\n\n🔴 Attualmente non disponibile\n\n🔔 Ti informerò non appena tornerà disponibile\n\n🔗 {product_url}",
			"tracked_product--used": "Mi dispiace {custom_name} 😔 ma il prodotto che hai inviato sembra essere usato, e purtroppo non posso tracciarne il prezzo in modo affidabile.\n\nI prezzi dei prodotti usati possono variare molto a seconda delle loro condizioni, e non vorrei confonderti con notifiche imprecise.\n\nMa hey, ho un'idea! 🌟 Che ne dici di tracciare lo stesso prodotto, ma nella versione nuova? 🆕\n\nCosì posso fornirti aggiornamenti accurati e tempestivi sui prezzi! Fammi sapere se ti va, sarò più che felice di aiutarti. 🤓✨",
			
			"yes_button": "✅ Si, traccia il nuovo",

			"alert--available": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong> è ora <strong>DISPONIBILE</strong>! 🟢\n\n🏷️ Prezzo attuale <strong>{product_price}€</strong>\n\n🏪 Venduto da {product_merchant}\n\n🔗 {product_url}",
			"alert--threshold": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Prezzo ridotto da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Venduto da {product_merchant}\n\n🔗 {product_url}",
			
			"change_threshold": "🎯 Scrivi il prezzo di notifica per <em>{product_name}</em>",
			"threshold_success": "La soglia per <em>{product_name}</em> è stata impostata correttamente a <strong>{alert_price}€</strong> ✅",
			"threshold_high": "🚫 La soglia deve essere inferiore al prezzo attuale di <strong>{product_price}€</strong>. Inserisci un nuovo prezzo.",
			"threshold_not_valid": "Valore non valido 🚫. Usa solo numeri e il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",
			
			"premium": "<strong>🌟 ELEVA IL TUO SHOPPING SU AMAZON CON PREMIUM! 🌟</strong>\n\n\n<strong>🚀 Perché Scegliere Premium?</strong>\n\nCome assistente bot su Telegram, offro già un'eccellente esperienza nel tracciare i prezzi su Amazon, ma con l'opzione Premium, la tua esperienza di shopping raggiungerà nuove vette tecnologiche!\n\n\n<strong>🔓 Sblocca Potenzialità Illimitate</strong>\n\nIn qualità di utente Standard, puoi monitorare fino a {free_limit} prodotti. Con Premium, supera ogni limite! Monitora <strong>fino a {premium_limit} prodotti</strong> contemporaneamente.\n\nNon perdere mai un'offerta, tieni d'occhio gli articoli che desideri e ottimizza il tuo tempo e le tue risorse finanziarie!\n\n\n<strong>💡 Tariffe Convenzionali</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo {annual_price}€! Meno di 2€ al mese per un controllo totale e automatizzato dei prezzi.</em>\n\n<strong>Abbonamento Lifetime:</strong> <em>Un unico pagamento di {lifetime_price}€ per un monitoraggio illimitato a vita! Nessun rinnovo, nessuna complicazione.</em>\n\n\n<strong>🎁 Vantaggi Esclusivi</strong>\n\nSblocca tutte le mie funzionalità premium come le nuove personalità e personalizza la tua esperienza con un tocco di tecnologia avanzata.\n\n\n<strong>🔒 Sicurezza e Affidabilità</strong>\n\nLa tua privacy è una mia priorità fondamentale. Gestisco i tuoi dati con i massimi standard di sicurezza e riservatezza.\n\n\n👉 <strong>Pronto per l'Upgrade?</strong>\n\nNon perdere questa opportunità tecnologica! Aggiorna ora al Premium e trasforma il tuo modo di fare shopping su Amazon.",
			"premium_activate": "<strong>COME ATTIVARE LA VERSIONE PREMIUM </strong>\n\n1️⃣ Invia l'importo dell'abbonamento scelto (annuale o lifetime) a https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il nostro bot di supporto https://t.me/ReportPricePeekerBot \n\n3️⃣ Invia un messaggio con scritto: <em>Premium {user_ID}</em>\n\n4️⃣ Goditi il tuo account premium 🌟",
			"premium_activated": "👋 <strong>CONGRATULAZIONI!</strong> 🌟\n\n Hai effettuato l'upgrade a PREMIUM. 🎉\n\nOra puoi accedere a tutto ciò che è extra-speciale! 🚀 Per dare un'occhiata ai dettagli del tuo abbonamento, usa il comando /profile",

			"share": "Sto monitorando attentamente i prezzi su Amazon per te. Anche se sono solo un bot, mi preoccupo del tuo risparmio!\n\nCondividi questo bot con altri e aiutali a risparmiare anche loro.\n\nInsieme possiamo fare la differenza! ❤️",
			"share_forward": "Hey! Ho scoperto questo fantastico bot che traccia i prezzi su Amazon e ti informa sugli sconti! È super utile e affidabile. Dai un'occhiata!",
			"share_button": "🤖 INVITA GLI AMICI",
			
			"profile": "<strong>👀 INFOMAZIONI PROFILO</strong>\n\n<strong>✏️ Nome personalizzato</strong>: {custom_name}\n\n<strong>🛍️ Prodotti tracciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Personalità bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Non Attivo ❌",
			"profile_premium":"<strong>INFOMAZIONI PROFILO</strong>\n\n<strong>✏️ Nome personalizzato</strong>: {custom_name}\n\n<strong>🛍️ Prodotti tracciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Personalità bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Attivo ✅\n\n<strong>🎁 Pacchetto</strong>: {premium_type}\n\n<strong>⏳ Scadenza</strong>: {premium_expiry}",
		
			"remove_button": "❌ Rimuovi",
			"view_button": "🤩 COMPRA SU AMAZON ORA!",
			"cart_button": "🤩 AGGIUNGI AL CARRELLO AMAZON ORA",
			"threshold_button": "🎯 Cambia Prezzo di Notifica",
			"chart_button": "📊 Grafico Prezzi",
			"premium_button": "💎 ATTIVA PREMIUM ORA",

			"robot_friendly": "🤖 ROBOT AMICHEVOLE",
			"dark_wizard": "🧙‍♂️ MAGO OSCURO (💎)",
			"merchant_viking": "🛡️ VICHINGO COMMERCIANTE",

			"version": "<strong>🌟 Changelog Versione 2.0 del Bot 🌟</strong>\n\n🔷 <strong>Possibilità di Scegliere il Prezzo di Notifica per il Prodotto:</strong> <em>Decidi tu a quale prezzo vuoi essere avvisato! 🔔 Scegli la soglia che preferisci per ogni prodotto tracciato.</em>\n\n🔷 <strong>Grafico con lo Storico dei Prezzi del Prodotto:</strong> <em>Ora puoi visualizzare la cronologia dei prezzi per ogni prodotto! 📈 Un modo efficace per capire le tendenze e fare acquisti intelligenti.</em>\n\n🔷 <strong>Messaggi Personalizzati in Base alla Personalità del Bot:</strong> <em>Il bot ora ha diverse personalità! 🤖 Scegli quella che preferisci per una comunicazione su misura.</em>\n\n🔷 <strong>Abbonamenti Premium:</strong> <em>Accedi a funzioni esclusive con il nostro abbonamento premium! 🌐 Più potere nelle tue mani per un'esperienza di shopping ancora migliore.</em>\n\n🔷 <strong>Controllo dei Prezzi ad Orario Fisso 10:00 e 17:00 per Non Disturbare l'Utente:</strong> <em>I controlli dei prezzi avvengono ora a orari fissi 🕙🕔 per assicurarti di non essere disturbato in momenti inopportuni.</em>\n\n\nPremi /help se hai bisogno di aiuto o se vuoi scoprire la lista dei comandi disponibili."
		},

		'dark_wizard': {

			"welcome": "Ah, {custom_name}, benvenuto nel mio dominio oscuro. Io sono il tuo araldo delle ombre, il custode dei segreti su Amazon 🧙‍♂️.\n\nCon il mio occhio che tutto vede, monitorerò i prodotti e ti svelerò i loro mutamenti di prezzo o la loro emersione dalle tenebre ⏳.\n\n<strong>COME SCOVARE UN ARTEFATTO 🛍️</strong>\n\n1️⃣ Vaga per le cripte di <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Seleziona l'artefatto da procacciare\n\n3️⃣ Cattura il link come un segreto oscuro\n\n4️⃣ Inviamelo attraverso i canali oscuri di questa chat\n\n\nInvoca /help se hai bisogno di assistenza nelle arti oscure o per scoprire l'arsenale di poteri a tua disposizione.",
			"default_message": "Ah, {custom_name}, la mia maestria nelle conversazioni è limitata come il confine tra luce e oscurità 🧙‍♂️. Potresti condividere un link di Amazon da scrutare? Questo è un potere che posseggo!\n\nForse...",
			"invalid_link": "Il link che hai inviato è un enigma, privo di verità. Per favore, invia soltanto i segnali provenienti dal regno di Amazon 🛍️\n\nInvoca /help per un'illuminazione 🪄",
			"product_not_found": "Ah, {custom_name}, anche con le mie arti oscure non ho scorto tracce di questo artefatto su Amazon, eludendo così il mio sguardo. Mi dispiace 😓",
			
			"choose_personality": "Scegli l'essenza della mia ombra",
			"personality_changed": "Che la mia nuova forma oscura ti sia di gradimento 🧙‍♂️",
			"personality_not_changed": "Per abbracciare questa essenza oscura, devi attraversare il portale del premium. Attivalo con il comando /premium 🧙‍♂️",
			
			"choose_username": "Quale nome vuoi che risuoni nelle ombre? 🧙‍♂️",
			"selected_username": "Saluti, {custom_name}. Un onore incontrarti nel cuore delle tenebre 🧙‍♂️",

			"help": "Ah, {custom_name}, desideri esplorare i segreti nascosti? 🧙‍♂️\n\nEcco una pergamena oscura che rivela il modo per utilizzarmi: https://youtube.com/shorts/HlG2XXDhtUI?feature=share \n\n<strong>GLIFI DEL POTERE 📜</strong>\n\n",
			"commands": {
				"start": "Inizia il tuo viaggio nelle ombre",
				"view_products": "Evoca gli artefatti che hai catturato",
				"help": "Scopri come manipolare il tuo servitore oscuro",
				"set_username": "Scegli il nome con cui sarai invocato dalle tenebre",
				"set_personality": "Scegli l'aspetto del tuo famiglio",
				"premium": "Evoca i poteri nascosti della versione premium",
				"report": "Segnala una distorsione nella magia allo stregone supremo",
				"coffee": "Offri un tributo al creatore del tuo araldo oscuro",
				"share": "Diffondi la magia oscura tra i tuoi compagni",
				"profile": "Guarda nel tuo specchio riflettente",
				"version": "Svela gli ultimi incantesimi intessuti"
				# ... (altre descrizioni di comandi)
			},

			"remove": "❌🧙‍♂️ Abbandonerò la sorveglianza di <em>{product_name}</em>.",
			"list_empty": "Ah, {custom_name}, sembra che tu non stia monitorando alcun artefatto. Invoca /help per una guida 🧙‍♂️",
			
			"coffee": "Oh, {custom_name}! 😇\n\nDesideri offrire un elisir al mio creatore? ☕️\n\nCon essenza dolce, per favore ⬇️\nhttps://www.paypal.me/vitodigrigoli",
			"coffee_button": "Offri un Elisir Puro 😈",
			
			"report": "Salve, {custom_name}! Vuoi inviare un messaggio criptato allo stregone supremo? 👨‍💻\n\nContattalo tramite il famiglio dei messaggi:\nhttps://t.me/ReportPricePeekerBot",
			"report_button": "📬 INVIA IL TUO MESSAGGIO ORA",

			"retrieving": "⏳ <em>Sto evocando dal nulla le informazioni sull'artefatto...</em>",
			"track_limit": "Hai raggiunto il limite di {limit} artefatti procacciati. Elimina qualcuno dai tuoi incantesimi con /view_products o attraversa il portale oscuro di /premium per osservare senza confini.",

			"chart": "📊 <em>Sto disegnando con la magia oscura il grafico di {product_name}...</em>",
			"chart_not_available": "Nelle oscure nebbie degli ultimi 90 giorni, non si celano dati da rivelare",

			"tracked_product--available": "<strong>{product_name}</strong>\n\n🏷️ Il tributo in oro è <strong>{product_price}€</strong>\n\n🏪 Procacciato da <em>{product_merchant}</em>\n\n🎯 Ho fissato il mio incantesimo di allerta a {alert_price}€\n\n🔗 {product_url}",
			"tracked_product--not_available": "<strong>{product_name}</strong>\n\n🔴 Si cela nelle ombre, attualmente irraggiungibile\n\n🔔 Ti informerò non appena emergerà dalle tenebre\n\n🔗 {product_url}",
			"tracked_product--used": "Ah, {custom_name} 😔 l'artefatto che hai scovato è già stato toccato da altre mani, e le sue vibrazioni sono incerte. I prezzi dei beni usati sono come fumi che cambiano forma.\n\nMa attento! 🌟 Che ne dici di inseguire lo stesso oggetto, ma nella sua forma pura e originale? 🆕\n\nCosì, potrò guidarti con precisione tra le nebbie dei prezzi! Fammi sapere se desideri questo sentiero oscuro. 🤓✨",
			"yes_button": "✅ Sì, scova il nuovo",
			
			"alert--available": "<strong>🚨 ALLARME! 🚨</strong>\n\n<strong>{product_name}</strong> è ora <strong>DISPONIBILE</strong>! 🟢\n\n🏷️ Il tributo in oro è <strong>{product_price}€</strong>\n\n🏪 Procacciato da <em>{product_merchant}</em>\n\n🔗 {product_url}",
			"alert--threshold": "<strong>🚨 ALLARME! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Il tributo in oro è sceso da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Procacciato da <em>{product_merchant}</em>\n\n🔗 {product_url}",
			
			"change_threshold": "🎯 Scrivi la soglia di allarme incantesimo per <em>{product_name}</em>",
			"threshold_success": "Ho impostato con successo la soglia per <em>{product_name}</em> a <strong>{alert_price}€</strong> ✅",
			"threshold_high": "🚫 La soglia deve essere sotto il tributo oro di <strong>{product_price}€</strong>. Scegli una nuova soglia di allarme incantesimo.",
			"threshold_not_valid": "Valore non valido 🚫. Usa solo numeri e il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",

			"premium": "<strong>🌟 TRASFORMA IL TUO SHOPPING SU AMAZON CON IL POTERE DI PREMIUM! 🌟</strong>\n\n\n<strong>🚀 Perché Invocare Premium?</strong>\n\nCome tuo araldo oscuro su Telegram, già ti conduco attraverso i sentieri nascosti dei prezzi su Amazon, ma con l'antica formula di Premium, eleverai la tua esperienza di shopping a nuovi piani di potere!\n\n\n<strong>🔓 Svela Potenzialità Senza Limiti</strong>\n\nCome mortale Standard, puoi osservare fino a {free_limit} artefatti. Con il sigillo di Premium, infrangi ogni barriera! Sorveglia <strong>fino a {premium_limit} artefatti</strong> simultaneamente.\n\nNon lasciarti sfuggire nemmeno un'offerta, tieni sotto controllo ciò che brami e ottimizza il tuo tempo e le tue risorse!\n\n\n<strong>💡 Tariffe Arcane</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo {annual_price}€! Meno di 2€ al mese per un dominio totale sui prezzi.</em>\n\n<strong>Abbonamento Eterno:</strong> <em>Un unico tributo di {lifetime_price}€ per un monitoraggio senza fine! Nessuna rinascita, nessuna catena.</em>\n\n\n<strong>🎁 Privilegi Arcani</strong>\n\nSblocca tutte le mie arti segrete premium, incluse nuove personalità arcane, e plasma la tua esperienza con un tocco di magia nera.\n\n\n<strong>🔒 Sicurezza e Segretezza</strong>\n\nLa tua privacy è un sigillo che custodisco gelosamente. Proteggo i tuoi dati con gli incantesimi più potenti e oscuri.\n\n\n👉 <strong>Pronto per l'Ascensione?</strong>\n\nNon perdere questa occasione di potere arcano! Trasfigurati ora in Premium e trasmuta il tuo modo di fare shopping su Amazon.",
			"premium_activate": "<strong>COME EVOCARE LA VERSIONE PREMIUM </strong>\n\n1️⃣ Offri il tributo per l'abbonamento scelto (annuale o eterno) a https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il portale del nostro bot di supporto https://t.me/ReportPricePeekerBot \n\n3️⃣ Invoca con un messaggio: <em>Premium {user_ID}</em>\n\n4️⃣ Assapora il tuo status di Premium 🌟",
			"premium_activated": "👋 <strong>CONGRATULAZIONI!</strong> 🌟\n\n Sei ora trasfigurato in PREMIUM. 🎉\n\nAccedi a ciò che è nascosto e proibito! 🚀 Per scrutare i segreti del tuo abbonamento, usa il comando /profile",

			"share": "Sto scrutando con occhi da corvo i prezzi su Amazon per te. Anche se sono solo un'entità digitale, veglio sul tuo risparmio come un guardiano oscuro!\n\nDiffondi il potere di questo bot tra gli altri e aiutali a scoprire i segreti del risparmio.\n\nInsieme, possiamo tessere una rete di potere e risparmio! ❤️",
			"share_forward": "Ehi! Ho incrociato il cammino di questo magnifico bot che traccia i prezzi su Amazon e ti svela gli sconti! È un alleato utile e fedele nel regno del commercio. Esploralo!",
			"share_button": "🧙‍♂️ INVITA I TUOI ALLEATI",
			
			"profile": "<strong>👀 VISIONI DEL PROFILO OCCULTO</strong>\n\n<strong>✏️ Nome Arcano</strong>: {custom_name}\n\n<strong>🛍️ Artefatti procacciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua degli Antichi</strong>: {language}\n\n<strong>🤖 Essenza del Bot</strong>: {personality_mode}\n\n<strong>💎 Sigillo di Premium</strong>: Non Evocato ❌",
			"profile_premium": "<strong>VISIONI DEL PROFILO OCCULTO</strong>\n\n<strong>✏️ Nome Arcano</strong>: {custom_name}\n\n<strong>🛍️ Artefatti procacciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua degli Antichi</strong>: {language}\n\n<strong>🤖 Essenza del Bot</strong>: {personality_mode}\n\n<strong>💎 Sigillo di Premium</strong>: Evocato ✅\n\n<strong>🎁 Formula</strong>: {premium_type}\n\n<strong>⏳ Ciclo Eterno</strong>: {premium_expiry}",

			"remove_button": "❌ Dissolvi",
			"view_button": "🤩 EVOCA ARTEFATTO SU AMAZON ORA!",
			"cart_button": "🤩 AGGIUNGI AL CARRELLO AMAZON ORA",
			"threshold_button": "🎯 Cambia Incantesimo di Allerta",
			"chart_button": "📊 Mappa Mistica",
			"premium_button": "💎 ATTIVA PREMIUM ORA",

			"robot_friendly": "🤖 ROBOT AMICHEVOLE",
			"dark_wizard": "🧙‍♂️ MAGO OSCURO (💎)",
			"merchant_viking": "🛡️ VICHINGO COMMERCIANTE",

			"version": "<strong>🌟 Changelog Versione 2.0 del Bot 🌟</strong>\n\n🔷 <strong>Possibilità di Scegliere il Prezzo di Notifica per il Prodotto:</strong> <em>Decidi tu a quale prezzo vuoi essere avvisato! 🔔 Scegli la soglia che preferisci per ogni prodotto tracciato.</em>\n\n🔷 <strong>Grafico con lo Storico dei Prezzi del Prodotto:</strong> <em>Ora puoi visualizzare la cronologia dei prezzi per ogni prodotto! 📈 Un modo efficace per capire le tendenze e fare acquisti intelligenti.</em>\n\n🔷 <strong>Messaggi Personalizzati in Base alla Personalità del Bot:</strong> <em>Il bot ora ha diverse personalità! 🤖 Scegli quella che preferisci per una comunicazione su misura.</em>\n\n🔷 <strong>Abbonamenti Premium:</strong> <em>Accedi a funzioni esclusive con il nostro abbonamento premium! 🌐 Più potere nelle tue mani per un'esperienza di shopping ancora migliore.</em>\n\n🔷 <strong>Controllo dei Prezzi ad Orario Fisso 10:00 e 17:00 per Non Disturbare l'Utente:</strong> <em>I controlli dei prezzi avvengono ora a orari fissi 🕙🕔 per assicurarti di non essere disturbato in momenti inopportuni.</em>\n\n\nPremi /help se hai bisogno di aiuto o se vuoi scoprire la lista dei comandi disponibili."
		},

		'merchant_viking':{
			"welcome": "Ahoy, {custom_name}! Sono il tuo scudiero bot, un navigatore dei mari digitali! 🛡️ Veglio sulle terre di Amazon, pronto a segnalarti ogni abbassamento di prezzo o tesoro disponibile ⏳\n\n<strong>PER CATTURARE UN TESORO 🛍️</strong>\n\n1️⃣ Naviga verso <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Scegli il tuo bottino\n\n3️⃣ Cattura il link come un vero vichingo\n\n4️⃣ Inviamelo qui nella mia tana digitale\n\n\nBatti /help sul tuo scudo se cerchi saggezza o vuoi scoprire l'arsenale dei comandi!",
			"default_message": "Odin sia con te, {custom_name}, non eccello nelle chiacchiere ⚔️\n\nPotresti mandare un link di Amazon da saccheggiare? Ecco, questo è il mio campo di battaglia!\n\nForse...",
			"invalid_link": "Il messaggio in bottiglia che hai inviato non conduce a nessun luogo conosciuto. Manda solo segnali da Amazon, guerriero 🛍️\n\nBatti /help sullo scudo per imparare il giusto incantesimo 🤖",
			"product_not_found": "Mi dispiace, {custom_name}. La tua preda è sfuggita anche ai miei occhi di falco. Non ho trovato tracce su Amazon, quindi non posso monitorarlo. Mi dispiace 😓",
			
			"choose_personality": "Scegli il colore del mio vessillo",
			"personality_changed": "Che il nuovo volto di questo vecchio guerriero ti sia gradito ⚔️",
			"personality_not_changed": "Per indossare queste vesti, devi unirti al clan premium. Rivendica il tuo posto con il comando /premium ⚔️",
			
			"choose_username": "Quale nome griderai in battaglia? ⚔️",
			"selected_username": "Salve, {custom_name}! Al tuo servizio, nobile guerriero ⚔️",

			"help": "All'arrembaggio, {custom_name}! Ti serve aiuto, navigatore? 🗺️\n\nEcco una mappa per guidarti: https://youtube.com/shorts/HlG2XXDhtUI?feature=share \n\n<strong>ELENCO DEGLI ARNESI DEL VICHINGO ⚔️</strong>\n\n",
			"commands": {
				"start": "Solleva l'ancora e inizia l'avventura",
				"view_products": "Osserva i tesori che stai tracciando",
				"help": "Istruzioni per navigare le tempeste digitali",
				"set_username": "Scegli il nome con cui sarai acclamato",
				"set_personality": "Scegli il vessillo del tuo bot",
				"premium": "Issa la bandiera premium per maggiori privilegi",
				"report": "Invia un corvo allo sviluppatore per segnalare un bug",
				"coffee": "Offri un calice di idromele allo sviluppatore",
				"share": "Invita altri guerrieri a unirsi alla flotta",
				"profile": "Guarda il ritratto del tuo eroe",
				"version": "Scopri le nuove incisioni sulla tua ascia"
				# ... (altre descrizioni di comandi)
			},

			"remove": "❌🛡️ Non caccierò più <em>{product_name}</em> dai mari.",
			"list_empty": "Ah, {custom_name}, le tue reti sono vuote. Nessun tesoro da tracciare.\n\nBatti /help sullo scudo per chiedere consiglio 🛡️",
			
			"coffee": "Salve, {custom_name}! 😇\n\nVuoi brindare al mio creatore con un boccale di idromele? ☕️\n\nCon miele, per favore ⬇️\nhttps://www.paypal.me/vitodigrigoli",
			"coffee_button": "Offri SENZA MIELE 😈",
			
			"report": "Ciao {custom_name}! Vuoi mandare un corvo con un messaggio allo sviluppatore? 👨‍💻\n\nContattalo tramite il nostro corvo messaggero:\nhttps://t.me/ReportPricePeekerBot",
			"report_button": "📬 MANDA IL CORVO ORA",
			
			"retrieving": "⏳ <em>Sto scandagliando il mare per informazioni sul tesoro...</em>",
			"track_limit": "Hai riempito la tua nave con {limit} tesori tracciati. Scarica qualcosa da /view_products o issa la bandiera /premium per più spazio.",
			
			"chart": "📊 <em>Sto tracciando le stelle per il grafico di {product_name}...</em>",
			"chart_not_available": "Non ci sono segni nei cieli degli ultimi 90 giorni",

			"tracked_product--available": "<strong>{product_name}</strong>\n\n🏷️ Valore bottino <strong>{product_price}€</strong>\n\n🏪 Barattato da <em>{product_merchant}</em>\n\n🎯 Prezzo di saccheggio impostato a {alert_price}€\n\n🔗 {product_url}",
			"tracked_product--not_available": "<strong>{product_name}</strong>\n\n🔴 Attualmente è come un tesoro nascosto\n\n🔔 Ti informerò non appena emergerà dalle nebbie\n\n🔗 {product_url}",
			"tracked_product--used": "Mi dispiace {custom_name} 😔 ma il bottino che hai scovato pare essere di seconda mano, e non posso seguire il suo valore nel mare delle variazioni.\n\nI prezzi dei manufatti usati possono fluttuare come le onde, e non vorrei sbalzarti con notifiche erranti.\n\nMa hey, ho un'idea! 🌟 Che ne dici di tracciare lo stesso prodotto, ma nuovo di zecca? 🆕\n\nCosì posso fornirti aggiornamenti precisi come la rotta di un drakkar! Fammi sapere se ti va, sarò più che felice di aiutarti. 🤓✨",
			"yes_button": "✅ Sì, scova il nuovo",
			
			"alert--available": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong> è ora come un drakkar in vista! 🟢\n\n🏷️ Valore bottino <strong>{product_price}€</strong>\n\n🏪 Barattato da {product_merchant}\n\n🔗 {product_url}",
			"alert--threshold": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Bottino ridotto da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Barattato da {product_merchant}\n\n🔗 {product_url}",
			
			"change_threshold": "🎯 Scrivi il valore di saccheggio per <em>{product_name}</em>",
			"threshold_success": "La soglia di saccheggio per <em>{product_name}</em> è stata impostata correttamente a <strong>{alert_price}€</strong> ✅",
			"threshold_high": "🚫 La soglia di saccheggio deve essere inferiore al valore di bottino attuale di <strong>{product_price}€</strong>. Inserisci un nuovo valore di saccheggio.",
			"threshold_not_valid": "Valore saccheggio non valido 🚫. Usa solo numeri e il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",

			"premium": "<strong>🌟 ELEVA IL TUO SACCHEGGIO SU AMAZON CON PREMIUM! 🌟</strong>\n\n\n<strong>🚀 Perché Scegliere Premium?</strong>\n\nCome guardiano bot dei mari di Telegram, già ti guido tra le onde dei prezzi su Amazon, ma con l'opzione Premium, la tua esperienza diventerà leggendaria!\n\n\n<strong>🔓 Sblocca Potenzialità Illimitate</strong>\n\nCome guerriero Standard, puoi monitorare fino a {free_limit} tesori. Con Premium, non ci sono limiti! Monitora <strong>fino a {premium_limit} tesori</strong> contemporaneamente.\n\nNon lasciarti sfuggire nessun bottino, sorveglia gli articoli che desideri e ottimizza il tuo tempo e le tue risorse!\n\n\n<strong>💡 Tariffe degne di un Jarl</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo {annual_price}€! Meno di una manciata di monete al mese per un controllo totale e automatizzato dei prezzi.</em>\n\n<strong>Abbonamento a Vita:</strong> <em>Un unico pagamento di {lifetime_price}€ per un monitoraggio senza fine! Nessun rinnovo, nessuna complicazione.</em>\n\n\n<strong>🎁 Vantaggi Esclusivi</strong>\n\nSblocca tutte le mie abilità premium come le nuove personalità e personalizza la tua esperienza con la magia della tecnologia avanzata.\n\n\n<strong>🔒 Sicurezza e Affidabilità</strong>\n\nLa tua privacy è sacra come il codice d'onore dei Vichinghi. Gestisco i tuoi dati con i massimi standard di sicurezza e riservatezza.\n\n\n👉 <strong>Pronto per l'Upgrade?</strong>\n\nNon perdere questa opportunità leggendaria! Aggiorna ora al Premium e trasforma il tuo modo di saccheggiare su Amazon.",
			"premium_activate": "<strong>COME ATTIVARE LA VERSIONE PREMIUM </strong>\n\n1️⃣ Invia l'oro per l'abbonamento scelto (annuale o a vita) a https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il nostro corvo messaggero https://t.me/ReportPricePeekerBot \n\n3️⃣ Invia un messaggio con scritto: <em>Premium {user_ID}</em>\n\n4️⃣ Goditi il tuo status di Jarl 🌟",
			"premium_activated": "👋 <strong>CONGRATULAZIONI!</strong> 🌟\n\n Sei salito a bordo del PREMIUM. 🎉\n\nOra puoi accedere a tutti i tesori nascosti! 🚀 Per visionare il tuo bottino, usa il comando /profile",
			
			"share": "Come un vigile guardiano dei mari del Nord, tengo sotto stretta sorveglianza i mari di Amazon per scovare per te le offerte più ricche. Ricorda, anche se sono solo un bot, la caccia al risparmio è la mia epica battaglia! 🛡️\n\nDiffondi la voce di questo fedele bot tra i tuoi compagni di clan e aiutali a unirsi alla nostra gloriosa spedizione per conquistare le onde dei prezzi.\n\nInsieme, issiamo le vele verso il trionfo nel vasto oceano del risparmio! ❤️",
			"share_forward": "Hey! Ho scoperto questo fantastico bot che traccia i prezzi su Amazon e ti informa sugli sconti! È come avere un Vichingo digitale al tuo fianco. Dai un'occhiata!",
			"share_button": "🤖 INVITA I TUOI FRATELLI DI BATTAGLIA",
			
			"profile": "<strong>👀 INFORMAZIONI DEL GUERRIERO</strong>\n\n<strong>✏️ Nome da battaglia</strong>: {custom_name}\n\n<strong>🛍️ Tesori scovati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Vessillo del bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Non Attivo ❌",
			"profile_premium": "<strong>INFORMAZIONI DEL GUERRIERO</strong>\n\n<strong>✏️ Nome da battaglia</strong>: {custom_name}\n\n<strong>🛍️ Tesori scovati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Vessillo del bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Attivo ✅\n\n<strong>🎁 Pacchetto</strong>: {premium_type}\n\n<strong>⏳ Scadenza</strong>: {premium_expiry}",
		
			"remove_button": "❌ Scaccia Via",
			"view_button": "🤩 SACCHEGGIA BOTTINO SU AMAZON ORA!",
			"cart_button": "🤩 AGGIUNGI AL CARRELLO AMAZON ORA",
			"threshold_button": "🎯 Cambia Prezzo di Saccheggio",
			"chart_button": "📊 Mappa Bottino",
			"premium_button": "💎 ATTIVA PREMIUM ORA",

			"robot_friendly": "🤖 ROBOT AMICHEVOLE",
			"dark_wizard": "🧙‍♂️ MAGO OSCURO (💎)",
			"merchant_viking": "🛡️ VICHINGO COMMERCIANTE",

			"version": "<strong>🌟 Changelog Versione 2.0 del Bot 🌟</strong>\n\n🔷 <strong>Possibilità di Scegliere il Prezzo di Notifica per il Prodotto:</strong> <em>Decidi tu a quale prezzo vuoi essere avvisato! 🔔 Scegli la soglia che preferisci per ogni prodotto tracciato.</em>\n\n🔷 <strong>Grafico con lo Storico dei Prezzi del Prodotto:</strong> <em>Ora puoi visualizzare la cronologia dei prezzi per ogni prodotto! 📈 Un modo efficace per capire le tendenze e fare acquisti intelligenti.</em>\n\n🔷 <strong>Messaggi Personalizzati in Base alla Personalità del Bot:</strong> <em>Il bot ora ha diverse personalità! 🤖 Scegli quella che preferisci per una comunicazione su misura.</em>\n\n🔷 <strong>Abbonamenti Premium:</strong> <em>Accedi a funzioni esclusive con il nostro abbonamento premium! 🌐 Più potere nelle tue mani per un'esperienza di shopping ancora migliore.</em>\n\n🔷 <strong>Controllo dei Prezzi ad Orario Fisso 10:00 e 17:00 per Non Disturbare l'Utente:</strong> <em>I controlli dei prezzi avvengono ora a orari fissi 🕙🕔 per assicurarti di non essere disturbato in momenti inopportuni.</em>\n\n\nPremi /help se hai bisogno di aiuto o se vuoi scoprire la lista dei comandi disponibili."
		}


	}
}