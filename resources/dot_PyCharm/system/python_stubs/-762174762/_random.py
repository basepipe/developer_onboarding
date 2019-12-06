# encoding: utf-8
# module _random
# from (built-in)
# by generator 1.147
""" Module implements the Mersenne Twister random number generator. """
# no imports

# no functions
# classes

class Random(object):
    """ Random() -> create a random number generator with its own internal state. """
    def getrandbits(self, k): # real signature unknown; restored from __doc__
        """ getrandbits(k) -> x.  Generates a long int with k random bits. """
        pass

    def getstate(self): # real signature unknown; restored from __doc__
        """ getstate() -> tuple containing the current state. """
        return ()

    def jumpahead(self, p_int): # real signature unknown; restored from __doc__
        """ jumpahead(int) -> None.  Create new state from existing state and integer. """
        pass

    def random(self): # real signature unknown; restored from __doc__
        """ random() -> x in the interval [0, 1). """
        pass

    def seed(self, n=None): # real signature unknown; restored from __doc__
        """ seed([n]) -> None.  Defaults to current time. """
        pass

    def setstate(self, state): # real signature unknown; restored from __doc__
        """ setstate(state) -> None.  Restores generator state. """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


