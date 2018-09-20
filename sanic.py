#Discord.py Libraries Import
import discord
from discord.ext.commands import Bot
from discord.ext import commands
#asynco Libraries Import
import asyncio
#other module Libraries Import
import json
import random
import time
import datetime

import os

print(os.getcwd())

TOKEN = "NDgwODA1NTQ4MTU4MzUzNDE4.DltIuQ.rD258sO3ZRjBE8gOxZBEXwg09WQ"

#Extension Directories
EXTENSION_DIR = "cogs"
BIN_DIR = "bin"
BUFFER_DIR = BIN_DIR+"/buffer"
CONFIG_DIR = BIN_DIR+"/config"
DATA_DIR = BIN_DIR+"/data"

#Embed Colour
EMBED_COLOUR = 0x00b3ff


#Extensions
extensions = [
'admincommands',
'helpcommands',
'infocommands',
'tokenengine'
]

Client = discord.Client()
client = commands.Bot(command_prefix = ">")
client.remove_command('help')

#Channels
def get_channel(channels, channel_name):
    for channel in client.get_all_channels():
        if channel.name == channel_name:
            return channel
    return None


@client.command(pass_context=True)
async def modules(ctx):#cogs list
    embed = discord.Embed(title="Loaded Modules : :gear:", description="List of 'cogs'/'extensions' loaded into the bot currently", color=EMBED_COLOUR)

    for extension in extensions:
        if "cogs."+extension not in client.extensions:
            embed.add_field(name=extension, value=":x: : unloaded", inline=False)
        else:
            embed.add_field(name=extension, value=":white_check_mark: : loaded", inline=False)

    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def load(ctx, extension):
    embed = discord.Embed(color=EMBED_COLOUR)

    try:
        client.load_extension(EXTENSION_DIR + "." + extension)
        print('Loaded [{}]'.format(extension))
        embed.add_field(name="Extension Loaded", value=extension, inline=False)

    except Exception as error:
        print('{} cannot be unloaded -ERROR:[{}]'.format(extension, error))

        embed.add_field(name="Extension Failed to Load", value=extension, inline=False)

    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def unload(ctx, extension):
    embed = discord.Embed(color=EMBED_COLOUR)

    try:
        client.unload_extension(EXTENSION_DIR + "." + extension)
        print('unloaded [{}]'.format(extension))
        embed.add_field(name="Extension Unloaded", value=extension, inline=False)
    except Exception as error:
        print('{} cannot be unloaded -ERROR:[{}]'.format(extension, error))
        embed.add_field(name="Extension Failed Unload", value=extension, inline=False)

    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def rulesaccept(ctx):
    user = ctx.message.author
    NORMIE = discord.utils.get(user.server.roles, name ="Normie")
    await client.add_roles(user, NORMIE)

    await client.send_message(ctx.message.channel, content="Thank You <@{}> for Accepting the #rules".format(str(user.id)))

@client.event
async def on_member_join(member):
    print("- member joined - [{}]".format(str(member)))
    print("- ^Sending Rules, awaiting >rulesaccept...")

    channel = get_channel(client.get_all_channels(), "welcome-messages")

    f = open(CONFIG_DIR+"/broadcasts/rules.txt","r")
    string = f.read()
    categories = string.split("#")

    embed = discord.Embed(title=":cop: - Rules", description="Rules of the server, failure to comply will result in sanctions", color=EMBED_COLOUR)
    embed.add_field(name="Bannable Offences: ", value=categories[0], inline=False)
    embed.add_field(name="Warnable Offences: ", value=categories[1], inline=False)
    embed.add_field(name="Rule Explanations: ", value=categories[2], inline=False)
    embed.add_field(name=":thinking: ", value=categories[3], inline=False)

    await client.send_message(channel, content = "Welcome <@{}>, Please read the #rules before you continue! Accept the rules by doing the command >rulesaccept".format(str(member.id)), embed=embed)
    f.close()


@client.event
async def on_ready():
    CONSOLE_CHANNEL = get_channel(client.get_all_channels(),"bot-console")

    async for msg in client.logs_from(CONSOLE_CHANNEL):
        await client.delete_message(msg)

    await client.change_presence(game=discord.Game(name='>help', type=1))

    embed = discord.Embed(color=EMBED_COLOUR)
    embed.set_author(name="ONLINE", icon_url = client.user.avatar_url)
    embed.add_field(name="What do i do?", value="type >commands in #bot-channel to see what commands are avaliable", inline=False)
    await client.send_message(CONSOLE_CHANNEL, embed=embed)



if __name__ == "__main__":
    for extension in extensions:
        client.load_extension(EXTENSION_DIR + "." + extension)
        print('Loaded [{}]'.format(extension))

        #try:
        #    client.load_extension(EXTENSION_DIR + "." + extension)
        #    print('Loaded [{}]'.format(extension))
        #except Exception as error:
        #    print('{} cannot be loaded -ERROR:[{}]'.format(extension, error))

    client.run(TOKEN, bot=True, reconnect=True)
