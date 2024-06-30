from locust import task
from utils.logger import logger
import utils.event_listeners  
from locust_base import BaseApiUser

class GetPetApiUser(BaseApiUser):
    
    @task(2)
    def get_pet(self):
            if hasattr(self.environment, 'pet_id')and self.environment.pet_id is not None:
                pet_id = self.environment.pet_id
                response = self.api_client.request('get', 'pet', endpoint_path=f"/{pet_id}")
                logger.info("Response Status Code: %s", response.status_code)
                assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
            else:
                logger.warning("No pet_id found in environment.")
                
    assert utils.event_listeners