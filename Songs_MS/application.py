import connexion as connexion
from business.songs_controller import *
from CRUD.ORM import db
from flask_eureka.eurekaclient import EurekaClient


app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

eureka_client = EurekaClient(name="songs-ms", vip_address="songs-ms", secure_vip_address="songs-ms")
eureka_client.star()


@application.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == '__main__':
    app.run(port=5001, threaded=True, debug=True)
