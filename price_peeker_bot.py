"""
----------------------
LISTA COMANDI
----------------------

start - Welcome message
view_tracked - View all currently tracked products
help - How to use the bot correctly
set_language - Select the bot language
set_username - Choose the name the bot will use to call you
report - Report a bug to the developer
coffee - Thank the developer

start - Inizia a usare il bot
view_tracked - Visualizza i prodotti tracciati
help - Come usare il bot correttamente
set_language - Seleziona la lingua del bot
set_username - Scegli un nome personaizzato
report - Segnala un bug allo sviluppatore
coffee - Ringrazia lo sviluppatore


"""


# Libraries
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Updater, Filters, MessageHandler, CallbackQueryHandler, ConversationHandler
import requests
import re
import firebase_admin
from firebase_admin import credentials, firestore
import time
from translations import it_strings, en_strings
from functools import wraps
from amazon_paapi import AmazonApi
import os
import json

# Constant
NOT_AVAILABLE = 99999

# Get enviroment variables
FIREBASE_CREDENTIALS_JSON = os.environ.get('FIREBASE_CREDENTIALS_JSON')
AMAZON_ACCESS_KEY = os.environ.get('AMAZON_ACCESS_KEY')
AMAZON_SECRET_KEY = os.environ.get('AMAZON_SECRET_KEY')
AMAZON_ASSOC_TAG = os.environ.get('AMAZON_ASSOC_TAG')
AMAZON_COUNTRY = os.environ.get('AMAZON_COUNTRY')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
DEV_ID = os.environ.get('DEV_ID')

# Initialization Firestore DB
cred_dict = json.loads(FIREBASE_CREDENTIALS_JSON)
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Crea un'istanza di Amazon
amazon = AmazonApi(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, AMAZON_COUNTRY, throttling=10)


# Definition of the Product class
class Product:
    def __init__(self, name="Default Name", asin='XXXXXXXXXX', price=0, url="https://default.url", user_ID='XXXXXXXXXX', doc_ID='XXXXXXXXXX'):
        self.name = name
        self.asin = asin
        self.url = url
        self.price = price
        self.user_ID = user_ID
        self.doc_ID = doc_ID


    def __repr__(self):
        return f"Product(name='{self.name}', asin={self.asin}, prezzo={self.price}, url='{self.url}', user_ID={self.user_ID}, doc_ID={self.doc_ID})"


# Decorator that checks the user's language and sets the correct strings in the bot's context
def language_handler(func):
    @wraps(func)
    def wrapper(update, context, *args, **kwargs):
        user_language = context.user_data.get('language', 'it')  # Use 'it' as the default language

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
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username
    update.message.reply_text(strings['welcome'].format(custom_name=custom_name), parse_mode='HTML', disable_web_page_preview=True)


# Function to generate a report message
@language_handler
def report(update, context):
    strings = context.user_data['strings']
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    keyboard = [
            [
                InlineKeyboardButton(strings['report_button'], url="https://t.me/ReportPricePeekerBot"),
            ],
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(strings['report'].format(custom_name=custom_name), reply_markup=reply_markup)


# Function to generate a coffe message
@language_handler
def coffee(update, context):
    strings = context.user_data['strings']
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    keyboard = [
            [
                InlineKeyboardButton(strings['coffee_button'], url="https://www.paypal.me/vitodigrigoli"),
            ],
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(strings['coffee'].format(custom_name=custom_name), reply_markup=reply_markup)


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
def help(update, context):
    strings = context.user_data['strings']
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    commands = "\n".join([f"🔹 /{command} - <em>{description}</em>\n" for command, description in strings["commands"].items()])
    update.message.reply_text(strings["help"].format(custom_name=custom_name) + commands, parse_mode='HTML', disable_web_page_preview=True)


# Function to generate an Amazon affiliate link
def generate_affiliate_link(asin):

    url = "https://www.amazon.it/dp/" +  asin

    if AMAZON_ASSOC_TAG:
        if '?' in url:
            return f"{url}&tag={AMAZON_ASSOC_TAG}"
        else:
            return f"{url}?tag={AMAZON_ASSOC_TAG}"
    else:
        return url


# Function that generates a link to add a product directly to the cart
def generate_add_to_cart_link(asin):
    url = f'https://www.amazon.it/gp/aws/cart/add.html?ASIN.1={asin}&Quantity.1=1&AssociateTag={AMAZON_ASSOC_TAG}'

    return url


def get_full_url_from_shortlink(shortlink):
    response = requests.get(shortlink, allow_redirects=True)
    return response.url


# Function to extract a link within a message
def extract_amazon_link(text):
    # Cerca link Amazon standard e shortlinks
    regex = r'(https?://(?:www\.amazon\.[a-zA-Z]{2,3}/.+|amzn\.[a-zA-Z]{2,3}/.+))'

    try:
        link = re.findall(regex, text)[0]

        # Se non ci sono link, ritorna None
        if not link:
            link = None

        # Controlla se il link è uno shortlink
        if 'amzn' in link:
            link = get_full_url_from_shortlink(link)
        
    except:
        return None

    return link

# Function to get Amazon product info
def get_amazon_product(url):
    
    item = amazon.get_items(url)[0]

    name = item.item_info.title.display_value
    asin = item.asin
    affiliate_url = item.detail_page_url

    try:
        price = item.offers.listings[0].price.amount
    except:
        price = NOT_AVAILABLE

    return name, asin, price, affiliate_url


@language_handler
# Function to send an Amazon affiliate link
def track (update, context):

    user_ID = update.message.from_user.id
    strings = context.user_data['strings']
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    # Find URL in message
    message = update.message.text
    url = extract_amazon_link(message)

    if url:
        update.message.reply_text(strings['retrieving '].format(custom_name=custom_name), parse_mode='HTML')
        print(url)
        name, asin, price, affiliate_url = get_amazon_product(url)
        product = Product(name, asin, price, affiliate_url, user_ID)

        add_to_database(product)

        print_products(update, context, [product])
        update.message.reply_text(strings['tracking'].format(custom_name=custom_name))
       
    else:
        update.message.reply_text(strings['invalid_link'].format(custom_name=custom_name))


# Function that adds a product to be tracked to the database
def add_to_database(product: Product):
    doc_ref = db.collection('user_data').document()

    print(doc_ref.id)

    doc_ref.set({
        'product_name': product.name,
        'product_asin':  product.asin,
        'product_price': product.price,
        'product_url': product.url,
        'user_ID': product.user_ID
    })
    
    product.doc_ID = doc_ref.id


# Function that removes a tracked product from the database
def remove_from_database(doc_ID):
    try:
        db.collection('user_data').document(doc_ID).delete()
        print(f'Documento con ID {doc_ID} eliminato con successo.')

    except Exception as e:
        print(f'Errore nell\'eliminare il documento: {e}')


# Function that checks whether the price has dropped
def check_price(context):
    
    print("Start Check Price")
    start_time = time.time()
    # Retrieve all documents from 'user_data' collection
    docs = db.collection('user_data').stream()
    count = 0

    for doc in docs:
        count += 1
        data = doc.to_dict()
        user_ID = data['user_ID']
        product_url = data['product_url']
        initial_price = data['product_price']
        doc_ID = doc.id
        
        name, asin, price, affiliate_url = get_amazon_product(product_url)
        product = Product(name, asin, price, affiliate_url, user_ID, doc_ID)
        print(product)

        if product.price != initial_price:
            # updates the price and in the database
            doc.reference.update({'product_price': product.price})

            if  product.price < initial_price:
                keyboard = [
                    [
                        InlineKeyboardButton(it_strings['remove_button'], callback_data=f'remove:{product.doc_ID}'),
                        InlineKeyboardButton(it_strings['view_button'], url=product.url),
                    ],
                    [
                        InlineKeyboardButton(it_strings['cart_button'], url=generate_add_to_cart_link(product.asin)),
                    ],
                ]
                text = it_strings['price_dropped'].format(product_name=product.name, product_price=product.price, initial_price=initial_price, product_url = product.url)
                reply_markup = InlineKeyboardMarkup(keyboard)
                context.bot.send_message(chat_id=user_ID, text=text, reply_markup=reply_markup, parse_mode='HTML')

    end_time = time.time()
    elapsed_time = end_time - start_time
    [hours, minutes, seconds] = time_converter(elapsed_time)
    [avg_hours, avg_minutes, avg_seconds] = time_converter(elapsed_time/count)

    dev_text = f"--------------------------------------------------------------\n<strong>CHECK PRICE JOB STATISTICS</strong> 📊 \n--------------------------------------------------------------\n\n⏱ <strong>Elapsed Time</strong>: {int(hours)} hours - {int(minutes)} minutes - {int(seconds)} seconds\n\n📦 <strong>Tracked Products</strong>: {count}\n\n🧮 <strong>Time/Products</strong>: {int(avg_hours)} hours - {int(avg_minutes)} minutes - {int(avg_seconds)} seconds"
    context.bot.send_message(chat_id=DEV_ID, text=dev_text, parse_mode='HTML')


# Function that converts time into hours, minutes and seconds
def time_converter(elapsed_time):
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    return [hours, minutes, seconds]


# Function that prints all the user's tracked products
@language_handler
def view_tracked_products(update, context):
    user_ID = update.message.from_user.id
    tracked_products = get_user_products(user_ID)

    strings = context.user_data['strings']
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    for product in tracked_products:
        print(product)

    
    # Se la lista è vuota, invia un messaggio che indica che non ci sono elementi tracciati
    if tracked_products:
        print_products( update, context, tracked_products)
    else:
        update.message.reply_text(strings['list_empty'].format(custom_name=custom_name))
    

# Function that prints a list of products
@language_handler
def print_products(update, context, products):

    strings = context.user_data['strings']

    for product in products:
        keyboard = [
            [
                InlineKeyboardButton(strings['remove_button'], callback_data=f'remove:{product.doc_ID}'),
                InlineKeyboardButton(strings['view_button'], url=product.url),
            ],
            [
                InlineKeyboardButton(strings['cart_button'], url=generate_add_to_cart_link(product.asin)),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        if product.price != NOT_AVAILABLE:
            update.message.reply_text(f'<strong>🛍️ {product.name}\n\n💰 {product.price} €</strong>\n\n🟢 {strings["available"]}\n\n🔗 {product.url}', reply_markup=reply_markup, parse_mode='HTML')
        else:
            update.message.reply_text(f'<strong>🛍️ {product.name}</strong>\n\n🔴 {strings["not_available"]}\n\n🔗 {product.url}', reply_markup=reply_markup, parse_mode='HTML')


# Function that manages button callbacks
@language_handler
def button(update, context):
    query = update.callback_query
    query.answer()

    strings = context.user_data['strings']

    # Analizzare i dati della callback
    action, value = query.data.split(':')

    if action == 'remove':
        # Delete the item with ID item_id
        remove_from_database(value)
        text = strings["remove"]
    
    elif action == 'lang':
        #  Saves the user's language preference in the context
        if value ==  'it':
            context.user_data['language'] = 'it'
            text = "✅ La lingua è stata impostata correttamente"
        else:
            context.user_data['language'] = 'en'
            text = "✅ The language has been selected correctly"
        
    else:
        print("button default behavior")

    query.edit_message_text(text=text)


# Retrieves the user's products from the database
def get_user_products(user_ID):

    # Create a query to get all documents where 'user_id' matches the ID of the user who sent the message
    query_ref = db.collection('user_data').where('user_ID', '==', user_ID)

    # Run the query and get all matching documents
    docs = query_ref.stream()

    products_list = []

    for doc in docs:
        data = doc.to_dict()
        products_list.append(Product(data['product_name'], data['product_asin'], data['product_price'], data['product_url'], data['user_ID'], doc.id))

    return products_list


@language_handler
def set_username(update, context):
    strings = context.user_data['strings']
    update.message.reply_text(strings['choose_username'])
    context.user_data['set_username'] = True


@language_handler
def name_callback(update, context):
    strings = context.user_data['strings']
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    if context.user_data.get('set_username'):
        context.user_data['custom_name'] = update.message.text
        update.message.reply_text(strings['selected_username'].format(custom_name=update.message.text))
        context.user_data['set_username'] = False
    else:
        update.message.reply_text(strings['default_message'].format(custom_name=custom_name))


def get_stat(update, context):

    docs = db.collection('user_data').stream()
    user_list = []

    for doc in docs:
        data = doc.to_dict()
        user_list.append(data['user_ID'])

    n_products = len(user_list)
    n_users = len(set(user_list))

    # Send the information to the developer
    dev_text = f"--------------------------------------------------------------\n<strong>BOT STATISTICS</strong> 📊 \n--------------------------------------------------------------\n\n📦 <strong>Tracked Products</strong>: {n_products}\n\n👥 <strong>Users</strong>: {n_users}"
    context.bot.send_message(chat_id=DEV_ID, text=dev_text, parse_mode='HTML')


def main():
    
    # Initialization Bot
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    job_queue = updater.job_queue

    print("The bot is about to launch...")

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('view_tracked', view_tracked_products))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('set_language', set_language))
    dp.add_handler(CommandHandler('set_username', set_username), group=1)
    dp.add_handler(CommandHandler('coffee', coffee))
    dp.add_handler(CommandHandler('dev', get_stat))
    dp.add_handler(CommandHandler('report', report))
    dp.add_handler(MessageHandler(Filters.text & Filters.entity("url"), track), group=0)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.entity("url"), name_callback))
    dp.add_handler(CallbackQueryHandler(button))


    # Add a job to check the price every 6 hours
    job_queue.run_repeating(check_price, interval=21600, first=0)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

