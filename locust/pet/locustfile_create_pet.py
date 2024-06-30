from locust import task
from utils.logger import logger
import utils.event_listeners  
from locust_base import BaseApiUser

class CreatePetApiUser(BaseApiUser):
    
    @task(3)
    def create_pet(self):
        pet_data = self.data_generator.generate_pet_data_with_faker()
        response = self.api_client.request('post', 'pet', data=pet_data)
        if response.status_code == 200:
            pet_id = response.json()['id']
            self.environment.pet_id = pet_id
            logger.info("Created Pet ID: %s", pet_id)
        else:
            logger.warning("Failed to create pet. Status Code: %s", response.status_code)
            self.environment.pet_id = None  # Clear pet_id if creation fails
        
    assert utils.event_listeners