import random 

from grid import MazeGrid

def blobby(maze: MazeGrid):
    maze.close_outer_walls()
    cells = list(maze.cells.values())

    A_cells = []
    B_cells = []

    def mark_A(cell):
        x, y = cell.x, cell.y
        maze.update_cell(x, y, fill=0.25)

    def mark_B(cell):
        x, y = cell.x, cell.y
        maze.update_cell(x, y, fill=0.75)

    def select_and_remove_random_cell():
        c = random.choice(cells)
        cells.remove(c)
        return c

    cell_marker_function = {
        "A": mark_A,
        "B": mark_B,
    }

    def add_cell_to_group(cell_group, cell=None):
        if not cell:
            cell = select_and_remove_random_cell()
        vars(f"{cell_group}_cells").append(cell)
        cell_marker_function[cell_group](cell)




    add_cell_to_group("A")

    r = random.choice(A_cells)
    print(r.x, r.y)
        
    print(maze)
    print(A_cells)
    print(B_cells)
    print(cells)
        
        
    
    
def main():
    m = MazeGrid(10, 7)
    blobby(m)
    m.publish()

if __name__ == "__main__":
    main()