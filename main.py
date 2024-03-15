from flask import Flask, jsonify, render_template
from common_model.mainservice import getProduct, getProductUrl, getRetailPrice


app = Flask(__name__)
port = 5100
 

@app.route('/')
def index():
    get_product = getProduct()
    get_product_url = getProductUrl()
    get_retail_price = getRetailPrice()
    context = {
        'get_product': get_product,
        'get_product_url': get_product_url,
        'get_retail_price': get_retail_price
    }
    return render_template('index.html', data=context)



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=port)