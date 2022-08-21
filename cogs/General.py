import datetime
from discord.ext import commands
from discord.errors import Forbidden

class General(commands.Cog):
    """General commands"""

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     print(message.author.id)
    #     if (message.author.id == 442678097393876992):
    #         msg_content = message.content.lower()

    #         curseWord = ['> :banana:']

    #         if any(word in msg_content for word in curseWord):
    #             await message.delete()

    @commands.Cog.listener(name='on_command')
    async def print(self, ctx):
        dn = datetime.datetime.now()
        ds = dn.strftime("%d.%m.%Y - %H:%M:%S")
        server = ctx.guild.name
        user = ctx.author
        command = ctx.command
        print(f'[{ds}] Server: {server} - User: {user} - Command: {command}')

    @commands.command(help="Will return Pong!")
    async def ping(self, ctx):
        try:
            await ctx.channel.send('Pong!')
        except Exception as err:
            print(err)
            await ctx.channel.send('There was an error!')

async def setup(client):
    await client.add_cog(General(client))
