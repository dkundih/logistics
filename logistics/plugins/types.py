# dependencies import.
from typing import Dict, List, Union

# prototype.
VandalType = 'Specific Input / Output vandal type of supported data.'

# generic types.
IntegerType: VandalType = int # integer.
FloatType: VandalType = float # float.
NumberType: VandalType = Union[IntegerType, FloatType] # both floats and integers supported.
ReturnType: VandalType = object # basic return object or empty return.
PrintType: VandalType = str # print function as an output.
GraphType: VandalType = object # graph return.
StringType: VandalType = str # string.
ListType: VandalType = list # list.
TupleType: VandalType = tuple # tuple.
DictionaryType: VandalType = dict # dictionary.
BooleanType: VandalType = bool # bool.
FilePathType: VandalType = 'File path.' # file path.
SpecialType: VandalType = 'Special data type that does not fit in any of the categories.' # data type that does not fit in any of the categories.

# structured types.
NumberVector: VandalType = List[float] # one-dimensional vector of integers or floats.
StringVector: VandalType = List[str] # one-dimensional vector of strings.
StringDictionary: VandalType = Dict[str, str] # one-dimensional 'str' : 'str' dictionary vector.
DictionaryVector: VandalType = Dict[str, NumberVector] # one-dimensional 'str' : 'NumberVector' dictionary.

# complex types.
NumberVectorAlike: VandalType = Union[NumberVector, DictionaryVector] # only number-supported list/vector of values.
NumberArrayAlike: VandalType = Union[List[NumberVector], List[DictionaryVector]] # array of numerical values only.
AnyArrayAlike: VandalType = Union[List[NumberVector], List[StringVector], List[StringDictionary], List[DictionaryVector]] # any =>2 dimensional type.
AnyVectorAlike: VandalType = Union[NumberVector, StringVector, StringDictionary, DictionaryVector] # any one-dimensional type.
AnyType: VandalType = Union[IntegerType, FloatType, NumberType, StringType, ListType, TupleType, DictionaryType, NumberVector, StringVector, StringDictionary, DictionaryVector, NumberVectorAlike, NumberArrayAlike, AnyVectorAlike, AnyArrayAlike] # any type.

# all available types.
def VandalTypes():
    info = [
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
]
    return info
