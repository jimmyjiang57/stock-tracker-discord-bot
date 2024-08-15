import discord
from discord.ext import commands
from polygon import RESTClient
import requests

bot = commands.Bot(command_prefix = ".", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")

with open("api-key.txt") as file:
    key = file.read()

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VOO&apikey=' + key
r = requests.get(url)
data = r.json()
date = data["Meta Data"]["3. Last Refreshed"]
quote = data["Time Series (Daily)"][date]["4. close"]
print(quote)

@bot.event
async def on_message(message):
    if message.content.startswith('VOO'):
        await message.channel.send(quote)

with open("token.txt") as file:
    token = file.read()

bot.run(token)