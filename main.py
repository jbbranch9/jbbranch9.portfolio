import logging
from gametoolbox.board.board import Checkerboard, Chessboard
from gametoolbox.gui.demo_window import DemoWindow
from gametoolbox.games.tic_tac_toe import TicTacToeGame
from gametoolbox.gui.turn_indicator import TurnIndicator


def main():

    # logging.basicConfig(level=logging.DEBUG)

    # DemoWindow(
    #     single_gui_object=TurnIndicator(font=()),
    # )

    TicTacToeGame()

    # demo = Checkerboard()
    #
    # post_final = demo.setup_methods()
    #
    # DemoWindow(
    #     single_gui_object=demo.get_frame(),
    #     post_finalization_array=post_final,
    # )
    #

if __name__ == "__main__":
    main()
