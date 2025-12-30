"""using the current_thread()"""
""" using attributes of Thread class"""
""" working on main thread"""

import threading
# if no explicit thread is created by default it is the main thread
print(threading.current_thread())
# it has .name attribute of the thread class,
# returns the name of the thread
print(threading.current_thread().name)
# it returns the id of the thread
print(threading.current_thread().ident)
# to check the status of the current working thread
# using is_alive()
# returns boolean value 
print(threading.current_thread().is_alive())
