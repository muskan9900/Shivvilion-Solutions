""" semaphore """
"""
# semaphore allow us to use paticular number of threads at once 
# in lock and Rlock only one thread is allowed to perform at a time
# semaphore can be used to limit the access to the shared resources wih limited capacity
"""

from threading import *
from time import sleep

# creating semaphore object
s=Semaphore(2)
# using acquire and release methods 
# semaphore has inbuilt Rlock (multiple times using acquire() and release())

def display(name):
    # calling acquire method
    # acquire= decrement by one
    s.acquire()
    for i in range(1,5+1):
        print('Hello')
        print(name)
        sleep(0.5)
    # calling release method
    s.release()
    # release= increment by one

# creating multiple 
t1=Thread(target=display,args=("Thread-1",))
t2=Thread(target=display,args=("Thread-2",))
t3=Thread(target=display,args=("Thread-3",))
t4=Thread(target=display,args=("Thread-4",))
t5=Thread(target=display,args=("Thread-5",))

# calling the threads 
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# bounded semaphore is used when unequal count happens 
# like aqcuire is one and 2 release are there this shows uneven flow,when such conditions occurs and to avoid them use bounded semaphore