import discord
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Channel IDs
austin = os.getenv('austin')
ansh = os.getenv('ansh')
ani = os.getenv('ani')
jay = os.getenv('jay')

TOKEN = os.getenv('application_id')
CHANNEL_IDS = [austin, ansh, ani, jay]

client = discord.Client(intents=discord.Intents.default())

messages = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for channel_id in CHANNEL_IDS:
        channel = client.get_channel(channel_id)
        if channel is not None:
            async for message in channel.history(limit=None):
                messages.append(message.content)
    print("Messages collected")
    await client.close()

client.run(TOKEN)
