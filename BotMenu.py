import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import BotFunctions

# constants
UCF_LOGO = discord.File("imagesFolder/knights_logo.jpg", filename="knights_logo.jpg")   # todo - (maybe delete)

# opens the '.env' file and stores its content
load_dotenv('venv/.env')
TOKEN = os.getenv('TOKEN')

# set the Bot's prefix to '$' and remove the default help command
bot = commands.Bot(command_prefix='$')
bot.remove_command("help")


# confirms the bot is ON
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# TODO
@bot.command(name="help", aliases=["h"])
async def help_command(ctx):
    await BotFunctions.help_command(ctx)


# initiates the GPA calculation process
@bot.command(name="calculateGPA", aliases=["GPA", "calculate", "gpa", "start"])
async def calculateGPA(ctx, credit_points: float, credits_taken: float):
    await BotFunctions.calculateGPA(ctx, credit_points, credits_taken)


@bot.command(name="add", aliases=["ass"])
async def add(ctx, class_name, class_grade, class_credit: int):
    await BotFunctions.add(ctx, class_name, class_grade, class_credit)


@bot.command(name="finish", aliases=["end", "f", "e"])
async def finish_info(ctx):
    await BotFunctions.finish_info(ctx)


# TODO - DELETE LATER!!!!!
@bot.command()
async def test(ctx):
    pass

bot.run(TOKEN)
