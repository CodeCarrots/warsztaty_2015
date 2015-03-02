vector = [1, 2, 3]

print('orig:', vector)


def expand_and_reverse_v1(vector, prefix, suffix):
    vector = prefix + vector + suffix
    return list(reversed(vector))


def expand_and_reverse_v2(vector, prefix, suffix):
    vector = prefix + vector
    vector.extend(suffix)
    vector.reverse()
    return vector


new_vector_v1 = expand_and_reverse_v1(vector, [-2, -1], [100, 200])

print('after-use v1:', vector)

print('new v1:', new_vector_v1)

new_vector_v2 = expand_and_reverse_v2(vector, [-2, -1], [100, 200])

print('after-use v2:', vector)

print('new v2:', new_vector_v2)

