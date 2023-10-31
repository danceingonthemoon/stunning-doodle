from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify, request
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
# Path: stunning-doodle/app.py_object()


base_url = 'https://www.coles.com.au/on-special'
headers = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'})


@app.route('/on-special')
def on_special():
    # Send a GET request to the website
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        print(response.status_code)
    else:
        print('Failed to load page')
        exit()
# Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

# Find all the elements with the class 'product'
    products = soup.find_all('h2', class_='product__title')
    products_price = soup.find_all(
        'div', class_='price')

    product_data = []
# Loop through the elements and print them out
    for product, price in zip(products, products_price):
        # print(f"{product.text.strip()} -- Price: {price.text.strip()}")
        product_data.append({
            'product_name': product.text.strip(),
            'price': price.text.strip(),
        })

    return json.dumps(product_data)


@app.route('/categories')
def get_categories():
    url = 'https://www.coles.com.au/browse'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.find_all('a', attrs={
            'class': 'sc-ac926323-0 kOgghk coles-targeting-ShopCategoriesShopCategoryStyledCategoryContainer'})
        category_data = []
        for category in categories:
            category_data.append({
                'category_name': category.text.strip(),
                'category_url': 'https://www.coles.com.au' + category['href'],
            })
        return json.dumps(category_data)

    else:
        print('Failed to load page')
        exit()


if __name__ == '__main__':
    app.run(debug=True)
