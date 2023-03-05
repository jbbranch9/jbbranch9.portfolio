from gametoolbox.gui.grid import ButtonGrid, ImageGrid
from gametoolbox.gui.demo_window import DemoWindow

def main():

    DemoWindow(single_gui_object=ButtonGrid().get_frame())



if __name__ == "__main__":
    main()