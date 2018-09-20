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

class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def usage(self, ctx):
        args = ctx.message.content

        if args == ">HELP":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">help", value="Example: >help", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">COMMANDS":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">commands", value="Example: >commands", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">INFO":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">info", value="Example: >info", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">RULES":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">rules", value="Example: >rules", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">TOON":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">toon", value="Example: >toon", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">TOKENHELP":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">tokenhelp", value="Example: >tokenhelp", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">TOKENTOP":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">tokentop", value="Example: >tokentop", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">TOKENS":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">tokens", value="Example: >tokens", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">SEETOKENS":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">seetokens", value="Example: >seetokens -@user", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">GIVETOKENS":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">givetokens", value="Example: >givetokens @user -tokenamount x -gtokenamount x (x = Amount)", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">RANKUP":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">rankup", value="Example: >rankup (No rank needs to be specified, it will rank you up to the next rank avaliable)", inline=False)
            await self.client.send_message(message.channel, embed=embed)

        elif args == ">USAGE":
            embed = discord.Embed(title="Command Usage Guide", description="Clarification on correct command usage", color=EMBED_COLOUR)
            embed.add_field(name=">usage", value="Example: >usage ''>command'", inline=False)
            await self.client.send_message(message.channel, embed=embed)


    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        f = open(CONFIG_DIR+"broadcasts/help.txt","r")
        string = f.read()
        categories = string.split("#")

        embed = discord.Embed(title=":children_crossing: - Help", description="Some tips to help you around the server", color=EMBED_COLOUR)
        embed.add_field(name="Welcome! ", value=string, inline=False)
        await self.client.send_message(author, embed=embed)
        await self.client.send_message(ctx.message.channel,content="@"+str(author)+" Check your DM's!")
        f.close()


    @commands.command(pass_context=True)
    async def faq(self, ctx):
        author = ctx.message.author

        f = open(CONFIG_DIR+"broadcasts/faq.txt","r")
        string = f.read()
        categories = string.split("#")

        embed = discord.Embed(title=":gear: : - FAQ", description="Frequently Asked Questions", color=EMBED_COLOUR)
        embed.add_field(name="Why does the bot not do anything when i do a command?", value=categories[0], inline=False)
        embed.add_field(name="Why does the bot say i have no balance?", value=categories[1], inline=False)
        embed.add_field(name="If I change my discord name, will that affect my balance?", value=categories[2], inline=False)
        embed.add_field(name="If i have a question about the bot, who should i ask?", value=categories[3], inline=False)
        embed.add_field(name="Can i suggest a question for this section?", value=categories[4], inline=False)

        await self.client.send_message(author, embed=embed)
        await self.client.send_message(ctx.message.channel,content="@"+str(author)+" Check your DM's!")

        f.close()


    @commands.command(pass_context=True)
    async def commands(self, ctx):
        author = ctx.message.author

        f = open(CONFIG_DIR+"broadcasts/commands.txt","r")
        string = f.read()
        categories = string.split("#")

        embed = discord.Embed(title=":gear: : - Commands", description="Commands you can use around the server", color=EMBED_COLOUR)
        embed.add_field(name="General Commands: ", value=categories[0], inline=False)
        embed.add_field(name="Token Commands: ", value=categories[1], inline=False)

        await self.client.send_message(author, embed=embed)
        await self.client.send_message(ctx.message.channel,content="@"+str(author)+" Check your DM's!")

        f.close()

def setup(client):
    client.add_cog(Commands(client))
