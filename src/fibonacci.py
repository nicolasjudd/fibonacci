def fibonacci_pos(pos):
    """
    Calculate the Fibonacci number located as position pos.
    Considering 0 is at position 0 of the Fibonacci sequence

    Parameters
    ----------
    pos : int
        Position of the value of the Fibonacci sequnce to start with.

    Returns
    -------
    int :
        Fibonacci number at position pos
    """
    assert type(pos) == int and pos >= 0, "Position must be a positive integer"

    a, b = (0, 1)
    if pos < 2:
        b = pos
    else:
        for _ in range(pos-1):
            a, b = (b, a+b)
    return b


def fibonacci_nearest(num, kind="nearest"):
    """
    Produces the fibonacci number near the entered number.

    Parameters
    ----------
    num : real number
        Number near the fibonacci number to be found

    kind : str, optional
        Determination of which fibonacci number to return if num is between two
        fibonacci numbers.

        * "lower" -- Produces the nearest fibonacci number
          less than or equal to num
        * "upper" -- Produces the nearest fibonacci number
          greater than or equal to num
        * "nearest" -- Produces the nearest fibonacci number.
          Produces the higher number if num is equidistant from both. Default


    Return
    ------
    int :
        Fibonacci number near num
    """
    assert (type(num) == float) or (type(num) == int), "num must be a real"
    assert kind in ('lower', 'upper', 'nearest'), "kind must be a valid option"

    pos = 0
    fib_lower = 0
    fib_upper = fibonacci_pos(pos)
    while (fib_upper < num):
        pos += 1
        fib_lower = fib_upper
        fib_upper = fibonacci_pos(pos)

    if kind == 'lower':
        result = fib_lower if fib_upper != num else fib_upper
    elif kind == 'upper':
        result = fib_upper
    elif kind == 'nearest':
        measure = abs(fib_upper - num) <= abs(fib_lower - num)
        result = fib_upper if measure else fib_lower

    return result


def fibonacci_sequence(size, pos=0, stride=1):
    """
    Produce a generator of the Fibonacci sequence containing a number of
    elements begining at a given position

    Parameters
    ----------
    size : positive int
        Size of the produced Fibonacci segment

    pos : positive int, optional
        Position of the Fibonnaci sequence that the segment should begin with.

        The 0 th position of the Fibonacci sequence is 0 here.

    stride : int, optional
        Number of positions to move while traversing sequence

    Return
    ------
    generator of int
        Generator of Fibonnaci sequence with length elemnets
    """
    assert type(size) == int and size >= 0, "Size must be a positive integer"
    assert type(pos) == int and pos >= 0, "Position must be a positive integer"
    assert type(stride) == int, "Stride must be integer"

    size *= abs(stride)
    size += pos

    if stride > 0:
        return (fibonacci_pos(x) for x in range(pos, size, stride))
    elif stride < 0:
        size += stride
        pos += stride
        return (fibonacci_pos(x) for x in range(size, pos, stride))
    else:
        raise ValueError("Stride can not be 0")
