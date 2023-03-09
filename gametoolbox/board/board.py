from ..gui.grid import GridBase, ButtonGrid
from ..color.palettes import palettes

class Board(ButtonGrid):

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

    # overload this function in inherited class
    def get_post_finalization_array(self) -> list:
        def enclosed_func():
            pass
        pf_array = [enclosed_func, ]
        return pf_array


class Checkerboard(Board):
    def __init__(
            self,
            constructor_kwargs: dict = None,
            color_palette: str = "wooden",
    ):
        self.color_palette = color_palette
        super().__init__(num_rows=8, num_columns=8, constructor_kwargs=constructor_kwargs)

    def get_post_finalization_array(self) -> list:
        def checkerize_enclosed():
            self.checkerize(**palettes["board"]["chess"][self.color_palette])
        pf_array = [checkerize_enclosed, ]
        return pf_array



def main():
    pass


if __name__ == "__main__":
    main()