import connexion as connexion
from business.aggregator_controller import *
from flask_eureka.eurekaclient import EurekaClient


# Logging configuration
logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')


app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

eureka_client = EurekaClient(name="aggr-ms", vip_address="aggr-ms", secure_vip_address="aggr-ms")
eureka_client.star()


if __name__ == '__main__':
    app.run(port=5004, threaded=True, debug=True)
