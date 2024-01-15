from flask import Flask, request, jsonify
from config import Config
import os
import json

# app = Flask(__name__)
metricsLocal = Flask(__name__)
metricsLocal.config.from_object(Config)

# TODO: add authentication
# SECRET_KEY = 'your-secret-key'
# app.config['SECRET_KEY'] = SECRET_KEY

# Error handler for 404 page not found
@metricsLocal.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404


@metricsLocal.route("/countly", methods=['POST'])
def countly_endpoint():
    
    metrics = request.get_json()

    if not metrics:
        return jsonify(error="No data provided"), 400

    # Process metrics here (e.g., validate data, transform, etc.)

    save_metrics(metrics)

    return jsonify(success=True), 200

def save_metrics(metrics_data):
    file_path = os.path.join(os.path.dirname(__file__), "data/metrics.json")

    with open(file_path, 'w') as file:
        json.dump(metrics_data, file)


if __name__ == "__main__":
    metricsLocal.run(host='0.0.0.0', port=80)
