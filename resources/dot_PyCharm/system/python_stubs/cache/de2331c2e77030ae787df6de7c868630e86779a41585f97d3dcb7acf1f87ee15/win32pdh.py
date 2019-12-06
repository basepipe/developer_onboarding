# encoding: utf-8
# module win32pdh
# from C:\Python27\lib\site-packages\win32\win32pdh.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

PDH_FMT_1000 = 8192
PDH_FMT_ANSI = 32
PDH_FMT_DOUBLE = 512
PDH_FMT_LARGE = 1024
PDH_FMT_LONG = 256
PDH_FMT_NODATA = 16384
PDH_FMT_NOSCALE = 4096
PDH_FMT_RAW = 16
PDH_FMT_UNICODE = 64

PDH_MAX_SCALE = 7

PDH_MIN_SCALE = -7

PDH_PATH_WBEM_INPUT = 2
PDH_PATH_WBEM_RESULT = 1

PDH_VERSION = 1283

PERF_DETAIL_ADVANCED = 200
PERF_DETAIL_EXPERT = 300
PERF_DETAIL_NOVICE = 100
PERF_DETAIL_WIZARD = 400

# functions

def AddCounter(*args, **kwargs): # real signature unknown
    pass

def AddEnglishCounter(*args, **kwargs): # real signature unknown
    pass

def BrowseCounters(*args, **kwargs): # real signature unknown
    pass

def CloseQuery(*args, **kwargs): # real signature unknown
    pass

def CollectQueryData(*args, **kwargs): # real signature unknown
    pass

def ConnectMachine(*args, **kwargs): # real signature unknown
    pass

def EnumObjectItems(*args, **kwargs): # real signature unknown
    pass

def EnumObjects(*args, **kwargs): # real signature unknown
    pass

def ExpandCounterPath(*args, **kwargs): # real signature unknown
    pass

def GetCounterInfo(*args, **kwargs): # real signature unknown
    pass

def GetFormattedCounterArray(*args, **kwargs): # real signature unknown
    pass

def GetFormattedCounterValue(*args, **kwargs): # real signature unknown
    pass

def LookupPerfIndexByName(*args, **kwargs): # real signature unknown
    pass

def LookupPerfNameByIndex(*args, **kwargs): # real signature unknown
    pass

def MakeCounterPath(*args, **kwargs): # real signature unknown
    pass

def OpenQuery(*args, **kwargs): # real signature unknown
    pass

def ParseCounterPath(*args, **kwargs): # real signature unknown
    pass

def ParseInstanceName(*args, **kwargs): # real signature unknown
    pass

def RemoveCounter(*args, **kwargs): # real signature unknown
    pass

def SetCounterScaleFactor(*args, **kwargs): # real signature unknown
    pass

def ValidatePath(*args, **kwargs): # real signature unknown
    pass

# classes

class counter_status_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



