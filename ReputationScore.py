import discord
import json
import os
from discord.ext import commands


if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

bannedWords = configData["bannedWords"]


class Reputation(commands.Cog):
    def __init__(self, client,):
        self.client = client

    @commands.command()
    async def addbannedword(self, ctx, word):
        if str(word).lower() in bannedWords:
            await ctx.send("Already banned")
        else:
            bannedWords.append(str(word).lower())

            with open("./config.json", "r+") as f:
                data = json.load(f)
                data["bannedWords"] = bannedWords
                f.seek(0)
                f.write(json.dumps(data))
                f.truncate()

                await ctx.message.delete()
                await ctx.send("Word added to banned Words")
    
                

    @commands.command()
    async def removebannedword(self, ctx, word):
        if str(word).lower() in bannedWords:
            bannedWords.remove(word.lower())

            with open("./config.json", "r+") as f:
                data = json.load(f)
                data["bannedWords"] = bannedWords
                f.seek(0)
                f.write(json.dumps(data))

                f.truncate()

            await ctx.message.delete()
            await ctx.send("Word removed from banned words.")
        else:
            await ctx.send("Word isnt banned")

def setup(client):
    client.add_cog(Reputation(client))