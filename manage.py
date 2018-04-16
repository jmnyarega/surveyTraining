from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.main import *
from app.EventsResource import *
from app.SessionResource import *
from app.RolesResource import *

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.run()
