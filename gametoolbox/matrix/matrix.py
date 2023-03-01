"""
a Matrix is any nested list with 2 or more dimensions. variations include:
Matrix2D
Matrix3D

related classes include:
Point
TimeDimension
"""


class Matrix(list):
    def __init__(
            self,
            *args,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.timekeeper = self.TimeDimension(parent=self)

    # def newMatrix2D(self, source: list):
    #     y_dim = len(source)
    #     x_dim = max(*[len(row) for row in source])
    #     g2d = Matrix2D(x_dim, y_dim)
    #
    #     for row_ix, row in enumerate(source):
    #         for col_ix, col in enumerate(row):
    #             source_content = source[row_ix][col_ix]

    def record(self):
        self_copy = list(self)
        self.timekeeper.update_record(frame=self_copy)

    """
    TimeDimension is a list of all past states of a Matrix object.
    Future plans for this class:
    1) delta recording mode, i.e. frames only track differences from previous frame, 
       rather than copy the entire matrix each frame (which is bad for memory)
    2) offloading of oldest/most distant frames onto external files,
       in order to save memory when dealing with particularly long timelines or large matrices
    """
    class TimeDimension(list):
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
                raise Exception("This matrix's timekeeper is not set to record.")

    """
    The main purpose of the Point class is to be able to easily assert that you have reached the base dimension of a Matrix  
    Point is also a container for EVERYTHING at its coordinates.
    """
    class Point:
        def __init__(self, coordinates: tuple[int, ...], init_contents=None):
            self.coordinates = coordinates
            self.contents = init_contents

        def __str__(self):
            return f".@{self.coordinates}"  # literally reads as "[the] point at [these] coordinates"

        def __repr__(self):
            return str(self)


class Matrix2D(Matrix):
    __DEFAULT_x_dimension = 8
    __DEFAULT_y_dimension = 8

    def __init__(
            self,
            x_dimension: int = __DEFAULT_x_dimension,
            y_dimension: int = __DEFAULT_y_dimension,
    ):

        super().__init__([[self.Point((column, row))
                           for column in range(x_dimension)]
                          for row in range(y_dimension)])

    def __str__(self):
        output = ""
        for row in self:
            output += str(row)+"\n"
        return output


def main():

    # sample = [
    #     [],
    #     [],
    #     [],
    # ]

    g = Matrix2D(
        x_dimension=3,
        y_dimension=4,
    )
    print(g)


if __name__ == "__main__":
    main()
