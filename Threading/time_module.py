""" using time module to check how much time is required for each thread to be executed """
""" difference between single threading and multi threading """
# example demonstrated

from threading import Thread
import time
def square(num):
    print("finding square.....")
    time.sleep(2)
    print(f"the square of{num}:",num**2)

def cube(num):
    print("finding cube.....")
    time.sleep(2)
    print("the cube of {num}:",num**3)
begin=time.time()
t1=Thread(target=square,args=(3,))
t2=Thread(target=cube,args=(3,))
t1.start()
t2.start()
print("the total time taken is:", time.time()-begin)

