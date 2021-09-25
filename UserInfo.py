
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

        # attributes that will be used as the string representation
        self.__course_name = course_name

        # attributes that will be used as the ACTUAL DATA (MAKE A LIST FOR EACH IN USER() INSTEAD)
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
        # embed-used string attributes
        self.__names_str = str()
        self.__grades_str = str()
        self.__hours_str = str()

        # can only create a User() with current info
        self.__current_info = OldClassesInfo(earned_credits, credits_taken)

        # list will be empty AT FIRST
        self.__new_classes_list = []

        # size of list
        self.__class_list_size = int()

        # Reference to the last embed (for deletion purposes)
        self.__last_message_id = int()

        # last created embed
        self.__last_embed = None

        # Discord user that is the owner of the data
        self.__discord_user = str()


    # getters
    def get_current_info(self):
        return self.__current_info

    def get_classes(self):
        return self.__new_classes_list

    def get_class(self, index: int):
        return self.__new_classes_list[index]

    def get_list_size(self):
        return self.__class_list_size

    def get_last_embed(self):
        return self.__last_embed

    def get_last_message(self):
        return self.__last_message_id

    def get_discord_user(self):
        return self.__discord_user

    def get_name_str(self):
        return self.__names_str

    def get_grades_str(self):
        return self.__grades_str

    def get_hours_str(self):
        return self.__hours_str


    # setters
    def set_user_embed(self, new_embed):
        self.__last_embed = new_embed

    def set_last_message(self, last_id):
        self.__last_message_id = last_id

    def set_discord_user(self, discord_user):
        self.__discord_user = discord_user


    # creates and add a new class to the User() list of new classes
    def add_class(self, course_name, course_grade, course_credit_hours: int):

        # create and add new class to the list
        self.__new_classes_list.append(NewClassesInfo(course_name, course_grade, course_credit_hours))

        # increments list size
        self.__class_list_size += 1


    def concatenate_name_str(self):
        last_element = self.__new_classes_list[self.__class_list_size - 1]
        self.__names_str += last_element.get_course_name() + '\n'

    def concatenate_grades_str(self):
        last_element = self.__new_classes_list[self.__class_list_size - 1]
        self.__grades_str += last_element.get_course_grade() + '\n'

    def concatenate_hours_str(self):
        last_element = self.__new_classes_list[self.__class_list_size - 1]
        self.__hours_str += str(last_element.get_credit_hours()) + '\n'


    # mainly for debugging purposes
    def print_User(self):
        print(f'[{self.__names_str}, {self.__grades_str}, {self.__hours_str}]')













# not too important - FOR NOW
# I NEED A HASH TABLE FOR USERS !!!!!!!!!!! (will deal with first users trying to use "add)
class Database:

    def __init__(self):
        self.__list_of_users = list[User] # CHANGE THIS TO HASH TABLE AFTERWARDS!!!!

