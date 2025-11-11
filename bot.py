# import discord
# from discord.ext import commands
# import logging
# import os
# from dotenv import load_dotenv
# from datetime import datetime


# load_dotenv()


# os.makedirs("log", exist_ok=True)


# log_filename = datetime.now().strftime("bot-%Y-%m-%d.log")
# log_path = os.path.join("log", log_filename)


# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
#     handlers=[
#         logging.FileHandler(log_path, encoding="utf-8"),
#         logging.StreamHandler()
#     ]
# )


# intents = discord.Intents.default()
# intents.message_content = True  # Required for message commands

# bot = commands.Bot(command_prefix="**", intents=intents)


# @bot.event
# async def on_ready():
#     logging.info(f"{bot.user} ~_~ ✅ ONLINE")

# @bot.command()
# async def ping(ctx):
#     await ctx.send("🏓 Pong!")
#     logging.info(f"Ping command used by {ctx.author} in #{ctx.channel}")


# token = os.getenv("DISCORD_TOKEN")
# if not token:
#     logging.error("❌ No DISCORD_TOKEN found in .env file.")
# else:
#     bot.run(token)

import discord
from discord import app_commands
from discord.ext import commands

# Replace this with your bot token
TOKEN = "TOKE HERE YOUR LOVEDAYYY"

intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔗 Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello", description="Say hello to the bot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"modi sar car , {interaction.user.mention}! ")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if "hi bot" in message.content.lower():
        await message.channel.send(f"shut your bitch ass up {message.author.mention}! 👋")
    await bot.process_commands(message)

bot.run(TOKEN)

