import logging
from gametoolbox.board.board import Checkerboard
from gametoolbox.gui.window import DefaultWindow

def main():

    logging.basicConfig(level=logging.DEBUG)

    cb = Checkerboard()

    win = DefaultWindow(layout=cb.get_layout())






if __name__ == "__main__":
    main()
