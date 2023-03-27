#導入 Discord.py
import discord
from discord.ext import commands
from Token import token
import random
import youtube_dl
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents= intents)
# voice_client = discord.voice_client(intents = intents)
#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.command()
async def join(ctx):
    
    #這裡的指令會讓機器人進入call他的人所在的語音頻道
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if ctx.author.voice == None:
        await ctx.send("You are not connected to any voice channel")
    elif voice == None:
        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
    else:
        await ctx.send("Already connected to a voice channel")
#當有訊息時
@client.command()
async def draw(message):
    #排除自己的訊息，避免陷入無限循環
    # if message.author == client.user:
    #     return
    #如果包含 ping，機器人回傳 pong
    c = random.randint(0,100)
    if c < 10:
        await message.channel.send('六星!')
    elif 11<c<35:
        await message.channel.send('五星!')
    else:
         await message.channel.send('四星 可憐那非洲人')


client.run(token) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面