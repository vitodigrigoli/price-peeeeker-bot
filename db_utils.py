from config import db
from datetime import datetime
from user import User
from product import Product
from amazon_utils import get_amazon_product
from toolbox import generate_alert_price, generate_price_history
import time



def users_migration():

    docs = db.collection('user_data').stream()

    print("Users Migration...")

    for doc in docs:
        data = doc.to_dict()

        user_ID = str(data['user_ID'])

        user = User(user_ID)
        user.save()

    print("Users Migration Done!")


def products_migration():
    docs = db.collection('user_data').stream()

    print("Products Migration...")

    for doc in docs:
        data = doc.to_dict()
        product_url = data['product_url']

        amazon_product = get_amazon_product(product_url, 'New')

        if(amazon_product):
            current_date = datetime.now().strftime("%Y-%m-%d")
            product_ID = amazon_product.get('ID'),
            product_name =	amazon_product.get('name'),
            product_url =	amazon_product.get('url'),
            product_price =	amazon_product.get('price'),
            product_merchant =	amazon_product.get('merchant'),
            product_history = generate_price_history(product_price)
            product_history[current_date] = product_price

            product = Product(
                ID = product_ID,
                name = product_name,
                url = product_url,
                price = product_price,
                merchant = product_merchant,
                history = product_history
            )
            
            product.save()
        
    print("Products Migration Done!")


def users_products_migration():

    docs = db.collection('user_data').stream()

    print("Users Products Migration...")
    for doc in docs:
        data = doc.to_dict()

        user_ID = str(data['user_ID'])
        user = User(user_ID)

        amazon_product = get_amazon_product(data['product_url'])

        product_ID = amazon_product['ID']
        product_name = amazon_product['name']
        product_url = amazon_product['url']
        product_price =	amazon_product['price']
        product_merchant = amazon_product['merchant']
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

        alert_price = generate_alert_price(product_price)
        product_data = {
            'ID': product.ID,
            'alert_price': alert_price,
            'last_alerted_price': product_price
        }

        user.add_product(product_data)

    print("Users Products Migration Done!")


def update_products():
    
    docs = db.collection('products').stream()
    count = 0

    for doc in docs:
        count += 1
        data = doc.to_dict()
        
        # update product
        amazon_product = get_amazon_product(data['url'], 'New')

        if(amazon_product == 'Not Found'):
            product = Product.get_product(doc.id)
            product.delete()

        elif(amazon_product):

            new_name = amazon_product['name']
            new_price =	amazon_product['price']
            new_merchant = amazon_product['merchant']
            product = Product(doc.id, new_name, data['url'], new_price, new_merchant, data['history'])

            product.save()
        
        else:
            product = Product.get_product(doc.id)
            product.delete()
        

def clean_products_history():
    docs = db.collection('products').stream()
    
    for doc in docs:
        product = Product.get_product(doc.id)
        product.clean_history(10)


def update_premium_status(user_ID, is_premium, type=None, expiry_date=None):
        # Reference to the user's document
        user_ref = db.collection('users').document(user_ID)

        # Aggiorna i campi all'interno del dizionario 'tracked_products'
        update_data = {
            f'premium_status.is_premium': is_premium,
            f'premium_status.type': type,
            f'premium_status.expiry_date': expiry_date
        }

        # Update to remove the product
        try:
            user_ref.update(update_data)
            print(f"The user {user_ID} update premium_status with is_premium = {is_premium} type = {type} expiry_date = {expiry_date}")
        except Exception as e:
            print(f"Error while updating premium_status for user {user_ID}: {e}")


def count_documents_in_collection(collection_name):
    # Recupera la collezione
    collection_ref = db.collection(collection_name)
    # Recupera i documenti
    documents = collection_ref.stream()
    # Conta i documenti
    doc_count = sum(1 for _ in documents)
    return doc_count

def main():
    users_products_migration()

if __name__ == '__main__':
    main()
