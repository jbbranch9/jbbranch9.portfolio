from characters import Vertex
from characters import Horizontal
from characters import Vertical
from characters import Center


class MazeGrid:
    def __init__(self, number_of_columns: int, number_of_rows: int):
        
        self.grid_dimensions = (number_of_columns, number_of_rows)

        self.all_characters = {}
        self.cells = {}
        self.horizontals = {}
        self.verticals = {}
        self.all_walls = {}
        self.vertices = {}

        self.x_range = [x_double/2 for x_double in range(1, (number_of_columns * 2) + 2)]
        self.y_range = [y_double/2 for y_double in range(1, (number_of_rows * 2) + 2)]

        for x in self.x_range:
            for y in self.y_range:

                if x.is_integer() and y.is_integer():
                    character_constructor = Center
                    character_category = self.cells

                elif x.is_integer() ^ y.is_integer():
                    if x.is_integer():
                        character_constructor = Horizontal
                        character_category = self.horizontals
                    else:
                        character_constructor = Vertical
                        character_category = self.verticals

                else:
                    character_constructor = Vertex
                    character_category = self.vertices

                character = character_constructor()
                character.x, character.y = x, y
                character_category.update({(x,y): character})
                
                self.all_characters.update({(x,y): character})
                if character_category in (self.horizontals, self.verticals):
                    self.all_walls.update({(x,y): character})

    def get(self, x, y):
        x, y = float(x), float(y)
        return self.all_characters[(x, y)]

    def update_wall(self, x: float, y:float, close:bool):
        assert (x, y) in self.all_walls.keys()

        # update wall
        if close:
            action = "close"
        else:
            action = "open"
        wall = self.all_walls[(x,y)]
        update_func = getattr(wall, action)
        update_func()
        
        # update adjacent vertices
        if (x, y) in self.horizontals.keys():
            # orientation = horizontal
            left_vertex = self.vertices[(x-0.5, y)]
            left_vertex.update(right= close)
            right_vertex = self.vertices[(x+0.5, y)]
            right_vertex.update(left= close)
        else:
            # orientation = vertical
            upper_vertex = self.vertices[(x, y-0.5)]
            upper_vertex.update(down= close)
            lower_vertex = self.vertices[(x, y+0.5)]
            lower_vertex.update(up= close)


    def update_cell(self,
                    x:float,
                    y:float,
                    
                    up_wall:bool = None,
                    right_wall:bool = None,
                    down_wall:bool = None,
                    left_wall:bool = None,
                    
                    fill: float = None,
                    change_fill_type:str = None):
        
        assert (x, y) in self.cells.keys()

        cell = self.cells[(x, y)]

        if change_fill_type is not None:
            assert change_fill_type in cell.valid_character_sets_for_type
        
        cell.set_shape(char_name=fill, char_type=change_fill_type)

        if up_wall is not None:
            self.update_wall(x, y-0.5, close=up_wall)

        if right_wall is not None:
            self.update_wall(x+0.5, y, close=right_wall)

        if down_wall is not None:
            self.update_wall(x, y+0.5, close=down_wall)

        if left_wall is not None:
            self.update_wall(x-0.5, y, close=left_wall)

    def close_outer_walls(self):
        x_min = self.x_range[0]
        x_max = self.x_range[-1]
        y_min = self.y_range[0]
        y_max = self.y_range[-1]
        
        for key in self.all_walls.keys():
            x, y = key
            if x == x_min or x == x_max or y == y_min or y == y_max:
                self.update_wall(x, y, True)
                

    def close_all_walls(self):
        for x, y in self.all_walls.keys():
            self.update_wall(x, y, True)
        

    def __str__(self):
        output = ""
        for y in self.y_range:
            for x in self.x_range:
                output += str(self.all_characters[(x,y)])
            output += "\n"
        return output

    def publish(self, filename="maze.txt"):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str(self))
            file.close
            
    def get_neighbors(self, x, y):
        x, y = float(x), float(y)
        up = (x, y-1)
        right = (x+1, y)
        down = (x, y+1)
        left = (x-1, y)
        
        cardinals = []
        for neighbor in (up, right, down, left):
            try:
                nx, ny = neighbor
                cardinals.append(self.get(nx, ny))
            except KeyError:
                pass
            
        return cardinals
        

def main():
    mz = MazeGrid(16, 8)
    for c in mz.get_neighbors(8,6):
        mz.update_cell(c.x, c.y, fill=1.0)
        
    print(mz)

if __name__ == "__main__":
    main()
