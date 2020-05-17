import discord
from discord.ext import commands
import os
import json

os.chdir(r"C:\Users\Ryan\Desktop\Discord")


class Brownie(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Brownie Cog is online')

    # check user profile
    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        with open('users.json', 'r') as f:
            users = json.load(f)

        if not member:
            id = str(ctx.author.id)
            stars = users[id]['Star Bits']
            rank = users[id]['Rank']
            author = ctx.author
            avatar = ctx.author.avatar_url

        else:
            id = str(member.id)
            stars = users[id]['Star Bits']
            rank = users[id]['Rank']
            author = member
            avatar = member.avatar_url

        embed = discord.Embed()
        embed.add_field(name = 'Star Bits', value = stars, inline = True)
        embed.add_field(name = 'Rank', value = rank, inline = True)
        embed.set_author(name = author, icon_url = avatar)
        await ctx.send(embed = embed)


    # Upvote command
    @commands.command()
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def upvote(self, ctx, member: discord.Member = None):
        with open('users.json', 'r') as f:
            users = json.load(f)

        # checks if user included @mention
        if not member:
            await ctx.send("You didn't upvote anyone")

        # checks if user is upvoting him or herself
        if member.id == ctx.author.id:
            await ctx.send("You cannot upvote yourself")

        # Proceeds to upvote rank
        else:
            id = str(member.id)
            users[id]['Star Bits'] += 1
            await ctx.send(f"{ctx.author.mention} has upvoted {member.mention}")

            if -500 < users[id]['Star Bits'] < 10:
                users[id]['Rank'] = 'Novice Astronomer'

            elif 10 <= users[id]['Star Bits'] < 25:
                users[id]['Rank'] = 'Star Mapper'

            elif 25 <= users[id]['Star Bits'] < 99:
                users[id]['Rank'] = 'Space Engineer'

        with open('users.json', 'w+') as f:
            json.dump(users, f)

    #downvote command
    @commands.command()
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def downvote(self, ctx, member: discord.Member = None):
        with open('users.json', 'r') as f:
            users = json.load(f)

        if not member:
            await ctx.send("You didn't downvote anyone")

        if member.id == ctx.author.id:
            await ctx.send("You cannot downvote yourself")

        else:
            id = str(member.id)
            users[id]['Star Bits'] -= 1
            await ctx.send(f"{ctx.author.mention} has downvoted {member.mention}")

            if -500 < users[id]['Star Bits'] < 10:
                users[id]['Rank'] = 'Novice Astronomer'

            elif 10 <= users[id]['Star Bits'] < 25:
                users[id]['Rank'] = 'Star Mapper'

            elif 25 <= users[id]['Star Bits'] < 99:
                users[id]['Rank'] = 'Space Engineer'


        with open('users.json', 'w+') as f:
            json.dump(users, f)



def setup(client):
    client.add_cog(Brownie(client))
