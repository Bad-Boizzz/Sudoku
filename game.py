def game():
    rows_cols_no = 9

    print("#" * (rows_cols_no * 6 + 1))
    for i in range(rows_cols_no):
        for _ in range(3):
            for j in range(rows_cols_no):
                print("#     ", end="")
            print("#")
        print("#" * (rows_cols_no * 6 + 1))

if __name__ == "__main__":
    game()
