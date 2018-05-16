import logging
import time
from .eurekaclient import EurekaClient


def register_service(name=None, vip_address=None, secure_vip_address=None):
    """
    Register service with eureka service
    """

    eureka_client = EurekaClient(name=name, vip_address=vip_address,
                                 secure_vip_address=secure_vip_address)

    while True:
        try:
            eureka_client.star()
        except Exception:
            logging.debug("Eureka is down. Reconnecting in 5 seconds ....")
            time.sleep(5)
            continue
        break
