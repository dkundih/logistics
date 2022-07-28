# type hints and annotations.
from logistics.plugins.types import *

# package.
class Meta(type):

    '''
    * makes multiple instances of the object available.
    '''

    def __call__(
        self, 
        *args, 
        **kwargs,
        ) -> ReturnType:
        instance = super(Meta, self).__call__(*args, **kwargs)

        return instance

    def __init__(
        self, 
        name, 
        base, 
        attr,
        ) -> ReturnType:
        super(Meta, self).__init__(name, base, attr)
