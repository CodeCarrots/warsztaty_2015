from utils.checks import check

valid_letters = 'AaBbCcIiZz'
valid_numbers = (1, 2, 3, 4, 100, 101, 102, 103, 104)
valid_words = (
    'Ala',
    'ma',
    'kota'
)


def is_valid(value):
    """
    Returns True of False if `value` is in either of:
    - valid_letters
    - valid_numbers
    - valid_words
    """
    # Put your code here.


data = (
    ('a', True),
    ('b', True),
    ('D', False),
    ('1', False),
    (1, True),
    ('ala', True),
    ('Ma', False),
    ('130', False),
)


check(is_valid, data)