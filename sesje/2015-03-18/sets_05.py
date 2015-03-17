from utils.checks import check


def mix(values):
    """
    Returns elements that are:
    - either in `a` OR `b` but NOT in both.
    AND
    - are common with elements in `c`
    """
    a, b, c = values
    # Put your code here.


data = (
    (['ab', 'bc', 'ad'], {'a'}),
    ([[1, 2], [2, 3, 4], [3, 4]], {3, 4}),
    ([[1, 'a'], ['b', 3], [3, 4]], {3}),
)

check(mix, data)
