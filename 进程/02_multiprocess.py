"""
创建普通进程
"""
from multiprocessing import Process
import os

def run_proc(name):
    print("Run child %s is %s" % (name, os.getpid()))


if __name__ == "__main__":
    print("Parent Process %s" % os.getpid())
    p = Process(target=run_proc, args=("test",))
    p1 = Process(target=run_proc, args=("test1",))
    print("Child process will start")
    p.start()
    p.join()
    p1.start()
    p1.join()
    print("Child process end.")


"""
注意事项:
1. target是一个函数的名字,不是字符串
"""