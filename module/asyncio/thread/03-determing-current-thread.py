# Using arguments to identify or name the thread is cumbersome, and unnecessary. Each Thread instance has a name with a default value that can be changed as the thread is created. Naming threads is useful in server processes with multiple service threads handling different operations.

import threading
import time

def worker():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(), 'Exiting')

def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(3)
    print(threading.current_thread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()
