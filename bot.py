import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')

bot = commands.Bot(command_prefix='$', help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="Skjævelandsbrunå"))

async def load_extensions():
    for filename in os.listdir('./cogs'):
        try:
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename[:-3]}')
        except:
            print(f'Unable to load {filename[:-3]}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

asyncio.run(main())
