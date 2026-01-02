""" need of Rlock """

from threading import *
from time import sleep
l=RLock()
# if only lock class is used it wont wont work

def get_first_line():
    l.acquire()
    nm=current_thread().name
    print(nm)
    print("code for fetching first line")
    l.release()

def get_second_line():
    l.acquire()
    nm=current_thread().name
    print(nm)
    print("code for fetching second line")
    l.release()

def main():
    l.acquire()
    get_first_line()
    get_second_line()
    l.release()

t1=Thread(target=main)
# t2=Thread(target=get_first_line)
t1.start()
# t2.start()