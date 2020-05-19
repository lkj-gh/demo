from flask import Blueprint
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from Login import create_app


app = create_app()

from Login.views import blue
app.register_blueprint(blue)
manager = Manager(app = app)


# 初始化数据库
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Nice.tv520@47.103.107.144:3306/KTS?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()



