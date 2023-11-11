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
        new_name = amazon_product['name']
        new_price =	amazon_product['price']
        new_merchant = amazon_product['merchant']
        product = Product(doc.id, new_name, data['url'], new_price, new_merchant, data['history'])

        product.save()

        if(data['price'] == None and product.price != None):
            print(f'Il prodotto {product.ID} è tornato disponibile')

        elif(product.price < data['price']):
            print(f'Il prodotto {product.ID} si è abbassato di prezzo')
        


'''


# Function that adds a tracked product to the users collection
def add_tracked_product(user_ID, product_ID, price, alert_price):
    
    # Reference to the user's document
    user_ref = db.collection('users').document(user_ID)

    # Construct the key to remove the product from the dictionary
    product_key = f'tracked_products.{product_ID}'

    try:
        user_ref.update({ product_key: {'last_alerted_price': price, 'alert_price': alert_price} })
        print(f"Product with ID {product_ID} has been added to user {user_ID}.")

    except Exception as e:
        print(f"Error while add the tracked product: {e}")


# Function that removes a product from the users collection
def delete_user(user_ID):

    ref_user = db.collection('users').document(user_ID)
    doc = ref_user.get()

    if doc.exists:
        ref_user.delete()
        print(f'The user {user_ID} was successfully removed')
    else:
        print(f'The user {user_ID} was not found')


# Function that removes a product from the products collection
def delete_product(product_ID):
    ref_user = db.collection('products').document(product_ID)
    doc = ref_user.get()

    if doc.exists:
        ref_user.delete()
        print(f'The product {product_ID} was successfully removed')
    else:
        print(f'The product {product_ID} was not found')


# Function that removes a tracked product from the user
def delete_tracked_product(user_ID, product_ID):

    # Reference to the user's document
    user_ref = db.collection('users').document(user_ID)

    # Construct the key to remove the product from the dictionary
    product_key = f'tracked_products.{product_ID}'

    # Update to remove the product
    try:
        user_ref.update({product_key: firestore.DELETE_FIELD})
        print(f"Product with ID {product_ID} has been removed from user {user_ID}.")
    except Exception as e:
        print(f"Error while removing the product: {e}")


# Function that gets a product from products collection
def get_product(product_ID):
     # Reference to the products' document
    product_ref = db.collection('products').document(product_ID)

    product_doc = product_ref.get()

    if product_doc.exists:

        product_data = product_doc.to_dict()
        print(product_data)
        return product_data

    else:
        print("Product not found")


# Function that gets a tracked products from users collection
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


# Function that gets a tracked products from users collection
def get_tracked_product(user_ID, product_ID):

    # Reference to the user's document
    user_ref = db.collection('users').document(user_ID)

    user_doc = user_ref.get()

    if user_doc.exists:

        user_data = user_doc.to_dict()
        print(user_data)
        tracked_products = user_data.get('tracked_products', {})

        product_info = tracked_products.get(product_ID)

        if product_info:
            print(product_info)
            return product_info
        else:
            print(f"Product with ID {product_ID} not found for User {user_ID}.")
            return None

    else:
        print("User not found")


def set_alert_price(user_ID, product_ID, alert_price):
    # Reference to the user's document
    user_ref = db.collection('users').document(user_ID)

    # Construct the key to remove the product from the dictionary
    product_key = f'tracked_products.{product_ID}.alert_price'

    # Update to remove the product
    try:
        user_ref.update({product_key: alert_price})
        print(f"The user {user_ID} changed the price target of product {product_ID} to {alert_price}.")
    except Exception as e:
        print(f"Error while changing the price target: {e}")
    

def generate_alert_price(price):

    if (price < 100):
        alert_price = round( price - price / 100 * 5, 2)
    else:
        alert_price = round( price - price / 100 * 2, 2)

    return alert_price







'''

def main():
    check_price()

if __name__ == '__main__':
    main()
