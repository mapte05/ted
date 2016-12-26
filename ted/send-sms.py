# test message

import os
from twilio.rest import TwilioRestClient
from datetime import date
import time
from os.path import join, dirname
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
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


scheduler = BackgroundScheduler()
scheduler.add_job(sendMessage, 'cron', hour='17', minute='16')
scheduler.start()

# taken from example: https://github.com/agronholm/apscheduler/blob/master/examples/schedulers/background.py
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
try:
    # This is here to simulate application activity (which keeps the main thread alive).
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    # Not strictly necessary if daemonic mode is enabled but should be done if possible
    scheduler.shutdown()







# messages = client.messages.list(
#     to="+17013615368",
#     # date_sent=date(2011,1,1),
# )

# for message in messages:
#     print message.body
