from gametoolbox.gui.grid import ButtonGrid
from gametoolbox.gui.demo_window import DemoWindow


def main():
    demo = ButtonGrid(4, 3)
    print(demo)
    DemoWindow(single_gui_object=demo.get_frame())


if __name__ == "__main__":
    main()