## Common Loot Ordering System
# This webserver allows users to place orders for Common Loot Mystery Boxes.
# It also serves the Home page

## Setup
# 1. System Imports
# 2. Logging
# 3. Load Arguements and Config
# 4. Modules
# 5. Flask
# 6. Start server

# 1. System Imports
import os, sys, time, json
from datetime import datetime

# 2. Logging
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 3. Load Arguments and Config
import argparse
parser = argparse.ArgumentParser(description='Common Loot Ordering System')
parser.add_argument('--config', default='config.json', help='Path to the config file')
parser.add_argument('--port', type=int, default=5000, help='Port to run the server on')
args = parser.parse_args()

if not os.environ.get("DOCKER", "false") == "true": logging.warning("Running outside of a Docker container, this is not recommended.")

from modules.config import Config
config = Config(args.config)

# 4. Modules
from modules.db import Database
db = Database(
    dbname='common_loot',
    user=config.config['db_user'],
    password=config.config['db_password'],
    host=config.config['db_host'],
    port=config.config['db_port'],
    init_tables=True
)

# 5. Flask
from flask import Flask, request, jsonify, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = config.config['app_secret_key']

@app.route('/')
def index():
    return render_template('index.html') # render homepage

@app.route("/order")
def orderflow():
    render_template("order.html", products=None) # todo: setup products

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/track/<order_id>")
def track_order(order_id):
    pass

## API
@app.route("/api/order", methods=["POST"])
def api_order():
    pass

# 6. Start server
if __name__ == "__main__":
    logging.info(f"Starting server on port {args.port}")
    app.run(host="0.0.0.0", port=args.port)
else:
    logging.error("This script is not meant to be imported as a module. Exiting.")
    sys.exit(1)