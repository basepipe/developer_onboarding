# encoding: utf-8
# module pandas._libs.groupby
# from C:\Python27\lib\site-packages\pandas\_libs\groupby.pyd
# by generator 1.147
# no doc

# imports
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
from pandas._libs.algos import (groupsort_indexer, 
    take_2d_axis1_float64_float64)


# Variables with simple values

_int64_max = 9223372036854775807L

# functions

def group_add_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_add_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_any_all(*args, **kwargs): # real signature unknown
    """
    Aggregated boolean values to show truthfulness of group elements
    
        Parameters
        ----------
        out : array of values which this method will write its results to
        labels : array containing unique label for each group, with its
            ordering matching up to the corresponding record in `values`
        values : array containing the truth value of each element
        mask : array indicating whether a value is na or not
        val_test : str {'any', 'all'}
            String object dictating whether to use any or all truth testing
        skipna : boolean
            Flag to ignore nan values during truth testing
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object.
        The returned values will either be 0 or 1 (False or True, respectively).
    """
    pass

def group_cummax(*args, **kwargs): # real signature unknown
    """ Only transforms on axis=0 """
    pass

def group_cummin(*args, **kwargs): # real signature unknown
    """ Only transforms on axis=0 """
    pass

def group_cumprod_float64(*args, **kwargs): # real signature unknown
    """ Only transforms on axis=0 """
    pass

def group_cumsum(*args, **kwargs): # real signature unknown
    """ Only transforms on axis=0 """
    pass

def group_fillna_indexer(*args, **kwargs): # real signature unknown
    """
    Indexes how to fill values forwards or backwards within a group
    
        Parameters
        ----------
        out : array of int64_t values which this method will write its results to
            Missing values will be written to with a value of -1
        labels : array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`
        mask : array of int64_t values where a 1 indicates a missing value
        direction : {'ffill', 'bfill'}
            Direction for fill to be applied (forwards or backwards, respectively)
        limit : Consecutive values to fill before stopping, or -1 for no limit
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_last_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_last_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_last_int64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_last_object(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_max(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_mean_float32(*args, **kwargs): # real signature unknown
    pass

def group_mean_float64(*args, **kwargs): # real signature unknown
    pass

def group_median_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_min(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_nth_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_nth_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_nth_int64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_nth_object(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_ohlc_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_ohlc_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_prod_float32(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_prod_float64(*args, **kwargs): # real signature unknown
    """ Only aggregates on axis=0 """
    pass

def group_rank_float32(*args, **kwargs): # real signature unknown
    """
    Provides the rank of values within each group.
    
        Parameters
        ----------
        out : array of float64_t values which this method will write its results to
        values : array of float32_t values to be ranked
        labels : array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`
        is_datetimelike : bool, default False
            unused in this method but provided for call compatibility with other
            Cython transformations
        ties_method : {'average', 'min', 'max', 'first', 'dense'}, default
            'average'
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : boolean, default True
            False for ranks by high (1) to low (N)
            na_option : {'keep', 'top', 'bottom'}, default 'keep'
        pct : boolean, default False
            Compute percentage rank of data within each group
        na_option : {'keep', 'top', 'bottom'}, default 'keep'
            * keep: leave NA values where they are
            * top: smallest rank if ascending
            * bottom: smallest rank if descending
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_rank_float64(*args, **kwargs): # real signature unknown
    """
    Provides the rank of values within each group.
    
        Parameters
        ----------
        out : array of float64_t values which this method will write its results to
        values : array of float64_t values to be ranked
        labels : array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`
        is_datetimelike : bool, default False
            unused in this method but provided for call compatibility with other
            Cython transformations
        ties_method : {'average', 'min', 'max', 'first', 'dense'}, default
            'average'
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : boolean, default True
            False for ranks by high (1) to low (N)
            na_option : {'keep', 'top', 'bottom'}, default 'keep'
        pct : boolean, default False
            Compute percentage rank of data within each group
        na_option : {'keep', 'top', 'bottom'}, default 'keep'
            * keep: leave NA values where they are
            * top: smallest rank if ascending
            * bottom: smallest rank if descending
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_rank_int64(*args, **kwargs): # real signature unknown
    """
    Provides the rank of values within each group.
    
        Parameters
        ----------
        out : array of float64_t values which this method will write its results to
        values : array of int64_t values to be ranked
        labels : array containing unique label for each group, with its ordering
            matching up to the corresponding record in `values`
        is_datetimelike : bool, default False
            unused in this method but provided for call compatibility with other
            Cython transformations
        ties_method : {'average', 'min', 'max', 'first', 'dense'}, default
            'average'
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : boolean, default True
            False for ranks by high (1) to low (N)
            na_option : {'keep', 'top', 'bottom'}, default 'keep'
        pct : boolean, default False
            Compute percentage rank of data within each group
        na_option : {'keep', 'top', 'bottom'}, default 'keep'
            * keep: leave NA values where they are
            * top: smallest rank if ascending
            * bottom: smallest rank if descending
    
        Notes
        -----
        This method modifies the `out` parameter rather than returning an object
    """
    pass

def group_shift_indexer(*args, **kwargs): # real signature unknown
    pass

def group_var_float32(*args, **kwargs): # real signature unknown
    pass

def group_var_float64(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

tiebreakers = {
    'average': 0,
    'dense': 5,
    'first': 3,
    'max': 2,
    'min': 1,
}

__test__ = {}

