import discord
from dotenv import load_dotenv
import os
# import asyncio

load_dotenv()

# Channel IDs
austin_channel = os.getenv('austin')
ansh_channel = os.getenv('ansh')
ani_channel = os.getenv('ani')
jay_channel = os.getenv('jay')
channel_ids = [austin_channel, ansh_channel, ani_channel, jay_channel]

quote_game_channel = 1251976839736332369

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)
print(f"client name: {client}")

austin_quotes = []
ansh_quotes = []
ani_quotes = []
jay_quotes = []
all_quotes = [austin_quotes, ansh_quotes, ani_quotes, jay_quotes]

''''
1. go through each channel ✅ 
2. get each person's quotes in their own array ✅ 
3. repeat step 2 4 times ✅
4. combine all arrays into all_quotes ✅
5. (optional) git pull -m "sum bitches" ❌ - 404 error: not found
'''

@client.event
async def on_ready():
    for i in range(len(channel_ids)):
        print(f"Getting quotes from channel {channel_ids[i]}")
        await get_quotes(channel_ids[i], all_quotes[i])
    await client.close()

async def get_quotes(channel, quote_list):
    chan = client.get_channel(int(channel))
    print(chan)
    if chan is not None:
        async for message in chan.history(limit=None):
            quote_list.append(message.content)

client.run(TOKEN)

print(all_quotes)