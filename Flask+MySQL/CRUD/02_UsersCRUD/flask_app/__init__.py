
from flask import Flask

app = Flask(__name__)
app.secret_key = "my super secret key!"

import flask_app.controllers.users