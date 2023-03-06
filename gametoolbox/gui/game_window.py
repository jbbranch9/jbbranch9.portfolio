"""
This is the parent class for all game windows.

"""

from PySimpleGUI import Window, WIN_CLOSED


def exit_events():
    return WIN_CLOSED, 'Exit', 'exit', 'EXIT', 'Escape:27', 'F5:116'


def restart_events():
    return 'Restart', 'restart', 'RESTART', 'F2:113'





class GameWindow(Window):
    __EXIT_EVENTS = exit_events()
    __RESTART_EVENTS = restart_events()

    __print_events_enabled = True

    # these parameters are passed to the parent class __init__ method,
    # override with game-specific params
    def default_window_parameters():
        return {
            'title': '',
            'layout': [[]],
            'return_keyboard_events': True,
            'no_titlebar': False,
            'grab_anywhere': True,
            'finalize': True,
            'resizable': True,
        }
    
    def __init__(self, **kwargs):
        
        if kwargs:
            window_parameter_kwargs = kwargs
        else:
            window_parameter_kwargs = default_window_parameters()

        super().__init__(
            **window_parameter_kwargs
            )

        self.finalize()
        
        self.__window_event_loop()

    # DO NOT override. Use game_event_loop instead,
    # which is called once per __window_event_loop cycle.
    def __window_event_loop(self):
        
        while True:
            event, values = self.read()
            if self.__print_events_enabled:
                self.__print_event(event, values)
            
            if event in GameWindow.__EXIT_EVENTS: 
                break 
            
            if event in GameWindow.__RESTART_EVENTS:
                self.__restart()
                break
                
            self.game_event_loop()

        self.close()  # This is a redundant failsafe to ensure the window closes.

    # override this method for each game's specific loop(s).
    def game_event_loop(self):
        pass
    
    def __restart(self):
        self.close()
        return GameWindow()

    def __print_event(self, event, values):
        print("event:")
        print(event)
        print("values:")
        print(values)

    def toggle_print_event(self, enable: bool = not __print_events_enabled):
        self.__print_events_enabled = enable

    def get_default_parameters(self):
        return dict(self.default_window_parameters)
        

def main():
    demo = GameWindow()
    return demo


if __name__ == "__main__":
    main()
    print('done')
