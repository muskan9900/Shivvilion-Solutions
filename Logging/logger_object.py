""" logger object """
""" how to do logging  with logger object"""

from logging import *

basicConfig(filename='object.log',filemode='w',
            format="%(name)s:%(levelname)s:%(message)s")

# getLogger() creates the logger object 
# we can also change the name of name:(logger name)
logger=getLogger("PYTHON")

# similar way to print the methods but with object

# level can be set by logger object by setLevel()
logger.setLevel(10)
logger.info("here is the information")
logger.error("error message goes here")
