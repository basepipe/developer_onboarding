# encoding: utf-8
# module _multiprocessing
# from (pre-generated)
# by generator 1.147
# no doc
# no imports

# functions

def address_of_buffer(obj): # real signature unknown; restored from __doc__
    """
    address_of_buffer(obj) -> int
    Return address of obj assuming obj supports buffer inteface
    """
    return 0

# classes

class Connection(object):
    """
    Connection type whose constructor signature is
    
        Connection(handle, readable=True, writable=True).
    
    The constructor does *not* duplicate the handle.
    """
    def close(self, *args, **kwargs): # real signature unknown
        """ close the connection """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """ file descriptor or handle of the connection """
        pass

    def poll(self, *args, **kwargs): # real signature unknown
        """ whether there is any input available to be read """
        pass

    def recv(self, *args, **kwargs): # real signature unknown
        """ receive a (picklable) object """
        pass

    def recv_bytes(self, *args, **kwargs): # real signature unknown
        """ receive byte data as a string """
        pass

    def recv_bytes_into(self, *args, **kwargs): # real signature unknown
        """
        receive byte data into a writeable buffer-like object
        returns the number of bytes read
        """
        pass

    def send(self, *args, **kwargs): # real signature unknown
        """ send a (picklable) object """
        pass

    def send_bytes(self, *args, **kwargs): # real signature unknown
        """ send the byte data from a readable buffer-like object """
        pass

    def __init__(self, handle, readable=True, writable=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is closed"""

    readable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is readable"""

    writable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is writable"""



class PipeConnection(object):
    """
    Connection type whose constructor signature is
    
        Connection(handle, readable=True, writable=True).
    
    The constructor does *not* duplicate the handle.
    """
    def close(self, *args, **kwargs): # real signature unknown
        """ close the connection """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """ file descriptor or handle of the connection """
        pass

    def poll(self, *args, **kwargs): # real signature unknown
        """ whether there is any input available to be read """
        pass

    def recv(self, *args, **kwargs): # real signature unknown
        """ receive a (picklable) object """
        pass

    def recv_bytes(self, *args, **kwargs): # real signature unknown
        """ receive byte data as a string """
        pass

    def recv_bytes_into(self, *args, **kwargs): # real signature unknown
        """
        receive byte data into a writeable buffer-like object
        returns the number of bytes read
        """
        pass

    def send(self, *args, **kwargs): # real signature unknown
        """ send a (picklable) object """
        pass

    def send_bytes(self, *args, **kwargs): # real signature unknown
        """ send the byte data from a readable buffer-like object """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is closed"""

    readable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is readable"""

    writable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the connection is writable"""



class SemLock(object):
    """ Semaphore/Mutex type """
    def acquire(self, *args, **kwargs): # real signature unknown
        """ acquire the semaphore/lock """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        """ release the semaphore/lock """
        pass

    def _after_fork(self, *args, **kwargs): # real signature unknown
        """ rezero the net acquisition count after fork() """
        pass

    def _count(self, *args, **kwargs): # real signature unknown
        """ num of `acquire()`s minus num of `release()`s for this process """
        pass

    def _get_value(self, *args, **kwargs): # real signature unknown
        """ get the value of the semaphore """
        pass

    def _is_mine(self, *args, **kwargs): # real signature unknown
        """ whether the lock is owned by this thread """
        pass

    def _is_zero(self, *args, **kwargs): # real signature unknown
        """ returns whether semaphore has value zero """
        pass

    @classmethod
    def _rebuild(cls, *args, **kwargs): # real signature unknown
        """  """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ enter the semaphore/lock """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ exit the semaphore/lock """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxvalue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    SEM_VALUE_MAX = 2147483647L


class win32(object):
    # no doc
    def CloseHandle(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def ConnectNamedPipe(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def CreateFile(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def CreateNamedPipe(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def ExitProcess(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def GetLastError(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def OpenProcess(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def SetNamedPipeHandleState(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def WaitNamedPipe(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ERROR_ALREADY_EXISTS = 183
    ERROR_NO_DATA = 232
    ERROR_PIPE_BUSY = 231
    ERROR_PIPE_CONNECTED = 535
    ERROR_SEM_TIMEOUT = 121
    GENERIC_READ = 2147483648L
    GENERIC_WRITE = 1073741824
    INFINITE = 4294967295L
    NMPWAIT_WAIT_FOREVER = 4294967295L
    NULL = 0
    OPEN_EXISTING = 3
    PIPE_ACCESS_DUPLEX = 3
    PIPE_ACCESS_INBOUND = 1
    PIPE_READMODE_MESSAGE = 2
    PIPE_TYPE_MESSAGE = 4
    PIPE_UNLIMITED_INSTANCES = 255
    PIPE_WAIT = 0
    PROCESS_ALL_ACCESS = 2035711


# variables with complex values

flags = {
    'HAVE_FD_TRANSFER': 0,
}

