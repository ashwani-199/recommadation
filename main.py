from flask import Flask, jsonify, render_template
from common_model.mainservice import getProduct, getProductUrl, getRetailPrice


app = Flask(__name__)
port = 5100
 

@app.route('/')
def index():
    get_product = getProduct()
    product = []
    for prod in get_product:
        product.append(prod)

    return jsonify(product)



if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host="0.0.0.0", port=port)