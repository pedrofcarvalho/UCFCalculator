import discord
import UserInfo

# DICTIONARY (Hash Table) of users (key = discord "mention", value = user obj)
user_dict = dict()

# CONSTANT dictionary (todo - look up how make it unchangeable)
CONVERSION_DICTIONARY = dict(A=4, B=3, C=2, D=1, F=0)


# TODO
async def help_command(ctx):
    print("help")


# initiates the GPA calculation process
async def calculateGPA(ctx, credit_points: float, credits_taken: float):

    # if the user already has an embed, block him from creating another one
    # (CHANGE USER LATER)
    if ctx.author.id in user_dict:
        await ctx.channel.send(
            f'{ctx.author.mention}, you already have a GPA session open. Use `$help` for more commands.')
        return

    # creates new User
    new_user = UserInfo.User(credit_points, credits_taken)

    # calculates the GPA
    initial_GPA = round(credit_points / credits_taken, 2)

    # checks if the GPA is valid. If not, stop and let user know
    if initial_GPA < 0.0 or initial_GPA > 4.0:
        await ctx.channel.send(f'{ctx.author.mention}, your input is invalid')
        return

    # create empty embed
    await show_embed(ctx, initial_GPA, new_user, False, name='*Empty*', grade='*Empty*', hours='*Empty*')

    # add new user to Hash Table
    user_dict[ctx.author.id] = new_user


# adds user given class to current user list
async def add(ctx, class_name, class_grade, class_credit: int):

    # if author IS NOT in the dictionary, tell user to calculate GPA
    if ctx.author.id not in user_dict:
        await ctx.channel.send(f'{ctx.author.mention}, calculate your GPA first!')
        return

    # get the current user
    curr_user = user_dict[ctx.author.id]

    # adds a new class to the user's list based on user input
    curr_user.add_class(class_name, class_grade, class_credit)

    # makes the call to display on embed
    await display_classes_on_embed(ctx, curr_user)


async def finish_info(ctx):
    # get the user that called the function
    curr_user = user_dict[ctx.author.id]

    # add each class info to user's current info
    for eachClass in curr_user.get_classes():
        # calculate each added class info
        curr_user.add_earned_credits(CONVERSION_DICTIONARY[eachClass.get_course_grade()] * eachClass.get_credit_hours())
        curr_user.add_taken_credits(eachClass.get_credit_hours())

    # calculates final user GPA
    final_GPA = round(curr_user.get_earned_credits() /
                      curr_user.get_taken_credits(), 2)

    # display final embed
    await show_embed(ctx, final_GPA, curr_user, True,
                     curr_user.get_name_str(), curr_user.get_grades_str(), curr_user.get_hours_str())

    # delete user from the hash table
    del user_dict[ctx.author.id]


# TODO - DELETE THIS LATER
async def test(ctx):
    pass


# general methods - BELOW

# shows embed with user info
async def show_embed(ctx, gpa, user, ended, name, grade, hours):
    # for the final call, create the final embed and make proper user adjustments
    if ended is True:
        final_embed = discord.Embed(
            title='Final GPA',
            description=f'{ctx.author.mention}, your final GPA is `{gpa}`',
            colour=discord.Colour.gold())

        # reassign user embed
        user.set_user_embed(final_embed)

        # delete last embed
        await ctx.channel.delete_messages([discord.Object(id=user.get_last_message())])


    # checks if user already has an embed. If yes, just change the info
    elif user.get_last_embed() is not None:
        curr_embed = user.get_last_embed()
        curr_embed.set_field_at(index=0, name='Class Names', value=name, inline=True)
        curr_embed.set_field_at(index=1, name='Class Grades', value=grade, inline=True)
        curr_embed.set_field_at(index=2, name='Class Credit', value=hours, inline=True)

        # delete last embed
        await ctx.channel.delete_messages([discord.Object(id=user.get_last_message())])

    # creating the embed for the first time
    else:
        # create Embed
        new_embed = discord.Embed(
            title='Class List',
            description=f'{ctx.author.mention} GPA is `{gpa}`' + '\n\n',
            colour=discord.Colour.gold()
        )

        # display empty fields
        new_embed.add_field(name='Class Names', value=name, inline=True)
        new_embed.add_field(name='Class Grades', value=grade, inline=True)
        new_embed.add_field(name='Class Credit', value=hours, inline=True)

        # set the new embed to the newly create one
        user.set_user_embed(new_embed)

    # send embed to the channel
    await ctx.channel.send(embed=user.get_last_embed())

    # set the last message to user info
    user.set_last_message(ctx.channel.last_message_id)


# called to display class as an embed
async def display_classes_on_embed(ctx, user):
    # calculate current user's GPA
    gpa = user.get_earned_credits() / user.get_taken_credits()

    # "increments" the string data representation
    user.concatenate_name_str()
    user.concatenate_grades_str()
    user.concatenate_hours_str()

    # display embed
    await show_embed(ctx, gpa, user, False, user.get_name_str(), user.get_grades_str(), user.get_hours_str())
