import logging
import os
from flask import Flask
from waitress import serve

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info("Received request on /")
    return "Hello, World!"

@app.route('/health')
def health():
    logger.info("Received request on /health")
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting server on port {port}")
    serve(app, host="0.0.0.0", port=port)