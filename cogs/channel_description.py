import discord
from discord.ext import commands


class ChannelDescriptions(commands.Cog):
    # Class name is not descriptive

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="VorschlagPic")
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def suggestion_pic(self, ctx):
        # What is this needed for?
        embed = discord.Embed(colour=discord.Colour.teal())
        embed.set_image(url="https://img.max1021.de/cooltext413443916933016.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def suggestion_description(self, ctx):
        embed = discord.Embed(title="Vorschlag einreichen!",
                              description="Dieser Channel ist für Vorschläge für Fragen, die in den FAQ aufgenommen "
                                          "werden sollen gedacht. Bitte schreibt eure Fragen und eine mögliche Antwort "
                                          "in diesen Channel\n\n_Beispiel:_\n**F**: Wie bekomme ich ein Server?\n"
                                          "**A**: Erstelle ein Ticket!"
                                          "\n\nDer Bot fügt automatisch :thumbsup: und :thumbsdown: an deine "
                                          "Nachricht als Reaktion hinzu. Jeder User kann dafür abstimmen!!\nDu kannst "
                                          "nur alle 60 Minuten eine Nachricht in den Channel schreiben!",
                              colour=discord.Colour.teal())
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="URLAUB")
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def vacation(self, ctx):
        # Questionable use of capital letters
        embed = discord.Embed(title="Urlaub vom 22.8 - 28.8 - Veränderter Support ",
                              description="Lieber Member des Discords\n\nFür mich geht es ab Montag in den Urlaub. "
                                          "In dieser Zeit kann ich keinen Support leisten und Server einrichten\n\n"
                                          "Für alle bestehenden Server geht aber die aktuelle Aktivitätskontrolle und "
                                          "der Support wie gewohnt weiter. Hierfür stehen euch <@572808505304809502> "
                                          "und <@560491862880944139> zu Verfügung. (An alle anderen Bewerber ihr seid "
                                          "schon noch im Rennen!)\n\n Ich bin für euch ab dem 29. August wieder da\n"
                                          "\nVielen Dank für euer Verständnis und bis nächstes mal",
                              colour=discord.Colour.teal())
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(ChannelDescriptions(bot))
