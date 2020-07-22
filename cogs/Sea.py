import discord
from discord.ext import commands

import pandas as pd

filedir = '/Users/Ryan/Desktop/Discord/data'
df = pd.read_csv(filedir + '/sea_data.csv')

# Turn df column into lists
v_name = df.Name.to_list()
v_price = df.Price.to_list()
v_shadow = df.Shadow.to_list()
v_pattern = df.Pattern.to_list()
v_time = df.Time.to_list()
v_jan = df.Jan.to_list()
v_feb = df.Feb.to_list()
v_mar = df.Mar.to_list()
v_apr = df.Apr.to_list()
v_may = df.May.to_list()
v_jun = df.Jun.to_list()
v_jul = df.Jul.to_list()
v_aug = df.Aug.to_list()
v_sep = df.Sep.to_list()
v_oct = df.Oct.to_list()
v_nov = df.Nov.to_list()
v_dec = df.Dec.to_list()
v_search = df.search.to_list()
v_png = df.pngurl.to_list()

#name but lowercase
v_name2 = [name.lower() for name in v_name]

# list of months
mo = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


class Sea(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Sea Cog is online')

    @commands.command()
    async def sea(self, ctx, *, sea: str):
        if sea.lower() in v_name2:
            idx = v_name2.index(sea.lower())
        elif sea.lower() in v_search:
            idx = v_search.index(sea.lower())
        else:
            return

        # Availability
        a = [] # create an empty list a to append to

        if v_jan[idx] == True: # if index number of jan == true, append it to a. etc
            a.append('Jan')
        if v_feb[idx] == True: # etc.
            a.append('Feb')
        if v_mar[idx] == True:
            a.append('Mar')
        if v_apr[idx] == True:
            a.append('Apr')
        if v_may[idx] == True:
            a.append('May')
        if v_jun[idx] == True:
            a.append('Jun')
        if v_jul[idx] == True:
            a.append('Jul')
        if v_aug[idx] == True:
            a.append('Aug')
        if v_sep[idx] == True:
            a.append('Sep')
        if v_oct[idx] == True:
            a.append('Oct')
        if v_nov[idx] == True:
            a.append('Nov')
        if v_dec[idx] == True:
            a.append('Dec')

        b = ' '.join(a)

        embed = discord.Embed(
            title = v_name[idx],
            colour = discord.Colour.teal()
            #colour = discord.Colour(0xFFC0CB)
        )
        embed.set_thumbnail(url = v_png[idx])
        embed.add_field(name = 'Price', value = v_price[idx], inline=True)
        embed.add_field(name = 'Shadow', value = v_shadow[idx], inline = True)
        embed.add_field(name = 'Pattern', value = v_pattern[idx], inline = True)
        embed.add_field(name = 'Time', value = v_time[idx], inline = True)
        embed.add_field(name = 'Availability', value = b, inline = False)
        await ctx.send(embed=embed)


    @commands.command()
    async def sea_month(self, ctx, month):

        # If month is in month list, take the first three letters of it and capitalize the first
        if month.lower() in mo:
            month = (month[:3]).title()
        else:
            month = month.title()

        q4 = df[(df[month]==True)]
        img = q4.pngurl.to_list()
        q4 = list(q4.Name)
        q4 = ', '.join(q4)

        embed = discord.Embed(
            title = f'{month.upper()} Sea Creatures',
            colour = discord.Colour.teal()
        )

        #embed.set_thumbnail(url = img)
        embed.set_thumbnail(url = img[-1])
        embed.add_field(name = 'Sea Query', value = q4, inline = False)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Sea(client))
