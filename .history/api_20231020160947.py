 import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Define the API endpoint and HTTP method
@app.route('/get_price', methods=['GET'])
def get_price():
    # Get the name of the shopping item from the request parameters
    item_name = request.args.get('item_name')

    # Call a function to get the price of the shopping item
    price = get_item_price(item_name)

    # Return the price in JSON format
    return jsonify({'price': price})

# Function to get the price of a shopping item
def get_item_price(item_name):
    # Send GET requests to Aldi and Coles websites with item_name as query parameter
    aldi_url = f'https://www.aldi.com.au/en/groceries/{item_name}/'
    coles_url = f'https://shop.coles.com.au/a/national/everything/search/{item_name}'
    aldi_response = requests.get(aldi_url)
    coles_response = requests.get(coles_url)

    # Parse the HTML response and extract the price information
    aldi_soup = BeautifulSoup(aldi_response.content, 'html.parser')
    coles_soup = BeautifulSoup(coles_response.content, 'html.parser')
    aldi_price = aldi_soup.find('span', {'class': 'product-price__value'})
    coles_price = coles_soup.find('span', {'class': 'value'})
    if aldi_price:
        price = float(aldi_price.text.strip('$'))
    elif coles_price:
        price = float(coles_price.text.strip('$'))
    else:
        price = None

    return price

if __name__ == '__main__':
    app.run(debug=True)