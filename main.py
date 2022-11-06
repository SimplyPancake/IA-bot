import discord
import os
import os.path
from dotenv import load_dotenv

# Load the .env file
if not os.path.isfile('.env'):
	print(".env File including the token is missing!")
	print("Please create environment variables according to the documentation.")
	exit()

# Configure .env vars
load_dotenv()

# Configure the client (TODO: Place to seperate file)
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))