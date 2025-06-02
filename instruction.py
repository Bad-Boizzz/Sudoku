from time import sleep
from main import print_initial_message
from typing import Callable, Optional
from language.LanguageManager import LanguageManager

lm = LanguageManager(
        languagePacks_path="language/languagePacks",
        languages_prefixes=["PL","ENG"],
        default_lang="ENG",
        postfix="pack",
        debug_mode=False
    )

def clear_terminal() -> None:
  print("\033[2J\033[H")
  
def go_back_to_instruction() -> None:
  while True:
    response: str = input(lm.get("instruction.GoBack"))
    if (response == ""):
      break
    else:
      clear_terminal()
      print(lm.get("instruction.InvalidChoice"))
      sleep(1)
  clear_terminal()
  instruction()
  
def go_back_to_main_menu() -> None:
  while True:
    response: str = input(lm.get("instruction.GoBackToMainMenu")).strip()
    if (response == ""):
      break
    else:
      print(lm.get("instruction.InvalidChoice"))
      sleep(1)
      clear_terminal()
  clear_terminal()
  print_initial_message()

def instruction() -> None:
    while True:
        clear_terminal()
        print(lm.get("instruction.ChoseSudoku"))
        print(lm.get("instruction.ClassicSudoku"))
        print(lm.get("instruction.DiagonalSudoku"))
        print(lm.get("instruction.JigsawSudoku"))
        print(lm.get("instruction.KillerSudoku"))
        print("5. " + lm.get("instruction.GoBackToMainMenuOption"))

        options: dict[int, Callable[[], None]] = {
            1: classic_sudoku,
            2: diagonal_sudoku,
            3: jigsaw_sudoku,
            4: killer_sudoku,
            5: go_back_to_main_menu
        }

        try:
            choice = int(input(lm.get("instruction.ChoseOption")))
            func = options.get(choice)
            if func:
                clear_terminal()
                func()
                break
            else:
                raise ValueError
        except ValueError:
            print(lm.get("instruction.InvalidChoice"))
            sleep(1)

def classic_sudoku () -> None:
  clear_terminal()
  print(lm.get("instruction.ClassicIntro"))
  print(lm.get("instruction.ClassicDetails1"))
  print(lm.get("instruction.ClassicDetails2")) 
  print(lm.get("instruction.ClassicRule1"))
  print(lm.get("instruction.ClassicRule2"))
  print(lm.get("instruction.ClassicRule3"))
  sleep(2)
  go_back_to_instruction()
  
def diagonal_sudoku () -> None:
  clear_terminal()
  print(lm.get("instruction.DiagonalIntro"))
  print(lm.get("instruction.DiagonalStandardRules"))
  print(lm.get("instruction.ClassicRule1"))
  print(lm.get("instruction.ClassicRule2"))
  print(lm.get("instruction.ClassicRule3"))
  print(lm.get("instruction.DiagonalExtra"))
  sleep(2)
  go_back_to_instruction()
  
def jigsaw_sudoku () -> None:
  clear_terminal()
  print(lm.get("instruction.JigsawIntro"))
  print(lm.get("instruction.JigsawChange"))
  print(lm.get("instruction.ClassicRule1"))
  print(lm.get("instruction.ClassicRule2"))
  print(lm.get("instruction.JigsawRule3"))
  sleep(2)
  go_back_to_instruction()
  
  
def killer_sudoku () -> None:
  clear_terminal()
  print(lm.get("instruction.KillerIntro"))
  print(lm.get("instruction.ClassicRule1"))
  print(lm.get("instruction.ClassicRule2"))
  print(lm.get("instruction.ClassicRule3"))
  print(lm.get("instruction.KillerCage1"))
  print(lm.get("instruction.KillerCage2"))
  print(lm.get("instruction.KillerCage3"))
  sleep(2)
  go_back_to_instruction()
  
