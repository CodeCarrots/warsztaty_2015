from utils.checks import check


valid_letters = 'bcdefghijklmnopqrstuvwxyz'


def unique_letters(word):
    """
    Returns string of sorted unique letters that are both in `word` and `valid_letters`.
    Case insensitive!
    """
    return ''.join(sorted(set(word.lower()) & set(valid_letters)))


data = (
    ('Bike', 'beik'),
    ('Molllly', 'lmoy'),
    ('Abrakadabra', 'abdkr'),
    ('Ala ma kota', 'aklmot')
)

check(unique_letters, data)