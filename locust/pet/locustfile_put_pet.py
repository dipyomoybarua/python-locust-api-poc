from locust import task
from utils.logger import logger
from locust_base import BaseApiUser
import utils.event_listeners  

class PetApiUser(BaseApiUser):

    @task(2)
    def update_pet(self):
        pet_id = self.data_generator.fake.random_int(min=1, max=500)
        pet_data = self.data_generator.generate_update_pet_data_with_faker(pet_id=pet_id)
        response = self.api_client.request('put', 'pet', data=pet_data)
        logger.info("Response Status Code: %s", response.status_code)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        
    assert utils.event_listeners