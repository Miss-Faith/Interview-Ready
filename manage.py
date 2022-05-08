from app import create_app,db
from app.models import User,Role,Comment
from  flask_migrate import Migrate, MigrateCommand

app = create_app('development')

migrate = Migrate(app,db)

if __name__ == '__main__':
    app.run()