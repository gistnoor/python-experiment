# It useful to be able to spawn a thread and pass it arguments to tell it what work to do. This example passes a number, which the thread then prints.

import threading

def worker(num):
    """thread worker function"""
    print("worker : {}".format(num))
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)
    t.start()
