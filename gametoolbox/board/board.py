from ..gui.grid import GridBase, ButtonGrid
from ..color.palettes import palettes

class Board(ButtonGrid):

    def __init__(
            self,
            num_rows: int = GridBase._default_dimension,
            num_columns: int = GridBase._default_dimension):

        super().__init__(num_rows, num_columns)

    # recolors buttons into a checkerboard pattern
    def checkerize(self, light_color: str, dark_color: str, reverse_colors: bool = False):
        def even(x: int):
            return x % 2 == 0

        def odd(x: int):
            return not even(x)

        def light_tile(row_ix: int, col_ix: int):
            r, c = row_ix, col_ix
            E, O = even, odd
            return (E(r) and E(c)) or (O(r) and (O(c)))

        for r, row in enumerate(self.get_layout()):
            for c, col in enumerate(row):
                new_color = ""
                if light_tile(r, c):
                    new_color = light_color
                else:
                    new_color = dark_color
                col.update(button_color=new_color)
        return


class Checkerboard(Board):
    def __init__(
            self,
            num_rows: int = GridBase._default_dimension,
            num_columns: int = GridBase._default_dimension):

        super().__init__(num_rows, num_columns)

    # override
    def get_post_finalization_array(self) -> list:
        def enclosed_func():

            self.checkerize(**palettes["board"]["chess"]["wooden"])
        pf_array = [enclosed_func, ]

        return pf_array



def main():
    pass


if __name__ == "__main__":
    main()