from PySimpleGUI import Push
from gametoolbox.board.board import Board
from gametoolbox.gui.window import DefaultWindow
from gametoolbox.gui.turn_indicator import TurnIndicator
from gametoolbox.color.palettes import colors, palettes


class T3Window(DefaultWindow):

    def __init__(self, game, *args, **kwargs):
        self.game = game
        super().__init__(*args, **kwargs)

    def event_loop(self, event, values) -> bool:
        repeat_loop = True

        self.game.claim(tile=self[event])

        return repeat_loop


class T3Board(Board):

    _default_kwargs = {
        "pad": (5, 5),
        "font": ("consolas", 20),
        "button_color": colors["gray_75"]
    }

    def __init__(self):

        super().__init__(
            num_rows=3,
            num_columns=3,
            constructor_kwargs=self._default_kwargs)




class TicTacToeGame:

    __P1 = "X"
    __P2 = "O"

    def player_color(self, player: str):
        return {
            self.__P1: "green",
            self.__P2: "red",
        }[player]

    def claim(self, tile):
        player_name = self.turn_indicator.get_player()
        tile.update(
            text=player_name,
            disabled_button_color=(self.player_color(player_name), "black"),
            disabled=True,
        )
        self.turn_indicator.toggle_arrow()


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
