import requests
import re
from config import amazon, AMAZON_ASSOC_TAG
import amazon_paapi 



# Function that generates a link to add a product directly to the cart
def generate_add_to_cart_link(asin):
    url = f'https://www.amazon.it/gp/aws/cart/add.html?ASIN.1={asin}&Quantity.1=1&AssociateTag={AMAZON_ASSOC_TAG}'
    return url


# Function that returns the full link from a short link.
def get_full_url_from_shortlink(shortlink):
    response = requests.get(shortlink, allow_redirects=True)
    return response.url


# Function to extract a link within a message
def extract_amazon_link(text):
    # Cerca link Amazon standard e shortlinks
    regex = r'(https?://(?:www\.amazon\.[a-zA-Z]{2,3}/.+|amzn\.[a-zA-Z]{2,3}/.+))'

    try:
        link = re.findall(regex, text)[0]

        # Se non ci sono link, ritorna None
        if not link:
            link = None

        # Controlla se il link è uno shortlink
        if 'amzn' in link:
            link = get_full_url_from_shortlink(link)
        
    except:
        return None

    return link


# Function to get Amazon product info
def get_amazon_product(url, condition='Any'):

    try:
        product = amazon.get_items(url, condition)[0]

    except amazon_paapi.errors.exceptions.ItemsNotFound as e:
        print("ItemsNotFound:", e)
        product_condition = 'Not Found'
        return {
            'condition': product_condition
        }

    except Exception as e:
        print(f"Error while fetching Amazon product: {e}")
        product_condition = None
        return {
            'condition': product_condition
        }
    
    product_ID = product.asin
    product_name = product.item_info.title.display_value
    product_url = product.detail_page_url

    try:
        product_price = float(product.offers.listings[0].price.amount)

    except Exception as e:
        print(f"Product not available: {e}")

        product_price = None
        product_merchant = None
        product_condition = 'Not Available'

        return {
            'ID': product_ID,
            'name': product_name,
            'url': product_url,
            'price': product_price,
            'merchant': product_merchant,
            'condition': product_condition
        }
    

    product_condition = product.offers.listings[0].condition.value
    product_merchant = product.offers.listings[0].merchant_info.name

    amazon_product = {
        'ID': product_ID,
        'name': product_name,
        'url': product_url,
        'price': product_price,
        'merchant': product_merchant,
        'condition': product_condition
    }

    return amazon_product



# Function to get Amazon product info
def print_amazon_product(url, condition='Used'):
    
    products = amazon.get_items(url, condition)

    for product in products:
        for listing in product.offers.listings:
            if listing.merchant_info:
                print(f'{listing.merchant_info.name}\n')





def main():

    url='https://www.amazon.it/dp/B0BDKJ4WWC?tag=price-peeker-21&linkCode=ogi&th=1&psc=1'
    amazon_product = get_amazon_product('B0BDKJ4WWC', 'New')
    print(amazon_product)

    

    

if __name__ == '__main__':
    main()


    