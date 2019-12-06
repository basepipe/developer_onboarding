# encoding: utf-8
# module pandas._libs.ops
# from C:\Python27\lib\site-packages\pandas\_libs\ops.pyd
# by generator 1.147
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import operator as operator # <module 'operator' (built-in)>
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc

# functions

def maybe_convert_bool(*args, **kwargs): # real signature unknown
    pass

def scalar_binop(*args, **kwargs): # real signature unknown
    """
    Apply the given binary operator `op` between each element of the array
        `values` and the scalar `val`.
    
        Parameters
        ----------
        values : ndarray[object]
        val : object
        op : binary operator
    
        Returns
        -------
        result : ndarray[object]
    """
    pass

def scalar_compare(*args, **kwargs): # real signature unknown
    """
    Compare each element of `values` array with the scalar `val`, with
        the comparison operation described by `op`.
    
        Parameters
        ----------
        values : ndarray[object]
        val : object
        op : {operator.eq, operator.ne,
              operator.le, operator.lt,
              operator.ge, operator.gt}
    
        Returns
        -------
        result : ndarray[bool]
    """
    pass

def vec_binop(*args, **kwargs): # real signature unknown
    """
    Apply the given binary operator `op` pointwise to the elements of
        arrays `left` and `right`.
    
        Parameters
        ----------
        left : ndarray[object]
        right : ndarray[object]
        op : binary operator
    
        Returns
        -------
        result : ndarray[object]
    """
    pass

def vec_compare(*args, **kwargs): # real signature unknown
    """
    Compare the elements of `left` with the elements of `right` pointwise,
        with the comparison operation described by `op`.
    
        Parameters
        ----------
        left : ndarray[object]
        right : ndarray[object]
        op : {operator.eq, operator.ne,
              operator.le, operator.lt,
              operator.ge, operator.gt}
    
        Returns
        -------
        result : ndarray[bool]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__test__ = {}

