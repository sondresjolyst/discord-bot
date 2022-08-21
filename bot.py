import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')

bot = commands.Bot(command_prefix='$', help_command=None, intents=discord.Intents.default())

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="Skjævelandsbrunå", url="https://www.google.com"))

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

  else:
    print(f'Unable to load {filename[:-3]}')

bot.run(token)
