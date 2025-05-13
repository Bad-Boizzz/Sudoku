# from math import ceil
from graphic import change_text_color

def game():
    rows_cols_no = 9
    cell_width = 3
    group_by = 3

    default_color = "white"
    fulfillment_color = "cyan"

    change_text_color(default_color)
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
                change_text_color(fulfillment_color) if j % group_by != 0 else None
                print("║" + " " * cell_width, end="")
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

if __name__ == "__main__":
    game()
