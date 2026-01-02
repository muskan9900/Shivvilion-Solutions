""" Rlocks  """
# modified version of locks
# allows you  to use acquire() multiple times
 
from threading import *
from time import sleep

l=RLock()
class Bus:
    def __init__(self,name,available_seats,lock):
        self.available_seats=available_seats
        self.name=name
        self.lock=lock
    def reserve(self,need_seats):
        self.lock.acquire()
        self.lock.acquire()
        print("Available seats are:",self.available_seats)
        if self.available_seats>=need_seats:
            nm=current_thread().name
            #code
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("no seats are available")
        self.lock.release()
        self.lock.release()

B1=Bus("Mahalakshmi travels",2,l)
t1=Thread(target=B1.reserve,args=(2,), name="Jay")
t2=Thread(target=B1.reserve,args=(1,),name="Raj")
t1.start()
t2.start()