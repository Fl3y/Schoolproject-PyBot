
import discord
import json
import os
from discord.ext import commands
from discord import Guild
from firebase_admin import db


standart_Ctzn_Score = 300;

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

    @commands.command()
    async def addPoints(self, ctx, member: discord.Member, points):
        ref = db.reference("Users")
        Score = ref.child(str(member.id)).child('Ctzn_Score').get()
        print(Score)
        newScore = Score + int(points)
        ref.update({
            member.id:{
                    "Ctzn_Score": newScore
            }
        })

    @commands.command()
    async def removePoints(self, ctx, member: discord.Member, points):
        ref = db.reference("Users")
        Score = ref.child(str(member.id)).child('Ctzn_Score').get()
        print(Score)
        newScore = Score - int(points)
        ref.update({
            member.id:{
                    "Ctzn_Score": newScore
            }
        })

    @commands.command()
    async def setPoints(self, ctx, member: discord.Member, points):
        ref = db.reference("Users")
        Score = ref.child(str(member.id)).child('Ctzn_Score').get()
        print(Score)
        newScore = int(points)
        ref.update({
            member.id:{
                    "Ctzn_Score": newScore
            }
        })

    @commands.command()
    async def myPoints(self, ctx,):
        member = ctx.message.author
        ref = db.reference("Users")
        Score = ref.child(str(member.id)).child('Ctzn_Score').get()
        await ctx.send(f'Ni hao {member} the party got reports you have {Score} Points')
     


    @commands.command()
    async def checkDatabase(self, ctx):
        names = list()
        users = db.reference("Users").get()
        for user in ctx.guild.members:
            names.append(user.id)
        for x in range(len(names)):
            if names[x] not in users.values():
                ref = db.reference(f"/Users")
                ref.update({
                        names[x]:{
                            "Ctzn_Score": standart_Ctzn_Score
                        }    
                    }
                )

         

def setup(client):
    client.add_cog(Reputation(client))