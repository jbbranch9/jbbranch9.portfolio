import random

from grid import MazeGrid


def coin_toss():
    return bool(random.randint(0,1))

def blobby(maze: MazeGrid):
    maze.close_outer_walls()
    cells = list(maze.cells.values())
        
    print(maze)
        

def binary(maze: MazeGrid):
    
    num_cols, num_rows = maze.grid_dimensions
    col_ix_range = range(1, num_cols+1)
    row_ix_range = range(1, num_rows+1)
    
    maze.close_all_walls()

    for y in row_ix_range:
        columns = list(col_ix_range)

        run = []

        while columns:
            x = columns.pop(0)
            
            cut_right = coin_toss() and len(columns) > 0
                
            if cut_right or len(run) == 0:
                run.append((x, y))
                
            if cut_right or y == row_ix_range[-1]:
                maze.update_cell(x=x, y=y, right_wall=False)
            else:
                down_cut_x, down_cut_y = random.choice(run)
                run = []
                if y != row_ix_range[-1]:
                    maze.update_cell(x=down_cut_x, y=down_cut_y, down_wall=False)
                
            

            print(maze)
    
    maze.update_cell(1,1, left_wall=False)
    
def main():
    m = MazeGrid(15, 15)
    binary(m)
    print(m)


if __name__ == "__main__":
    main()
