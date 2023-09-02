import discord
from discord.ext import commands

from config import config


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role_name = config.get("roles.user")
        role = discord.utils.get(member.guild.roles, id=role_name)
        if role is not None:
            bot_member = member.guild.get_member(self.bot.user.id)
            bot_permissions = bot_member.guild_permissions
            if bot_permissions.manage_roles:
                await member.add_roles(role)


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
