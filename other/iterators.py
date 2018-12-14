"""Decorators practise"""


def bread(func):
    def wrapper():
        print("</-----\>")
        func()
        print("<\_____/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~~salad~~")
    return wrapper


@bread
@ingredients
def sandwich(food="--becon--"):
    print(food)


sandwich()


# sandwich()
# sandwich = bread(ingredients(sandwich))
# sandwich()
# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
#
#
# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
#
#
# @make_bold
# @make_italic
# def hello():
#     return "hello habr"
#
#
# print(hello())

# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
#
#
# mul(4)(3)

# a = [1, 2, 3, 4, 5]
# sq = lambda x: x**2
# print(sq(5))
# 25
# print(sq(6))
# 36
# b = list(map(sq, a))
# print(b)
# [1, 4, 9, 16, 25]
# def simple_generator(val):
#     while val > 0:
#         val -= 1
#         yield 1
#
#
# gen_iter = simple_generator(5)
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))

# class SimpleIterator:
#     def __int__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration
#
#
# s_iter1 = SimpleIterator(5)
# print(next(s_iter1))

# num_list = [1, 2, 3, 4, 5]
#
# for i in num_list:
#     print(i)
