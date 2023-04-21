import hashlib
import pandas as pd
import getpass
import pwinput
import os
import time
import welcome
import odbc_connection
import pyfiglet
from termcolor import colored
import sys

class UserAuthentication:
    def __init__(self):
        self.get_user_type()

    def all_users(self):
        conn = odbc_connection.get_db_connection()
        query = 'SELECT ud.*, ua.approval_status FROM user_details ud JOIN user_approval ua ON ud.email = ua.email'
        df = pd.read_sql(query, conn)
        return df

    def get_user_type(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        ascii_art = pyfiglet.figlet_format("Cub Hopper", font="slant")
        colored_ascii_art = colored(ascii_art, color="cyan")
        print(colored_ascii_art)
        user_type = input("Enter 1: Existing User \nEnter 2: New User\n")

        while user_type not in ["1", "2"]:
            print("Invalid input. Please enter 1 or 2.")
            user_type = input("Enter 1: Existing User \nEnter 2: New User\n")

        if user_type == "1":
            self.authenticate_existing_user()
        elif user_type == "2":
            self.create_new_user()
        elif user_type == "3":
            exit


    def authenticate_existing_user(self):

        df = self.all_users()

        email = input("Enter email: ")
        while email not in df['email'].values:
            print("Email does not exit. Click 0 to exit.")
            if email == "0":
                sys.exit()
            email = input("Enter valid email: ")

        approval_status = df.loc[df['email'] == email, 'approval_status'].values[0]

        if approval_status == 'B':
            print("Your email ID is blocked.")
            while True:
                user_input = input("\nPress 1 to return to main menu.\nPress 2 to exit.\n")
                if user_input == "1":
                    self.get_user_type()
                elif user_input == "2":
                    sys.exit()
                else:
                    print("Enter valid Input.")

        password = df.loc[df['email'] == email, 'password'].values[0]
        entered_pass = pwinput.pwinput(prompt='Enter Password: ', mask='*')
        while password != hashlib.sha256(entered_pass.encode()).hexdigest():
            entered_pass = pwinput.pwinput("Password does not match. Press 0 to exit. Enter valid password: ")
            if entered_pass == "0":
                sys.exit()
        print("Login Successfull")
        # Close the database connection
        #self.conn.close()
        print("Redirecting...")
        time.sleep(1)
        # filter the rows with email
        row = df[df['email'] == email].iloc[0]
        welcome.welcome(row)


    def create_new_user(self):
        df = self.all_users()
        print("Hello, please provide the asked information, and we will create an account for you.\n")

        first_name = input("Enter First Name: ")
        while not first_name:
            first_name = input("You didn't enter anything. Please enter your name: ")

        last_name = input("Enter Last Name: ")
        while not last_name:
            last_name = input("You didn't enter anything. Please enter your last name: ")

        phone = input("Enter Phone Number: ")
        while not phone:
            phone = input("You didn't enter anything. Please enter your phone: ")

        address1 = input("Enter Address Line 1: ")
        while not address1:
            address1 = input("You didn't enter anything. Please enter your address1: ")

        address2 = input("Enter Address Line 2: ")

        city = input("Enter City: ")
        while not first_name:
            first_name = input("You didn't enter anything. Please enter your name: ")

        province = input("Enter Province: ")
        while not city:
            city = input("You didn't enter anything. Please enter your city: ")

        postalcode = input("Enter Postal Code: ")
        while not postalcode:
            postalcode = input("You didn't enter anything. Please enter your name: ")

        country = input("Enter Country: ")
        while not country:
            country = input("You didn't enter anything. Please enter your country: ")

        email = input("Enter email: ")
        while not email:
            email = input("You didn't enter anything. Please enter your email: ")
        while email in df['email'].values:
            print("Email already exits. Click 0 to exit.")
            if email == "0":
                exit
            email = input("Enter valid email: ")

        # Hash the password using SHA-256
        entered_pass = pwinput.pwinput(prompt='Enter Password: ', mask='*')
        while not entered_pass:
            entered_pass = input("You didn't enter anything. Please enter your password: ")
        hashed_password = hashlib.sha256(entered_pass.encode()).hexdigest()

        sql_query = '''INSERT INTO user_details (first_name, last_name, phone_number, address_line_1, address_line_2, city, province, postal_code, country, email, password)
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}')'''.format(first_name,
                                                                                                        last_name,
                                                                                                        phone, address1,
                                                                                                        address2, city,
                                                                                                        province,
                                                                                                        postalcode,
                                                                                                        country, email, hashed_password)
        sql_query2 = '''INSERT INTO user_approval (email)
                VALUES ('{0}')'''.format(email)

        conn = odbc_connection.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        cursor.execute(sql_query2)
        conn.commit()

        print("Account Created")
        self.authenticate_existing_user()




