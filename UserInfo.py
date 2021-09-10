
# there should have only one object for this class
class OldClassesInfo:

    # constructor - all attributes are PRIVATE
    def __init__(self, earned_credits, credits_taken):
        self.__earned_credits = earned_credits
        self.__taken_credits = credits_taken

    # getters
    def get_earned_credits(self):
        return self.__earned_credits

    def get_taken_credits(self):
        return self.__taken_credits

    # setters
    def set_earned_credits(self, new_value):
        self.__earned_credits = new_value

    def set_taken_credits(self, new_value):
        self.__taken_credits = new_value

    # test (debug)
    def displayTest(self):
        print(f'earned credits: {self.get_earned_credits()}')
        print(f'taken credits: {self.get_taken_credits()}')


# there will have a list of this class
class NewClassesInfo:

    # constructor - all attributes are PRIVATE
    def __init__(self, course_name, course_grade, course_credit_hours):
        self.__course_name = course_name
        self.__course_grade = course_grade
        self.__course_credit_hours = course_credit_hours

    def __str__(self):
        return f"NewClassesInfo @{id(self)}(course_name={self.get_course_name()}, " \
               f"course_grade={self.get_course_grade()}, " \
               f"credit_hours={self.get_credit_hours()})"

    def __repr__(self):
        return f"NewClassesInfo @{id(self)}(course_name={self.get_course_name()}, " \
               f"course_grade={self.get_course_grade()}, " \
               f"credit_hours={self.get_credit_hours()})"

    # getters
    def get_course_name(self):
        return self.__course_name

    def get_course_grade(self):
        return self.__course_grade

    def get_credit_hours(self):
        return self.__course_credit_hours

    # setters
    def set_course_name(self, course_name):
        self.__course_name = course_name

    def set_course_grade(self, course_grade):
        self.__course_grade = course_grade

    def set_credit_hours(self, course_credit_hours):
        self.__course_credit_hours = course_credit_hours


# wrapper class (will contain all info from a user)
class User:

    # constructor - all attributes are PRIVATE
    def __init__(self, earned_credits, credits_taken):

        # can only create a User() with current info
        self.__current_info = OldClassesInfo(earned_credits, credits_taken)

        # List will be empty AT FIRST
        self.__new_classes_list = []

        # Reference to the last embed (for deletion purposes)
        self.__last_embed_id = int()

        # Discord user that is the owner of the data
        self.__discord_user = str()

    # getters
    def get_current_info(self):
        return self.__current_info

    def get_class_list(self):
        return self.__new_classes_list

    def get_last_embed(self):
        return self.__last_embed_id

    def get_discord_user(self):
        return self.__discord_user

    # setters
    def set_user_embed(self, new_embed_id):
        self.__last_embed_id = new_embed_id

    def set_discord_user(self, discord_user):
        self.__discord_user = discord_user

    # creates and add a new class to the User() list of new classes
    def add_to_class_to_List(self, course_name, course_grade, course_credit_hours):

        # create new class object
        new_element = NewClassesInfo(course_name, course_grade, course_credit_hours)

        # adds new class to the List
        self.__new_classes_list.append(new_element)

    # mainly for debugging purposes
    def print_User(self):
        print(f'current_info: {self.get_current_info()}')
        print(f'class_list: {self.get_class_list()}')
        print(f'last_embed: {self.get_last_embed()}')
        print(f'discord_user: {self.get_discord_user()}')













# not too important - FOR NOW
class Database:

    def __init__(self):
        self.__list_of_users = User()
