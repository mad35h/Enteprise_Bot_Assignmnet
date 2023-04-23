from flask import Blueprint, jsonify, request
from sentiment_model import SentimentAnalyzerModel

sentiment_api = Blueprint('sentiment_api', __name__)
model = SentimentAnalyzerModel()

@sentiment_api.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')
    sentiment = model.analyze_sentiment(text)
    return jsonify({'sentiment': sentiment})
