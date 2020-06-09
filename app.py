# -*- coding: utf-8 -*-
"""

"""

from flask import Flask
from web_app.blueprints.temp_all_pages import pages
from web_app.blueprints.errors.handlers import error_pages


app = Flask(__name__)
app.register_blueprint(pages)
app.register_blueprint(error_pages)

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
