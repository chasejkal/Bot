import discord
import os
import time
import random
import datetime
import keep_alive
import json
import asyncio
from discord import Permissions
from discord import Member
from discord.utils import get
from datetime import timedelta
from webserver import keep_alive
import requests
from random import randint
#from discord import commands, timers




#from discord.ext.command import has_permissions
#import discord.utils.get
from discord.ext.commands import Bot
from discord.ext import commands
from discord import ext

#bot = Bot("[")
#Client = commands.Bot(commands.when_mentioned_or('...'))
client = commands.Bot(command_prefix = '[')
client.remove_command("help")
#client = discord.Client()
start_time = time.time()


@client.event
async def on_ready():
     activity = discord.Game(name="I'll Catch You Lackin")
     await client.change_presence(status=discord.Status.idle, activity=activity) 
     print ('Im Online')
     print ('Logged in as:')
     print (client.user)
     print ('---------------')

time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}

def convert_time_to_seconds(time):
    try:
        return int(time[:-1]) * time_convert[time[-1]]
    except:
        return time

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        msg = 'This command does not exist.'
        await ctx.send(msg, delete_after=2.0)


@client.event
async def on_message(message):
   
        id = message.author.id
        msg = message.content
        time = message.created_at
        msgid = message.id
        srvr = message.guild
        chnl = message.channel.id
        guild = message.guild
        if message.author.bot: return

        if 'keifer' in message.content.lower():
          await message.delete()
        if 'kiefer' in message.content.lower():
          await message.delete()
        
        
        with open("tierone.txt") as file: 
         tierone = [tierone.strip().lower() for tierone in file.readlines()]
 
        with open("tiertwo.txt") as file: 
         tiertwo = [tiertwo.strip().lower() for tiertwo in file.readlines()]
         
        
        with open("tierthree.txt") as file: 
          tierthree = [tierthree.strip().lower() for tierthree in file.readlines()]
          
        with open("tierfour.txt") as file: 
         tierfour = [tierfour.strip().lower() for tierfour in file.readlines()]
        
        with open("exempt.txt") as file: 
         exempt = [tierfour.strip().lower() for tierfour in file.readlines()]
        
        with open("ping.txt") as file: 
         ping = [ping.strip().lower() for ping in file.readlines()]


        if any(tierfour in message.content.lower() for tierfour in tierfour):
         chl = discord.utils.get(message.guild.channels, name="serious-offenses")
         if message.author.bot: return
         if message.channel.id == 706967371880857650: return
       
         embedVar= discord.Embed(title="Level 3 banned link", description="<@" + str(id) + "> said a banned word", color=0xFF0000)
         embedVar.add_field(name="Message", value=str(msg), inline=False)
         embedVar.add_field(name="Recommended Punishment", value="Ban", inline=False)
         embedVar.add_field(name="Channel", value='<#' + str(chnl) + '>',inline=False)
         embedVar.add_field(name="Time", value=message.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
         embedVar.add_field(name="Message ID", value=str(msgid), inline=True)
         embedVar.add_field(name="Author ID", value=str(id), inline=True)  
         embedVar.add_field(name="What to do?", value="Please do not delete this message but react with :thumbsup: once appropriate measures have been taken.",inline=False)
         await chl.send(embed=embedVar)
         await message.delete()
         #print (message.author.name +' at: ' +  message.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S') +' Said: ' + str(msg))
         
         await message.author.send('You sent a prohibited link in **' + str(srvr) + '**. ```' + str(msg) + '``` ')
    
     


        elif any(tierthree in message.content.lower() for tierthree in tierthree):
         await message.channel.send('https://media.giphy.com/media/KDajoZn09d0nC61Ogw/giphy.gif')
         if message.author.bot: return
         if message.channel.id == 706967371880857650: return
       
         channel = discord.utils.get(message.guild.channels, name="serious-offenses")
         await message.delete()
        # if (message.channel.id == '706967371880857650'): 
         embedVar= discord.Embed(title="Level 3 banned word", description="<@" + str(id) + "> said a banned word", color=0xFF0000)
         embedVar.add_field(name="Message", value=str(msg), inline=False)
         embedVar.add_field(name="Recommended Punishment", value="Ban, or a 12hr+ mute depending on context.", inline=False)
         embedVar.add_field(name="Channel", value='<#' + str(chnl) + '>',inline=False)
         embedVar.add_field(name="Time", value=message.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
         embedVar.add_field(name="Message ID", value=str(msgid), inline=True)
         embedVar.add_field(name="Author ID", value=str(id), inline=True)   
         embedVar.add_field(name="What to do?", value="Please do not delete this message, but react with :thumbsup: once appropriate measures have been taken.", inline=False)
         await channel.send(embed=embedVar)
         await message.author.send('You sent a prohibited link in **' + str(srvr) + '**. ```' + str(msg) + '``` ')
         await message.delete()





        

        



        if '[verify arki' in message.content.lower():
          if get(message.author.roles, name="Verified" ): 
            await message.channel.send('You are already verified <@'+str(id)+'>.')
          else:
           user = message.author
           past = time - timedelta(days=14)
           date = user.created_at
           account_date = user.created_at.__format__(' %d %B %Y')
           if past < date:
             await message.channel.send('Your account must be older than 14 days in order to verify')
             await message.author.send('Your account needs to be 14 days old to access ' + str(srvr) + '. Your account does not meet these criteria. Your account was created on: ' + str(account_date))
           else:
             await message.channel.send('Success!')
             role = discord.utils.get(user.guild.roles, name="Verified")
             role2 = discord.utils.get(user.guild.roles, name="Unverified")
             #await user.remove_roles
             await user.add_roles(role)
      
        #if message.author.id == 705877877429633105:
         # await message.delete()
      

        #if message.author.id == 745067030952149093:
         # await message.delete()
          
          
         

        if '[settingup' in message.content.lower():
          embedVar= discord.Embed(color=0xea7938)
          embedVar.add_field(name='Verifying', value='`[verify`', inline=False)
          embedVar.add_field(name='Setting the bot up', value='`[setup`', inline=False)
          embedVar.add_field(name='Staff PCs', value='`[pc staff`', inline=False)
          embedVar.set_footer(text='nibbzi#7362')
          await message.channel.send(embed=embedVar)

        

        if '[info' in message.content.lower():
          embedVar= discord.Embed(color=0xea7938)
          embedVar.add_field(name='User Info', value='`[userinfo`', inline=False)
          embedVar.add_field(name='Server Info', value='`[serverinfo`', inline=False)
          embedVar.add_field(name='Staff PCs', value='`[pc staff`', inline=False)
          embedVar.set_footer(text='nibbzi#7362')
          await message.channel.send(embed=embedVar)


        if '[commands' in message.content.lower():
          embedVar= discord.Embed(color=0xea7938)
          embedVar.add_field(name='Commands', value='Keith has an ever exapnding library of commands.', inline=False)
          embedVar.add_field(name='`[verify`', value='If an account is over a certain number of days, using this command will give them the role to be able to speak', inline=False)
          embedVar.set_footer(text='nibbzi#7362')
          await message.channel.send(embed=embedVar)

         


        if '[verify cacti' in message.content.lower():
          if get(message.author.roles, name="Baby Cacti" ): 
            await message.channel.send('You are already verified <@'+str(id)+'>.')
          if get(message.author.roles, name="eclipsed" ): 
            await message.channel.send('You are eclipsed <@'+str(id)+'>.')
          else:
           user = message.author
           past = time - timedelta(days=14)
           date = user.created_at
           account_date = user.created_at.__format__(' %d %B %Y')
           if past < date:
             await message.channel.send('Your account must be older than 14 days in order to verify')
             await message.author.send('Your account needs to be 14 days old to access ' + str(srvr) + '. Your account does not meet these criteria. Your account was created on: ' + str(account_date))
           else:
             await message.channel.send('Success!')
             role = discord.utils.get(user.guild.roles, name="Baby Cacti")
             role2 = discord.utils.get(user.guild.roles, name="Keith Unverified 2")
             await user.remove_roles(role2)
             await user.add_roles(role)
          

        if '[website' in message.content.lower():
          embedVar= discord.Embed(color=0xea7938)
          embedVar.add_field(name='Website', value='https://glizzy.us', inline=False)
          embedVar.set_footer(text='nibbzi#7362')
          await message.channel.send(embed=embedVar)


        elif '[help' in message.content.lower():
          embedVar= discord.Embed(color=0xea7938)
          embedVar.add_field(name='Setting Up', value='`[settingup`', inline=False)
          embedVar.add_field(name='Information', value='`[info`', inline=True)
          embedVar.add_field(name='Commands', value='`[commands`', inline=True)
          embedVar.add_field(name='Website', value='`[website`', inline=True)
          embedVar.set_footer(text='nibbzi#7362')
          await message.channel.send(embed=embedVar)



        
        


       
        

     














        elif any(tierone in message.content.lower() for tierone in tierone):
         if any(exempt in message.author.name for exempt in exempt): return
         channel = discord.utils.get(message.guild.channels, name="bruh-logs")
         if 'pcpartpicker' in message.content.lower(): return
         if 'tiktok' in message.content.lower(): return
         if 'youtube' in message.content.lower(): return
         if 'twitch.tv' in message.content.lower(): return
         if 'amazon' in message.content.lower(): return
         if 'twitter' in message.content.lower(): return
         if 'youtu.be' in message.content.lower(): return
         #if get(message.author.roles, name="Admin"): return
         
         #if (message.author.name == 'nibbzi'):  return
      
         
         embedVar = discord.Embed(title="Link", description="<@" + str(id) + "> sent a link", color=0x00ff00)
         embedVar.add_field(name="Message", value=str(msg), inline=False)
         embedVar.add_field(name="Recommended Consequence", value="Nothing, unless its an ip logger or nsfw link.", inline=False)
         embedVar.add_field(name="Channel", value='<#' + str(chnl) + '>',inline=False)
         embedVar.add_field(name="Time", value=message.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
         embedVar.add_field(name="Message ID", value=str(msgid), inline=True)
         embedVar.add_field(name="Author ID", value=str(id), inline=True)  
       
         await channel.send(embed=embedVar)

         


        elif any(tiertwo in message.content.lower() for tiertwo in tiertwo):
         channel = discord.utils.get(message.guild.channels, name="bruh-logs")
         if message.author.bot: return
         if get(message.author.roles, name="Admin"): return
         embedVar = discord.Embed(title="Level 2 banned word", description="<@" + str(id) + "> said a banned word", color=0xDFA030)
         embedVar.add_field(name="Message", value=str(msg), inline=False)
         embedVar.add_field(name="Channel", value='<#' + str(chnl) + '>',inline=False)
         embedVar.add_field(name="Recommended Punishment", value="Warn (Preferably verbal) however, depending on context it may change", inline=False)
         embedVar.add_field(name="Time", value=message.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
         embedVar.add_field(name="Message ID", value=str(msgid), inline=True)
         embedVar.add_field(name="Author ID", value=str(id), inline=True)  
         await channel.send(embed=embedVar)

        await client.process_commands(message) 







@client.command()
async def givenum(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("Type a number")
    msg1 = await client.wait_for("message", check=check)
    await ctx.send("Type a second, larger number")
    msg2 = await client.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        await ctx.send(f"You got {value}.")
    else:
        await ctx.send(":warning: Please ensure the first number is smaller than the second number.")


@client.command(pass_context=True)
@commands.has_any_role('Staff', 'Advisor')
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f":table_tennis: Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

@client.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if user ==None:
      user = ctx.author

    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)

    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)
   

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)



@client.command()
async def serverinfo(ctx, guild: discord.Guild = None):
        guild = ctx.guild
        emoji_count = len(guild.emojis)
        embed = discord.Embed(title=f'{guild} Server Information', description="Coded by nibbzi#1917",
                          timestamp=ctx.message.created_at, color=discord.Color.orange())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name='Name', value=guild.name)
        embed.add_field(name="Channel count:", value=len(guild.channels))
        embed.add_field(name="Role Count:", value=len(guild.roles))
        embed.add_field(name="Boosters Count:", value=guild.premium_subscription_count)
        embed.add_field(name="Member count:", value=guild.member_count)
        embed.add_field(name="Server created at:", value=guild.created_at)
        embed.add_field(name="Server owner:", value=guild.owner)
        embed.add_field(name='Number of emotes', value=str(emoji_count))
        embed.add_field(name='Region', value=guild.region)
        embed.add_field(name='Verification Level', value=str(guild.verification_level))
        embed.set_footer(text=f"Command {ctx.author} Used by.", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

@client.command(aliases=['ld'])
@commands.has_role('Admin')
async def lockdown(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
  ()
  #await ctx.delete()
  await ctx.send('Channel is now locked down :lock:')
    
    

@client.command(aliases=['uld'])
@commands.has_role('Admin')
async def unlockdown(ctx):
 
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
  await ctx.channel.edit(sync_permissions=True)
  #await ctx.delete()
  await ctx.send('Channel is now unlocked :unlock:')



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    check = False
    for i in member.roles:
        if i in ctx.author.roles[1:]:
            check = True

    if(check):
        await ctx.send('Cant ban Moderators/Admins')
    else:
        await member.ban(delete_message_days=0, reason=reason)
        
        embedVar = discord.Embed(title="Member Banned", description=str(member.name), color=0x00ff00)
        embedVar.add_field(name="Member ID", value=str(member.id), inline=False)
        embedVar.add_field(name="By:", value=str(ctx.author), inline=True)
        embedVar.add_field(name="Reason:", value=str(reason), inline=True)
        embedVar.set_footer(text="nibbzi#1917")
        await ctx.send(embed=embedVar)
        
@client.command()
async def unban(ctx, *, user=None):

    try:
        user = await commands.converter.UserConverter().convert(ctx, user)
    except:
        await ctx.send("Error: user could not be found!")
        return

    try:
        bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
        if user in bans:
            await ctx.guild.unban(user, reason="Responsible moderator: "+ str(ctx.author))
        else:
            await ctx.send("User not banned!")
            return

    except discord.Forbidden:
        await ctx.send("I do not have permission to unban!")
        return

    except:
        await ctx.send("Unbanning failed!")
        return

    await ctx.send(f"Successfully unbanned {user.mention}!")

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def poggers(ctx):
    await ctx.send('champ')
          
          
@poggers.error
async def poggers_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg, delete_after=2.0)
    else:
        raise error

@client.command()
@commands.has_permissions(manage_roles=True)
async def tempmute(ctx, member : discord.Member, time=0, unit = None, reason=None):
  if get(member.roles, name="Staff" ): 
        await ctx.send('Cant mute Staff')
  else:
        
    if not member or time == 0 or time == str:
        return
    elif reason == None:
        reason = "No Reason Provided"
    if unit == "s":
       wait = 1 * time
    elif unit == "m":
      wait = 60 * time
    elif unit == "h":
      wait = 3600 * time
    elif unit == "d":
      wait = 86400 * time
    elif unit == "w":
      wait = 604,800 * time 
     
    

    muteRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(muteRole)

    #tempMuteEmbed = discord.Embed(description=f"**Reason:** {reason}")
    #tempMuteEmbed.set_author(name=f"{member} Has Been Muted", icon_url=f"{member.avatar_url}")
    #tempMuteEmbed.set_footer(text="bruh")

    #await ctx.channel.send(embed=tempMuteEmbed)

    tempMuteModLogEmbed = discord.Embed()
    tempMuteModLogEmbed.set_author(name=f"[MUTE] {member}", icon_url=f"{member.avatar_url}")
    tempMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    tempMuteModLogEmbed.add_field(name="Moderator", value=f"{ctx.message.author}")
    tempMuteModLogEmbed.add_field(name="Reason", value=f"{reason}")
    tempMuteModLogEmbed.add_field(name="Duration", value=f"{str(wait)}")
    tempMuteModLogEmbed.set_footer(text="embedfooter")
    #modlog = client.get_channel(638783464438759464)
    await ctx.send(embed=tempMuteModLogEmbed)

    

    tempMuteDM = discord.Embed(title="Mute Notification", description="You Were Muted In ***")
    tempMuteDM.set_footer(text="embedfooter")
    tempMuteDM.add_field(name="Reason", value=f"{reason}")
    tempMuteDM.add_field(name="Duration", value=f"{wait}")

    userToDM = client.get_user(member.id)
    await userToDM.send(embed=tempMuteDM)

    await asyncio.sleep(wait)
    unMuteModLogEmbed = discord.Embed()
    unMuteModLogEmbed.set_author(name=f"[UNMUTE] {member}", icon_url=f"{member.avatar_url}")
    unMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    unMuteModLogEmbed.set_footer(text="embedfooter")
    await ctx.send(embed=unMuteModLogEmbed)
    await member.remove_roles(muteRole)

        
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
      if limit > 100:
        await ctx.send("I'm only allowed to purge up to 100 messages.")
      else:
        await ctx.channel.purge(limit=limit)
        msg = (str(limit) + ' Messages purged by {}'.format(ctx.author.mention))
        await ctx.send(msg, delete_after=2.0)
        await ctx.message.delete()

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
    
from discord.ext.commands import CommandNotFound

 

@client.command(aliases=['sm'])
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int):
  if seconds == '0':
    await ctx.send('Slowmode off!')
  else:
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to " + str(seconds) + " seconds!")

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
      if discord.utils.get(ctx.guild.roles, name="Staff"):
        await ctx.send('Cant Mute Moderators/Admins')
        return
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.add_roles(role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):

        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.remove_roles(role)
        embed=discord.Embed(title="User Unuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_roles=True)
async def timer(ctx, time=0, unit = None, reason=None):

        
    if not time == 0 or time == str:
        return
    elif reason == None:
        reason = "No Reason Provided"
    if unit == "s":
       wait = 1 * time
    elif unit == "m":
      wait = 60 * time
    elif unit == "h":
      wait = 3600 * time
    

    muteRole = discord.utils.get(ctx.guild.roles, name="Muted")


    tempMuteEmbed = discord.Embed(description=f"**Reason:** {reason}")
    tempMuteEmbed.set_author(name=f"{member} set a timer", icon_url=f"{member.avatar_url}")
    tempMuteEmbed.set_footer(text="bruh")

    await ctx.channel.send(embed=tempMuteEmbed)


    unMuteModLogEmbed = discord.Embed()
    unMuteModLogEmbed.set_author(name=f"[UNMUTE] {member}", icon_url=f"{member.avatar_url}")
    unMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    unMuteModLogEmbed.set_footer(text="embedfooter")
    await ctx.send(embed=unMuteModLogEmbed)

    tempMuteDM = discord.Embed(title="Mute Notification", description="You Were Muted In ***")
    tempMuteDM.set_footer(text="embedfooter")
    tempMuteDM.add_field(name="Reason", value=f"{reason}")
    tempMuteDM.add_field(name="Duration", value=f"{wait}")

    userToDM = client.get_user(member.id)
    await userToDM.send(embed=tempMuteDM)

    await asyncio.sleep(wait)
    unMuteModLogEmbed = discord.Embed()
    unMuteModLogEmbed.set_author(name=f"[TIMER] {member}", icon_url=f"{member.avatar_url}")
    unMuteModLogEmbed.add_field(name="User", value=f"{member.mention}")
    unMuteModLogEmbed.set_footer(text="embedfooter")
    await ctx.send(embed=unMuteModLogEmbed)

@client.command
async def blacklist(self, ctx, word= str):
    with open("tier3") as f:
        user = str(username)
        pointamount = str(points)
        points = 0
        f.write(f'{user}, {pointamount}')
        f.close()


@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def spam(ctx, user: discord.Member, amount: int, *, content):
        if amount > 20:
            await ctx.send("Can't spam over 20.")
            return
        elif get(member.roles, name="Staff"): 
            await ctx.send("You are not allowed to do this command")
            return 
        elif '@everyone' in content:
            await ctx.send("Nice try.")
            return
        elif '@here' in content:
            await ctx.send("Nice try.")
            return
        
        messages = 0 
        while messages < amount:
            await ctx.send('<@{}> {}'.format(user.id, content))
            messages = messages + 1
            await asyncio.sleep(0.2)
@spam.error
async def spam_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
    if isinstance(error, commands.CommandOnCooldown):
      msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
      await ctx.send(msg, delete_after=2.0)
    else:
        raise error

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.has_any_role('Admin', 'Advisor','Visitor')
async def spamdm(ctx, user: discord.Member, amount: int, *, content):
        if amount > 20:
            await ctx.send("Can't spam over 20.")
            return
        elif get(member.roles, name="Staff"): 
            await ctx.send("You are not allowed to do this command")
            return 
        elif '@everyone' in content:
            await ctx.send("Nice try.")
            return
        elif '@here' in content:
            await ctx.send("Nice try.")
            return
            
        messages = 0 
        while messages < amount:
            await user.send(content)
            messages = messages + 1
            await asyncio.sleep(0.2)
@spamdm.error
async def spamdm_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
        return
    if isinstance(error, commands.CommandOnCooldown):
      msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
      await ctx.send(msg, delete_after=2.0)
    if isinstance(error, commands.NoPrivateMessage):
      msg = "This user can't be DM'D"
      await ctx.send(msg, delete_after=2.0)
    else:
        raise error

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    if get(member.roles, name="Staff" ): 
        await ctx.send('Cant warn Staff')
    else:
        embedVar = discord.Embed(title="Member Warned", description=str(member.name), color=0x00ff00)
        embedVar.add_field(name="Member ID", value=str(member.id), inline=False)
        embedVar.add_field(name="By:", value=str(ctx.author), inline=True)
        embedVar.add_field(name="Reason:", value=str(reason), inline=True)
        embedVar.set_footer(text="nibbzi#1917")
        with open("warns.txt", "a") as f:
          f.write(f"Member ID: {member.id}, Reason: {reason}, Person Warned: {member}, Who Warned? {ctx.author}\n")
        await ctx.send(embed=embedVar)

@client.command(name='coinflip', aliases=['flip'])
async def flip(ctx, ammount: int = 1):
        '''Flip a Coin
        ```css
        Example Usage:
        ``````css
        ?coinflip // Flips a single coin
        ``````css
        ?flip 5 // Flips five coins.
        ```
        '''
        def flip():
            heads = randint(0, 1) == 1  # Returns true if heads
            if heads:
                return 'Heads'
            else:
                return 'Tails'

        if ammount == 1:
            desc = f'You got __{flip()}__!'

        elif ammount <= 20:

            desc = 'Results: ```css\n'

            for n in range(ammount):
                desc += f'#{n+1}: {flip()}\n'

            desc += '```'

        else:
            desc = "**Can't flip more then 20 coins at a time!!!**"

        await ctx.send(desc)



@client.command(pass_context=True)
async def uptime(ctx):
        current_time = time.time()

        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Coded by nibbzi#1917")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

@client.command()
async def say(ctx, *, message: str):
 await ctx.send(f'{ctx.author} says: {message}')


@client.command()
@commands.has_permissions(ban_members=True)
async def fire(ctx, member : discord.Member, *, Reason=None):
       if Reason==None:
         Reason = 'No Defined Reason'
       roles = role_string = ' '.join([r.mention for r in user.roles][1:])
       embedVar = discord.Embed(title="Member Fired", description=str(member.name), color=0x00ff00)
       embedVar.add_field(name="Member ID", value=str(member.id), inline=False)
       embedVar.add_field(name="By:", value=str(ctx.author), inline=True)
       embedVar.add_field(name="Reason:", value=str(Reason), inline=True)

       embedVar.add_field(name="Roles Removed:", value=str(Reason), inline=True)
       embedVar.set_footer(text="nibbzi#1917")
       await member.remove_role(roles)
       await ctx.send(embed=embedVar)
        
@client.command()
@commands.has_permissions(manage_messages=True)
async def setup(ctx):
  await ctx.send('Setting Up...')
  guild = ctx.message.guild
  name = 'logs'
  category = discord.utils.get(guild.categories, name=name)
  member = client.user.bot
  embedVar = discord.Embed(title="Setting Up!", description="Please Adjust Permissions accordingly",
    color=0x2eb3d1)
  member = client.user.bot
  #await guild.create_text_channel('bru', category=category)
  await guild.create_text_channel('bruh-logs', category = category)
  await guild.create_text_channel('serious-offenses', category = category)
  embedVar = discord.Embed(title="Setting Up!", description="Please Adjust Permissions accordingly", color=0x2eb3d1)
  embedVar.add_field(name="Who executed the command?", value=ctx.author.mention, inline=False)
  embedVar.add_field(name="Time", value=message.created_at.__format__('%H:%M:%S. %A, %d. %B %Y'), inline=False)
  #embedVar.add_field(name="What to do now", value='Please make sure all channels are setup corroctly according to your servers roles ', inline=False)
  #embedVar.set_footer(text="nibbzi#1917")
  await ctx.send(embed=embedVar)
  await asyncio.sleep(2)
  await ctx.send('Setup Complete!')

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_any_role('Admin', 'Advisor','Visitor')
async def sleep(ctx, user: discord.Member, amount: int):
        if amount > 20:
            await ctx.send("Can't spam over 20.")
            return
            
        messages = 0 
        while messages < amount:
            await user.send(f'**{ctx.author}** would like you to sleep. Please do so')
            messages = messages + 1
            await asyncio.sleep(0.2)
@sleep.error
async def sleep_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
        return
    if isinstance(error, commands.CommandOnCooldown):
      msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
      await ctx.send(msg, delete_after=2.0)
    if isinstance(error, commands.NoPrivateMessage):
      msg = "This user can't be DM'D"
      await ctx.send(msg, delete_after=2.0)
    else:
        raise error



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def nuke(ctx):

        await ctx.channel.purge(limit=100000)
        msg = ('Channel Nuked by {}'.format(ctx.author.mention))
        await ctx.message.delete()
        await ctx.send(msg, delete_after=2.0)

@nuke.error
async def nuke_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")
    

@client.event
async def on_reaction_add(reaction, user):
    suggestion_author_id = int(reaction.message.embeds[0].footer.text)
    if reaction.message.author.id == client.user.id and user.id == suggestion_author_id:
        try:
            await user.dm_channel.send("You can't react to your own suggestions!")
        except:
            await user.create_dm()
            await user.dm_channel.send("You can't react to your own suggestions!")
        await reaction.message.remove_reaction(reaction.emoji, user)


@client.command()
async def suggest(ctx, *args):
    if ctx.author == client.user:
        return
    suggestion = ""
    for arg in args:
        suggestion += arg + " "
      
    embed = discord.Embed(description=suggestion)
    embed.set_author(name=ctx.author.name + " suggested:", icon_url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.author.id)

    await ctx.message.delete()
    sent_message = await ctx.send(embed=embed)
    await sent_message.add_reaction("✅")
    await sent_message.add_reaction("❌")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run('NjQxMzc1NDczMzIyMDMzMTYz.XkG1Lw.Bo8obXkQcWO29tyzJZP9F1Db_wc') 