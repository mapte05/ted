
import os
from flask import Flask, request, redirect
import twilio.twiml
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
		body=message,
	    to=MANEESH,
	    from_=TED, 
	    )
	print(message.sid)

def call_parents_reminder():
	options = [
		"Hey make sure to call the parents",
		"Don't forget to call the rents",
		"Teddy and Sunny want to talk. Call home!",
		"You're a loser call mom"
	]
	message = random.choice(options) # nifty random choice
	send_message(message)



app = Flask(__name__)
app.use_reloader = False
# app.debug=True
# if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
#     # The app is not in debug mode or we are in the reloaded process
#     app.config.from_object(Config())
#     scheduler = APScheduler()
#     scheduler.init_app(app)
#     print "starting scheduler"
#     scheduler.start()


@app.route("/", methods=['GET', 'POST'])
def respond():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Hey you texted me!" + os.environ.get("JOKE"))
    return str(resp)



if __name__ == "__main__":
	print "starting app"
	app.run(debug=True, use_reloader=False)

	# app.run(debug=True)



