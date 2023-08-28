import random
import discord

# Handles the bot response to the users input

# Basically handles how the Bot should respond. Uses 2 arguments 1 message and 1 username.
def handle_response(message, username): # <-- When adding more arguments, remember to update all the places where this is called (send_message() function).
    p_message = message.lower()
    if p_message in ["hello", "hey", "hi", "yo", "hej"]:
        return f"what is up {username}"
    if p_message == "roll":
        return str(random.randint(1,6))
    help_text = "welcome to the !help page.\n"
    help_text += "1. ?message: write a private message to the bot\n"
    help_text += "2. roll: rolls a dice between 1 and 6\n"
    help_text += "3. calc: start the calculater function of the bot."
    if p_message == "!help":
        return help_text


