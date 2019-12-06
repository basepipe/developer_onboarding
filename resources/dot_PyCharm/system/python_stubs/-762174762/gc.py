# encoding: utf-8
# module gc
# from (built-in)
# by generator 1.147
"""
This module provides access to the garbage collector for reference cycles.

enable() -- Enable automatic garbage collection.
disable() -- Disable automatic garbage collection.
isenabled() -- Returns true if automatic collection is enabled.
collect() -- Do a full collection right now.
get_count() -- Return the current collection counts.
set_debug() -- Set debugging flags.
get_debug() -- Get debugging flags.
set_threshold() -- Set the collection thresholds.
get_threshold() -- Return the current the collection thresholds.
get_objects() -- Return a list of all objects tracked by the collector.
is_tracked() -- Returns true if a given object is tracked.
get_referrers() -- Return the list of objects that refer to an object.
get_referents() -- Return the list of objects that an object refers to.
"""
# no imports

# Variables with simple values

DEBUG_COLLECTABLE = 2
DEBUG_INSTANCES = 8
DEBUG_LEAK = 62
DEBUG_OBJECTS = 16
DEBUG_SAVEALL = 32
DEBUG_STATS = 1
DEBUG_UNCOLLECTABLE = 4

# functions

def collect(generation=None): # real signature unknown; restored from __doc__
    """
    collect([generation]) -> n
    
    With no arguments, run a full collection.  The optional argument
    may be an integer specifying which generation to collect.  A ValueError
    is raised if the generation number is invalid.
    
    The number of unreachable objects is returned.
    """
    pass

def disable(): # real signature unknown; restored from __doc__
    """
    disable() -> None
    
    Disable automatic garbage collection.
    """
    pass

def enable(): # real signature unknown; restored from __doc__
    """
    enable() -> None
    
    Enable automatic garbage collection.
    """
    pass

def get_count(): # real signature unknown; restored from __doc__
    """
    get_count() -> (count0, count1, count2)
    
    Return the current collection counts
    """
    pass

def get_debug(): # real signature unknown; restored from __doc__
    """
    get_debug() -> flags
    
    Get the garbage collection debugging flags.
    """
    pass

def get_objects(): # real signature unknown; restored from __doc__
    """
    get_objects() -> [...]
    
    Return a list of objects tracked by the collector (excluding the list
    returned).
    """
    pass

def get_referents(*objs): # real signature unknown; restored from __doc__
    """
    get_referents(*objs) -> list
    Return the list of objects that are directly referred to by objs.
    """
    return []

def get_referrers(*objs): # real signature unknown; restored from __doc__
    """
    get_referrers(*objs) -> list
    Return the list of objects that directly refer to any of objs.
    """
    return []

def get_threshold(): # real signature unknown; restored from __doc__
    """
    get_threshold() -> (threshold0, threshold1, threshold2)
    
    Return the current collection thresholds
    """
    pass

def isenabled(): # real signature unknown; restored from __doc__
    """
    isenabled() -> status
    
    Returns true if automatic garbage collection is enabled.
    """
    pass

def is_tracked(obj): # real signature unknown; restored from __doc__
    """
    is_tracked(obj) -> bool
    
    Returns true if the object is tracked by the garbage collector.
    Simple atomic objects will return false.
    """
    return False

def set_debug(flags): # real signature unknown; restored from __doc__
    """
    set_debug(flags) -> None
    
    Set the garbage collection debugging flags. Debugging information is
    written to sys.stderr.
    
    flags is an integer and can have the following bits turned on:
    
      DEBUG_STATS - Print statistics during collection.
      DEBUG_COLLECTABLE - Print collectable objects found.
      DEBUG_UNCOLLECTABLE - Print unreachable but uncollectable objects found.
      DEBUG_INSTANCES - Print instance objects.
      DEBUG_OBJECTS - Print objects other than instances.
      DEBUG_SAVEALL - Save objects to gc.garbage rather than freeing them.
      DEBUG_LEAK - Debug leaking programs (everything but STATS).
    """
    pass

def set_threshold(threshold0, threshold1=None, threshold2=None): # real signature unknown; restored from __doc__
    """
    set_threshold(threshold0, [threshold1, threshold2]) -> None
    
    Sets the collection thresholds.  Setting threshold0 to zero disables
    collection.
    """
    pass

# no classes
# variables with complex values

garbage = []

