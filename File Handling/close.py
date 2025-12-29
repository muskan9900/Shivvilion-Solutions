""" closing a file  """

f=open("geek.txt",'r')
# performing file operations
f.close()
# f.closed returns true if file is closed and false if not 
print("is closed:",f.closed)
