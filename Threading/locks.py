""" locking mechanism in python """

from threading import *
from time import sleep 
# step-1 
mylock=Lock()
# to avoid race condition we use lock class
def task(mylock,msg):
# acquire method will lock the thread until it finishes its job
    mylock.acquire()
    for i in range(5):
        print(msg)
    sleep(3)
# this release the the locked state of thread to unlocked  
    mylock.release()

t1=Thread(target=task,args=(mylock,'hello world'))
t2=Thread(target=task,args=(mylock,'welcome'))
t1.start()
t2.start()