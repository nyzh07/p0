import requests
import time
import json
import os
from dotenv import load_dotenv
import re

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None
SENDER_ID = os.getenv("SENDER_ID")
API_KEY = "b16305ea94491f1af2fb603cc7d960c3"

def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def get_weather(city):
    api_url = "http://api.weatherstack.com/current"
    params = {"access_key": API_KEY, "query": city, "units": "f"}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        temp = response.json().get("current", {}).get("temperature", "")
        feels_like = response.json().get("current", {}).get("feelslike", "")
        loc = response.json().get("location", {}).get("name", "")
        weather = "The temperature in " + str(loc) + " is " + str(temp) + "°F. Feels like " + str(feels_like) +  "°F."
    else:
        error_message = response.json.get("error", {}).get("info", [])
        weather = "Failed to retrieve:" + error_message
    return weather


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()
    sender_id = message["sender_id"]
    sender_type = message["sender_type"]

    # i.e. responding to a specific sender
    if sender_id == SENDER_ID and "what's the weather in" not in text:
        send_message("sup")
    elif sender_type != "bot":
        if "good morning" in text:
            send_message("Good morning, " + message["name"])
        elif "good night" in text:
            send_message("Good night, " + message["name"])
        elif "what's the weather in" in text:
            match = re.search(r"what's the weather in ([\w\s]+)", text, re.IGNORECASE)
            city = match.group(1).strip()
            weather = get_weather(city)
            send_message(weather)

    LAST_MESSAGE_ID = message["id"]

def get_last_message_id():
    # last message only
    params = {"token": ACCESS_TOKEN, "limit": 1}
    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        messages = response.json().get("response", {}).get("messages", [])
        if messages:
            return messages[0]["id"]
    return []

def main():
    global LAST_MESSAGE_ID
    LAST_MESSAGE_ID = get_last_message_id()

    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()
