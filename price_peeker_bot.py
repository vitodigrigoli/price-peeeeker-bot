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
help - Impara a usare il bot correttamente
set_username - Scegli un nome personaizzato
set_personality - Scegli la personalità del bot
premium - Attiva le funzionalità premium del bot
report - Segnala un bug allo sviluppatore
coffee - Ringrazia lo sviluppatore
share - Condividimi con i tuoi amici
profile - Guarda il tuo profilo
version - Visualizza le novità della nuova versione

"""


# Libraries
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, error
from telegram.ext import CommandHandler, Updater, Filters, MessageHandler, CallbackQueryHandler



from datetime import time as dt_time
import time
from pytz import timezone

from translations import it_strings

from db_utils import update_products, count_documents_in_collection
from amazon_utils import extract_amazon_link, get_amazon_product, generate_add_to_cart_link
from toolbox import generate_alert_price, time_converter, create_chart, generate_price_history, disable_auto_link

from product import Product
from user import User
from config import DEV_ID, BOT_TOKEN, db, FREE_PRODUCTS_LIMIT, PREMIUM_PRODUCTS_LIMIT, DELAY, ANNUAL_PRICE, LIFETIME_PRICE

from bot_responses import responses




# Function to generate a welcome message at start
def start(update, context):
    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()

    strings = responses[user.language_preference][user.personality_mode]

    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use first name as the default username

    update.message.reply_text(strings['welcome'].format(custom_name=custom_name), parse_mode='HTML', disable_web_page_preview=True)

    

# Function to generate a report message
def report(update, context):

    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

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

    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]
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

    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

    update.message.reply_text(strings['choose_username'])

    context.user_data['set_username'] = True
    context.user_data['set_alert_price'] = False
    context.user_data['start_broadcast'] = False



def start_broadcast(update, context):

    update.message.reply_text("Per favore, inviami il messaggio che vuoi trasmettere.")

    context.user_data['start_broadcast'] = True
    context.user_data['set_username'] = False
    context.user_data['set_alert_price'] = False


# Function that generates a help message
def help(update, context):

    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    commands = "\n".join([f"🔹 /{command} - <em>{description}</em>\n" for command, description in strings["commands"].items()])
    update.message.reply_text(strings["help"].format(custom_name=custom_name) + commands, parse_mode='HTML', disable_web_page_preview=True)



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
        user = User(doc.id, user_data['premium_status'], user_data['language_preference'], user_data['personality_mode'], user_data['tracked_products'])
        
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
                            context.bot.send_message(chat_id = user.ID, text=text.format(product_name=product.name, product_price=product.price, product_url=product.url, product_merchant=disable_auto_link(product.merchant), alert_price=new_alert_price, last_alerted_price=product_data['last_alerted_price']), reply_markup=reply_markup, parse_mode='HTML')

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
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    # Check if tracked_products is not empty
    if user.tracked_products:
        
        for product_ID, product_data in user.tracked_products.items():

            product = Product.get_product(product_ID)
            #print_product(update, context, product, product_data)
            send_product(context, user.ID, product, product_data)

            time.sleep(DELAY)
    else:
        update.message.reply_text(strings['list_empty'].format(custom_name=custom_name))
    

def print_product(update, context, product: Product, product_data):

    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

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
    update.message.reply_text(text.format(product_name=product.name, product_price=product.price, product_url=product.url, product_merchant=disable_auto_link(product.merchant), alert_price=alert_price, last_alerted_price=last_alerted_price), reply_markup=reply_markup, parse_mode='HTML')


def change_threshold(update, context, user_ID, product_ID):

    context.user_data['set_alert_price'] = True
    context.user_data['set_username'] = False
    context.user_data['start_broadcast'] = False

    context.user_data['user_ID'] = user_ID
    context.user_data['product_ID'] = product_ID



def input_callback(update, context):

    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

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

    elif context.user_data.get('start_broadcast'):
        message = update.message.text
        context.bot.send_message(chat_id=DEV_ID, text="Messaggio ricevuto. Inviando a tutti gli utenti...")
        # Invia il messaggio a tutti gli utenti
        broadcast_message(update, context, message)
        context.user_data['start_broadcast'] = False

    else:
        update.message.reply_text(strings['default_message'].format(custom_name=custom_name))


# Function to send an Amazon affiliate link
def track (update, context):

    context.user_data['set_username'] = False
    context.user_data['set_alert_price'] = False

    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

    # Find URL in message
    message = update.message.text
    url = extract_amazon_link(message)

    if user.count_tracked_products() >= FREE_PRODUCTS_LIMIT and user.premium_status['is_premium'] == False:
        update.message.reply_text(strings['track_limit'].format(custom_name=custom_name, limit=FREE_PRODUCTS_LIMIT))

    elif user.count_tracked_products() >= PREMIUM_PRODUCTS_LIMIT and user.premium_status['is_premium'] == True:
        update.message.reply_text(strings['track_limit'].format(custom_name=custom_name, limit=PREMIUM_PRODUCTS_LIMIT))
    
    else:

        if url:
            update.message.reply_text(strings['retrieving'].format(custom_name=custom_name), parse_mode='HTML')

            amazon_product = get_amazon_product(url)

            if(amazon_product == None or amazon_product == 'Not Found'):
                update.message.reply_text(strings['product_not_found'].format(custom_name=custom_name))

            elif(amazon_product['condition'] == 'Used'):
                product_ID = amazon_product['ID']
                keyboard = [
                    [
                        InlineKeyboardButton(strings['yes_button'], callback_data=f'track:{product_ID}'),
                    ],
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                update.message.reply_text(strings['tracked_product--used'].format(custom_name=custom_name), reply_markup=reply_markup, parse_mode='HTML')

            else:
                add_product(amazon_product, user)

                product_ID = amazon_product.get('ID')
                product = Product.get_product(product_ID)
                product_data = User.get_user(user_ID).get_product(product_ID)

                print_product(update, context, product, product_data)      
        
        else:
            update.message.reply_text(strings['invalid_link'].format(custom_name=custom_name))



def add_product(amazon_product, user: User):

    product_ID = amazon_product.get('ID')
    product_name = amazon_product.get('name')
    product_url = amazon_product.get('url')
    product_price =	amazon_product.get('price')
    product_merchant = amazon_product.get('merchant')
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

    alert_price = generate_alert_price(product.price)
    product_data = {
        'ID': product.ID,
        'alert_price': alert_price,
        'last_alerted_price': product.price
    }

    user.add_product(product_data)

    return product, product_data



# Function that manages button callbacks
def buttons_callback(update, context):
    
    query = update.callback_query
    query.answer()

    user_ID = str(query.message.chat_id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

    # Analizzare i dati della callback
    action, value = query.data.split(':')
    

    # Delete the item with ID item_id
    if action == 'remove':
        product_ID = value
        product = Product.get_product(product_ID)
        user.remove_product(product_ID)
        query.edit_message_text(strings["remove"].format(product_name=product.name), parse_mode='HTML')

    # Change threshold price of user's product
    elif action == 'threshold':
        product_ID = value
        product = Product.get_product(product_ID)
        change_threshold(update, context, user_ID, product_ID)
        text = strings['change_threshold'].format(product_name=product.name)
        context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')

    elif action == 'chart':
        product_ID = value
        product = Product.get_product(product_ID)
        text = strings['chart'].format(product_name=product.name)
        context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')

        # Crea il grafico e ottieni il buffer
        buf = create_chart(product.history)

        if buf:
            # Invia il grafico come foto
            context.bot.send_photo(chat_id=user_ID, photo=buf)
            # Chiudi il buffer
            buf.close()
        else:
            text = strings['chart_not_available']
            context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')

    elif action == 'track':
        product_ID = value
        context.bot.send_message(chat_id=user_ID, text=strings['retrieving'], parse_mode='HTML')
        amazon_product = get_amazon_product(product_ID, 'New')
        if(amazon_product != None and amazon_product != 'Not Found'):
            product, product_data = add_product(amazon_product, user.ID)

            send_product(context, user_ID, product, product_data)

    elif action == 'premium':
        text = strings['premium_activate'].format(user_ID=user_ID)
        context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')

    elif action == 'personality':
        personality_mode = value

        if( (value == 'merchant_viking') and user.premium_status['is_premium'] == False ):
            text = strings['personality_not_changed']
        else:
            user.update_personality_mode(personality_mode)
            user = User.get_user(user_ID)
            strings = responses[user.language_preference][user.personality_mode]
            text = strings['personality_changed']

        context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')


    else:
        print("button default behavior")



def send_product( context, user_ID, product: Product, product_data):

    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]

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
        reply_markup = InlineKeyboardMarkup(keyboard)
    
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


    try:
        context.bot.send_message(chat_id = user_ID, text=text.format(product_name=product.name, product_price=product.price, product_url=product.url, product_merchant=disable_auto_link(product.merchant), alert_price=alert_price, last_alerted_price=last_alerted_price), reply_markup=reply_markup, parse_mode='HTML')

    except error.TelegramError as e:
        print(f'General error: {e}')



def get_stat(update, context):

    users_count = count_documents_in_collection('users')
    products_count = count_documents_in_collection('products')


    # Send the information to the developer
    dev_text = f"<strong>BOT STATISTICS</strong> 📊 \n\n📦 Products: {products_count}\n\n👥 Users: {users_count}"
    context.bot.send_message(chat_id=DEV_ID, text=dev_text, parse_mode='HTML')



def broadcast_message(update, context, message):

    users = db.collection('users').stream()

    for doc in users:

        user = User.get_user(doc.id)

        try:    
            context.bot.send_message(chat_id=user.ID, text=message, parse_mode='MarkdownV2')
            time.sleep(DELAY)
        
        except error.Unauthorized:
            print(f"User {user.ID} blocked the bot. I'm removing it from the database")
            user.delete()

        except error.TelegramError as e:
            print(f'General error: {e}')


    

# Function to generate a upgrade premium message
def premium(update, context):
    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use first name as the default username

    keyboard = [
            [
                InlineKeyboardButton(strings['premium_button'], callback_data=f'premium:'),
            ],
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(strings['premium'].format(custom_name=custom_name, user_ID=user_ID, free_limit=FREE_PRODUCTS_LIMIT, premium_limit=PREMIUM_PRODUCTS_LIMIT, annual_price=ANNUAL_PRICE, lifetime_price=LIFETIME_PRICE ), reply_markup=reply_markup, parse_mode='HTML')



def set_personality(update, context):
    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()

    strings = responses[user.language_preference][user.personality_mode]
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username



    keyboard = [
            [
                InlineKeyboardButton(strings['robot_friendly'], callback_data=f'personality:robot_friendly'),
            ],
            [
                InlineKeyboardButton(strings['robot_devil'], callback_data=f'personality:robot_devil'),
            ],
            [
                InlineKeyboardButton(strings['merchant_viking'], callback_data=f'personality:merchant_viking'),
            ],
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(strings['choose_personality'], reply_markup=reply_markup)


# Function to generate a upgrade premium message
def share(update, context):
    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use first name as the default username

    share_button = InlineKeyboardButton(
        strings['share_button'], 
        switch_inline_query=strings['share_forward']
    )

    # Crea la tastiera inline
    keyboard = [[share_button]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Invia un messaggio con la tastiera inline
    update.message.reply_text(strings['share'], reply_markup=reply_markup)


# Function to generate a upgrade premium message
def profile(update, context):
    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use first name as the default username

    if user.premium_status['is_premium']:
        # Invia un messaggio con la tastiera inline
        update.message.reply_text(strings['profile_premium'].format(custom_name=custom_name, tracked_products=user.count_tracked_products(), personality_mode=user.personality_mode, language=user.language_preference, premium_type=user.premium_status['type'], premium_expiry=user.premium_status['expiry_date'], limit=PREMIUM_PRODUCTS_LIMIT), parse_mode='HTML')
    else:
        # Invia un messaggio con la tastiera inline
        keyboard = [
            [
                InlineKeyboardButton(strings['premium_button'], callback_data=f'premium:'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(strings['profile'].format(custom_name=custom_name, tracked_products=user.count_tracked_products(), personality_mode=user.personality_mode, language=user.language_preference, limit=FREE_PRODUCTS_LIMIT), reply_markup=reply_markup, parse_mode='HTML')

# Function to generate a upgrade premium message
def version(update, context):
    user_ID = str(update.message.from_user.id)
    user = User.get_user(user_ID)
    if user == None:
        user = User(user_ID)
        user.save()
    strings = responses[user.language_preference][user.personality_mode]
    custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use first name as the default username

    # Invia un messaggio con la tastiera inline
    update.message.reply_text(strings['version'], parse_mode='HTML')




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
    dp.add_handler(CommandHandler('stat', get_stat))
    dp.add_handler(CommandHandler('report', report))
    dp.add_handler(CommandHandler('premium', premium))
    dp.add_handler(CommandHandler('set_personality', set_personality))
    dp.add_handler(CommandHandler('share', share))
    dp.add_handler(CommandHandler('profile', profile))
    dp.add_handler(CommandHandler('version', version))
    dp.add_handler(MessageHandler(Filters.text & Filters.entity("url"), track), group=0)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.entity("url"), input_callback))
    dp.add_handler(CallbackQueryHandler(buttons_callback))

    dp.add_handler(CommandHandler('broadcast_channel_message', start_broadcast))


    # Imposta il fuso orario di Roma
    roma_zone = timezone('Europe/Rome')

    # Orari di esecuzione: 10:00 e 17:00 nel fuso orario di Roma
    orari_esecuzione = [dt_time(10, 0, 0, tzinfo=roma_zone), dt_time(17, 0, 0, tzinfo=roma_zone)]

    # Aggiungi i job alla job queue
    for orario in orari_esecuzione:
        job_queue.run_daily(check_price, orario)
    

    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

