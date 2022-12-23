def merge_sorted_arrays(array1, array2):
    if len(array1) == 0:
        return array2
    elif len(array2) == 0:
        return array1

    merged_array = []
    array1_elem = array1[0]
    array2_elem = array2[0]
    i = 1
    j = 1
    while array1_elem or array2_elem:
        if array1_elem is not None and (array2_elem is None or array1_elem <= array2_elem):
            merged_array.append(array1_elem)
            if i < len(array1):
                array1_elem = array1[i]
                i += 1
            else:
                array1_elem = None
        elif array2_elem is not None and (array1_elem is None or array1_elem > array2_elem):
            merged_array.append(array2_elem)
            if j < len(array2):
                array2_elem = array2[j]
                j += 1
            else:
                array2_elem = None

    return merged_array


print(merge_sorted_arrays([0,3,4,31], [4,6,30]))
print(merge_sorted_arrays([4,6,30], [0,3,4,31]))
print(merge_sorted_arrays([0,3,4,31], []))
print(merge_sorted_arrays([], [4,6,30]))
print(merge_sorted_arrays([], []))