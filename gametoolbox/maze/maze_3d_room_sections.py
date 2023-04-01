from gametoolbox.os.file_handling import clip_from_text_file


class MazeRoomSection(list):

    def __init__(
            self,
            horizontal_range: tuple[int, int] = None,
            vertical_range: tuple[int, int] = None,
            room: str = "main",
            state: str = "open",
    ):

        assert room in ("main", "next")
        assert state in ("open", "closed", "open_open", "open_closed", "open_hidden")

        filename = f"maze_room_reference/mazeroom_{room}_{state}.txt"

        x_min, x_max = horizontal_range
        y_min, y_max = vertical_range

        clip = clip_from_text_file(
            filename=filename,
            x_start=x_min,
            x_end=x_max,
            y_start=y_min,
            y_end=y_max,
        )

        super().__init__([x.rstrip("\n") for x in clip])

    def print_all(self):
        print(*self, sep="\n")

    def get_range(self, range_name: str):
        left_range = (0, 25)
        center_range = (25, 54)
        right_range = (54, 80)

        ceiling_range = (0, 13)
        wall_range = (13, 25)
        floor_range = (25, 36)

        assert range_name in ("left", "center", "right", "ceiling", "wall", "floor")
        return vars()[f"{range_name}_range"]


class Ceiling(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("center"),
            vertical_range=get_range("ceiling"),
            room="main",
            state=state,
        )


class Floor(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("center"),
            vertical_range=get_range("floor"),
            room="main",
            state=state,
        )


class CenterWall(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("center"),
            vertical_range=get_range("wall"),
            room="main",
            state=state,
        )


class LeftWall(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("left"),
            vertical_range=get_range("wall"),
            room="main",
            state=state,
        )


class RightWall(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("right"),
            vertical_range=get_range("wall"),
            room="main",
            state=state,
        )


class RightCeilingJoint(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("right"),
            vertical_range=get_range("ceiling"),
            room="main",
            state=state,
        )


class LeftCeilingJoint(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("left"),
            vertical_range=get_range("ceiling"),
            room="main",
            state=state,
        )


class RightFloorJoint(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("right"),
            vertical_range=get_range("floor"),
            room="main",
            state=state,
        )


class LeftFloorJoint(MazeRoomSection):
    def __init__(self, state: str):
        get_range = super().get_range
        super().__init__(
            horizontal_range=get_range("left"),
            vertical_range=get_range("floor"),
            room="main",
            state=state,
        )


def main():
    pass


if __name__ == "__main__":
    main()



