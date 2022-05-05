import database
from discord.ext import commands


class Newuser(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="newuser")
    @commands.has_permissions(administrator=True)
    async def insert_user(self, ctx, *args):
        try:
            name = ' '.join(args)
            discord = ' '.join(args)
        except IndexError:
            try:
                name = ' '.join(args)
                age = ' '.join(args)
            except ValueError:
                await ctx.send("Please enter a name")
                return
            except IndexError:
                await ctx.send("Please add users details")
                return
        add = database.insert_user(player_name=name, discord_tag=discord)
        if isinstance(add, Exception):
            await ctx.send(f"Database error when adding a new admin:\n```\n{add}\n```")
            return
        await ctx.send("Added the role to my admin list.")


def setup(client):
    client.add_cog(Newuser(client))