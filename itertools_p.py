from itertools import islice, count
from itertools import cycle
from itertools import repeat
from itertools import accumulate
from itertools import chain
from itertools import compress
from itertools import dropwhile
import operator


data = list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
print(data)

# letters = 'ABCDEFG'
# bools = [True, False, True, True, False]
#
# data = list(compress(letters, bools))
# print(data)

# numbers = list(range(5))
# cmd = ['ls', '/some/dir']
#
# data = list(chain.from_iterable([cmd, numbers]))
# print(data)

# numbers = list(range(5))
# cmd = ['ls', '/some/dir']
#
# my_list = list(chain(['foo', 'bar'], cmd, numbers))
#
# print(my_list)

# result = list(accumulate(range(1, 5), operator.mul))
# print(result)

# result = list(accumulate(range(10)))
# print(result)

# iterator = repeat('test', 5)

# polys = ['triangle', 'square', 'pentagon', 'rectangle']
# iterator = cycle(polys)

# count = 0
# for item in cycle("XYZ"):
#     if count > 7:
#         break
#     print(item)
#     count += 1


# for i in islice(count(10), 5):
#     print(i)


# from itertools import count
#
#
# for i in count(10):
#     if i > 20:
#         break
#     else:
#         print(i)
