import json
from redbot.core import commands
from discord.utils import get
from discord.ext import tasks
import discord
import requests
from time import sleep
import os
import urllib.request
import csv
import random
import time
import datetime


#password=""
#RegionalNation=""

intro="""Now entering the TNP citizen, Deputy Minister of Defense,
Maker of so many card tools and several R/D ones too, NS Trading cards & Potato Alliance moderator,
Former Epic Rarity, 4th most valuable deck, (7x) Card Olympics Host, Member of Petz, Commended by the SC,
Ex-General of Mordor, Overall NPA Legend, Fastest Trader in the Midwest, (1x) SC Author, Potato General,
He Who Bested so many other traders using TCALS, Supreme Owner of many card farms and cards,
Anti-Fascist King, NSTC Prize distributor, Big Farma founder, he who nuked Noahs Almighty Second Country,
Nine thousand "Absolute Fucking Godgamer" three"""
lasttarg="\n"
target=[]

class HereCog(commands.Cog):
    Jointlist=[]
    reglist=[]
    lasttarg="\n"
    password=""
    RegionalNation=""
    hits=[]
    targets=[]

    def __init__(self, bot):
        self.bot = bot
        self.bot.target=[]
        self.bot.tarcount=int(0)
        self.password=""
        self.RegionalNation=""

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send("Welcome! Are you a TNPer or visitor? Have you ever thought about joining the NPA?  Let me know by saying NPA.")
            await channel.send("If you have already applied please link your application")


    @commands.has_role('NPA Officer')
    @commands.command(pass_context=True,aliases=['SDP'])
    async def StartDailyPile(self,ctx):
        await ctx.send("This can take a few momements")
        response = requests.get("https://esfalsa.github.io/puree/data/detags.csv")
        if response.status_code == 200:
            csv_lines = response.text.splitlines()
            csv_reader = csv.reader(csv_lines, delimiter=",")
            data = []
            for row in csv_reader:
                data.append(row)
            del data[0]
            if not len(data) > 0:
                await ctx.send("The world is quite there are no tags left")
            while len(data) > 0:
                tar = random.choice(data)
                if not "WFE" in tar[1]:
                    data.remove(tar)
                else:
                    await ctx.send("Hello and welcome to a daily pile these are easy ops all you have to do is slide your WA nation in and endorce the point")
                    await ctx.send(f"**Target**: {tar[0]} **Last Minor update time:** {tar[3]} **Last Major update time:** {tar[5]} **Linky for the lazy:** {tar[7]}. Once you are in please say DP_in, this lets me track who is particiapting each time")
                    await ctx.send("Don't forgot to ping Daily Pile  role to get folks attention.  If you would like the Daily Pile role just say join_DP and I'll add it shortly")
                    channel = ctx.guild.get_channel(830554742169272362) # Replace channel_id with the actual ID of the channel you want to send the message to
                    await channel.send(f"**__Daily Pile__** \n lead by {ctx.author.mention} \n {tar[7]}")
                    data = []
        else:
            await ctx.send("Failed to fetch the CSV file")

    @commands.command(pass_context=True,aliases=['dp_in'])
    async def DP_in(self,ctx):
        channel = ctx.guild.get_channel(830554742169272362) # Replace channel_id with the actual ID of the channel you want to send the message to
        await channel.send(f"{ctx.author.mention} Daily Pile")


    @commands.command()
    async def mission(self,ctx):
        await ctx.send("https://docs.google.com/spreadsheets/d/12l7zoYXrV7L_5uXM5HeVoe93ZBU70ypYf3jS1I0TZuE/edit#gid=577970735")



    @commands.has_role('High Command')
    @commands.command(aliases=['Broadcast'])
    async def broadcast1(self,ctx,*,args):
        output = args
        output = output + "\n This is an automated messsage sent by "+ctx.author.mention+" please respond to them!"
        role=discord.utils.get(ctx.guild.roles, name="NPA Soldier")
        for m in ctx.guild.members:
            if role in m.roles:
                try:
                    await m.send(output)
                except Exception as e:
                    await ctx.send(e)
                    await ctx.send(m)
        await ctx.send("Done you should have gotten it by now")


    @commands.command(pass_context=True,aliases=['NPA'])
    async def npa(self, ctx):
        await ctx.send("""
You can apply to join the North Pacific Army military force of the North Pacific, here: https://forum.thenorthpacific.org/topic/9145375
""")

    @commands.command()
    async def test(self, ctx):
        """This is to see if the Cog is loaded correctly"""
        await  ctx.send("I work")

    @commands.command(pass_context=True,aliases=['join_dp','Join_DP'])
    async def join_DP(self,ctx):
        await ctx.send("adding role now")
        member = ctx.author
        var = discord.utils.get(ctx.guild.roles, name = "Daily Pile")
        # This is the code needed to give a user a role
        member = ctx.message.author # Member object that you want to add the role to
        await member.add_roles(var) # Adds the role to the member


    @commands.has_role('NPA Soldier')
    @commands.command(pass_context=True,aliases=['here'])
    async def join(self, ctx):
        """Adds the Mini Ops role"""
        member = ctx.author
        var = discord.utils.get(ctx.guild.roles, name = "miniops")
        # This is the code needed to give a user a role
        member = ctx.message.author # Member object that you want to add the role to
        await member.add_roles(var) # Adds the role to the member
        given_name="spiderweb"
        channel = discord.utils.get(ctx.guild.channels, name=given_name)
        channel_id = channel.id
        channel_out = ctx.guild.get_channel(channel_id)
        if "9003" in ctx.author.name:
             await channel_out.send(intro +"Oh ya I almost forgot to ping him as well "+ ctx.author.mention)
        else:
             await channel_out.send("Now presenting the most honorable " +ctx.author.mention)

    @commands.has_role('NPA Officer')
    @commands.command(pass_context=True,aliases=['update_end'])
    async def end_update(self, ctx):
        """Ends a regular update with report"""
        await ctx.send("The start of the end")
        #This also does stuff like remove roles and lists who had them
        target=[]
        tarcount=0
        list=discord.utils.get(ctx.guild.roles, name='miniops')
        #CHANGE TO REPORTS CHANNEL ******************************************************
        given_name="npa-reports"
        channel = discord.utils.get(ctx.guild.channels, name=given_name)
        channel_id = channel.id
        channel_out = ctx.guild.get_channel(channel_id)
        #CHANGE THE ABOVE TO REPORTS CHANNEL ********************************************
        memberlist=[]
        for person in ctx.guild.members:
            outbutt="The following members partook: \n"
            if list in person.roles:
               await person.remove_roles(list)
               memberlist.append(f"{person.mention}")
            for grunt in memberlist:
               outbutt= outbutt+grunt+"\n"
            for each in HereCog.hits:
                outbutt=outbutt+each
            HereCog.hits=[]
        await channel_out.send(outbutt)
        await ctx.send("The end of the end")

    @commands.has_role('NPA Officer')
    @commands.command(pass_context=True)
    async def end_joint_update(self, ctx):
        """Ends a joint update with a report"""
        await ctx.send("The start of the end of the joint oh no!")
        #This also does stuff like remove roles and lists who had them
        target=[]
        tarcount=0
        list=discord.utils.get(ctx.guild.roles, name='Blazing Joints')
        #CHANGE TO REPORTS CHANNEL ******************************************************
        given_name="npa-reports"
        channel = discord.utils.get(ctx.guild.channels, name=given_name)
        channel_id = channel.id
        channel_out = ctx.guild.get_channel(channel_id)
        #CHANGE THE ABOVE TO REPORTS CHANNEL ********************************************
        memberlist=[]
        for person in ctx.guild.members:
            outbutt="The following members partook: \n"
            if list in person.roles:
               await person.remove_roles(list)
               memberlist.append(f"{person.mention}")
            for grunt in memberlist:
               outbutt= outbutt+grunt+"\n"
            for each in HereCog.hits:
                outbutt=outbutt+each
            HereCog.hits=[]
            await channel_out.send(outbutt)
        await ctx.send("That was a nice joint.  Cya all later")

    @commands.command(pass_context=True,aliases=["joint_join","join_joint"])
    async def joint_here(self, ctx):
        """Joins the Joint op channel"""
        member = ctx.author
        var = discord.utils.get(ctx.guild.roles, name = "Blazing Joints")
        # This is the code needed to give a user a role
        member = ctx.message.author # Member object that you want to add the role to
        await member.add_roles(var) # Adds the role to the member
#*************************************************************8
        given_name="blazing-joints"
        channel = discord.utils.get(ctx.guild.channels, name=given_name)
        channel_id = channel.id
        channel_out = ctx.guild.get_channel(channel_id)
#**************************************************************
        if "9003" in ctx.author.name:
             await channel_out.send(intro +"Oh ya I almost forgot to ping him as well "+ ctx.author.mention)
        else:
             await channel_out.send("Now presenting the most honorable "+ ctx.author.mention)

    @commands.has_role('Joint Ops')
    @commands.command(pass_context=True)
    async def bye(self, ctx):
        """Leaves the op channel"""
        member = ctx.author
        var = discord.utils.get(ctx.guild.roles, name = "Joint Ops")
        member = ctx.message.author # Member object that you want to add the role to
        await member.remove_roles(var)
        await ctx.send("Bye!")

    @commands.has_role('miniops')
    @commands.command(pass_context=True)
    async def bye(self, ctx):
        """Leaves the op channel"""
        member = ctx.author
        var = discord.utils.get(ctx.guild.roles, name = "miniops")
        member = ctx.message.author # Member object that you want to add the role to
        await member.remove_roles(var)
        await ctx.send("Bye!")

    @commands.command(pass_context=True)
    @commands.has_role('NPA Officer')
    async def add(self,ctx,*args):
        """Adds a list of targets use " " to surround each target"""
        #adds targets to the list
        for every in args:
             HereCog.targets.append(every)
        await ctx.send('{} targets added'.format(len(args)))

    @commands.command(pass_context=True)
    @commands.has_role('NPA Officer')
    async def clear(self,ctx):
        """Run this before addding targets to clear everything"""
        HereCog.targets=[]
        HereCog.hits=[]
        await ctx.send("Cleared the current list")

    @commands.command(pass_context=True,aliases=['H','Hit','h','hit','M','m','Miss','miss','t','T'])
    async def next(self,ctx):
        """Next target asumming a miss.  Use Hit/Miss for auto reports"""
        #await ctx.send(HereCog.targets)
        if ctx.invoked_with == 'H' or ctx.invoked_with == 'Hit' or ctx.invoked_with == 'h' or ctx.invoked_with == 'hit':
            HereCog.hits.append(lasttarg)
        if HereCog.targets:
            try:
                if len(str(HereCog.targets[0])) < 1:
                    raise Exception(" ")
                await ctx.send("Next target is: "+ str(HereCog.targets[0]))
                HereCog.lasttarg=str(HereCog.targets[0])
                del HereCog.targets[0]
            except Exception:
                await ctx.send("Thanks for coming out, this op is now over! Pleae do end_update or end_joint_update")
                HereCog.lasttarg=""
        else:
            await ctx.send("No targets left please add more with add or type end_update/end_joint_update to close out.")
            return

    def api_request(self,data, header):
        url = "https://www.nationstates.net/cgi-bin/api.cgi"
        response = requests.post(url, data=data, headers=header)
        head = response.headers
        if waiting_time := head.get("Retry-After"):
            time.sleep(int(waiting_time)+1)
            self.api_request(data,header)
        try:
            requests_left = int(head["X-RateLimit-Remaining"])
        except KeyError:
            requests_left = int(head["RateLimit-Remaining"])
        try:
            seconds_until_reset = int(head["X-RateLimit-Reset"])
        except KeyError:
            seconds_until_reset = int(head["RateLimit-Reset"])
        time.sleep(seconds_until_reset / requests_left)
        return response
