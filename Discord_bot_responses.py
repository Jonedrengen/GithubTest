import random
import discord

# Importing the required module for making HTTP requests
import requests

# Defining a function that fetches weather data based on given latitude and longitude
def get_weather(latitude=52.52, longitude=13.41):
    # Constructing the URL for the API request
    url = f'https://api.open-meteo.com/v1/forecast?latitude=56&longitude=10&hourly=temperature_2m,rain,weathercode'
    
    # Making the API request and converting the response to a JSON object
    response = requests.get(url).json()
    # Returning the JSON data
    return response



# Defining a function to extract specific weather information from the fetched JSON data
def get_weather_info(json_data):
    # Getting the current temperature from the 'hourly' key of the JSON data
    current_temperature = json_data['hourly']["temperature_2m"][0]
    # Getting the weather code for the current day from the 'daily' key
    weather_code_today = json_data['hourly']["weathercode"][0]
    
    # Checking if the weather code is 3 (Assuming this indicates rain might come soon)
    if weather_code_today == 3:
        is_raining = "maybe soon"
    # Checking if the weather code falls within a set of codes indicating actual rain
    if weather_code_today in [20, 21, 22, 23, 24, 25, 26, 27, 29]:
        is_raining = "actually raining"
    # If none of the above conditions match, then it's not raining
    else:
        is_raining = "no"
    
    # Returning a dictionary containing the current temperature and the rain status
    return {
        "Temperature": current_temperature,
        "Raining": is_raining
    }

# Basically handles how the Bot should respond. Uses 2 arguments 1 message and 1 username.
def handle_response(message, username): # <-- When adding more arguments, remember to update all the places where this is called (send_message() function).
    p_message = message.lower()
    if p_message.lower() in ["hello", "hey", "hi", "yo", "hej"]:
        return f"what is up {username}"
    if p_message == "roll":
        return str(random.randint(1,6))
    help_text = "welcome to the !help page.\n"
    help_text += "1. ?message: write a private message to the bot\n"
    help_text += "2. roll: rolls a dice between 1 and 6\n"
    help_text += "3. calc: start the calculater function of the bot."
    if p_message == "!help":
        return help_text
    if p_message.lower() in ["weather", "forecast", "vejr", "vejret"]:
        #fetching weather data (in the handle_response() function, to make sure data is updated every time)
        # Calling the function to fetch weather data and storing it in 'result'
        current_weather_data = get_weather()

        # Calling the function to extract weather info and storing it in 'weather_info'
        weather_info = get_weather_info(current_weather_data)
        return weather_info



