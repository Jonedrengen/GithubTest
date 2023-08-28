# Importing a library to use random functions.
import random

# Importing a library to work with the Discord API.
import discord

# Importing a library to make web requests.
import requests

# This function fetches weather data from an API for a given location.
def get_weather(latitude=52.52, longitude=13.41):
    # Creating the specific web address to get weather for the given location.
    url = f'https://api.open-meteo.com/v1/forecast?latitude=56&longitude=10&hourly=temperature_2m,rain,weathercode'
    
    # Fetching the weather data from the web address and converting it to a format we can work with (JSON).
    response = requests.get(url).json()
    # Sending the fetched data back to whoever called this function.
    return response

# This function extracts and interprets specific details from the weather data.
def get_weather_info(json_data):
    # Extracting the current temperature from the weather data.
    current_temperature = json_data['hourly']["temperature_2m"][0]
    # Extracting the code that tells us the current weather type (like rain, sun, etc.).
    weather_code_today = json_data['hourly']["weathercode"][0]
    
    # Checking if the weather code suggests rain might be coming soon.
    if weather_code_today == 3:
        is_raining = "maybe soon"
    # Checking if the weather code says it's currently raining.
    if weather_code_today in [20, 21, 22, 23, 24, 25, 26, 27, 29]:
        is_raining = "actually raining"
    # If neither of the above checks are true, it means it's not raining.
    else:
        is_raining = "no"
    
    # Combining the temperature and rain status into one data package to send back.
    return {
        "Temperature": current_temperature,
        "Raining": is_raining
    }

# This function decides how the bot should reply based on the user's message.
def handle_response(message, username):
    # Converting the user's message to lowercase to make it easier to check.
    p_message = message.lower()
    # If the user sends a greeting, the bot sends back a friendly response.
    if p_message.lower() in ["hello", "hey", "hi", "yo", "hej"]:
        return f"what is up {username}"
    # If the user asks the bot to "roll", the bot simulates a dice roll and sends the result.
    if p_message == "roll":
        return str(random.randint(1,6))
    # Preparing a help message for the user.
    help_text = "welcome to the !help page.\n"
    help_text += "1. ?message: write a private message to the bot\n"
    help_text += "2. roll: rolls a dice between 1 and 6\n"
    help_text += "3. calc: start the calculator function of the bot."
    # If the user asks for help, the bot sends back the help message.
    if p_message == "!help":
        return help_text
    # If the user asks about the weather, the bot fetches current weather data.
    if p_message.lower() in ["weather", "forecast", "vejr", "vejret"]:
        current_weather_data = get_weather()
        # The bot then extracts the relevant details from the weather data.
        weather_info = get_weather_info(current_weather_data)
        # The bot sends back the extracted details.
        return weather_info
