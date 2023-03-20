import json


def print_dict(dictionary: dict, indent: int = 2):
    printable = json.dumps(dictionary, indent=indent)
    print(printable)
    return printable
