from threading import Lock, RLock, Condition #可重入的锁

total = 0
lock = RLock()
# RLcok是可以重入的锁，在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等
def add():
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        # lock.acquire() # 这段代码如果用Lock()会死锁，必须释放了才能继续acquire
        dosomething()
        lock.release()
def dosomething():
    global lock
    global total
    lock.acquire()
    total += 1
    lock.release()
def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()


thread1.join()
thread2.join()
print(total)

#1. 用锁会影响性能
#2. 锁会引起死锁
#死锁的情况 A（a，b）
"""
A(a、b)
acquire (a)
acquire (b)

B(a、b)
acquire (a)
acquire (b)
"""

