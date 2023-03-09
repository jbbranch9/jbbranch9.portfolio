from PySimpleGUI import Frame, Text


class TurnIndicator(Frame):

    _default_font = ("consolas", 30)

    def __init__(
            self,
            player1_name: str = "X",
            player2_name: str = "O",
            font: tuple = None,
    ):

        if not font:
            font = tuple(self._default_font)

        p1 = Text(text=player1_name, font=font)
        p2 = Text(text=player2_name, font=font)

        layout = [[p1, p2]]

        super().__init__(
            title="",
            layout=layout,
        )


def main():
    pass


if __name__ == "__main__":
    main()
