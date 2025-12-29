""" reading a file  """

file=open("geek.txt",'r')
content=file.read()
print(content)
file.close()