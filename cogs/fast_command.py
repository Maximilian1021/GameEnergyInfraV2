import discord
from discord.ext import commands


class FastCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pmbybot", alias="dmbybot")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def dm_by_bot(self, ctx):
        # Could be sent at the same time as the dm
        embed = discord.Embed(title="Anfrage zum Anlegen des Benutzeraccounts", colour=discord.Colour.blurple(),
                              description=f"Der Bot {self.bot.user.mention} hat dir eine PM geschrieben, in der du "
                                          "aufgefordert wirst einen Benutzeraccount für das Panel zu erstellen, auf "
                                          "dem du dein Server verwalten kannst. Bitte fülle das ganze aus und melde "
                                          "dich erneut hier im Ticket")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="pmWelcome")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def dm_welcome(self, ctx):
        embed = discord.Embed(title="Herzlich Willkommen bei Game-Energy", colour=discord.Colour.blurple(),
                              description="Willkommen bei **Game-Energy**. Vielen Dank, dass du eine Anfrage für ein "
                                          "Server Sponsoring schickst.\n Bevor ich entscheiden kann, ob ein Sponsoring "
                                          "in Frage kommt, benötige ich noch einige Infos von dir.\n\n"
                                          "- Stelle dein Projekt bitte kurz vor \n"
                                          "- Mit wie vielen Spielern gleichzeitig rechnest auf dem Server?\n"
                                          "- Kannst du mir sagen wie lange dein Projekt geht?\n"
                                          "- Hast du Erfahrungen, wie du einen Server verwaltest und einrichtest?\n\n"
                                          "Schreibe bitte auf jede Frage __eine Antwort__")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    # @commands.command() async def botHelp(self, ctx): embed = discord.Embed(title="Game-Energy Infra Command Help",
    # colour=discord.Colour.green(), description="Hier bekommst du alle Commands und Funktionen von Game-Energy Infra
    # Bot!\n" "Es gibt einen Musikbot und weitere Sinnvolle Commands Diese findest du hier")
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

    @commands.command("pmWelcomeBot")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def dm_welcome_bot(self, ctx):
        # Could be merged with dm_welcome
        embed = discord.Embed(title="Herzlich Willkommen bei Game-Energy", colour=discord.Colour.blurple(),
                              description="Willkommen bei **Game-Energy**. Vielen Dank, dass du eine Anfrage für ein "
                                          "Discord-Bot-Hosting schickst.\n Bevor ich entscheiden kann, ob ein "
                                          "Discordbot-Sponsoring in Frage kommt. Benötige ich noch einige Infos "
                                          "von dir.\n\n"
                                          "- Stell dein Projekt bitte kurz vor\n"
                                          "- Mit welcher Sprache ist der Bot geschrieben? (Java, Python, JS etc.)\n"
                                          "- Welche Funktionen hat der Bot? (Kick, Ban, Verify, Musik etc.) \n"
                                          "- Auf wie vielen Server ist dein Bot derzeit aktiv? \n"
                                          "\n Bitte beantworte alle Fragen ehrlich!")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command("resetPW")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def reset_password(self, ctx):
        embed = discord.Embed(title="Passwort zurücksetzen", colour=discord.Colour.blurple(),
                              description="Du kannst dein Passwort unter \n\n"
                                          "https://panel.game-energy.de/auth/password \n \n zurücksetzen!")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="Subdomain")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def subdomain(self, ctx):
        embed = discord.Embed(title="Eigene Subdomain", colour=discord.Colour.blurple(),
                              description="Es stehen folgende Domains für eine Subdomain zur Verfügung! \n\n"
                                          "`***.game-energy.de`\n"
                                          "`***.game-energy.eu`\n"
                                          "`***.super-creative.de`\n\n"
                                          "Es kann nur das `***` geändert werden.")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command("SubdomainDone")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def subdomain_done(self, ctx):
        embed = discord.Embed(title="Subdomain erstellt", colour=discord.Colour.blurple(),
                              description="Deine Subdomain wurde nun angelegt. \n\n"
                                          "Es kann jedoch bis zu 24 Stunden dauern bis diese funktioniert \n \n "
                                          "Melde dich bitte erneut sollte sie nach 36h (1.5 Tagen) nicht "
                                          "funktionieren!")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="IpChange")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def ip_change(self, ctx):
        embed = discord.Embed(title="Du bist betroffen", color=discord.Colour.dark_red(),
                              description="Dein Server liegt auf einer Node, die von dem IP Wechsel"
                                          "betroffen ist. Es wird sich für dich nicht viel ändern, die Verwaltung "
                                          "findet weiterhin über das Web-Panel statt.\n\n Ich habe mit dem Hoster "
                                          "besprochen, dass der Wechsel zum folgenden Zeitpunkt stattfindet\n\n "
                                          "**Wann?** -> Am 21.05.2023 zwischen  20:30 - 20:45\n\nZu dem Zeitpunkt "
                                          "wird der Server in dem Wartungsmodus versetzt und alle laufenden Server "
                                          "heruntergefahren. Eine Verwaltung oder ein nutzen des Servers ist in der "
                                          "Zeit dann nicht möglich.\n\n **Muss ich etwas am Server ändern?** \n Du "
                                          "musst nur was ändern wenn du bspw. eine eigene Domain auf den Server "
                                          "geschaltet hast __oder__ von Game-Energy eine Domain geschaltet wurde. "
                                          "Diese wird nach dem Wechsel vorerst nicht funktionieren. Bitte melde dich "
                                          "dann bei uns.\n\n __Wenn du weitere Fragen hast oder Unsicherheit "
                                          "herrscht --> Melde dich__ ")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="ServerGesperrt")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def server_locked(self, ctx):
        embed = discord.Embed(title="Dein Server wurde gesperrt", colour=discord.Colour.dark_red(),
                              description="Am **__06.03.2023__** wurden alle Discord-Bot User aufgerufen sich zu "
                                          "melden, ob der Bot noch aktiv ist bzw. weiterentwickelt wird.\n\n Da du "
                                          "dich bis heute nicht gemeldet hast, wurde dein Server nun gestoppt und "
                                          "gesperrt!. Du hast nun **3 Tage Zeit**, dich zu melden, ansonsten wird das "
                                          "Sponsoring beendet und ihr bekommt ein Backup zugesendet.")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(FastCommands(bot))
