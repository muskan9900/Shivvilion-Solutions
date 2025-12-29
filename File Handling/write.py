""" write handling """
#  it uses with statement which automatically closes the file
# 'w' mode creates a file if it doesnt exist 
# it overwrites if the file exist 
# the write() is used to add content 
#  a file must be closed if opened 

with open("geek.txt","w") as file:
    file.write("hello, Python!\n")
    file.write("file handling is easy with python.")
print("file is written successfully")


