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
    'NumberVector',
    'StringVector',
    'StringDictionary',
    'DictionaryVector',
    'NumberVectorAlike',
    'NumberArrayAlike',
    'AnyArrayAlike',
    'AnyVectorAlike',
    'AnyType',
    Meta,
]

# all available types.
__types__ = [
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
__metaclass__ = [
    Meta,
]