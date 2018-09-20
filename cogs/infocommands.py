import discord
from discord.ext import commands

#Extension Directories
EXTENSION_DIR = "cogs"
BIN_DIR = "bin/"
BUFFER_DIR = BIN_DIR+"buffer/"
CONFIG_DIR = BIN_DIR+"config/"
DATA_DIR = BIN_DIR+"data/"

#Embed Colour
EMBED_COLOUR = 0x00b3ff

class InfoCommands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def info(self, ctx):
        f = open(CONFIG_DIR+"broadcasts/info.txt","r")
        string = f.read()
        categories = string.split("//")

        embed = discord.Embed(title=":question: - Bot Information", description="Some information about Sanic", color=EMBED_COLOUR)
        embed.add_field(name="Custom Written:", value=categories[0], inline=False)
        embed.add_field(name="In Development?", value=categories[1], inline=False)
        embed.add_field(name="Got any suggestions?", value=categories[2], inline=False)
        embed.add_field(name="Something wrong?", value=categories[3], inline=False)
        await client.send_message(ctx.message.channel, embed=embed)
        f.close()

    @commands.command(pass_context=True)
    async def rules(self, ctx):
        f = open(CONFIG_DIR+"broadcasts/rules.txt","r")
        string = f.read()
        categories = string.split("#")

        embed = discord.Embed(title=":cop: - Rules", description="Rules of the server, failure to comply will result in sanctions", color=EMBED_COLOUR)
        embed.add_field(name="Bannable Offences: ", value=categories[0], inline=False)
        embed.add_field(name="Warnable Offences: ", value=categories[1], inline=False)
        embed.add_field(name="Rule Explanations: ", value=categories[2], inline=False)
        embed.add_field(name=":thinking: ", value=categories[3], inline=False)
        await client.send_message(ctx.message.channel, embed=embed)

        f.close()

    @commands.command(pass_context=True)
    async def toon(self, ctx):
        f = open(CONFIG_DIR+"broadcasts/toon.txt", "r")
        string = f.read()
        categories = string.split("#")

        embed = discord.Embed(title=":crown:  - Toon", description="Links to his Socials and Youtube", color=EMBED_COLOUR)
        embed.add_field(name="Youtube:", value=categories[0], inline=False)
        embed.add_field(name="Instagram:", value=categories[1], inline=False)
        embed.add_field(name="Twitter:", value=categories[2], inline=False)
        embed.add_field(name="Patreon:", value=categories[3], inline=False)
        await client.send_message(ctx.message.channel, embed=embed)

def setup(client):
    client.add_cog(InfoCommands(client))
