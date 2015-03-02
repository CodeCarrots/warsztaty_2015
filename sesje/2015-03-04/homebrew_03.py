# Błądżej

average_vector = []

val = 1
row_list = [val]
average_vector.append(sum(row_list) / len(row_list))
iteration = 0
val = val * (4 - iteration) / (iteration + 1)
row_list.append(int(val))
average_vector.append(sum(row_list) / len(row_list))
iteration = 1
val = val * (4 - iteration) / (iteration + 1)
row_list.append(int(val))
average_vector.append(sum(row_list) / len(row_list))
iteration = 2
val = val * (4 - iteration) / (iteration + 1)
row_list.append(int(val))
average_vector.append(sum(row_list) / len(row_list))
iteration = 3
val = val * (4 - iteration) / (iteration + 1)
row_list.append(int(val))
average_vector.append(sum(row_list) / len(row_list))

print('N-th row:', row_list)
print('averages vector:', average_vector)
