# importing discord specificaly
import discord
from discord.utils import get
from discord.ext import commands
# use secret tokens
import os
# import canvas
from canvasapi import Canvas

# initialize canvas values
print("Starting up...")
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
C_NUM = os.getenv('C_NUM')
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(C_NUM)
print("Canvas connected successfully...")

# setting up the discord bot
intents = discord.Intents.all()

# creating the discord bot
client = commands.Bot(command_prefix = '-', intents=intents)

# a message when the discord bot is live
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# a message when joining a server
@client.event
async def on_guild_join(guild):
	await guild.system_channel.send(f"Hey guys! Thanks for inviting me to {guild.name}. I am totally not going to hack ur credit cards... You can read more about me and what I do here:\nhttps://replit.com/@SaminAmanat/Canvas-Bot-2")
		
@client.command()
async def ping(ctx):
	await ctx.send(course.name)
	await ctx.send("text")

# getting the bot to turn on using the token
client.run(os.getenv('TOKEN'))