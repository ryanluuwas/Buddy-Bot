import discord
from discord.ext import commands
import os

class Uwufy(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'uwu Cog is online')

    @commands.command()
    async def uwu(self, ctx, *, string: str):
        s = string.lower()
        s = s.replace('r','w')
        s = s.replace('l','w')
        s = s.replace('ing','wing')
        s = s.replace('?', '? OwO')

        await ctx.send(f'{s}')



def setup(client):
    client.add_cog(Uwufy(client))
