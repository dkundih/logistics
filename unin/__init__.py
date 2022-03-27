'''

NOTE: unin library runs on top of the vandal library, in order to see more about the actual code visit the vandal library repositories at:
	https://github.com/dkundih/vandal
    https://pypi.org/project/vandal

unin - University North library that runs on top of the vandal library.
=====================================================================

This is a connection to the main folder of the unin library.

'''

#ignore __pycache__ from forming inside the library directory.
import sys
sys.dont_write_bytecode = True

#meta data imports from the unin library.
from unin.misc._meta import (
    __author__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __documentation__,
    __contact__,
    __donate__,
)

#object and module imports.
from vandal import *
from duality import *
