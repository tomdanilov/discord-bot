from __future__ import annotations
from discord.ext import commands
import time


class Fun(commands.Cog):

    def __init__(self, bot) -> None:
        """ All the fun commands are contained in this Fun cog class. """
        self.bot = bot

    @commands.command()
    async def ping(self, ctx) -> None:
        start = time.perf_counter()
        await ctx.trigger_typing()

        end = time.perf_counter()
        time_delta = round((end - start) * 1000)

        await ctx.send(f'Pong! {time_delta}ms')


def setup(bot) -> None:
    bot.add_cog(Fun(bot))
