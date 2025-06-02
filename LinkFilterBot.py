import discord
import os
import re
from discord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv

# === CONFIG ===
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
ALLOWED_CHANNEL_ID = 1378465036397449316  # Replace with your specific channel ID


keep_alive()

# Regex to detect links
VALID_LINK_REGEX = re.compile(
    r"(https?://)?(www\.)?(tiktok\.com|youtu\.be|youtube\.com)/\S+"
)

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == ALLOWED_CHANNEL_ID:
        if not VALID_LINK_REGEX.search(message.content):
            await message.delete()
            await message.channel.send(
                f"{message.author.mention} Only **YouTube** and **TikTok** links are allowed in this channel.",
                delete_after=5
            )
    await bot.process_commands(message)

bot.run(TOKEN)
