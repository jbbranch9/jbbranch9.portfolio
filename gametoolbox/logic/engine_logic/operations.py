from .assertions import all_required_kwargs


def kwargs_to_vars(kwargs_dict: dict, vars_target, required_kwargs: iter = ()):
    assert all_required_kwargs(kwargs_dict, required_kwargs)
    vars(vars_target).update(kwargs_dict)
    return


def main():
    pass


if __name__ == "__main__":
    main()
