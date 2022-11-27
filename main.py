import os, random, hashlib, string, secrets
from colorama import Fore, Back, Style, init

init()

os.system("echo off")
os.system("cls")

Songoda = (Fore.BLUE +
"\n\n                           ░██████╗░█████╗░███╗░░██╗░██████╗░░█████╗░██████╗░░█████╗░\n"
    "                           ██╔════╝██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗\n"
    "                           ╚█████╗░██║░░██║██╔██╗██║██║░░██╗░██║░░██║██║░░██║███████║\n"                  
    "                           ░╚═══██╗██║░░██║██║╚████║██║░░╚██╗██║░░██║██║░░██║██╔══██║\n"                   
    "                           ██████╔╝╚█████╔╝██║░╚███║╚██████╔╝╚█████╔╝██████╔╝██║░░██║\n"                   
    "                           ╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝\n")

print(Songoda)

print(Fore.CYAN +"\n\n","Welcome to Songoda's Multitools!".center(110, " "),"\n\n")

def PasswordSystem():
    print("\n\n", "[1] Password Generator  [2] Password Vault [3] Manage Account  [0] Return to main menu".center(110, " "))
    print("\n")
    while True:
        choice = input("        >> ").strip()
        if choice == "0" or choice == "return":
            print("\n\n", "Back to main menu".center(110, " "), "\n")
            print("[1] Project Setup  [2] Password System  [3] Info  [4] Credits [5] Clear [0] Exit the program".center(110, " "))
            print("\n")
            return
        elif choice == "1":
            print("\n", "Password Generator:".center(110, " "))
            pwdlen = int(input("Please enter length of password: "))
            print("Here is your generated password".center(110, " "))
            print(GeneratePassword(pwdlen).center(110, " "), "\n")
        elif choice == "2":
            PassVault()
        elif choice == "3":
            pass
        else:
            print("Invalid option. Please try again.".center(110, " "))

def PassVault():
    pass

def GeneratePassword(length:int):
    abc = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += secrets.choice(abc)

    return password

def Info():
    print("\n","Songoda's Multitools:".center(110, " "))
    print("I created this program for my personal use, and to learn more about programming.".center(110, " "))
    print("But most importantly, to impress my crush 😉".center(110, " "))
    print("And Songoda isn't a company or whatever it's just in my head, my actual name is GuestTox.".center(110, " "))
    print("\n","---- PERMISSIONS: ----".center(110, " "))
    print("You can do whatever you want with this, you can reupload it as your own, give it to your friends,".center(110, " "),)
    print("read the source code, or even break the hell out of it.".center(110, " "))
    print("The only thing you can't do is sell it, I'd be more than happy to take down a paid version of my work.".center(110, " "), "\n")

def Credits():
    print("\n","Made by GuestTox".center(110, " "))
    print("\n","---- CONTACT: ----".center(110, " "))
    print("Discord: GuestTox#7644".center(110, " "))
    print("Github: @guesttox".center(110, " "))
    print("Twitter: @guesttox".center(110, " "))
    print("YouTube (somehow): @guesttox".center(110, " "), "\n")

def Clear():
    os.system("cls")
    print(Songoda, Fore.CYAN +"\n\n\n")
    main()

def ProjectSetup():
    print("\n       - Project Setup:")
    projectext = input("          Please enter main file extension: ")
    projectname = input("          Please enter the name of your project: ")
    projectpath = input("          Please enter your project path: ")
    if projectpath == "app":
        pass
    print(f"\n               Project Name: {projectname}\n               Project Path: {projectpath}\n")
    while True:
        yesno = input("               Are you sure to make this project? ")
        if yesno == "yes" or yesno == "y":
            break
        elif yesno == "no" or yesno == "n":
            print()
            return
        else:
            print("\n               Invalid answer. Please use (yes|no).\n")
    try:
        os.mkdir(path=f"{projectpath}\\{projectname}")
        print(f"          Successfully created directory: {projectpath}\\{projectname}\n")
    except OSError:
        print("          Directory already exists.")
    with open(f"{projectpath}\\{projectname}\\main.{projectext}", "w") as file:
        if projectext == "py":
            file.write("# Generated with Songoda's Multitools")
        else:
            file.write("// Generated with Songoda's Multitools")
        print(f"          Successfully created project.\n          Path to project: {projectpath}\\{projectname}\n")
        
def main():
    print("[1] Project Setup  [2] Password System  [3] Info  [4] Credits [5] Clear [0] Exit the program".center(110, " "))
    print("\n\n")
    while True:
        choice = input("        >> ").strip()
        if choice == "0" or choice == "exit":
            os.system("cls")
            print(Songoda)
            print("\n\n" + Fore.CYAN + "Thank you for using my program!".center(110, " "), "\n")
            input("Press enter to exit.".center(110, " ") + "\n")
            exit("")
        elif choice == "1":
            ProjectSetup()
        elif choice == "2":
            PasswordSystem()
        elif choice == "3":
            Info()
        elif choice == "4":
            Credits()
        elif choice == "5":
            Clear()
        else:
            print("Invalid option. Please try again.".center(110, " "))

if __name__ == "__main__":
    main()
