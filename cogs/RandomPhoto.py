import discord
from discord.ext import commands
import os
import random

cwd = os.getcwd()
publicImgPath = "/public/img/"

class RandomPhoto(commands.Cog):
    """List available collections"""

    def __init__(self, client):
        self.client = client

    def randomFile(self, path):
        return random.choice(os.listdir(cwd + path))

    async def sendFile(self, path, ctx):
        return await ctx.message.channel.send(file=discord.File(f".{path}" + self.randomFile(path)))

    @commands.command(help="Random banana")
    async def banana(self, ctx):
        try:
            path = f"{publicImgPath}bananaCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random apple")
    async def apple(self, ctx):
        try:
            path = f"{publicImgPath}appleCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random tomato")
    async def tomato(self, ctx):
        try:
            path = f"{publicImgPath}tomatoCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random mushroom")
    async def mushroom(self, ctx):
        try:
            path = f"{publicImgPath}mushroomCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random grape")
    async def grape(self, ctx):
        try:
            path = f"{publicImgPath}grapeCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random wood")
    async def wood(self, ctx):
        try:
            path = f"{publicImgPath}woodCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random car")
    async def car(self, ctx):
        try:
            path = f"{publicImgPath}carCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random tractor")
    async def tractor(self, ctx):
        try:
            path = f"{publicImgPath}tractorCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')
    
    @commands.command(help="Random stone")
    async def stone(self, ctx):
        try:
            path = f"{publicImgPath}stoneCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

    @commands.command(help="Random cat")
    async def cat(self, ctx):
        try:
            path = f"{publicImgPath}catCollection/"
            await self.sendFile(path, ctx)
        except:
            await ctx.channel.send('There was an error!')

async def setup(client):
    await client.add_cog(RandomPhoto(client))
