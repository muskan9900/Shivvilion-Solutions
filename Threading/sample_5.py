""" creating threads by extending thread class """

from time import sleep
from threading import Thread

videos=['OOP Syllabus','constructor','destructor','file handling']

# t1 will hand this program 
class MyThread(Thread):
# using constructor in this class
    def __init__(self,val):
        print("constructor called")
        # creating instance variable
        self.kids=val
        # we will use super()
        # reference of  that means constructor of thread class
        Thread.__init__(self)

# creating a methods 
    def compression(self):
        print("video compression code")
# overriding the methods from the Thread class
    def run(self):
    # creating some variables and assigning values
        a=10
        b=40
    #  using the compression()
        self.compression()
    # using a condition for checking if suitable for kids or not
        if self.kids is True:
            print("suitable for kids")
        
        else:
            print("not suitable for kids")

        for vid in videos:
            print(f"{vid} started uploading....")
            sleep(1)
            print(f"{vid} uploaded.....")
        self.temp=a+b
# creating new threads
t1=MyThread(False)
t1.start()
# this shows error because before the run() executes ,
# the main thread calls this line before t1 thread does 
# to avoid this we will use sleep(10)
sleep(10)
print(t1.temp)
# for main thread
for i in range(4):
    sleep(0.5)
    print("checking copyrights")