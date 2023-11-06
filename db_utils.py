import os
import firebase_admin
from firebase_admin import credentials, firestore
import json
from product import Product
from user import User
from datetime import datetime


# Get enviroment variables
FIREBASE_CREDENTIALS_JSON = os.environ.get('FIREBASE_CREDENTIALS_JSON')

# Initialization Firestore DB
cred_dict = json.loads(FIREBASE_CREDENTIALS_JSON)
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)
db = firestore.client()



def users_migration():

    docs = db.collection('user_data').stream()

    print("Users Migration...")

    for doc in docs:
        data = doc.to_dict()

        user_ID = str(data['user_ID'])
        user_ref = db.collection('users').document(user_ID)

        user_doc = user_ref.get()

        if user_doc.exists:
            print(f"Il documento per l'utente {user_ID} esiste già.")
        else:
            # Il documento non esiste, quindi crealo
            user_data = {
                'is_premium': True,
                'tracked_products': {}
            }
            user_ref.set(user_data)
            print(f"Documento creato per l'utente {user_ID} con dati premium e tracked_products.")

    print("Users Migration Done!")


def products_migration():
    docs = db.collection('user_data').stream()

    print("Products Migration...")

    for doc in docs:
        data = doc.to_dict()

        product_asin = data['product_asin']
        product_ref = db.collection('products').document(product_asin)

        product_doc = product_ref.get()
        current_date = datetime.now().strftime("%Y-%m-%d")

        if product_doc.exists:
            print(f"Il documento per il prodotto {product_asin} esiste già.")
        else:
            # Il documento non esiste, quindi crealo
            product_data = {
                'name':  data['product_name'],
                'url': data['product_url'],
                'price': data['product_price'],
                'history': [
                    {
                        'date': current_date,
                        'price': data['product_price'] 
                    }
                ]
            }

            product_ref.set(product_data)
            print(f"Documento creato per il prodotto {product_asin}.")
        
    print("Products Migration Done!")


def users_products_migration():

    docs = db.collection('user_data').stream()

    print("Users Products Migration...")
    for doc in docs:
        data = doc.to_dict()

        user_ID = str(data['user_ID'])
        user_ref = db.collection('users').document(user_ID)

        product_ID = data['product_asin']
        ref_product_ID = db.collection('products').document(product_ID)

        if (data['product_price'] < 100):
            target_price = round( data['product_price'] - data['product_price'] / 100 * 5, 2)
        else:
            target_price = round( data['product_price'] - data['product_price'] / 100 * 2, 2)

        product_key = f'tracked_products.{product_ID}'
        user_ref.update({
            product_key: target_price
        })

    print("Users Products Migration Done!")



# Function that adds a user to the users collection
def add_user(user_ID):

    ref_user = db.collection('users').document(user_ID)
    doc = ref_user.get()

    if not doc.exists:
        ref_user.set({
            'tracked_products':  {},
            'is_premium': False
            })
        print(f'The user {user_ID} was successfully added')
    else:
        print(f'The user {user_ID} already exists')


# Function that adds a product to the products colectione
def add_product(product: Product):
    product_ref = db.collection('products').document(product.ID)
    doc = product_ref.get()

    if not doc.exists:
        product_ref.set({
            'name': product.name,
            'url': product.url,
            'price':  product.price,
            'history': product.history
        })
        print(f'The product {product.ID} was successfully added')

    else:
        print(f'The product {product.ID} already exists')


def add_tracked_product(user_ID, product_ID, target_price):
    
    # Reference to the user's document
    user_ref = db.collection('users').document(user_ID)

    # Construct the key to remove the product from the dictionary
    product_key = f'tracked_products.{product_ID}'

    try:
        user_ref.update({ product_key: target_price })
        print(f"Product with ID {product_ID} has been added to user {user_ID}.")

    except Exception as e:
        print(f"Error while add the tracked product: {e}")

# Function that remove a product from the users collection
def delete_user(user_ID):

    ref_user = db.collection('users').document(user_ID)
    doc = ref_user.get()

    if doc.exists:
        ref_user.delete()
        print(f'The user {user_ID} was successfully removed')
    else:
        print(f'The user {user_ID} was not found')


# Function that remove a product from the products collection
def delete_product(product_ID):
    ref_user = db.collection('products').document(product_ID)
    doc = ref_user.get()

    if doc.exists:
        ref_user.delete()
        print(f'The product {product_ID} was successfully removed')
    else:
        print(f'The product {product_ID} was not found')

# Function that remove a tracked product from the user
def delete_tracked_product(user_ID, product_ID):

    # Reference to the user's document
    user_ref = db.collection('users').document(user_ID)

    # Construct the key to remove the product from the dictionary
    product_key = f'tracked_products.{product_ID}'

     # Update to remove the product
    try:
        user_ref.update({product_key: firestore.DELETE_FIELD})
        print(f"Product with ID {product_ID} removed from user {user_ID}.")
    except Exception as e:
        print(f"Error while removing the product: {e}")


def get_product(product_ID):
     # Reference to the products' document
    product_ref = db.collection('products').document(product_ID)

    product_doc = product_ref.get()

    if product_doc.exists:

        product_data = product_doc.to_dict()

        return product_data

    else:
        print("Product not found")


def get_tracked_products(user_ID):

    # Reference to the user's document
    user_ref = db.collection('users').document(user_ID)

    user_doc = user_ref.get()

    if user_doc.exists:

        user_data = user_doc.to_dict()
        tracked_products = user_data.get('tracked_products', {})
        print("Tracked Products:", tracked_products)

        return tracked_products

    else:
        print("User not found")














def main():

    pass


if __name__ == '__main__':
    main()
