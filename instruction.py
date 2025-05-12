import os
def clear_terminal():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def instruction ():
  print("Rules of which sudoku would you like to see:\n")
  print("1. Classic sudoku")
  print("2. Diagonal sudoku")
  print("3. Region sudoku")
  print("4. Killer sudoku")
  print("5. Jigsaw sudoku")

def classic_sudoku ():
  clear_terminal()
  print("A standard sudoku puzzle consists of a grid of 9 blocks. Each block contains 9 boxes arranged in 3 rows and 3 columns.")
  print("Some blocks will be pre-filled for you and they cannot be changed.")
  print("In order to solve the puzzle all 81 boxes must contain numbers and the Sudoku rules must be followed:\n") 
  print("1. Each column must contain all digits from 1 to 9, with no repetitions.")
  print("1. Each row must contain all digits from 1 to 9, with no repetitions.")
  print("1. Each block must contain all digits from 1 to 9, with no repetitions.")
  
def diagonal_sudoku ():
  pass #TODO
  
def region_sudoku ():
  pass #TODO
  
def killer_sudoku ():
  pass #TODO
  
def jigsaw_sudoku ():
  pass #TODO
