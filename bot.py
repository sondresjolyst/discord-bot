import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
token = os.getenv('token')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')
    if message.content.startswith('$banana'):
        cwd = os.getcwd()
        randomBanana = random.choice(os.listdir(cwd + "/public/img/bananaCollection"))
        await message.channel.send(file=discord.File('./public/img/bananaCollection/' + randomBanana))

client.run(token)
