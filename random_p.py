import random
import timeit


_sysrand = random.SystemRandom()


def prng() -> None:
    random.randint(0, 95)


def csprng() -> None:
    _sysrand.randint(0, 95)


setup = 'import random; from __main__ import prng, csprng'

if __name__ == '__main__':
    print('Best of 3 trials with 1,000,000 loops per trial:')

    for f in ('prng()', 'csprng()'):
        best = min(timeit.repeat(f, setup=setup))
        print('\t{:8s} {:0.2f} seconds total time.'.format(f, best))


# import string
# import random
#
#
# def unique_strings(k: int, ntokens: int,
#                    pool: str=string.ascii_letters) -> set:
#     seen = set()
#     while len(seen) < ntokens:
#         token = ''.join(random.choices(pool, k=k))
#         seen.add(token)
#     return seen


# class NotSoRandom(object):
#     def seed(self, a=3):
#         """The most mysterious random number generator in the world."""
#         self.seedval = a
#
#     def random(self):
#         """See, random numbers!"""
#         self.seedval = (self.seedval * 3) % 19
#         return self.seedval
#
#
# _inst = NotSoRandom()
# seed = _inst.seed
# random = _inst.random
