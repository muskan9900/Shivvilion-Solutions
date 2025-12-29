""" handling exceptions when closing a file """
# exceptions are handled with try and finally keyword 
#  finally keyword is responsible for the operation in files even if error occurs 

# in the following example the finally block ensures the file is closed even if their is error

try:
    file=open("geek.txt",'r')
    content=file.read()
    print(content)

finally:
    file.close()
    print("is closed:",file.closed)

