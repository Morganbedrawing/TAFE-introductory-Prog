#THOMAS MORGAN 
#880629289 student number
# Event 2 Part 3 - Basic Login System MAY 2025

# Functions
def DisplayMenu(MenuTitle, MenuPrompt, MenuOptionList):
    # Function to display a menu
    print("\n\n" + MenuTitle + "\n")
    print(MenuPrompt, "\n")
    count = 1
    for Option in MenuOptionList:
        print("   ", count, Option)
        count += 1
    print()

from inputimeout import inputimeout, TimeoutOccurred  

def GetSelection():
    # Function to get a selection from the user
        Selection = inputimeout(prompt="Please select from the above numbered options: ")
        return int(Selection)


def ProcessSelectionMain(Selection):
    # Process the selection from the main menu
    if Selection == 1:
        Result = RegisterUser()
    elif Selection == 2:
        Result = LoginUser()
    elif Selection == 3:
        Result = DisplayUsers()
    elif Selection == 4:
        # This is the quit 
        Result = 0
    else:
        Result = ProcessUnknownOption(Selection)
    return Result

#register code below

#Count users p4 edit component below
def RegisterUser():
    # no non-blank usernames check
    while True:
        try:
            username = inputimeout(prompt="Enter a new username: ", timeout=30)
        except TimeoutOccurred:
            print("\nTimeout! Please try again and type a little faster.")
            return 1
        if username.strip() == "":
            print("Username cannot be blank. Please enter a username.")
        else:
            break

    # Check if username already exists
    with open('accountsList.txt', 'r') as f:
        accounts = f.readlines()
        for account in accounts:
            stored_username, _ = account.strip().split(',')
            if stored_username == username:
                print("Username already exists. Please choose a different username.")
                return 1

    # no non-blank passwords check
    while True:
        try:
            password = inputimeout(prompt="Enter a new password: ", timeout=30)
        except TimeoutOccurred:
            print("\nTimeout! Please try again and type a little faster.")
            return 1
        if password.strip() == "":
            print("Password cannot be blank. Please enter a password.")
        else:
            break

    if len(password) < 10:
        print("Password must be at least 10 characters long.")
    else:
        with open('accountsList.txt', 'a') as f:
            f.write(f"{username},{password}\n")
        print('User registered successfully.')

    return 1
def LoginUser():
    global is_logged_in
    try:
        username = inputimeout(prompt="Enter your username: ", timeout=25)
    except TimeoutOccurred:
        print("\nTimeout! Please try again and type a little faster.")
        return 1
    try:
        password = inputimeout(prompt="Enter your password: ", timeout=30)
    except TimeoutOccurred:
        print("\nTimeout! Please try again and type a little faster.")
        return 1
    with open('accountsList.txt', 'r') as f:
        accounts = f.readlines()
    for account in accounts:
        stored_username, stored_password = account.strip().split(',')
        if stored_username == username and stored_password == password:
            print("Login successful.")
            is_logged_in = True
            return 1
    print("Invalid username or password.")
    return 1

def DisplayUsers():
    # Display users component
    with open('accountsList.txt', 'r') as f:
        accounts = f.readlines()
    print("List of usernames:")
    index = 1
    for account in accounts:
        username = account.strip().split(',')[0]
        print(f"{index}. {username}")
        index += 1

    # Print total number of users
    total_users = len(accounts)
    print(f"\nTotal number of registered users: {total_users}")

    return 1


def ProcessUnknownOption(Selection):
    # Placeholder for eventual processing of incorrect options
    print("Invalid Option Selected", Selection)
    return Selection

# Initialise Local Variables
is_logged_in = False  # Tracks if a user is logged in
# Main Menu Definition
MainMenuTitle = "Main Menu"
MainMenuPrompt = "Choose one of the following options"
MainMenu = ["Register User", "Login User", "Display Users", "Quit"]

# Beginning of the main program
print("Welcome")

# Set Option initially to enter the loop below
Option = 0
while Option != 4:
    DisplayMenu(MainMenuTitle, MainMenuPrompt, MainMenu)
    Option = GetSelection()
    ProcessSelectionMain(Option)

import time  # 2 second delay requirement before exiting the program.
time.sleep(2)
print("Program ended by selecting Quit Option")
# End of program

# This code was assisted by GitHub Copilot, an AI programming assistant.
# Model: GPT-4.1 (as of June 2025)
# Provider: Microsoft GitHub Copilot
# Copilot can help with code suggestions, explanations, and error fixes.