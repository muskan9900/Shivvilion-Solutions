""" methods of creating threads"""
"""method 1 : by using threading module which conatins the Thread class
method 2 : by extending the Thread class using inheritance"""

# using method 1
# step 1 import thread class
from threading import Thread,current_thread

# step 2 create a function conataining code to be executed parallaly
# def display():
#     for i in range(4):
#         print("hello word")

# # step 3 creating threads
# # Thread class is already imported 
# # create object using Thread class

# t1=Thread(target=display)
# till t1 as object the main thread is considered

# # step 4 starting the thread 
# here  the next thread t1 is created after main thread
# main thread is the parent thread that creates another threads
# t1.start()
# #  printing the details of threads using attributes 
# print(t1.name)
# print(t1.ident)

# same with user arguments 

def display(n,msg):
    print("t1 thread details:",current_thread())
    for i in range(n):
        print(msg)

# step 3 creating threads
# Thread class is already imported 
# create object using Thread class

# t1=Thread(target=display, args=(4,"hello world"))
# for single arguments use args=(4,)
# include comma or else it throws type error 
# use tupel

# using kwargs
# use dict
t1=Thread(target=display, kwargs={'n':4,'msg':'t1 thread'})

# step 4 starting the thread  
t1.start()
#  printing the details of threads using attributes 
# print(t1.name)
# print(t1.ident)


####### a more  clear way to get which threads what code #########
for i in range (4):
    print("main thread")













