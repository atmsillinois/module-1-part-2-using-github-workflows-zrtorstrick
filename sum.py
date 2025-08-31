def sum_of_integers(a, b):
    if not isinstance(a, int):
        raise TypeError(f'"{a}" is not an integer', a)

    if not isinstance(b, int):
        raise TypeError(f'"{b}" is not an integer', b)

