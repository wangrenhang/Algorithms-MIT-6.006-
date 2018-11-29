array = [[0, 17, 9, 2, 3],
         [3, 17, 99, 388, 2],
         [100, 91, 3, 6, 9997],
         [800, 5, 8, 1, 0]]


def column_max(column):
    max = 0
    for i in range(4):
        if array[i][column] > max:
            max = array[i][column]
            index = i
    return index


def peak_find(start, end):

    column = (start + end) // 2

    # 1. Stop condition
    if end - start == 0:
        return array[column_max(start)][start]
    elif end - start == 1:
        return max([array[column_max(start)][start], array[column_max(end)][end]])

    # 2. Column max
    index = column_max(column)
    print(array[index][column])

    # 3. Row compare
    if array[index][column] <= array[index][column-1]:
        return peak_find(start, column-1)
    elif array[index][column] <= array[index][column+1]:
        return peak_find(column+1, end)
    else:
        return array[index][column]

peak = peak_find(0, 4)
print(peak)