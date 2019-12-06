# encoding: utf-8
# module sys
# from (built-in)
# by generator 1.147
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

exitfunc -- if sys.exitfunc exists, this routine is called when Python exits
  Assigning to sys.exitfunc is deprecated; use the atexit module instead.

stdin -- standard input file object; used by raw_input() and input()
stdout -- standard output file object; used by the print statement
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

exc_type -- type of exception currently being handled
exc_value -- value of exception currently being handled
exc_traceback -- traceback of exception currently being handled
  The function exc_info() should be used instead of these three,
  because it is thread-safe.

Static objects:

float_info -- a dict with information about the float inplementation.
long_info -- a struct sequence with information about the long implementation.
maxint -- the largest supported integer (the smallest is -maxint-1)
maxsize -- the largest supported length of containers.
maxunicode -- the largest supported character
builtin_module_names -- tuple of module names built into this interpreter
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
hexversion -- version information encoded as a single integer
copyright -- copyright notice pertaining to this interpreter
platform -- platform identifier
executable -- absolute path of the executable binary of the Python interpreter
prefix -- prefix used to find the Python library
exec_prefix -- prefix used to find the machine-specific Python library
float_repr_style -- string indicating the style of repr() output for floats
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in __builtin__._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exc_clear() -- clear the exception state for the current thread
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setcheckinterval() -- control how often the interpreter checks for events
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
"""

# imports
from exceptions import exc_type


# Variables with simple values

api_version = 1013

byteorder = 'little'

copyright = 'Copyright (c) 2001-2019 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

dllhandle = 1887502336L

dont_write_bytecode = True

executable = 'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27\\python.exe'

exec_prefix = 'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27'

float_repr_style = 'short'

hexversion = 34017520

maxint = 2147483647
maxsize = 9223372036854775807L
maxunicode = 65535

platform = 'win32'

prefix = 'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27'

py3kwarning = False

version = '2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)]'

winver = '2.7'

# functions

def callstats(): # real signature unknown; restored from __doc__
    """
    callstats() -> tuple of integers
    
    Return a tuple of function call statistics, if CALL_PROFILE was defined
    when Python was built.  Otherwise, return None.
    
    When enabled, this function returns detailed, implementation-specific
    details about the number of function calls executed. The return value is
    a 11-tuple where the entries in the tuple are counts of:
    0. all function calls
    1. calls to PyFunction_Type objects
    2. PyFunction calls that do not create an argument tuple
    3. PyFunction calls that do not create an argument tuple
       and bypass PyEval_EvalCodeEx()
    4. PyMethod calls
    5. PyMethod calls on bound methods
    6. PyType calls
    7. PyCFunction calls
    8. generator calls
    9. All other calls
    10. Number of stack pops performed by call_function()
    """
    return ()

def call_tracing(func, args): # real signature unknown; restored from __doc__
    """
    call_tracing(func, args) -> object
    
    Call func(*args), while tracing is enabled.  The tracing state is
    saved, and restored afterwards.  This is intended to be called from
    a debugger from a checkpoint, to recursively debug some other code.
    """
    return object()

def displayhook(p_object): # real signature unknown; restored from __doc__
    """
    displayhook(object) -> None
    
    Print an object to sys.stdout and also save it in __builtin__._
    """
    pass

def excepthook(exctype, value, traceback): # real signature unknown; restored from __doc__
    """
    excepthook(exctype, value, traceback) -> None
    
    Handle an exception by displaying it with a traceback on sys.stderr.
    """
    pass

def exc_clear(): # real signature unknown; restored from __doc__
    """
    exc_clear() -> None
    
    Clear global information on the current exception.  Subsequent calls to
    exc_info() will return (None,None,None) until another exception is raised
    in the current thread or the execution stack returns to a frame where
    another exception is being handled.
    """
    pass

def exc_info(): # real signature unknown; restored from __doc__
    """
    exc_info() -> (type, value, traceback)
    
    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.
    """
    pass

def exit(status=None): # real signature unknown; restored from __doc__
    """
    exit([status])
    
    Exit the interpreter by raising SystemExit(status).
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).
    """
    pass

def exitfunc(): # reliably restored by inspect
    """
    run any registered exit functions
    
        _exithandlers is traversed in reverse order so functions are executed
        last in, first out.
    """
    pass

def getcheckinterval(): # real signature unknown; restored from __doc__
    """ getcheckinterval() -> current check interval; see setcheckinterval(). """
    pass

def getdefaultencoding(): # real signature unknown; restored from __doc__
    """
    getdefaultencoding() -> string
    
    Return the current default string encoding used by the Unicode 
    implementation.
    """
    return ""

def getfilesystemencoding(): # real signature unknown; restored from __doc__
    """
    getfilesystemencoding() -> string
    
    Return the encoding used to convert Unicode filenames in
    operating system filenames.
    """
    return ""

def getprofile(): # real signature unknown; restored from __doc__
    """
    getprofile()
    
    Return the profiling function set with sys.setprofile.
    See the profiler chapter in the library manual.
    """
    pass

def getrecursionlimit(): # real signature unknown; restored from __doc__
    """
    getrecursionlimit()
    
    Return the current value of the recursion limit, the maximum depth
    of the Python interpreter stack.  This limit prevents infinite
    recursion from causing an overflow of the C stack and crashing Python.
    """
    pass

def getrefcount(p_object): # real signature unknown; restored from __doc__
    """
    getrefcount(object) -> integer
    
    Return the reference count of object.  The count returned is generally
    one higher than you might expect, because it includes the (temporary)
    reference as an argument to getrefcount().
    """
    return 0

def getsizeof(p_object, default): # real signature unknown; restored from __doc__
    """
    getsizeof(object, default) -> int
    
    Return the size of object in bytes.
    """
    return 0

def gettrace(): # real signature unknown; restored from __doc__
    """
    gettrace()
    
    Return the global debug tracing function set with sys.settrace.
    See the debugger chapter in the library manual.
    """
    pass

def getwindowsversion(): # real signature unknown; restored from __doc__
    """
    getwindowsversion()
    
    Return information about the running version of Windows as a named tuple.
    The members are named: major, minor, build, platform, service_pack,
    service_pack_major, service_pack_minor, suite_mask, and product_type. For
    backward compatibility, only the first 5 items are available by indexing.
    All elements are numbers, except service_pack which is a string. Platform
    may be 0 for win32s, 1 for Windows 9x/ME, 2 for Windows NT/2000/XP/Vista/7,
    3 for Windows CE. Product_type may be 1 for a workstation, 2 for a domain
    controller, 3 for a server.
    """
    pass

def setcheckinterval(n): # real signature unknown; restored from __doc__
    """
    setcheckinterval(n)
    
    Tell the Python interpreter to check for asynchronous events every
    n instructions.  This also affects how often thread switches occur.
    """
    pass

def setprofile(function): # real signature unknown; restored from __doc__
    """
    setprofile(function)
    
    Set the profiling function.  It will be called on each function call
    and return.  See the profiler chapter in the library manual.
    """
    pass

def setrecursionlimit(n): # real signature unknown; restored from __doc__
    """
    setrecursionlimit(n)
    
    Set the maximum depth of the Python interpreter stack to n.  This
    limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.
    """
    pass

def settrace(function): # real signature unknown; restored from __doc__
    """
    settrace(function)
    
    Set the global debug tracing function.  It will be called on each
    function call.  See the debugger chapter in the library manual.
    """
    pass

def _clear_type_cache(): # real signature unknown; restored from __doc__
    """
    _clear_type_cache() -> None
    Clear the internal type lookup cache.
    """
    pass

def _current_frames(): # real signature unknown; restored from __doc__
    """
    _current_frames() -> dictionary
    
    Return a dictionary mapping each current thread T's thread id to T's
    current stack frame.
    
    This function should be used for specialized purposes only.
    """
    return {}

def _getframe(depth=None): # real signature unknown; restored from __doc__
    """
    _getframe([depth]) -> frameobject
    
    Return a frame object from the call stack.  If optional integer depth is
    given, return the frame object that many calls below the top of the stack.
    If that is deeper than the call stack, ValueError is raised.  The default
    for depth is zero, returning the frame at the top of the call stack.
    
    This function should be used for internal and specialized
    purposes only.
    """
    pass

def __displayhook__(*args, **kwargs): # real signature unknown
    """
    displayhook(object) -> None
    
    Print an object to sys.stdout and also save it in __builtin__._
    """
    pass

def __excepthook__(*args, **kwargs): # real signature unknown
    """
    excepthook(exctype, value, traceback) -> None
    
    Handle an exception by displaying it with a traceback on sys.stderr.
    """
    pass

# no classes
# variables with complex values

argv = [] # real value of type <type 'list'> skipped

builtin_module_names = () # real value of type <type 'tuple'> skipped

exc_traceback = None # (!) real value is '<traceback object at 0x00000000019814C8>'

exc_value = None # (!) real value is "ImportError('No module named faulthandler',)"

flags = None # (!) real value is 'sys.flags(debug=0, py3k_warning=0, division_warning=0, division_new=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=1, no_user_site=0, no_site=0, ignore_environment=0, tabcheck=0, verbose=0, unicode=0, bytes_warning=0, hash_randomization=0)'

float_info = None # (!) real value is 'sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)'

long_info = None # (!) real value is 'sys.long_info(bits_per_digit=30, sizeof_digit=4)'

meta_path = [
    None, # (!) real value is '<six._SixMetaPathImporter object at 0x0000000001A01B38>'
]

modules = {} # real value of type <type 'dict'> skipped

path = [
    'C:\\BuildAgent\\work\\7116a2615eef197f\\out\\kotlinRun\\classes\\production\\intellij.python.helpers',
    'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27\\python27.zip',
    'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27\\DLLs',
    'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27\\lib',
    'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27\\lib\\plat-win',
    'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27\\lib\\lib-tk',
    'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27',
    'C:\\BuildAgent\\system\\.persistent_cache\\pythons\\python27\\lib\\site-packages',
]

path_hooks = [
    None, # (!) real value is "<type 'zipimport.zipimporter'>"
]

path_importer_cache = {} # real value of type <type 'dict'> skipped

stderr = open('') # real value of type <type 'file'> replaced

stdin = open('') # real value of type <type 'file'> replaced

stdout = open('') # real value of type <type 'file'> replaced

subversion = (
    'CPython',
    '',
    '',
)

version_info = None # (!) real value is "sys.version_info(major=2, minor=7, micro=16, releaselevel='final', serial=0)"

warnoptions = []

_git = (
    'CPython',
    'v2.7.16',
    '413a49145e',
)

__stderr__ = None # (!) real value is "<open file '<stderr>', mode 'w' at 0x000000000131B150>"

__stdin__ = None # (!) real value is "<open file '<stdin>', mode 'r' at 0x000000000131B030>"

__stdout__ = stdout

# intermittent names
exc_value = Exception()
exc_traceback=None
