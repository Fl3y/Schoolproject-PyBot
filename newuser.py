from tokenize import Name
from unicodedata import name
import database
import ReputationScore
from discord.ext import commands
import discord

class Newuser(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="newuser")
    @commands.has_permissions(administrator=True)
    async def insert_user(self, ctx, member: discord.Member, score):
        try:
            database.insert_user(member, score)
            await ctx.send(f"user added to Database")
        except Exception as e:
            return e

        


def setup(client):
    client.add_cog(Newuser(client))