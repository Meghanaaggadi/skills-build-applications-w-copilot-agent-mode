from flask import Flask, jsonify
import os

app = Flask(__name__)

# Placeholder MongoDB URI from environment variable
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
# TODO: initialize MongoDB client when ready (e.g., motor or pymongo)
# Example with pymongo:
# from pymongo import MongoClient
# client = MongoClient(MONGO_URI)
# db = client['octofit']

@app.route('/')
def hello():
    return jsonify(message='Hello from OctoFit Tracker backend!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Placeholder MongoDB URI from environment variable
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
# TODO: initialize MongoDB client when ready (e.g., motor or pymongo)
# from pymongo import MongoClient
# client = MongoClient(MONGO_URI)

@app.route('/')
def hello():
    return jsonify(message='Hello from OctoFit Tracker!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
