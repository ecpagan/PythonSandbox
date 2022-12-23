# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8


def fibonacci_iterative(n):  # O(n)
    if type(n) is not int or n < 0:
        raise Exception()
    array = [0, 1]
    for i in range(2, n+1):
        array.append(array[i-1]+array[i-2])
    return array[n]


calculations_recursive = 0


def fibonacci_recursive(n):  # O(2^n)
    global calculations_recursive
    calculations_recursive += 1
    if type(n) is not int or n < 0:
        raise Exception()
    if n < 2:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


calculations_dynamic = 0


# A "closure"
def fibonacci_master():  # O(n)
    """recursive fibonacci with dynamic programming and memoization"""
    cache = {}

    def fib(n):
        global calculations_dynamic
        calculations_dynamic += 1
        if n in cache:
            return cache[n]
        if n < 2:
            return n
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    # Note we are returning function WITHOUT parenthesis
    return fib


f1 = fibonacci_iterative(3)  # =2
f2 = fibonacci_iterative(8)  # =21
f3 = fibonacci_iterative(0)  # =0
f4 = fibonacci_iterative(1)  # =1
f5 = fibonacci_iterative(2)  # =1

print('ITERATIVE')
print(f'fibonacci(3)={f1}')
print(f'fibonacci(8)={f2}')
print(f'fibonacci(0)={f3}')
print(f'fibonacci(1)={f4}')
print(f'fibonacci(2)={f5}')

print('RECURSIVE')
f11 = fibonacci_recursive(3)  # =2
print(f'fibonacci(3)={f11}\tcalculations:{calculations_recursive}')
calculations_recursive = 0
f12 = fibonacci_recursive(8)  # =21
print(f'fibonacci(8)={f12}\tcalculations:{calculations_recursive}')
calculations_recursive = 0
f13 = fibonacci_recursive(0)  # =0
print(f'fibonacci(0)={f13}\tcalculations:{calculations_recursive}')
calculations_recursive = 0
f14 = fibonacci_recursive(1)  # =1
print(f'fibonacci(1)={f14}\tcalculations:{calculations_recursive}')
calculations_recursive = 0
f15 = fibonacci_recursive(2)  # =1
print(f'fibonacci(2)={f15}\tcalculations:{calculations_recursive}')
calculations_recursive = 0

print('DYNAMIC')
faster_fib = fibonacci_master()
f101 = faster_fib(3)  # =2
print(f'fibonacci(3)={f101}\tcalculations:{calculations_dynamic}')
calculations_dynamic = 0
f102 = faster_fib(8)  # =21
print(f'fibonacci(8)={f102}\tcalculations:{calculations_dynamic}')
calculations_dynamic = 0
f103 = faster_fib(0)  # =0
print(f'fibonacci(0)={f103}\tcalculations:{calculations_dynamic}')
calculations_dynamic = 0
f104 = faster_fib(1)  # =1
print(f'fibonacci(1)={f104}\tcalculations:{calculations_dynamic}')
calculations_dynamic = 0
f105 = faster_fib(2)  # =1
print(f'fibonacci(2)={f105}\tcalculations:{calculations_dynamic}')
calculations_dynamic = 0
