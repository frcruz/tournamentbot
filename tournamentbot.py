from tournament import Tournament
import os 
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print("Tournament Bot ready!")

@bot.command(name='tournament')
async def tournament(ctx, name): 
    tourny = Tournament(ctx.author, name)
    response = tourny.name + "tournament has been created! " + ctx.author.mention + " is the tournament admin!"
    await ctx.send(response)
@bot.command(name='status')
async def status(ctx):
    response = tourny.name + " is still in progress Rounds x/y"
    await ctx.send(response)

bot.run(TOKEN)