import discord
from discord.ext import commands
import datetime
import json

#Extension Directories
EXTENSION_DIR = "cogs"
BIN_DIR = "bin/"
BUFFER_DIR = BIN_DIR+"buffer/"
CONFIG_DIR = BIN_DIR+"config/"
DATA_DIR = BIN_DIR+"data/"

#Embed Colour
EMBED_COLOUR = 0x00b3ff

def get_channel(channels, channel_name):
    for channel in channels:
        if channel.name == channel_name:
            return channel

        if channel.id == channel_name:
            return channel
    return None

class AdminCommands:
    def __init__(self, client):
        self.client = client

    async def checkowner(self, member, ctx):
        user = ctx.message.author
        if user.id == "234770387848658948":
            return True

        if user.id == "324043168280608768":
            return True

        elif user.id == "224995739716026383":
            return True

        else:
            embed = discord.Embed(title="Permission Error", description="You do not Host the Bot", color=EMBED_COLOUR)
            embed.add_field(name="Tag Needed:", value="BotOwner", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

    async def checkadmin(self, member, ctx):
        if await self.checkowner(member, ctx):
            return True

        if discord.utils.get(member.server.roles, name="Babes") in member.roles:
            return True

        else:

            embed = discord.Embed(title="Permission Error", description="You do not have sufficient Permissions needed to run this command", color=EMBED_COLOUR)
            embed.add_field(name="Tag Needed:", value="Babes", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

            return False

    async def checksanic(self, member, ctx):
        if await self.checkowner(member, ctx):
            return True

        if member.top_role == discord.utils.get(member.server.roles, name ="Sanic"):
            return True

    @commands.command(pass_context=True)
    async def admincommands(self, ctx):
        f = open(CONFIG_DIR+"broadcasts/admincommands.txt","r")
        string = f.read()
        categories = string.split("#")

        embed = discord.Embed(title=":tools: - Admin Commands", description="List of Admin Commands", color=EMBED_COLOUR)
        embed.add_field(name="Sanic Commands", value=categories[0], inline=False)
        embed.add_field(name="Dyno Commands:", value=categories[1], inline=False)
        embed.add_field(name="Notes:", value=categories[2], inline=False)
        await self.client.send_message(ctx.message.channel, embed=embed)
        f.close()

    @commands.command(pass_context=True)
    async def warns(self, ctx):
        user = ctx.message.author

        if await self.checkadmin(user, ctx):
            recipient = ctx.message.mentions[0]

            with open('bin/data/sanctions/warns.json', 'r') as f:
                warns = json.load(f)

            try:
                test = warns[recipient.id]['name']
            except:
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name="No Warns Found for {}".format(str(recipient)), icon_url = recipient.avatar_url)
                await self.client.send_message(ctx.message.channel, embed=embed)

            else:
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name="Warns Found for {}".format(str(recipient)), icon_url = recipient.avatar_url)
                index = 1

                for element in warns[recipient.id]:
                    if index != 1:
                        embed.add_field(name="Warning: {}".format(str(index)), value=warns[recipient.id][str(element)], inline=True)
                        index += 1

                await self.client.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    async def warn(self, ctx):
        user = ctx.message.author

        if await self.checkadmin(user, ctx):
            recipient = ctx.message.mentions[0]
            blacklist = "480805548158353418"
            for blacklisteduser in blacklist:
                if recipient.id == blacklisteduser:
                    embed = discord.Embed(title="Permission Error", description="This User cannot be warned", color=EMBED_COLOUR)
                    embed.add_field(name="Tag Needed:", value="canWarn", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)
                    return

            messageContent = ctx.message.content
            args = messageContent.split(" ")

            stringlist = args[2:]
            warning = ""

            for element in stringlist:
                warning += element+" "

            with open('bin/data/sanctions/warns.json', 'r') as f:
                warns = json.load(f)

            try:
                test = warns[recipient.id]['name']
            except:
                print("")
                warns[recipient.id] = {}
                warns[recipient.id]['name'] = str(recipient)
                warns[recipient.id]['warn1'] = warning
                warncount = 1

            else:
                print(warns[recipient.id])
                index = 0
                for element in warns[recipient.id]:
                    print(element)
                    index += 1

                if index == 1:
                    warns[recipient.id]['warn1'] = warning
                    warncount = 1

                elif index == 2:
                    warns[recipient.id]['warn2'] = warning
                    warncount = 2

                elif index == 3:
                    warns[recipient.id]['warn3'] = warning
                    warncount = 3

                elif index == 4:
                    if self.checkowner(user, ctx):
                        warns[recipient.id]['ban'] = warning

                        embed = discord.Embed(color=EMBED_COLOUR)
                        embed.set_author(name="{} Has Been Banned".format(str(recipient)), icon_url = recipient.avatar_url)
                        embed.add_field(name="Banned By:", value=str(user), inline=True)
                        embed.add_field(name="Ban Reason:", value=warning, inline=True)
                        await self.client.send_message(ctx.message.channel, embed=embed)

                        embed = discord.Embed(color=EMBED_COLOUR)
                        embed.set_author(name="You Have Been Banned", icon_url = recipient.avatar_url)
                        embed.add_field(name="Banned By:", value=str(user), inline=True)
                        embed.add_field(name="Ban Reason:", value=warning, inline=True)
                        await self.client.send_message(recipient, embed=embed)

            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name="{} Has Been Warned".format(str(recipient)), icon_url = recipient.avatar_url)
            embed.add_field(name="Warned By:", value=str(user), inline=True)
            embed.add_field(name="Warn Reason:", value=warning, inline=True)
            embed.add_field(name="Warns Left Before Ban", value=str(3-warncount), inline=True)
            await self.client.send_message(ctx.message.channel, embed=embed)

            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name="You Have Been Warned...", icon_url = recipient.avatar_url)
            embed.add_field(name="Warned By:", value=str(user), inline=True)
            embed.add_field(name="Warn Reason:", value=warning, inline=True)
            embed.add_field(name="Warns Left Before Ban", value=str(3-warncount), inline=True)
            await self.client.send_message(recipient, embed=embed)

            with open('bin/data/sanctions/warns.json', 'w') as f:
                json.dump(warns, f)

            print("- user warned [{}][{}] - warned by [{}]".format(str(recipient),warning,str(user)))



    @commands.command(pass_context=True)
    async def say(self, ctx):
        user = ctx.message.author
        blacklist = "335643611188297733","450442736303210496"
        if await self.checkadmin(user, ctx):
            for blacklisteduser in blacklist:
                if user.id == blacklisteduser:
                    embed = discord.Embed(title="Permission Error", description="You are blocked from using this command", color=EMBED_COLOUR)
                    embed.add_field(name="Tag Needed:", value="notBlacklisted", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)
                    return

            args = ctx.message.content.split(" ")

            channelid = args[1]
            channelid = channelid.replace("<","")
            channelid = channelid.replace(">","")
            channelid = channelid.replace("#","")

            stringlist = args[2:]
            string = ""

            for element in stringlist:
                string += element+" "

            channel = get_channel(ctx.message.server.channels, channelid)

            await self.client.send_message(channel, content=string)

    @commands.command(pass_context=True)
    async def blacklist(self, ctx):
        user = ctx.message.author
        recipient = ctx.message.mentions[0]
        if await self.checkowner(user, ctx):
            with open('bin/config/eco/blacklistedusers.json', 'r') as f:
                blacklist = json.load(f)

            if blacklist[recipient.id]["name"] == None:
                blacklist[recipient.id] = {}
                blacklist[recipient.id]["name"] = str(recipient)
                blacklist[recipient.id]["blacklist"] = True

                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name = str(recipient), icon_url = recipient.avatar_url)
                embed.add_field(name="User Blacklisted", value="Admin: "+str(user), inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)

                print("[{}] - User blacklisted : Admin [{}]".format(str(recipient),str(user)))

            else:
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name = str(recipient), icon_url = recipient.avatar_url)
                embed.add_field(name="User Already Blacklisted", value="Admin: "+str(user), inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)

                print("[{}] - User Already blacklisted : Admin [{}]".format(str(recipient),str(user)))

            with open('bin/config/eco/blacklistedusers.json', 'w') as f:
                json.dump(blacklist, f)

    @commands.command(pass_context=True)
    async def changelog(self, ctx):
        user = ctx.message.author

        if await self.checkowner(user, ctx):
            temp = ctx.message.content
            temp2 = temp.split(" -")

            now = datetime.datetime.now()
            changetime = str(now.strftime("%Y-%m-%d"))

            changetitle = str(temp2[1])
            change = str(temp2[2])

            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = "Bot Updated!", icon_url = self.client.user.avatar_url)
            embed.add_field(name="[{}] - Feature Added: {}".format(changetime, changetitle), value=change, inline=False)
            await self.client.send_message(get_channel(self.client.get_all_channels(),"changelog"), embed=embed)



def setup(client):
    client.add_cog(AdminCommands(client))
