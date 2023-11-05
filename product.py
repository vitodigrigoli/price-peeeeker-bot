# Definition of the Product class
class Product:
    def __init__(self, name="Default Name", asin='XXXXXXXXXX', price=0, url="https://default.url", user_ID='XXXXXXXXXX', doc_ID='XXXXXXXXXX'):
        self.name = name
        self.asin = asin
        self.url = url
        self.price = price
        self.user_ID = user_ID
        self.doc_ID = doc_ID


    def __repr__(self):
        return f"Product(name='{self.name}', asin={self.asin}, prezzo={self.price}, url='{self.url}', user_ID={self.user_ID}, doc_ID={self.doc_ID})"
