import os, json, string, secrets, sqlite3
from colorama import Fore, init
from tkinter import filedialog

init()

os.system("cls")

config = {
    "Settings": {
        "Version": 1,
        "Devtools": "False",
        "Opened before": "True"
    }
}

try:
    with open("config.json") as read:
        config = json.load(read)
except:
    with open("config.json", "w") as write:
            write.write("")
            json.dump(config, write)

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
    os.system("cls")
    print(Songoda)
    print("\n\n", Fore.CYAN + "Welcome to the Password Vault".center(110, " "), "\n\n","[1] Password Generator  [2] Password Vault [3] Manage Account  [0] Return to main menu".center(110, " "))
    print("\n")
    while True:
        choice = input("        >> ").strip()
        if choice == "0" or choice == "return":
            os.system("cls")
            print(Songoda)
            main()
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
    db = sqlite3.connect("password.vault")
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS accounts(id TEXT, password TEXT, website TEXT)")

    print("\n", "Welcome to the Password Vault.".center(110, " "), "\n")
    print("[1] View vault  [2] Manage passwords [3] Change master password  [0] Return to password menu".center(110, " "), "\n")

    choice = input("        >> ").strip()

def GeneratePassword(length:int):
    abc = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += secrets.choice(abc)

    return password

def Settings():
    pass

def Info():
    print("\n","Songoda's Multitools:".center(110, " "))
    print("I created this program for my personal use, and to learn more about programming.".center(110, " "))
    print("And Songoda isn't a company or whatever it's just in my head, my actual name is GuestTox.".center(110, " "))
    print("\n","---- PERMISSIONS: ----".center(110, " "))
    print("You can do whatever you want with this, you can reupload it as your own, give it to your friends,".center(110, " "),)
    print("read the source code, or even break the hell out of it.".center(110, " "))
    print("The only thing you can't do is sell it, I'd be more than happy to take down a paid version of my work.".center(110, " "), "\n")
    print("\n","---- CREDITS: ----".center(110, " "))
    print("Made by GuestTox".center(110, " "))
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
    if projectpath == "gui":
        projectpath = filedialog.askdirectory()
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
    print("[1] Project Setup  [2] Password System".center(110, " "))
    print("\n", "[I] Info [C] Clear [S] Settings [0] Exit the program".center(110, " "))
    print("\n\n")
    while True:
        choice = input("        >> ").strip().lower()
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
        elif choice == "i":
            Info()
        elif choice == "c":
            Clear()
        elif choice == "s":
            Settings()
        else:
            print("Invalid option. Please try again.".center(110, " "))

if __name__ == "__main__":
    main()
