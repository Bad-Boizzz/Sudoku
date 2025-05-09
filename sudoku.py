import math 


class Cell:
    def __init__(self, value:int, notes_numbers:list[int]=None) -> None:
        self.value = value
        self.notes_numbers = notes_numbers

    def __str__(self) -> str:
        return str(self.value)



class Sudoku_Square_Boxes:
    def __init__(self,grid:list[list[Cell]]=None) -> None:
       
        self.__check_if_grid_is_valid_Sudoku_Square_Boxes(grid)
        
        self.grid: list[list[Cell]] = grid
        self.size: int = len(grid)
        self._box_size:int = int(math.sqrt(self.size))
        
    

    def __str__(self):
        
        lines = []
        sep = '+' + '+'.join(['-' * (2 * self._box_size + 1)] * self._box_size) + '+'
        for r in range(len(self.grid)):
            if r % self._box_size == 0:
                lines.append(sep)
            row_vals = []
            for c in range(self.size):
                if c % self._box_size == 0:
                    row_vals.append('|')
                val = self.grid[r][c]
                row_vals.append(str(val) if val != 0 else '.')
            row_vals.append('|')
            lines.append(' '.join(row_vals))
        lines.append(sep)
        return '\n'.join(lines)

    @staticmethod
    def Cell_Sudoku_from_2D_int_list(grid: list[list[int]]) -> None:
        if (math.ceil(math.sqrt(len(grid))) != math.floor(math.sqrt(len(grid)))):
            raise ValueError("Grid must be a perfect square.")
        if not all(len(row) == len(grid[0]) for row in grid):
            raise ValueError("All rows in the grid must have the same length.")
        if not len(grid) == len(grid[0]):
            raise ValueError("Grid must be a square.")
        if not all(isinstance(cell, int) for row in grid for cell in row):
            raise ValueError("All elements in the grid must be of type int.")
        if not all(0 <= cell <= len(grid) for row in grid for cell in row):
            raise ValueError("Cell values must be between 0 and {}.".format(len(grid)))
        return [[Cell(value) for value in row] for row in grid]


    @staticmethod
    def __check_if_grid_is_valid_Sudoku_Square_Boxes(grid: list[list[Cell]]) -> None:
        if (math.ceil(math.sqrt(len(grid))) != math.floor(math.sqrt(len(grid)))):
            raise ValueError("Grid must be a perfect square.")
        if not all(len(row) == len(grid[0]) for row in grid):
            raise ValueError("All rows in the grid must have the same length.")
        if not len(grid) == len(grid[0]):
            raise ValueError("Grid must be a square.")
        if not all(isinstance(cell, Cell) for row in grid for cell in row):
            raise ValueError("All elements in the grid must be of type Cell.")
        if not all(0 <= cell.value <= len(grid) for row in grid for cell in row):
            raise ValueError("Cell values must be between 0 and {}.".format(len(grid)))

if __name__ == "__main__":
    sud = Sudoku_Square_Boxes(Sudoku_Square_Boxes.Cell_Sudoku_from_2D_int_list([
        [7,5,2,0,3,1,0,0,0],
        [3,0,6,5,0,9,8,0,2],
        [4,8,9,0,0,0,5,1,3],
        [0,0,8,0,5,0,4,6,9],
        [0,0,0,3,0,0,0,8,1],
        [6,0,0,2,0,0,0,0,5],
        [0,7,3,0,0,0,0,0,6],
        [0,0,4,7,0,0,1,0,0],
        [0,0,5,0,2,8,0,4,0]
    ]))

    print(sud)