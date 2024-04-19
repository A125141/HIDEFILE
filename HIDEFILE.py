import os
import colorama
from colorama import Fore, Style
from tqdm import tqdm
import time

# Function to get the user's name
def get_user_name():
    return os.getlogin()

# Function to show loading animation
def show_loading():
    print("Loading...")
    for _ in tqdm(range(100), ncols=80):
        time.sleep(0.02)


# Function to hide folders
def hide_folders():
    print()
    print(Fore.YELLOW + "What do you want to HIDE today?")
    print(Fore.BLUE + "--ENTER THE FOLDERS PATH :" + Style.RESET_ALL)

    folder_paths = input().split()
    print(Fore.GREEN + "-----------------------------------------------------------------")

    for path in folder_paths:
        os.system('attrib +h +a +s ' + '"' + path + '"')
        print(Fore.YELLOW + "Hiding folder:", path)

    print()
    print(Fore.GREEN + "  Folders hidden successfully!")
    print(Fore.GREEN + "-------------------------------------------------------------------")

# Function to unhide folders
def unhide_folders():
    print()
    print(Fore.YELLOW + "What do you want to UNHIDE today?")
    print(Fore.BLUE + "--ENTER THE FOLDERS PATH :" + Style.RESET_ALL)

    folder_paths = input().split()
    print(Fore.MAGENTA + "-----------------------------------------------------------------")

    for path in folder_paths:
        os.system('attrib -h -a -s ' + '"' + path + '"')
        print(Fore.YELLOW + "Unhiding folder:", path)

    print()
    print(Fore.GREEN + "  Folders unhidden successfully!")
    print(Fore.MAGENTA + "-------------------------------------------------------------------")

# Main program
def main():
    colorama.init()
    print()
    show_loading()
    print(Fore.MAGENTA + " __    __ ______ _______  ________ ________ ______ __       ________ ")
    print("|  \\  |  |      |       \\|        |        |      |  \\     |        \\")
    print("| $$  | $$\\$$$$$| $$$$$$$| $$$$$$$| $$$$$$$\\$$$$$| $$     | $$$$$$$$")
    print("| $$__| $$ | $$ | $$  | $| $$__   | $$__     | $$ | $$     | $$__    ")
    print("| $$    $$ | $$ | $$  | $| $$  \\  | $$  \\    | $$ | $$     | $$  \\   ")
    print("| $$$$$$$$ | $$ | $$  | $| $$$$$  | $$$$$    | $$ | $$     | $$$$$   ")
    print("| $$  | $$_| $$_| $$__/ $| $$_____| $$      _| $$_| $$_____| $$_____ ")
    print("| $$  | $|   $$ | $$    $| $$     | $$     |   $$ | $$     | $$     \\")
    print(" \\$$   \\$$\\$$$$$$\\$$$$$$$ \\$$$$$$$$\\$$      \\$$$$$$\\$$$$$$$$\\$$$$$$$$")
    print(Fore.LIGHTWHITE_EX + "                                                  by abdalrahman125141")
    print(Fore.CYAN + "Logged in as:", get_user_name())
    print()

    print(Fore.YELLOW + "Welcome to the HIDEFILE Tool!")

    while True:
        print()

        print(Fore.RED + "[ 1 ]", Fore.YELLOW + "HIDE FOLDERS")
        print(Fore.RED + "[ 2 ]", Fore.YELLOW + "UNHIDE FOLDERS")
        print(Fore.RED + "[ 3 ]", Fore.YELLOW + "Contact US for a problem")
        print(Fore.RED + "[ 4 ]", Fore.YELLOW + "HELP")
        print(Fore.RED + "[ 0 ]", Fore.YELLOW + "EXIT")
        print(Fore.GREEN + "-----------------------------")
        print()

        choice = input(Fore.YELLOW + "WDYW: ")

        if choice == '1':
            hide_folders()

        elif choice == '2':
            unhide_folders()

        elif choice == '3':
            print(Fore.MAGENTA + "-------------------------------------------------")
            print(Fore.YELLOW + "Contact US for a problem at [a6291088@gmail.com]")
            print(Fore.MAGENTA + "-------------------------------------------------")

        elif choice == '4':
            print(Fore.WHITE + "Hello, you are using the latest version of the" , Fore.YELLOW + "Hidefile tool")
            print(Fore.MAGENTA + "the most advanced tool for hiding folders and files, you can hide:")
            print(Fore.GREEN + "------------------------------------------------------------------------------------")
            print(Fore.YELLOW + "files, images , vidoes,folders and more.")
            print(Fore.GREEN + "---you can HIDEFILES on:")
            print(Fore.MAGENTA + "your computer,flash drive or an external hard disk.")
            print(Fore.GREEN + "------------------------------------------------------------------------------------")
            print(Fore.LIGHTRED_EX + "you only have to choose what suits you from the options by writing")
            print(Fore.LIGHTRED_EX + "the number next to the option, then enter the file path or The folder")
            print(Fore.LIGHTRED_EX + "that you want to hide or show.")
            print(Fore.GREEN + "------------------------------------------------------------------------------------")
            print(Fore.YELLOW + "to know the path of your file, all you have to do is:")
            print(Fore.LIGHTBLUE_EX+ "go to the file that you want to hide or show and press it with the right click")
            print(Fore.MAGENTA + "and choose -properties- and you will find the file path next to the location,")
            print(Fore.MAGENTA + "but you must pay attention that you must write the name of the file and its format,")
            print(Fore.LIGHTCYAN_EX + "For example:")
            print(Fore.LIGHTGREEN_EX+ "we have a file called test, which is an MP4 video in the path C:\\Users\\Desktop")
            print(Fore.LIGHTGREEN_EX+ "so you have to modify the path to be as follows: C:\\Users\\ABooD\\Desktop\\test.mp4")
            print(Fore.GREEN + "------------------------------------------------------------------------------------")
            print(Fore.YELLOW + "--Note:" ,Fore.CYAN + "It is recommended that you save the file path and its format in a note")
            print(Fore.CYAN + "because without the path it is impossible to recover the files.")
            print(Fore.LIGHTRED_EX + "Abdalrahman125141")

        elif choice == '0':
         break

        else:
            print(Fore.RED + "Invalid choice. Please select again.")

    print(Fore.LIGHTMAGENTA_EX + "-------------------------------------------------------------------")
    print(Fore.YELLOW + "Thank you for using the HIDEFILE Tool!")
    print(Fore.CYAN + "Created by ABDALRAHMAN125141")
    print(Fore.LIGHTMAGENTA_EX + "-------------------------------------------------------------------")
    print(Fore.YELLOW + "Have a great day!")
    print()

if __name__ == "__main__":
    main()
    time.sleep(3)  # Delay for 3 seconds
