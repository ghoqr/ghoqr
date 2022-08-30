import discord

client = discord.Client()
token = 'MTAxMzY5MTI5ODQzMzIwODM1MA.GVRfmF.9ZZmB-LgWccEKDAaza-Fkh5DfIyGHzlwPnH_vI'

@client.event
async def on_ready():
    print('Logged in')

client.run(token)
