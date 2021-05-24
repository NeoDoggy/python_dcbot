#!pip3 install os python-dotenv discord.py DateTime wget
#main bot py file
import os
from posix import uname_result
import discord 
from dotenv import load_dotenv
from datetime import datetime as dt

#settings
load_dotenv()
token = os.getenv('bot_token')
prefix = os.getenv('prefix')
client = discord.Client()

#ready
@client.event
async def on_ready():
    print(f'{client.user} is ready to work')
    #Playing -> activity = discord.Game(name="!help")
    #Streaming -> activity = discord.Streaming(name="!help", url="twitch_url_here")
    #Listening -> activity = discord.Activity(type=discord.ActivityType.listening, name="!help")
    #Watcing -> activity = discord.Activity(type=discord.ActivityType.watching, name="ニオ programming")
    activity = activity = discord.Game(name="幫ニオ做家事的遊戲")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    

#main
@client.event
async def on_message(msg):

    if msg.author==client.user:
        return
    
    if msg.content.startswith(f'{prefix}hi'):
        await msg.channel.send('hi')

    if msg.content.startswith(f'{prefix}nh'):
        num=msg.content.split(' ')
        await msg.channel.send('file fetching... please wait...',delete_after=5)
        os.system(f'./nhcrawl.sh -n {num[1]} -l 1')
        tmpfile=discord.File(f'./temphtml/{num[1]}/1.png',filename="image.png")
        nhembed=discord.Embed(title=f'cover of {num[1]}',url=f'https://nhentai.net/g/{num[1]}',description='wah',color=0xFFC0CB)
        nhembed.set_image(url='attachment://image.png')
        await msg.channel.send('Finished',delete_after=5)
        await msg.channel.send(file=tmpfile,embed=nhembed)
        os.system(f'rm -rf ./temphtml/{num[1]}')


    if msg.channel.id != 846392215424598057:
        backstagech = client.get_channel(846392215424598057)
        now = dt.now()
        nowtime = now.strftime("%H:%M:%S")
        print(f'\n{nowtime} - {msg.author} - sent {msg.content}')
        await backstagech.send(f'\n{nowtime} - {msg.author} - sent {msg.content}')

client.run(token)