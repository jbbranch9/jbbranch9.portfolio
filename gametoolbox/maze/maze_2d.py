from numpy import array
from gametoolbox.maze.characters import Vertex, Vertical, Horizontal, Center
from gametoolbox.logic.general_logic.assertions import even, odd


class Maze2dGrid:
    def __init__(self, num_rows: int, num_cols: int):

        def scale_up(dimension: int):
            return int((2 * dimension) + 1)

        num_rows = scale_up(num_rows)
        num_cols = scale_up(num_cols)

        def get_cell_constructor(row: int, col: int):
            if even(row) and even(col):
                return Vertex
            elif even(row) and odd(col):
                return Horizontal
            elif odd(row) and even(col):
                return Vertical
            elif odd(row) and odd(col):
                return Center

        character_grid_list = []
        cell_grid_list = []
        for r in range(num_rows):
            character_grid_row = []
            character_grid_list.append(character_grid_row)
            if odd(r):
                cell_grid_row = []
                cell_grid_list.append(cell_grid_row)
            else:
                cell_grid_row = None
            for c in range(num_cols):
                new_cell = get_cell_constructor(r, c)()
                character_grid_row.append(new_cell)
                if cell_grid_row and isinstance(new_cell, Center):
                    cell_grid_row.append(new_cell)


        self.character_grid = array(character_grid_list)

    def __str__(self):
        output = ""
        for row in self.character_grid:
            for char in row:
                output += str(char)
            output += "\n"
        return output

    def __repr__(self):
        return str(self)

    def write_to_file(self):
        with open("test.txt", mode="w", encoding="utf-8") as file:
            file.write(str(self))
            file.close()


def main():
    pass


if __name__ == "__main__":
    main()
