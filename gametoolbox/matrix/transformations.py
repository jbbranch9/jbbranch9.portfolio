"""
Collection of functions that take a Matrix object as a parameter,
and

"""

class MatrixTransformations():

    def rotate2D(self, grid2d, direction):
        assert direction in ("CW", "WS")

        print(type(grid2d))

        rotation_count = {
            "CW": 1,
            "WS": 3,
        }

        # returns a copy of a Grid2D object, rotated CW once
        def rotated_CW_2D(grid2D_object):
            return list(map(list, zip(*reversed(grid2D_object))))

        for _count in range(rotation_count[direction]):
            grid2d = rotated_CW_2D(grid2D)

    def rotate_WS_2D(self, grid2d):
        self.rotate_CW_2D(self.rotate_CW_2D(self.rotate_CW_2D(grid2d)))

    ROTATE_CW_3D = lambda mtx3D: Matrix_3D(copy_matrix= [Matrix_3D.ROTATE_CW_2D(layer) for layer in mtx3D])
    ROTATE_WS_3D = lambda mtx3D: Matrix_3D(copy_matrix= [Matrix_3D.ROTATE_WS_2D(layer) for layer in mtx3D])

    ROLL_CW_3D   = lambda mtx3D: Matrix_3D(copy_matrix= zip(*[Matrix_3D.ROTATE_CW_2D(face) for face in zip(*mtx3D)]))
    ROLL_WS_3D   = lambda mtx3D: Matrix_3D(copy_matrix= Matrix_3D.ROLL_CW_3D(Matrix_3D.ROLL_CW_3D(Matrix_3D.ROLL_CW_3D(mtx3D))))
    ROLL_FWD_3D  = lambda mtx3D: Matrix_3D(copy_matrix= Matrix_3D.ROTATE_CW_3D(Matrix_3D.ROLL_CW_3D(Matrix_3D.ROTATE_WS_3D(mtx3D))))
    ROLL_BACK_3D = lambda mtx3D: Matrix_3D(copy_matrix= Matrix_3D.ROTATE_WS_3D(Matrix_3D.ROLL_CW_3D(Matrix_3D.ROTATE_CW_3D(mtx3D))))
