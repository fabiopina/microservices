import connexion as connexion
from business.aggregator_controller import *
from flask_eureka.eureka import register_service


# Logging configuration
logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

register_service(name="aggr-ms", vip_address="aggr-ms", secure_vip_address="aggr-ms", host_name="aggr")

app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app


if __name__ == '__main__':
    app.run(port=5004, threaded=True, debug=True)
