#!/usr/bin/env python3

import connexion
import json
import logging

from flask import current_app
import database.database as database

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'tapi-connectivity API generated from tapi-connectivity.yang'})
    app.app.config['JSON_SORT_KEYS']=False
    with app.app.app_context():
        with current_app.open_resource("database/context.json", 'r') as f:
            database.context = json.load(f)
    app.run(port=8080)
