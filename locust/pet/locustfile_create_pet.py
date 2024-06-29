from locust import task
from utils.logger import logger
import utils.event_listeners  
from locust_base import BaseApiUser

class PetApiUser(BaseApiUser):
    
    @task(3)
    def create_pet(self):
        pet_data = self.data_generator.generate_pet_data_with_faker()
        response = self.api_client.request('post', 'pet', data=pet_data)
        logger.info("Response Status Code: %s", response.status_code)
        
    assert utils.event_listeners