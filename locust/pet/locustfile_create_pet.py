from locust import HttpUser, task, between, events
from utils.data_generator import DataGenerator
from utils.logger import logger
from utils.api_client import APIClient
import yaml
import os

class PetApiUser(HttpUser):
    wait_time = between(1, 5)

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

    @task(3)
    def create_pet(self):
        pet_data = self.data_generator.generate_pet_data_with_faker()
        response = self.api_client.request('post', 'pet', data=pet_data)
        logger.info("Response Status Code: %s", response.status_code)

    @task(1)
    def get_pets(self):
        status = self.data_generator.generate_pet_data_with_faker()["status"]
        url = f"/findByStatus?status={status}"
        response = self.api_client.request('get', 'pet', endpoint_path=url)

        logger.info("Response Status Code: %s", response.status_code)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        
    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        logger.info("Test is starting...")
            
    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        logger.info("Test is stopping...")