from textblob import TextBlob

class SentimentAnalyzerModel:
    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        return sentiment
