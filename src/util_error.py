from util_class import CLASSINIT,DOCUMENTATION,ERROR

class ERRORMODULE(object):
    """
    A custom error handling class designed to manage and raise errors in a structured manner.

    Attributes:
        error (Exception): A default error stored in the instance, set to NotImplementedError.

    Methods:
        __str__: Returns a string representation of the error module.
        __call__: When called, returns the default error.
        __getstate__: Raises the default error, used in serialization scenarios.
        __repr__: Returns the documentation of the class.
        Default (property): A property that, when accessed, raises the default error.
        Manuel: A method for manually raising specified errors with custom messages.
    """
    def __init__(self)->CLASSINIT:
        self.error = NotImplementedError(NotImplemented)
    def __str__(self)->str:
        return "Error Module - Sub(Script)"
    def __call__(self)->ERROR:
        return self.error
    def __getstate__(self)->ERROR:
        raise self.error
    def __repr__(self)->DOCUMENTATION|str:
        return ERRORMODULE.__doc__
    @property
    def Default(self)->ERROR:
        raise self.error
    def Manuel(self,errorType:ERROR,errorMessage:str)->ERROR:
        raise errorType(errorMessage)
        