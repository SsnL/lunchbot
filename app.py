import os
import time
import re
import json
import socket
import slack

HOST = f"{socket.gethostname()}.csail.mit.edu"
SLACK_AUTH_FILE = os.path.join(os.path.dirname(__file__), 'SLACK_AUTH')

def main():
    with open(SLACK_AUTH_FILE, 'r') as f:
        SLACK_BOT_TOKEN = json.load(f)['SLACK_BOT_TOKEN']

    client = slack.WebClient(token=SLACK_BOT_TOKEN)

    client.chat_postMessage(
      channel="zoomlunch",
      text="Hello from your app! :tada:"
    )