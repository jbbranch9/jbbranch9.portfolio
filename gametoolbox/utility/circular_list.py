
class CircularList(list):
    def __init__(self, init_list: list):
        self.__cursor_index = 0
        super().__init__(init_list)

    def get(self, index: int):

        while index not in range(len(self)):
            if index > 0:
                index -= len(self)
            if index < 0:
                index += len(self)

        value = self[index]
        self.__cursor_index = index

        return value

    def get_delta(self, delta: int, start_index: int = None, from_object=None):

        if from_object is not None:
            try:
                start_index = self.index(from_object)
            except ValueError:
                raise Exception("The parameter 'from_object' is not found in this list.")

        elif start_index is None:
            start_index = self.__cursor_index

        return self.get(start_index + delta)

    def next(self, from_object=None):
        return self.get_delta(start_index=1, from_object=from_object)

    def previous(self, from_object=None):
        return self.get_delta(start_index=-1, from_object=from_object)



def main():

    pass


if __name__ == "__main__":
    main()
