"""
bot.py
Discord bot for fetching and sharing memes via API integration.

Created: 2025-02-17 01:20:13 (UTC)
Author: rinmz
"""

import logging
import os
import json
from typing import Any, Dict

import discord
import requests
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if DISCORD_TOKEN is None:
    logger.error("DISCORD_TOKEN is not set. Please check your .env file.")
    exit(1)

MEME_API_URL = "https://meme-api.com/gimme"

class MemeClient(discord.Client):
    """Custom Discord client for meme handling with enhanced error management."""

    async def on_ready(self) -> None:
        """Callback when bot successfully connects to Discord."""
        logger.info("Logged on as %s (ID: %d)", self.user.name, self.user.id)

    async def on_message(self, message: discord.Message) -> None:
        """Handle incoming messages with command processing.

        Args:
            message (discord.Message): The message that was received.
        """
        if message.author == self.user:
            return

        if message.content.startswith("$meme"):
            try:
                meme_url = self._fetch_meme()
                await message.channel.send(meme_url)
            except requests.exceptions.RequestException as e:
                logger.error("API request failed: %s", str(e))
                await message.channel.send("🚫 Couldn't fetch meme. Try again later!")

    def _fetch_meme(self) -> str:
        """Fetch meme URL from API with proper error handling.

        Returns:
            str: The URL of the fetched meme.

        Raises:
            requests.exceptions.RequestException: An error occurred during the API request.
        """
        response = requests.get(MEME_API_URL, timeout=10)
        response.raise_for_status()
        return response.json()["url"]

def configure_intents() -> discord.Intents:
    """Configure and return Discord intents.

    Returns:
        discord.Intents: The configured intents.
    """
    intents = discord.Intents.default()
    intents.message_content = True
    return intents

def main() -> None:
    """Entry point for bot execution."""
    intents = configure_intents()
    client = MemeClient(intents=intents)
    client.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()