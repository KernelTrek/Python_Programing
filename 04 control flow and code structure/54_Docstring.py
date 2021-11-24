def example_func(food, *args, **kwargs):
    """Example function with types documented in the docstring

    Args:
        :param food:
        :param args:
        :param kwargs:
    :return:
    """
    print(food)
    print(args)
    print(kwargs)
    return True

help(example_func)