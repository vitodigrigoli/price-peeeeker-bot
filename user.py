from config import db, firestore
from toolbox import generate_expiry_date

# Definition of the User class
class User:

    def __init__(self, ID, premium_status = {'is_premium': False, 'type': None, 'expiry_date': None}, language_preference='it', personality_mode='robot_friendly', tracked_products={} ):

        self.ID = ID
        self.premium_status = premium_status
        self.language_preference = language_preference
        self.personality_mode = personality_mode
        self.tracked_products = tracked_products


    def __repr__(self):

        return f"User( ID = '{self.ID}', premium_status = {self.premium_status}, language_preference = {self.language_preference}, personality_mode = {self.personality_mode}, tracked_products = {self.tracked_products} )"
    

    def save(self):

        try:
            user_ref = db.collection('users').document(self.ID)
            user_doc = user_ref.get()

            if not user_doc.exists:

                user_data = {
                    'premium_status': self.premium_status,
                    'language_preference': self.language_preference,
                    'personality_mode': self.personality_mode,
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

        premium_status = user_data.get('premium_status')
        language_preference = user_data.get('language_preference')
        personality_mode = user_data.get('personality_mode')
        tracked_products = user_data.get('tracked_products')

        return cls(user_ID, premium_status, language_preference, personality_mode, tracked_products )


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


    # Function that removes a product from the users collection
    def delete(self):

        user_ref = db.collection('users').document(self.ID)
        doc = user_ref.get()

        if doc.exists:
            user_ref.delete()
            print(f'The user {self.ID} was successfully removed')
        else:
            print(f'The user {self.ID} was not found')


    def get_product(self, product_ID):
        user_ref = db.collection('users').document(self.ID)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            tracked_product = user_data['tracked_products'][product_ID]

            product_data = {
                'ID': product_ID,
                'alert_price': tracked_product['alert_price'],
                'last_alerted_price': tracked_product['last_alerted_price']
            }

            return product_data

        else:
            return None
        
    
    def count_tracked_products(self):
        return len(self.tracked_products)

   
    def update_premium_status(self, type=None):
        # Reference to the user's document
        user_ref = db.collection('users').document(self.ID)

        if type == 'trial':
            is_premium = True
            expiry_date = generate_expiry_date('months', 3)

        elif type == 'annual':
            is_premium = True
            expiry_date = generate_expiry_date('years', 1)

        elif type == 'lifetime':
            is_premium = True
            expiry_date = None

        else:
            is_premium = False
            expiry_date = None


        # Aggiorna i campi all'interno del dizionario 'tracked_products'
        update_data = {
            f'premium_status.is_premium': is_premium,
            f'premium_status.type': type,
            f'premium_status.expiry_date': expiry_date
        }

        # Update to remove the product
        try:
            user_ref.update(update_data)
            print(f"The user {self.ID} update premium_status with is_premium = {is_premium} type = {type} expiry_date = {expiry_date}")
        except Exception as e:
            print(f"Error while updating premium_status for user {self.ID}: {e}")


    def update_personality_mode(self, personality_mode):
        # Reference to the user's document
        user_ref = db.collection('users').document(self.ID)

        # Aggiorna i campi all'interno del dizionario 'tracked_products'
        update_data = {
            f'personality_mode': personality_mode,
        }

        # Update to remove the product
        try:
            user_ref.update(update_data)
            print(f"The user {self.ID} update personality_mode with {personality_mode}")
        except Exception as e:
            print(f"Error while updating personality_mode for user {self.ID}: {e}")


def main():

    user = User.get_user('37104959')

    user.update_premium_status('lifetime')





if __name__ == '__main__':
    main()


