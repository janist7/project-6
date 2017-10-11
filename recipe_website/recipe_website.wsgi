#!/usr/bin/python

activate_this = '/var/www/html/sites/recipe_website/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.append('/var/www/html/sites/recipe_website')

from app import app as application