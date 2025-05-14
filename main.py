import sys
import os
import game
from time import sleep
# import settings
# import instruction


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_mainmenu() -> int:
    try:
        print("Gra, która pobudzi Twój umysł!")
        sleep(1)
        clear()
        print("SUDOKU \n \n \n")
        print("1. Zagraj")
        print("2. Jak grać?")
        print("3. Ustawienia")
        print("4. Zakończ")
        choice = int(input("Wybierz opcję: "))
        match choice:
            #game start
            case 1:
                clear()
                game.game()
                return 1
            
            #how to play    
            case 2:
                clear()
                # instruction.instruction()
                return 1
            
            #settings    
            case 3:
                #settings.settings()
                clear()
                return 1
            
            #game exit
            case 4: 
                clear()
                print("Dziękujemy za grę!")
                sleep(1)
                sys.exit()   
                return 1
            
            case _:
                print("Niepoprawny wybór, spróbuj ponownie.")
                sleep(0.5)
                clear()
                
    except ValueError:
        print("Niepoprawny wybór, spróbuj ponownie.")
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
