import os
import dotenv
import discord

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

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


