from discord.ext import commands

from config import config


class SuggestionsAddReactions(commands.Cog):
    # Might be better in other file
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = config.get("channels.suggestions")

    @commands.Cog.listener('on_message')
    async def add_reaction(self, message):
        if message.channel.id == self.channel_id:
            await message.add_reaction("👍")
            await message.add_reaction("👎")


def setup(bot: commands.Bot):
    bot.add_cog(SuggestionsAddReactions(bot))
