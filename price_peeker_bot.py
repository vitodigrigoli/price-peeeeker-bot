"""
----------------------
LISTA COMANDI
----------------------

start - Welcome message
view_tracked - View all currently tracked products
set_language - Select the bot language
set_username - Choose the name the bot will use to call you
help - How to use the bot correctly
coffee - Thank the developer for saving you money on Amazon


"""


# Libraries
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Updater, Filters, MessageHandler, CallbackQueryHandler, ConversationHandler
import requests
from bs4 import BeautifulSoup
import regex
import firebase_admin
from firebase_admin import credentials, firestore
import time, random
from translations import it_strings, en_strings
from functools import wraps


# Constant
TOKEN = "6420747835:AAE-6-JFsSoccOCXpA_opgmLsGS3dQWEzd4"
AMAZON_AFFILIATE_TAG = "advicenology_vito-21"


# Initialization Firebase
cred = credentials.Certificate("price-peeker-bot-firebase-adminsdk-i71n8-df7db42e8b.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# Definition of the Product class
class Product:
    def __init__(self, name="Default Name", url="https://default.url", price=0, asin='XXXXXXXXXX', id='XXXXXXXXXX'):
        self.name = name
        self.url = url
        self.price = price
        self.asin = asin
        self.id = id

    def __repr__(self):
        return f"Product(nome='{self.name}', url='{self.url}', prezzo={self.price}, ASIN={self.asin}, ID={self.id})"


# Decorator that checks the user's language and sets the correct strings in the bot's context
def language_handler(func):
    @wraps(func)
    def wrapper(update, context, *args, **kwargs):
        user_language = context.user_data.get('language', 'en')  # Use 'en' as the default language

        if user_language == 'it':
            context.user_data['strings'] = it_strings
        else:
            context.user_data['strings'] = en_strings
        
        return func(update, context, *args, **kwargs)
    
    return wrapper


# Function to generate a welcome message at start
@language_handler
def start(update, context):
    strings = context.user_data['strings']
    custom_name = context.user_data.get('custom_name', '')  # Use empty string as the default username
    update.message.reply_text(strings['welcome'].format(custom_name=custom_name))



# Function to generate a shutdown message when stopping
def stop(update, context):
    update.message.reply_text('Il bot si sta spegnendo...')



@language_handler
# Function that allows you to choose the language
def set_language(update, context):
    keyboard = [
        [InlineKeyboardButton("Italiano 🇮🇹", callback_data='lang:it')],
        [InlineKeyboardButton("English 🇬🇧", callback_data='lang:en')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    strings = context.user_data['strings']
    update.message.reply_text(strings['choose_language'], reply_markup=reply_markup)

@language_handler
# Function that generates a help message
def show_help(update, context):
    strings = context.user_data['strings']
    help_text = "\n".join([f"/{command} - {description}" for command, description in strings["commands"].items()])
    update.message.reply_text(help_text)


# Function to generate an Amazon affiliate link
def generate_affiliate_link(url):
    if AMAZON_AFFILIATE_TAG:
        if '?' in url:
            return f"{url}&tag={AMAZON_AFFILIATE_TAG}"
        else:
            return f"{url}?tag={AMAZON_AFFILIATE_TAG}"
    else:
        return url


# Function that generates a link to add a product directly to the cart
def generate_add_to_cart_link(asin):
    url = f'https://www.amazon.it/gp/aws/cart/add.html?ASIN.1={asin}&Quantity.1=1&AssociateTag={AMAZON_AFFILIATE_TAG}'

    return url


# Function to extract a link within a message
def find_link_in_message(message):
    url_pattern = r'(https?://[^\s]+)'
    match = regex.search(url_pattern, message)
    
    if match:
        # Returns the first URL found in the message
        return match.group(0)
    else:
        # Returns None if no URL is found
        return None


# Function to extract price from Amazon link
def get_amazon_product(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # CSS selector
    price = soup.select_one('span.a-offscreen')
    name = soup.select_one('#productTitle')
    asin = soup.find('input', id='ASIN').get('value')

    # Clean values
    price = float(price.text.replace('€', '').replace(',', '.').strip())
    name = str(name.text).strip()

    product = Product(name, url, price, asin)

    return product


# Function to send an Amazon affiliate link
def track (update, context):
    message = update.message.text
    link = find_link_in_message(message)
    user_id = update.message.from_user.id

    if link:
        affiliate_link = generate_affiliate_link(link)
        product = get_amazon_product(affiliate_link)
        print(product)

        if product :
            add_to_database(user_id, product)
            update.message.reply_text("I am tracking your product correctly!")
            print_products([product], update)
            
        else:
            update.message.reply_text("I could not find the price for this product.")

    else:
            update.message.reply_text(f'No valid link found in message.')


# Function that adds a product to be tracked to the database
def add_to_database(user_id, product):
    doc_ref = db.collection('user_data').document()

    doc_ref.set({
        'user_id': user_id,
        'product_name': product.name,
        'product_url': product.url,
        'product_price': product.price,
        'product_asin':  product.asin,
    })


# Function that removes a tracked product from the database
def remove_from_database(document_id):
    try:
        db.collection('user_data').document(document_id).delete()
        print(f'Documento con ID {document_id} eliminato con successo.')

    except Exception as e:
        print(f'Errore nell\'eliminare il documento: {e}')


# Function that checks whether the price has dropped
def check_price(context):
    
    print("Start Check Price")
    # Retrieve all documents from 'user_data' collection
    docs = db.collection('user_data').stream()

    for doc in docs:
        data = doc.to_dict()
        user_id = data['user_id']
        product_url = data['product_url']
        initial_price = data['product_price']
        
        product = get_amazon_product(product_url)
        print(product)
        
        if product.price is not None and product.price < initial_price:
            context.bot.send_message(chat_id=user_id, text=f"The price for {product.asin} has dropped! Now it is €{product.price}. Buy now: {product_url}")

            # updates the initial price in the database
            doc.reference.update({'product_price': product.price})
            
        else:
            context.bot.send_message(chat_id=user_id, text=f"The price for {product.asin} has not decreased! I'll check back in 1 minute")
        
        time.sleep(random.uniform(1, 5))


# Function that prints all the user's tracked products
def view_tracked_products(update, context):
    user_id = update.message.from_user.id
    tracked_products = get_user_products(user_id)

    for product in tracked_products:
        print(product)

    
    # Se la lista è vuota, invia un messaggio che indica che non ci sono elementi tracciati
    if tracked_products:
        print_products(tracked_products, update)
    else:
        response_message = "Non stai tracciando alcun prodotto al momento."
        update.message.reply_text(response_message)


# Function that prints a list of products
def print_products(products, update):

    for product in products:
        keyboard = [
            [
                InlineKeyboardButton("Remove", callback_data=f'remove:{product.id}'),
                InlineKeyboardButton("View on Amazon", url=product.url),
            ],
            [
                InlineKeyboardButton("Add to Cart NOW", url=generate_add_to_cart_link(product.asin)),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(f'{product.name}\n', reply_markup=reply_markup)


# Function that manages button callbacks
@language_handler
def button(update, context):
    query = update.callback_query
    query.answer()

    # Analizzare i dati della callback
    action, value = query.data.split(':')
    

    if action == 'remove':
        # Delete the item with ID item_id
        remove_from_database(value)
        query.edit_message_text(text=f"Elemento con ID {value} eliminato")
    
    elif action == 'lang':
        #  Saves the user's language preference in the context
        if value ==  'it':
            context.user_data['language'] = 'it'
            text = "La lingua è stata impostata correttamente ✅"
        else:
            context.user_data['language'] = 'en'
            text = "The language has been selected correctly ✅"

        query.edit_message_text(text=text)
    else:
        print("button default behavior")


# Retrieves the user's products from the database
def get_user_products(user_id):

    # Create a query to get all documents where 'user_id' matches the ID of the user who sent the message
    query_ref = db.collection('user_data').where('user_id', '==', user_id)

    # Run the query and get all matching documents
    docs = query_ref.stream()

    products_list = []

    for doc in docs:
        data = doc.to_dict()
        products_list.append(Product(data['product_name'], data['product_url'], data['product_price'], data['product_asin'], doc.id ))

    return products_list


@language_handler
def set_username(update, context):
    strings = context.user_data['strings']
    update.message.reply_text(strings['choose_username'])
    context.user_data['set_username'] = True


@language_handler
def name_callback(update, context):

    if context.user_data.get('set_username'):
        custom_name = f" {update.message.text}"
        context.user_data['custom_name'] = custom_name

        strings = context.user_data['strings']
        update.message.reply_text(strings['selected_username'].format(custom_name=custom_name))
        context.user_data['set_username'] = False
    else:
        update.message.reply_text(f'Manda un link disgraziato')


def main():
    
    # Initialization Bot
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    job_queue = updater.job_queue


    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(CommandHandler('set_language', set_language))

    dp.add_handler(CommandHandler('help', show_help))
    dp.add_handler(CommandHandler('view_tracked', view_tracked_products))
    dp.add_handler(MessageHandler(Filters.text & Filters.entity("url"), track), group=0)
    dp.add_handler(CommandHandler('set_username', set_username), group=1)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.entity("url"), name_callback))
    dp.add_handler(CallbackQueryHandler(button))



    # Add a job to check the price every 1 minute
    #job_queue.run_repeating(check_price, interval=60, first=0)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

