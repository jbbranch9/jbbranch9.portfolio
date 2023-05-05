import unicodedata 

def arrow(direction: str, weight: int = 2) -> str:
        
    directions = {
        'NW': 'NORTH WEST',
        'W': 'LEFTWARDS',
        'SW': 'SOUTH WEST',
        'S': 'DOWNWARDS',
        'SE': 'SOUTH EAST',
        'E': 'RIGHTWARDS',
        'NE': 'NORTH EAST',
        'N': 'UPWARDS',
        None: None,
        }
    
    weights = (
        None,
        'LIGHT',
        '',
        'MEDIUM',
        'HEAVY',
        'VERY HEAVY',
        )

    weight_range = range(len(weights))
    valid_directions = directions.keys()
    
    assert weight in weight_range
    assert direction in valid_directions

    if direction is None:
        return unicodedata.lookup("MIDDLE DOT")
    elif weight == 0:
        return " "
    else:
        return unicodedata.lookup(f"WIDE-HEADED {directions[direction]} {weights[weight]} BARB ARROW".replace("  "," "))


def main():
    print(arrow("N"))


if __name__ == "__main__":
    main()
