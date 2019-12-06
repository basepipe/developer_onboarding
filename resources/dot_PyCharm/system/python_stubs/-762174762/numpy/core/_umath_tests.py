# encoding: utf-8
# module numpy.core._umath_tests
# from C:\Python27\lib\site-packages\numpy\core\_umath_tests.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__version__ = '0.1'

# functions

def cross1d(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cross1d(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    cross product on the last dimension and broadcast on the rest 
         "(3),(3)->(3)"
    """
    pass

def cumsum(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    cumsum(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Cumulative sum of the input (n)->(n)
    """
    pass

def euclidean_pdist(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    euclidean_pdist(x, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    pairwise euclidean distance on last two dimensions 
         "(n,d)->(p)"
    """
    pass

def inner1d(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    inner1d(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    inner on the last dimension and broadcast on the rest 
         "(i),(i)->()"
    """
    pass

def inner1d_no_doc(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ inner1d_no_doc(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) """
    pass

def innerwt(x1, x2, x3, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    innerwt(x1, x2, x3, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    inner1d with a weight argument 
         "(i),(i),(i)->()"
    """
    pass

def matmul(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    matmul(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    matmul on last two dimensions, with some being optional
         "(m?,n),(n,p?)->(m?,p?)"
    """
    pass

def matrix_multiply(x1, x2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    matrix_multiply(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    matrix multiplication on last two dimensions 
         "(m,n),(n,p)->(m,p)"
    """
    pass

def test_signature(*args, **kwargs): # real signature unknown
    """
    Test signature parsing of ufunc. 
    Arguments: nin nout signature 
    If fails, it returns NULL. Otherwise it returns a tuple of ufunc internals.
    """
    pass

# no classes
