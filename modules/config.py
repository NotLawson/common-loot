## Config Module
# This module handles the configuration settings for the application.
import json
import sys, os
import logging

# Start logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Config:
    def __init__(self, config_file):
        try:
            with open(config_file, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            logging.error(f"Configuration file {config_file} not found, forcing an exit.")
            sys.exit(1)
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from the configuration file {config_file}, forcing an exit.")
            sys.exit(1)
        logging.info(f"Configuration loaded from {config_file}")

        try:
            assert 'stripe_api_key' in self.config.keys(), "stripe_api_key"
            assert 'app_secret_key' in self.config.keys(), "app_secret_key"
            assert 'db_host' in self.config.keys(), "db_host"
            assert 'db_port' in self.config.keys(), "db_port"
            assert 'db_user' in self.config.keys(), "db_user"
            assert 'db_password' in self.config.keys(), "db_password"
            assert 'product_information' in self.config.keys(), "product_information"
        except AssertionError as e:
            logging.error(f"Missing configuration key: {e.args[0]}, forcing an exit.")
            sys.exit(1)


            