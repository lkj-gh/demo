from flask_script import Manager

from Login import create_app
from Login.views import blue

app = create_app()

manager = Manager(app = app)

app.register_blueprint(blue)


if __name__ == '__main__':
    manager.run()
