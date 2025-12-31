""" configuring thread name """
""" Threading identity numbers """

from threading import Thread, current_thread
import os

def display():
    for i in range(4):
        print("hello world")

def show():
    for i in range(3):
        print("welcome")

t1=Thread(target=display)
t2=Thread(target=show)
# changing the thread name by following the statement
t1.start()
t1.name="XYZ"
print(t1.name)
# getting the name
print(t1.name)
print(t2.name)
# getting the thread and native ids
print(t1.ident)
print(t1.native_id)

# ---- naming main thread----#
current_thread().name="ABCmain"
print(current_thread().name) 
print(os.getpid())

# another way to get name is by getName() but not used or being to be deprecation
# print(t1.getName())
# by using setName() we can change name but its deprecated 

""" thread identifiers """

# thread identifier assigned by process
# Native identifier assigned by OS 

# ----- thread indentifier----#
# thread identifier: unique identifier within a python process
# assigned by the python interpreter 
# read -only positive integer and unique in process
# assigned after starting thread
#  the identifier is stored in an instance variable:- ident

# ----- native identifiers-----#
# each thread has a unique identifier assigned by the operating system 
# property  name:- native_id (assigned after threads has started)

# ----note:---#
# generally ident and native_id are same with values
# but are completely different identifiers

# ---- PID----#

# identifiers for process(program)
# used by importing OS Module and getpid()