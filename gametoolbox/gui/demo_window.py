"""
DemoWindow is a GameWindow that takes a single gui object as a parameter.
It is used to display, test, and debug one object at a time, without having to run the entire program.
"""

from PySimpleGUI import Text
from PySimpleGUI import Element as GuiElement

from .game_window import GameWindow


class DemoWindow(GameWindow):

    def sample_gui_object():
        new_object = Text(
            "This is a demo window.\n"
            "It displays a single gui object like this text box.\n"
            "Use it for controlled testing/debugging."
        )
        return new_object
    
    def __init__(self, single_gui_object: GuiElement, post_finalization_array: list = None):

        if post_finalization_array is None:
            post_finalization_array = [single_gui_object]

        window_params = self._default_parameters
        window_params.update({"layout": [[single_gui_object]]})

        super().__init__(
            post_finalization_array=post_finalization_array,
            **window_params,
        )


class SampleDemoWindow(DemoWindow):

    def __init__(self):
        super().__init__(DemoWindow.sample_gui_object())


def main():
    SampleDemoWindow()


if __name__ == "__main__":
    main()
