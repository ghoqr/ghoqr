import discord

client = discord.Client()
token = 'MTAxMzY5MTI5ODQzMzIwODM1MA.G79II0.hUnnyoW8WZ-C_Xt16iiwNFuxdhUZLdDsY1bbO8'

@client.event
async def on_ready():
    print('Logged on')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == 'a':
        await message.channel.send('a')

client.run(token)