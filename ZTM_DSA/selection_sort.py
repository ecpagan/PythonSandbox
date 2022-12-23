numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(array):
    length = len(array)

    for j in range(length):
        min_index = j
        for i in range(j+1, length):
            if array[i] < array[min_index]:
                min_index = i
        temp = array[j]
        array[j] = array[min_index]
        array[min_index] = temp
    return array


selection_sort(numbers)
print(numbers)
