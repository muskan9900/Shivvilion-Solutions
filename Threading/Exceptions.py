""" Exception in multi threading """

import threading 
from time import sleep 

# if exception occurs from main thread -> sys.excepthook() is called
# if exception occurs from thread created -> threading.excepthook()
# threading.excephook()-> has 4 arguments in tuple

# defining a custom_hook exception 
def custom_hook(args):
    # args are the arguments from the threading.excepthook()
    print("Exception occurred in thread")
    print(args[0])# exception name
    print(args[1])# message 
    print(args[2])# object traceback
    print(args[3]) # thread details 

# this function contains exception
def display():
    for i in range(4):
        sleep(0.1)
        print("hello"+10)

def show():
    for i in range(4):
        print("hello")
        sleep(0.5)

# this is responsible to catch exception where exception occurs
threading.excepthook=custom_hook
# creating threads
t1=threading.Thread(target=display)
t2=threading.Thread(target=show)
t1.start()
t2.start()

