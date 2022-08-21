import discord
from discord.ext import commands
import os
import random

cwd = os.getcwd()
publicImgPath = "/public/media/"

class Media(commands.Cog):
    """List available video clips"""

    def __init__(self, client):
        self.client = client

    def randomFile(self, path):
        return random.choice(os.listdir(cwd + path))

    async def sendFile(self, path, ctx):
        return await ctx.message.channel.send(file=discord.File(f".{path}"))

    @commands.command(help="Clip from Jæren rundt")
    async def edna(self, ctx):
        name = "edna"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command(help="Clip from Jæren rundt")
    async def elfin(self, ctx):
        name = "elfin"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command(help="Clip from Jæren rundt")
    async def jarle(self, ctx):
        name = "jarle"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command(help="Clip from Jæren rundt")
    async def john(self, ctx):
        name = "john"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command(help="Clip from Jæren rundt")
    async def sveinung(self, ctx):
        name = "sveinung"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command(help="Clip from Jæren rundt")
    async def arne(self, ctx):
        name = "arne"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

    @commands.command(help="Clip from Jæren rundt")
    async def moped(self, ctx):
        name = "moped"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)
    
    @commands.command(help="Clip from Rober Maddox")
    async def rocketman(self, ctx):
        name = "rocketman"
        path = f"{publicImgPath}{name}.mp4"
        await self.sendFile(path, ctx)

async def setup(client):
    await client.add_cog(Media(client))
