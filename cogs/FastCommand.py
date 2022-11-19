import discord
from discord.ext import commands


class Fastcommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def pmbybot(self, ctx):
        embed = discord.Embed(title="Anfrage zum Anlegen des Benutzeraccounts", colour=discord.Colour.blurple(),
                              description="Der Bot <@962376837063905301> hat dir eine PM geschrieben, in der du "
                                          "aufgefordert wirst einen Benutzeraccount für das Panel zu erstellen, auf dem"
                                          " du dein Server verwalten kannst. Bitte fülle das ganze aus und melde dich "
                                          "erneut hier im Ticket")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def pmWelcome(self, ctx):
        embed = discord.Embed(title="Herzlich Willkommen bei Game-Energy", colour=discord.Colour.blurple(),
                              description="Willkommen bei **Game-Energy**. Vielen Dank, dass du eine Anfrage für ein "
                                          "Server Sponsoring schickst.\n Bevor ich entscheiden kann, ob ein Sponsoring"
                                          " in Frage kommt, benötige ich noch einige Infos von dir.\n\n"
                                          "- Mit wie vielen Spielern gleichzeitig rechnest auf dem Server?\n"
                                          "- Kannst du mir sagen wie lange dein Projekt geht?\n"
                                          "- Hast du Erfahrungen, wie du einen Server verwaltest und einrichtest?\n\n"
                                          "Schreibe bitte auf jede Frage __eine Antwort__")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    # @commands.command()
    # async def botHelp(self, ctx):
    #     embed = discord.Embed(title="Game-Energy Infra Command Help", colour=discord.Colour.green(),
    #                           description="Hier bekommst du alle Commands und Funktionen von Game-Energy Infra Bot!\n"
    #                                       "Es gibt einen Musikbot und weitere Sinnvolle Commands Diese findest du hier")
    #
    #     embed.add_field(name='$join', value="Der Musikbot joint in deinen aktuellen Channel", inline="false")
    #     embed.add_field(name='$play <text/Url>', value="Spielt den ersten Song", inline="false")
    #     embed.add_field(name='$leave', value='Der Bot verlässt den Channel', inline="false")
    #     embed.add_field(name='$queue', value="Der Bot zeigt dir die Warteschlange", inline="false")
    #     embed.add_field(name='$skip', value="Überspringt den aktuellen Song", inline="false")
    #     embed.add_field(name='$stop', value="Stoppt die Wiedergabe", inline='false')
    #     embed.add_field(name='$current', value='Zeigt aktuelle Infos zum Song', inline='false')
    #     embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
    #                      icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
    #     await ctx.send(embed=embed)
    #     await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def pmWelcomeBot(self, ctx):
        embed = discord.Embed(title="Herzlich Willkommen bei Game-Energy", colour=discord.Colour.blurple(),
                              description="Willkommen bei **Game-Energy**. Vielen Dank, dass du eine Anfrage für ein "
                                          "Discord-Bot-Hosting schickst.\n Bevor ich entscheiden kann, ob ein "
                                          "Discordbot-Sponsoring in Frage kommt. Benötige ich noch einige Infos "
                                          "von dir.\n\n"
                                          "- Stell dein Projekt bitte kurz vor"
                                          "- Mit welcher Sprache ist der Bot geschrieben? (Java, Python, JS etc.)\n"
                                          "- Welche Funktionen hat der Bot? (Kick, Ban, Verify, Musik etc.) \n"
                                          "- Auf wie vielen Server ist dein Bot derzeit aktiv? \n"
                                          "\n Bitte beantworte alle Fragen ehrlich!")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(Fastcommands(bot))
