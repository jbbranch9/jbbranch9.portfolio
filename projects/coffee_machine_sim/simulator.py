from PySimpleGUI import Frame, Button
from gametoolbox.gui.demo_window import DemoWindow

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

FONT = ("consolas", 14)

coin_values = (".01", ".05", ".10", ".25", ".50", "1.00")


class Simulator(DemoWindow):
    def __init__(self):

        def get_flavor_btn(flavor: str):
            txt = flavor+"\n"+\
                  "-"*11+"\n"+\
                  f"${MENU[flavor]['cost']}0"

            btn = Button(
                button_text=txt,
                key=f"selection:{flavor}",
                size=(12, 3),
                font=FONT,
            )
            return btn

        select_flavor_panel = [get_flavor_btn(flavor) for flavor in MENU.keys()]

        def get_coin_btn(value: str):
            btn = Button(
                button_text=value,
                key=f"add_coin:{value}",
                font=FONT,
                size=(5, 2),
            )
            return btn

        add_coin_panel = [get_coin_btn(c_val) for c_val in coin_values]

        layout = [
            select_flavor_panel,
            add_coin_panel,
        ]

        frame = Frame(
            title="",
            layout=layout,
        )

        super().__init__(single_gui_object=frame)


    def event_loop(self, event, values) -> bool:

        event_type, event_arg = event.split(":")

        print(event_type, event_arg)
        return True

    # This is an overload of the DefaultWindow event_loop. It is called once per cycle.
    # Put all simulator code in self.event_loop() instead.
    def game_event_loop(self, event, values) -> bool:
        return self.event_loop(event, values)








def main():
    Simulator()


if __name__ == "__main__":
    main()
