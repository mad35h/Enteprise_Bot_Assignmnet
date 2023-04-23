from flask import Flask, jsonify, request
from review_retrievel import ReviewRetrievalModel

app = Flask(__name__)
model = ReviewRetrievalModel()

@app.route('/reviews', methods=['GET'])
def get_reviews():
    color = request.args.get('color')
    storage_size = request.args.get('storage_size')
    rating = request.args.get('rating')
    
    reviews = model.get_reviews(color, storage_size, rating)
    
    return jsonify({'reviews': reviews})

if __name__ == '__main__':
    app.run()
