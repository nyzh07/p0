
### 389T Bot

###### Purpose

This bot is a GroupMe bot that can read and respond to messages in a GroupMe chat.  
- Responds to me and only me when I send a message
- Responds to any user when "good morning" or "good night" is sent
- Responds to any user when the weather of a particular city is requested

###### Features

- **Response to Me**: When I send a message, the bot responds with "sup". Even if someone else with the same name sends the same message, the bot will not respond.
- **Good Morning/Good Night**: When any user in the group chat sends a message containing "good morning" or "good night", the bot will respond with "Good morning" or "Good night," appropriately, along with the name of the user. The bot will not respond to other bots or itself.
> - Eg. If a user named "Nicole" sends "good morning," then the bot will respond with "Good morning, Nicole"
- **Weather Request**: When a user queries "What is the weather in [city name]", the bot fetches and provides the current temperature in the city and what it feels like, both in degrees Fahrenheit. The bot will not respond to other bots or itself.
> - Eg. If a user sends "What is the weather in Baltimore," the bot will respond with "The temperature in Baltimore is [current temperature in Baltimore]°F. Feels like [current feels like temperature in Baltimore]°F."

###### How to Run

To run the bot, you must have Python installed, a GroupMe account, and a GroupMe bot. Clone the bot repository to your local machine and make sure to create an .env file with the BOT_ID, GROUP_ID, and ACCESS_TOKEN. Create and activate a virtual environment, install dependencies located in the requirements.txt file, and run the bot. The steps are shown below:

```bash
# clone the **forked** repo to your local machine and cd into it 
git clone https://github.com/<your-username>/p0.git && cd p0

# create virtual environment (this creates a folder called venv)
python3 -m venv venv

# activate virtual environment
source venv/bin/activate # for mac/linux
venv\Scripts\activate # for windows

# install dependencies
pip install -r requirements.txt

# run bot
python3 bot.py
```
