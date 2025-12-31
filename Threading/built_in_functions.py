""" built in function in threads """
# ----- list of built in function----#
# 1.) is_alive():- checks thread is running or not
# 2) main_thread():- Returns main threads details
# 3) active_count():- Number of running threads
# 4) enumerate():- List of all running threads with details
# 5) get_native_id():- to know native id of thread

# the following example explains well

from threading import Thread,main_thread,active_count,enumerate,get_native_id
import os
def display():
# now using main_thread() , need to import it
# main_thread is used to print the details of main thread
# if we use current_thread inside the function it prints the details of t1 thread becuase its the current thread
    print("main thread deatils:",main_thread())
    for i in range(4):
        print("hello world")

def show():
    for i in range(3):
        print("hi")

t1=Thread(target=display)
print("before start:",t1.is_alive()) 
t1.start()
print("the t1 thread TID",t1.ident)
print("the t1 Native ID",t1.native_id)# print native id of thread t1
# get_native_id returns the native id of main thread
print("the main thread native_id",get_native_id())
# we need to also import active_count()
print("number of threads:",active_count())
# enumerate function
# this returns the list of threads present in the process
print("list of threads:",enumerate())
# is_alive() method checks thread is running or not
print("after start:",t1.is_alive())
print("the process ID is:",os.getpid())


