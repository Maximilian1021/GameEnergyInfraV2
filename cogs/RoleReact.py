import typing

import discord
from discord.ext import commands


class RoleReact(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.message_id: int = 988133183541354516

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def RollenverteilungPic(self, ctx):

        embed = discord.Embed(colour=discord.Colour.teal())
        embed.set_image(url="https://img.max1021.de/cooltext393608521752631.png")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def RollenverteilungDesc(self, ctx):

        embed = discord.Embed(title="Rollen erhalten!!",
                              description="Hier könnt ihr euch selbstständig Rollen zuweisen. Derzeit gibt es folgende "
                                          "Rollen zur Benachrichtigung \n\n"
                                          ":fire: - Notify-Störung (Wird markiert bei Größeren Störungen)\n"
                                          ":green_book: - Notify-Neuerung (Wird markiert bei Neuerungen am "
                                          "Panel oder Discord)\n\n Reagiere mit dem entsprechenden Emote um die Rolle "
                                          "zu erhalten!",
                              colour=discord.Colour.teal())
        mess = await ctx.send(embed=embed)
        await mess.add_reaction("🔥")
        await mess.add_reaction("📗")
        await ctx.message.delete()

    @commands.Cog.listener("on_raw_reaction_add")
    async def reaction_add(self, payload: discord.RawReactionActionEvent):
        role = await self.get_role(payload)
        if not role:
            return
        await role.guild.get_member(payload.user_id).add_roles(role, reason="Reactionroles")

    @commands.Cog.listener("on_raw_reaction_remove")
    async def reaction_remove(self, payload: discord.RawReactionActionEvent):
        role = await self.get_role(payload)
        if not role:
            return
        await role.guild.get_member(payload.user_id).remove_roles(role, reason="Reactionroles")

    async def get_role(self, payload: discord.RawReactionActionEvent) -> typing.Union[discord.Role, None]:
        """
        Returns the corresponding role to a given reaction
        :param payload: The payload of the reaction
        :return: The role
        """
        if not payload.message_id == self.message_id:
            return None
        guild = self.bot.get_guild(payload.guild_id)
        if payload.emoji.id:
            return None
        if str(payload.emoji) == "🔥":
            return guild.get_role(889983007480479744)
        elif str(payload.emoji) == "📗":
            return guild.get_role(889983085108678686)
        else:
            return None

def setup(bot: commands.Bot):
    bot.add_cog(RoleReact(bot))


    # 889983085108678686 -> Notify Neuerung 📗
    # 889983007480479744 -> Notify Störung 🔥