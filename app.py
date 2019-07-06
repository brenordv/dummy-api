# -*- coding: utf-8 -*-

from flask import Flask

from blueprints.dummy_api_v1 import api_v1

app = Flask(__name__)
app.register_blueprint(api_v1)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
