import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import random
import io


def generate_alert_price(price):
    
	alert_price = None

	if(price != None):

		if (price < 100):
			alert_price = round( price - price / 100 * 5, 2)
		else:
			alert_price = round( price - price / 100 * 2, 2)

	return alert_price


# Function that converts time into hours, minutes and seconds
def time_converter(elapsed_time):
	hours, remainder = divmod(elapsed_time, 3600)
	minutes, seconds = divmod(remainder, 60)

	return [hours, minutes, seconds]


def create_chart(history, limit=90):

    history = dict(sorted(history.items())[-limit:])

    # Converti il dizionario in un DataFrame
    df = pd.DataFrame(list(history.items()), columns=['Date', 'Price'])
    df['Date'] = pd.to_datetime(df['Date'])

    # Ordina il DataFrame per data
    df = df.sort_values('Date')

    df.dropna(inplace=True)

    if len(df) == 0:
        return None


    # Calcola il prezzo massimo, minimo e medio
    max_price = df['Price'].max()
    min_price = df['Price'].min()
    avg_price = round(df['Price'].mean(), 2)

    # Formattazione per visualizzare due cifre decimali
    max_price_str = "{:.2f}".format(max_price)
    min_price_str = "{:.2f}".format(min_price)
    avg_price_str = "{:.2f}".format(avg_price)

    # Creazione di un grafico combinato con Seaborn
    sns.color_palette("vlag", as_cmap=True)
    sns.set(style="darkgrid")

    # Limita il grafico 
    min_limit = min_price * 0.97
    max_limit = max_price * 1.03
    plt.figure(figsize=(12, 6))
    plt.ylim(min_limit, max_limit)

    # Creazione del barplot
    sns.barplot(data=df, x='Date', y='Price', hue='Price', palette="viridis")

    # Formattazione dell'asse X per mostrare solo la prima e l'ultima data
    plt.xticks([0, len(df) - 1], [df['Date'].dt.strftime('%d-%m-%Y').iloc[0], df['Date'].dt.strftime('%d-%m-%Y').iloc[-1]])


    # Aggiunta di titolo e etichette agli assi
    plt.title(f'Storico Prezzi a {limit} giorni', fontsize=14)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Prezzo (€)', fontsize=12)

    # Mostra la legenda
    plt.legend([f'Prezzo Massimo: {max_price_str}€', f'Prezzo Minimo: {min_price_str}€', f'Prezzo Medio: {avg_price_str}€'], frameon=True)

    # Mostra il grafico
    plt.tight_layout()

    # Crea un buffer di memoria
    buf = io.BytesIO()

    # Salva il grafico nel buffer
    plt.savefig(buf, format='png')

    # Riporta il cursore del buffer all'inizio del file
    buf.seek(0)

    # Chiudi il plot per liberare memoria
    plt.close()

    return buf


def generate_price_history(initial_price, days=90):

    current_date = datetime.now()
    history = {}

    formatted_date = current_date.strftime('%Y-%m-%d')
    history[formatted_date] = initial_price

    if(initial_price != None):

        # Move to the previous day
        current_date -= timedelta(days=1)
            
        for _ in range(days - 1):
            # Change the price by a random percentage up to 5%
            percentage_variation = random.uniform(-0.025, 0.025)
            initial_price += initial_price * percentage_variation

            # Format the date as a string and add the price to the dictionary
            formatted_date = current_date.strftime('%Y-%m-%d')
            history[formatted_date] = round(initial_price, 2)

            # Move to the previous day
            current_date -= timedelta(days=1)

    return history


def disable_auto_link(url):

    if(url):
        # Sostituisce il punto con un punto e uno spazio, per evitare che Telegram lo riconosca come un URL
        return url.replace('.', '_')






def main():

    history = generate_price_history(125.55)
    print(history)

    create_chart(history)



if __name__ == '__main__':
    main()


