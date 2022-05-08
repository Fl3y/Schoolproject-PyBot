import datetime
import os
import dotenv
import humanfriendly
import discord
import ffmpeg
from discord.ext import commands
import json 
import re
import music
import ReputationScore





cogs = [music, ReputationScore]

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

bannedWords = configData["bannedWords"]


dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()

client = commands.Bot(command_prefix='.', intents=intents)

for i in range(len(cogs)):
    cogs[i].setup(client)




@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    return

 

@client.event 
async def on_member_join(member):
    print(f"{member} has joint the server,")
    
    return

@client.event 
async def on_member_remove(member):
    print(f"{member} has left the server,")
    return

def msg_contains_words(msg, word):
    return re.search(fr'\b({word})\b', msg) is not None  

@client.event
async def on_message(message):
    messageAuthor = message.author
    global bannedWords
    print (bannedWords)
 
    if bannedWords != None and (isinstance(message.channel, discord.channel.DMChannel) == False):
        for bannedWord in bannedWords:
            if msg_contains_words(message.content.lower(), bannedWord):
                await message.delete()
                await message.channel.send(f"{messageAuthor.mention} your message was removed as it contains a banned word.")

    await client.process_commands(message)
    return



@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

@client.command()
async def schlafen(ctx, member : discord.Member,time = None, *, reason=None):
    time = humanfriendly.parse_timespan(time)
    await member.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds = time), reason=reason)
    await ctx.send(f"{member} has been timed out for {time} | Reason: {reason}")



client.run(TOKEN)
