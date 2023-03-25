from PySimpleGUI import Push
from gametoolbox.board.board import Board
from gametoolbox.gui.window import DefaultWindow
from gametoolbox.gui.turn_indicator import TurnIndicator
from gametoolbox.color.palettes import colors, palettes


class T3Window(DefaultWindow):
    _default_parameters = {
        'title': 'tic-tac-toe',
        'no_titlebar': False,
        'grab_anywhere': True,
        'finalize': True,
        'use_ttk_buttons': True,
    }

    def __init__(self, game, *args, **kwargs):
        self.game = game
        super().__init__(*args, **kwargs)

    def event_loop(self, event, values) -> bool:
        repeat_loop = True

        player_name = self.game.claim(tile=self[event])

        row, col = [int(coordinate) for coordinate in event.split(":")]

        self.game.board.mark(row=row, col=col, player=player_name)

        print(self.game.board)

        return repeat_loop


class T3Board(Board):

    _default_kwargs = {
        "pad": (5, 5),
        "font": ("consolas", 20),
        "button_color": colors["gray_75"]
    }

    def __init__(self):

        self.__tracker = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

        super().__init__(
            num_rows=3,
            num_columns=3,
            constructor_kwargs=self._default_kwargs)

    def __str__(self):
        output = ""
        for row_ix, row in enumerate(self.__tracker):
            output += row[0] + "┃" + row[1] + "┃" + row[2] + "\n"
            if row_ix in range(2):
                output += "━╋━╋━\n"
        return output

    def __repr__(self):
        return str(self)

    def mark(self, row: int, col: int, player: str):
        self.__tracker[row][col] = player

class TicTacToeGame:

    __P1 = "X"
    __P2 = "O"

    def player_color(self, player: str):
        return {
            self.__P1: "red",
            self.__P2: "green",
        }[player]

    def claim(self, tile):
        player_name = self.turn_indicator.get_player()
        tile.update(
            text=player_name,
            disabled_button_color=(self.player_color(player_name), "black"),
            disabled=True,
        )
        self.turn_indicator.toggle_arrow()
        return player_name


    def __init__(self):

        self.turn_indicator = TurnIndicator(
            player1_name=self.__P1,
            player2_name=self.__P2,
        )
        self.board = T3Board()
        layout = [
            [Push(), self.turn_indicator, Push()],
            [self.board.get_frame()],
        ]
        self.window = T3Window(
            game=self,
            layout=layout,
            post_finalization_array=self.get_post_finalization_array(),
        )

        self.window.turn_indicator = self.turn_indicator

    # override
    def get_post_finalization_array(self) -> list:
        def enclosed_func():

            self.board.checkerize(**palettes["board"]["checker"]["grayscale"])
        pf_array = [enclosed_func, ]

        return pf_array


def main():
    TicTacToeGame()


if __name__ == "__main__":
    main()
