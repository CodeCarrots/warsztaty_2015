def trigram(word):
    return [word[x:x+3] for x in range(len(word) - 2)]


a = trigram('alohomora')
b = trigram('omoraaloh')


def union(first, second):
    """
    Returns sorted list of elements in both `first` and `second` collection, without duplicates.
    """
    # Put your code here.

result = union(a, b)

print(result)