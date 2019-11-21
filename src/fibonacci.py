def fibonacci_pos(pos):
    """
    Calculate the Fibonacci number located as position pos, considering 0 is at
    position 0 of the Fibonacci sequence

    Parameters
    ----------
    pos : int
        Index of the value of the Fibonacci sequnce to start with. E.g.,

    Returns
    -------
    int :
        Fibonacci number at position pos
    """
    assert type(pos) == int and pos >= 0, "Position must be a positive integer"
    return pos if pos < 2 else fibonacci_pos(pos-1) + fibonacci_pos(pos-2)
