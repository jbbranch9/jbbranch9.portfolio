from PySimpleGUI import Frame, Button


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
                print(cell)
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


class GridCell:
    # the GUI returns this key whenever an input event originates from the cell at these coordinates
    def generate_key(self, row_ix: int, column_ix: int):
        return f"{row_ix}:{column_ix}"

    def _build_cell_constructor(self, constructor_type, constructor_args):
        def enclosed_constructor(row_ix: int, column_ix: int):
            gui_event_key = self.generate_key(row_ix, column_ix)
            return constructor_type(**constructor_args, key=gui_event_key)

        return enclosed_constructor


class ButtonCell(GridCell):
    __default_args = {
        "size": (3, 1),
        "font": "consolas",
        "pad": (1, 1),
    }

    def get_cell_constructor(self, constructor_args=None):

        if constructor_args is None:
            constructor_args = {}

        args = self.__default_args
        args.update(constructor_args)

        cell_constructor = super()._build_cell_constructor(
            constructor_type=Button,
            constructor_args=args,
        )

        print(type(cell_constructor))

        return cell_constructor



class ButtonGrid(Grid):

    def __init__(
            self,
            num_rows: int = Grid._default_dimension,
            num_columns: int = Grid._default_dimension,
            button_constructor_args: dict = None,
    ):
        constructor_func = ButtonCell().get_cell_constructor(button_constructor_args)

        super().__init__(num_rows, num_columns, cell_constructor=constructor_func)


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
