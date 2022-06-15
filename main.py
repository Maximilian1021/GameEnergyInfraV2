import datetime
import os
from pathlib import Path
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("Bot.env")

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"), intents=discord.Intents.all(),
                   case_insensitive=True, description="Bot description", help_command=None, auto_sync_commands=True
                   )


@bot.event
async def on_ready():
    print('---------------------------')
    print(datetime.datetime.now())
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------------------')


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
    print(f"Reloaded at {datetime.datetime.now()}")


@bot.command()
async def reload(ctx):
    await client_reload()
    embed = discord.Embed(title="Reload abgeschlossen!", colour=discord.Colour.red(),
                          description="Alle Module des Discordsbots wurden erfolgreich neugeladen")
    embed.set_footer(text=f"Reload wurde von {ctx.author} ausgelöst",
                     icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx: commands.Context, error):
    errormsg = error
    embed = discord.Embed(title="Nicht berechtigt!", colour=discord.Colour.red(),
                          description=f"Du bist nicht berechtigt den Command auszuführen.\n Error: {errormsg}")
    embed.set_footer(text="Nachricht wird in 10 Sekunden gelöscht")

    await ctx.send(embed=embed)


if __name__ == "__main__":
    load()
    bot.run(f"{os.getenv('TOKEN')}")
