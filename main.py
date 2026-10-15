import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Online als {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Commands gesynct")
    except Exception as e:
        print(e)

@bot.tree.command(name="ping", description="Test ob der Bot online ist")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong! Bot ist online! 🏓")

bot.run(os.getenv("DISCORD_TOKEN"))
