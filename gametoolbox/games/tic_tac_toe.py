import logging
from PySimpleGUI import Push, popup_auto_close
from gametoolbox.board.board import Board
from gametoolbox.gui.window import DefaultWindow, default_font
from gametoolbox.gui.turn_indicator import TurnIndicator
from gametoolbox.color.palettes import colors, palettes


class T3Window(DefaultWindow):
    _default_parameters = {
        'title': 'tic-tac-toe',
        'no_titlebar': False,
        'grab_anywhere': True,
        'finalize': True,
        'font': default_font(),
        'use_custom_titlebar': True,
        'titlebar_font': default_font(10),
    }

    def __init__(self, game, *args, **kwargs):
        self.game = game
        super().__init__(*args, **kwargs)

    # overload
    def restart(self):
        self.close()
        TicTacToeGame()

    # overload
    def event_loop(self, event, values) -> bool:
        repeat_loop = True

        player_name = self.game.claim(tile=self[event])

        row, col = self.game.board.get_row_and_column_from_gui_event(event)

        self.game.board.mark(row=row, col=col, player=player_name)

        victory, winning_triplets = self.game.board.victory()

        if victory:
            winner = player_name
            game_over_message = f"game over:\n" \
                                f"  {winner} wins"
            popup_auto_close(
                game_over_message,
                title="game over",
                modal=True,
                auto_close=True,
                auto_close_duration=2,
                relative_location=(0, -100),
            )

            logging.info(msg=game_over_message)
            logging.info(msg=f"winning conditions:\n{winning_triplets.items()}")

            self.restart()
            repeat_loop = False

        return repeat_loop


class T3Board(Board):

    _default_kwargs = {
        "pad": (5, 5),
        "font": ("consolas", 20),
        "button_color": colors["gray_75"]
    }

    __diagonals = (
        ("0:0", "1:1", "2:2"),
        ("0:2", "1:1", "2:0")
    )

    def __init__(self):

        self.__tracker = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        super().__init__(
            num_rows=3,
            num_columns=3,
            constructor_kwargs=self._default_kwargs)

    def __str__(self):
        output = ""
        for row_ix, row in enumerate(self.__tracker):
            output += row[0] + "┃" + row[1] + "┃" + row[2] + "\n"
            if row_ix in range(2):
                output += "━╋━╋━\n"
        return output

    def __repr__(self):
        return str(self)

    def mark(self, row: int, col: int, player: str):
        self.__tracker[row][col] = player

    def victory(self):

        is_victory = False

        def match(list_of_three: list):
            assert len(list_of_three) == 3
            return list_of_three[0] == list_of_three[1] == list_of_three[2] \
                and " " not in list_of_three

        winning_triplets = {
            "rows": [],
            "diagonals": [],
            "columns": [],
        }

        board = self.__tracker

        # check for rows and columns for matches
        for ix in range(3):
            row = board[ix]
            if match(row):
                winning_triplets["rows"].append(ix)
                is_victory = True
            column = [r[ix] for r in board]
            if match(column):
                winning_triplets["columns"].append(ix)
                is_victory = True

        # check diagonals for matches
        for ix, diagonal_set in enumerate(self.__diagonals):
            tiles = []
            for coordinates in diagonal_set:
                r, c = self.get_row_and_column_from_gui_event(coordinates)
                tiles.append(board[r][c])
            if match(tiles):
                winning_triplets["diagonals"].append(ix)
                is_victory = True

        return is_victory, winning_triplets



class TicTacToeGame:

    __P1 = "X"
    __P2 = "O"

    def player_color(self, player: str):
        return {
            self.__P1: "red",
            self.__P2: "green",
        }[player]

    def claim(self, tile):
        player_name = self.turn_indicator.get_player()
        tile.update(
            text=player_name,
            disabled_button_color=(self.player_color(player_name), "black"),
            disabled=True,
        )
        self.turn_indicator.toggle_arrow()
        return player_name


    def __init__(self):

        self.turn_indicator = TurnIndicator(
            player1_name=self.__P1,
            player2_name=self.__P2,
        )
        self.board = T3Board()
        layout = [
            [Push(), self.turn_indicator, Push()],
            [self.board.get_frame()],
        ]
        self.window = T3Window(
            game=self,
            layout=layout,
        )

        self.window.turn_indicator = self.turn_indicator



def main():
    TicTacToeGame()


if __name__ == "__main__":
    main()
