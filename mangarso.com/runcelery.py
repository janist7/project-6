activate_this = '/var/www/html/sites/recipe_website/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app.run import create_app
from app.extensions import celery

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        celery.start()
