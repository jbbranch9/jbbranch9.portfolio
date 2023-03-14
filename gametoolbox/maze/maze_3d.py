from maze_3d_room_sections import \
    RightWall, RightCeilingJoint, RightFloorJoint, \
    LeftWall, LeftCeilingJoint, LeftFloorJoint, \
    Ceiling, CenterWall, Floor


class MazeRoom(list):
    def __init__(
            self,
            left_state: str,
            center_state: str,
            right_state: str,
            ceiling_state: str,
            floor_state: str,
    ):

        self.left_ceiling = LeftCeilingJoint(state=left_state)
        self.left = LeftWall(state=left_state)
        self.left_floor = LeftFloorJoint(state=left_state)

        self.ceiling = Ceiling(state=ceiling_state)
        self.center = CenterWall(state=center_state)
        self.floor = Floor(state=floor_state)

        self.right_ceiling = RightCeilingJoint(state=right_state)
        self.right = RightWall(state=right_state)
        self.right_floor = RightFloorJoint(state=right_state)

        left_side = self.left_ceiling + self.left + self.left_floor
        center = self.ceiling + self.center + self.floor
        right_side = self.right_ceiling + self.right + self.right_floor

        zipped = list(zip(left_side, center, right_side))

        super().__init__([row[0]+row[1]+row[2]+"\n" for row in zipped])

    def __str__(self):
        output = ""
        for row in self:
            output += row
            output += "\n"
        return output

def main():
    mr = MazeRoom(
        left_state="open",
        center_state="open",
        right_state="open",
        ceiling_state="open",
        floor_state="open",
    )

    print(list(len(ln) for ln in str(mr).split("\n\n")))

    print(str(mr).replace("\n\n","\n"))

    with open("test.txt", mode="w", encoding="utf-8") as file:
        file.writelines(mr)


if __name__ == "__main__":
    main()