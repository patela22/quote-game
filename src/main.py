from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from quotes import give_quote_call, check_answer_call

load_dotenv()

# Channel IDs
austin_channel = os.getenv('austin')
ansh_channel = os.getenv('ansh')
ani_channel = os.getenv('ani')
jay_channel = os.getenv('jay')
channel_ids = [austin_channel, ansh_channel, ani_channel, jay_channel]
game_channel = int(os.getenv('game'))

TOKEN = os.getenv('TOKEN')

# Configure intents to allow the bot to receive messages
intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="/b0t ", intents=intents)

austin_quotes = ["Austin"]
ansh_quotes = ["Ansh"]
ani_quotes = ["Ani"]
jay_quotes = ["Jay"]
all_quotes = [austin_quotes, ansh_quotes, ani_quotes, jay_quotes]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    # Load message histories asynchronously on bot start
    for i in range(len(channel_ids)):
        print(f"Getting quotes from channel {channel_ids[i]}")
        await get_quotes(channel_ids[i], all_quotes[i])
    print (all_quotes)

async def get_quotes(channel_id, quote_list):
    channel = bot.get_channel(int(channel_id))
    if channel:
        async for message in channel.history(limit=None):  # You can adjust the limit as needed
            quote_list.append(message.content)
        print(f"Loaded {len(quote_list)} quotes from {channel.name}.")

# @bot.command(help="Gives a random quote")
# async def give_quote(game_channel):
#     quote = await give_quote_call(all_quotes)
#     await game_channel.send(quote)

# @bot.command(help="Checks the current game answer")
# async def check_answer(game_channel):
#     answer = await check_answer_call()
#     await game_channel.send(answer)

@bot.command(help="Gives a random quote")
async def give_quote(ctx):
    if ctx.channel.id == game_channel:
        quote = give_quote_call(all_quotes)
        await ctx.send(quote)
    else:
        await ctx.send("This command can only be used in the game channel.")

@bot.command(help="Checks the current game answer")
async def check_answer(ctx):
    if ctx.channel.id == game_channel:
        answer = check_answer_call()
        await ctx.send(answer)
    else:
        await ctx.send("This command can only be used in the game channel.")

bot.run(TOKEN)
