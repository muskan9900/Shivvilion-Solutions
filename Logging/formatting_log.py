""" formatting logs in python """
""" how to change format of log messages """
""" how to add date and time in log messages """

from logging import *

# some functions in logging to display messages 

# using basicConfig() to change levels
# by default filename has append mode
# basicConfig(filename='app.log',level=DEBUG)

# we can also change the mode 
# we can also change the logger message format
# by default it is levelname:name(logger name):message
# by using format argument we can change log formats 
basicConfig(filename='app.log',
            level=DEBUG,
            filemode='w',
            format="%(asctime)s:%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s",
            datefmt='%d-%b-%y %M:%H:%S')
            # style="{")

# style="{" this is used change the style of format 
# datefmt='%d-%b-%y %M:%H:%S' this is used to change the format of date and time 


# %(process)s this placeholder prints the process id of log
# we can also get the line number in log by using %(lineno)s
# eg we want name(loggername):levelname:message


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