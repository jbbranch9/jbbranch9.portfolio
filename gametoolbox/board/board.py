from ..gui.grid import ButtonGrid
from ..color.palettes import palettes


class Board(ButtonGrid):

    # recolors buttons into a checkerboard pattern
    def checkerize(self, light_color: str, dark_color: str, reverse_pattern: bool = False):

        if reverse_pattern:
            light_color, dark_color = dark_color, light_color

        def even(x: int):
            return x % 2 == 0

        def odd(x: int):
            return not even(x)

        def light_tile(row_ix: int, col_ix: int):
            _r, _c = row_ix, col_ix
            _E, _O = even, odd
            return (_E(_r) and _E(_c)) or (_O(_r) and (_O(_c)))

        for r, row in enumerate(self.get_layout()):
            for c, col in enumerate(row):
                if light_tile(r, c):
                    new_color = light_color
                else:
                    new_color = dark_color
                col.update(button_color=new_color)
        return


class Checkerboard(Board):
    def __init__(
            self,
            constructor_kwargs: dict = None,
            color_palette: str = "wooden",
    ):
        self.color_palette = color_palette
        super().__init__(num_rows=8, num_columns=8, constructor_kwargs=constructor_kwargs)

    def setup_methods(self) -> list:
        def checkerize_enclosed():
            self.checkerize(**palettes["board"]["checker"][self.color_palette])
        post_finalization_methods = [checkerize_enclosed, ]
        return post_finalization_methods


class Chessboard(Checkerboard):
    def __init__(self):
        super().__init__(constructor_kwargs=None, color_palette="green-white")


def main():
    pass


if __name__ == "__main__":
    main()
