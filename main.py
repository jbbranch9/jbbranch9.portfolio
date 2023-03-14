import logging
from gametoolbox.board.board import Checkerboard, Chessboard
from gametoolbox.gui.demo_window import DemoWindow
from gametoolbox.maze.editor_2d import Maze2dEditor


def main():

    logging.basicConfig(level=logging.DEBUG)

    m = Maze2dEditor((3,3))



if __name__ == "__main__":
    main()
