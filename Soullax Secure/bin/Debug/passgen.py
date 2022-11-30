print("[#] Importing Libraries...")
import os
os.system("title Password Generator")
os.system("cls")
os.system("mode con: cols=50 lines=10")
try:
    from colorama import Fore
except:
    print("[!] A python module is missing, we will install it...")
    os.system("timeout>nul 1")
    os.system("cls")
    os.system("pip install colorama")
    os.system("cls")
    print("[#] Importing Libraries...")
    from colorama import Fore


os.system("cls")
print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} Importing Libraries...")

try:
    import random
except:
    print(f"{Fore.RED}[!]{Fore.RESET}{Fore.YELLOW} A python module is missing, we will install it...")
    os.system("timeout>nul 1")
    os.system("cls")
    os.system("pip install random")
    os.system("cls")
    print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} Importing Libraries..")
    import random


print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} Loading characters variable...")
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} Loading others variable...")

use_for = lower_case + upper_case + number + symbols
lenght_for_pass = 40

print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.RED} GENERATING PASSWORD...")

password = "".join(random.sample(use_for, lenght_for_pass))

print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} wirting password...")

with open('password.txt', 'w') as f:
    f.write(password)

print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} Restarting UI")
os.startfile("Soullax Secure.exe")

print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} Clearing txt file {Fore.RED}(for no stealing)")
os.system("timeout>nul 2")

with open('password.txt', 'w') as f:
    f.write("The generated password will appear here.")
print(f"{Fore.GREEN}[#]{Fore.RESET}{Fore.YELLOW} TXT file is cleared")

print(f"{Fore.GREEN}[#] FINISHED")

print(f"{Fore.RESET}")