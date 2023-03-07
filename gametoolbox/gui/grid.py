from PySimpleGUI import Frame, Button, Image, Text


class Grid:

    _default_dimension = 8

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

    """
    One of the constraints of the PySimpleGUI library is that 
    no element can be used more than once in any window.
    For this reason, get_layout() and get_frame() are mutually exclusive, 
    and neither should be called more than once.
    Instantiate a new Grid object instead.
    """

    __ReusedGuiElementException = Exception("This grid's layout and its GUI elements are already in use. "
                                            "PySimpleGUI does not allow reused elements."
                                            "Instantiate a new Grid object instead.")

    def get_layout(self):
        if self.__activated:
            raise Grid.__ReusedGuiElementException
        else:
            return self.__layout

    def get_frame(self):
        return Frame(title="", layout=self.get_layout(), border_width=0)

    """
    This is automatically* called after the parent GameWindow calls finalize() or read() for the first time.
    It is needed because some GUI object methods are unavailable until post-finalization, 
    and calling each of these methods individually is tedious, and makes the code messy.
    Override this method in inherited classes, and put all post-finalization method calls inside of it.
    """
    def post_finalization(self):
        pass


"""
GridCell (and its inherited classes) are factories. 
They build constructor functions for the GUI elements that make up a Grid, like Button(), Image(), or Text().
The most important method is 'get_cell_constructor', which takes as its only parameter: 
    a dictionary containing all kwargs for that element's constructor function
It returns (essentially) a modified constructor function for that element, but with new parameters: row_ix, column_ix
This means that the Grid doesn't need to know anything about the cells it's making, other than where it's putting them. 
    And it allows the cells to know their coordinates within the Grid, but nothing else (unless added to metadata)
"""


class GridCell:
    __default_kwargs = {}
    
    # the GUI returns this key whenever an input event originates from the cell at these coordinates
    def _generate_key(self, row_ix: int, column_ix: int):
        return f"{row_ix}:{column_ix}"

    def _prepare_cell_constructor(self, constructor_type, constructor_kwargs):
        def enclosed_constructor(row_ix: int, column_ix: int):
            gui_event_key = self._generate_key(row_ix, column_ix)
            return constructor_type(**constructor_kwargs, key=gui_event_key)

        return enclosed_constructor

    # overload this method in all inherited classes
    def get_cell_constructor(self, constructor_kwargs=None):
        pass


class ButtonCell(GridCell):
    __default_kwargs = {
        "size": (3, 1),
        "font": "consolas",
        "pad": (1, 1),
    }
    
    def get_cell_constructor(self, constructor_kwargs=None):

        if constructor_kwargs is None:
            constructor_kwargs = {}

        args = self.__default_kwargs
        args.update(constructor_kwargs)

        cell_constructor = super()._prepare_cell_constructor(
            constructor_type=Button,
            constructor_kwargs=args,
        )


        return cell_constructor



class ButtonGrid(Grid):

    def __init__(
            self,
            num_rows: int = Grid._default_dimension,
            num_columns: int = Grid._default_dimension,
            button_constructor_kwargs: dict = None,
    ):
        constructor_func = ButtonCell().get_cell_constructor(button_constructor_kwargs)

        super().__init__(num_rows, num_columns, cell_constructor=constructor_func)


class ImageCell(GridCell):
    pass


class ImageGrid(Grid):
    pass


class TextCell(GridCell):
    pass


class TextGrid(Grid):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
