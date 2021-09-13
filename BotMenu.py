import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import UserInfo

# TODO - DELETE THIS LATER (USE A HASH TABLE)
single_user = UserInfo.User(168.750, 45.000)

# constants
UCF_LOGO = discord.File("imagesFolder/knights_logo.jpg", filename="knights_logo.jpg")

# opens the '.env' file and stores its content
load_dotenv('venv/.env')
TOKEN = os.getenv('TOKEN')

# set the Bot's prefix to '$'
bot = commands.Bot(command_prefix='$')


# confirms the bot is ON
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# initiates the GPA calculation process
@bot.command(name="calculateGPA", aliases=["GPA", "calculate"])
async def calculateGPA(ctx, credit_points: float, credits_taken: float):
    single_user.get_class_list()

    # calculates the GPA
    final_GPA = round(credit_points / credits_taken, 2)

    # checks if the GPA is valid
    if final_GPA < 0.0 or final_GPA > 4.0:
        await ctx.channel.send('Invalid Input')
        return

    await show_embed(ctx, final_GPA, ctx.author)


@bot.command(name="delete")
async def clear(ctx):
    message = await ctx.channel.fetch_message()
    await message.delete()


# TODO - MAKE THE CLASS DESIGN BETTER HERE
@bot.command(name="add", aliases=["ass"])
async def add(ctx, class_name, class_grade, class_credit: int):
    # adds a new class to the user's list based on user input
    await single_user.add_class(class_name, class_grade, class_credit)

    CHANGE = await display_classes_on_embed(await single_user.get_class_list(), await single_user.get_list_size())
    print(CHANGE)


# general methods

async def show_embed(message, GPA, curr_user):
    test = ['hello', 'this', 'is', 'a', 'test']

    # create Embed
    embed = discord.Embed(
        title='Class List',
        description=f'Current GPA is `{GPA}`' + '\n\n',
        colour=discord.Colour.gold()
    )

    # display empty fields
    embed.add_field(name='Class Names', value='test1\ntest2', inline=True)
    embed.add_field(name='Class Grades', value='*Empty*', inline=True)
    embed.add_field(name='Class Credit', value='*Empty*', inline=True)

    # send to the channel
    await message.channel.send(embed=embed)


# @bot.command()
async def display_classes_on_embed(classes_list: list[UserInfo.NewClassesInfo], list_length):
    NAME_INDEX = 0
    GRADE_INDEX = 1
    CREDIT_INDEX = 2

    final_list = ['', '', '']

    # if list is empty, return "empty" list
    if not classes_list:
        return ['*Empty*', '*Empty*', '*Empty*']

    for each_index in range(list_length):
        final_list[NAME_INDEX] += classes_list.get_course_name() + '\n'
    #
    # for each_index in range(list_length):
    #     final_list[GRADE_INDEX] += classes_list.get_course_grade() + '\n'
    #
    # for each_index in range(list_length):
    #     final_list[CREDIT_INDEX] += classes_list.get_credit_hours() + '\n'

    print(final_list)   # debug
    return final_list


bot.run(TOKEN)
