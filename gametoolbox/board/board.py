from ..gui.grid import ButtonGrid


class Board(ButtonGrid):

    def __init__(self):
        super().__init__()

    # recolors buttons into a checkerboard pattern
    def __checkerize(self, light_color: str, dark_color: str, reverse_colors: bool = False):
        def even(x: int):
            return x % 2 == 0

        def odd(x: int):
            return not even(x)

        def dark_tile(row_ix: int, col_ix: int):
            r, c = row_ix, col_ix
            E, O = even, odd
            return (E(r) and E(c)) or (O(r) and (O(c)))

        for r, row in enumerate(self.get_layout()):
            for c, col in enumerate(row):
                new_color = ""
                if dark_tile(r, c):
                    new_color = dark_color
                else:
                    new_color = light_color
                col.update(button_color=new_color)
        return


class Checkerboard(Board):
    def __init__(self):
        super().__init__()

    # override
    def post_finalization(self):
        self.__checkerize(light_color="#FFFFFF", dark_color="#000000")



def main():
    pass


if __name__ == "__main__":
    main()