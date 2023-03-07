import logging


class EventLogger(logging.Logger):
    def __init__(self, parent__name__, level=logging.DEBUG):
        super().__init__(name=parent__name__, level=level)

        handler = logging.FileHandler(f"{parent__name__}.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        handler.setFormatter(formatter)
        self.addHandler(handler)


def main():
    logger = logging.getLogger(__name__)
    print(type(logger))


if __name__ == "__main__":
    main()
