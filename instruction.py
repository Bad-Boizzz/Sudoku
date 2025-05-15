import main 
from time import sleep

def clear_terminal():
  print("\033[2J\033[H")
  
def go_back_to_instruction():
  while True:
    response = input("Press enter to go back...")
    if (response == ""):
      break
    else:
      clear_terminal()
      print("Invalid choice, try again")
  clear_terminal()
  instruction()

def instruction ():
  clear_terminal()
  print("Rules of which sudoku would you like to see:\n")
  print("1. Classic sudoku")
  print("2. Diagonal sudoku")
  print("3. Jigsaw sudoku")
  print("4. Killer sudoku")
  options = {
    1: classic_sudoku,
    2: diagonal_sudoku,
    3: jigsaw_sudoku,
    4: killer_sudoku
  }
  try:
    choice = int(input("Choose the option (1-4):"))
    func = options.get(choice)
    if func:
      clear_terminal()
      func()
    else:
      print("Invalid choice, try again")
      sleep(1)
      clear_terminal()
      instruction()      
  except ValueError:
    print("Invalid choice, try again")
    sleep(1)
    clear_terminal()
    instruction()
                  

def classic_sudoku ():
  clear_terminal()
  print("A standard Sudoku puzzle consists of a grid of 9 blocks. Each block contains 9 boxes arranged in 3 rows and 3 columns.\n")
  print("Some blocks will be pre-filled for you and they cannot be changed.")
  print("In order to solve the puzzle all 81 boxes must contain numbers and the Sudoku rules must be followed:\n") 
  print("1. Each column must contain all digits from 1 to 9, with no repetitions.")
  print("2. Each row must contain all digits from 1 to 9, with no repetitions.")
  print("3. Each block must contain all digits from 1 to 9, with no repetitions.\n")
  go_back_to_instruction()
  
def diagonal_sudoku ():
  clear_terminal()
  print("A Diagonal Sudoku puzzle follows the standard rules of Sudoku with one change.\n")
  print("Standard sudoku rules:")
  print("1. Each column must contain all digits from 1 to 9, with no repetitions.")
  print("2. Each row must contain all digits from 1 to 9, with no repetitions.")
  print("3. Each block must contain all digits from 1 to 9, with no repetitions.")
  print("Additionally both main diagonals must also contain all digits from 1 to 9, with no repetitions.\n")
  go_back_to_instruction()
  
def jigsaw_sudoku ():
  clear_terminal()
  print("A Jigsaw Sudoku puzzle is a variant of standard Sudoku where the 9 standard 3x3 boxes are replaced by 9 irregularly shaped regions.\n")
  print("The puzzle follows the standard rules of Sudoku with one change:")
  print("1. Each column must contain all digits from 1 to 9, with no repetitions.")
  print("2. Each row must contain all digits from 1 to 9, with no repetitions.")
  print("3. Each irregular region must contain all digits from 1 to 9, with no repetitions.\n")
  go_back_to_instruction()
  
  
def killer_sudoku ():
  clear_terminal()
  print("A Killer Sudoku puzzle follows the standard rules of Sudoku with additional rules:\n")
  print("1. Each column must contain all digits from 1 to 9, with no repetitions.")
  print("2. Each row must contain all digits from 1 to 9, with no repetitions.")
  print("3. Each block must contain all digits from 1 to 9, with no repetitions.")
  print("Additionally the grid is divided into cages, outlined with dotted or bold lines")
  print("The number shown in the upper corner of the cage is the target sum that the digits within that cage must add up to")
  print("In each cage digits cannot be repeated\n")
  go_back_to_instruction()
  
