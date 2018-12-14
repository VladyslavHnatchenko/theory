import hashlib
import cProfile
# from python_scripts import ptest
import ptest


cProfile.run("ptest.main()")

# cProfile.run("hashlib.md5(b'abcdefghijkl').digest()")

# import pstats
# p = pstats.Stats("output.txt")
# p.strip_dirs().sort_stats(-1).print_stats()