numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def merge_sort(array):
    length = len(array)
    if length == 1:
        return array

    # Split Array in into right and left
    middle = int(length / 2)
    left = array[:middle]
    right = array[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    result += list(left[l_index:]) + list(right[r_index:])
    return result


answer = merge_sort(numbers)
print(answer)
