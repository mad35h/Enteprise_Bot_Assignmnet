from flask import Flask
from sentiment_api import sentiment_api

app = Flask(__name__)
app.register_blueprint(sentiment_api)

if __name__ == '__main__':
    app.run()
