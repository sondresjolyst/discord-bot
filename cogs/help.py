import discord
from discord.ext import commands
from discord.errors import Forbidden

async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("seems like I can't send embeds. Please check permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)

class Help(commands.Cog):
    """Sends this help message"""

    def __init__(self, client):
        self.client = client

    @commands.command(help="Shows all modules of that client")
    async def help(self, ctx, *input):
	
        prefix = self.client.command_prefix

        if not input:
            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description=f'Use `{prefix}help <module>` to gain more information about that module '
                                            f':smiley:\n')

            cogs_desc = ''
            for cog in self.client.cogs:
                cogs_desc += f'`{cog}` {self.client.cogs[cog].__doc__}\n'

            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            commands_desc = ''
            for command in self.client.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            emb.add_field(name="About", value=f"Visit https://github.com/Digital-Utvinning/Discord.py-example to submit ideas or bugs.")

        # block called when one cog-name is given
        elif len(input) == 1:
            for cog in self.client.cogs:
                if cog.lower() == input[0].lower():
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.client.cogs[cog].__doc__,
                                        color=discord.Color.green())

                    for command in self.client.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    break
            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                    color=discord.Color.orange())

        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once :sweat_smile:",
                                color=discord.Color.orange())

        else:
            emb = discord.Embed(title="It's a magical place.",
                                description="Ay how did you come down here? please report it to"
                                            "https://github.com/Digital-Utvinning/Discord.py-example/issues\n",
                                color=discord.Color.red())

        await send_embed(ctx, emb)

def setup(client):
    client.add_cog(Help(client))
