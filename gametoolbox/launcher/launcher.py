from PySimpleGUI import Button, Listbox, LISTBOX_SELECT_MODE_SINGLE, Push, PopupQuickMessage
from gametoolbox.gui.window import DefaultWindow, default_font
from gametoolbox.games.tic_tac_toe import TicTacToeGame
from gametoolbox.games.sweeper import SweeperGame
from gametoolbox.games.blackout import BlackoutGame


class LauncherWindow(DefaultWindow):

    __dummy_function = lambda: PopupQuickMessage(
        "This game is not finished.\n¯\_(ツ)_/¯\nPlease check back later.",
        font=default_font(),
        auto_close_duration=2,
        keep_on_top=True,
        )

    launch_functions = {
        "tic-tac-toe": TicTacToeGame,
        "sweeper": SweeperGame,
        "blackout": BlackoutGame,
        "connect-4": __dummy_function,
        "reversi": __dummy_function,
        "checkers": __dummy_function,
        "chess": __dummy_function,
        }
    
    def __init__(self, launch_functions: dict = None):
        if launch_functions is None:
            launch_functions = LauncherWindow.launch_functions
        self.launch_functions = launch_functions

        vals = list(self.launch_functions.keys())

        selector_panel = Listbox(
            values=vals,
            default_values=[vals[0]],
            select_mode=LISTBOX_SELECT_MODE_SINGLE,
            size=(15, 10),
            font=default_font(),
            key="selector_panel",
            expand_x=True,
            bind_return_key=True,
            )

        start_btn = Button(
            button_text="run",
            size=(8, 2),
            font=default_font(),            
            )

        exit_btn = Button(
            button_text="exit",
            size=(8, 2),
            font=default_font(),            
            )

        layout = [
            [selector_panel],
            [Push(), start_btn, exit_btn, Push()],
            ]
        
        super().__init__(
            layout=layout,
            title="demo games",
            font=default_font(),
            use_custom_titlebar= True,
            titlebar_font=default_font(),
            return_keyboard_events=True,
            )

    # overload
    def event_loop(self, event, values) -> bool:
        repeat_loop = True

        try:
            selection = values["selector_panel"][0]
        except IndexError:
            selection = None

        if selection and event in ("run", "selector_panel"):
            self.iconify()
            self.run_selection(selection)
            self.deiconify()
            
        return repeat_loop

    # overload
    def restart(self):
        self.close()
        LauncherWindow()


    def run_selection(self, selection:str):
        self.launch_functions[selection]()


class LevelLauncher(LauncherWindow):
    def __init__(self):
        super().__init__(
            launch_functions={
                "level_1": lambda: None,
            }
        )


def main():
    LauncherWindow()


if __name__ == "__main__":
    main()
