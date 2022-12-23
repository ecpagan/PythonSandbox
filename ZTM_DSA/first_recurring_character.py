# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2
array1 = [2,5,1,2,3,5,1,2,4]

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1
array2 = [2,1,1,2,3,5,1,2,4]

# Given an array = [2,3,4,5]:
# It should return undefined
array3 = [2,3,4,5]

# Bonus... What if we had this:
#  [2,5,5,2,3,5,1,2,4]
#  return 5 because the pairs are before 2,2

array4 = [2,5,5,2,3,5,1,2,4]


def first_recurring_character(array):
    "it seems like O(n), but doing 'e not in array' will be O(n^2)?"
    temp_array = []
    for e in array:
        if e not in temp_array:
            temp_array.append(e)
        else:
            return e
    return None


def first_recurring_character2(array):
    temp_dict = dict()
    for e in array:
        if temp_dict.get(e, None) is not None:
            return e
        else:
            temp_dict[e] = True
    return None


print(first_recurring_character(array1))
print(first_recurring_character(array2))
print(first_recurring_character(array3))
print(first_recurring_character(array4))
print('-'*80)
print(first_recurring_character2(array1))
print(first_recurring_character2(array2))
print(first_recurring_character2(array3))
print(first_recurring_character2(array4))
