# encoding: utf-8
# module pandas._libs.join
# from C:\Python27\lib\site-packages\pandas\_libs\join.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
from pandas._libs.algos import ensure_platform_int, groupsort_indexer


# functions

def asof_join_backward(*args, **kwargs): # real signature unknown
    pass

def asof_join_backward_on_X_by_Y(*args, **kwargs): # real signature unknown
    pass

def asof_join_forward(*args, **kwargs): # real signature unknown
    pass

def asof_join_forward_on_X_by_Y(*args, **kwargs): # real signature unknown
    pass

def asof_join_nearest(*args, **kwargs): # real signature unknown
    pass

def asof_join_nearest_on_X_by_Y(*args, **kwargs): # real signature unknown
    pass

def ffill_indexer(*args, **kwargs): # real signature unknown
    pass

def full_outer_join(*args, **kwargs): # real signature unknown
    pass

def inner_join(*args, **kwargs): # real signature unknown
    pass

def inner_join_indexer(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_float32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_float64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_int32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_int64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_object(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def inner_join_indexer_uint64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_float32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_float64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_int32(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_int64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_object(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_uint64(*args, **kwargs): # real signature unknown
    """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
    pass

def left_join_indexer_unique(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_float32(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_float64(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_int32(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_int64(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_object(*args, **kwargs): # real signature unknown
    pass

def left_join_indexer_unique_uint64(*args, **kwargs): # real signature unknown
    pass

def left_outer_join(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_float32(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_float64(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_int32(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_int64(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_object(*args, **kwargs): # real signature unknown
    pass

def outer_join_indexer_uint64(*args, **kwargs): # real signature unknown
    pass

def take_nd(arr, indexer, axis=0, out=None, fill_value=nan, mask_info=None, allow_fill=True): # reliably restored by inspect
    """
    Specialized Cython take which sets NaN values in one pass
    
        This dispatches to ``take`` defined on ExtensionArrays. It does not
        currently dispatch to ``SparseArray.take`` for sparse ``arr``.
    
        Parameters
        ----------
        arr : array-like
            Input array.
        indexer : ndarray
            1-D array of indices to take, subarrays corresponding to -1 value
            indices are filed with fill_value
        axis : int, default 0
            Axis to take from
        out : ndarray or None, default None
            Optional output array, must be appropriate type to hold input and
            fill_value together, if indexer has any -1 value entries; call
            _maybe_promote to determine this type for any fill_value
        fill_value : any, default np.nan
            Fill value to replace -1 values with
        mask_info : tuple of (ndarray, boolean)
            If provided, value should correspond to:
                (indexer != -1, (indexer != -1).any())
            If not provided, it will be computed internally if necessary
        allow_fill : boolean, default True
            If False, indexer is assumed to contain no -1 values so no filling
            will be done.  This short-circuits computation of a mask.  Result is
            undefined if allow_fill == False and -1 is present in indexer.
    
        Returns
        -------
        subarray : array-like
            May be the same type as the input, or cast to an ndarray.
    """
    pass

def _get_result_indexer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__test__ = {}

