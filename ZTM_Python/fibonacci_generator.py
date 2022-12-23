def fibonacci_generator(index):
    a = 0
    b = 1
    for i in range(index):
        yield a
        temp = a
        a = b
        b = temp + b


def fibonacci_list(index):
    a = 0
    b = 1
    result = []
    for i in range(index):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


for x in fibonacci_generator(21):
    print(x)

for x in fibonacci_list(21):
    print(x)
