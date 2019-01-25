from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print("写的进程:%s" % os.getpid())
    for value in ["A", "B", "C", "D"]:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print("读的进程:%s" % os.getpid())
    while True:
        value = q.get(True)
        print("GET %s from queue." % value)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
