# encoding: utf-8
# module _lsprof
# from (built-in)
# by generator 1.147
""" Fast profiler """
# no imports

# no functions
# classes

class Profiler(object):
    """
    Profiler(timer=None, timeunit=None, subcalls=True, builtins=True)
    
        Builds a profiler object using the specified timer function.
        The default timer is a fast built-in one based on real time.
        For custom timer functions returning integers, timeunit can
        be a float specifying a scale (i.e. how long each integer unit
        is, in seconds).
    """
    def clear(self): # real signature unknown; restored from __doc__
        """
        clear()
        
        Clear all profiling information collected so far.
        """
        pass

    def disable(self): # real signature unknown; restored from __doc__
        """
        disable()
        
        Stop collecting profiling information.
        """
        pass

    def enable(self, subcalls=True, builtins=True): # real signature unknown; restored from __doc__
        """
        enable(subcalls=True, builtins=True)
        
        Start collecting profiling information.
        If 'subcalls' is True, also records for each function
        statistics separated according to its current caller.
        If 'builtins' is True, records the time spent in
        built-in functions separately from their caller.
        """
        pass

    def getstats(self): # real signature unknown; restored from __doc__
        """
        getstats() -> list of profiler_entry objects
        
        Return all information collected by the profiler.
        Each profiler_entry is a tuple-like object with the
        following attributes:
        
            code          code object
            callcount     how many times this was called
            reccallcount  how many times called recursively
            totaltime     total time in this entry
            inlinetime    inline time in this entry (not in subcalls)
            calls         details of the calls
        
        The calls attribute is either None or a list of
        profiler_subentry objects:
        
            code          called code object
            callcount     how many times this is called
            reccallcount  how many times this is called recursively
            totaltime     total time spent in this call
            inlinetime    inline time (not in further subcalls)
        """
        return []

    def __init__(self, timer=None, timeunit=None, subcalls=True, builtins=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class profiler_entry(object):
    # no doc
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    callcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this was called"""

    calls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """details of the calls"""

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """code object or built-in function name"""

    inlinetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inline time in this entry (not in subcalls)"""

    reccallcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times called recursively"""

    totaltime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total time in this entry"""


    n_fields = 6
    n_sequence_fields = 6
    n_unnamed_fields = 0


class profiler_subentry(object):
    # no doc
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    callcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this is called"""

    code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """called code object or built-in function name"""

    inlinetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inline time (not in further subcalls)"""

    reccallcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """how many times this is called recursively"""

    totaltime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total time spent in this call"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


