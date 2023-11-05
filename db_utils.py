import os
import firebase_admin
from firebase_admin import credentials, firestore
import json
from product import Product


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
                'premium': True,
                'tracked_products': []
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
                'product_name':  data['product_name'],
                'product_url': data['product_url'],
                'product_current_price': data['product_price'],
                'product_min_price': data['product_price'],
                'product_max_price': data['product_price'],
                'product_history': [
                    {
                        'date': '2023-11-05',
                        'price': data['product_price'] 
                    }
                ]
            }

            product_ref.set(product_data)
            print(f"Documento creato per il prodotto {product_asin} con dati premium e tracked_products.")
        
    print("Products Migration Done!")


def users_products_migration():

    docs = db.collection('user_data').stream()

    print("Users Products Migration...")
    for doc in docs:
        data = doc.to_dict()

        user_ID = str(data['user_ID'])
        user_ref = db.collection('users').document(user_ID)

        user_ref.update({
            'tracked_products': firestore.ArrayUnion([data['product_asin']])
        })

    print("Users Products Migration Done!")





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











def main():

    print("Refactoring DB...")

    users_migration()
    products_migration()
    users_products_migration()

    print("Refactoring DB done!")



if __name__ == '__main__':
    main()
