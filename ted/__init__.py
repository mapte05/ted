# I followed directions given here: http://flask.pocoo.org/docs/0.12/patterns/packages/
# the module name is ted; therefore procfile has ted
# for details regarding scheduler see: http://stackoverflow.com/questions/32424148/how-to-use-flask-apscheduler-in-existed-flask-app

from flask import Flask

app = Flask(__name__)

import ted.views
from ted.scheduler import SchedulerConfig
from flask_apscheduler import APScheduler
app.config.from_object(SchedulerConfig())
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
print "started scheduler"