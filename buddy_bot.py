# Packages
import discord # standard set up
from discord.ext import commands # standard package for commands

import random
import pandas as pd
import json
import os

from os import listdir # for cogs
from os.path import isfile, join # for cogs

import csv

# Start of Discord Bot
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client = commands.Bot(command_prefix = commands.when_mentioned_or('~'))
client.remove_command('help') # removes default help command

# Load Cogs
cogs_dir = "cogs"
if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            client.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

@client.event
async def on_ready(): # When Bot is ready
    print('Bot is ready.')

# --------------- Command section -------------------
# Ping check commands
@client.command()
async def ping(ctx): # when user types the function name with the command command_prefix
    await ctx.send(f'{round(client.latency * 1000)}ms')

# ----------- Help Section ----------------------
@client.command()
async def help(ctx):

    embed = discord.Embed(
        title = 'Command Lines',
        description = 'A simple Animal Crossing: New Horizon bot. Seasonal information queried are for the Northern Hemisphere players. \n',
        #colour = discord.Colour.blue()
        colour = discord.Colour(0xFFC0CB)
    )
    embed.add_field(name = '~about {villager}', value = 'Returns information about a villager', inline = False)
    embed.add_field(name = '~bug {bug name}', value = 'Returns information about a bug', inline = False)
    embed.add_field(name = '~bug_month {month}', value = 'Returns information about the available bugs in {month}.', inline = False)
    embed.add_field(name = '~fish {fish name}', value = 'Returns information about a fish', inline = False)
    embed.add_field(name = '~fish_month {month}', value = 'Returns information about the available fishes in {month}', inline = False)
    embed.add_field(name = '~compliment {@mention}', value = 'Returns a compliment to you or @mention', inline = False)
    embed.add_field(name = '~profile {@mention}', value = "View user's Nook Bay Profile", inline = False)
    embed.add_field(name = '~upvote {@mention}', value = 'Show your appreciation for someone by upvoting him/her! (Once a day)', inline = False)
    embed.add_field(name = '~downvote {@mention}', value = 'Show your dissatisfcation for someone by downvoting him/her (Once a day)', inline = False)
    embed.add_field(name = '~ping', value = 'Returns ping', inline = False)
    embed.set_footer(text = f'Please private message my senpai deruluu#2131 any bugs!')

    await ctx.send(embed = embed)

# -------- Profanity Filter ------------ #

os.chdir(r"C:\Users\Ryan\Desktop\Discord")

# Opens Bad word list txt file and stores it into a list
with open('badwords.txt') as f:
    badwords = [row[0] for row in csv.reader(f, delimiter = '\t')]

@client.event
async def on_message(message):

    # Opens JSON FILE for Brownie Cog
    with open('users.json', 'r') as f:
        users = json.load(f)

    # Checks if User is not in the JSON file
    if str(message.author.id) not in users:
        users[message.author.id] = {}
        users[message.author.id]['Star Bits'] = 0
        users[message.author.id]['Reports'] = 0
        users[message.author.id]['Rank'] = 'Novice Astronomer'

    # Saves Json files
    with open('users.json', 'w+') as f:
        json.dump(users, f)

    await client.process_commands(message) # VERY IMPORTANT SO IT WON'T BREAK THE COMMANDS

    channel = client.get_channel(707356794229358633)
    if message.author == client.user: #check if user is not a bot.
        return
    string = message.content.split() #splits message into a list

    for word in string: # for each word in the split message
        if word in badwords: # check if word is in the badwords

            await message.delete() # deletes message
            await message.channel.send(f"{message.author.mention} your message has been deleted because it was not nice!") # sends message to channel where profanity was found
            embed = discord.Embed( # creates embed message to send to destinated text channel
                title = f"Found at Text Channel : {message.channel}",
                description = f"{message.content}",
                colour = discord.Colour.blue()
                #colour = discord.Colour(0xFFC0CB)
            )
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            embed.set_footer(text = f"This message was created on {message.created_at}")

            await channel.send(embed = embed)

    # -------------------------- #

client.run(TOKEN)

client.run(TOKEN) # Buddy bot's token
