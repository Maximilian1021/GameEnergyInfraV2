import datetime
import json
import os

import aiohttp
import discord
from discord.ext import commands

from config import config

url = f'{config.get("pterodactyl")}api/application/users'

headers = {
    "Authorization": f"Bearer {os.getenv('PTERODACTYL_KEY')}",
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

    @commands.slash_command(guild_ids=config.get("guilds"), description="Erstellt einen Benutzeraccount")
    @commands.has_permissions(view_audit_log=True, ban_members=True)
    async def account(self,
                      ctx: discord.ApplicationContext,
                      member: discord.Option(discord.Member, "Member, dem die DM zugestellt wird")
                      ):

        """
        Sendet ein Accounterstellungs-Modal an den gewählten Member
        :param ctx:
        :param member:
        :return:
        """
        embed = discord.Embed(title="Benutzeraccount anlegen", colour=discord.Colour.green(),
                              description=f"Hallo {member.display_name}\n\n "
                                          "Du erhältst diese Nachricht, da dein Antrag auf ein Sponsoring "
                                          "__akzeptiert__ wurde.\n\nDamit ich dir ein Server anlegen kann, "
                                          "benötigst du nun einen Benutzeraccount! Diesen kannst du dir mit dieser "
                                          "Nachricht selbst erstellen\n\n **WICHTIG**\n"
                                          "- Bitte gib eine E-Mail an auf welche du zugreifen kannst\n"
                                          "- Bitte gib auch einen Nachnamen an. Wenn du diesen nicht angeben "
                                          "möchtest, gib etwas fiktives / erfundenes ein!\n\n"
                                          "Nachdem du erfolgreich deinen Account hier erstellt hast, bekommst du "
                                          "eine E-Mail, mit der du dein Passwort festlegen kannst.\n"
                                          "Teilweise landen diese auch im Spam! Schau dann auch dort nach")
        embed.set_footer(text=f"Nachricht wurde von {ctx.author} ausgelöst",
                         icon_url="https://cdn.max1021.de/G-E/GameEnergy_Green.png")

        try:
            await member.send(embed=embed, view=CreateAccount())
            await ctx.respond(f"Eine DM wurde an {member.display_name} zugestellt.", ephemeral=True)
        except discord.Forbidden:
            await ctx.respond(f"Der Bot konnte {member.display_name} keine DM zustellen", ephemeral=True)

    @account.error
    async def error(self, ctx, err):
        embed = discord.Embed(title="Nicht berechtigt!", colour=discord.Colour.red(),
                              description="Du bist nicht berechtigt den Command auszuführen.")
        embed.set_footer(text="Nachricht wird in 10 Sekunden gelöscht")
        raise err
        # Currently unreachable code (due to raise). Commenting out for now.
        # print(err)
        # await ctx.respond(embed=embed, delete_after=10)


def setup(bot: commands.Bot):
    bot.add_cog(Pterodactyl(bot))


async def create_user(first_name, last_name, username, email):
    payload = {"email": email, "username": username, "first_name": first_name, "last_name": last_name}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=json.dumps(payload), headers=headers) as r:
            if r.status == 201:
                return
            else:
                errmsg = json.loads(await r.text())
                for i in errmsg["errors"]:
                    raise CreationException(f"{i['code']}: {i['detail']}")


class CreateAccount(discord.ui.View):
    def __init__(self, *items: discord.ui.Item):
        super().__init__(*items, timeout=None)

    @discord.ui.button(label="Account erstellen", style=discord.ButtonStyle.primary, custom_id="CreateAccount")
    async def send_modal(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(AccountModal())


class AccountModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Account erstellen")
        self.add_item(discord.ui.InputText(label="Vorname", placeholder="Max"))
        self.add_item(discord.ui.InputText(label="Nachname (ggf. fiktiv)", placeholder="Mustermann"))
        self.add_item(discord.ui.InputText(label="E-Mail", placeholder="max@mustermann.de"))
        self.add_item(discord.ui.InputText(label="Benutzername", placeholder="M4XMU"))

    async def callback(self, interaction: discord.Interaction):
        try:
            await create_user(self.children[0].value, self.children[1].value, self.children[3].value,
                              self.children[2].value)
            print(datetime.datetime.now(), " User created", self.children[3].value)
        except CreationException as e:
            embed = discord.Embed(title="Fehler bei Account Erstellung", colour=discord.Colour.red(),
                                  description=f"Bei der Erstellung des Accounts ist folgender Fehler aufgetreten: "
                                              f"{e.args[0]}")
            embed.set_footer(text="Diese Nachricht wird in 2 Minuten gelöscht.")
            await interaction.response.send_message(embed=embed, delete_after=120)
            return
        embed = discord.Embed(title="Account erfolgreich erstellt", colour=discord.Colour.brand_green(),
                              description=f"Dein Account wurde erfolgreich erstellt\n"
                                          f"Schau nun in dein E-Mail Postfach!")
        await interaction.response.edit_message(content=None, embed=embed, view=None)
