from config import db

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
        




def main():

    print('main')
    user = User('12345', True, 'it', {'BCM000000':{'alert_price': 25, 'last_alerted_price': 28.58}})
    user.save()

    user_2 = User.get_user('12345')
    print(user_2)


if __name__ == '__main__':
    main()


