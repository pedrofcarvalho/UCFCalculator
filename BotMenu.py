import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import BotFunctions
import UserInfo

# TODO - DELETE THIS LATER (USE A HASH TABLE)
single_user = UserInfo.User(168.750, 45.000)

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
async def help(ctx):
    await BotFunctions.help(ctx)


# initiates the GPA calculation process
@bot.command(name="calculateGPA", aliases=["GPA", "calculate"])
async def calculateGPA(ctx, credit_points: float, credits_taken: float):
    await BotFunctions.calculateGPA(ctx, credit_points, credits_taken)


@bot.command(name="add", aliases=["ass"])
async def add(ctx, class_name, class_grade, class_credit: int):
    await BotFunctions.add(ctx, class_name, class_grade, class_credit)


# TODO
@bot.command(name="finish", aliases=["end", "f", "e"])
async def finish(ctx):
    await BotFunctions.finish(ctx)


# general methods
async def show_embed(ctx, gpa, user, name, grade, hours):
    await BotFunctions.show_embed(ctx, gpa, user, name, grade, hours)


async def display_classes_on_embed(ctx, user):
    await BotFunctions.display_classes_on_embed(ctx, user)


bot.run(TOKEN)
