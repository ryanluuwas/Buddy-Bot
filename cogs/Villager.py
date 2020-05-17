import discord
from discord.ext import commands

import pandas as pd

# Set-up
filedir = '/Users/Ryan/Desktop/Discord/data'
df = pd.read_csv(filedir + '/villager_data.csv')

# Turn df column into lists
v_name = df.Name.to_list()
v_gender = df.Gender.to_list()
v_personality = df.Personality.to_list()
v_specie = df.Specie.to_list()
v_bday = df.Birthday.to_list()
v_phrase = df.Catchphrase.to_list()
v_skill = df.Skill.to_list()
v_goal = df.Goal.to_list()
v_coffee = df.Coffee.to_list()
v_milk = df.Milk.to_list()
v_sugar = df.Sugar.to_list()
v_song = df['Favorite Song'].to_list()
v_png = df.pngurl.to_list()
v_search = df.search.to_list()

v_name2 = [name.lower() for name in v_name]

class Villager(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Villager Cog is online')

    @commands.command()
    async def about(self, ctx, *, villager: str):
        if villager.lower() in v_search:
            idx = v_search.index(villager.lower())
        elif villager.lower() in v_name2:
            idx = v_name2.index(villager.lower())
        else:
            return

        embed = discord.Embed(
            title = v_name[idx],
            colour = discord.Colour.teal()
            #colour = 0xe60012
        )

        embed.set_thumbnail(url = v_png[idx])
        embed.add_field(name = 'Gender', value = v_gender[idx], inline = True)
        embed.add_field(name = 'Personality', value = v_personality[idx], inline = True)
        embed.add_field(name = 'Species', value = v_specie[idx], inline = True)
        embed.add_field(name = 'Birthday', value = v_bday[idx], inline = True)
        embed.add_field(name = 'Catchphrase', value = v_phrase[idx], inline = True)
        embed.add_field(name = 'Talent', value = v_skill[idx], inline = True)
        embed.add_field(name = 'Goal', value = v_goal[idx], inline = True)
        embed.add_field(name = 'Favorite Song', value = v_song[idx], inline = True) # Reached embed limit

        # resolves unknown with unknown and unknown (for new new horizon characters)
        if v_coffee[idx] == 'Unknown':
            embed.add_field(name = 'Coffee Order', value = v_coffee[idx], inline = True)
        else:
            embed.add_field(name = 'Coffee Order', value = f'{v_coffee[idx]} with {v_milk[idx].lower()} and {v_sugar[idx].lower()}', inline = True)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Villager(client))
