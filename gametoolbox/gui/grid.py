from PySimpleGUI import Frame, Button


class Grid:

    _default_dimension = 8

    # Abstract class; use inherited classes only.
    def __init__(
            self,
            num_rows: int,
            num_columns: int,
            cell_constructor,
            cell_args: dict
    ):
        self.__layout = []

        self.__activated = False

        # the GUI returns this key whenever an input event originates from the cell at these coordinates
        def generate_key(row_ix: int, column_ix: int):
            return f"{row_ix}:{column_ix}"

        for r in range(num_rows):
            row = []
            self.__layout.append(row)
            for c in range(num_columns):
                cell_args.update({"key": generate_key(r, c)})
                row.append(cell_constructor(**cell_args))
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


class ButtonGrid(Grid):

    __default_button_args = {
        "size": (3, 1),
        "font": "consolas",
        "pad": (1, 1),
    }

    def __init__(
            self,
            num_rows: int = Grid._default_dimension,
            num_columns: int = Grid._default_dimension,
            cell_args=None,
    ):
        if cell_args is None:
            cell_args = self.__default_button_args

        super().__init__(num_rows, num_columns, cell_constructor=Button, cell_args=cell_args)


class ImageGrid(Grid):

    __default_image_args = {
        "enable_events": True,
    }

    def __init__(
            self,
            num_rows: int = Grid._default_dimension,
            num_columns: int = Grid._default_dimension,
            cell_args=None,
    ):

        if cell_args is None:
            cell_args = self.__default_image_args

        assert "enable_events" in cell_args.keys()  # enable_events is a required key
        assert type(cell_args["enable_events"]) == bool

        super().__init__(num_rows, num_columns, cell_constructor=Button, cell_args=cell_args)


def main():
    pass


if __name__ == "__main__":
    main()
