# encoding: utf-8
# module servicemanager
# from C:\Python27\lib\site-packages\win32\servicemanager.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

COINIT_APARTMENTTHREADED = 2

COINIT_DISABLE_OLE1DDE = 4

COINIT_MULTITHREADED = 0

COINIT_SPEED_OVER_MEMORY = 8

EVENTLOG_AUDIT_FAILURE = 16
EVENTLOG_AUDIT_SUCCESS = 8

EVENTLOG_ERROR_TYPE = 1

EVENTLOG_INFORMATION_TYPE = 4

EVENTLOG_WARNING_TYPE = 2

PYS_SERVICE_STARTED = 1073745922
PYS_SERVICE_STARTING = 1073745920
PYS_SERVICE_STOPPED = 1073745924
PYS_SERVICE_STOPPING = 1073745923

# functions

def CoInitializeEx(*args, **kwargs): # real signature unknown
    pass

def CoUninitialize(*args, **kwargs): # real signature unknown
    pass

def Debugging(*args, **kwargs): # real signature unknown
    pass

def Finalize(*args, **kwargs): # real signature unknown
    pass

def Initialize(*args, **kwargs): # real signature unknown
    pass

def LogErrorMsg(*args, **kwargs): # real signature unknown
    pass

def LogInfoMsg(*args, **kwargs): # real signature unknown
    pass

def LogMsg(*args, **kwargs): # real signature unknown
    pass

def LogWarningMsg(*args, **kwargs): # real signature unknown
    pass

def PrepareToHostMultiple(*args, **kwargs): # real signature unknown
    pass

def PrepareToHostSingle(*args, **kwargs): # real signature unknown
    pass

def PumpWaitingMessages(*args, **kwargs): # real signature unknown
    pass

def RegisterServiceCtrlHandler(*args, **kwargs): # real signature unknown
    pass

def RunningAsService(*args, **kwargs): # real signature unknown
    pass

def SetEventSourceName(*args, **kwargs): # real signature unknown
    pass

def StartServiceCtrlDispatcher(*args, **kwargs): # real signature unknown
    pass

# classes

class startup_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



