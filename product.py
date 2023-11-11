from config import db
from datetime import datetime


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
                # update field
                current_date = datetime.now().strftime('%Y-%m-%d')
                history_key = f'history.{current_date}'
                print(f'The product {self.ID} already exists. Update the price to {self.price}')
                product_ref.update({
                    'price':  self.price,
                    'merchant': self.merchant,
                    history_key: self.price
                })



        except Exception as e:
            print(f"Error while save the product: {e}")
        
    @classmethod
    def from_dict(cls, product_ID, product_data):

        name = product_data.get('name')
        url = product_data.get('url')
        price = product_data.get('price')
        merchant = product_data.get('merchant')
        history = product_data.get('history')

        return cls(product_ID, name, url, price, merchant, history)


    @staticmethod
    def get_product(product_ID):

        product_ref = db.collection('products').document(product_ID)
        product_doc = product_ref.get()

        if product_doc.exists:
            product_data = product_doc.to_dict()
            return Product.from_dict(product_ID, product_data)
        else:
            return None
        

        
        

def main():

    product = Product.get_product('B0BZJM3742')
    print(product)


if __name__ == '__main__':
    main()


