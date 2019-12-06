# encoding: utf-8
# module thread
# from (built-in)
# by generator 1.147
"""
This module provides primitive operations to write multi-threaded programs.
The 'threading' module provides a more convenient interface.
"""
# no imports

# functions

def allocate(): # real signature unknown; restored from __doc__
    """
    allocate_lock() -> lock object
    (allocate() is an obsolete synonym)
    
    Create a new lock object.  See help(LockType) for information about locks.
    """
    pass

def allocate_lock(): # real signature unknown; restored from __doc__
    """
    allocate_lock() -> lock object
    (allocate() is an obsolete synonym)
    
    Create a new lock object.  See help(LockType) for information about locks.
    """
    pass

def exit(): # real signature unknown; restored from __doc__
    """
    exit()
    (exit_thread() is an obsolete synonym)
    
    This is synonymous to ``raise SystemExit''.  It will cause the current
    thread to exit silently unless the exception is caught.
    """
    pass

def exit_thread(): # real signature unknown; restored from __doc__
    """
    exit()
    (exit_thread() is an obsolete synonym)
    
    This is synonymous to ``raise SystemExit''.  It will cause the current
    thread to exit silently unless the exception is caught.
    """
    pass

def get_ident(): # real signature unknown; restored from __doc__
    """
    get_ident() -> integer
    
    Return a non-zero integer that uniquely identifies the current thread
    amongst other threads that exist simultaneously.
    This may be used to identify per-thread resources.
    Even though on some platforms threads identities may appear to be
    allocated consecutive numbers starting at 1, this behavior should not
    be relied upon, and the number should be seen purely as a magic cookie.
    A thread's identity may be reused for another thread after it exits.
    """
    return 0

def interrupt_main(): # real signature unknown; restored from __doc__
    """
    interrupt_main()
    
    Raise a KeyboardInterrupt in the main thread.
    A subthread can use this function to interrupt the main thread.
    """
    pass

def stack_size(size=None): # real signature unknown; restored from __doc__
    """
    stack_size([size]) -> size
    
    Return the thread stack size used when creating new threads.  The
    optional size argument specifies the stack size (in bytes) to be used
    for subsequently created threads, and must be 0 (use platform or
    configured default) or a positive integer value of at least 32,768 (32k).
    If changing the thread stack size is unsupported, a ThreadError
    exception is raised.  If the specified size is invalid, a ValueError
    exception is raised, and the stack size is unmodified.  32k bytes
     currently the minimum supported stack size value to guarantee
    sufficient stack space for the interpreter itself.
    
    Note that some platforms may have particular restrictions on values for
    the stack size, such as requiring a minimum stack size larger than 32kB or
    requiring allocation in multiples of the system memory page size
    - platform documentation should be referred to for more information
    (4kB pages are common; using multiples of 4096 for the stack size is
    the suggested approach in the absence of more specific information).
    """
    pass

def start_new(function, args, kwargs=None): # known case of thread.start_new
    """
    start_new_thread(function, args[, kwargs])
    (start_new() is an obsolete synonym)
    
    Start a new thread and return its identifier.  The thread will call the
    function with positional arguments from the tuple args and keyword arguments
    taken from the optional dictionary kwargs.  The thread exits when the
    function returns; the return value is ignored.  The thread will also exit
    when the function raises an unhandled exception; a stack trace will be
    printed unless the exception is SystemExit.
    """
    return 0

def start_new_thread(function, args, kwargs=None): # real signature unknown; restored from __doc__
    """
    start_new_thread(function, args[, kwargs])
    (start_new() is an obsolete synonym)
    
    Start a new thread and return its identifier.  The thread will call the
    function with positional arguments from the tuple args and keyword arguments
    taken from the optional dictionary kwargs.  The thread exits when the
    function returns; the return value is ignored.  The thread will also exit
    when the function raises an unhandled exception; a stack trace will be
    printed unless the exception is SystemExit.
    """
    pass

def _count(): # real signature unknown; restored from __doc__
    """
    _count() -> integer
    
    Return the number of currently running Python threads, excluding 
    the main thread. The returned number comprises all threads created
    through `start_new_thread()` as well as `threading.Thread`, and not
    yet finished.
    
    This function is meant for internal and specialized purposes only.
    In most applications `threading.enumerate()` should be used instead.
    """
    return 0

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class LockType(object):
    """
    A lock object is a synchronization primitive.  To create a lock,
    call the PyThread_allocate_lock() function.  Methods are:
    
    acquire() -- lock the lock, possibly blocking until it can be obtained
    release() -- unlock of the lock
    locked() -- test whether the lock is currently locked
    
    A lock is not owned by the thread that locked it; another thread may
    unlock it.  A thread attempting to lock a lock that it has already locked
    will block until another thread unlocks it.  Deadlocks may ensue.
    """
    def acquire(self, wait=None): # real signature unknown; restored from __doc__
        """
        acquire([wait]) -> bool
        (acquire_lock() is an obsolete synonym)
        
        Lock the lock.  Without argument, this blocks if the lock is already
        locked (even by the same thread), waiting for another thread to release
        the lock, and return True once the lock is acquired.
        With an argument, this will only block if the argument is true,
        and the return value reflects whether the lock is acquired.
        The blocking operation is not interruptible.
        """
        return False

    def acquire_lock(self): # real signature unknown; restored from __doc__
        """
        acquire([wait]) -> bool
        (acquire_lock() is an obsolete synonym)
        
        Lock the lock.  Without argument, this blocks if the lock is already
        locked (even by the same thread), waiting for another thread to release
        the lock, and return True once the lock is acquired.
        With an argument, this will only block if the argument is true,
        and the return value reflects whether the lock is acquired.
        The blocking operation is not interruptible.
        """
        pass

    def locked(self): # real signature unknown; restored from __doc__
        """
        locked() -> bool
        (locked_lock() is an obsolete synonym)
        
        Return whether the lock is in the locked state.
        """
        return False

    def locked_lock(self): # real signature unknown; restored from __doc__
        """
        locked() -> bool
        (locked_lock() is an obsolete synonym)
        
        Return whether the lock is in the locked state.
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        release()
        (release_lock() is an obsolete synonym)
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        but it needn't be locked by the same thread that unlocks it.
        """
        pass

    def release_lock(self): # real signature unknown; restored from __doc__
        """
        release()
        (release_lock() is an obsolete synonym)
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        but it needn't be locked by the same thread that unlocks it.
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        acquire([wait]) -> bool
        (acquire_lock() is an obsolete synonym)
        
        Lock the lock.  Without argument, this blocks if the lock is already
        locked (even by the same thread), waiting for another thread to release
        the lock, and return True once the lock is acquired.
        With an argument, this will only block if the argument is true,
        and the return value reflects whether the lock is acquired.
        The blocking operation is not interruptible.
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        release()
        (release_lock() is an obsolete synonym)
        
        Release the lock, allowing another thread that is blocked waiting for
        the lock to acquire the lock.  The lock must be in the locked state,
        but it needn't be locked by the same thread that unlocks it.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class _local(object):
    """ Thread-local data """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


