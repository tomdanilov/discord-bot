from __future__ import annotations
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.bot.log('Bot is up.')


def setup(bot) -> None:
    bot.add_cog(Events(bot))
