"""Main entry point for the Discord bot.

This module initializes the bot, loads cogs, and starts the bot.
"""

import asyncio
import logging
import discord
import settings

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# *: https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop
try:
	asyncio.get_running_loop()
except RuntimeError:
	asyncio.set_event_loop(asyncio.new_event_loop())

bot = discord.Bot(
	intents=discord.Intents.default(),
	owner_id=int(settings.uid) if settings.uid else None,
)

def load_cogs() -> None:
	"""Load all cogs from the cogs directory."""
	if not settings.cogs_directory.exists():
		logger.warning("Cogs directory not found: %s", settings.cogs_directory)
		return

	for cog_file in settings.cogs_directory.glob("*.py"):
		if cog_file.name.startswith("_"):
			continue

		cog_name = f"cogs.{cog_file.stem}"
		try:
			bot.load_extension(cog_name)
			logger.info("Loaded cog: %s", cog_name)
		except Exception:
			logger.exception("Failed to load cog: %s", cog_name)


@bot.event
async def on_ready() -> None:
	"""Event handler for when the bot is ready."""
	if bot.user is None:
		logger.error("Bot user is None")
		return

	logger.info("Logged in as %s (ID: %s)", bot.user.name, bot.user.id)
	await bot.change_presence(
		status=discord.Status.online,
		activity=discord.Game("with Pycord"),
	)

def main() -> None:
	"""Main function to start the bot."""
	logger.info("Starting bot...")
	load_cogs()
	bot.run(settings.token)

if __name__ == "__main__":
	main()
