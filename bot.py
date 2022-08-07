import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
token = os.getenv('token')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await message.channel.send('Working!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

client.run(token)
