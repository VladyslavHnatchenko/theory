class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initialization {0})".format(self.name))

        Robot.population += 1

    def __del__(self):
        print("{0} died!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{0} it was the last.".format(self.name))
        else:
            print("The last {0:d} worked robots.".format(Robot.population))

    def say_hi(self):
        print("Welcome! My owners call me {0}.".format(self.name))

    def how_many():
        print("We've {0:d} robots.".format(Robot.population))

    how_many = staticmethod(how_many)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Ro


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print("Hi man! My name is ", self.name)
#
#
# p = Person('Swaroop')
# p.say_hi()

# class Person:
#     def say_hi(self):
#         print("What's up Man! How are you?)")
#
#
# p = Person()
# p.say_hi()

# class Person:
#     pass
#
#
# p = Person()
# print(p)

# name = "Swaroop"
#
# if name.startswith("Swa"):
#     print("Yes, string startswith 'Swa'")
#
# if 'a' in name:
#     print("Yes, she's contains char 'a'")
#
# if name.find('war') != -1:
#     print("Yes, she's contains chars 'war'")
#
# delimiter = "_*_"
#
# my_list = ['Brazil', 'Ukraine', 'India', 'China']
# print(delimiter.join(my_list))

# ab = {
#     "Swarrop": "swarrop@gmail.com",
#     "Larry": "larry@gmail.com",
#     "Matsumoto": "matz@gmail.com",
#     "Spammer": "spammer@gmail.com"
# }
#
# print("Email Swarrop'a: ", ab['Swarrop'])
#
# del ab["Spammer"]
#
# print("\nThe mail-book contain's {0} contacts\n".format(len(ab)))
#
# for name, address in ab.items():
#     print("Contact {0} with mail {1}".format(name, address))
#
# ab['Guido'] = "quido@python.org"
#
# if 'Guido' in ab:
#     print("\nAddress Guido:", ab['Guido'])


# from math import *
#
#
# n = input("Enter range:- ")
# p = [2, 3]
# count = 2
# a = 5
# while count < int(n):
#     b = 0
#     for i in range(2, a):
#         if i <= sqrt(a):
#             if a % i == 0:
#                 print("a neprost", a)
#                 b = 1
#             else:
#                 pass
#     if b != 1:
#         print("a prost", a)
#         p = p + [a]
#     count = count + 1
#     a = a + 2
# print(p)

# import sys
#
#
# print("Arguments cmd:")
# for i in sys.argv:
#     print(i)
#
# print("\n\nVariable PYTHONPATH contains", sys.path, "\n")

# def print_max(x, y):
#     """We can see maximum number.
#
# Both of numbers must be integer number."""
#
#     x = int(x)
#     y = int(y)
#
#     if x > y:
#         print(x, ' max')
#     else:
#         print(y, ' max')
#
#
# print_max(3, 5)
# print(print_max.__doc__)

# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'Numbers equals.'
#     else:
#         return y
#
#
# print(maximum(2, 2.000003))

# def total(initial=5, *numbers, extra_number):
#     count = initial
#
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
#
#
# total(10, 1, 2, 3, extra_number=50)
# total(10, 1, 2, 3, extra_number=-16)

# def total(initial=5, *numbers, **keywords):
#     count = initial
#
#     for number in numbers:
#         count += number
#
#     for key in keywords:
#         count += keywords[key]
#     return count
#
#
# print(total(10, 1, 2, 3, vegetables=50, fruits=100))

# def func(a, b=5, c=10):
#     print('a equals', a, ',  b equals', b, ', a c equals', c)
#
#
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)

# def func_outer():
#     x = 2
#     print("x equals", x)
#
#     def func_inner():
#         nonlocal x
#         x = 5
#
#     func_inner()
#     print("Local x changed on", x)
#
#
# func_outer()

# x = 50
# def func():
#     global x
#
#     print('x equals', x)
#     x = 2
#     print("Changed global variable x on ", x)
#
#
# func()
# print('Value x equals', x)

# x = 50
#
#
# def func(x):
#     print('x equals', x)
#     x = 2
#     print("Change local x on", x)
#
#
# func(x)
# print('X = ', x)

# def print_max(a, b):
#     if a > b:
#         print(a, 'max')
#     elif a == b:
#         print(a, 'equals', b)
#     else:
#         print(b, 'max')
#
#
# print_max(3, 4)

# import os
# import time
# source = ['C:\\Users\\vladyslav.hnatchenko\\PycharmProjects\\theory']
# target_dir = ['C:\\Users\\vladyslav.hnatchenko\\PycharmProjects\\theory\\other']
# target = target_dir + os.sep + time.strftime['%Y%m%d%H%M%S'] + '.zip'
# zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
#
# if os.system(zip_command) == 0:
#     print('The reserve copy successfully created in ', target)
# else:
#     print("The reserve copy doesn't created")



