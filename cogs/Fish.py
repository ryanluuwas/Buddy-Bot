import discord
from discord.ext import commands

import pandas as pd

filedir = '/Users/Ryan/Desktop/Discord/data'
df = pd.read_csv(filedir + '/fish_data.csv')

# Turn df column into lists
v_name = df.Name.to_list()
v_price = df.Price.to_list()
v_location = df.Location.to_list()
v_shadow = df.Shadow.to_list()
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
v_rarity = df.Rarity.to_list()

#name but lowercase
v_name2 = [name.lower() for name in v_name]

mo = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

class Fish(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Fish Cog is online')

    @commands.command()
    async def fish(self, ctx, *, fish: str):
        if fish.lower() in v_name2:
            idx = v_name2.index(fish.lower())
        elif fish.lower() in v_search:
            idx = v_search.index(fish.lower())
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
        embed.add_field(name = 'Location', value = v_location[idx], inline = True)
        embed.add_field(name = 'Rarity', value = v_rarity[idx].title(), inline = True)
        embed.add_field(name = 'Shadow Size', value = v_shadow[idx], inline = True)
        embed.add_field(name = 'Time', value = v_time[idx], inline = True)
        embed.add_field(name = 'Availability', value = b, inline = False)
        await ctx.send(embed=embed)


    @commands.command()
    async def fish_month(self, ctx, month):

        # If month is in month list, take the first three letters of it and capitalize the first
        if month.lower() in mo:
            month = (month[:3]).title()
        else:
            month = month.title()

        q1 = df[(df.Rarity == 'common') & (df[month]==True)] # queries for common fish of the requested month
        q1 = list(q1.Name) # turns the dataframe column of fish names into a list
        q1 = ', '.join(q1) # joins them into a string

        q2 = df[(df.Rarity == 'fairly common') & (df[month]==True)]
        q2 = list(q2.Name)
        q2 = ', '.join(q2)

        q3 = df[(df.Rarity == 'uncommon') & (df[month]==True)]
        q3 = list(q3.Name)
        q3 = ', '.join(q3)

        q4 = df[(df.Rarity == 'scarce') & (df[month]==True)]
        img = list(q4.pngurl)[0] # Get img url of the first rare bug #adjust q# for rarity image
        q4 = list(q4.Name)
        q4 = ', '.join(q4)

        q5 = df[(df.Rarity == 'rare') & (df[month]==True)]
        q5 = list(q5.Name)
        q5 = ', '.join(q5)

        embed = discord.Embed(
            title = f'{month.upper()} Fish',
            colour = discord.Colour.teal()
        )

        embed.set_thumbnail(url = img)
        embed.add_field(name = 'Common', value = q1, inline = False)
        embed.add_field(name = 'Fairly Common', value = q2, inline = False)
        embed.add_field(name = 'Uncommon', value = q3, inline = False)
        embed.add_field(name = 'Scarce', value = q4, inline = False)
        embed.add_field(name = 'Rare', value = q5, inline = False)

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Fish(client))
