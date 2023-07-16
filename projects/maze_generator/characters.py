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
            "NW": "┏",
            "SE": "┛",
            "NE": "┓",
            "SW": "┗",

            "top": "┳",
            "bottom": "┻",
            "right": "┫",
            "left": "┣",

            "all": "╋",
            "none": "·",
            "blank": " ",
            None: "╋",

        },

        "Horizontal": {
            "closed": "━━━",
            "gated": "╸ ╺",
            "opened": "   ",
            None: "   ",
        },

        "Vertical": {
            "closed": "┃",
            "gated": " ",
            "opened": " ",
            None: " ",
        },

        "Fill": {
            1.0: "███",
            .75: "▓▓▓",
            .50: "▒▒▒",
            .25: "░░░",
            0.0: "   ",
            None:"   ",
        },

        "Ladder": {
            "up":   "▲# ",
            "down": " #▼",
            "both": "▲#▼",
            None: " # ",
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

    def __init__(self, char_type: str = None, char_name: str = None):
        self.__character_type = None
        self.__character_name = None
        self.__shape = None

        self.set_shape(char_name, char_type)

    def __str__(self):
        return str(self.__shape)

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return str(str(self)+str(other))

    def set_shape(self, char_name: str, char_type: str = None):

        if char_type == None:
            char_type = self.__character_type

        assert char_type in self.__CHARACTERS.keys()
        assert char_name in self.__CHARACTERS[char_type].keys()

        self.__character_type = char_type
        self.__character_name = char_name

        self.__shape = self.__CHARACTERS[char_type][char_name]

    def get_type(self):
        return str(self.__character_type)

    def get_name(self):
        return str(self.__character_name)




class Vertex(MazeCharacter):

    def __init__(self):
        super().__init__(char_type= "Vertex", char_name= "all")


class Wall(MazeCharacter):

    def __init__(self, orientation: str):
        assert orientation in ("Horizontal", "Vertical")
        super().__init__(char_type= orientation, char_name= "closed")

    def can_pass_through(self) -> bool:
        return self.get_name() != "closed"

    def close(self):
        self.set_shape(char_name= "closed")

    def open(self):
        self.set_shape(char_name= "opened")

    def gate(self):
        self.set_shape(char_name= "gated")

class Horizontal(Wall):
    def __init__(self):
        super().__init__(orientation="Horizontal")


class Vertical(Wall):
    def __init__(self):
        super().__init__(orientation="Vertical")

class Center(MazeCharacter):
    def __init__(self, init_shape = None):
        super().__init__(char_type= "Fill", char_name=0.25)


def main():
    Vertex()
    x = (Vertex() + Horizontal()) + Vertex()
    print(x)


if __name__ == "__main__":
    main()
