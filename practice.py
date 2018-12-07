# List comprehension
# Генераторы списков
# names = ['jack', 'john', 'oleg', 'ula']
#
# # new_names = [n for n in names if n.startswith('j')]
# # print(new_names)
#
# new_names = []
# for n in names:
#     if n.startswith('j'):
#         new_names.append(n)
#
# print(new_names)
# jack = {
#     'name': 'jack',
#     'car': 'bmw'
# }
#
# john = {
#     'name': 'john',
#     # 'car': 'audi'
# }
#
# users = [jack, john]
#
# # cars = [person['car'] for person in users]
# # print(cars)
# # cars = []
# # for person in users:
# #     cars.append(person['car'])
#
# new_cars = [person.get('car', '') for person in users]
# # new_cars = [person['car'] for person in users]
# print(new_cars)
# print(cars)
# some_list = [1, 2]
# things = [x for x in some_list]

# a = '123'
#
#
# def add():
#     pass
#
#
# print(globals())

# def add(a, *args):
#     print(a)
#     print(args)
#     print(sum(args))
#
#
# List1 = [1, 2, 3]
# add(*List1)

# def add(a, b, c):
#     print(a + b + c)
#
#
# add(2, 3, 4)

# import socket
# import sys
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = "127.0.0.1"
# port = 8007
#
#
# s.bind((host, port))
# s.listen(1)
# conn, addr = s.accept()
# data = conn.recv(1000000)
# print("client is at", addr, data)
# conn.send(data)
# z = input()
# conn.close()


# import socket
# import sys
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = "localhost"
# port = 8007
# s.connect((host, port))
# s.send("Hello")
# data = s.recv(1000000)
# print("received", data, len(data), "bytes")
# s.close()
