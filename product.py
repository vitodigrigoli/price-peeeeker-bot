from config import db


# Definition of the Product class
class Product:

    def __init__(self, ID, name, url, price, merchant , history={} ):
        self.ID = ID
        self.name = name
        self.url = url
        self.price = price
        self.merchant = merchant
        self.history = history


    def __repr__(self):
        return f"Product(ID='{self.ID}', name={self.name}, url='{self.url}', price={self.price}, merchant={self.merchant}, history={self.history})"
    

    def save(self):

        try:
            product_ref = db.collection('products').document(self.ID)
            product_doc = product_ref.get()

            if not product_doc.exists:

                product_data = {
                    'name': self.name,
                    'url': self.url,
                    'price': self.price,
                    'merchant': self.merchant,
                    'history': self.history
                }

                db.collection('products').document(self.ID).set(product_data)
                print(f'The product {self.ID} was successfully added')

            else:
                print(f'The product {self.ID} already exists')

        except Exception as e:
            print(f"Error while save the user: {e}")
        

        

