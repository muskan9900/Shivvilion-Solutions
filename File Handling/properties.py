""" properties of files  """

f=open("geek.txt",'r')
# f.name is used for name of the file 
print("filename:",f.name)
# f.mode it prints which mode the file is in 
print("Mode:",f.mode)
# f.closed returns true if closed and returns false if not 
print("Is closed?",f.closed)
f.close()
print("Is closed?",f.closed)