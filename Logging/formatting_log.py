""" formatting logs in python """
""" how to change format of log messages """
""" how to add date and time in log messages """

from logging import *

# some functions in logging to display messages 

# using basicConfig() to change levels
# by default filename has append mode
# basicConfig(filename='app.log',level=DEBUG)

# we can also change the mode 
basicConfig(filename='app.log',
            level=DEBUG,
            filemode='w',
            format=)




# debug()
debug("this is a debug message")
# info()
info("module 2 got completed")
# warning()
warning("the warning mesaage is displaying")
# error()
error("the error message is displaying")
# critical()
critical('the critical message is displaying')