import logging
import time
from .eurekaclient import EurekaClient


def register_service(name=None):
    """
    Register service with eureka service
    """

    eureka_client = EurekaClient(name=name)

    while True:
        try:
            eureka_client.star()
        except Exception:
            logging.debug("Eureka is down. Reconnecting in 5 seconds ....")
            time.sleep(5)
            continue
        break
