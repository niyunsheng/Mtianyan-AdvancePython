import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
#多进程编程
#耗cpu的操作，用多进程编程， 对于io操作来说， 使用多线程编程，进程切换代价要高于线程

#1. 对于耗费cpu的操作，多进程由于多线程
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    # 多进程
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25,35)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            # print("exe result: {}".format(data))
        print("last time is: {}".format(time.time()-start_time))
    # 多线程
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25,35)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            # print("exe result: {}".format(data))

        print("last time is: {}".format(time.time()-start_time))