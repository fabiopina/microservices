import connexion as connexion
from business.playlists_controller import *
from CRUD.ORM import db
from flask_eureka.eurekaclient import EurekaClient


app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

eureka_client = EurekaClient(name="playlists-ms", vip_address="playlists-ms", secure_vip_address="playlists-ms")
eureka_client.star()


@application.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == '__main__':
    app.run(port=5002, threaded=True, debug=True)
