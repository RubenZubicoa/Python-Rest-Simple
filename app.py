from products import products
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/products')
def getProducts():
    return jsonify(products)


@app.route('/products/<string:product_name>')
def getOne(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify(productFound)
    return jsonify({"Message":"Error"})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = request.json
    products.append(new_product[0])
    return jsonify(products)




if __name__ == '__main__':
    app.run(debug=True, port=4000)
