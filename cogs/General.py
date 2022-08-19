from discord.ext import commands

class General(commands.Cog):
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

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send('Pong!')

def setup(client):
    client.add_cog(General(client))