# access .env variables via this module
# make sure this is in same directory as .env file
# this needs to be a class

import os
from os.path import join, dirname
from dotenv import load_dotenv


def main():
	dotenv_path = join(dirname(__file__), '.env')
	load_dotenv(dotenv_path)


TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

