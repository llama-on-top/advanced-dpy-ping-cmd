# Imports
import discord
from discord.ext import commands
import time
import asyncio

# Intents + Prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='p!', intents=intents)

# When bot is ready
@bot.event
async def on_ready():
    print(f'Ping command is ready to be used!')

# Ping command
@bot.command(name='ping')
async def ping(ctx):
    """Check API latency, bot latency, and reply delay."""
    # Measure API latency to Discord servers
    api_latency = round(bot.latency * 1000, 2)

    # Measure bot latency to Discord servers
    start_time_bot = time.time()
    message_bot = await ctx.send("Pinging Discord servers...")
    end_time_bot = time.time()
    bot_latency = round((end_time_bot - start_time_bot) * 1000, 2)

    # Measure user latency
    start_time_user = time.time()
    async with ctx.typing():  # Use ctx.typing() to trigger a typing indicator
        await asyncio.sleep(0.5)  # Simulate some work to measure user latency
    end_time_user = time.time()
    user_latency = round((end_time_user - start_time_user) * 1000, 2)

    # Calculate reply delay
    reply_delay = round((time.time() - end_time_bot) * 1000, 2)

# Create message
    embed = discord.Embed(title='Pong! 🏓', color=0x3498db)
    embed.add_field(name='API Latency', value=f'{api_latency}ms', inline=False)
    embed.add_field(name='Bot Latency', value=f'{bot_latency}ms', inline=False)
    embed.add_field(name='User Latency', value=f'{user_latency}ms', inline=False)
    embed.add_field(name='Reply Delay', value=f'{reply_delay}ms', inline=False)

    await message_bot.edit(content=None, embed=embed)

# Error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use `!help` for a list of available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument. Check the command usage with `!help`.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(f"Error executing the command: {error.original}")
    else:
        await ctx.send(f"An error occurred: {error}")

# Bot token
bot.run('MTE3Mjk2MjUxODQ2NjA0ODA4Mg.GwnxAi.PXaa5Vgd6BgxtER4gbgsSRaJpYnLeMYBy4650U')
