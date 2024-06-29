from locust import events
from utils.logger import logger

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logger.info("Test is starting...")
    _ = environment, kwargs

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logger.info("Test is stopping...")
    _ = environment, kwargs