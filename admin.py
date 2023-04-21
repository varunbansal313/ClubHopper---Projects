import odbc_connection
import pandas as pd
import pwinput
import sys
from tabulate import tabulate
import os
from datetime import datetime

def all_users():
    conn = odbc_connection.get_db_connection()
    query = 'SELECT * FROM admin'
    df = pd.read_sql(query, conn)
    return df

def createDir():
    # Get current working directory
    current_directory = os.getcwd()

    # Define the new directory name
    new_directory = "MyRecords"

    # Join the current directory with the new directory name
    new_directory_path = os.path.join(current_directory, new_directory)

    # Check if the directory already exists
    if not os.path.exists(new_directory_path):
        # Create the directory if it doesn't exist
        os.mkdir(new_directory_path)
        return new_directory_path
    else:
        return new_directory_path


def adminLogin():
    df = all_users()
    email = input("Enter email: ")
    while email not in df['email'].values:
        print("Email does not exit. Click 0 to exit.")
        if email == "0":
            sys.exit()
        email = input("Enter valid email: ")

    password = df.loc[df['email'] == email, 'password'].values[0]
    entered_pass = pwinput.pwinput(prompt='Enter Password: ', mask='*')
    while password != entered_pass:
        entered_pass = pwinput.pwinput("Password does not match. Enter valid password: . Enter 0 to exit.")
        if entered_pass == "0":
            sys.exit()

    adminTasks()


def adminTasks():
    conn = odbc_connection.get_db_connection()

    admin_input = input("\nPress 1: Download list of all the clubs.\n"
                        "Press 2: Approve new clubs.\n"
                        "Press 3: Block any club.\n"
                        "Press 4: Download list of all the users. \n"
                        "Press 5: Exit.\n")

    while admin_input not in ["1", "2", "3", "4", "5"]:
        print("\nInvalid input. Please enter 1, 2, 3, 4 or 5.")
        admin_input = input("Press 1: Download list of all the clubs.\n"
                            "Press 2: Approve new clubs.\n"
                            "Press 3: Block any club.\n"
                            "Press 4: Download list of all the users. \n"
                            "Press 5: Exit \n")

    if admin_input == "1":
        query = 'SELECT * FROM clubs'
        df = pd.read_sql(query, conn)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        directory_path = createDir()
        file_name = os.path.join(directory_path, f'AllClubs_{timestamp}.xlsx')
        df.to_excel(file_name, index=False)
        print(f"\nFile saved to file '{file_name}' successfully!\n\n")
        a = input("Enter 1 to go to main menu. \nEnter 2 to exit.\n")
        if a == "1":
            adminTasks()
        else:
            sys.exit()

    elif admin_input == "2":
        query = "SELECT club_id,club_name, CONCAT(Address1,', ', Address2) as Address, " \
                "postal_code, city, Email, website, Ratings FROM clubs where approval_status = 'N'"
        df = pd.read_sql(query, conn)
        if len(df) == 0:
            print("No approvals pending.")
            a = input("Enter 1 to go to main menu. \nEnter 2 to exit.\n")
            if a == "1":
                adminTasks()
            else:
                sys.exit()

        print(tabulate(df, headers='keys', tablefmt="grid"))

        clubID = input("\nEnter the club ID to approve. ")
        while not clubID.isdigit():
            clubID = input("Enter digit only. ")
        clubID = int(clubID)

        while clubID not in df["club_id"].values:
            clubID = input("\nEnter Club ID for the list above. ")

        clubID = str(clubID)
        query_update = "UPDATE CLUBS SET approval_status = 'Y' WHERE club_id = '" + clubID + "'"
        cursor = conn.cursor()
        cursor.execute(query_update)
        conn.commit()

        print("\nClub Approved.\n")

        a = input("Enter 1 to go to main menu. \nEnter 2 to exit.\n")
        if a == "1":
            adminTasks()
        else:
            sys.exit()

    elif admin_input == "3":
        query = "SELECT club_id,club_name, CONCAT(Address1,', ', Address2) as Address, " \
                "postal_code, city, Email, website, Ratings FROM clubs where approval_status = 'Y'"
        df = pd.read_sql(query, conn)

        print(tabulate(df, headers='keys', tablefmt="grid"))

        clubID = input("Enter the club ID to block. ")
        while not clubID.isdigit():
            clubID = input("Enter digit only. ")
        clubID = int(clubID)

        while clubID not in df["club_id"].values:
            clubID = input("Enter Club ID for the list above. ")

        clubID = str(clubID)
        query_update = "UPDATE CLUBS SET approval_status = 'B' WHERE club_id = '" + clubID + "'"
        cursor = conn.cursor()
        cursor.execute(query_update)
        conn.commit()

        print("\nClub Blocked.\n")

        a = input("Enter 1 to go to main menu. \nEnter 2 to exit.\n")
        if a == "1":
            adminTasks()
        else:
            sys.exit()
    elif admin_input == "4":
        query = 'SELECT * FROM users'
        df = pd.read_sql(query, conn)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
        directory_path = createDir()
        file_name = os.path.join(directory_path, f'AllUsers_{timestamp}.xlsx')
        df.to_excel(file_name, index=False)
        print(f"\nFile saved to file '{file_name}' successfully!\n\n")

        a = input("Enter 1 to go to main menu. \nEnter 2 to exit.\n")
        if a == "1":
            adminTasks()
        else:
            sys.exit()

    else:
        sys.exit()
