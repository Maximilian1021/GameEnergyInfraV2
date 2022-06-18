from discord.ext import commands

channelid = 987494836783427594


class VorschaegeAddReaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def addReaction(self, message):
        if message.channel.id == channelid:
            await message.add_reaction("👍")
            await message.add_reaction("👎")


def setup(bot: commands.Bot):
    bot.add_cog(VorschaegeAddReaction(bot))
