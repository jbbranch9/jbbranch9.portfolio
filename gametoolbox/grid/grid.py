from ..logic.engine_logic.operations import kwargs_to_vars



class Grid(list):
    def __init__(
            self,
            *args,
            **kwargs,
    ):

        kwargs_to_vars(kwargs, self)
        print(vars(self))

        print(vars())

        super().__init__([])

def main():
    g = Grid(dimensions= (1,1),
             init_list=None,
             extra_param=2)

    print(vars(g))
if __name__ == "__main__":
    main()