from flask import Flask, jsonify
from recommender import get_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Product Recommendation API. Use /recommend/<product_name> to get recommendations."

@app.route('/recommend/<string:product>', methods=['GET'])
def recommend(product):
    recommendations = get_recommendations(product)
    if not recommendations:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({
        "input": product,
        "recommendations": recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)
