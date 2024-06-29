from locust import HttpUser, between
from utils.api_client import APIClient
from utils.data_generator import DataGenerator
import yaml
import os

class BaseApiUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds between tasks
    abstract = True

    def on_start(self):
        config_path = "../../config/config.yaml"
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {os.path.abspath(config_path)}")

        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            self.api_base_url = config['api_base_url']
            self.headers = config['headers']
            self.endpoints = config['endpoints']

        self.api_client = APIClient(self.api_base_url, self.headers, self.endpoints)
        self.data_generator = DataGenerator()
