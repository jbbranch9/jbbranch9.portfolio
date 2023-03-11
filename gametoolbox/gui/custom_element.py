
class CustomGuiElement:
    # Overload this method in inherited classes.
    # Within the overloaded methods, define and compile a list of all of the method closures to pass to the GameWindow,
    # to be executed after the first read() or finalize() call.
    def setup_methods(self) -> list:
        def enclosed_func():
            pass
        post_finalization_methods = [enclosed_func, ]
        return post_finalization_methods