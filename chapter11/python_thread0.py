#对于io操作来说，多线程和多进程性能差别不大
#1.通过Thread类实例化
import time
import threading

def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")

if  __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html,args=("",))
    thread2 = threading.Thread(target=get_detail_url,args=("",))
    # thread1.setDaemon(True)
    thread2.setDaemon(True) # 主线程退出时强制退出thread2
    start_time = time.time()
    thread1.start() # 启动线程，主线程和两个线程时并行的
    thread2.start()

    thread1.join() # 阻塞线程，等待thread1执行完毕
    thread2.join() # 阻塞线程

    #当主线程退出的时候， 子线程kill掉
    print ("last time: {}".format(time.time()-start_time))