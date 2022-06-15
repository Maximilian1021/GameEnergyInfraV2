import datetime
import json
import os

import discord
import requests
from discord.ext import commands

url = f'{os.getenv("SITE")}api/application/users'

headers = {
    "Authorization": f"Bearer {os.getenv('KEY')}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}


class CreationException(BaseException):
    pass


class Pterodactyl(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def initializer(self):
        self.bot.add_view(CreateAccount())

    @commands.slash_command(guild_ids=[889887499810394112])
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def account(self, ctx: discord.ApplicationContext, member: discord.Option(discord.Member,
                                                                                    "Member, dem die DM zugestellt "
                                                                                    "wird")):

        """
        Sendet ein Accounterstellungs-Panel an den gewählten Member
        :param ctx:
        :param member:
        :return:
        """
        try:
            embed = discord.Embed(title="Benutzeraccount anlegen", colour=discord.Colour.green(),
                                  description=f"Hallo {member.display_name} \n\n "
                                              "Diese Nachricht hast du "
                                              "erhalten, weil dein Antrag auf "
                                              "Sponsoring __akzeptiert__ wurde. "
                                              "\n\n Damit "
                                              "ich dir ein Server anlegen kann, "
                                              "benötigst du ein Benutzeraccount! "
                                              "Diesen kannst du dir mit dieser "
                                              "Nachricht selbst erstellen \n\n "
                                              "**WICHTIG** \n"
                                              "- Bitte gib eine E-Mail an auf welche"
                                              "du zugreifen kannst\n"
                                              "- Bitte gib auch einen Nachnamen an. "
                                              "Wenn du diesen nicht angeben möchtest,"
                                              "gibt etwas fiktives / erfundenes ein! "
                                              "\n\nNachdem du erfolgreich dein Account"
                                              " hier erstellt hast, bekommst du eine "
                                              "E-Mail wo du dein Password festlegen"
                                              "kannst.\n Teilweise landen diese auch "
                                              "im Spam! Schau dann auch dort nach")
            embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                             icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")
            await member.send(embed=embed, view=CreateAccount())
            await ctx.respond(f"Eine DM wurde an {member.display_name} zugestellt.", ephemeral=True)
        except discord.Forbidden:
            await ctx.respond(f"Der Bot konnte {member.display_name} keine DM zustellen", ephemeral=True)

    @account.error
    async def Error(self, ctx, err):
        embed = discord.Embed(title="Nicht berechtigt!", colour=discord.Colour.red(),
                              description="Du bist nicht berechtigt den Command auszuführen.")
        embed.set_footer(text="Nachricht wird in 10 Sekunden gelöscht")
        raise err
        print(err)
        await ctx.respond(embed=embed, delete_after=10)


def setup(bot: commands.Bot):
    bot.add_cog(Pterodactyl(bot))


def create_user(first_name, last_name, username, email):
    payload = {"email": email, "username": username, "first_name": first_name, "last_name": last_name}
    response = requests.request('POST', url, data=json.dumps(payload), headers=headers)
    if response.status_code == 201:
        return
    else:
        errmsg = json.loads(response.text)
        for i in errmsg["errors"]:
            raise CreationException(f"{i['code']}: {i['detail']}")


class CreateAccount(discord.ui.View):
    def __init__(self, *items: discord.ui.Item):
        super().__init__(*items, timeout=None)

    @discord.ui.button(label="Account erstellen", style=discord.ButtonStyle.primary, custom_id="CreateAccount")
    async def send_modal(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(AcccountModal())


class AcccountModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Account erstellen")
        self.add_item(discord.ui.InputText(label="Vorname", placeholder="Max"))
        self.add_item(discord.ui.InputText(label="Nachname (evtl. fiktiv)", placeholder="Mustermann"))
        self.add_item(discord.ui.InputText(label="E-Mail", placeholder="max@mustermann.de"))
        self.add_item(discord.ui.InputText(label="Benutzername", placeholder="M4XMU"))

    async def callback(self, interaction: discord.Interaction):
        try:
            create_user(self.children[0].value, self.children[1].value, self.children[3].value, self.children[2].value)
            print(datetime.datetime.now(), " User created", self.children[3].value)
        except CreationException as e:
            embed = discord.Embed(title="Fehler bei Accounterstellung", colour=discord.Colour.red(),
                                  description=f"Bei der Erstellung des Accounts ist folgender Fehler aufgetreten: "
                                              f"{e.args[0]}")
            embed.set_footer(text="Diese Nachricht wird in 2 Min gelöscht.")
            await interaction.response.send_message(embed=embed, delete_after=120)
            return
        embed = discord.Embed(title="Account erfolgreich erstellt", colour=discord.Colour.brand_green(),
                              description=f"Dein Account wurde erfolgreich erstellt "
                                          f"Schau nun in dein E-Mail Postfach!")
        await interaction.response.edit_message(content=None, embed=embed, view=None)
