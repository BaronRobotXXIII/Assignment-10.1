#The program should then prompt the user for their name, address, and phone number.  
#Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 
#Once the data has been written your program should read the file you just wrote to the file system 
#and display the file contents to the user for validation purposes. 
#Submit a link to your Github repository.

import os

def check_dir(target_dir):
    """Checks the existence of the target directory and offers to create the directory if it does not exist."""
    all_dirs = os.listdir(os.getcwd())
    if target_dir in all_dirs:
        pass
    else:
        green_light = True
        while green_light == True:
            print("That directory does not exist in the current working directory.")
            user_input = input(f"Would you like to create {target_dir} in the current working directory? y/n \n")
            if user_input.lower() == 'y':
                green_light = False
                os.mkdir(target_dir)
                return None
            elif user_input.lower() == 'n':
                green_light = False
                return "continue"
            else:
                print("That is not a valid response.")


while True:
    print("Welcome to Assignment 10.1")
    target_dir = input("What directory would you like to save the file in? ")
    check_dir_val = check_dir(target_dir)
    if check_dir_val:
        continue

    target_file = input("What would you like to name the file? ")
