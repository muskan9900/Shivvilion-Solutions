""" threading in python  """

# step 1 import thread module
import threading
# import time module
import time 

# program code or instructions
def square(num):
    print(f"square:{num*num}")
    time.sleep(1)

def cube(num):
    print(f"cube:{num*num*num}")
    time.sleep(1)

# step 2 creating a threads 
t1=threading.Thread(target=square,args=(4,))
t2=threading.Thread(target=cube,args=(4,))

# step 3 starting threads 
t1.start()
t2.start()
# step 4 wait for completion
t1.join()
t2.join()

print("Done")
