numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(array):
    length = len(array)

    for i in range(length):
        if array[i] < array[0]:
            # move number to the first position
            array.insert(0, array.pop(i))
        else:
            # find where the number should go
            for j in range(1, length):
                if array[j] > array[i] > array[j - 1]:
                    array.insert(j, array.pop(i))


insertion_sort(numbers)
print(numbers)
