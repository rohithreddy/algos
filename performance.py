## Useful boiler plate code to test performance of algorithms
from bArrSearch import bs_contains
from time import time
def performance():
    n = 1024
    while n < 50000000:
        sorted = range(n)
        before = time()
        bs_contains(sorted, n + 1)
        done = time()
        print n, (done - before) * 1000
        n *= 2


if __name__ == "__main__":
    performance()
