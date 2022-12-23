def reverse(s):
    new_s = ''
    for i in range(len(s)):
        new_s += s[len(s)-i-1]
    return new_s

print(reverse("Hello World"))