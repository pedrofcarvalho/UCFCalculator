import discord
import UserInfo


# TODO - DELETE THIS LATER (USE A HASH TABLE)
single_user = UserInfo.User(168.750, 45.000)

# TODO
async def help(ctx):
    print("help")
    pass


# initiates the GPA calculation process
async def calculateGPA(ctx, credit_points: float, credits_taken: float):

    # if the user already has an embed, block him from creating another one
    # (CHANGE USER LATER)
    if single_user.get_last_embed() is not None:
        await ctx.channel.send(f'{ctx.author.mention}, you have a GPA session open')
        return

    # (CHANGE USER LATER)
    single_user.set_discord_user(ctx.author)    # CHECK THIS LINE!!!

    # calculates the GPA
    final_GPA = round(credit_points / credits_taken, 2)

    # checks if the GPA is valid. If not, stop and let user know
    if final_GPA < 0.0 or final_GPA > 4.0:
        await ctx.channel.send(f'{ctx.author.mention}, your input is invalid')
        return

    # call empty embed
    await show_embed(ctx, final_GPA, single_user, False, name='*Empty*', grade='*Empty*', hours='*Empty*')  # CHECK THE USER



async def add(ctx, class_name, class_grade, class_credit: int):

    # checks if user started the calculation process (pre-requisite for this command)
    # (CHANGE USER LATER)
    if single_user.get_last_embed() is None:
        await ctx.channel.send(f'{ctx.author.mention}, calculate your GPA first!')
        return

    # delete last embed (CHANGE USER LATER)
    await ctx.channel.delete_messages([discord.Object(id=single_user.get_last_message())])

    # adds a new class to the user's list based on user input
    single_user.add_class(class_name, class_grade, class_credit)    # (CHANGE USER LATER)

    # makes the call to display on embed
    await display_classes_on_embed(ctx, single_user)    # (CHANGE USER LATER)


# TODO - calculate user's GPA and create embed
async def finish(ctx):
    print("finish")
    pass



#general methods
async def show_embed(ctx, gpa, user, ended: bool, name, grade, hours):

    # checks if user already has an embed. If yes, just change the info
    if user.get_last_embed() is not None:
        embed = user.get_last_embed()
        embed.set_field_at(index=0, name='Class Names', value=name, inline=True)
        embed.set_field_at(index=1, name='Class Grades', value=grade, inline=True)
        embed.set_field_at(index=2, name='Class Credit', value=hours, inline=True)

    # creating the embed for the first time
    else:
        final_phrase = 'final' if ended is True else ''

        # create Embed
        new_embed = discord.Embed(
            title='Class List',
            description=f'{ctx.author.mention}{final_phrase} GPA is `{gpa}`' + '\n\n',
            colour=discord.Colour.gold()
        )

        if ended is False:
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


async def display_classes_on_embed(ctx, user):
    # calculate current user's GPA
    gpa = user.get_current_info().get_earned_credits() / user.get_current_info().get_taken_credits()

    # "increments" the string data representation
    user.concatenate_name_str()
    user.concatenate_grades_str()
    user.concatenate_hours_str()

    # display embed
    await show_embed(ctx, gpa, user, False, user.get_name_str(), user.get_grades_str(), user.get_hours_str())
