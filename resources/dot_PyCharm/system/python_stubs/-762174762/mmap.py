# encoding: utf-8
# module mmap
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ACCESS_COPY = 3
ACCESS_READ = 1
ACCESS_WRITE = 2

ALLOCATIONGRANULARITY = 65536

PAGESIZE = 4096

# no functions
# classes

class error(EnvironmentError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class mmap(object):
    """
    Windows: mmap(fileno, length[, tagname[, access[, offset]]])
    
    Maps length bytes from the file specified by the file handle fileno,
    and returns a mmap object.  If length is larger than the current size
    of the file, the file is extended to contain length bytes.  If length
    is 0, the maximum length of the map is the current size of the file,
    except that if the file is empty Windows raises an exception (you cannot
    create an empty mapping on Windows).
    
    Unix: mmap(fileno, length[, flags[, prot[, access[, offset]]]])
    
    Maps length bytes from the file specified by the file descriptor fileno,
    and returns a mmap object.  If length is 0, the maximum length of the map
    will be the current size of the file when mmap is called.
    flags specifies the nature of the mapping. MAP_PRIVATE creates a
    private copy-on-write mapping, so changes to the contents of the mmap
    object will be private to this process, and MAP_SHARED creates a mapping
    that's shared with all other processes mapping the same areas of the file.
    The default value is MAP_SHARED.
    
    To map anonymous memory, pass -1 as the fileno (both versions).
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def read_byte(self, *args, **kwargs): # real signature unknown
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        pass

    def rfind(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def write_byte(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, fileno, length, tagname=None, access=None, offset=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
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

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass


