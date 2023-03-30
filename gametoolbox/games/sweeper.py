from PySimpleGUI import Column
from gametoolbox.board.board import Board
from gametoolbox.gui.window import DefaultWindow, default_font


class SweeperBoard(Board):

    __difficulties = {
        "beginner": (9, 9, 10),
        "intermediate": (16, 16, 40),
        "expert": (16, 30, 99),
        }
    
    def __init__(self, difficulty_level: str = "beginner"):

        num_rows, num_cols, mine_count = self.__difficulties[difficulty_level]
        
        super().__init__(
            num_rows=num_rows,
            num_columns=num_cols,
            )


class SweeperWindow(DefaultWindow):

    def event_loop(self, event, values) -> bool:
        repeat_loop = True

        return repeat_loop


class SweeperGame:
    def __init__(self):
        self.board = SweeperBoard()

        padded_frame = Column(
            layout=[[self.board.get_frame()]],
            pad=(15, 15),
            )
        
        SweeperWindow(layout=[[padded_frame]])


def main():
    SweeperGame()


if __name__ == "__main__":
    main()
