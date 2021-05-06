from functools import lru_cache
import time
from time import time_ns


@lru_cache(maxsize=None)
def s(n):
    if n <= 1:
        return 1
    else:
        new = s(n - 1) + s(n - 2)
        return new


# 1 1 2 3 5 8 13
def run():
    global e
    t = time_ns()
    for i in range(selected):
        e = str(s(i))
    print('DONE')
    print(e)
    elapsed_time = time_ns() - t
    print(elapsed_time)


selected = int(input('n = ?'))
run()
time.sleep(60)
