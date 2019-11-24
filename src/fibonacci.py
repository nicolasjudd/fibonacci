def fibonacci_pos(pos):
    """
    Calculate the Fibonacci number located as position pos.
    Considering ``0`` is at position ``0`` of the Fibonacci sequence

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

        The ``0`` th position of the Fibonacci sequence is ``0`` here.

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
        pos  += stride
        return (fibonacci_pos(x) for x in range(size, pos, stride))
    else:
        raise ValueError("Stride can not be 0")
