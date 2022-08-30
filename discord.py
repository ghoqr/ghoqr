import discord

client = discord.Client()
token = 'MTAxMzY5MTI5ODQzMzIwODM1MA.G79II0.hUnnyoW8WZ-C_Xt16iiwNFuxdhUZLdDsY1bbO8'

@client.event
async def on_ready():
    print('Logged in')

client.run(token)
