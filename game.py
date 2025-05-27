import random
from math import ceil
from time import sleep
import main
from graphic import change_text_color

def generate_sudoku(sudoku_solution, num_holes = 48):
    puzzle = [row[:] for row in sudoku_solution]
    
    holes = set()
    while len(holes) < num_holes:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if (row, col) not in holes:
            puzzle[row][col] = 0
            holes.add((row, col))
    
    return puzzle

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
    print("\n1. Wróć do menu głównego")
    print("2. Uzupełnij komórkę")
    print("3. Wyczyść komórkę")
    choice = input("Wybierz opcję: ")
    
    if not choice.isdigit():
        print("Podaj liczbę.")
        sleep(1)
        return 0

    choice = int(choice)

    if choice <= 0 or choice > 3:
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
    x, y = get_pos()
    
    if blank_sudoku[x][y] != 0:
        print("Tej komórki nie można edytować.")
        sleep(1)
        return
    
    value = get_cell_value(x, y)
    result_sudoku[x][y] = value

def clear_cell(result_sudoku, blank_sudoku):
    x, y = get_pos()
    
    if blank_sudoku[x][y] != 0:
        print("Tej komórki nie można wyczyścić.")
        sleep(1)
        return
    
    result_sudoku[x][y] = 0

sudoku_sample = [
    [6, 7, 1, 3, 5, 8, 2, 4, 9],
    [8, 9, 3, 7, 4, 2, 6, 5, 1],
    [2, 4, 5, 9, 6, 1, 8, 7, 3],
    [4, 5, 9, 6, 7, 3, 1, 2, 8],
    [3, 6, 8, 1, 2, 5, 7, 9, 4],
    [7, 1, 2, 8, 9, 4, 3, 6, 5],
    [9, 3, 4, 2, 1, 7, 5, 8, 6],
    [1, 2, 6, 5, 8, 9, 4, 3, 7],
    [5, 8, 7, 4, 3, 6, 9, 1, 2],
]

def game():
    blank_sudoku = generate_sudoku(sudoku_sample)
    result_sudoku = [row[:] for row in blank_sudoku]

    while True:
        main.clear()

        print_sudoku(blank_sudoku, result_sudoku)

        choice = choose_option()

        match choice:
            case 1:
                main.main()
                return
            case 2:
                fill_cell(result_sudoku, blank_sudoku)
            case 3:
                clear_cell(result_sudoku, blank_sudoku)
            case _:
                continue

if __name__ == "__main__":
    game()
