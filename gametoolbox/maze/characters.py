
"""
MazeCharacter's purpose is to collect, organize, and allow access to
a useful set of Unicode characters that can be used to draw mazes using only text.
Characters are grouped by type, called char_type (analogous to a class),
and then by its name within that type, called char_name.
"""


from gametoolbox.utility.circular_list import CircularList


class MazeCharacter:

    __UNICODE_CHARACTERS = {
        None: {},

        "Vertex": {
            "NW": "┏",
            "SE": "┛",
            "NE": "┓",
            "SW": "┗",

            "top":    "┳",
            "bottom": "┻",
            "right":  "┫",
            "left":   "┣",

            "all":  "╋",
            "none": "·",
            None:   "╋",

            "blank": " ",

        },

        "Horizontal": {
            "closed": "━━━",
            "gated":  "╸ ╺",
            "opened":   "   ",
        },

        "Vertical": {
            "closed": "┃",
            "gated":  " ",
            "opened":   " ",
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
            "ladder_up":   "▲# ",
            "ladder_down": " #▼",
            "ladder_both": "▲#▼",
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
        },

        "Block": {
            1.0: "██",
            .75: "▓▓",
            .50: "▒▒",
            .25: "░░",
            0.0: "  ",
        },
    }

    def __init__(self, character_sets: tuple = (None,)):
        self.__CHARACTERS = {}
        for char_set in character_sets:
            self.__CHARACTERS.update(MazeCharacter.__UNICODE_CHARACTERS[char_set])
        # The line above ensures that subclasses can only access characters related to that subclass,
        # while allowing all characters to be stored in one location in the code, for human-readability.

        self.character_keys = CircularList(list(self.__CHARACTERS.keys()))

        self.__shape = ""

    def __str__(self):
        return str(self.__shape)

    def __repr__(self):
        return str(self)

    def set_shape(self, shape: str):  # Note: calling this method from MazeCharacter base class will create errors
        self.__shape = self.lookup_character(shape)

    def get_shape(self):
        return str(self.__shape)

    # Note: lookup_character is for finding character values from within __CHARACTERS by name.
    # It's not the getter function for the MazeCharacter's current shape.
    def lookup_character(self, char_name) -> str:  # DO NOT call from MazeCharacter base class, only from inherited classes
        return str(self.__CHARACTERS[char_name])


class Vertex(MazeCharacter):
    __default_shape = None

    def __init__(self, init_shape = None):
        super().__init__(character_sets=("Vertex",))

        self.set_shape(self.__default_shape)

class Wall(MazeCharacter):
    __default_shape = "closed"

    def __init__(self, orientation: str):
        assert orientation in ("Horizontal", "Vertical")
        super().__init__(character_sets=(orientation, "Arrow"))

        self.set_shape(self.__default_shape)

    def can_pass_through(self) -> bool:
        return self.get_shape() is not self.lookup_character("closed")

    def close(self):
        self.set_shape("closed")

    def open(self):
        self.set_shape("opened")

    def gate(self):
        self.set_shape("gated")

class Horizontal(Wall):
    def __init__(self):
        super().__init__(orientation="Horizontal")


class Vertical(Wall):
    def __init__(self):
        super().__init__(orientation="Vertical")

class Center(MazeCharacter):
    __default_shape = None

    def __init__(self, init_shape = None):
        super().__init__(character_sets=("Fill", "Arrow", "Ladder"))

        self.set_shape(self.__default_shape)


def main():
    C = Center()
    print(C)


if __name__ == "__main__":
    main()
