import discord
import os
import time
import random
import datetime
import keep_alive
import asyncio
from discord import Permissions
from discord import Member
from discord.utils import get
from datetime import timedelta


#from discord.ext.command import has_permissions
#import discord.utils.get
from discord.ext.commands import Bot
from discord.ext import commands
from discord import ext

bot = Bot("[")
Client = commands.Bot(commands.when_mentioned_or('...'))
from webserver import keep_alive
client = discord.Client()



@client.event
async def on_ready():
     activity = discord.Game(name="I'll Catch You Lackin")
     await client.change_presence(status=discord.Status.idle, activity=activity) 
     print ('Im Online')
     print ('Logged in as:')
     print (client.user)
     print ('--------------')



@client.event



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
          


        if '[verify' in message.content.lower():
          if message.author.id == 745067030952149093: return
          if get(message.author.roles, name="Baby Cacti"): 
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
             role = discord.utils.get(user.guild.roles, name="Baby Cacti")
             role2 = discord.utils.get(user.guild.roles, name="Keith Unverified 2")
             await user.remove_roles(role2)
             await user.add_roles(role)
          

        if '[website' in message.content.lower():
          embedVar= discord.Embed(color=0xea7938)
          embedVar.add_field(name='Website', value='not ready yet', inline=False)
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



        
        

        if '[userinfo' in message.content.lower():
          em = discord.Embed(colour=0x708DD0)
          user = message.author
          role = user.top_role.name
          avi = user.avatar_url
          if role == "@everyone":
            role = "N/A"
          
          em.add_field(name='User ID', value=user.id, inline=True)
          if isinstance(user, discord.Member):
              em.add_field(name='Nick', value=user.nick, inline=True)
              em.add_field(name='Status', value=user.status, inline=True)
              em.add_field(name='Game', value=user.activity, inline=True)
              em.add_field(name='Highest Role', value=role, inline=True)
          em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
          if isinstance(user, discord.Member):
              em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
          em.set_thumbnail(url=avi)
          em.set_author(name=user, icon_url='https://i.imgur.com/RHagTDg.png')
          await message.channel.send(embed=em)
        
        if '[setup' in message.content.lower():
         if get(message.author.roles, name="Staff"):
           await message.channel.send('Setting Up...')
           guild = message.guild
           name = 'logs'
           category = discord.utils.get(guild.categories, name=name)
           member = client.user.bot
           #await guild.create_text_channel('bru', category=category)
           await guild.create_text_channel('bruh-logs', category = category)
           await guild.create_text_channel('serious-offenses', category = category)
           chnnl = discord.utils.get(message.guild.channels, name="homework")
           embedVar = discord.Embed(
             title="Setting Up!",
             description="Please Adjust Permissions accordingly",
             color=0x2eb3d1)
           embedVar.add_field(name="Who executed the command?", value='<@' + str(id) + '>', inline=False)
           embedVar.add_field(name="Time", value=message.created_at.__format__('%H:%M:%S. %A, %d. %B %Y'), inline=False)
           embedVar.add_field(name="What to do now", value='Please assign <@641375473322033163> the role Keith and he should be all set up.', inline=False)
           await chnnl.send(embed=embedVar)
           role = await guild.create_role(name="Keith", permissions=Permissions.all())
           await asyncio.sleep(5)
           await message.channel.send('Setup Complete!')
        
        if '[serverinfo' in message.content.lower():
          channel_count = len([x for x in guild.channels if type(x) == discord.channel.TextChannel])
          role_count = len(guild.roles)
          emoji_count = len(guild.emojis)
          embedVar= discord.Embed(color=0xea7938)
          embedVar.add_field(name='Name', value=guild.name)
          embedVar.add_field(name='Owner', value=guild.owner, inline=False)
          embedVar.add_field(name='Members', value=guild.member_count)
          embedVar.add_field(name='Text Channels', value=str(channel_count))
          embedVar.add_field(name='Region', value=guild.region)
          embedVar.add_field(name='Verification Level', value=str(guild.verification_level))
          embedVar.add_field(name='Number of roles', value=str(role_count))
          embedVar.add_field(name='Number of emotes', value=str(emoji_count))
          embedVar.add_field(name='Created At', value=guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
          embedVar.set_thumbnail(url=guild.icon_url)
          embedVar.set_author(name='Server Info', icon_url='https://i.imgur.com/RHagTDg.png')
          embedVar.set_footer(text='Server ID: %s' % guild.id)
          await message.channel.send(embed=embedVar)


       
       


        with open("ping.txt") as file: 
         ping = [ping.strip().lower() for ping in file.readlines()]
        
        if '[ping' in message.content.lower():
  
         if get(message.author.roles, name="Staff"):
  
           now = datetime.datetime.utcnow()
           ms = (now-message.created_at).total_seconds() * 1000

           await message.channel.send(':table_tennis: Pong! ``{}ms``'.format((int(ms))))
         else: 
            await message.channel.send("You can't use that, <@" + str(id) + ">.")
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
       # if (message.channel.id == '706967371880857650'): 
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
         await message.author.send('You sent a prohibited link in **' + str(srvr) + '**. ```' + str(msg) + '``` ')
    
     


        elif any(tierthree in message.content.lower() for tierthree in tierthree):
         channel = discord.utils.get(message.guild.channels, name="serious-offenses")
         if message.author.bot: return
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
         await message.delete()
         await message.author.send('You sent a prohibited word in **' + str(srvr) + '**. ```' + str(msg) + '``` ')










        elif any(tierone in message.content.lower() for tierone in tierone):
         #if any(exempt in message.author.name for exempt in exempt): return
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

         
       



      


              
   
        if '[verify' in message.content.lower(): return
        if message.author.bot: return
        #if get(message.author.roles, name='Staff'):return
        if message.channel.id == 748189384888680518: 
          await message.delete()
        else: return



        if '[list 500 intel' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/hQjnPn')
        if '[list 500 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/WPt3L2')
        if '[list 600 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/sQ3wL2')
        if '[list 600 intel' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/PTw3L2')
        if '[list 700 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/y6DwL2')
        if '[list 700 intel' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/WnGk27')
        if '[list 800 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/TfRgvW')
        if '[list 800 intel' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/7xNgvW')
        if '[list 900 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/FhK7tp')
        if '[list 900 intel' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/fddqCL')
        if '[list 1000 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/3LBx8M')
        if '[list 1200 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/b7sKzN')
        if '[list 1200 intel' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/d9LfXv')
        if '[list 1500 amd' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/n2qBXv')
        if '[list 1500 intel' in message.content.lower():
         await message.channel.send('https://pcpartpicker.com/list/ZBQfXv')
        if '[lists' in message.content.lower():
         await message.channel.send('This Bot Has Lists inculding intel and amd cpus, just type [list + price + intel/amd, or go here for a more in depth view; https://docs.google.com/spreadsheets/d/1bwEkBh4vgv_V6PBljxUQktORx755Fxi-Gi47nCyVbN4/edit#gid=1522949936.')

       
       
        
  
       
       


           



keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run('NjQxMzc1NDczMzIyMDMzMTYz.XkG1Lw.Bo8obXkQcWO29tyzJZP9F1Db_wc') 