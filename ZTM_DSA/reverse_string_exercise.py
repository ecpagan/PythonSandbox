# Implement a function that reverses a string using iteration...and then recursion!
def reverse_string(string):
    new_string = ''
    # len(string)-1, because it starts with 0
    # -1 because is not inclusive, we need to include 0 so 0 -1 = -1
    # -1 because we want the step to be backwards
    for i in range(len(string)-1, -1, -1):
        new_string += string[i]
    return new_string


def reverse_string_recursive(string):
    if len(string) == 1:
        return string
    return string[-1] + reverse_string_recursive(string[:-1])


rs1 = reverse_string('yoyo mastery')  # should return: 'yretsam oyoy'
rs2 = reverse_string_recursive('yoyo mastery')  # should return: 'yretsam oyoy'
