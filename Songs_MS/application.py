import connexion as connexion
from business.songs_controller import *
from CRUD.ORM import db


app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app


@application.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == '__main__':
    app.run(port=5001, threaded=True, debug=True)
