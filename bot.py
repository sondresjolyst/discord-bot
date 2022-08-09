import os
import discord
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
        await message.channel.send(new Discord.Attachment('./public/img/banana.jpg') )

client.run(token)
