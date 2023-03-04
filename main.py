from gametoolbox.gui.grid import ButtonGrid, ImageGrid
from gametoolbox.gui.demo_window import DemoWindow

def main():
    btn_args = {

    }
    DemoWindow(single_gui_object=ButtonGrid(num_rows=4, num_columns=5, button_args=btn_args).get_frame())



if __name__ == "__main__":
    main()