import discord
client = discord.Client()

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
            await message.channel.send("よろぴくついでに投票よろ")


    if ("マスク" in message.content):
        if client.user != message.author:
            await message.channel.send("マスク二枚くれてやるよ")
            
           



            
client.run("Njk4MDgxMTA0MDQwNTU4NjIy.XpB7tg.pK20RlsJBvNCzbgTi-16XWsFwow")

