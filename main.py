import sys
import os
def print_mainmenu() -> int:
    print("SUDOKU \n \n \n")
    print("1. Zagraj")
    print("2. Jak grać?")
    print("3. Ustawienia")
    print("4. Zakończ")
    choice = int(input("Wybierz opcję: "))
    match choice:
        case 1:
            os.system('cls')
            #funkcja do rozpoczęcia gry
            return 1
            
        case 2:
            os.system('cls')
            #instruction()
            return 1
            
        case 3:
            os.system('cls')
            #settings()
            return 1
        
        case 4:
            os.system('cls')
            sys.exit()
            return 1
            
        case _:
            os.system('cls')
            return 0
            
if __name__ == "__main__":
    while True:
        choice_result = print_mainmenu()
        if choice_result == 1:
            break
        
        
