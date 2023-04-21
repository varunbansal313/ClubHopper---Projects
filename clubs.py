import sys

import odbc_connection
import pandas as pd
import pwinput
import hashlib
import os
import pyfiglet
from termcolor import colored


def all_clubs():
    conn = odbc_connection.get_db_connection()
    query = 'SELECT * FROM ClubOwnerDetails'
    df = pd.read_sql(query, conn)
    return df


def get_club_type():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = pyfiglet.figlet_format("Cub Hopper", font="slant")
    colored_ascii_art = colored(ascii_art, color="cyan")
    print(colored_ascii_art)
    user_type = input("Enter 1: Existing Club. \nEnter 2: Register your Club on Club Hopper\n")

    while user_type not in ["1", "2"]:
        print("Invalid input. Please enter 1 or 2.")
        user_type = input("Enter 1: Existing Club. \nEnter 2: Register your Club on Club Hopper\n")

    if user_type == "1":
        clubLogin()
    elif user_type == "2":
        registerClub()
    elif user_type == "3":
        exit


def clubLogin():
    df = all_clubs()

    email = input("Enter email: ")
    while email not in df['OwnerEmail'].values:
        print("Email does not exit. Click 0 to exit.")
        if email == "0":
            exit
        email = input("Enter valid email: ")

    password = df.loc[df['OwnerEmail'] == email, 'password'].values[0]
    entered_pass = pwinput.pwinput(prompt='Enter Password: ', mask='*')
    while password != hashlib.sha256(entered_pass.encode()).hexdigest():
        entered_pass = pwinput.pwinput("Password does not match. Press 0 to exit. Enter valid password: ")
        if entered_pass == "0":
            sys.exit()
    print("Login Successfull")
    # Close the database connection
    # self.conn.close()
    print("Redirecting...")
    viewMyClub(email)
    # filter the rows with email
    # row = df[df['email'] == email].iloc[0]
    # welcome.welcome(row)


def viewMyClub(email):
    conn = odbc_connection.get_db_connection()

    sql_query = f"SELECT c.[club_id], c.[OwnerEmail], c.[club_name], c.[about], c.[Address1], c.[Address2], \
             c.[postal_code], c.[city], c.[country], c.[Email], c.[Phone], c.[website], c.[avgcost], \
             c.[opening_time], c.[closing_time], c.[Ratings], c.[manager_name], c.[approval_status], \
             co.[ClubOwnerName], co.[ClubName], co.[OwnerPhone] \
             FROM [ClubHopper].[dbo].[clubs] c \
             INNER JOIN ClubOwnerDetails co ON c.OwnerEmail = co.OwnerEmail \
             WHERE c.OwnerEmail = '{email}'"
    df = pd.read_sql(sql_query, conn)
    print("\nBelow are the details of ur club:\n")
    print(f"1. Club ID: {df.at[0, 'club_id']}")
    print(f"2. Owner Email: {df.at[0, 'OwnerEmail']}")
    print(f"3. Club Name: {df.at[0, 'club_name']}")
    print(f"4. About: {df.at[0, 'about']}")
    print(f"5. Address1: {df.at[0, 'Address1']}")
    print(f"6. Address2: {df.at[0, 'Address2']}")
    print(f"7. Postal Code: {df.at[0, 'postal_code']}")
    print(f"8. City: {df.at[0, 'city']}")
    print(f"9. Country: {df.at[0, 'country']}")
    print(f"10. Email: {df.at[0, 'Email']}")
    print(f"11. Phone: {df.at[0, 'Phone']}")
    print(f"12. Website: {df.at[0, 'website']}")
    print(f"13. Avg. Cost: {df.at[0, 'avgcost']}")
    print(f"14. Opening Time: {df.at[0, 'opening_time']}")
    print(f"15. Closing Time: {df.at[0, 'closing_time']}")
    print(f"16. Ratings: {df.at[0, 'Ratings']}")
    print(f"17. Manager Name: {df.at[0, 'manager_name']}")
    print(f"18. Approval Status: {df.at[0, 'approval_status']}")
    print(f"19. Club Owner Name: {df.at[0, 'ClubOwnerName']}")
    print(f"20. Club Name: {df.at[0, 'ClubName']}")
    print(f"21. Owner Phone: {df.at[0, 'OwnerPhone']}")



    # while club_input not in ["1", "2", "3"]:
    #     print("Invalid input. Please enter 1 or 2.\n")
    #     club_input = input("Press 1: De-list my club.\n"
    #                        "Press 2: Re-activate my club.\n"
    #                        "Press 3: View ur club details.\n"
    #                        "Press 4: Exit.\n")

    while True:
        club_input = input("\nPress 1: De-list my club.\n"
                           "Press 2: Re-list my club.\n"
                           "Press 3: View ur club details.\n"
                           "Press 4: Exit.\n")

        if club_input == "1":
            sql_query = f"UPDATE [ClubHopper].[dbo].[clubs] SET approval_status = 'D' WHERE OwnerEmail = '{email}'"
            cursor = conn.cursor()
            cursor.execute(sql_query)
            conn.commit()
            input("Club Successfully De-listed. Press any key to continue.")

        elif club_input == "2":
            sql_query = f"SELECT [approval_status] FROM [ClubHopper].[dbo].[clubs]  WHERE OwnerEmail = '{email}'"
            df = pd.read_sql(sql_query, conn)
            approval_status = df.at[0, 'approval_status']

            if approval_status == 'Y':
                print("Your club is approved and already Activated.")
                input("Press any key to continue.")

            elif approval_status == 'N':
                print("Your club is pending Admin Approval.")
                input("Press any key to continue.")
            else:
                sql_query = f"UPDATE [ClubHopper].[dbo].[clubs] SET approval_status = 'N' WHERE OwnerEmail = '{email}'"
                cursor = conn.cursor()
                cursor.execute(sql_query)
                conn.commit()
                print("Account Activated.")

        elif club_input == "3":
            viewMyClub(email)

        elif club_input == "4":
            sys.exit()
        else:
            print("Invalid Input. Enter 1, 2, 3 or 4.")




def registerClub():
    df = all_clubs()
    print("Hello, please provide the asked information, and we will create an account for you.\n")

    OwnerEmail = input("Enter club owner email: ")
    while not OwnerEmail:
        OwnerEmail = input("You didn't enter anything. Please enter your email: ")
    while OwnerEmail.lower() in map(str.lower, df['OwnerEmail'].values):
        print("Email already exits. Click 0 to exit.")
        if OwnerEmail == "0":
            exit
        OwnerEmail = input("Enter valid email: ")

    ClubOwnerName = input("Enter club Owner name: ")
    while not ClubOwnerName:
        ClubOwnerName = input("You didn't enter anything. Please enter your name: ")

    ClubName = input("Enter Club Name: ")
    while not ClubName:
        ClubName = input("You didn't enter anything. Please enter your club name: ")

    OwnerPhone = input("Enter Phone Number: ")
    while not OwnerPhone:
        OwnerPhone = input("You didn't enter anything. Please enter your phone: ")

    # Hash the password using SHA-256
    entered_pass = pwinput.pwinput(prompt='Enter Password: ', mask='*')
    while not entered_pass:
        entered_pass = input("You didn't enter anything. Please enter your password: ")
    hashed_password = hashlib.sha256(entered_pass.encode()).hexdigest()

    sql_query = '''INSERT INTO ClubOwnerDetails (OwnerEmail, ClubOwnerName, ClubName, OwnerPhone, password)
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')'''.format(OwnerEmail,
                                                                 ClubOwnerName, ClubName,
                                                                 OwnerPhone,
                                                                 hashed_password)
    print("\nCongrats, Account Created. ")
    print("\nPlease remember ur credential. \n User name: ", OwnerEmail,
          "\n Password: ", entered_pass, "\n")

    conn = odbc_connection.get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    conn.commit()

    input("press one to continue registration")

    os.system('cls' if os.name == 'nt' else 'clear')

    about = input("Enter about: ")
    while not about:
        about = input("You didn't enter anything. Please enter about: ")

    address1 = input("Enter Address 1: ")
    while not address1:
        address1 = input("You didn't enter anything. Please enter Address 1: ")

    address2 = input("Enter Address 2: ")

    postal_code = input("Enter Postal Code: ")
    while not postal_code:
        postal_code = input("You didn't enter anything. Please enter Postal Code: ")

    city = input("Enter City: ")
    while not city:
        city = input("You didn't enter anything. Please enter City: ")

    country = input("Enter Country: ")
    while not country:
        country = input("You didn't enter anything. Please enter Country: ")

    email = input("Enter Email: ")
    while not email:
        email = input("You didn't enter anything. Please enter Email: ")

    phone = input("Enter Phone: ")
    while not phone:
        phone = input("You didn't enter anything. Please enter Phone: ")

    website = input("Enter Website: ")
    while not website:
        website = input("You didn't enter anything. Please enter Website: ")

    avgcost = input("Enter Average Cost: ")
    while not avgcost:
        avgcost = input("You didn't enter anything. Please enter Average Cost: ")
    avgcost = float(avgcost)

    opening_time = input("Enter Opening Time (HH:MM:SS format): ")
    while not opening_time:
        opening_time = input("You didn't enter anything. Please enter Opening Time (HH:MM:SS format): ")

    closing_time = input("Enter Closing Time (HH:MM:SS format): ")
    while not closing_time:
        closing_time = input("You didn't enter anything. Please enter Closing Time (HH:MM:SS format): ")

    ratings = input("Enter Ratings: ")
    while not ratings:
        ratings = input("You didn't enter anything. Please enter Ratings: ")

    manager_name = input("Enter Manager Name: ")
    while not manager_name:
        manager_name = input("You didn't enter anything. Please enter Manager Name: ")

    sql_query2 = '''INSERT INTO clubs (OwnerEmail, club_name, about, Address1, 
    Address2, postal_code, city, country, email, Phone, website, 
    avgcost, opening_time, closing_time, Ratings, manager_name) 
    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', 
    '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}')'''.format(
        OwnerEmail, ClubName, about, address1, address2, postal_code, city, country, email, phone, website, avgcost,
        opening_time, closing_time, ratings, manager_name)

    conn = odbc_connection.get_db_connection()
    cursor = conn.cursor()
    cursor.execute(sql_query2)
    conn.commit()

    print("Successfully added the club to our system."
          "\nWait for admin to approve the request.")
