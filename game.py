import random
from math import ceil
from time import sleep
from graphic import change_text_color
from language.LanguageManager import LanguageManager

lm = LanguageManager(
    languagePacks_path="language/languagePacks",
    languages_prefixes=["PL","EN", "PLSLASK","ES","PT","RU","DE"],
    default_lang="PL",
    postfix="pack",
    debug_mode=False
)

def generate_sudoku(num_holes = 48):
    # Generate a complete, valid 9x9 Sudoku solution using backtracking

    # Function to check if a number can be placed in a given cell
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    # Fill the board with numbers 1-9
    def fill_board(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if fill_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    sudoku_solution = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(sudoku_solution)

    # Remove numbers to create holes in the Sudoku puzzle
    blank_sudoku = [[num for num in row] for row in sudoku_solution]

    holes = set()
    while len(holes) < num_holes:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if (row, col) not in holes:
            blank_sudoku[row][col] = 0
            holes.add((row, col))
    
    return blank_sudoku, sudoku_solution

def print_sudoku(blank_sudoku, result_sudoku,
                 rows_cols_no=9, cell_width=3, group_by=3,
                 default_color="red", fulfillment_color="white", new_value_color="blue"):
    change_text_color(default_color)
    print("╔", end="")
    for _ in range(rows_cols_no-1):
        print("═" * cell_width + "╦", end="")
    print("═" * cell_width + "╗")

    for i in range(rows_cols_no):
        for n in range(cell_width // 2):
            for j in range(rows_cols_no):
                change_text_color(fulfillment_color) if j % group_by != 0 else None
                print("║" + " " * ((cell_width-1) // 2), end="")

                if n == cell_width // 2 // 2:
                    change_text_color(fulfillment_color if blank_sudoku[i][j] == result_sudoku[i][j] else new_value_color)
                    print(result_sudoku[i][j] if result_sudoku[i][j] != 0 else " ", end="")
                    change_text_color(fulfillment_color) if j % group_by != 0 else None

                print(" " * ceil((cell_width-1) / 2), end="")
                change_text_color(default_color)
            print("║")

        if i != rows_cols_no - 1:
            print("╠", end="")
            for n in range(rows_cols_no-1):
                change_text_color(fulfillment_color) if i % group_by != group_by - 1 else None
                print("═" * cell_width, end="")
                change_text_color(default_color) if n % group_by == group_by - 1 else None
                print("╬", end="")
                change_text_color(default_color)
            print("═" * cell_width + "╣")
        else:
            print("╚", end="")
            for _ in range(rows_cols_no-1):
                print("═" * cell_width + "╩", end="")
            print("═" * cell_width + "╝")

    change_text_color(fulfillment_color)

def choose_option():
    # print("\n1. Wróć do menu głównego")
    # print("2. Uzupełnij komórkę")
    # print("3. Wyczyść komórkę")
    # print("4. Otrzymaj podpowiedź")
    print("1. " + lm.get("game.exit_to_main_menu"))
    print("2. " + lm.get("game.fill_cell"))
    print("3. " + lm.get("game.clear_cell"))
    print("4. " + lm.get("game.get_hint"))
    choice = input("Wybierz opcję: ")

    
    if not choice.isdigit():
        print("Podaj liczbę.")
        sleep(1)
        return 0

    choice = int(choice)

    if choice <= 0 or choice > 4:
        print("Liczba poza zakresem.")
        sleep(1)
    
    return choice

def get_pos():
    x = -1
    y = -1
    while x == -1 or y == -1:
        x = input("Podaj wiersz (1-9) komórki: ")
        y = input("Podaj kolumnę (1-9) komórki: ")
        if not x.isdigit() or not y.isdigit():
            print("Podaj liczby.")
            x = -1
            y = -1
        else:
            x = int(x) - 1
            y = int(y) - 1
            if x < 0 or x > 8 or y < 0 or y > 8:
                print("Liczby poza zakresem.")
                x = -1
                y = -1
    
    return x, y

def get_pos_and_value_Vector2i():
    x=-1
    y=-1
    while x == -1 or y == -1:
        agrest = input(f"x y d: ")
        agrest = agrest.strip()
        agrest = agrest.split(" ")
        print(agrest, sep=",")

        if len(agrest) != 3:
            print("Podaj 3 liczby.")
            x = -1
            y = -1  
            d = -1
        else:
            x = int(agrest[0]) - 1
            y = int(agrest[1]) - 1
            d = int(agrest[2])
            if x < 0 or x > 8 or y < 0 or y > 8:
                print("Liczby poza zakresem.")
                x = -1
                y = -1
                d = -1

    return (x, y, d)

def get_cell_value(x=0, y=0):
    value = 0
    while value == 0:
        value = input(f"Podaj wartość (1-9) do komórki ({y+1}, {x+1}): ")
        if not value.isdigit():
            print("Podaj liczbę.")
            value = 0
        else:
            value = int(value)
            if value < 1 or value > 9:
                print("Liczba poza zakresem.")
                value = 0
    
    return value

def fill_cell(result_sudoku, blank_sudoku):
    #x, y = get_pos()
    x,y,d = get_pos_and_value_Vector2i()
    if blank_sudoku[x][y] != 0:
        print("Tej komórki nie można edytować.")
        sleep(1)
        return
    
    result_sudoku[x][y] = d

def clear_cell(result_sudoku, blank_sudoku):
    x, y = get_pos()
    
    if blank_sudoku[x][y] != 0:
        print("Tej komórki nie można wyczyścić.")
        sleep(1)
        return
    
    result_sudoku[x][y] = 0

def check_if_game_finished(result_sudoku):
    for i in range(9):
        for j in range(9):
            if result_sudoku[i][j] == 0:
                return False
    return True

def check_if_result_is_valid(result_sudoku):
    # Check rows
    for row in result_sudoku:
        if len(set(row)) != 9 or 0 in row:
            return False

    # Check columns
    for col_index in range(9):
        col = [result_sudoku[row_index][col_index] for row_index in range(9)]
        if len(set(col)) != 9 or 0 in col:
            return False

    # Check 3x3 squares
    for box_row in range(3):
        for box_col in range(3):
            square = set()
            for i in range(3):
                for j in range(3):
                    value = result_sudoku[box_row * 3 + i][box_col * 3 + j]
                    if value != 0:
                        square.add(value)
            if len(square) != 9:
                return False

    return True

def get_level_difficulty():
    from main import clear
    while True:
        try:
            clear()
            print("1. " + lm.get("game.easy_level"))
            print("2. " + lm.get("game.medium_level"))
            print("3. " + lm.get("game.hard_level"))
            print("4. " + lm.get("game.expert_level"))
            level = int(input("Wybierz poziom trudności (1-4): "))
            if level in [1, 2, 3, 4]:
                return level
            else:
                print("Wybierz liczbę z zakresu 1-4.")
        except ValueError:
            print("Podaj poprawną wartość.")

        sleep(1)

def get_hint(blank_sudoku, sudoku_solution):
    x, y = get_pos()

    if blank_sudoku[x][y] != 0:
        print("Tej komórki nie można podpowiedzieć.")
        sleep(1)
        return

    print(f"Podpowiedź: w komórce ({y+1}, {x+1}) możesz wpisać {sudoku_solution[x][y]}.")

    print("Kliknij Enter, aby kontynuować...")
    x = input()


def exit_game():
    from main import clear, main

    answer = input("Czy na pewno chcesz wyjść z gry? (T/n): ").strip()

    if answer == "T":
        return 1
    return -1

def game():
    import main
    is_modified = True

    level_difficulty = get_level_difficulty()

    match level_difficulty:
        case 1:
            num_holes = 45
        case 2:
            num_holes = 50
        case 3:
            num_holes = 56
        case 4:
            num_holes = 60
        case _:
            num_holes = 45

    blank_sudoku, sudoku_solution = generate_sudoku(num_holes)
    result_sudoku = [row[:] for row in blank_sudoku]

    while True:
        main.clear()

        print_sudoku(blank_sudoku, result_sudoku)

        if is_modified and check_if_game_finished(result_sudoku):
            if check_if_result_is_valid(result_sudoku):
                change_text_color("green")
                print("Gratulacje! Ukończyłeś sudoku!")
            else:
                change_text_color("red")
                print("Niestety, rozwiązanie jest nieprawidłowe.")
            
            sleep(2)
            change_text_color("white")
            is_modified = False

        choice = choose_option()

        match choice:
            case 1:
                exit_game()
            case 2:
                is_modified = True
                fill_cell(result_sudoku, blank_sudoku)
            case 3:
                is_modified = True
                clear_cell(result_sudoku, blank_sudoku)
            case 4:
                get_hint(blank_sudoku, sudoku_solution)
            case _:
                continue
        break
if __name__ == "__main__":
    game()
