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

        for _r in range(num_rows):
            row = []
            self.__layout.append(row)
            for _c in range(num_columns):
                row.append(cell_constructor(**cell_args))

    """
    One of the constraints of the PySimpleGUI library is that 
    no element can be used more than once in any window.
    For this reason, get_layout() and get_frame() are mutually exclusive, 
    and neither should be called more than once.
    Instantiate a new Grid object instead.
    """

    __ReusedGuiElementException = Exception("This grid's layout is already in use. "
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
