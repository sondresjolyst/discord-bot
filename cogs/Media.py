import discord
from discord.ext import commands
import os
import random

cwd = os.getcwd()
publicImgPath = "/public/media/"

class Media(commands.Cog):

    def __init__(self, client):
        self.client = client

    def randomFile(self, path):
        return random.choice(os.listdir(cwd + path))

    async def sendFile(self, path, ctx):
        return await ctx.message.channel.send(file=discord.File(f".{path}"))

    @commands.command()
    async def edna(self, ctx):
        name = "edna"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command()
    async def elfin(self, ctx):
        name = "elfin"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command()
    async def jarle(self, ctx):
        name = "jarle"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command()
    async def john(self, ctx):
        name = "john"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command()
    async def sveinung(self, ctx):
        name = "sveinung"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command()
    async def arne(self, ctx):
        name = "arne"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command()
    async def moped(self, ctx):
        name = "moped"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

async def setup(client):
    await client.add_cog(Media(client))
