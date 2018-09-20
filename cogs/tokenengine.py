import discord
from discord.ext import commands

import random
import json
import os

#Extension Directories
EXTENSION_DIR = "cogs"
BIN_DIR = "bin/"
BUFFER_DIR = BIN_DIR+"buffer/"
CONFIG_DIR = BIN_DIR+"config/"
DATA_DIR = BIN_DIR+"data/"

#Embed Colour
EMBED_COLOUR = 0x00b3ff

os.chdir(r'D:/Data/Desktop/Bot/bot sanic 2.0')

#Channels
def get_channel(channels, channel_name):
    for channel in client.get_all_channels():
        if channel.name == channel_name:
            return channel
    return None


class TokenEngine:
    def __init__(self, client):
        self.tokenValue = 1
        self.goldenTokenChance = 100

        self.client = client

    async def on_member_join(self, member):
        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

        await self.checkUserHasEco(eco, member)

        with open('bin/data/eco/eco.json', 'w') as f:
            json.dump(eco, f)

    async def on_message(self, message):
        user = message.author

        with open('bin/config/eco/blacklistedusers.json', 'r') as f:
            blacklist = json.load(f)

        try:
            check = blacklist[user.id]
        except:
            pass

        else:
            return

        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

        await self.checkUserHasEco(eco, message.author)

        if random.randint(1, self.goldenTokenChance) == self.goldenTokenChance:
            goldenTokenGiven = True
            gtokensGiven = 1
        else:
            goldenTokenGiven = False
            gtokensGiven = 0

        tokensGiven = self.tokenValue

        await self.addTokens(eco, message.author, tokensGiven, gtokensGiven)

        with open('bin/data/eco/eco.json', 'w') as f:
            json.dump(eco, f)

    #-------------------------------------------------------------------------#


    async def checkUserHasEco(self, eco, user):
        try:
            test = eco[user.id]['name']
        except:
            print(" - added balance - ["+str(user)+"]")
            eco[user.id] = {}
            eco[user.id]['name'] = str(user)
            eco[user.id]['tokens'] = 0
            eco[user.id]['gtokens'] = 0
            eco[user.id]['rank'] = str(user.top_role)

        else:
            if eco[user.id]['rank'] != user.top_role:
                eco[user.id]['rank'] = str(user.top_role)

            if eco[user.id]['name'] != str(user):
                eco[user.id]['name'] = str(user)

    async def addTokens(self, eco, user, tokensGiven, gtokensGiven):
        print("- updated balance - ["+str(user)+"] ")
        eco[user.id]['tokens'] += tokensGiven
        eco[user.id]['gtokens'] += gtokensGiven

    #-------------------------------------------------------------------------#

    @commands.command(pass_context=True)
    async def tokenhelp(self, ctx):
        f = open(CONFIG_DIR+"broadcasts/tokens.txt", "r")
        string = f.read()
        categories = string.split("#")
        f.close()

        embed = discord.Embed(color=EMBED_COLOUR)
        embed.set_author(name = "Token Help", icon_url = self.client.user.avatar_url)
        embed.add_field(name="Token Value:", value=categories[0], inline=False)
        embed.add_field(name="Ranks & Prices:", value=categories[1], inline=False)
        embed.add_field(name="Commands:", value=categories[2], inline=False)

        await self.client.send_message(ctx.message.channel, embed=embed)




    @commands.command(pass_context=True)
    async def rankup(self, ctx):
        user = ctx.message.author
        userIconURL = user.avatar_url

        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

        curRank = user.top_role

        NORMIE = discord.utils.get(user.server.roles, name ="Normie")
        TOON_ARMY = discord.utils.get(user.server.roles, name ="Toon Army")
        TOON_SECRET_SERVICE = discord.utils.get(user.server.roles, name ="Toon Secret Service")


        if curRank == discord.utils.get(user.server.roles, name ="Daddy"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="YOU PICKED THE WRONG HOUSE FOOL", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Creator"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="You are a Creator, if you want Babe, talk to Toon, Not me!!", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Dr. Eggman"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="Dad? You Created me...", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Royal Babes"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="You are a Royal Babe!? What more do you want from me!?", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Babes"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="You are a Babe!? What more do you want from me!?", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)


        elif curRank == discord.utils.get(user.server.roles, name ="Sanic"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="I shouldn't be able to give myself roles... can i?", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Patreon"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="You might wanna spend some more money on Toon if you want a higher rank ;)", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="SJW"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="SJW'S DONT GET ROLES SUCKERRRRRRR", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Toon Secret Service"):
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="You are in the Secret Service... What more do you want from the Babes :(", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Normie"):
            if eco[user.id]['tokens'] >= 500:
                if eco[user.id]['gtokens'] >= 10:
                    await self.client.add_roles(user, TOON_ARMY)

                    embed = discord.Embed(color=EMBED_COLOUR)
                    embed.set_author(name = str(user), icon_url = userIconURL)
                    embed.add_field(name="New Rank:", value="Toon Army", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)

                    return
                else:
                    embed = discord.Embed(color=EMBED_COLOUR)
                    embed.set_author(name = str(user), icon_url = userIconURL)
                    embed.add_field(name="Not Enough Tokens", value="You do not have enough Golden Tokens to purchase this rank", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)
            else:
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name = str(user), icon_url = userIconURL)
                embed.add_field(name="Not Enough Tokens", value="You do not have enough Tokens to purchase this rank", inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)

        elif curRank == discord.utils.get(user.server.roles, name ="Toon Army"):
            if eco[user.id]['tokens'] >= 2500:
                if eco[user.id]['gtokens'] >= 25:
                    await self.client.add_roles(user, TOON_SECRET_SERVICE)

                    embed = discord.Embed(color=EMBED_COLOUR)
                    embed.set_author(name = str(user), icon_url = userIconURL)
                    embed.add_field(name="New Rank:", value="Toon Secret Service", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)

                    return
                else:
                    embed = discord.Embed(color=EMBED_COLOUR)
                    embed.set_author(name = str(user), icon_url = userIconURL)
                    embed.add_field(name="Not Enough Tokens", value="You do not have enough Golden Tokens to purchase this rank", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)
            else:
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name = str(user), icon_url = userIconURL)
                embed.add_field(name="Not Enough Tokens", value="You do not have enough Tokens to purchase this rank", inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)


        else:
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = str(user), icon_url = userIconURL)
            embed.add_field(name="Could Not Rankup", value="Your Balance is empty, You have an invalid role", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        with open('bin/data/eco/eco.json', 'w') as f:
            json.dump(eco, f)


    @commands.command(pass_context=True)
    async def tokens(self, ctx):
        user = ctx.message.author
        print("- balance requested by - [{}]".format(str(user)))

        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

        tokens = eco[user.id]['tokens']
        gtokens = eco[user.id]['gtokens']

        embed = discord.Embed(color=EMBED_COLOUR)
        embed.set_author(name = "Balance [{}]".format(str(user)), icon_url = user.avatar_url)
        embed.add_field(name="Tokens", value=tokens, inline=True)
        embed.add_field(name="Golden Tokens", value=gtokens, inline=True)
        await self.client.send_message(ctx.message.channel, embed=embed)


    @commands.command(pass_context=True)
    async def tokentop(self, ctx):
        server = ctx.message.server
        user = ctx.message.author

        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

        tokentop = []
        embed = discord.Embed(color=EMBED_COLOUR)
        embed.set_author(name = "Token Leaderboard", icon_url = self.client.user.avatar_url)

        amount = 0

        for member in server.members:

            try:
                name = eco[member.id]['name']
            except:
                pass
            else:
                username = str(member)
                tokens = eco[member.id]['tokens']
                gtokens = eco[member.id]['gtokens']

                tokentop.append([tokens,username,member, gtokens])

        sortedtokentop = sorted(tokentop, key=lambda x: x[0], reverse=True)

        while amount != 9:
            for element in sortedtokentop[:9]:
                if amount == 0:
                    user = element[2]
                    embed.add_field(name="1. **{}** Is in First place with **{}** Tokens!".format(element[1], element[0]), value="They also have {} Golden Tokens!".format(element[3]), inline=False)
                    embed.set_thumbnail(url=user.avatar_url)
                    amount +=1
                else:
                    embed.add_field(name=str(amount+1)+". "+str(element[1]), value=str(element[0]), inline=False)
                    amount +=1

        await self.client.send_message(ctx.message.channel, embed=embed)


    @commands.command(pass_context=True)
    async def seetokens(self, ctx):
        user = ctx.message.author
        recipient = ctx.message.mentions[0]

        if recipient == None:
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = "See Tokens", icon_url = user.avatar_url)
            embed.add_field(name=str(user)+" requested to see "+str(recipient)+"'s Balance", value="Failed, Error shown Below:", inline=False)
            embed.add_field(name="User Not Specified", value="You Must specify the user", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

            try:
                name = eco[recipient.id]['name']
            except:
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name = "See Tokens", icon_url = user.avatar_url)
                embed.add_field(name=str(user)+" requested to see "+str(recipient)+"'s Balance", value="Failed, Error shown Below:", inline=False)
                embed.add_field(name="Balance File Empty", value="The Users Balance is empty, this could be because they have not messaged in the server yet", inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)
            else:
                username = str(recipient)
                tokens = eco[recipient.id]['tokens']
                gtokens = eco[recipient.id]['gtokens']

                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name = "See Tokens", icon_url = user.avatar_url)
                embed.add_field(name=str(user)+" requested to see "+str(recipient)+"'s Balance", value="Current Balance:", inline=False)
                embed.add_field(name="Tokens", value=tokens, inline=False)
                embed.add_field(name="Golden Tokens", value=gtokens, inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)



    @commands.command(pass_context=True)
    async def givetokens(self, ctx):
        user = ctx.message.author
        recipient = ctx.message.mentions[0]

        args = ctx.message.content.split(" ")

        if recipient == None:
            print("^Recipient Not Specified")
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
            embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
            embed.add_field(name="Recipient Not Specified", value="You Must specify the Recipient", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        if len(args) != 3:
            print("^Amount Not Specified")
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
            embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
            embed.add_field(name="Amount Not Specified", value="You Must Specify 'Amount'", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

            try:
                name = eco[user.id]['name']
            except:
                print("^User balance empty")
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
                embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
                embed.add_field(name="Balance File Empty", value="The Recipients Balance is empty, this could be because they have not messaged in the server yet", inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)
            else:
                donator = user
                donatorTokens = eco[donator.id]['tokens']
                recipientTokens = eco[recipient.id]['tokens']

                try:
                    amount = int(args[2])
                except:
                    print("^Amount Not Integer")
                    embed = discord.Embed(color=EMBED_COLOUR)
                    embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
                    embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
                    embed.add_field(name="Amount Returned not an Integer", value="You Must Specify Amount as an Integer", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)
                else:
                    if donatorTokens < amount:
                        print("^Not Enough Tokens")
                        embed = discord.Embed(color=EMBED_COLOUR)
                        embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
                        embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
                        embed.add_field(name="Not Enough Tokens to give", value="You Must have enough tokens to give", inline=False)
                        await self.client.send_message(ctx.message.channel, embed=embed)

                    else:
                        print("^Completed")
                        eco[donator.id]['tokens'] -= amount

                        eco[recipient.id]['tokens'] += amount

                        with open('bin/data/eco/eco.json', 'w') as f:
                            json.dump(eco, f)

                        embed = discord.Embed(color=EMBED_COLOUR)
                        embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
                        embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Completed, Receipt shown Below:", inline=False)
                        embed.add_field(name="Tokens Deducted", value=amount, inline=False)
                        embed.add_field(name="Current Balance", value=donatorTokens-amount, inline=False)
                        await self.client.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    async def givegoldentokens(self, ctx):
        user = ctx.message.author
        recipient = ctx.message.mentions[0]

        args = ctx.message.content.split(" ")

        if recipient == None:
            print("^Recipient Not Specified")
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
            embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
            embed.add_field(name="Recipient Not Specified", value="You Must specify the Recipient", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        if len(args) != 3:
            print("^Amount Not Specified")
            embed = discord.Embed(color=EMBED_COLOUR)
            embed.set_author(name = "Give Tokens", icon_url = user.avatar_url)
            embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
            embed.add_field(name="Amount Not Specified", value="You Must Specify 'Amount'", inline=False)
            await self.client.send_message(ctx.message.channel, embed=embed)

        with open('bin/data/eco/eco.json', 'r') as f:
            eco = json.load(f)

            try:
                name = eco[user.id]['name']
            except:
                embed = discord.Embed(color=EMBED_COLOUR)
                embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
                embed.add_field(name="Balance File Empty", value="The Recipients Balance is empty, this could be because they have not messaged in the server yet", inline=False)
                await self.client.send_message(ctx.message.channel, embed=embed)
            else:
                donator = user
                donatorTokens = eco[donator.id]['tokens']
                recipientTokens = eco[recipient.id]['gtokens']

                try:
                    amount = int(args[2])
                except:
                    embed = discord.Embed(color=EMBED_COLOUR)
                    embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
                    embed.add_field(name="Amount Returned not an Integer", value="You Must Specify Amount as an Integer", inline=False)
                    await self.client.send_message(ctx.message.channel, embed=embed)
                else:
                    if donatorTokens < amount:
                        embed = discord.Embed(color=EMBED_COLOUR)
                        embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Failed, Error shown Below:", inline=False)
                        embed.add_field(name="Not Enough Golden Tokens to give", value="You Must have enough golden tokens to give", inline=False)
                        await self.client.send_message(ctx.message.channel, embed=embed)

                    else:
                        eco[donator.id]['tokens'] -= amount

                        eco[recipient.id]['tokens'] += amount

                        with open('bin/data/eco/eco.json', 'w') as f:
                            json.dump(eco, f)

                        embed = discord.Embed(color=EMBED_COLOUR)
                        embed.set_author(name = "Give Golden Tokens", icon_url = user.avatar_url)
                        embed.add_field(name=str(user)+" requested to give Golden Tokens to "+str(recipient), value="Completed, Receipt shown Below:", inline=False)
                        embed.add_field(name="Tokens Deducted", value=amount, inline=False)
                        embed.add_field(name="Current Balance", value=donatorTokens-amount, inline=False)
                        await self.client.send_message(ctx.message.channel, embed=embed)



def setup(client):
    client.add_cog(TokenEngine(client))
