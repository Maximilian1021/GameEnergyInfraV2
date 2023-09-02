import discord
from discord.ext import commands

from helpers.ip_manager import block, unblock


class BlockIP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.command(name="blockIP")
    async def block_ip(self, ctx, ip: str):
        embed = discord.Embed(title="IP Block", colour=discord.Colour.blue(),
                              description=f"Die IP {ip} wird geblockt. Bitte habe einen Moment geduld.")
        embed.set_footer(text=f"IP Block wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        mess = await ctx.send(embed=embed)
        try:
            block(ip)
        except Exception as e:
            # Code für Fehlerfall
            embed = discord.Embed(title="Es ist ein Fehler aufgetreten", colour=discord.Colour.red(),
                                  description=f"Bei der Ausführung des Commands ist ein Fehler aufgetreten.\n "
                                              f"**Error:** {e} \n Mehr Information findest du in der Konsole!")
            await mess.edit(embed=embed)
            return

        # Code für erfolgreiche Ausführung
        embed = discord.Embed(title="IP erfolgreich geblockt", colour=discord.Colour.green(),
                              description=f"Die IP {ip} wurde erfolgreich auf allen Servern gesperrt")
        embed.set_footer(text=f"IP Block wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await mess.edit(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command(name="unblockIP")
    async def unblock_ip(self, ctx, ip: str):
        embed = discord.Embed(title="IP Unblock", colour=discord.Colour.blue(),
                              description=f"Die IP {ip} wird entblockt. Bitte habe einen Moment geduld.")
        embed.set_footer(text=f"IP Block wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        mess = await ctx.send(embed=embed)
        try:
            unblock(ip)
        except Exception as e:
            # Code für Fehlerfall
            embed = discord.Embed(title="Es ist ein Fehler aufgetreten", colour=discord.Colour.red(),
                                  description=f"Bei der Ausführung des Commands ist ein Fehler aufgetreten.\n "
                                              f"**Error:** {e} \n Mehr Information findest du in der Konsole!")
            await mess.edit(embed=embed)
            return
        embed = discord.Embed(title="IP erfolgreich freigegeben", colour=discord.Colour.green(),
                              description=f"Die IP {ip} wurde erfolgreich auf allen Servern freigegeben")
        embed.set_footer(text=f"IP Block wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await mess.edit(embed=embed)


def setup(bot):
    bot.add_cog(BlockIP(bot))
