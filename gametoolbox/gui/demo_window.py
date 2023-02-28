"""
DemoWindow is a GameWindow that takes a single gui object as a parameter.
It is used to display, test, and debug one object at a time, without having to run the entire program.
"""

import PySimpleGUI as gui

from .game_window import GameWindow


class DemoWindow(GameWindow):

    def sample_gui_object():
        new_object = gui.Text(
            "This is a demo window.\nIt displays a single gui object like this text box.\nUse it for controlled testing debugging."
        )
        return new_object
    
    def __init__(self, single_gui_object, window_parameters: dict = GameWindow._GameWindow__default_window_parameters):
        window_parameters["layout"] = [[single_gui_object]]

        super().__init__(**window_parameters)


class SampleDemoWindow(DemoWindow):

    def __init__(self):
        super().__init__(DemoWindow.sample_gui_object())


def main():
    SampleDemoWindow()


if __name__ == "__main__":
    main()
