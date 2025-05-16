import sys
import os
import game
from time import sleep
from language.LanguageManager import LanguageManager
# import settings
import instruction

lm = LanguageManager(
        languagePacks_path="language/languagePacks",
        languages_prefixes=["PL","EN"],
        default_lang="PL",
        postfix="pack",
        debug_mode=False
    )

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_mainmenu() -> int:
    try:
        print(lm.get("mainmenu.startingmessage"))
        sleep(1)
        clear()
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
                return 1
            
            #how to play    
            case 2:
                clear()
                instruction.instruction()
                return 1
            
            #settings    
            case 3:
                #settings.settings()
                clear()
                return 1
            
            #game exit
            case 4: 
                clear()
                print(lm.get("mainmenu.exitmessage"))
                sleep(1)
                sys.exit() 
                return 1
            
            case _:
                print(lm.get("mainmenu.wrongoption"))
                sleep(0.5)
                clear()
                
    except ValueError:
        print(lm.get("mainmenu.wrongoption"))
        sleep(0.5)
        clear()
        return 0
        
def main():
    while True:
        choice_result = print_mainmenu()
        if choice_result == 1:
            break

            
if __name__ == "__main__":
    main()
