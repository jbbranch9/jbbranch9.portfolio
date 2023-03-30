"""
functions for finding cardinal and ordinal neighbors, based on coordinates
"""


def locate_neighbor_coordinates(row: int, column: int) -> dict:
    up = row - 1
    down = row + 1
    left = column - 1
    right = column + 1
    output = {
        # center, origin
        "C": (row, column),
        "O": (row, column),
        # cardinals
        "N": (up, column),
        "W": (row, left),
        "S": (down, column),
        "E": (row, right),
        # ordinals
        "NW": (up, left),
        "SW": (down, left),
        "SE": (down, right),
        "NE": (up, right),
    }
    return output


def get_neighbor_set(row: int, column: int, include: [str] = None) -> set:
    if include is None:
        include = ["cardinals", "ordinals"]

    for inclusion_type in include:
        assert inclusion_type in ("cardinals", "ordinals", "origin")

    neighbor_coordinates = locate_neighbor_coordinates(row, column)

    key_sets = {
        "cardinals": ["N", "W", "S", "E"],
        "ordinals": ["NE", "NW", "SW", "SE"],
        "origin": ["O", ],
        }

    included_keys = []
    for i in include:
        included_keys += key_sets[i]

    return set(neighbor_coordinates[key] for key in included_keys)


def main():
    print(get_neighbor_set(row=5, column=5))


if __name__=="__main__":
    main()