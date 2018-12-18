def multiply_all(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product


numbers = [2, 1, 3, 4, 7, 11, 18]
product = multiply_all(numbers)
print(product)

# from functools import reduce
#
#
# numbers = [2, 1, 3, 4, 7, 11, 18]
# product = reduce(lambda x, y: x * y, numbers, 1)
#
# print(product)

# numbers = [2, 1, 3, 4, 7, 11, 18]
# squared_numbers = (n**2 for n in numbers)
# odd_numbers = (n for n in numbers if n % 2 == 1)
# print(odd_numbers)
# print(squared_numbers)
# print(numbers)

# numbers = [2, 1, 3, 4, 7, 11, 18]
# squared_numbers = map(lambda n: n**2, numbers)
# odd_numbers = filter(lambda n: n % 2 == 1, numbers)
# print(squared_numbers)
# print(odd_numbers)
# print(numbers)

# def color_of_point(point):
#     (x, y), color = point
#     return color
#
#
# points = [((1, 2), 'red'), ((3, 4), 'green')]
# points_by_color = sorted(points, key=color_of_point)
# print(points_by_color)

# def length_and_alphabetical(string):
#     return len(string), string.casefold()
#
#
# colors = (["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"])
# colors_by_length = sorted(colors, key=length_and_alphabetical)
# print(colors_by_length)

# colors = (["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"])
# print(sorted(colors, key=lambda s: s.casefold()))

# normalized_colors = map(lambda s: s.casefold(), colors)

# colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]
#
#
# def normalize_case(string):
#     return string.casefold()
#
#
# normalized_colors = map(normalize_case, colors)
