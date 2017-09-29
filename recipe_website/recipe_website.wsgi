#!/usr/bin/python
import sys
from app import create_app, config
sys.path.insert(0, os.path.dirname(__file__))

application = create_app(config=config.prod_config)

if __name__ == '__main__':
    application.run("0.0.0.0")