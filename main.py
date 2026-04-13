import asyncio

import discord
from discord.ext import commands

from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.command()
async def salve(ctx):
    await ctx.send("Fala meu chefe, oq ce manda")


async def main():
    async with bot:
        await bot.load_extension("cogs.music")
        await bot.load_extension("cogs.ai")
        await bot.start(TOKEN)


asyncio.run(main())
