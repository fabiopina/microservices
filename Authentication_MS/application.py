import connexion as connexion
from business.authentication_controller import *
from flask_eureka.eureka import register_service


# Logging configuration
logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

register_service(name="auth-ms", vip_address="auth-ms", secure_vip_address="auth-ms")

app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app


if __name__ == '__main__':
    app.run(port=5003, threaded=True, debug=True)
