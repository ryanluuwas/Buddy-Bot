import discord
from discord.ext import commands
import random


#emoji list
uwu = '\U0001F97A'
cry = '\U0001F62D'
wink = '\U0001F609'
happy = '\U0001F604'
star = '\U0001F31F'
kiss = '\U0001F618'
yum = '\U0001F60B'

# Compliment response list
r = [f'You are the reason I am constantly smiling {happy}',
    f'You are so cute, puppies and baby seals send pictures of you to each other {uwu}',
    f'You are absolutely, astoundingly gorgeous and that is the least interesting thing about you.',
    f'I am happy you are around. Seeing you every day brightens my mood.',
    f'I love talking with you. Can we talk every day, please?',
    f'Every time I see you, my day gets better!',
    f'It is so impossible not to like you! I am your number one fan {wink}',
    f'If you were to leave, I would be very sad {cry} You mean a lot to me.',
    f"You're like hot air balloon — because being with you lifts me up {uwu}",
    f"You should write a book about how to be amazing — it would be the best seller!",
    f"You remind me of a luminous sphere of plasma floating in space — because you're a star {star}",
    f"If I could travel through all of time and space, I'd want to come hang out with you {kiss}",
    f"Your personality's like chocolate... sweet sweet sweet! {yum}"
    ]

class Compliment(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Compliment Cog is online')

    @commands.command()
    async def compliment(self, ctx, user: discord.User = None):
        if not user:
            await ctx.send(random.choice(r).lower())
        else:
            await ctx.send(f'hi {user.mention}-san, {random.choice(r).lower()}')



def setup(client):
    client.add_cog(Compliment(client))
