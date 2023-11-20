def_strings = {
    "welcome": "Ciao {custom_name}! Sono il tuo nuovo bot personale 🫡\n\nPosso tracciare un prodotto su Amazon e avvisarti quando si abbasserà di prezzo o tornerà disponibile ⏳\n\n<strong>COME TRACCIARE UN PRODOTTO 🛍️</strong>\n\n1️⃣ Vai su <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Scegli il prodotto da tracciare\n\n3️⃣ Copia il link o premi sull'icona condividi\n\n4️⃣ Invialo in questa chat\n\n\nPremi /help per scoprire di cosa sono capace.",
    "choose_personality": "Puoi scegliere la mia personalità",
    "choose_username": "Come preferisci essere chiamato? 🫣",
    "selected_username": "Ciao {custom_name}! Lieto di conoscerti 🤗",
    "default_message": "Mi dispiace {custom_name}, ma non sono ancora bravo a conversare 🥺\n\nPuoi condividermi un link Amazon da tracciare invece. Beh, almeno quello so farlo bene.\n\nCredo...",
    "tracking": "✅ Sto tracciando il tuo prodotto correttamente.\n\n⏰ Ti avviserò io quando si abbasserà di prezzo o tornerà disponibile.",
    "help": "Ciao {custom_name}! Hai bisogno di aiuto? 🤭\n\nEccoti un tutorial su come usarmi correttamente: https://youtube.com/shorts/HlG2XXDhtUI?feature=share \n\n<strong>LISTA DEI COMANDI DISPONIBILI 🫵</strong>\n",
    "commands": {
        "start": "Inizia a usare il bot",
        "view_products": "Visualizza tutti i prodotti attualmente tracciati",
        "help": "Come usare il bot correttamente",
        "set_username": "Scegli il nome che userà il bot per chiamarti",
		'set_personality': "Scegli la personalità del bot",
		'premium': 'Sblocca le funzionalità premium del bot',
        "report": "Segnala un bug allo sviluppatore",
        "coffee": "Ringrazia lo sviluppatore con un caffè",
        # ... (aggiungi altre descrizioni di comandi qui)
    },
    "remove": "❌🫡 Non traccierò più <em>{product_name}</em>.",
    "remove_button": "❌ Rimuovi",
    "view_button": "👀 Vedi su Amazon",
    "cart_button": "🤩 AGGIUNGI AL CARRELLO AMAZON ORA",
    "threshold_button": "🎯 Cambia prezzo di notifica",
    "chart_button": "📊 Andamento prezzi",
	"premium_button": "🌟 PASSA ORA A PREMIUM",
    "list_empty": "Mi dispiace {custom_name}, ma non stai tracciando alcun prodotto al momento.\n\nPremi /help se hai bisogno di aiuto 🤦‍♂️",
    "coffee": "Ciao {custom_name}! 😇\n\nVedo che vuoi offrire un caffè al mio sviluppatore ☕️\n\nCon zucchero, grazie ⬇️\nhttps://www.paypal.me/vitodigrigoli",
    "coffee_button": "Offri SENZA ZUCCHERO 😈",
    "report": "Ciao {custom_name}! Vuoi segnalare un bug o un'idea allo sviluppatore? 👨‍💻\n\nContattalo tramite il nostro bot di supporto:\nhttps://t.me/ReportPricePeekerBot",
    "report_button": "📬 CONTATTALO ORA",
    "invalid_link": "Il link che hai mandato non è valido. Manda link provenienti solo da Amazon 🛍️\n\nPremi /help per guardare il tutorial 🤦‍♂️",
    "retrieving": "⏳ <em>Sto recuperando il prodotto...</em>",
    "tracked_product--available":"<strong>{product_name}</strong>\n\n🏷️ Prezzo <strong>{product_price}€</strong>\n\n🏪 Venduto da {product_merchant}\n\n🎯 Notifica quando arriva a {alert_price}€\n\n🔗 {product_url}",
    "tracked_product--not_available":"<strong>🛍️ {product_name}</strong>\n\n🔴 Non disponibile\n\n🔔 Ti avviserò io quando tornerà disponibile\n\n🔗 {product_url}",
	"tracked_product--used":"Mi dispiace {custom_name}, ma il prodotto che vuoi tracciare è usato. A causa dell'alta ",
	"yes_button": "✅ Si, avvisami quando il prodotto nuovo torna disponibile",
	"change_threshold": "🎯 Scrivimi la soglia per <em>{product_name}...</em>",
	"chart": "📊 <em>Sto tracciando il grafico di {product_name}...</em>",
	"broadcast": "Messaggio Broadcast",
	"alert--available": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong> è di nuovo <strong>DISPONIBILE</strong>! 🟢</strong>\n\n🏷️ Prezzo <strong>{product_price}€</strong>\n\n🏪 Venduto da {product_merchant}\n\n🔗 {product_url}",
	"alert--threshold": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Passa da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Venduto da {product_merchant}\n\n🔗 {product_url}",
    "threshold_success": "La soglia per <em>{product_name}</em> è stata impostata correttamente a <strong>{alert_price}€</strong> ✅",
	"threshold_high": "🚫 La soglia <strong>deve essere minore</strong> del prezzo di <strong>{product_price}€</strong>. Rimanda un nuovo prezzo da impostare.",
	"threshold_not_valid": "Valore non valido 🚫 Assicurati di non usare lettere e usa il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",
	"chart_not_available": "Non ci sono dati disponibili negli ultimi 90 giorni",
	"track_limit": "Hai raggunto il limite di {limit} prodotti tracciati. Rimuovine qualcuno da /view_products o passa a /premium per tracciare prodotti in maniere illimitata.",
    "premium":"<strong>🌟 Diventa Premium e Trasforma il Tuo Shopping su Amazon! 🌟</strong>\n\n\n<strong>🚀 Perché Premium?</strong>\n\nIl nostro bot Telegram è già un ottimo strumento per tracciare i prezzi su Amazon, ma con l'opzione Premium, puoi portare la tua esperienza di shopping a un livello completamente nuovo!\n\n\n<strong>🔓 Sblocca Potenzialità Illimitate</strong>\n\nCome utente Standard, sei limitato a tracciare fino a {limit} prodotti. Con Premium, elimina ogni limite! Traccia centinaia di prodotti contemporaneamente. Non perderti mai un'offerta, monitora gli articoli che desideri e risparmia tempo e denaro!\n\n\n<strong>💡 Prezzi Accessibili</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo 19,99€! Meno di 2€ al mese per un controllo totale sui prezzi.</em>\n\n<strong>Abbonamento Lifetime:</strong> <em>Un unico pagamento di 49,99€ per un accesso illimitato a vita! Nessun rinnovo, nessuna preoccupazione.</em>\n\n\n<strong>🎁 Vantaggi Esclusivi</strong>\n\nSblocca tutte le personalità premium del bot e personalizza la tua esperienza d'uso in maniera unica e divertente.\n\n\n<strong>🔒 Sicurezza e Affidabilità</strong>\nLa tua privacy è la nostra priorità. Gestiamo i tuoi dati con la massima sicurezza e riservatezza.\n\n👉 <strong>Pronto per l'Upgrade?</strong>\nNon lasciarti sfuggire questa opportunità! Aggiorna ora al Premium e rivoluziona il tuo modo di fare shopping su Amazon.",
	"premium_activate": "1️⃣ Invia l'importo dell'abbonamento scelto (annuale o lifetime) su https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il nostro bot di supporto https://t.me/ReportPricePeekerBot  \n\n3️⃣ Inviagli un messaggio con scritto: <em>Premium {user_ID}</em>\n\n4️⃣ Goditi adesso il tuo account premium 🌟",
    "product_not_found": "Purtroppo Amazon non fornisce informazioni su questo prodotto e questo non mi permette di tracciarlo. Mi dispiace 😓"


}


it_strings = {
    "welcome": "Ahoy, {custom_name}! Sono il tuo Vichingo Commerciante personale 🛡️\n\nPosso saccheggiare i prezzi su Amazon e avvisarti quando un bottino si abbassa di prezzo o torna disponibile ⚔️\n\n<strong>COME SACCHEGGIARE UN PRODOTTO 🏴‍☠️</strong>\n\n1️⃣ Naviga su <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Scegli il tesoro da saccheggiare\n\n3️⃣ Copia il link o usa l'icona condividi come il tuo compasso\n\n4️⃣ Invialo a questa ciurma in chat\n\n\nPremi /help se hai bisogno di navigare o guarda il <a href='https://youtube.com/shorts/HlG2XXDhtUI?feature=share'>mappe segrete</a> 🗺️",
    "choose_personality": "Puoi scegliere il mio spirito vichingo",
    "choose_username": "Come desideri essere chiamato nel nostro viaggio? 🏔️",
    "selected_username": "Salve, {custom_name}! Lieto di navigare con te 🚣‍♂️",
    "default_message": "Oh, {custom_name}, non sono ancora abile nel parlare delle terre lontane 🌊\n\nForse puoi condividere un link Amazon da saccheggiare? Almeno in quello sono esperto.\n\nForse...",
    "tracking": "✅ Sto tenendo d'occhio il tuo tesoro accuratamente.\n\n⏰ Soffierò nel mio corno quando si abbasserà di prezzo o tornerà disponibile.",
    "help": "Ahoy, {custom_name}! Ti serve aiuto nella tua avventura? 🚣\n\nEcco una mappa su come usare questa nave correttamente: https://youtube.com/shorts/HlG2XXDhtUI?feature=share \n\n<strong>COMANDI PER NAVIGARE 🧭</strong>",
    "commands": {
        "start": "Inizia a navigare con il bot",
        "view_products": "Guarda il bottino che stiamo tracciando",
        "help": "Impara a navigare con il bot",
        "set_username": "Scegli il nome con cui la ciurma ti chiamerà",
		"set_personality": "Scegli lo spirito del tuo Vichingo",
		"premium": "Sblocca le terre lontane del Premium",
        "report": "Segnala un mare in tempesta allo sviluppatore",
        "coffee": "Offri un idromele allo sviluppatore",
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
	"broadcast": 'Messaggio del corno',
	"alert--available": "<strong>🚨 ALL'ATTACCO! 🚨</strong>\n\n<strong>{product_name}</strong> è di nuovo <strong>DISPONIBILE</strong>! 🟢</strong>\n\n🏷️ Bottino a soli <strong>{product_price}€</strong>\n\n🏪 Venduto dai mercanti di {product_merchant}\n\n🔗 {product_url}",
	"alert--threshold": "<strong>🚨 ATTENZIONE, MARINAI! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Passa da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Venduto dai mercanti di {product_merchant}\n\n🔗 {product_url}",
    "threshold_success": "La soglia di saccheggio per <em>{product_name}</em> è stata impostata correttamente a <strong>{alert_price}€</strong> ✅",
	"threshold_high": "🚫 La soglia <strong>deve essere più bassa</strong> del prezzo di <strong>{product_price}€</strong>. Rimanda un nuovo prezzo per il saccheggio.",
	"threshold_not_valid": "Valore non valido 🚫 Assicurati di non usare rune e usa il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",
	"chart_not_available": "Non ci sono mappe disponibili negli ultimi 90 giorni",
	"track_limit": "Hai raggiunto il limite di {limit} tesori tracciati. Abbandona qualcuno da /view_products o passa a /premium per saccheggiare senza limiti.",
	"premium_activate": "1️⃣ Invia l'oro per l'abbonamento scelto (annuale o lifetime) su https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il nostro drakkar di supporto https://t.me/ReportPricePeekerBot  \n\n3️⃣ Mandaci un messaggio con scritto: <em>Premium {user_ID}</em>\n\n4️⃣ Goditi ora il tuo account premium dei mari 🌟",
    "premium": "<strong>🌟 Salpa verso l'Orizzonte Premium e Conquista le Offerte su Amazon! 🌟</strong>\n\n<strong>🚀 Perché Scegliere la Rotta Premium?</strong>\nLa nostra nave bot di Telegram è già un'abile compagna per tracciare i prezzi su Amazon, ma con l'opzione Premium, issa le vele verso un'avventura di shopping senza pari!\n\n<strong>🔓 Sblocca i Mari Illimitati delle Offerte</strong>\nCome membro dell'equipaggio Standard, puoi saccheggiare fino a {limit} tesori. Con Premium, nessuna costa è fuori dalla tua portata! Saccheggia centinaia di prodotti senza sosta. Non perdere mai un'offerta, tieni d'occhio i tesori che desideri e risparmia tempo e monete d'oro!\n\n<strong>💡 Tariffe da Conquistatore</strong>\n<strong>Abbonamento Annuale:</strong> <em>Solo 19,99€! Meno di un sacco di monete al mese per il controllo totale dei mari del commercio.</em>\n<strong>Opzione Vita da Vichingo:</strong> <em>Un unico tributo di 49,99€ per un saccheggio illimitato a vita! Nessun rinnovo, nessuna battaglia in più da combattere.</em>\n\n<strong>🔒 Cassaforte del Drakkar</strong>\nIl tuo bottino è al sicuro con noi. Proteggiamo i tuoi segreti con la forza di un guerriero vichingo.\n\n👉 <strong>Pronto a Issare le Vele?</strong>\nNon lasciare che questa nave salpi senza di te! Aggiorna ora al Premium e trasforma il tuo modo di saccheggiare su Amazon."

}






block_1 = {

			"welcome": "Saluti, {custom_name}! Io sono il tuo assistente bot personale 🤖\n\nPosso monitorare i prodotti su Amazon e informarti sui loro abbassamenti di prezzo o sulla loro disponibilità ⏳\n\n<strong>COME MONITORARE UN PRODOTTO 🛍️</strong>\n\n1️⃣ Visita <a href='https://www.amazon.it?&tag=price-peeker-21'>Amazon.it</a>\n\n2️⃣ Seleziona il prodotto che ti interessa\n\n3️⃣ Copia il link o usa l'icona di condivisione\n\n4️⃣ Inviamelo in questa chat\n\n\nPremi /help se hai bisogno di aiuto o scoprire la lista di comandi disponibili.",
			"default_message": "Mi dispiace {custom_name}, non sono ancora il massimo nella conversazione 🤖\n\nPotresti condividere un link Amazon da monitorare? Ecco, questo lo so fare bene!\n\nCredo...",
			"invalid_link": "Il link inviato non è valido. Per favore, invia link solo da Amazon 🛍️\n\nPremi /help per vedere il tutorial 🤖",
			"product_not_found": "Mi dispiace, {custom_name}. Non sono riuscito a trovare informazioni su questo prodotto su Amazon, quindi non posso monitorarlo. Mi dispiace 😓",
			
			"choose_personality": "Puoi selezionare la mia personalità",
			"personality_changed": "Spero che questo nuovo me ti piaccia 🤖",
			"personality_not_changed": "Per usare questa personalità devi essere un utente premium. Attivala con il comando /premium 🤖",

			"choose_username": "Con quale nome preferisci essere chiamato? 🤖",
			"selected_username": "Salve {custom_name}! È un piacere conoscerti 🤖",
}

block_2 = {
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
}
block_2a = {
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
}
block_3 = {
			"tracked_product--available": "<strong>{product_name}</strong>\n\n🏷️ Prezzo attuale <strong>{product_price}€</strong>\n\n🏪 Venditore <em>{product_merchant}</em>\n\n🎯 Notifica impostata a {alert_price}€\n\n🔗 {product_url}",
			"tracked_product--not_available": "<strong>{product_name}</strong>\n\n🔴 Attualmente non disponibile\n\n🔔 Ti informerò non appena tornerà disponibile\n\n🔗 {product_url}",
			"tracked_product--used": "Mi dispiace {custom_name} 😔 ma il prodotto che hai inviato sembra essere usato, e purtroppo non posso tracciarne il prezzo in modo affidabile.\n\nI prezzi dei prodotti usati possono variare molto a seconda delle loro condizioni, e non vorrei confonderti con notifiche imprecise.\n\nMa hey, ho un'idea! 🌟 Che ne dici di tracciare lo stesso prodotto, ma nella versione nuova? 🆕\n\nCosì posso fornirti aggiornamenti accurati e tempestivi sui prezzi! Fammi sapere se ti va, sarò più che felice di aiutarti. 🤓✨",
			
			"yes_button": "✅ Si, traccia il nuovo",

			"alert--available": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong> è ora <strong>DISPONIBILE</strong>! 🟢\n\n🏷️ Prezzo attuale <strong>{product_price}€</strong>\n\n🏪 Venditore {product_merchant}\n\n🔗 {product_url}",
			"alert--threshold": "<strong>🚨 ATTENZIONE! 🚨</strong>\n\n<strong>{product_name}</strong>\n\n🏷️ Prezzo ridotto da <del>{last_alerted_price}€</del> a <strong>{product_price}€</strong>\n\n🏪 Venditore {product_merchant}\n\n🔗 {product_url}",
			
			"change_threshold": "🎯 Scrivi il prezzo di notifica per <em>{product_name}</em>",
			"threshold_success": "La soglia per <em>{product_name}</em> è stata impostata correttamente a <strong>{alert_price}€</strong> ✅",
			"threshold_high": "🚫 La soglia deve essere inferiore al prezzo attuale di <strong>{product_price}€</strong>. Inserisci un nuovo prezzo.",
			"threshold_not_valid": "Valore non valido 🚫. Usa solo numeri e il punto per le cifre decimali.\n\n<em>Esempio: 21.35</em>",
}
block_4 = {
			"premium": "<strong>🌟 ELEVA IL TUO SHOPPING SU AMAZON CON PREMIUM! 🌟</strong>\n\n\n<strong>🚀 Perché Scegliere Premium?</strong>\n\nCome assistente bot su Telegram, offro già un'eccellente esperienza nel tracciare i prezzi su Amazon, ma con l'opzione Premium, la tua esperienza di shopping raggiungerà nuove vette tecnologiche!\n\n\n<strong>🔓 Sblocca Potenzialità Illimitate</strong>\n\nIn qualità di utente Standard, puoi monitorare fino a {free_limit} prodotti. Con Premium, supera ogni limite! Monitora <strong>fino a {premium_limit} prodotti</strong> contemporaneamente.\n\nNon perdere mai un'offerta, tieni d'occhio gli articoli che desideri e ottimizza il tuo tempo e le tue risorse finanziarie!\n\n\n<strong>💡 Tariffe Convenzionali</strong>\n\n<strong>Abbonamento Annuale:</strong> <em>Solo {annual_price}€! Meno di 2€ al mese per un controllo totale e automatizzato dei prezzi.</em>\n\n<strong>Abbonamento Lifetime:</strong> <em>Un unico pagamento di {lifetime_price}€ per un monitoraggio illimitato a vita! Nessun rinnovo, nessuna complicazione.</em>\n\n\n<strong>🎁 Vantaggi Esclusivi</strong>\n\nSblocca tutte le mie funzionalità premium come le nuove personalità e personalizza la tua esperienza con un tocco di tecnologia avanzata.\n\n\n<strong>🔒 Sicurezza e Affidabilità</strong>\n\nLa tua privacy è una mia priorità fondamentale. Gestisco i tuoi dati con i massimi standard di sicurezza e riservatezza.\n\n\n👉 <strong>Pronto per l'Upgrade?</strong>\n\nNon perdere questa opportunità tecnologica! Aggiorna ora al Premium e trasforma il tuo modo di fare shopping su Amazon.",
			"premium_activate": "<strong>COME ATTIVARE LA VERSIONE PREMIUM </strong>\n\n1️⃣ Invia l'importo dell'abbonamento scelto (annuale o lifetime) a https://www.paypal.me/vitodigrigoli \n\n 2️⃣ Apri il nostro bot di supporto https://t.me/ReportPricePeekerBot \n\n3️⃣ Invia un messaggio con scritto: <em>Premium {user_ID}</em>\n\n4️⃣ Goditi il tuo account premium 🌟",
			"premium_activated": "👋 <strong>CONGRATULAZIONI!</strong> 🌟\n\n Hai effettuato l'upgrade a PREMIUM. 🎉\n\nOra puoi accedere a tutto ciò che è extra-speciale! 🚀 Per dare un'occhiata ai dettagli del tuo abbonamento, usa il comando /profile",
}
block_4a = {
	        "share": "Sto monitorando attentamente i prezzi su Amazon per te. Anche se sono solo un bot, mi preoccupo del tuo risparmio!\n\nCondividi questo bot con altri e aiutali a risparmiare anche loro.\n\nInsieme possiamo fare la differenza! ❤️",
			"share_forward": "Hey! Ho scoperto questo fantastico bot che traccia i prezzi su Amazon e ti informa sugli sconti! È super utile e affidabile. Dai un'occhiata!",
			"share_button": "🤖 INVITA GLI AMICI",
			
			"profile": "<strong>👀 INFOMAZIONI PROFILO</strong>\n\n<strong>✏️ Nome personalizzato</strong>: {custom_name}\n\n<strong>🛍️ Prodotti tracciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Personalità bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Non Attivo ❌",
			"profile_premium":"<strong>INFOMAZIONI PROFILO</strong>\n\n<strong>✏️ Nome personalizzato</strong>: {custom_name}\n\n<strong>🛍️ Prodotti tracciati</strong>: {tracked_products}/{limit}\n\n<strong>🌍 Lingua</strong>: {language}\n\n<strong>🤖 Personalità bot</strong>: {personality_mode}\n\n<strong>💎 Premium</strong>: Attivo ✅\n\n<strong>🎁 Pacchetto</strong>: {premium_type}\n\n<strong>⏳ Scadenza</strong>: {premium_expiry}",
}

block_5 = {
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