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
    choice = input("Wybierz opcję: ")
    
    if not choice.isdigit():
        print("Podaj liczbę.")
        sleep(1)
        return 0

    choice = int(choice)

    if choice <= 0 or choice > 1:
        print("Liczba poza zakresem.")
        sleep(1)
    
    return choice

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
            case _:
                continue

if __name__ == "__main__":
    game()
