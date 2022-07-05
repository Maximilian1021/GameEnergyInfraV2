import random
import discord
from discord.ext import commands


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(manage_guild=True)
    async def giveaway(self, ctx, message_link: str, winners: int, emoji: str):
        """
        Chooses a winner from a giveaway
        :param ctx: Command Context
        :param message_link: Link to the message you want
        :param winners: Amount of winners
        :param emoji: Emoji that has been used for the giveaway
        :return:
        """
        info = message_link.split("/")
        try:
            if not int(info[4]) == ctx.guild.id:
                raise commands.CommandError("Bitte gib eineen Link zu einer Nachricht in diesem Server an.")
            message = await ctx.guild.get_channel(int(info[5])).fetch_message(int(info[6]))
        except IndexError or discord.NotFound:
            raise commands.CommandError("Bitte gib einen gültigen Link an")
        reaction: discord.Reaction = discord.utils.get(message.reactions, emoji=emoji)
        if not reaction:
            raise commands.CommandError("Bitte gib ein gültiges Emoji an")
        if winners > reaction.count:
            raise commands.CommandError("Bitte gib eine kleinere Anzahl an Gewinnern an")
        if winners < 1:
            raise commands.CommandError("Bitte gib eine größere Anzahl an Gewinnern an")
        if winners == 1:
            winner = random.choice(await reaction.users().flatten())
            await ctx.respond(f"Der Gewinner ist {winner.mention}")
        else:
            users = await reaction.users().flatten()
            _winners = []
            for i in range(winners):
                winner = random.choice(users)
                _winners.append(winner)
                users.remove(winner)
            _winners = [f"{i.mention}" for i in _winners]
            await ctx.respond(f"Die Gewinner sind {', '.join(_winners)}")


def setup(bot):
    bot.add_cog(Giveaway(bot))
