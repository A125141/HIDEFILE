import os
import colorama
from colorama import Fore, Style
from tqdm import tqdm
import time

def get_user_name():
    return os.getlogin()


def show_loading():
    print("Loading...")
    for _ in tqdm(range(100), ncols=80):
        time.sleep(0.02)



def hide_folders():
    print()
    print(Fore.YELLOW + "What do you want to HIDE today?")
    print(Fore.BLUE + "--ENTER THE PATH :" + Style.RESET_ALL)

    folder_paths = input().split()
    print(Fore.GREEN + "-----------------------------------------------------------------")

    for path in folder_paths:
        os.system('attrib +h +a +s ' + '"' + path + '"')
        print(Fore.YELLOW + "Hiding:", path)

    print()
    print(Fore.GREEN + "  hidden successfully!")
    print(Fore.GREEN + "-------------------------------------------------------------------")


def unhide_folders():
    print()
    print(Fore.YELLOW + "What do you want to UNHIDE today?")
    print(Fore.BLUE + "--ENTER THE PATH :" + Style.RESET_ALL)

    folder_paths = input().split()
    print(Fore.MAGENTA + "-----------------------------------------------------------------")

    for path in folder_paths:
        os.system('attrib -h -a -s ' + '"' + path + '"')
        print(Fore.YELLOW + "Unhiding:", path)

    print()
    print(Fore.GREEN + "  unhidden successfully!")
    print(Fore.MAGENTA + "-------------------------------------------------------------------")


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
    print(Fore.LIGHTWHITE_EX + "                                                  by A125141")
    print(Fore.CYAN + "Logged in as:", get_user_name())
    print()

    print(Fore.YELLOW + "V1 2024")

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
            print(Fore.YELLOW + "Contact US for a problem at [a125141contact@gmail.com]")
            print(Fore.MAGENTA + "-------------------------------------------------")

        elif choice == '4':
            print(Fore.WHITE + "Hello, you are using the latest version of the" , Fore.YELLOW + "Hidefile")
            print(Fore.MAGENTA + "the most advanced tool for hiding folders and files, you can hide:")
            print(Fore.GREEN + "------------------------------------------------------------------------------------")

            print(Fore.GREEN + "------------------------------------------------------------------------------------")
            print(Fore.YELLOW + "--Note:" ,Fore.CYAN + "It is recommended that you save the file path and its format in a note")
            print(Fore.CYAN + "because without the path it is impossible to recover the files.")
            print(Fore.LIGHTRED_EX + "A125141")

        elif choice == '0':
         break

        else:
            print(Fore.RED + "Invalid choice. Please select again.")

    print(Fore.LIGHTMAGENTA_EX + "-------------------------------------------------------------------")
    print(Fore.YELLOW + "Thank you for using the HIDEFILE")
    print(Fore.CYAN + "Created by A125141")
    print(Fore.LIGHTMAGENTA_EX + "-------------------------------------------------------------------")
    print(Fore.YELLOW + "HacK tHe WoRld!")
    print()

if __name__ == "__main__":
    main()
    time.sleep(3)
