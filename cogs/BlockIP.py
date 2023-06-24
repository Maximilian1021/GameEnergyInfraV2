import os

import discord
from discord.ext import commands
from functions.blockIpFunc import add_ip_to_docker_user_chain


class BlockIP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def blockIP(self, ctx, message: str):
        try:
            add_ip_to_docker_user_chain("server1.max1021.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("server2.max1021.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("server4.max1021.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("server5.max1021.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("server7.max1021.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("bots.max1021.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("ServerR1.game-energy.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("ServerR2.game-energy.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)
            add_ip_to_docker_user_chain("ServerR3.game-energy.de", "2811", os.getenv('Path_To_SSHKey'), "root", message)

            # Code für erfolgreiche Ausführung
            embed = discord.Embed(title="Ip erfolgreich geblockt", colour=discord.Colour.green(),
                                  description="Die IP wurde erfolgreich auf allen Server gesperrt")
            embed.set_footer(text=f"IP Block wurde von {ctx.author} ausgelöst",
                             icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
            await ctx.send(embed=embed)

        except Exception as e:
            # Code für Fehlerfall
            embed = discord.Embed(title="Es ist ein Fehler aufgetreten", colour=discord.Colour.red(),
                                  description=f"Bei der Ausführung des Commands ist ein Fehler aufgetreten.\n "
                                              f"**Error:** {e} \n Mehr Information findest du in der Console!")
            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(BlockIP(bot))
