""" creating logging """
# steps to use logging
# import the logging module

from logging import *

# some functions in logging to display messages 

# using basicConfig() to change levels
basicConfig(filename='app.log',level=DEBUG)
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

#==== logging concepts====#

# logging has level 
# debug() has 10 
# info() has 20

# messages are print from warning() by default
# warning () has 30
# error() has 40
# critical() 50 
""" #  to include other level we need to use basicConfig()
    this methods has a parameter which has levels to be printed 
 
    format of log message:
    WARNING:root:the warning mesaage is displaying
    # warning: is the level
    #root: is the logger name
    # "the warning mesaage is displaying" -> is the message
    level:logger name:message

    === to log messages into log file====
    # use the basicConfig() method
    # use parameter as filename="app.log"



 """