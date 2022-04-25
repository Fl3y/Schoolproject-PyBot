import os
import dotenv
import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix='.', intents=intents)




@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event 
async def on_Member_join(member):
    print(f"{member} has joint the server,")

@client.event 
async def on_Member_remove(member):
    print(f"{member} has left the server,")

@client.event
async def on_Message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return
    
    if message.channel.name == "general-bot":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}!")
            return

        elif user_message.lower() == "bye":
            await message.channel.send(f"See you later {username}!")
            return
        

client.run(TOKEN)


