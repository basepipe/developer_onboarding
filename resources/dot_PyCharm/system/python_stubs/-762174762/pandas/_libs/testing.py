# encoding: utf-8
# module pandas._libs.testing
# from C:\Python27\lib\site-packages\pandas\_libs\testing.pyd
# by generator 1.147
# no doc

# imports
import pandas.compat as compat # C:\Python27\lib\site-packages\pandas\compat\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc

# functions

def array_equivalent(left, right, strict_nan=False): # reliably restored by inspect
    """
    True if two arrays, left and right, have equal non-NaN elements, and NaNs
        in corresponding locations.  False otherwise. It is assumed that left and
        right are NumPy arrays of the same dtype. The behavior of this function
        (particularly with respect to NaNs) is not defined if the dtypes are
        different.
    
        Parameters
        ----------
        left, right : ndarrays
        strict_nan : bool, default False
            If True, consider NaN and None to be different.
    
        Returns
        -------
        b : bool
            Returns True if the arrays are equivalent.
    
        Examples
        --------
        >>> array_equivalent(
        ...     np.array([1, 2, np.nan]),
        ...     np.array([1, 2, np.nan]))
        True
        >>> array_equivalent(
        ...     np.array([1, np.nan, 2]),
        ...     np.array([1, 2, np.nan]))
        False
    """
    pass

def assert_almost_equal(*args, **kwargs): # real signature unknown
    """
    Check that left and right objects are almost equal.
    
        Parameters
        ----------
        a : object
        b : object
        check_less_precise : bool or int, default False
            Specify comparison precision.
            5 digits (False) or 3 digits (True) after decimal points are
            compared. If an integer, then this will be the number of decimal
            points to compare
        check_dtype: bool, default True
            check dtype if both a and b are np.ndarray
        obj : str, default None
            Specify object name being compared, internally used to show
            appropriate assertion message
        lobj : str, default None
            Specify left object name being compared, internally used to show
            appropriate assertion message
        robj : str, default None
            Specify right object name being compared, internally used to show
            appropriate assertion message
    """
    pass

def assert_dict_equal(*args, **kwargs): # real signature unknown
    pass

def isna(obj): # reliably restored by inspect
    """
    Detect missing values for an array-like object.
    
        This function takes a scalar or array-like object and indicates
        whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN``
        in object arrays, ``NaT`` in datetimelike).
    
        Parameters
        ----------
        obj : scalar or array-like
            Object to check for null or missing values.
    
        Returns
        -------
        bool or array-like of bool
            For scalar input, returns a scalar boolean.
            For array input, returns an array of boolean indicating whether each
            corresponding element is missing.
    
        See Also
        --------
        notna : Boolean inverse of pandas.isna.
        Series.isna : Detect missing values in a Series.
        DataFrame.isna : Detect missing values in a DataFrame.
        Index.isna : Detect missing values in an Index.
    
        Examples
        --------
        Scalar arguments (including strings) result in a scalar boolean.
    
        >>> pd.isna('dog')
        False
    
        >>> pd.isna(np.nan)
        True
    
        ndarrays result in an ndarray of booleans.
    
        >>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
        >>> array
        array([[ 1., nan,  3.],
               [ 4.,  5., nan]])
        >>> pd.isna(array)
        array([[False,  True, False],
               [False, False,  True]])
    
        For indexes, an ndarray of booleans is returned.
    
        >>> index = pd.DatetimeIndex(["2017-07-05", "2017-07-06", None,
        ...                           "2017-07-08"])
        >>> index
        DatetimeIndex(['2017-07-05', '2017-07-06', 'NaT', '2017-07-08'],
                      dtype='datetime64[ns]', freq=None)
        >>> pd.isna(index)
        array([False, False,  True, False])
    
        For Series and DataFrame, the same type is returned, containing booleans.
    
        >>> df = pd.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
        >>> df
             0     1    2
        0  ant   bee  cat
        1  dog  None  fly
        >>> pd.isna(df)
               0      1      2
        0  False  False  False
        1  False   True  False
    
        >>> pd.isna(df[1])
        0    False
        1     True
        Name: 1, dtype: bool
    """
    pass

def is_dtype_equal(source, target): # reliably restored by inspect
    """
    Check if two dtypes are equal.
    
        Parameters
        ----------
        source : The first dtype to compare
        target : The second dtype to compare
    
        Returns
        ----------
        boolean : Whether or not the two dtypes are equal.
    
        Examples
        --------
        >>> is_dtype_equal(int, float)
        False
        >>> is_dtype_equal("int", int)
        True
        >>> is_dtype_equal(object, "category")
        False
        >>> is_dtype_equal(CategoricalDtype(), "category")
        True
        >>> is_dtype_equal(DatetimeTZDtype(), "datetime64")
        False
    """
    pass

# no classes
# variables with complex values

__test__ = {}

