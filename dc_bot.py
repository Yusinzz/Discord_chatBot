#導入 Discord.py
import discord
from discord import app_commands
import genshin
from discord.ext import commands
from config import token

import random
import youtube_dl
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    await client.tree.sync()
    print('目前登入身份：', client.user)

@client.tree.command(name = "hello") 
async def hello(interaction:discord.integrations):
    user = interaction.user
    pingmention = user.mention

    await interaction.response.send_message(pingmention + "Hello!")

@client.tree.command(name = "抽卡", description="94抽卡") 
async def 抽卡(interaction:discord.integrations):
    # if message.author == client.user:
    #     return
    c = random.randint(0,100)
    if c < 10:
        await interaction.response.send_message('六星!浪漫突進')
        await interaction.followup.send("https://memeprod.ap-south-1.linodeobjects.com/user-template/1bb9864a78e928542f725e5ac7faee1b.png")
    elif 11<c<35:
        await interaction.response.send_message('五星!')
        await interaction.followup.send('https://i.imgur.com/YiMUiop.gif')
    else:
        await interaction.response.send_message('四星 可憐吶非洲人奧迪')
        await interaction.followup.send("https://scontent.ftpe7-2.fna.fbcdn.net/v/t1.18169-9/541764_358237567606942_1264280639_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=cdbe9c&_nc_ohc=YlkndYly4i0AX_06esJ&_nc_ht=scontent.ftpe7-2.fna&oh=00_AfDN2h-iiazhwyJKrTZcbVn0T5Hqf-1zeVtDGFewymoTGw&oe=6448EEB3")
         

@client.tree.command(name = "進來", description="小精靈陪伴") 
async def join(interaction:discord.integrations):
    
    #這裡的指令會讓機器人進入call他的人所在的語音頻道
    voice = discord.utils.get(client.voice_clients, guild=interaction.guild)
    if interaction.user.voice== None:
        await interaction.response.send_message("先滾進頻道再叫我==")
    elif voice == None:
        voiceChannel = interaction.user.voice.channel
        await voiceChannel.connect()
    else:
        await interaction.send("就在裡面了是在?")

@client.tree.command(name = "出去", description="請你離開") 
async def exit(interaction:discord.integrations):
    voice = discord.utils.get(client.voice_clients, guild=interaction.guild)
    await voice.disconnect()
    
# @client.command()
# async def genshin_search(id):
#     cookies = {"ltuid": id, "ltoken": "cnF7TiZqHAAvYqgCBoSPx5EjwezOh1ZHoqSHf7dT"}
#     client = genshin.Client(cookies)

#     data = await client.get_genshin_user(710785423)
#     print(f"User has a total of {data.stats.characters} characters")


client.run(token) #TOKEN 