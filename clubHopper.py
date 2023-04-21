import pandas as pd
import user
import clubs
import admin
import warnings
import pyfiglet
from termcolor import colored
warnings.filterwarnings('ignore')

class UserType:

    def main_screen(self):

        ascii_art = pyfiglet.figlet_format("Cub Hopper", font="slant")
        colored_ascii_art = colored(ascii_art, color="cyan")
        print(colored_ascii_art)

        user_type = input("Enter 1: User \nEnter 2: Club Owner\nEnter 3: Admin\n")

        while user_type not in ["1", "2", "3"]:
            print("Invalid input. Please enter 1, 2, or 3.")
            user_type = input("Enter 1: User \nEnter 2: Club Owner\nEnter 3: Admin\n")

        # At this point, user_type is guaranteed to be either "1", "2", or "3"
        if user_type == "1":
            # Create an instance of the class
            user.UserAuthentication()

        elif user_type == "2":
            clubs.get_club_type()
        else:
            admin.adminLogin()


obj = UserType()
obj.main_screen()




