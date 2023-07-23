class MazeCharacter:
    """
    MazeCharacter's purpose is to collect, organize, access a useful set of
    Unicode characters which can be used to draw mazes using only text.
    Characters are grouped by type, called char_type (analogous to a class),
    and then by its name within that type, called char_name.
    """
    __CHARACTERS = {
        None: {
            None: "",
        },

        "Vertex": {

            # (up, right, down, left)
            
            (0, 0, 0, 0): "·",
            
            (1, 0, 0, 0): "╹",
            (0, 1, 0, 0): "╺",
            (0, 0, 1, 0): "╻",
            (0, 0, 0, 1): "╸",
            
            (1, 1, 0, 0): "┗",
            (1, 0, 0, 1): "┛",
            (0, 1, 1, 0): "┏",
            (0, 0, 1, 1): "┓",
            (0, 1, 0, 1): "━",
            (1, 0, 1, 0): "┃",
            

            (1, 1, 0, 1): "┻",
            (1, 1, 1, 0): "┣",
            (0, 1, 1, 1): "┳",
            (1, 0, 1, 1): "┫",

            (1, 1, 1, 1): "╋",
            None: " ",

        },

        "Horizontal": {
            "closed": "━━━",
            "opened": "   ",
            "breadcrumb": " · ",
            None: "   ",
        },

        "Vertical": {
            "closed": "┃",
            "opened": " ",
            "breadcrumb": "·",
            None: " ",
        },

        "Fill": {
            1.0: "███",
            .75: "▓▓▓",
            .50: "▒▒▒",
            .25: "░░░",
            0.0: "   ",
            "breadcrumb_N_S": " · ",
            "breadcrumb_W": "·· ",
            "breadcrumb_E": " ··",
            "breadcrumb_W_E": "···",
            None:"   ",
        },

        "Ladder": {
            "up":   "▲# ",
            "down": " #▼",
            "both": "▲#▼",
            None: " # ",
        },

        "CenterArrow": {
            "NW": " ↖ ",
            "N":  " ↑ ",
            "NE": " ↗ ",
            "E":  " → ",
            "SE": " ↘ ",
            "S":  " ↓ ",
            "SW": " ↙ ",
            "W":  " ← ",
            "V":  " ↕ ",
            "H":  " ↔ ",
            None: " · ",
        },

        "Arrow": {
            "NW": "↖",
            "N":  "↑",
            "NE": "↗",
            "E":  "→",
            "SE": "↘",
            "S":  "↓",
            "SW": "↙",
            "W":  "←",
            "V":  "↕",
            "H":  "↔",
            None: "·",
        },
        
        "Block": {
            1.0: "██",
            .75: "▓▓",
            .50: "▒▒",
            .25: "░░",
            0.0: "  ",
            None: "  ",
        },
    }

    valid_character_sets_for_type = []

    def __init__(self, char_type: str = None, char_name = None):
        self.__character_type = None
        self.__character_name = None
        self.__shape = None
        self.x, self.y = None, None

        self.set_shape(char_name, char_type)

    def __str__(self):
        return str(self.__shape)

    def __repr__(self):
        return str((self.x, self.y))

    def set_shape(self, char_name: str, char_type: str = None):

        if char_type == None:
            char_type = self.__character_type

        if self.valid_character_sets_for_type:
            assert char_type in self.valid_character_sets_for_type

        assert char_type in self.__CHARACTERS.keys()
        assert char_name in self.__CHARACTERS[char_type].keys()

        self.__character_type = char_type
        self.__character_name = char_name

        self.__shape = self.__CHARACTERS[char_type][char_name]

    def get_type(self):
        return self.__character_type

    def get_name(self):
        return self.__character_name




class Vertex(MazeCharacter):

    valid_character_sets_for_type = ["Vertex"]

    def __init__(self):
        super().__init__(char_type= "Vertex", char_name= (0, 0, 0, 0))
        self.up = 0
        self.right = 0
        self.down = 0
        self.left = 0

    def update(self, up:int = None, right:int = None, down:int = None, left:int = None  ):
        for direction in (up, right, down, left):
            if direction is not None:
                direction = int(direction)
            assert direction in (0, 1, None)
        
        if up == None:
            up = self.up
        if right == None:
            right = self.right
        if down == None:
            down = self.down
        if left == None:
            left = self.left

        self.set_shape(char_name=(up, right, down, left))
        self.up, self.right, self.down, self.left = up, right, down, left


class Wall(MazeCharacter):

    def __init__(self, orientation:str):
        assert orientation in ("Horizontal", "Vertical")
        super().__init__(char_type= orientation, char_name= "opened")
        
    def is_opened(self) -> bool:
        return self.get_name() == "opened"
    
    def is_closed(self) -> bool:
        return self.get_name() == "closed"

    def close(self):
        self.set_shape(char_name= "closed")

    def open(self):
        self.set_shape(char_name= "opened")


class Horizontal(Wall):

    valid_character_sets_for_type = ["Horizontal"]
    
    def __init__(self):
        super().__init__(orientation= "Horizontal")


class Vertical(Wall):

    valid_character_sets_for_type = ["Vertical"]
        
    def __init__(self):
        super().__init__(orientation= "Vertical")

class Center(MazeCharacter):

    valid_character_sets_for_type = ["Fill", "Ladder", "CenterArrow"]
    
    def __init__(self, init_shape = None):
        super().__init__(char_type= "Fill", char_name=0.0)



def main():
    pass


if __name__ == "__main__":
    main()
