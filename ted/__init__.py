# I followed directions given here: http://flask.pocoo.org/docs/0.12/patterns/packages/
# the module name is ted; therefore procfile has ted

from flask import Flask

app = Flask(__name__)

import ted.views

