# encoding: utf-8
# module imp
# from (built-in)
# by generator 1.147
"""
This module provides the components needed to build your own
__import__ function.  Undocumented functions are obsolete.
"""
# no imports

# Variables with simple values

C_BUILTIN = 6
C_EXTENSION = 3

IMP_HOOK = 9

PKG_DIRECTORY = 5

PY_CODERESOURCE = 8
PY_COMPILED = 2
PY_FROZEN = 7
PY_RESOURCE = 4
PY_SOURCE = 1

SEARCH_ERROR = 0

# functions

def acquire_lock(): # real signature unknown; restored from __doc__
    """
    acquire_lock() -> None
    Acquires the interpreter's import lock for the current thread.
    This lock should be used by import hooks to ensure thread-safety
    when importing modules.
    On platforms without threads, this function does nothing.
    """
    pass

def find_module(name, path=None): # real signature unknown; restored from __doc__
    """
    find_module(name, [path]) -> (file, filename, (suffix, mode, type))
    Search for a module.  If path is omitted or None, search for a
    built-in, frozen or special module and continue search in sys.path.
    The module name cannot contain '.'; to search for a submodule of a
    package, pass the submodule name and the package's __path__.
    """
    pass

def get_frozen_object(*args, **kwargs): # real signature unknown
    pass

def get_magic(): # real signature unknown; restored from __doc__
    """
    get_magic() -> string
    Return the magic number for .pyc or .pyo files.
    """
    return ""

def get_suffixes(): # real signature unknown; restored from __doc__
    """
    get_suffixes() -> [(suffix, mode, type), ...]
    Return a list of (suffix, mode, type) tuples describing the files
    that find_module() looks for.
    """
    pass

def init_builtin(*args, **kwargs): # real signature unknown
    pass

def init_frozen(*args, **kwargs): # real signature unknown
    pass

def is_builtin(*args, **kwargs): # real signature unknown
    pass

def is_frozen(*args, **kwargs): # real signature unknown
    pass

def load_compiled(*args, **kwargs): # real signature unknown
    pass

def load_dynamic(*args, **kwargs): # real signature unknown
    pass

def load_module(name, file, filename, (suffix, mode, type)): # real signature unknown; restored from __doc__
    """
    load_module(name, file, filename, (suffix, mode, type)) -> module
    Load a module, given information returned by find_module().
    The module name must include the full package name, if any.
    """
    pass

def load_package(*args, **kwargs): # real signature unknown
    pass

def load_source(*args, **kwargs): # real signature unknown
    pass

def lock_held(): # real signature unknown; restored from __doc__
    """
    lock_held() -> boolean
    Return True if the import lock is currently held, else False.
    On platforms without threads, return False.
    """
    return False

def new_module(name): # real signature unknown; restored from __doc__
    """
    new_module(name) -> module
    Create a new module.  Do not enter it in sys.modules.
    The module name must include the full package name, if any.
    """
    pass

def release_lock(): # real signature unknown; restored from __doc__
    """
    release_lock() -> None
    Release the interpreter's import lock.
    On platforms without threads, this function does nothing.
    """
    pass

def reload(module): # real signature unknown; restored from __doc__
    """
    reload(module) -> module
    
    Reload the module.  The module must have been successfully imported before.
    """
    pass

# classes

class NullImporter(object):
    """ Null importer object """
    def find_module(self, *args, **kwargs): # real signature unknown
        """ Always return None """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


