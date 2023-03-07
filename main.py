import logging
from gametoolbox.gui.grid import ButtonGrid
from gametoolbox.gui.demo_window import DemoWindow



def main():

    logging.basicConfig(level=logging.DEBUG)

    demo = ButtonGrid(4, 3)
    DemoWindow(single_gui_object=demo.get_frame())


if __name__ == "__main__":
    main()