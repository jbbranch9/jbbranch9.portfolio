import base64
import logging


def safe_write(
        data: str,
        file_name: str,
        directory: str,
        file_extension: str = ".txt") -> bool:
    try:
        with open(f"{directory}/{file_name}.{file_extension}", "w", encoding='utf-8',) as file:
            file.write(data)
            file.close()
        return True
    except FileExistsError:
        logging.exception(msg="FileExistsError.\nSave failed.")
        return False


def save(
        data: str,
        file_name: str,
        folder_name: str,
        file_extension: str) -> bool:
    directory = "gametoolbox/save_data/" + folder_name
    return safe_write(data=data, file_name=file_name, directory=directory, file_extension=file_extension)


def save_level(
        data: str,
        level_name: str,
        folder_name: str) -> bool:
    return save(data=data, file_name=level_name, folder_name=f"levels/{folder_name}", file_extension="lvl")


def base64_string(filename: str) -> str:
    with open(filename, "rb") as binary_file:
        b64_string = base64.b64encode(binary_file.read())
        binary_file.close()

    return b64_string


def clip_from_text_file(
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