import discord
import os
import re
from discord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv

# === CONFIG ===
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN_IMAGE")
ALLOWED_CHANNEL_ID = 1378865895656521830  # Replace with your specific channel ID


keep_alive()


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required for reading message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    if message.channel.id == ALLOWED_CHANNEL_ID:
        # Check if message has attachments and all are images
        if message.attachments:
            if all(attachment.content_type and attachment.content_type.startswith('image/') for attachment in message.attachments):
                await bot.process_commands(message)
            else:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, only image files are allowed in this channel.", delete_after=5)
        else:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, only image messages are allowed in this channel.", delete_after=5)
    else:
        await bot.process_commands(message)

# Run the bot
# Commented out for external execution
# bot.run(TOKEN)

# Expose the bot and token for main.py
__all__ = ['bot']
bot.TOKEN = TOKEN

