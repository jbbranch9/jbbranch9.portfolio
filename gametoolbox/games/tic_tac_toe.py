from ..board.board import Board
from ..gui.game_window import GameWindow
from ..gui.grid_cell import ButtonCell
from ..color.palettes import colors, palettes



class TicTacToeBoard(Board):

    _default_kwargs = {
        "pad": (5, 5),
        "font": ("consolas", 20),
        "button_color": colors["gray_75"]
    }

    def __init__(self):
        constructor_kwargs = ButtonCell().get_default_kwargs()
        constructor_kwargs.update(self._default_kwargs)
        super().__init__(
            num_rows=3,
            num_columns=3,
            constructor_kwargs=constructor_kwargs)

    def get_post_finalization_array(self) -> list:
        return []


class TicTacToeGame:
    def __init__(self):

        self.board = TicTacToeBoard()
        layout = [[self.board.get_frame()]]
        post_final_array = self.board.get_post_finalization_array()
        self.window = GameWindow(
            layout=layout,
            post_finalization_array=post_final_array,
        )

    # override
    def get_post_finalization_array(self) -> list:
        def enclosed_func():

            self.checkerize(**palettes["board"]["chess"]["wooden"])
        pf_array = [enclosed_func, ]

        return pf_array