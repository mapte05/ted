
import os
from flask import Flask, request, redirect
import twilio.twiml
from flask_apscheduler import APScheduler
from twilio.rest import TwilioRestClient


account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = TwilioRestClient(account_sid, auth_token)

def sendMessage():
	message = client.messages.create(
		body="heyyy",
	    to="+17013615368",
	    from_="+17012039811", 
	    )
	print(message.sid)


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'run:sendMessage',
            # 'args': (1, 2),
            'trigger': 'cron',
            'minute': 26
        }
    ]
    SCHEDULER_VIEWS_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()



@app.route("/", methods=['GET', 'POST'])
def respond():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Hey you texted me!" + os.environ.get("JOKE"))
    return str(resp)



if __name__ == "__main__":
	app.run(debug=True, use_reloader=False)



