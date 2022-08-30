import discord

client = discord.Client()
token = 'MTAxMzY5MTI5ODQzMzIwODM1MA.GEqOCg.gRdrYw0emuhZFsRB_lvmvljTkWdCzpRDgfPObw'

@client.event
async def on_ready():
    print('Logged in')

client.run(token)
