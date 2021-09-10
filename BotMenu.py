import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# constants
ONCE = 1
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


# FIX BELOW **************************************************************


# initiates the GPA calculation process
@bot.command(name="calculateGPA", aliases=["GPA", "calculate"])
async def calculateGPA(ctx):
    # parse user input
    user_values = parseInputNums(ctx)

    # calculates the GPA
    final_GPA = user_values[0] / user_values[1]

    # checks if the GPA is valid
    if final_GPA < 0.0 or final_GPA > 4.0:
        await ctx.channel.send('Invalid Input')
        return

    await show_embed(ctx, str(round(final_GPA, 2)))
    return


def parseInputNums(ctx):
    # gets message content
    message = ctx.message.content

    # removes the command call from the message String and the extra space
    new_message = message.replace('$calculateGPA', '', ONCE)
    new_message = new_message[1:len(new_message)]  # inefficient (re-do without string concatenation)

    nums = new_message.split(' ')
    nums = [float(i) for i in nums]

    return nums  # return list of integers

# FIX ABOVE **************************************************************


async def show_embed(message, GPA):

    # create Embed
    embed = discord.Embed(
        title='Class List',
        description="Current GPA: " + '**`' + GPA + '`**' + "\n" +
                    "To add classes, use `$add`",
        colour=discord.Colour.gold()
    )

    # display empty fields
    embed.add_field(name='Class Names', value='*Empty*', inline=True)
    embed.add_field(name='Class Credit', value='*Empty*', inline=True)

    # send to the channel
    await message.channel.send(embed=embed)


@bot.command(name="delete")
async def clear(ctx):
    message = await ctx.channel.fetch_message()
    await message.delete()


@bot.command(name="add", aliases=["ass"])
async def add(ctx):
    await ctx.channel.send("mama minha :wink:")


bot.run(TOKEN)