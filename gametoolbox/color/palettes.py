
colors = {
    #  GRAYSCALES

    "white": "#ffffff",
    "black": "#000000",

    "gray_100":"#ffffff",
    "gray_99": "#ffffff",
    "gray_90": "#e6e6e6",
    "gray_80": "#cccccc",
    "gray_75": "#bfbfbf",
    "gray_70": "#b3b3b3",
    "gray_67": "#ababab",
    "gray_60": "#999999",
    "gray_50": "#808080",
    "gray_40": "#666666",
    "gray_33": "#545454",
    "gray_30": "#4d4d4d",
    "gray_25": "#404040",
    "gray_20": "#333333",
    "gray_10": "#1a1a1a",
    "gray_00": "#000000",

    # NAMED GRAYSCALES

    "black_jet": "#333333",

    "gray_silver": "#cccccc",
    "gray_timberwolf": "#d4d4d4",
    "gray_platinum": "#e6e6e6",

    # NAMED COLORS

    "brown": "#964B00",

    "green_brunswick": "#395949",

    "yellow_earth": "#E1A95F",
}

palettes = {
    "board": {
        "chess": {
            "black-white": {
                "light_color": colors["white"],
                "dark_color": colors["black"],
                },
            "black-white-soft": {
                "light_color": colors["gray_silver"],
                "dark_color": colors["gray_40"],
                },
            "green-white": {
                "light_color": colors["gray_timberwolf"],
                "dark_color": colors["green_brunswick"],
                },
            "wooden": {
                "light_color": colors["yellow_earth"],
                "dark_color": colors["brown"],
                },
        },
    },
}
