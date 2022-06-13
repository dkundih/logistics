'''

logistics - vandal framework logistics package.
=====================================================================

This is a connection to the __init__ file of the vandal library.

AVAILABLE FEATURES IN THE LIBRARY:

    TYPES (TYPE OBJECTS MODULE)
    --------------------------
    set of available type objects in a module.
        print(help(logistics.plugins.types)) in order to see the function details.

    Meta (OBJECT)
    -------------------
    logistics.Meta is an object that makes object cloning possible.
        print(help(logistics.Meta)) in order to see available features.

'''

# ignore __pycache__ from forming inside the library directory.
import sys
sys.dont_write_bytecode = True

# meta data imports from the vandal library.
from logistics.misc._meta import (
    __author__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __documentation__,
    __contact__,
    __donate__,
)

# plugin types.
from logistics.plugins.types import (
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    FilePathType,
    SpecialType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
    AnyType,
)

# imports relevant contents.
from logistics.plugins.metaclass import Meta

# all relevant contents.
__all__ = [
    'VandalType',
    'IntegerType',
    'FloatType',
    'NumberType',
    'ReturnType',
    'PrintType',
    'GraphType',
    'StringType',
    'ListType',
    'TupleType',
    'DictionaryType',
    'BooleanType',
    'FilePathType',
    'SpecialType',
    'NumberVector',
    'StringVector',
    'StringDictionary',
    'DictionaryVector',
    'NumberVectorAlike',
    'NumberArrayAlike',
    'AnyArrayAlike',
    'AnyVectorAlike',
    'AnyType',
    'Meta',
]

# all available types.
types = [
    VandalType,
    IntegerType,
    FloatType,
    NumberType,
    ReturnType,
    PrintType,
    GraphType,
    StringType,
    ListType,
    TupleType,
    DictionaryType,
    BooleanType,
    FilePathType,
    SpecialType,
    NumberVector,
    StringVector,
    StringDictionary,
    DictionaryVector,
    NumberVectorAlike,
    NumberArrayAlike,
    AnyArrayAlike,
    AnyVectorAlike,
    AnyType,
]

# metaclass.
metaclass = [
    'Meta',
]