from PySimpleGUI import Frame, Text
from ..color.palettes import colors


class TurnIndicator(Frame):

    _default_font = ("consolas", 30)
    _default_highlighted_color = colors["white"]
    _default_un_highlighted_color = colors["black"]

    def __init__(
            self,
            player1_name: str = "Player 1",
            player2_name: str = "Player 2",
            highlighted_text_color: str = None,
            un_highlighted_text_color: str = None,
            font: tuple = None,
    ):
        if highlighted_text_color:
            self.highlight_color = highlighted_text_color
        else:
            self.highlight_color = self._default_highlighted_color

        if un_highlighted_text_color:
            self.un_highlight_color = un_highlighted_text_color
        else:
            self.un_highlight_color = self._default_un_highlighted_color

        if not font:
            font = tuple(self._default_font)

        self.p1 = Text(text=player1_name, font=font, text_color=self.highlight_color)
        self.p2 = Text(text=player2_name, font=font, text_color=self.un_highlight_color)

        self.arrow = Text(
            text=self.__left_arrow_character(),
            font=font,
            pad=(5, 0),
            text_color=self._highlighted_color)

        layout = [[self.p1, self.arrow, self.p2]]

        super().__init__(
            title="",
            layout=layout,
        )

    def __right_arrow_character(self):
        return "→"

    def __left_arrow_character(self):
        return "←"


    def toggle_arrow(self):
        if self.arrow.get() is self.__right_arrow_character():
            self.arrow.update(value=self.__left_arrow_character())
        else:
            self.arrow.update(value=self.__right_arrow_character())

def main():
    pass


if __name__ == "__main__":
    main()
