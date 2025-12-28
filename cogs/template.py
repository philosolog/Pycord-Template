"""Template cog for the Discord bot.

This module serves as a template for creating new cogs.
"""

import discord
from discord.ext import commands

class TemplateCog(commands.Cog):
    """A template cog demonstrating basic slash command structure."""

    def __init__(self, bot: discord.Bot) -> None:
        """Initialize the template cog.

        Args:
            bot: The Discord bot instance.
        """
        self.bot = bot

    @discord.slash_command(
        name="example",
        description="An example slash command",
    )
    async def example_command(self, ctx: discord.ApplicationContext) -> None:
        """Example slash command that responds with a message.

        Args:
            ctx: The application context for the command.
        """
        await ctx.respond("# What a useful slash command!")


def setup(bot: discord.Bot) -> None:
    """Set up the template cog.

    Args:
        bot: The Discord bot instance.
    """
    bot.add_cog(TemplateCog(bot))
