# from math import ceil

def game():
    rows_cols_no = 9
    cell_width = 3

    print("╔", end="")
    for _ in range(rows_cols_no-1):
        print("═" * cell_width + "╦", end="")
    print("═" * cell_width + "╗")

    for i in range(rows_cols_no):
        for n in range(cell_width // 2):
            for j in range(rows_cols_no):
                # if n == cell_width // 2 // 2:
                #     print("║" + " " * ((cell_width-1) // 2) + str((i*rows_cols_no+j)%10) + " " * ceil((cell_width-1) / 2), end="")
                #     continue
                print("║" + " " * cell_width, end="")
            print("║")

        if i != rows_cols_no - 1:
            print("╠", end="")
            for _ in range(rows_cols_no-1):
                print("═" * cell_width + "╬", end="")
            print("═" * cell_width + "╣")
        else:
            print("╚", end="")
            for _ in range(rows_cols_no-1):
                print("═" * cell_width + "╩", end="")
            print("═" * cell_width + "╝")

if __name__ == "__main__":
    game()
