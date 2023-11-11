from config import db, firestore

# Definition of the User class
class User:

    def __init__(self, ID, is_premium = False, language_preference='it', tracked_products={} ):

        self.ID = ID
        self.is_premium = is_premium
        self.tracked_products = tracked_products
        self.language_preference = language_preference


    def __repr__(self):

        return f"User( ID = '{self.ID}', is_premium = {self.is_premium}, language_preference = {self.language_preference} tracked_products = {self.tracked_products} )"
    

    def save(self):

        try:
            user_ref = db.collection('users').document(self.ID)
            user_doc = user_ref.get()

            if not user_doc.exists:

                user_data = {
                    'is_premium': self.is_premium,
                    'language_preference': self.language_preference,
                    'tracked_products': self.tracked_products
                }

                db.collection('users').document(self.ID).set(user_data)
                print(f'The user {self.ID} was successfully added')

            else:
                print(f'The user {self.ID} already exists')

        except Exception as e:
            print(f"Error while save the user: {e}")


    @classmethod
    def from_dict(cls, user_ID, user_data):

        is_premium = user_data.get('is_premium')
        language_preference = user_data.get('language_preference')
        tracked_products = user_data.get('tracked_products')

        return cls(user_ID, is_premium, language_preference, tracked_products )


    @staticmethod
    def get_user(user_ID):

        user_ref = db.collection('users').document(user_ID)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            return User.from_dict(user_ID, user_data)
        else:
            return None
        

    def remove_product(self, product_ID):
        
        # Reference to the user's document
        user_ref = db.collection('users').document(self.ID)

        # Construct the key to remove the product from the dictionary
        product_key = f'tracked_products.{product_ID}'

        # Update to remove the product
        try:
            user_ref.update({product_key: firestore.DELETE_FIELD})
            print(f"Product with ID {product_ID} has been removed from user {self.ID}.")
        except Exception as e:
            print(f"Error while removing the product: {e}")

    
    def add_product(self, product_data):
    
        # Reference to the user's document
        user = User.get_user(self.ID)

        if (not user):
            user = User(self.ID)
            user.save()
        
        # Get product data from the dictionary
        product_ID = product_data.get("ID")
        alert_price = product_data.get("alert_price")
        last_alerted_price = product_data.get("last_alerted_price")

        # Construct the key to remove the product from the dictionary
        product_key = f'tracked_products.{product_ID}'

        try:
            user_ref = db.collection('users').document(user.ID)
            user_ref.update({ product_key: {'last_alerted_price': last_alerted_price, 'alert_price': alert_price} })
            print(f"Product with ID {product_ID} has been added to user {user.ID}.")

        except Exception as e:
            print(f"Error while add the tracked product: {e}")

    def update_price_alert(self, product_ID, new_alert_price):
        # Reference to the user's document
        user_ref = db.collection('users').document(self.ID)

        # Construct the key to remove the product from the dictionary
        product_key = f'tracked_products.{product_ID}.alert_price'

        # Update to remove the product
        try:
            user_ref.update({product_key: new_alert_price})
            print(f"The user {self.ID} changed the price target of product {product_ID} to {new_alert_price}.")
        except Exception as e:
            print(f"Error while changing the price target: {e}")


    def update_tracked_product(self, product_ID, new_alert_price, new_last_alerted_price):
        # Reference to the user's document
        user_ref = db.collection('users').document(self.ID)

        # Aggiorna i campi all'interno del dizionario 'tracked_products'
        update_data = {
            f'tracked_products.{product_ID}.alert_price': new_alert_price,
            f'tracked_products.{product_ID}.last_alerted_price': new_last_alerted_price
        }

        # Update to remove the product
        try:
            user_ref.update(update_data)
            print(f"The user {self.ID} update tracked product {product_ID} with price alert = {new_alert_price} last_alerted_price = {new_last_alerted_price}.")
        except Exception as e:
            print(f"Error while changing tracked product{product_ID} for user {self.IDr}: {e}")






def main():

    print('main')
    user = User('12345', True, 'it', {'BCM000000':{'alert_price': 25, 'last_alerted_price': 28.58}})
    user.save()

    user_2 = User('123458', True, 'it', {'BCM000000':{'alert_price': 25, 'last_alerted_price': 28.58}})
    
    product_data = {
        'ID': 'B456789',
        'alert_price': 62,
        'last_alerted_price': 62
    }

    user_2.add_product(product_data)



if __name__ == '__main__':
    main()


