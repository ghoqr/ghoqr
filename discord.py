import discord

client = discord.Client()
token = 'MTAxMzY5MTI5ODQzMzIwODM1MA.GpKcmz.XWhNtX8I2aD-0fBGdd2EKKp1NtZuxpo0uX7_Co'

@client.event
async def on_ready():
    print('Logged in')

client.run(token)