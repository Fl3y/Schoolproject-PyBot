import os
import dotenv
import discord
from discord.ext import commands


dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event 
async def on_member_join(member):
    print(f"{member} has joint the server,")
    return

@client.event 
async def on_member_remove(member):
    print(f"{member} has left the server,")
    return

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")
    
client.run(TOKEN)


