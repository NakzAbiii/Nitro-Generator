import random, string, time, requests, colorama, ctypes, os
from colorama import Fore, Style
from time import sleep
import webbrowser

banner = (f"""{Fore.BLUE}
                        ███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗
                        ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║
                        ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║
                        ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║
                        ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║
                        ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝{Style.RESET_ALL}
                                        {Fore.RED}Entwickelt von: Atrac{Style.RESET_ALL}
        """) 


print(f'{banner}')


def Main():
    os.system("cls")
    print(f'{banner}')
    colorama.init()
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Generator] von Atrac")
    print('\n')
    print(f'                                        [1] > {Fore.BLUE}Nitro Generator {Style.RESET_ALL}')
    print(f'                                        [2] > {Fore.BLUE}Discord{Style.RESET_ALL}')
    print(f'                                        [3] > {Fore.BLUE}Github{Style.RESET_ALL}')
    print('\n')
    print('\n')



    answer = input('\033[1;00m[\033[91m>\033[1;00m]\033[91m\033[00m Wähle eine Zahl aus : ')
 
    if answer == '1':
        Gen_Check()

    elif answer == '2':
        casa()

    elif answer == '3':
        no()
    else:
        print('Ungültig!, wähle eine zahl umd Nitro Codes zu generieren')
        Main()

def casa():
    webbrowser.open_new('https://discord.gg/mFshVPWryj')
    os.system("cls")
    Main()

def no():
    webbrowser.open_new('https://github.com/NakzAbiii')
    os.system("cls")
    Main()


def Gen_Check():
    os.system("cls")
    
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Generator] von Atrac  | Nitro Generator")
    checked = 0
    valid_codes = 0
    invalid_codes = 0

    print(f'{banner}')
    print('\n')
    num=input(f"Wie viele Codes willst du Generieren? ")
    to_gen = int(num)
    f=open("valid_codes.txt","w+", encoding='utf-8')
    
    for kele in range(int(num)):
        ncode = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        nitro = f"https://discord.gift/{ncode}"
        url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}GÜLTIG!{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} {nitro}')
            f.write(f"{nitro}\n")
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Generator] von Atrac | Checked: %s" % checked)
            checked += 1
            valid_codes += 1
        else:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}UNGÜLTIG!{Fore.LIGHTBLACK_EX}]{Fore.WHITE} {nitro}')
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Nitro Generator] von Atrac | Checked: %s" % checked)
            checked += 1
            invalid_codes += 1
 
    f.close()
    print(f"\n{Fore.LIGHTBLACK_EX} Gen {Fore.WHITE}{to_gen} {Fore.LIGHTBLACK_EX}Nitro Codes, {Fore.WHITE}{valid_codes} {Fore.GREEN}Valid{Fore.LIGHTBLACK_EX} {Fore.WHITE}{invalid_codes} {Fore.RED}Invalid{Fore.LIGHTCYAN_EX}\n")
    input(f"Drück Enter um zum Startbildschirm zurückzukommen.")
    Main()

Main()