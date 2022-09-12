import sys
import time
import math

def ft_progress(lst):
    start = time.time()
    for i in range(len(lst)):
        elapsed = time.time() - start
        percent = i / len(lst) * 100
        eta = (len(lst) - i) * elapsed / (i + 1)
        bar = math.floor(percent / 5)
        print("\rETA: %.2fs [%d%%][%s%s] %d/%d | elapsed time %.2fs" % (eta, percent+1, "=" * bar + ">", " " * (20 - bar - 1), i+1, len(lst), elapsed), end="")
        yield lst[i]
    print()

if __name__ == '__main__':
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
    # listy = range(3333)
    # ret = 0
    # for elem in ft_progress(listy):
    #     ret += elem
    #     time.sleep(0.005)
    # print()
    # print(ret)

