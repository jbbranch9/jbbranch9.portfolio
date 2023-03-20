import logging
from PySimpleGUI import Button
from gametoolbox.gui.demo_window import DemoWindow
from gametoolbox.os.file_handling import base64_string


def main():

    logging.basicConfig(level=logging.DEBUG)

    img_src = base64_string(filename="assets/jbbranch9.itch.io/token.gif")

    btn = Button(image_source=img_src)

    dw = DemoWindow(btn)



if __name__ == "__main__":
    main()
