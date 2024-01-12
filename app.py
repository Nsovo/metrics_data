from flask import Flask, request, jsonify
from config import Config
import os
import json

app = Flask(__name__)
app.config.from_object(Config)

# TODO: add authentication
# SECRET_KEY = 'your-secret-key'
# app.config['SECRET_KEY'] = SECRET_KEY

# Error handler for 404 page not found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

# Endpoint for receiving metrics and saving them to a file
@app.route("/countly", methods=['POST'])
def countly_endpoint():

    # if request.headers.get('X-Secret-Key') != SECRET_KEY:
    #     abort(401)  # Unauthorized

    metrics = request.get_json()

    # This path should point to there there usb stick is mounted
    path = os.path.join(os.path.dirname(__file__), "data/metrics.json")

    with open(path, 'w') as f:
        json.dump(metrics, f)

    return jsonify(success=True), 200

# Default route
@app.route("/")
def index():
    return "Imagine Worldwide!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
