def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

# def my_func(a, b):
#     global c
#     b, a = a, b
#     d = 'Mike'
#     print(a, b, c, d)
#
#
# a, b, c, d = 1, 2, 'c is global', 4
# my_func(1, 2)
# print(a, b, c, d)

# def my_func(a, b):
#     global x
#     print(x)
#     x = 5
#     print(x)
#
#
# if __name__ == '__main__':
#     x = 10
#     my_func(1, 2)
#     print(x)

# def my_func(a, b):
#     print(x)
#     x = 5
#     print(x)
#
#
# if __name__ == '__main__':
#     x = 10
#     my_func(1, 2)
#     print(x)

# def my_func(a, b):
#     x = 5
#     print(x)
#
#
# if __name__ == '__main__':
#     x = 10
#     my_func(1, 2)
#     print(x)

# x = 10
#
# def my_func(a, b):
#     print(x)
#     print(z)
#
# my_func(1, 2)
