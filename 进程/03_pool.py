"""
通过线程池创建子进程
"""
from multiprocessing import Pool
import os, time, random


def long_time_run(name):
    print("run task %s  (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("task %s runs %0.2f seconds" % (name, (end - start)))


if __name__ == "__main__":
    print("Parent Process is %s" % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_run, args=(i,))
    print("Waiting for all subprocesses done..")
    p.close()
    p.join()
    print("All subprocess done...")


"""
注意事项:
1. Pool类默认人cpu的核数
"""