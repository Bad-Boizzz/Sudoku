from language.LanguageManager import LanguageManager
lm = LanguageManager(
        languagePacks_path="language/languagePacks",
        languages_prefixes=["PL","EN", "PLSLASK"],
        default_lang="PLSLASK",
        postfix="pack",
        debug_mode=True
)

import sys
import os
import game
from time import sleep

import settings
# import settings
import instruction



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_initial_message():
        print(lm.get("mainmenu.startingmessage"))
        sleep(1)
        clear()

def print_mainmenu() -> int:
    try:
        print("SUDOKU \n \n \n")
        print("1. " + lm.get("mainmenu.start"))
        print("2. " + lm.get("mainmenu.HowToPlay"))
        print("3. " + lm.get("mainmenu.settings"))
        print("4. " + lm.get("mainmenu.exit"))
        choice = int(input(lm.get("mainmenu.chooseoption")))
        match choice:
            #game start
            case 1:
                clear()
                game.game()
                return -1
            
            #how to play    
            case 2:
                clear()
                instruction.instruction()
                return -1
            
            #settings    
            case 3:
                settings.main_settings()
                clear()
                return -1
            
            #game exit
            case 4: 
                clear()
                print(lm.get("mainmenu.exitmessage"))
                sleep(1)
                sys.exit() 
                return 1
            
            case _:
                print("\n" + lm.get("mainmenu.wrongoption"))
                sleep(1)
                clear()
                
    except ValueError:
        print("\n" + lm.get("mainmenu.wrongoption"))
        sleep(1)
        clear()
        return 0
        
def main():
    while True:
        choice_result = print_mainmenu()
        if choice_result == 1:
            break

            
if __name__ == "__main__":
    print_initial_message()
    main()
