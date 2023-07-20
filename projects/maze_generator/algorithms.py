from grid import MazeGrid

def blobby(maze: MazeGrid):
    maze.close_outer_walls()
    cells = list(maze.cells.values())
        
    print(maze)
        
        
    
    
def main():
    m = MazeGrid(10, 7)
    blobby(m)


if __name__ == "__main__":
    main()