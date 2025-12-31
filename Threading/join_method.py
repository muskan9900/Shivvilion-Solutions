""" join_method """
# if a thread wants to wait for some other thread, then we should go for join()method
#  join method is a thread class method , need to be called by object 

# example shown below
from threading import Thread

def display():
    for i in range(5):
        print("welcome")

def show():
    for i in range(5):
        print("let's start the program")


t1=Thread(target=display)
t2=Thread(target=show)
t1.start()
# t1.join()# this means let t1 finishe its execution 
# then start t2
t2.start()
t2.join() # similar way let t2 finish then let the main thread execute

# main thread #
for i in range(5):
    print("hello world")