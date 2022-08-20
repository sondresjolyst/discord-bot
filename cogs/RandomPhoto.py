import discord
from discord.ext import commands
import os
import random

cwd = os.getcwd()
publicImgPath = "/public/img/"

class RandomPhoto(commands.Cog):

    def __init__(self, client):
        self.client = client

    def randomFile(self, path):
        return random.choice(os.listdir(cwd + path))

    async def sendFile(self, path, ctx):
        return await ctx.message.channel.send(file=discord.File(f".{path}" + self.randomFile(path)))

    @commands.command()
    async def banana(self, ctx):
        path = f"{publicImgPath}bananaCollection/"
        await self.sendFile(path, ctx)

    @commands.command()
    async def apple(self, ctx):
        path = f"{publicImgPath}appleCollection/"
        await self.sendFile(path, ctx)

    @commands.command()
    async def tomato(self, ctx):
        path = f"{publicImgPath}tomatoCollection/"
        await self.sendFile(path, ctx)

    @commands.command()
    async def mushroom(self, ctx):
        path = f"{publicImgPath}mushroomCollection/"
        await self.sendFile(path, ctx)

    @commands.command()
    async def grape(self, ctx):
        path = f"{publicImgPath}grapeCollection/"
        await self.sendFile(path, ctx)

    @commands.command()
    async def wood(self, ctx):
        path = f"{publicImgPath}woodCollection/"
        await self.sendFile(path, ctx)

    @commands.command()
    async def car(self, ctx):
        path = f"{publicImgPath}carCollection/"
        await self.sendFile(path, ctx)

    @commands.command()
    async def tractor(self, ctx):
        path = f"{publicImgPath}tractorCollection/"
        await self.sendFile(path, ctx)

def setup(client):
    client.add_cog(RandomPhoto(client))