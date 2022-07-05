import discord
from discord.ext import commands


class ChannelBeschreibungen(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def VorschlagPic(self, ctx):
        embed = discord.Embed(colour=discord.Colour.teal())
        embed.set_image(url="https://img.max1021.de/cooltext413443916933016.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def VorschlagDesc(self, ctx):
        embed = discord.Embed(title="Vorschlag einreichen!",
                              description="Dieser Channel ist für Vorschläge welche Fragen im FAQ aufgenommen werden "
                                          "sollen. Bitte schreibt eure Fragen und eine Mögliche Antwort in den Channel "
                                          "\n\n_Beispiel:_\n  **F**: Wie bekomm ich ein Server\n**A**: Erstell "
                                          "ein Ticket!"
                                          "\n\n Der Bot fügt automatisch :thumbsup: und :thumbsdown: an deine "
                                          "Nachricht. Jeder User kann dafür abstimmen!! \nDu kannst nur alle 60 "
                                          "Minuten eine Nachricht in den Channel schreiben!",
                              colour=discord.Colour.teal())
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(ChannelBeschreibungen(bot))
