# encoding: utf-8
# module array
# from (built-in)
# by generator 1.147
"""
This module defines an object type which can efficiently represent
an array of basic values: characters, integers, floating point
numbers.  Arrays are sequence types and behave very much like lists,
except that the type of objects stored in them is constrained.  The
type is specified at object creation time by using a type code, which
is a single character.  The following type codes are defined:

    Type code   C Type             Minimum size in bytes 
    'c'         character          1 
    'b'         signed integer     1 
    'B'         unsigned integer   1 
    'u'         Unicode character  2 
    'h'         signed integer     2 
    'H'         unsigned integer   2 
    'i'         signed integer     2 
    'I'         unsigned integer   2 
    'l'         signed integer     4 
    'L'         unsigned integer   4 
    'f'         floating point     4 
    'd'         floating point     8 

The constructor is:

array(typecode [, initializer]) -- create a new array
"""
# no imports

# no functions
# classes

class ArrayType(object):
    """
    array(typecode [, initializer]) -> array
    
    Return a new array whose items are restricted by typecode, and
    initialized from the optional initializer value, which must be a list,
    string or iterable over elements of the appropriate type.
    
    Arrays represent basic values and behave very much like lists, except
    the type of objects stored in them is constrained.
    
    Methods:
    
    append() -- append a new item to the end of the array
    buffer_info() -- return information giving the current memory info
    byteswap() -- byteswap all the items of the array
    count() -- return number of occurrences of an object
    extend() -- extend array by appending multiple elements from an iterable
    fromfile() -- read items from a file object
    fromlist() -- append items from the list
    fromstring() -- append items from the string
    index() -- return index of first occurrence of an object
    insert() -- insert a new item into the array at a provided position
    pop() -- remove and return item (default last)
    read() -- DEPRECATED, use fromfile()
    remove() -- remove first occurrence of an object
    reverse() -- reverse the order of the items in the array
    tofile() -- write all items to a file object
    tolist() -- return the array converted to an ordinary list
    tostring() -- return the array converted to a string
    write() -- DEPRECATED, use tofile()
    
    Attributes:
    
    typecode -- the typecode character used to create the array
    itemsize -- the length in bytes of one array item
    """
    def append(self, x): # real signature unknown; restored from __doc__
        """
        append(x)
        
        Append new value x to the end of the array.
        """
        pass

    def buffer_info(self): # real signature unknown; restored from __doc__
        """
        buffer_info() -> (address, length)
        
        Return a tuple (address, length) giving the current memory address and
        the length in items of the buffer used to hold array's contents
        The length should be multiplied by the itemsize attribute to calculate
        the buffer length in bytes.
        """
        pass

    def byteswap(self): # real signature unknown; restored from __doc__
        """
        byteswap()
        
        Byteswap all items of the array.  If the items in the array are not 1, 2,
        4, or 8 bytes in size, RuntimeError is raised.
        """
        pass

    def count(self, x): # real signature unknown; restored from __doc__
        """
        count(x)
        
        Return number of occurrences of x in the array.
        """
        pass

    def extend(self, array_or_iterable): # real signature unknown; restored from __doc__
        """
        extend(array or iterable)
        
         Append items to the end of the array.
        """
        pass

    def fromfile(self, f, n): # real signature unknown; restored from __doc__
        """
        fromfile(f, n)
        
        Read n objects from the file object f and append them to the end of the
        array.  Also called as read.
        """
        pass

    def fromlist(self, p_list): # real signature unknown; restored from __doc__
        """
        fromlist(list)
        
        Append items to array from list.
        """
        pass

    def fromstring(self, string): # real signature unknown; restored from __doc__
        """
        fromstring(string)
        
        Appends items from the string, interpreting it as an array of machine
        values,as if it had been read from a file using the fromfile() method).
        """
        pass

    def fromunicode(self, ustr): # real signature unknown; restored from __doc__
        """
        fromunicode(ustr)
        
        Extends this array with data from the unicode string ustr.
        The array must be a type 'u' array; otherwise a ValueError
        is raised.  Use array.fromstring(ustr.decode(...)) to
        append Unicode data to an array of some other type.
        """
        pass

    def index(self, x): # real signature unknown; restored from __doc__
        """
        index(x)
        
        Return index of first occurrence of x in the array.
        """
        pass

    def insert(self, i, x): # real signature unknown; restored from __doc__
        """
        insert(i,x)
        
        Insert a new item x into the array before position i.
        """
        pass

    def pop(self, i=None): # real signature unknown; restored from __doc__
        """
        pop([i])
        
        Return the i-th element and delete it from the array. i defaults to -1.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        fromfile(f, n)
        
        Read n objects from the file object f and append them to the end of the
        array.  Also called as read.
        """
        pass

    def remove(self, x): # real signature unknown; restored from __doc__
        """
        remove(x)
        
        Remove the first occurrence of x in the array.
        """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """
        reverse()
        
        Reverse the order of the items in the array.
        """
        pass

    def tofile(self, f): # real signature unknown; restored from __doc__
        """
        tofile(f)
        
        Write all items (as machine values) to the file object f.  Also called as
        write.
        """
        pass

    def tolist(self): # real signature unknown; restored from __doc__
        """
        tolist() -> list
        
        Convert array to an ordinary list with the same items.
        """
        return []

    def tostring(self): # real signature unknown; restored from __doc__
        """
        tostring() -> string
        
        Convert the array to an array of machine values and return the string
        representation.
        """
        return ""

    def tounicode(self): # real signature unknown; restored from __doc__
        """
        tounicode() -> unicode
        
        Convert the array to a unicode string.  The array must be
        a type 'u' array; otherwise a ValueError is raised.  Use
        array.tostring().decode() to obtain a unicode string from
        an array of some other type.
        """
        return u""

    def write(self, *args, **kwargs): # real signature unknown
        """
        tofile(f)
        
        Write all items (as machine values) to the file object f.  Also called as
        write.
        """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        copy(array)
        
         Return a copy of the array.
        """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """
        copy(array)
        
         Return a copy of the array.
        """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __delslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__delslice__(i, j) <==> del x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
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

    def __iadd__(self, y): # real signature unknown; restored from __doc__
        """ x.__iadd__(y) <==> x+=y """
        pass

    def __imul__(self, y): # real signature unknown; restored from __doc__
        """ x.__imul__(y) <==> x*=y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
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
        """ Return state information for pickling. """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __setslice__(self, i, j, y): # real signature unknown; restored from __doc__
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y
                   
                   Use  of negative indices is not supported.
        """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        
        Size of the array in memory, in bytes.
        """
        return 0

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the size, in bytes, of one array item"""

    typecode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the typecode character used to create the array"""



array = ArrayType


