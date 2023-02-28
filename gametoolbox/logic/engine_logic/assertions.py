def even(x: int):
    return x % 2 == 0


def odd(x: int):
    return not even(x)


# returns False if a kwargs dict is missing a required keyword
def all_required_kwargs(kwargs_dict: dict, required_kwargs: iter) -> bool:
    return set(required_kwargs).issubset(set(kwargs_dict.keys()))


def main():
    pass


if __name__ == "__main__":
    main()
