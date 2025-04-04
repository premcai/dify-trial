from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
uri = "mongodb+srv://myapp_user:secureTest123@pii-dify.4inrrqu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["dify_demo"]
collection = db["users"]

@app.route("/")
def home():
    return "✅ Flask API is running!"

@app.route("/get-data", methods=["GET"])
def get_data():
    data = list(collection.find({}, {"_id": 0}))  # exclude _id for simplicity
    return jsonify(data)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

