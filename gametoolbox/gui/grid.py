import logging

from PySimpleGUI import Frame

from .grid_cell import ButtonCell, ImageCell, TextCell
from ..gui.custom_element import CustomGuiElement


class GridBase(CustomGuiElement):

    _default_dimension = 8

    _cell_factory = None

    # Abstract class; use inherited classes only.
    def __init__(
            self,
            num_rows: int,
            num_columns: int,
            cell_constructor,
    ):
        self.__layout = []

        # this is set to True after the first finalize() or read() call. it's main purpose to avoid gui element reuse
        self.__activated = False

        for r in range(num_rows):
            row = []
            self.__layout.append(row)
            for c in range(num_columns):
                cell = cell_constructor(r, c)
                row.append(cell)
        return

    def get_cell_constructor(self, constructor_kwargs: dict):
        return self._cell_factory().get_cell_constructor(constructor_kwargs)

    """
    One of the constraints of the PySimpleGUI library is that 
    no element can be used more than once in any window.
    For this reason, get_layout() and get_frame() are mutually exclusive, 
    and neither should be called more than once.
    Instantiate a new GridBase object instead.
    """

    __ReusedGuiElementException = Exception("This character_grid's layout and its GUI elements are already in use. "
                                            "PySimpleGUI does not allow reused elements."
                                            "Instantiate a new GridBase object instead.")

    def get_layout(self):
        if self.__activated:
            raise GridBase.__ReusedGuiElementException
        else:
            return self.__layout

    def get_frame(self):
        return Frame(title="", layout=self.get_layout(), border_width=0)



class CustomGrid(GridBase):
    def __init__(
            self,
            num_rows: int = GridBase._default_dimension,
            num_columns: int = GridBase._default_dimension,
            constructor_kwargs: dict = None,
    ):
        super().__init__(num_rows, num_columns, cell_constructor=self.get_cell_constructor(constructor_kwargs))


class ButtonGrid(CustomGrid):
    _cell_factory = ButtonCell


class ImageGrid(CustomGrid):
    _cell_factory = ImageCell



class TextGrid(CustomGrid):
    _cell_factory = TextCell


def main():
    pass


if __name__ == "__main__":
    main()
