from PySimpleGUI import Button
from gametoolbox.gui.window import DefaultWindow
from gametoolbox.gui.grid import CustomGrid
from gametoolbox.gui.grid_cell import ButtonCell
from gametoolbox.color.palettes import palettes
from gametoolbox.logic.game_logic.neighbor import get_neighbor_set


class BlackoutButton(Button):
    __palette = palettes["board"]["checker"]["blackout"]

    __on_color = __palette["light_color"]
    __off_color = __palette["dark_color"]

    def __init__(self, **constructor_kwargs):
        self.on = False
        constructor_kwargs.update({"button_color": self.__off_color})
        super().__init__(**constructor_kwargs)

    def toggle(self):
        self.on = not self.on
        if self.on:
            btn_color = self.__on_color
        else:
            btn_color = self.__off_color
        self.update(
            button_color=btn_color,
        )
        return self.on


class BlackoutCell(ButtonCell):

    def __init__(self):
        super().__init__(
            button_constructor=BlackoutButton,
        )


class BlackoutBoard(CustomGrid):
    _cell_factory = BlackoutCell

    def __init__(self):
        super().__init__(
            num_rows=9,
            num_columns=9,
        )


class BlackoutGame(DefaultWindow):

    def __init__(self):
        self.board = BlackoutBoard()
        layout = [[self.board.get_frame()]]
        super().__init__(
            layout=layout,
        )

    def event_loop(self, event, values) -> bool:
        repeat_loop = True

        try:
            cell = self.board.get_cell_from_gui_event(event)
        except ValueError:
            cell = None

        if cell:
            self.toggle_cell_and_neighbors(event)

        return repeat_loop

    def toggle_cell_and_neighbors(self, event):
        row, column = self.board.get_row_and_column_from_gui_event(event)
        neighborhood = get_neighbor_set(row, column, include=["cardinals", "origin"])
        for n in neighborhood:
            n_row, n_column = n
            height, width = self.board.get_dimensions()

            if n_row in range(0, height) and n_column in range(0, width):
                self.board.get_cell(n_row, n_column).toggle()

def main():
    BlackoutGame()


if __name__ == "__main__":
    main()
