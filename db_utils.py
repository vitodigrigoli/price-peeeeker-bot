import os
import firebase_admin
from firebase_admin import credentials, firestore
import json
from product import Product
from user import User


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
                        'date': '2023-11-05',
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



# Function that adds a user to the user collection
def add_user(user: User):
    doc_ref = db.collection('users').document(user.ID)

    doc_ref.set({
        'tracked_products':  user.tracked_products,
        'is_premium': user.is_premium
    })


# Function that adds a product to the database
def add_product(product: Product):
    doc_ref = db.collection('products').document(product.ID)

    doc_ref.set({
        'name': product.name,
        'url': product.url,
        'price':  product.price,
        'history': product.history
    })

def delete_user(user_ID):

    ref_user = db.collection('users').document(user_ID)
    doc = ref_user.get()

    if doc.exists:
        ref_user.delete()
        print(f'The user {user_ID} was successfully removed')
    else:
        print(f'The user {user_ID} was not found')


def delete_product(product_ID):
    ref_user = db.collection('products').document(product_ID)
    doc = ref_user.get()

    if doc.exists:
        ref_user.delete()
        print(f'The product {product_ID} was successfully removed')
    else:
        print(f'The product {product_ID} was not found')


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



def main():


    delete_tracked_product('37104959', '123456789')


if __name__ == '__main__':
    main()
