"""
a Grid is any matrix with 2 or more dimensions. variations include:
Grid2D
Grid3D

related classes include:
GridTimeDimension

"""


class Grid(list):
    def __init__(
            self,
            *args,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.timekeeper = self.GridTimeDimension(parent=self)

    def record(self):
        self_copy = list(self)
        self.timekeeper.update_record(frame=self_copy)

    """
    GridTimeDimension is a list of all past states of a Grid object.
    Future plans for this class:
    1) delta recording mode, i.e. frames only track differences from previous frame, 
       rather than copy the entire grid each frame (which is bad for memory)
    2) offloading of oldest/most distant frames onto external files,
       in order to save memory when dealing with particularly long timelines or large grids
    """
    class GridTimeDimension(list):
        def __init__(self, parent, auto_start_recording: bool = False):
            super().__init__([])
            self.__parent = parent
            self.__recording = auto_start_recording

        def start_recording(self):
            self.__recording = True

        def stop_recording(self):
            self.__recording = False

        def update_record(self, frame):
            if self.__recording:
                self.append(frame)
            else:
                raise Exception("This grid's timekeeper is not set to record.")


class Grid2D(Grid):
    __DEFAULT_x = 8
    __DEFAULT_y = 8

    def __init__(
            self,
            x_dimension: int = __DEFAULT_x,
            y_dimension: int = __DEFAULT_y,
            container_type=list,
    ):

        def empty_cell():
            container_type([])

        super().__init__(
            [[empty_cell() for _column in range(x_dimension)] for _row in range(y_dimension)]
        )

    def __str__(self):
        output = ""
        for row in self:
            output += str(row)+"\n"
        return output


def main():
    g = Grid2D(
        x_dimension=3,
        y_dimension=4,
        container_type=tuple

    )
    print(g)


if __name__ == "__main__":
    main()
