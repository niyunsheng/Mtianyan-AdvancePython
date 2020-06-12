# import os
# #fork只能用于linux/unix中
# pid = os.fork() # fork是复制进程，将父进程的全部数据和程序拷贝到子进程
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))

import multiprocessing

#多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


if __name__ == "__main__":
    # 单进程
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    #使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3,))
    result = pool.apply_async(get_html, args=(1,))
    
    #等待所有任务完成
    pool.close() # 进程池不再接受新的进程
    pool.join() # 阻塞同步

    print(result.get(),result.get())

    #imap
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))
