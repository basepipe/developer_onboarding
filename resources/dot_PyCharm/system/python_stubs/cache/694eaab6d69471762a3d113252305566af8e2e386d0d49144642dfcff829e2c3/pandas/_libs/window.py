# encoding: utf-8
# module pandas._libs.window
# from C:\Python27\lib\site-packages\pandas\_libs\window.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# functions

def ewma(*args, **kwargs): # real signature unknown
    """
    Compute exponentially-weighted moving average using center-of-mass.
    
        Parameters
        ----------
        vals : ndarray (float64 type)
        com : float64
        adjust: int
        ignore_na: int
        minp: int
    
        Returns
        -------
        y : ndarray
    """
    pass

def ewmcov(*args, **kwargs): # real signature unknown
    """
    Compute exponentially-weighted moving variance using center-of-mass.
    
        Parameters
        ----------
        input_x : ndarray (float64 type)
        input_y : ndarray (float64 type)
        com : float64
        adjust: int
        ignore_na: int
        minp: int
        bias: int
    
        Returns
        -------
        y : ndarray
    """
    pass

def get_window_indexer(*args, **kwargs): # real signature unknown
    """
    return the correct window indexer for the computation
    
        Parameters
        ----------
        values: 1d ndarray
        win: integer, window size
        minp: integer, minimum periods
        index: 1d ndarray, optional
            index to the values array
        closed: string, default None
            {'right', 'left', 'both', 'neither'}
            window endpoint closedness. Defaults to 'right' in
            VariableWindowIndexer and to 'both' in FixedWindowIndexer
        floor: optional
            unit for flooring the unit
        use_mock: boolean, default True
            if we are a fixed indexer, return a mock indexer
            instead of the FixedWindow Indexer. This is a type
            compat Indexer that allows us to use a standard
            code path with all of the indexers.
    
    
        Returns
        -------
        tuple of 1d int64 ndarrays of the offsets & data about the window
    """
    pass

def roll_count(*args, **kwargs): # real signature unknown
    pass

def roll_generic(*args, **kwargs): # real signature unknown
    pass

def roll_kurt(*args, **kwargs): # real signature unknown
    pass

def roll_max(*args, **kwargs): # real signature unknown
    """
    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values: numpy array
        window: int, size of rolling window
        minp: if number of observations in window
              is below this, output a NaN
        index: ndarray, optional
           index for window computation
        closed: 'right', 'left', 'both', 'neither'
                make the interval closed on the right, left,
                both or neither endpoints
    """
    pass

def roll_mean(*args, **kwargs): # real signature unknown
    pass

def roll_median_c(*args, **kwargs): # real signature unknown
    pass

def roll_min(*args, **kwargs): # real signature unknown
    """
    Moving max of 1d array of any numeric type along axis=0 ignoring NaNs.
    
        Parameters
        ----------
        values: numpy array
        window: int, size of rolling window
        minp: if number of observations in window
              is below this, output a NaN
        index: ndarray, optional
           index for window computation
    """
    pass

def roll_quantile(*args, **kwargs): # real signature unknown
    """ O(N log(window)) implementation using skip list """
    pass

def roll_skew(*args, **kwargs): # real signature unknown
    pass

def roll_sum(*args, **kwargs): # real signature unknown
    pass

def roll_var(*args, **kwargs): # real signature unknown
    """ Numerically stable implementation using Welford's method. """
    pass

def roll_window(*args, **kwargs): # real signature unknown
    """ Assume len(weights) << len(values) """
    pass

def _check_minp(*args, **kwargs): # real signature unknown
    """
    Parameters
        ----------
        win: int
        minp: int or None
        N: len of window
        floor: int, optional
            default 1
    
        Returns
        -------
        minimum period
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_FixedWindowIndexer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MockFixedWindowIndexer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_VariableWindowIndexer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_WindowIndexer(*args, **kwargs): # real signature unknown
    pass

# classes

class WindowIndexer(object):
    # no doc
    def get_data(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class FixedWindowIndexer(WindowIndexer):
    """
    create a fixed length window indexer object
        that has start & end, that point to offsets in
        the index object; these are defined based on the win
        arguments
    
        Parameters
        ----------
        values: ndarray
            values data array
        win: int64_t
            window size
        minp: int64_t
            min number of obs in a window to consider non-NaN
        index: object
            index of the values
        floor: optional
            unit for flooring the unit
        left_closed: bint
            left endpoint closedness
        right_closed: bint
            right endpoint closedness
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class MockFixedWindowIndexer(WindowIndexer):
    """
    We are just checking parameters of the indexer,
        and returning a consistent API with fixed/variable
        indexers.
    
        Parameters
        ----------
        values: ndarray
            values data array
        win: int64_t
            window size
        minp: int64_t
            min number of obs in a window to consider non-NaN
        index: object
            index of the values
        floor: optional
            unit for flooring
        left_closed: bint
            left endpoint closedness
        right_closed: bint
            right endpoint closedness
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class VariableWindowIndexer(WindowIndexer):
    """
    create a variable length window indexer object
        that has start & end, that point to offsets in
        the index object; these are defined based on the win
        arguments
    
        Parameters
        ----------
        values: ndarray
            values data array
        win: int64_t
            window size
        minp: int64_t
            min number of obs in a window to consider non-NaN
        index: ndarray
            index of the values
        left_closed: bint
            left endpoint closedness
            True if the left endpoint is closed, False if open
        right_closed: bint
            right endpoint closedness
            True if the right endpoint is closed, False if open
        floor: optional
            unit for flooring the unit
    """
    def build(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

interpolation_types = {
    'higher': 2,
    'linear': 0,
    'lower': 1,
    'midpoint': 4,
    'nearest': 3,
}

__test__ = {}

