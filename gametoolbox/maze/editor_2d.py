import logging

from PySimpleGUI import Text, Frame, Button
from gametoolbox.gui.window import DefaultWindow
from gametoolbox.maze.maze_2d import Maze2dGrid

class Maze2dEditor(DefaultWindow):
    __FONT = ("consolas", 14)

    def __init__(self, dimensions: tuple[int, int]):
        num_cols, num_rows = dimensions

        self.maze = Maze2dGrid(num_rows=num_rows, num_cols=num_cols)

        self.text_display = Text(
            text=str(self.maze),
        )

        layout = []
        for maze_row in self.maze.character_grid:
            layout_row = []
            layout.append(layout_row)
            for character in maze_row:
                char_display = Button(
                    button_text=character,
                    font=self.__FONT,
                    pad=(0, 0),
                )
                layout_row.append(char_display)

        frame = Frame(
            title="",
            layout=layout,
        )

        super().__init__(layout=[[frame]])

    def update(self):
        self.text_display.update(
            value=str(self.maze),
        )

    def event_loop(self, event, values) -> bool:
        repeat_loop = True
        clicked_button = self[event]
        assert isinstance(clicked_button, Button)

        return repeat_loop


def main():

    m = Maze2dEditor((5, 5))


if __name__ == "__main__":
    main()