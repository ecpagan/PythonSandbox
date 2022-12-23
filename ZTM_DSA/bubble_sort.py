numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubble_sort(array):
    length = len(array)
    for j in range(length):
        for i in range(length):
            if i + 1 < length and array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array


bubble_sort(numbers)
print(numbers)
