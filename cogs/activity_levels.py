import discord
from discord.ext import commands


class ActivityLevels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="akvSt1")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def activity_stage_one(self, ctx):
        embed = discord.Embed(title="Stufe 1 - Aktivitätsregelung", colour=discord.Colour.green(),
                              description="Ich habe festgestellt, das seit längerem keine Aktivität auf dem "
                                          "Server zu sehen ist!\n Gibt es derzeit irgendwelche Probleme bei welchen "
                                          "ich dich ggf. Unterstützen kann? \n\n Stufe 1 hat keine Auswirkungen "
                                          "auf deinen Server!\n\n Bitte melde dich innerhalb von **7 Tagen** hier "
                                          "im Ticket und sag mir wie es mit dem Sponsoring weitergehen soll!\n\n"
                                          "Viele Grüße \n\n **Maximilian1021** \n Game-Energy \n Administrator /"
                                          " Owner")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command("akvSt2")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def activity_stage_two(self, ctx):
        embed = discord.Embed(title="Stufe 2 - Aktivitätsregelung", colour=discord.Colour.orange(),
                              description="Ich habe weiterhin keine Aktivität auf deinem Server festgestellt oder "
                                          "du hast dich bei mir noch nicht gemeldet! Es treten nun folgende Punkte"
                                          " in Kraft: \n\nSollte dein Server noch laufen, wird dieser nun"
                                          " **gestoppt**. Du kannst ihn jederzeit wieder starten Der Server"
                                          " wird aber regelmäßig kontrolliert, ob auch wirklich drauf "
                                          "gespielt wird. \n oder \n Sollte der Server bereits gestoppt "
                                          "sein bleibt er gestoppt und steht weiterhin unter Beobachtung! "
                                          "\n\n Du hast nun __3 Tage__ Zeit dich bei mir Zurückzumelden, bevor du "
                                          "in Stufe 3 rutschst! \n\n"
                                          "Viele Grüße \n\n **Maximilian1021** \n Game-Energy \n Administrator /"
                                          " Owner")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="akvSt3")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def activity_stage_three(self, ctx):
        embed = discord.Embed(title="Stufe 3 - Aktivitätsregelung", colour=discord.Colour.red(),
                              description="Du hast dich nicht gemeldet oder die Aktivität auf dem Server hat "
                                          "sich nicht verändert! Dein Server ist nun gesperrt und du kannst "
                                          "auf keine Daten mehr zugreifen.\n\n **Das Sponsoring ist somit "
                                          "beendet**! \n\n Du erhältst in Kürze eine E-Mail mit "
                                          "dem letzten Backup deines Servers! \nDu bist für 3 Monate vom Sponsoring "
                                          "ausgeschlossen! Danach kannst du wieder eine Anfrage stellen.\n\n"
                                          "Viele Grüße \n\n **Maximilian1021** \n Game-Energy \n Administrator /"
                                          " Owner")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="MailBackup")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def mail_backup(self, ctx):
        embed = discord.Embed(title="Information über das Backup", colour=discord.Colour.darker_gray(),
                              description="Du erhältst in den nächsten paar Minuten eine E-Mail mit den Infos "
                                          "zu deinem Backup. Damit nur du das Backup herunterladen kannst bekommst "
                                          "eine PIN in der Mail mit dem Link zugeteilt. Damit kannst nur du auf "
                                          "den Download zugreifen! \n \n Wenn du Fragen dazu hast, schreib mich "
                                          "einfach an!\n\n"
                                          "Viele Grüße \n\n **Maximilian1021** \n Game-Energy \n Administrator /"
                                          " Owner")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(ActivityLevels(bot))
