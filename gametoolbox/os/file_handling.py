import base64
import logging


def safe_write(
        data: str,
        directory: str,
        file_name: str,
        file_extension: str = "txt") -> bool:
    try:
        with open(f"{directory}/{file_name}.{file_extension}", "w", encoding='utf-8',) as file:
            file.write(data)
            file.close()
        return True
    except FileExistsError:
        logging.exception(msg="FileExistsError.\nSave failed.")
        return False


def safe_read(
        directory: str,
        file_name: str,
        file_extension: str = "txt") -> str:
    output = None
    try:
        with open(f"{directory}/{file_name}.{file_extension}") as file:
            output = file.read()
            file.close()
    except FileNotFoundError:
        logging.exception(msg="FileNotFoundError.\nLoad failed.")
    return output


def saved_levels_directory(game_name: str) -> str:
    return f"gametoolbox/save_data/levels/{game_name}"

def save_level(
        data: str,
        level_name: str,
        game_name: str) -> bool:
    return safe_write(data=data, directory=saved_levels_directory(game_name), file_name=level_name, file_extension="lvl")


def load_level(
        level_name: str,
        game_name: str) -> str:
    return safe_read(directory=saved_levels_directory(game_name), file_name=level_name, file_extension="lvl")

def base64_string(filename: str) -> str:
    with open(filename, "rb") as binary_file:
        b64_string = str(base64.b64encode(binary_file.read()))
        binary_file.close()

    return b64_string


# extracts a rectangular section of characters from a text file
def clip_from_text_file(
        filename: str,
        x_start: int,
        x_end: int,
        y_start: int,
        y_end: int,
        ) -> list:

    with open(filename, "r", encoding='utf-8',) as file:
        lines = file.readlines()

    clipping = [line[x_start:x_end] for line in lines[y_start:y_end]]
    return clipping


def main():
    pass


if __name__ == "__main__":
    main()