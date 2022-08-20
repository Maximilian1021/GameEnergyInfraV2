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
                              description="Dieser Channel ist für Vorschläge welche Fragen in den FAQ aufgenommen "
                                          "werden sollen gedacht. Bitte schreibt eure Fragen und eine Mögliche Antwort"
                                          " in diesen Channel \n\n_Beispiel:_\n  **F**: Wie bekomme ich ein Server\n"
                                          "**A**: Erstelle ein Ticket!"
                                          "\n\n Der Bot fügt automatisch :thumbsup: und :thumbsdown: an deine "
                                          "Nachricht als Reaktion hinzu. Jeder User kann dafür abstimmen!! \nDu kannst "
                                          "nur alle 60 Minuten eine Nachricht in den Channel schreiben!",
                              colour=discord.Colour.teal())
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def URLAUB(self, ctx):
        embed = discord.Embed(title="Urlaub vom 22.8 - 28.8 - Veränderter Support ",
                              description="Lieber Member des Discords \n\n Für mich geht es ab Montag in den Urlaub. "
                                          "In dieser Zeit kann ich keinen Support leisten und Server einrichten \n\n"
                                          "Für alle bestehenden Server geht aber die aktuelle Aktivitätskontrolle und "
                                          "der Support wie gewohnt weiter. Hierfür stehen euch <@572808505304809502> "
                                          "und <@560491862880944139> zu Verfügung. (An alle anderen Bewerber ihr seid "
                                          "schon noch im Rennen!) \n \n Ich bin für euch ab dem 29. August wieder da \n"
                                          "\nVielen Dank für euer Verständnis und bis nächstes mal",
                              colour=discord.Colour.teal())
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(ChannelBeschreibungen(bot))
