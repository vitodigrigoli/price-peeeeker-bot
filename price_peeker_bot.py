"""
----------------------
LISTA COMANDI
----------------------

start - Welcome message
view_products - View all currently tracked products
help - How to use the bot correctly
set_language - Select the bot language
set_username - Choose the name the bot will use to call you
report - Report a bug to the developer
coffee - Thank the developer


start - Inizia a usare il bot
view_products - Visualizza i prodotti tracciati
help - Come usare il bot correttamente
set_username - Scegli un nome personaizzato
report - Segnala un bug allo sviluppatore
coffee - Ringrazia lo sviluppatore
version - Visualizza le novità della nuova versione

"""


# Libraries
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, error
from telegram.ext import CommandHandler, CallbackContext, Updater, Filters, MessageHandler, CallbackQueryHandler, ConversationHandler


import time
from translations import it_strings, en_strings
from functools import wraps
from datetime import datetime

from db_utils import update_products
from amazon_utils import extract_amazon_link, get_amazon_product, generate_add_to_cart_link
from toolbox import generate_alert_price, time_converter, create_chart, generate_price_history, disable_auto_link

from product import Product
from user import User
from config import DEV_ID, BOT_TOKEN, db

DELAY = 0.5


# Function to generate a welcome message at start
def start(update, context):
    strings = it_strings
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use first name as the default username

    update.message.reply_text(strings['welcome'].format(custom_name=custom_name), parse_mode='HTML', disable_web_page_preview=True)

    user_ID = str(update.message.from_user.id)
    User(user_ID).save()


# Function to generate a report message
def report(update, context):
    strings = it_strings
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    keyboard = [
            [
                InlineKeyboardButton(strings['report_button'], url="https://t.me/ReportPricePeekerBot"),
            ],
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(strings['report'].format(custom_name=custom_name), reply_markup=reply_markup)


# Function to generate a coffe message
def coffee(update, context):
    strings = it_strings
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    keyboard = [
            [
                InlineKeyboardButton(strings['coffee_button'], url="https://www.paypal.me/vitodigrigoli"),
            ],
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(strings['coffee'].format(custom_name=custom_name), reply_markup=reply_markup)


# Function that allows you to choose the username
def set_username(update, context):
    strings = it_strings
    update.message.reply_text(strings['choose_username'])

    context.user_data['set_username'] = True
    context.user_data['set_alert_price'] = False


# Function that generates a help message
def help(update, context):
    strings = it_strings
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    commands = "\n".join([f"🔹 /{command} - <em>{description}</em>\n" for command, description in strings["commands"].items()])
    update.message.reply_text(strings["help"].format(custom_name=custom_name) + commands, parse_mode='HTML', disable_web_page_preview=True)


# Function to send an Amazon affiliate link
def track (update, context):

    context.user_data['set_username'] = False
    context.user_data['set_alert_price'] = False

    user_ID = str(update.message.from_user.id)
    strings = it_strings
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    # Find URL in message
    message = update.message.text
    url = extract_amazon_link(message)

    if url:
        update.message.reply_text(strings['retrieving'].format(custom_name=custom_name), parse_mode='HTML')
        print(url)

        amazon_product = get_amazon_product(url)

        if(amazon_product == None):
            update.message.reply_text('Amazon non fornisce informazioni su questo prodotto'.format(custom_name=custom_name))

        elif(amazon_product == 'Used'):
            keyboard = [
                [
                    InlineKeyboardButton(strings['yes_button'], callback_data=f'track:yes_url'),
                    InlineKeyboardButton(strings['no_button'], callback_data=f'track:no'),
                ],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(strings['tracked_product--used'].format(custom_name=custom_name), reply_markup=reply_markup, parse_mode='HTML')

        else:
            product_ID = amazon_product.get('ID')
            product_name =	amazon_product.get('name')
            product_url =	amazon_product.get('url')
            product_price =	amazon_product.get('price')
            product_merchant =	amazon_product.get('merchant')
            product_history = generate_price_history(product_price)

            product = Product(
                ID = product_ID,
                name = product_name,
                url = product_url,
                price = product_price,
                merchant = product_merchant,
                history = product_history
            )

            product.save()

            user = User(user_ID)

            alert_price = generate_alert_price(product.price)
            product_data = {
                'ID': product.ID,
                'alert_price': alert_price,
                'last_alerted_price': product.price
            }

            print(product_data)
            user.add_product(product_data)

            print_product(update, context, product, product_data)
       
    else:
        update.message.reply_text(strings['invalid_link'].format(custom_name=custom_name))


# Function that checks whether the price has dropped
def check_price(context):

    strings = it_strings
    
    print("Start Check Price")
    start_time = time.time()

    update_products()
    
    docs = db.collection('users').stream()
    count = 0

    for doc in docs:
        count += 1
        user_data = doc.to_dict()
        user = User(doc.id, user_data['is_premium'], user_data['language_preference'], user_data['tracked_products'])
        
        for product_ID, product_data in user.tracked_products.items():

            product = Product.get_product(product_ID)

            if(product):

                if(product.price != None):

                    if(product_data['alert_price'] == None ):

                        print(f'Il prodotto {product.ID} è tornato disponibile per user {user.ID}')

                        new_alert_price = generate_alert_price(product.price)
                        new_last_alerted_price = product.price
                        user.update_tracked_product(product_ID, new_alert_price, new_last_alerted_price )

                        keyboard = [
                            [
                                InlineKeyboardButton(strings['remove_button'], callback_data=f'remove:{product.ID}'),
                                InlineKeyboardButton(strings['threshold_button'], callback_data=f'threshold:{product.ID}'),
                            ],
                            [
                                InlineKeyboardButton(strings['view_button'], url=product.url),
                                InlineKeyboardButton(strings['chart_button'], callback_data=f'chart:{product.ID}'),
                            ],
                            [
                                InlineKeyboardButton(strings['cart_button'], url=generate_add_to_cart_link(product.ID)),
                            ],
                        ]

                        text = strings['alert--available']
                        reply_markup = InlineKeyboardMarkup(keyboard)

                        try:
                            context.bot.send_message(chat_id = user.ID, text=text.format(product_name=product.name, product_price=product.price, product_url=product.url, product_merchant=disable_auto_link(product.merchant), alert_price=new_alert_price, last_alerted_price=new_last_alerted_price), reply_markup=reply_markup, parse_mode='HTML')

                        except error.Unauthorized:
                            print(f"User {user.ID} blocked the bot. I'm removing it from the database")
                            user.delete()

                        except error.TelegramError as e:
                            print('General error: {e}')

                    elif(product.price <= product_data['alert_price']):

                        print(f'Il prodotto {product.ID} ha raggiunto la soglia per user {user.ID}')
                        
                        new_alert_price = generate_alert_price(product.price)
                        new_last_alerted_price = product.price
                        user.update_tracked_product(product_ID, new_alert_price, new_last_alerted_price)

                        keyboard = [
                            [
                                InlineKeyboardButton(strings['remove_button'], callback_data=f'remove:{product.ID}'),
                                InlineKeyboardButton(strings['threshold_button'], callback_data=f'threshold:{product.ID}'),
                            ],
                            [
                                InlineKeyboardButton(strings['view_button'], url=product.url),
                                InlineKeyboardButton(strings['chart_button'], callback_data=f'chart:{product.ID}'),
                            ],
                            [
                                InlineKeyboardButton(strings['cart_button'], url=generate_add_to_cart_link(product.ID)),
                            ],
                        ]

                        text = strings['alert--threshold']
                        reply_markup = InlineKeyboardMarkup(keyboard)

                        try:
                            context.bot.send_message(chat_id = user.ID, text=text.format(product_name=product.name, product_price=product.price, product_url=product.url, product_merchant=disable_auto_link(product.merchant), alert_price=new_alert_price, last_alerted_price=new_last_alerted_price), reply_markup=reply_markup, parse_mode='HTML')

                        except error.Unauthorized:
                            print(f"User {user.ID} blocked the bot. I'm removing it from the database")
                            user.delete()

                        except error.TelegramError as e:
                            print('General error: {e}')

            else:
                print('The product is no longer in the products collection')
                user.remove_product(product_ID)
            time.sleep(DELAY)

        
    

    end_time = time.time()
    elapsed_time = end_time - start_time
    [hours, minutes, seconds] = time_converter(elapsed_time)
    [avg_hours, avg_minutes, avg_seconds] = time_converter(elapsed_time/count)

    dev_text = f"--------------------------------------------------------------\n<strong>CHECK PRICE JOB STATISTICS</strong> 📊 \n--------------------------------------------------------------\n\n⏱ <strong>Elapsed Time</strong>: {int(hours)} hours - {int(minutes)} minutes - {int(seconds)} seconds\n\n📦 <strong>Tracked Products</strong>: {count}\n\n🧮 <strong>Time/Products</strong>: {int(avg_hours)} hours - {int(avg_minutes)} minutes - {int(avg_seconds)} seconds"
    #context.bot.send_message(chat_id=DEV_ID, text=dev_text, parse_mode='HTML')


# Function that prints all the user's tracked products
def view_tracked_products(update, context):
    user_ID = str(update.message.from_user.id)

    strings = it_strings
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    user = User.get_user(user_ID)
    print(user)

    # Check if tracked_products is not empty
    if user.tracked_products:
        
        for product_ID, product_data in user.tracked_products.items():

            product = Product.get_product(product_ID)
            print_product(update, context, product, product_data)

            time.sleep(DELAY)
    else:
        update.message.reply_text(strings['list_empty'].format(custom_name=custom_name))
    

def print_product(update, context, product: Product, product_data):

    strings = it_strings

    alert_price = product_data.get('alert_price')
    last_alerted_price = product_data.get('last_alerted_price')

    if product.price != None:

        keyboard = [
            [
                InlineKeyboardButton(strings['remove_button'], callback_data=f'remove:{product.ID}'),
                InlineKeyboardButton(strings['threshold_button'], callback_data=f'threshold:{product.ID}'),
            ],
            [
                InlineKeyboardButton(strings['view_button'], url=product.url),
                InlineKeyboardButton(strings['chart_button'], callback_data=f'chart:{product.ID}'),
            ],
            [
                InlineKeyboardButton(strings['cart_button'], url=generate_add_to_cart_link(product.ID)),
            ],
        ]

        text = strings['tracked_product--available']
    
    else:

        keyboard = [
            [
                InlineKeyboardButton(strings['remove_button'], callback_data=f'remove:{product.ID}'),
                InlineKeyboardButton(strings['view_button'], url=product.url),
            ],
            [
                InlineKeyboardButton(strings['chart_button'], callback_data=f'chart:{product.ID}'),
            ],
        ]

        text = strings['tracked_product--not_available']

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text.format(name=product.name, price=product.price, url=product.url, product_merchant=disable_auto_link(product.merchant), alert_price=alert_price, last_alerted_price=last_alerted_price), reply_markup=reply_markup, parse_mode='HTML')


def change_threshold(update, context, user_ID, product_ID):

    context.user_data['set_alert_price'] = True
    context.user_data['set_username'] = False
    context.user_data['user_ID'] = user_ID
    context.user_data['product_ID'] = product_ID



def input_callback(update, context):
    strings = it_strings
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    if context.user_data.get('set_username'):
        context.user_data['custom_name'] = update.message.text
        update.message.reply_text(strings['selected_username'].format(custom_name=update.message.text))
        context.user_data['set_username'] = False

    elif context.user_data.get('set_alert_price'):
        user_ID = str(context.user_data.get('user_ID'))
        product_ID = context.user_data.get('product_ID')

        try:
            new_alert_price = float(update.message.text)
            print(new_alert_price)
            product = Product.get_product(product_ID)
            user = User.get_user(user_ID)

            if(product != None):
                if( new_alert_price < product.price):
                    user.update_price_alert(product_ID, new_alert_price)
                    update.message.reply_text(strings['threshold_success'].format(product_name=product.name, alert_price=new_alert_price), parse_mode='HTML')
                    context.user_data['set_alert_price'] = False
                else:
                    update.message.reply_text(strings['threshold_high'].format(product_name=product.name, product_price=product.price), parse_mode='HTML')

        except Exception as e:
            print(f"Error while entering the new price target: {e}")
            update.message.reply_text(strings['threshold_not_valid'], parse_mode='HTML')

    else:
        update.message.reply_text(strings['default_message'].format(custom_name=custom_name))


# Function that manages button callbacks
def buttons_callback(update, context):
    
    query = update.callback_query
    query.answer()

    strings = it_strings

    # Analizzare i dati della callback
    action, product_ID = query.data.split(':')
    user_ID = query.message.chat_id

    user = User(str(user_ID))
    product = Product.get_product(product_ID)

    # Delete the item with ID item_id
    if action == 'remove':
        user.remove_product(product_ID)
        query.edit_message_text(strings["remove"].format(product_name=product.name), parse_mode='HTML')

    # Change threshold price of user's product
    elif action == 'threshold':
        change_threshold(update, context, user_ID, product_ID)
        text = strings['change_threshold'].format(product_name=product.name)
        context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')

    elif action == 'chart':
        text = strings['chart'].format(product_name=product.name)
        context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')

        # Crea il grafico e ottieni il buffer
        buf = create_chart(product.history)
        
        # Invia il grafico come foto
        context.bot.send_photo(chat_id=user_ID, photo=buf)

        # Chiudi il buffer
        buf.close()

    else:
        print("button default behavior")


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


def broadcast_message(update, context):
    
    print()
    strings = it_strings
    users = db.collection('users').stream()

    for user in users:

        try:
            context.bot.send_message(chat_id=user.id, text=strings['broadcast'], parse_mode='HTML')
            time.sleep(DELAY)
        
        except Exception as e:
            print(f"Errore nell'invio del messaggio per user {user.id}: {e}")
    
    


def main():

    # Initialization Bot
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    job_queue = updater.job_queue

    print("The bot is about to launch...")

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('view_products', view_tracked_products))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('set_username', set_username), group=1)
    dp.add_handler(CommandHandler('coffee', coffee))
    dp.add_handler(CommandHandler('dev', get_stat))
    dp.add_handler(CommandHandler('report', report))
    dp.add_handler(MessageHandler(Filters.text & Filters.entity("url"), track), group=0)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.entity("url"), input_callback))
    dp.add_handler(CallbackQueryHandler(buttons_callback))

    # Configura un comando per inviare il broadcast
    dp.add_handler(CommandHandler("broadcast", broadcast_message))


    # Add a job to check the price every 6 hours
    job_queue.run_repeating(check_price, interval=30)
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

