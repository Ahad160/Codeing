import discord

TOKEN = 'MTIwNjg4OTgzMTk4OTUxMDIxNQ.GmYgry.fHzlPDU5h3DMpDqfZg8A5p5X3pb6mbugjf00cY'
CHANNEL_ID = 1206955833410330635  #
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await Upload("E:\Codeing\Python Language\Projects\Project_17\info.txt")
    await client.close()

async def Upload(file_path):
    channel = client.get_channel(CHANNEL_ID)

    with open(file_path, 'rb') as f:
        picture = discord.File(f)
        await channel.send(file=picture)

client.run(TOKEN)
