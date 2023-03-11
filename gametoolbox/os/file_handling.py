import base64


def base64_string(self, filename: str) -> str:
    with open(filename, "rb") as binary_file:
        b64_string = base64.b64encode(binary_file.read())
        binary_file.close()

    return b64_string


def clip_from_file(
        filename: str,
        x_start: int,
        x_end: int,
        y_start: int,
        y_end: int,
        ) -> tuple:

    with open(filename, "r", encoding='utf-8',) as file:
        lines = file.readlines()

    clipping = [line[x_start:x_end] for line in lines[y_start:y_end]]
    return tuple(clipping)


def main():
    pass


if __name__ == "__main__":
    main()