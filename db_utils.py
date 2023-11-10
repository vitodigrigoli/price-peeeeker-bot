from config import db
from datetime import datetime
from user import User
from product import Product
from amazon_utils import get_amazon_product
from toolbox import generate_alert_price


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
        
        
    print("Products Migration Done!")


def users_products_migration():

    docs = db.collection('user_data').stream()

    print("Users Products Migration...")
    for doc in docs:
        data = doc.to_dict()

        user_ID = str(data['user_ID'])
        user = User(user_ID)

        current_date = datetime.now().strftime("%Y-%m-%d")
        amazon_product = get_amazon_product(data['product_url'])

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

        alert_price = generate_alert_price(product.price)
        product_data = {
            'ID': product.ID,
            'alert_price': alert_price,
            'last_alerted_price': product.price
        }

        print(product_data)
        user.add_product(product_data)

    print("Users Products Migration Done!")

def migration():
    users_migration()
    products_migration()
    users_products_migration()


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
    users_products_migration()

if __name__ == '__main__':
    main()
