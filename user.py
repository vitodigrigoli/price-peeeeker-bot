# Definition of the User class
class User:
    def __init__(self, ID = 'XXXXXXXXXX', tracked_products = [], is_premium = False):
        self.ID = ID
        self.tracked_products = tracked_products
        self.is_premium = is_premium


    def __repr__(self):
        return f"User( user_ID = '{self.ID}', tracked_product = {self.tracked_products}, premium = {self.is_premium} )"
