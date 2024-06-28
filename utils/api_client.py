import yaml
import os
import requests

class APIClient:
    def __init__(self, base_url, headers, endpoints):
        self.base_url = base_url
        self.headers = headers
        self.endpoints = endpoints

    def request(self, method, endpoint_key, endpoint_path='', data=None, params=None, headers=None):
        url = f"{self.base_url}{self.endpoints[endpoint_key]}{endpoint_path}"
        if headers is None:
            headers = self.headers
        try:
            if method.lower() == 'get':
                response = requests.get(url, params=params, headers=headers)
            elif method.lower() == 'post':
                response = requests.post(url, json=data, headers=headers)
            elif method.lower() == 'put':
                response = requests.put(url, json=data, headers=headers)
            elif method.lower() == 'delete':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Invalid HTTP method. Supported methods: GET, POST, PUT, DELETE")
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response
        except requests.RequestException as e:
            raise requests.RequestException(f"Error making {method.upper()} request to {url}: {e}")
