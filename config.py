import firebase_admin
from firebase_admin import credentials, firestore
from amazon_paapi import AmazonApi
import os
import json

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

# Create an Amazon instance
amazon = AmazonApi(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, AMAZON_COUNTRY, throttling=2)

# Constant
FREE_PRODUCTS_LIMIT = 30
PREMIUM_PRODUCTS_LIMIT = 100

ANNUAL_PRICE = 19.99
LIFETIME_PRICE = 49.99

DELAY = 0.5


