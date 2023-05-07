from PySimpleGUI import Button, Menu, popup_get_text
from gametoolbox.gui.window import DefaultWindow
from gametoolbox.gui.grid import CustomGrid
from gametoolbox.gui.grid_cell import ButtonCell
from gametoolbox.color.palettes import palettes
from gametoolbox.logic.game_logic.neighbor import get_neighbor_set
from gametoolbox.os.file_handling import save_level


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

    def save(self, level_name: str = "test") -> bool:
        return save_level(
            data="test.",
            level_name=level_name,
            folder_name="blackout",
        )

    def __str__(self):
        output = ""
        layout = self.get_layout()
        for row in layout:
            for column in row:
                if column.on:
                    output += "O"
                else:
                    output += "X"
            if not row == layout[-1]:
                output += "\n"
        return output


class BlackoutGame(DefaultWindow):

    def __init__(self):
        menu = self.build_menu()
        self.board = BlackoutBoard()
        layout = [
            [menu],
            [self.board.get_frame()],
        ]
        super().__init__(
            layout=layout,
        )

    def build_menu(self):
        menu_def = [
            ['&Game', ['&Open:::open:', '&Save:::save::print:', '&Print:::print:', 'E&xit']],
        ]
        return Menu(menu_def)

    def event_loop(self, event, values) -> bool:
        repeat_loop = True

        if ":print:" in event:
            print()
            print(str(self.board))
            print()

        if ":save:" in event:
            level_name = popup_get_text(
                message="level name:",
                title="save level",
            )
            save_level(
                data=str(self.board),
                level_name=level_name,
                game_name="blackout",
            )

        try:
            cell = self.board.get_cell_from_gui_event(event)
        except (ValueError, AssertionError):
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
