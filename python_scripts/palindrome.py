import timeit


s = "abcdefghijklmnopqrstuvwxyz" * 10

timeit.repeat(lambda: reverse_string1(s))
timeit.repeat(lambda: reverse_string2(s))
timeit.repeat(lambda: reverse_string3(s))


def reverse_string3(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)


data = reverse_string3("TURBO")
# print(data)


# for elem in reversed("TURBO"):
#     print(elem)

text = "TURBO"[::-1]
# print(text)


def reverse_string2(s):
    return "".join(reversed(s))


data = reverse_string2("TURBO")
# print(data)


def reverse_string1(s):
    return s[::-1]


# print(reverse_string1("TURBO"))


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


# print(is_palindrome("TACOCAT"))
# print(is_palindrome("TURBO"))
