import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

PREFIX = ("!")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@bot.event
async def task():
    while True:
        await bot.change_presence(status=discord.Status.online)
        await asyncio.sleep(1)
        await bot.change_presence(status=discord.Status.idle)
        await asyncio.sleep(1)
        await bot.change_presence(status=discord.Status.dnd)
        await asyncio.sleep(1)


@bot.event
async def on_ready():
    bot.loop.create_task(task())
    print("Bot is ready!")



    

bot.run('OTgzNzUwMzk3MDk5NDA1MzEz.GfmFTU.4ixVpNBtyNCJEjrCBiE-1W71fEgczF63uLyR_8')