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
    if single_user.get_last_embed() is not None:
        await ctx.channel.send(f'{ctx.author.mention}, you have a GPA session open')
        return

    single_user.set_discord_user(ctx.author)

    # calculates the GPA
    final_GPA = round(credit_points / credits_taken, 2)

    # checks if the GPA is valid
    if final_GPA < 0.0 or final_GPA > 4.0:
        await ctx.channel.send('Invalid Input')
        return

    # call empty embed
    await show_embed(ctx, final_GPA, single_user, name='*Empty*', grade='*Empty*', hours='*Empty*')


@bot.command(name="delete")
async def clear(ctx):
    message = await ctx.channel.fetch_message()
    await message.delete()


@bot.command(name="add", aliases=["ass"])
async def add(ctx, class_name, class_grade, class_credit: int):

    if single_user.get_last_embed() is None:
        await ctx.channel.send(f'{ctx.author.mention}, calculate your GPA first!')
        return

    # delete last embed (CHANGE USER LATER)
    await ctx.channel.delete_messages([discord.Object(id=single_user.get_last_message())])

    # adds a new class to the user's list based on user input
    single_user.add_class(class_name, class_grade, class_credit)

    # makes the call to display on embed
    await display_classes_on_embed(ctx, single_user)


# general methods
async def show_embed(message, gpa, user, name, grade, hours):

    if user.get_last_embed() is not None:
        embed = user.get_last_embed()
        embed.set_field_at(index=0, name='Class Names', value=name, inline=True)
        embed.set_field_at(index=1, name='Class Grades', value=grade, inline=True)
        embed.set_field_at(index=2, name='Class Credit', value=hours, inline=True)

    # creating the embed for the first time
    else:
        # create Embed
        new_embed = discord.Embed(
            title='Class List',
            description=f'{message.author.mention} GPA is `{gpa}`' + '\n\n',
            colour=discord.Colour.gold()
        )

        # display empty fields
        new_embed.add_field(name='Class Names', value=name, inline=True)
        new_embed.add_field(name='Class Grades', value=grade, inline=True)
        new_embed.add_field(name='Class Credit', value=hours, inline=True)

        # set the new embed to the newly create one (CHANGE THE USER)
        user.set_user_embed(new_embed)

    # send to the channel
    await message.channel.send(embed=user.get_last_embed())  # CHANGE THE USER

    # set the last message to user info
    user.set_last_message(message.channel.last_message_id)   # CHANGE THE USER


async def display_classes_on_embed(ctx, user: UserInfo.User):
    # calculate current user's GPA
    gpa = user.get_current_info().get_earned_credits() / user.get_current_info().get_taken_credits()

    # "increments" the string data representation
    user.concatenate_name_str()
    user.concatenate_grades_str()
    user.concatenate_hours_str()

    # display embed
    await show_embed(ctx, gpa, user, user.get_name_str(), user.get_grades_str(), user.get_hours_str())


bot.run(TOKEN)
