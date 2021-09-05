import os

from discord.ext import commands
from dotenv import load_dotenv

# constants
ONCE = 1

# opens the '.env' file and stores its content
load_dotenv('venv/.env')
TOKEN = os.getenv('TOKEN')

# set the Bot's prefix to '$'
client = commands.Bot(command_prefix='$')


# user = discord.Member //  not sure what this means


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# TEST COMMAND (DELETE THIS LATER)
@client.command()
async def what(ctx):
    await ctx.channel.send('This command is working')


# TEST COMMAND (DELETE THIS LATER)
@client.command()
async def getInput(ctx):
    # gets message content
    message = ctx.message.content

    # removes the command call from the message String and the extra space
    new_message = message.replace('$getInput', '', 1)
    new_message = new_message[1:len(new_message)]  # inefficient

    # debug
    print(new_message)
    await ctx.channel.send(new_message)


# FIX BELOW **************************************************************


# initiates the GPA calculation process
@client.command()
async def calculate(ctx):
    user_values = parseInputNums(ctx)
    final_GPA = user_values[0] / user_values[1]
    await ctx.channel.send(f'GPA = {final_GPA}')


def parseInputNums(ctx):
    # gets message content
    message = ctx.message.content

    # removes the command call from the message String and the extra space
    new_message = message.replace('$calculate', '', ONCE)
    new_message = new_message[1:len(new_message)]  # inefficient (re-do without string concatenation)

    nums = new_message.split(' ')
    nums = [float(i) for i in nums]

    return nums  # return list of integers

# FIX ABOVE **************************************************************










# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     # testing command
#     if message.content.startswith('$hello'):  # try to improve this line with @Command
#         test = "What I got is: " + str(message.author.id) + "\n" + \
#                "EniGz \"ID\": " + str(message.author.id) + "\n" \
#                                                            "ID from \"mentions\" is: " + str(message.mentions)
#
#         await message.channel.send(test)
#
#     # report function
#     if message.content.startswith('$report'):  # try to improve this line with @Command
#         mentioned_user = message.mentions[0]
#         await mentioned_user.create_dm()
#         await ReportFunction.reportFunction('BeeMovieScript.txt', message, mentioned_user)
#         await message.author.send("DM to " + str(message.mentions[0].display_name) + " worked")


client.run(TOKEN)
