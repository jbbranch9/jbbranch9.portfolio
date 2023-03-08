import logging
from gametoolbox.board.board import Checkerboard
from gametoolbox.gui.demo_window import DemoWindow



def main():

    logging.basicConfig(level=logging.DEBUG)

    demo = Checkerboard()

    post_final = demo.get_post_finalization_array()

    DemoWindow(
        single_gui_object=demo.get_frame(),
        post_finalization_array=post_final)


if __name__ == "__main__":
    main()