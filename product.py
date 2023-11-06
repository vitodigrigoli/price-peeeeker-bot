# Definition of the Product class
class Product:
    def __init__(self, ID='XXXXXXXXXX', name='Default Name', url='https://default.url', price=0, history={} ):
        self.ID = ID
        self.name = name
        self.url = url
        self.price = price
        self.history = history


    def __repr__(self):
        return f"Product(ID='{self.ID}', name={self.name}, url='{self.url}', price={self.price}, history={self.history})"
