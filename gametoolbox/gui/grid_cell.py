"""
GridCell (and its inherited classes) are factories.
They build constructor functions for the GUI elements that make up a GridBase,
    like Button(), Image(), or Text().
The most important method is 'get_cell_constructor', which takes as its only parameter:
    a dictionary containing all kwargs for that element's constructor function
It returns (essentially) a modified constructor function for that element,
    but with new parameters: row_ix, column_ix
This means that the GridBase doesn't need to know anything about the cells it's making,
    other than where it's putting them.
And it allows the cells to know their coordinates within the GridBase,
    but nothing else (unless added to metadata)
"""

from PySimpleGUI import Button, Image, Text
from gametoolbox.gui.custom_element import CustomGuiElement
from gametoolbox.tokens.token_button import Token


class GridCell(CustomGuiElement):
    _default_kwargs = {}

    def __init__(self, constructor_type):
        self.__constructor_type = constructor_type

    def get_default_kwargs(self):
        return dict(self._default_kwargs)

    def get_cell_constructor(self, constructor_kwargs: dict = None, ignore_default_kwargs: bool = False):
        if constructor_kwargs is None:
            constructor_kwargs = self._default_kwargs
        else:
            if ignore_default_kwargs:
                default = {}
            else:
                default = self._default_kwargs
            default.update(constructor_kwargs)
            constructor_kwargs = default

        # the GUI returns this key whenever an input event originates from the cell at these coordinates
        def generate_key(row_ix: int, column_ix: int):
            return f"{row_ix}:{column_ix}"

        def enclosed_constructor(row_ix: int, column_ix: int):
            gui_event_key = generate_key(row_ix, column_ix)
            constructor_kwargs.update({"key": gui_event_key})
            return self.__constructor_type(**constructor_kwargs)

        return enclosed_constructor


class ButtonCell(GridCell):
    _default_kwargs = {
        "size": (3, 1),
        "font": ("consolas", 14),
        "pad": (0, 0),
    }

    def __init__(self, button_constructor=Button):
        super().__init__(button_constructor)


class TokenCell(ButtonCell):
    def __init__(self):
        super().__init__(button_constructor=Token)


class ImageCell(GridCell):
    def __init__(self):
        super().__init__(Image)


class TextCell(GridCell):
    _default_kwargs = {
        "size": (3, 1),
        "font": "consolas",
        "pad": (1, 1),
    }

    def __init__(self):
        super().__init__(Text)
