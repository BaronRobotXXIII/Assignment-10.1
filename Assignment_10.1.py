#This week we will create a program that performs file processing activities.  
#Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.  
#Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.  
#The program should then prompt the user for their name, address, and phone number.  
#Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 
#Once the data has been written your program should read the file you just wrote to the file system 
#and display the file contents to the user for validation purposes. 
#Submit a link to your Github repository.

import os

def check_dir(target_dir):
    """Checks the existence of the target directory and offers to create the directory if it does not exist."""
    all_dirs = os.listdir(os.getcwd())
    all_dirs.append(os.getcwd())
    #fix this
    if target_dir in all_dirs:
        change_dir(target_dir)
    else:
        create_dir_val = create_dir(target_dir)
        if create_dir_val:
            return 'continue'

def create_dir(target_dir):
    """Creates a directory if check_dir determines it does not exist"""
    green_light = True
    while green_light == True:
        print("That directory does not exist in the current working directory.")
        user_input = input(f"Would you like to create {target_dir} in the current working directory? y/n \n")
        if user_input.lower() == 'y':
            green_light = False
            os.mkdir(target_dir)
            change_dir(target_dir)
            return None
        elif user_input.lower() == 'n':
            green_light = False
            return "continue"
        else:
            print("That is not a valid response.")

def change_dir(target_dir):
    """Changes the current directory and verifies that the directory exists"""
    if target_dir != os.getcwd():
        all_content = os.listdir(os.getcwd())
        if target_dir in all_content:
            try: 
                os.chdir(target_dir)
            except:
                print("The target_dir might exist as a file")
                pass
    else:
        return None

def check_file(target_file):
    """Checks the existence of the file and alerts the user if a file already exists with that name"""
    green_light = True
    while green_light == True:
        all_content = os.listdir(os.getcwd())
        if target_file in all_content:
            user_input = input(f"That file may already exist, would you like to override the file? y/n \n")
            if user_input.lower() == "y":
                green_light = False
                return None
            elif user_input.lower() == "n":
                green_light = False
                return "continue"
            else:
                print("That is not a valid response.")
        else:
            return None

def gather_input():
    user_name = input(f"What is the user's name?\n")
    user_address = input(f"What is the user's address?\n")
    user_phone_num = input(f"What is the user's phone number?\n")
    user_data = user_name + ',' + user_address + ',' + user_phone_num
    return user_data

while True:
    print("Welcome to Assignment 10.1")
    target_dir = input(f"What directory would you like to save the file in? \nType q to exit \n")
    if target_dir.lower() == "q":
        break
    check_dir_val = check_dir(target_dir)
    if check_dir_val:
        print()
        continue

    target_file = input("What would you like to name the file? \nType q to exit \n")
    target_file = target_file + '.txt'
    if target_file.lower() == 'q.txt':
        break
    check_file_val = check_file(target_file)
    if check_file_val:
        print()
        continue
    
    user_data = gather_input()
    #print(user_data)

    with open(target_file, 'w') as f:
        f.write(user_data)

    with open(target_file) as f:
        contents = f.read()
        print(contents)
