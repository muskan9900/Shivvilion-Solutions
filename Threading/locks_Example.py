# this code has race condition
# to avoid this we are using locks by lock class

from threading import *
from time import sleep
lock=Lock()
class Bus:
    def __init__(self,name,available_seats,l):
        self.available_seats=available_seats
        self.name=name
        self.l=l
    def reserve(self,need_seats):
        self.l.acquire() 
        print("Available seats are:",self.available_seats)
        if self.available_seats>=need_seats:
            nm=current_thread().name
            #code
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("no seats are available")
        self.l.release()
B1=Bus("Mahalakshmi travels",2,lock)
t1=Thread(target=B1.reserve,args=(1,), name="Jay")
t2=Thread(target=B1.reserve,args=(2,),name="Raj")
t1.start()
t2.start()