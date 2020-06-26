import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("잼민이 명령어"):
        await message.channel.send("복돌깔아야지")
    if message.content.startswith("잼민아"):
        await message.channel.send("외")
    if message.content.startswith("잼민 샌즈"):
        await message.channel.send("와!아시는구나")
    if message.content.startswith("잼민 훈수"):
        await message.channel.send("아 그거 그렇게 하는거 아닌데")
    if message.content.startswith("잼민 나때"):
        await message.channel.send("꼰머 닥쳐")
    if message.content.startswith("잼민 마크"):
        await message.channel.send("복돌깔아야지")
    if message.content.startswith("잼민 나이"):
        await message.channel.send("물어바서머함")
    if message.content.startswith("잼민 마춤뻡"):
        await message.channel.send("아 불펴나네")
    if message.content.startswith("잼민 인성"):
        await message.channel.send("아 내가 좀 차카지")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
