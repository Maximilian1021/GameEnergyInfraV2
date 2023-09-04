import os
from datetime import datetime
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

from config import config

load_dotenv("bot.env")

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"),
    intents=discord.Intents.all(),
    case_insensitive=True,
    description="Game-Energy Discord Bot",
    help_command=None,
    auto_sync_commands=True
)

now = datetime.now()
dt_string = now.strftime("%d.%m.%Y %H:%M:%S")


@bot.event
async def on_ready():
    print('---------------------------')
    print(dt_string)
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------------------')
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Game-Energy Discord"
        ),
        status=discord.Status.idle
    )


def extensions():
    files = Path("cogs").rglob("*.py")
    for file in files:
        yield file.as_posix()[:-3].replace("/", ".")


def load():
    for ext_file in extensions():
        try:
            bot.load_extension(ext_file)
            print(f"Loaded {ext_file}")
        except Exception as ex:
            print(f"Failed to load {ext_file}: {ex}")


def unload():
    for ext_file in extensions():
        try:
            bot.unload_extension(ext_file)
            print(f"Unloaded {ext_file}")
        except Exception as ex:
            print(f"Failed to unload {ext_file}: {ex}")


async def client_reload():
    unload()
    load()
    print(f"\nReloaded at {dt_string}")


@bot.command()
async def reload(ctx):
    await client_reload()
    config.reload()
    embed = discord.Embed(title="Reload abgeschlossen!", colour=discord.Colour.red(),
                          description="Alle Module des Discord Bots wurden erfolgreich neu geladen")
    embed.set_footer(text=f"Reload wurde von {ctx.author} ausgelöst",
                     icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx: commands.Context, error):
    if ctx.invoked_with in ["rename", "close"]:
        return
    embed = discord.Embed(title="Es ist ein Fehler aufgetreten", colour=discord.Colour.red(),
                          description=f"Bei der Ausführung des Commands ist ein Fehler aufgetreten.\n "
                                      f"**Error:** {error}")
    await ctx.send(embed=embed)


if __name__ == "__main__":
    load()
    bot.run(f"{os.getenv('TOKEN')}")
