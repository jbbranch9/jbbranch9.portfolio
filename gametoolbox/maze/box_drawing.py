
sample = "┏━━━┳━━━┳━━━┳━━━┓"  +"\n"\
         "┃    ↑ ↓ ▼ ▲  ↕ ┃"  +"\n"\

print(sample)


class Wall():
    CHARACTERS = {
        "corner": {
            "NW": "┏",
            "SE": "┛",
            "NE": "┓",
            "SW": "┗",

            "top":    "┳",
            "bottom": "┻",
            "right":  "┫",
            "left":   "┣",

            "all":  "╋",
            "none": "·",

        },

        "horizontal": {
            "closed": "━━━",
            "gated":  "╸ ╺",
            "open":   "   ",
        },

        "vertical": {
            "closed": "┃",
            "gated":  " ",
            "open":   " ",
        },

        "center": {
            "fill_99": "███",
            "fill_75": "▓▓▓",
            "fill_50": "▒▒▒",
            "fill_25": "░░░",
            "fill_00": "   ",

            "ladder_up":   "▲# ",
            "ladder_down": " #▼",
            "ladder_both": "▲#▼",
        },
    }


def main():
    pass


if __name__ == "__main__":
    main()