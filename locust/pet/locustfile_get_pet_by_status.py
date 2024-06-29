from locust import task
from utils.logger import logger
import utils.event_listeners
from locust_base import BaseApiUser

class PetApiUser(BaseApiUser):
            
    @task(1)
    def get_pets(self):
        status = self.data_generator.generate_pet_data_with_faker()["status"]
        url = f"/findByStatus?status={status}"
        response = self.api_client.request('get', 'pet', endpoint_path=url)

        logger.info("Response Status Code: %s", response.status_code)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        
    assert utils.event_listeners