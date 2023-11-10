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


import time
from translations import it_strings, en_strings
from functools import wraps
from datetime import datetime

from amazon_utils import extract_amazon_link, get_amazon_product, generate_add_to_cart_link
from toolbox import generate_alert_price, time_converter, create_chart

from product import Product
from user import User
from config import DEV_ID, BOT_TOKEN


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


# Function that generates a help message
def help(update, context):
	strings = it_strings
	custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

	commands = "\n".join([f"🔹 /{command} - <em>{description}</em>\n" for command, description in strings["commands"].items()])
	update.message.reply_text(strings["help"].format(custom_name=custom_name) + commands, parse_mode='HTML', disable_web_page_preview=True)


# Function to send an Amazon affiliate link
def track (update, context):

	user_ID = str(update.message.from_user.id)
	strings = it_strings
	custom_name = context.user_data.get('custom_name', update.message.from_user.first_name)  # Use empty string as the default username

	# Find URL in message
	message = update.message.text
	url = extract_amazon_link(message)

	if url:
		update.message.reply_text(strings['retrieving '].format(custom_name=custom_name), parse_mode='HTML')
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
			current_date = datetime.now().strftime("%Y-%m-%d")
			product = Product(
				amazon_product.get('ID'),
				amazon_product.get('name'),
				amazon_product.get('url'),
				amazon_product.get('price'),
				amazon_product.get('merchant'),
				{
					current_date: amazon_product.get('price')
				}
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

			print(f"ID: {product_ID} alert: {product_data.get('alert_price')}")
			print_product(update, context, product, product_data)
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
	update.message.reply_text(text.format(name=product.name, price=product.price, url=product.url, alert_price=alert_price, last_alerted_price=last_alerted_price), reply_markup=reply_markup, parse_mode='HTML')


def change_threshold(update, context, user_ID, product_ID):

	context.user_data['set_alert_price'] = True
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
			product = Product.get_product(product_ID)
			user = User.get_user(user_ID)

			if(product != None):
				if( new_alert_price < product.price):
					user.update_price_alert(product_ID, new_alert_price)
					update.message.reply_text('Soglia cambiata con successo')
					context.user_data['set_alert_price'] = False
				else:
					update.message.reply_text(f"Il valore della soglia deve essere minore del prezzo attuale di {product.price}.")

		except Exception as e:
			print(f"Error while entering the new price target: {e}")
			update.message.reply_text('Il valore inserito non è valido. Inserisci un valore numerico.')

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

	# Delete the item with ID item_id
	if action == 'remove':
		user.remove_product(product_ID)
		query.edit_message_text(strings["remove"])

	# Change threshold price of user's product
	elif action == 'threshold':

		change_threshold(update, context, user_ID, product_ID)
		text = strings['change_threshold']
		context.bot.send_message(chat_id=user_ID, text=text)

	elif action == 'chart':
		text = strings['chart']
		context.bot.send_message(chat_id=user_ID, text=text, parse_mode='HTML')
		product = Product.get_product(product_ID)
		graph_path = create_chart(product.history)  # Assumi che 'history_data' sia il tuo dizionario
		context.bot.send_photo(chat_id=user_ID, photo=open(graph_path, 'rb'))

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
	dp.add_handler(CommandHandler('set_username', set_username), group=1)
	dp.add_handler(CommandHandler('coffee', coffee))
	dp.add_handler(CommandHandler('dev', get_stat))
	dp.add_handler(CommandHandler('report', report))
	dp.add_handler(MessageHandler(Filters.text & Filters.entity("url"), track), group=0)
	dp.add_handler(MessageHandler(Filters.text & ~Filters.command & ~Filters.entity("url"), input_callback))
	dp.add_handler(CallbackQueryHandler(buttons_callback))


	# Add a job to check the price every 6 hours
	#job_queue.run_repeating(check_price, interval=21600, first=0)
	
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()

