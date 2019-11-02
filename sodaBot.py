# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='soda', help='Responds with a random soda suggestion')
async def soda(ctx):
    soda_ideas = [
        'Dr.Pepper',
        'Dr.PibbXtra',
        'Sprite',
        'Mountain Dew',
        'Coke',
        'Fanta Orange',
        'A&W Root Beer',
    ]

    response = random.choice(soda_ideas)
    await ctx.send(response)

bot.run(token)