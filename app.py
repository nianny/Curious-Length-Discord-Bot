import discord
from discord.ext import commands

client = commands.Bot(command_prefix="l!", intents=discord.Intents.all(), allowed_mentions=discord.AllowedMentions.all())
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('l!help'))
    print("We have logged in as {0.user}".format(client))

@client.command()
async def sm(ctx):
    message = "hall"
    for i in range(10000):
        message += "o"
    await ctx.send(message)

client.run("") #insert auth token