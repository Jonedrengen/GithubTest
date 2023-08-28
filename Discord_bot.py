# Code explanation is always above

# Importing the discord library to interact with Discord
import discord
# Importing the commands extension for more advanced command handling
from discord.ext import commands
# Importing a custom module that presumably handles bot responses
import Discord_bot_responses

# Creating a default set of intents (permissions that define which events the bot can access)
intents = discord.Intents.default()
# Allowing the bot to access message content
intents.message_content = True
# Creating a client instance with the defined intents, which represents the connection to Discord
client = discord.Client(intents=intents)

# Asynchronous function to send a message to the author or channel
async def send_message(message, user_message, is_private):
    try:
        username = str(message.author)
        # Getting a response from the custom module
        response = Discord_bot_responses.handle_response(user_message, username) # <-- remember to update the bot all places when modifying response code
        # Sending the response privately or to the channel, depending on the is_private parameter
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        # Printing any exceptions that occur
        print(e)

# Function to run the Discord bot
def run_discord_bot():
    # Bot's token, which is used to log in (Note: Always keep this private!)
    TOKEN = "MTE0MzEzMDUzNTE5NjExOTExMQ.GbUQDe.ZjU4Dz9h-lJqyWg5asMOsAq2PQdLClAowyUhMQ"

    # Event that triggers when the bot is ready
    @client.event
    async def on_ready():
        # Printing a message to the console to confirm the bot is running
        print(f'{client.user} is now running!')

    # Event that triggers when a message is received
    @client.event
    async def on_message(message): # <-- Here's where the 'message' object is defined, from the discord library
        # Preventing the bot from responding to its own messages
        if message.author == client.user:
            return
        
        # Extracting the username, message, and channel from the message object
        username = str(message.author)
        user_message = str(message.content).strip()
        channel = str(message.channel)

        # Returning if the message is empty
        if user_message == "":
            return

        # Debugging code to print what the user said and where
        print(f'{username} said {user_message} in {channel}')

        # Checking if the message starts with '?' and processing it accordingly (private messages)
        if user_message and user_message[0] == '?':
            # Removing the '?' and sending the message privately
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            # Sending the message to the channel
            await send_message(message, user_message, is_private=False )

    # Starting the client with the given token
    client.run(TOKEN)
