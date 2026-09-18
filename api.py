from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/products", methods=["GET"])
def get_products():
    with open("Product.json", "r") as f:
        products = json.load(f)
    return jsonify(products)

@app.route("/api/policies", methods=["GET"])
def get_policies():
    with open("policy.json", "r",encoding="utf-8") as f:
        policies = json.load(f)
    return jsonify(policies)

if __name__ == "__main__":
    app.run(port=5000, debug=True)




