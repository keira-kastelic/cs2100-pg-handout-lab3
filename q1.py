# Use the debugger to find and fix the bug in triangular()
# Write a test, and start the debugger from the test

def triangular(n: int) -> int:
    """Returns the nth triangular number
    
    Parameters
    ----------
    n : int
        The number for which we want the triangular number
    
    Returns
    -------
    int
        The sum of all numbers between 1 and n, inclusive
    """
    result = 0
    for i in range(n):
        result += i
    return result
