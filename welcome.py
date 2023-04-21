import pyfiglet
from termcolor import colored
import pandas as pd
import odbc_connection
import datetime
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')
import os


def welcome(user_row):

    conn = odbc_connection.get_db_connection()
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = pyfiglet.figlet_format("Cub Hopper", font="slant")
    colored_ascii_art = colored(ascii_art, color="cyan")
    print(colored_ascii_art)

    print("Hello ", user_row['first_name'],
          ", What would to like to see today?\n")

    postal_code_entered = input("For refined results we request you to enter your postal code. ")

    postal_code_first3 = postal_code_entered[:3]
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')
        user_type = input("\nEnter 1: Clubs near me. \n"
                          "Enter 2: Cheapest clubs near me\n"
                          "Enter 3: Best Rated clubs near me.\n"
                          "Enter 4: Best deals available today.\n"
                          "Enter 5: ClubHopper Recommendations\n"
                          "Enter 6: Enter postal code again\n"
                          "Enter 7: Exit \n")

        if user_type == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored_ascii_art)
            print("Clubs near me:\n")
            query = f"""SELECT club_name, about, 
                    concat(address1,',',address2) as Address,
                    ratings  FROM clubs where postal_code like '{postal_code_first3}%'"""
            print(query)
            df = pd.read_sql(query, conn)
            if len(df) == 0:
                print("No clubs available near you\n")
                input("Press any key to continue")
            else:
                print(tabulate(df, headers='keys', tablefmt="grid", maxcolwidths=[None, 10, 20]))

        elif user_type == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored_ascii_art)
            print("Cheapest clubs near me you are:\n")
            query = "SELECT  top 10 club_name, about, " \
                    "concat(address1,',',address2) as Address, avgcost," \
                    "ratings  FROM clubs order by avgcost"
            df = pd.read_sql(query, conn)
            print(tabulate(df, headers='keys', tablefmt="grid", maxcolwidths=[None, 10, 20]))

        elif user_type == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored_ascii_art)
            print("Best Rated clubs near you:\n")
            query = "SELECT  top 10 club_name, about, " \
                    "concat(address1,',',address2) as Address, avgcost," \
                    "ratings  FROM clubs order by ratings desc"
            df = pd.read_sql(query, conn)
            print(tabulate(df, headers='keys', tablefmt="grid", maxcolwidths=[None, 10, 20]))

        elif user_type == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored_ascii_art)
            print("Best deals available today: ")
            query = "SELECT top 5 club_name, about, " \
                    "concat(address1,',',address2) as Address," \
                    "ratings  FROM clubs"
            df = pd.read_sql(query, conn)
            print(tabulate(df, headers='keys', tablefmt="grid", maxcolwidths=[None, 10, 20]))

        elif user_type == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored_ascii_art)
            print("ClubHopper Recommendations: ")
            query = "SELECT top 5 club_name, about, " \
                    "concat(address1,',',address2) as Address," \
                    "ratings  FROM clubs order by avgcost asc"
            df = pd.read_sql(query, conn)
            print(tabulate(df, headers='keys', tablefmt="grid", maxcolwidths=[None, 10, 20]))
        elif user_type == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored_ascii_art)
            welcome(user_row)
        elif user_type == "7":
            print("Thanks for using Club Hopper. See you soon.")
            exit(0)
            return
        else:
            print(colored_ascii_art)
            print("Invalid user input. Please try again.")

