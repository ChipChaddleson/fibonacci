from functools import lru_cache
from time import time_ns


@lru_cache(maxsize=None)
def s(n):
    if n <= 1:
        return 1
    else:
        new = s(n - 1) + s(n - 2)
        return new


def run():
    t = time_ns()
    for i in range(7000):
        print(str(s(i)))
    print('DONE')
    elapsed_time = time_ns() - t
    print(elapsed_time)


run()
