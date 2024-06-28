# Python Locust API Performance Testing

This repository contains scripts for performance testing APIs using Locust, a popular load testing tool in Python. The project focuses on testing the Petstore API from Swagger.

## Installation

1. Clone the repository:

`https://github.com/dipyomoybarua/python-locust-api-poc.git`

2. Install the required dependencies:

`pip install -r requirements.txt`

## Project Structure:-

`locust/`: Contains Locust files for defining tasks and scenarios.

`config/`: Holds configuration files like config.yaml for API endpoints and headers.

`tests/`: Includes test-related files.

## Usage:-
1. Modify config/config.yaml with your API base URL, headers, and endpoints.

2. Run Locust with:

`locust -f locust/pet/locustfile_create_pet.py --host=https://petstore.swagger.io/v2` (Modify according to your folder structure)
