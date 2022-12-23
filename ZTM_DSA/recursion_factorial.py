# Write two functions that finds the factorial of any number.
# One should use recursive, the other should just use a for loop


def find_factorial_recursive(number):  # O(n)
    if type(number) is not int or number < 0:
        raise Exception()
    if number == 2:
        return 2
    if number in (0, 1):
        return 1
    return number*find_factorial_recursive(number-1)


def find_factorial_iterative(number):  # O(n)
    if type(number) is not int or number < 0:
        raise Exception()

    answer = 1
    for i in range(number, 1, -1):
        answer *= i
    return answer


f1 = find_factorial_iterative(0)
f2 = find_factorial_iterative(1)
f3 = find_factorial_iterative(2)
f4 = find_factorial_iterative(5)

f11 = find_factorial_recursive(0)
f12 = find_factorial_recursive(1)
f13 = find_factorial_recursive(2)
f14 = find_factorial_recursive(5)
