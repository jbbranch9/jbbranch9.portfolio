from PySimpleGUI import Button
from gametoolbox.os.file_handling import base64_string
from gametoolbox.gui.window import DefaultWindow


class Window(DefaultWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def event_loop(self, event, values) -> bool:

        origin = self[event]
        print(type(origin))
        next_color = origin._colors[origin._colors.index(origin.color)-1]
        print(next_color)
        origin.set_image(
            color=next_color,
            size=9,
        )
        return True


class Token(Button):

    __size_range = range(-9, 10)

    _colors = ("black", "white", None)

    __IMAGE_SOURCES = tuple([base64_string(f"../assets/jbbranch9/token/{n}.png") for n in __size_range])

    def __init__(self, color: str = None, size: int = 0):

        self.color = color

        super().__init__(
            image_source=self.get_image(color, size),
        )

    def get_image(self, color: str, size: int):
        assert color in self._colors
        assert size in self.__size_range
        if color == "black":
            sign = -1
        else:
            sign = 1
        value = sign * size
        ix = value + len(self.__IMAGE_SOURCES)//2
        return self.__IMAGE_SOURCES[ix]

    def set_image(self, color: str, size: int):
        self.color = color
        if color is None:
            size = 0
        self.update(image_data=self.get_image(color, size))

    def black(self, size: int = 9):
        self.set_image(color="black", size=size)

    def white(self, size: int = 9):
        self.set_image(color="white", size=size)

    def blank(self):
        self.set_image(size=0)

def main():
    layout = [[Token()]]
    win = Window(layout=layout)



if __name__=="__main__":
    main()