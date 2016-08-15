
import os
from flask import Flask, request, redirect
import twilio.twiml
from flask_apscheduler import APScheduler
from twilio.rest import TwilioRestClient
import random


account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = TwilioRestClient(account_sid, auth_token)

DEFAULT_MESSAGE = "Hey I'm texting you but not sure what the message should be"
MANEESH = "+17013615368"
TED = "+17012039811"


def send_message(message=DEFAULT_MESSAGE):
	message = client.messages.create(
		body="heyyy",
	    to=MANEESH,
	    from_=TED, 
	    )
	print(message.sid)

def call_parents_reminder():
	options = [
		"Hey make sure to call the parents",
		"Don't forget to call the rents",
		"Boo boo and bow bow probably want to talk. Call home!",
		"You're a loser call your mom"
	]
	message = random.choice(options) # nifty random choice
	send_message(message)


class Config(object):
    JOBS = [
        {
            'id': 'call_parents_weekday',
            'func': 'run:call_parents_reminder',
            # 'args': (1, 2),
            'trigger': 'cron',
            'day_of_week': 'mon-fri',
            'hour': '19', #7pm
            'minute': '30'
        },
        {
            'id': 'call_parents_reminder_weekend',
            'func': 'run:call_parents_reminder',
            # 'args': (1, 2),
            'trigger': 'cron',
            'day_of_week': 'sat-sun',
            'hour': '16', #4pm
        },
        {
            'id': 'call_parents_reminder_test',
            'func': 'run:call_parents_reminder',
            # 'args': (1, 2),
            'trigger': 'cron',
            'day_of_week': 'sat-sun',
            'hour': '19', #4pm
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



