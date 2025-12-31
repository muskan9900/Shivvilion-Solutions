""" creating threads with Thread class """
""" using class methods, static methods for execution of threads """

from threading import Thread, current_thread

# class Example:

#     def display(self,n):
#         print("class thread details:",current_thread().name)
#         for i in range(n):
#             print("class thread")

# e1=Example()

# creating a thread with thread class using Example class methods
# method of example class is used in the t1 object 
# we need a reference of Example class to use the methods in Thread class
# t1=Thread(target=e1.display,args=(5,))
# t1.start()

#----- main thread----#
# for i in range(5):
#     print("main thread")
#     print("Main thread details:",current_thread().name)

#------ using class method----#

# class Example:

#     @classmethod
#     def display(self,n):
#         print("class thread details:",current_thread().name)
#         for i in range(n):
#             print("class thread")

# e1=Example()

# creating a thread with thread class using Example class methods
# method of example class is used in the t1 object 
# we need a reference of Example class to use the methods in Thread class
# as using class method use Example class as reference
# t1=Thread(target=Example.display,args=(5,))
# t1.start()

# for i in range(5):
#     print("main thread")
#     print("Main thread details:",current_thread().name)


# ----- using static method -----#

class Example:

    @staticmethod
    def display(n):
        print("class thread details:",current_thread().name)
        for i in range(n):
            print("class thread")

e1=Example()

t1=Thread(target=e1.display,args=(5,))
t1.start()

for i in range(5):
    print("main thread")
    print("Main thread details:",current_thread().name)
