"""
DefaultWindow is the parent class for all game windows.

"""

import logging
from PySimpleGUI import Window, WIN_CLOSED


def exit_events():
    return WIN_CLOSED, 'Exit', 'exit', 'EXIT', 'Escape:27', 'F5:116', ':exit:'


def restart_events():
    return 'Restart', 'restart', 'RESTART', 'F2:113', ':restart:'


def default_font(size: int = 14):
    return "consolas", size


class DefaultWindow(Window):
    __EXIT_EVENTS = exit_events()
    __RESTART_EVENTS = restart_events()

    # these parameters are passed to the parent class __init__ method,
    # override with game-specific params as needed
    _default_parameters = {
        'title': '',
        "layout": [[]],
        'return_keyboard_events': True,
        'no_titlebar': False,
        'grab_anywhere': True,
        'finalize': True,
        'resizable': True,
        'font': default_font(),
        'use_custom_titlebar': True,
        'titlebar_font': default_font(10),
    }

    def merge_window_parameters_into_default_parameters(self, update_parameters: dict):
        self._default_parameters = DefaultWindow._default_parameters
        self._default_parameters.update(update_parameters)
    
    def __init__(self, layout: list = None, post_finalization_array: list = None, **window_parameter_kwargs):

        if not window_parameter_kwargs:
            window_parameter_kwargs = self._default_parameters

        if layout:
            window_parameter_kwargs["layout"] = layout

        super().__init__(
            **window_parameter_kwargs
            )

        self.finalize()
        self.__post_finalization(post_finalization_array)
        self.__window_event_loop()

    # DO NOT overload '__window_event_loop'
    # For gameplay loops, use 'event_loop' instead,
    # which is called once per '__window_event_loop' cycle.
    def __window_event_loop(self):
        repeat_loop = True
        while repeat_loop:
            event, values = self.read()
            logging.info(f"\n  event:\n    {event}")
            logging.info(f"\n  values:\n    {values}")
            
            if event in DefaultWindow.__EXIT_EVENTS:
                break 
            
            if event in DefaultWindow.__RESTART_EVENTS:
                self.restart()
                break

            # calling 'event_loop' returns a bool, which indicates whether
            # '__window_event_loop' should repeat after this loop
            repeat_loop = self.event_loop(event, values)

        self.close()  # This is a redundant failsafe to ensure the window closes.

    """
    Overload this method for each game's specific loop(s).
    All overloads of this method MUST return a bool called 'repeat_loop', 
        and SHOULD also assign repeat_loop to True at the top of each loop.
    """
    def event_loop(self, event, values) -> bool:
        repeat_loop = True
        return repeat_loop
    
    def restart(self):
        self.close()
        return DefaultWindow()

    def iconify(self):
        root = self.TKroot
        root.update_idletasks()
        root.overrideredirect(False)
        root.iconify()

    def deiconify(self):
        root = self.TKroot
        root.update_idletasks()
        root.overrideredirect(True)
        root.deiconify()

    def __post_finalization(self, post_finalization_array: list = None):
        if post_finalization_array:
            for post_final_function in post_finalization_array:
                post_final_function()

        self.bind_hotkeys()

    def bind_hotkeys(self):
        self.bind("<Control-p>", ":print:")
        self.bind("<Control-s>", ":save:")
        self.bind("<Control-o>", ":open:")
        self.bind("<Control-w>", ":exit:")
        self.bind("<Control-r>", ":restart:")  # use this to restart the entire window
        self.bind("<Control-l>", ":reload:")   # use this to reload a level within the original window
        self.bind("<Control-`>", ":debug:")

        

def main():
    demo = DefaultWindow()
    return demo


if __name__ == "__main__":
    main()
