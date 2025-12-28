# Pycord-Template

My ***personal***, modern, and type-safe Discord bot template written in Python with [Pycord](https://pycord.dev/).

## Features
- [uv](https://github.com/astral-sh/uv) for fast dependency management
- [mypy](https://mypy-lang.org/) for static type checking
- [ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Main & debug bot configuration with `.env` support

## Quick Start

### Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Install dependencies**:

   ```bash
   uv sync
   ```

2. **Configure environment variables**:

   - Copy `.env.example` to `.env`
   - Get your bot token from the [Discord Developer Portal](https://discord.com/developers/applications)
   - Edit `.env` and add your Discord bot token:
     ```env
     token=YOUR_BOT_TOKEN_HERE
     uid=YOUR_BOT_ID_HERE
     ```

3. **Run the bot**:
   ```bash
   uv run python main.py
   ```

## Development

### Project Structure

```
Pycord-Template/
├── cogs/               # Bot command modules (cogs)
│   └── template.py     # Example cog
├── main.py             # Bot entry point
├── settings.py         # Configuration management
├── pyproject.toml      # Project metadata and dependencies
├── .env                # Environment variables (create from .env.example)
└── .env.example        # Example environment variables
```

### Creating New Cogs

Create a new file in the `cogs/` directory:

```python
"""Your cog description."""

import discord
from discord.ext import commands


class YourCog(commands.Cog):
    """Your cog class description."""

    def __init__(self, bot: discord.Bot) -> None:
        """Initialize the cog."""
        self.bot = bot

    @discord.slash_command(
        name="your_command",
        description="Your command description",
    )
    async def your_command(self, ctx: discord.ApplicationContext) -> None:
        """Your command implementation."""
        await ctx.respond("Hello!")


def setup(bot: discord.Bot) -> None:
    """Set up the cog."""
    bot.add_cog(YourCog(bot))
```

Cogs are automatically loaded from the `cogs/` directory when the bot starts.

### Debug/Testing Configuration

For running a test bot alongside your main bot, you can add debug variables to your `.env` file.


The bot will use `token_debug` and `uid_debug` if they exist, otherwise it falls back to `token` and `uid`. Simply comment out or remove the debug variables to switch back to your production bot.


