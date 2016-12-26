# all routes go here
from ted import app
from ted.scheduler import SchedulerConfig
import os
from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random
import logging
import sys


account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = TwilioRestClient(account_sid, auth_token)

DEFAULT_MESSAGE = "Hey I'm texting you but not sure what the message should be"
MANEESH = "+17013615368"
TED = "+17013531729"


def send_message(message_body=DEFAULT_MESSAGE):
	message = client.messages.create(
		body=message_body,
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


@app.route("/", methods=['GET', 'POST'])
def respond():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    resp.message("Hey this is Ted. I'm just answering your text!")
    return str(resp)













