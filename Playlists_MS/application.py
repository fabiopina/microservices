import connexion as connexion
from business.playlists_controller import *
from CRUD.ORM import db
from flask_eureka.eureka import register_service


# Logging configuration
logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

register_service(name="playlists-ms")

app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app


@application.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == '__main__':
    app.run(port=5002, threaded=True, debug=True)
