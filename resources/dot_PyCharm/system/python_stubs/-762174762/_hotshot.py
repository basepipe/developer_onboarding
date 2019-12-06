# encoding: utf-8
# module _hotshot
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

WHAT_ADD_INFO = 19

WHAT_DEFINE_FILE = 35
WHAT_DEFINE_FUNC = 67

WHAT_ENTER = 0
WHAT_EXIT = 1
WHAT_LINENO = 2

WHAT_LINE_TIMES = 51

WHAT_OTHER = 3

__version__ = ''

# functions

def coverage(logfilename): # real signature unknown; restored from __doc__
    """
    coverage(logfilename) -> profiler
    Returns a profiler that doesn't collect any timing information, which is
    useful in building a coverage analysis tool.
    """
    pass

def logreader(filename): # real signature unknown; restored from __doc__
    """
    logreader(filename) --> log-iterator
    Create a log-reader for the timing information file.
    """
    pass

def profiler(logfilename, lineevents=None, linetimes=None): # real signature unknown; restored from __doc__
    """
    profiler(logfilename[, lineevents[, linetimes]]) -> profiler
    Create a new profiler object.
    """
    pass

def resolution(): # real signature unknown; restored from __doc__
    """
    resolution() -> (performance-counter-ticks, update-frequency)
    Return the resolution of the timer provided by the QueryPerformanceCounter()
    function.  The first value is the smallest observed change, and the second
    is the result of QueryPerformanceFrequency().
    """
    pass

# classes

class LogReaderType(object):
    """
    logreader(filename) --> log-iterator
    Create a log-reader for the timing information file.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        Close the log file, preventing additional records from being read.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> file descriptor
        Returns the file descriptor for the log file, if open.
        Raises ValueError if the log file is closed.
        """
        return file('/dev/null')

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the logreader's input file has already been closed."""

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary mapping informational keys to lists of values."""



class ProfilerError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ProfilerType(object):
    """
    High-performance profiler object.
    
    Methods:
    
    close():      Stop the profiler and close the log files.
    fileno():     Returns the file descriptor of the log file.
    runcall():    Run a single function call with profiling enabled.
    runcode():    Execute a code object with profiling enabled.
    start():      Install the profiler and return.
    stop():       Remove the profiler.
    
    Attributes (read-only):
    
    closed:       True if the profiler has already been closed.
    frametimings: True if ENTER/EXIT events collect timing information.
    lineevents:   True if line events are reported to the profiler.
    linetimings:  True if line events collect timing information.
    """
    def addinfo(self, key, value): # real signature unknown; restored from __doc__
        """
        addinfo(key, value)
        Insert an ADD_INFO record into the log.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        Shut down this profiler and close the log files, even if its active.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> file descriptor
        Returns the file descriptor for the log file, if open.
        Raises ValueError if the log file is closed.
        """
        return file('/dev/null')

    def runcall(self, callable, args=None, kw=None): # real signature unknown; restored from __doc__
        """
        runcall(callable[, args[, kw]]) -> callable()
        Profile a specific function call, returning the result of that call.
        """
        pass

    def runcode(self, code, globals, locals=None): # real signature unknown; restored from __doc__
        """
        runcode(code, globals[, locals])
        Execute a code object while collecting profile data.  If locals is
        omitted, globals is used for the locals as well.
        """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """
        start()
        Install this profiler for the current thread.
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """
        stop()
        Remove this profiler from the current thread.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the profiler's output file has already been closed."""

    frametimings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lineevents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linetimings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



