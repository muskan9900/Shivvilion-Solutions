""" Race condition """
# example demonstrated:- bus ticketing system 
# race conditions:
# race conditions are bugs occurred when multiple thread try to access a resource concurrently
# this gives unreliable output
from threading import *

class Bus:
    def __init__(self,name,available_seats):
        self.available_seats=available_seats
        self.name=name
    def reserve(self,need_seats):
        print("Available seats are:",self.available_seats)
        if self.available_seats>=need_seats:
            nm=current_thread().name
            #code
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("no seats are available")

B1=Bus("Mahalakshmi travels",2)
t1=Thread(target=B1.reserve,args=(1,), name="Jay")
t2=Thread(target=B1.reserve,args=(2,),name="Raj")
t1.start()
t2.start()
#---- to avoid race conditiond-----#
# locks 
# rlocks
# semaphore 
# this techniques are used