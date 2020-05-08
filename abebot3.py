import random
import discord
from discord.ext import commands
import os
import traceback
client = discord.Client()

t = ""
b = 0
a = 0

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message):
    if ("よろ" in message.content):
        if client.user != message.author:
            my="よろぴくついでに投票よろ"
            await message.channel.send(my)
            

    if ("マスク" in message.content)or("コロナ" in message.content):
        if client.user != message.author:
            mm="マスク二枚くれてやるよ！"
            await message.channel.send(mm)

    if ("kusa" in message.content )or("草"in message.content) or\
       ("ワロタ"in message.content)or ("ｗ"in message.content):
        if client.user != message.author:
            m="草"
            await message.channel.send(m)
            
    if ("安倍トランプ" in message.content)or\
       ("安倍"in message.content)and ("やろ"in message.content) :
        if client.user != message.author:
            await message.channel.send("やりたければ国会議事堂にこい")

    if ("昭恵" in message.content):
        if client.user != message.author:
            await message.channel.send("だいちゅき")

    if ("やりますねぇ" in message.content):
        if client.user != message.author:
            await message.channel.send("あ///♂♂♂")

    if ("安倍" in message.content):
        if client.user != message.author:
            await message.channel.send("はーい")

    if ("ヤれ" in message.content):
        if client.user != message.author:
            await message.channel.send("はい。昭恵～")

#    if ("abeskip " in message.content):
 #       if client.user != message.author:
  #          music6 = message.content.lstrip("abeskip")
   #         await message.channel.send("!playskip"+ music6)


    if ("緊急事態宣言　"in message.content):
        if client.user != message.author:
            global t
            t = message.content.lstrip("緊急事態宣言　")
            await message.channel.send("緊急事態宣言を発令しました。"+ t +
                                       "の言葉を発することを控えてください。"
                                       "国民の皆様のご協力をお願いします。")
            
           
    if ("!p " in message.content):
        if client.user != message.author:
            if random.randint(0,13) == 0:
                await message.channel.send("いいね！")
      
    if message.content.startswith("abe"):
        if client.user != message.author:
            a = random.randint(0,2)
            if a == 0:
                await message.channel.send("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Shinz%C5%8D_Abe_Official.jpg/240px-Shinz%C5%8D_Abe_Official.jpg")
            elif a == 1:
                await message.channel.send("https://portal.st-img.jp/detail/47b60bc4550ae36ebf425f6926176ee5_1588586592_2.jpg")
            elif a == 2:
                await message.channel.send("https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Akie_Abe.jpg/200px-Akie_Abe.jpg")

    
            

    
        
        
            
           
            
client.run(token)

