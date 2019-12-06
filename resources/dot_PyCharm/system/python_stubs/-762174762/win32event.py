# encoding: utf-8
# module win32event
# from C:\Python27\lib\site-packages\win32\win32event.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

EVENT_ALL_ACCESS = 2031619

EVENT_MODIFY_STATE = 2

INFINITE = -1

MAXIMUM_WAIT_OBJECTS = 64

QS_ALLEVENTS = 1215
QS_ALLINPUT = 1279
QS_HOTKEY = 128
QS_INPUT = 1031
QS_KEY = 1
QS_MOUSE = 6
QS_MOUSEBUTTON = 4
QS_MOUSEMOVE = 2
QS_PAINT = 32
QS_POSTMESSAGE = 8
QS_SENDMESSAGE = 64
QS_TIMER = 16

SYNCHRONIZE = 1048576

UNICODE = 0

WAIT_ABANDONED = 128

WAIT_ABANDONED_0 = 128

WAIT_FAILED = -1

WAIT_IO_COMPLETION = 192

WAIT_OBJECT_0 = 0

WAIT_TIMEOUT = 258

# functions

def CancelWaitableTimer(*args, **kwargs): # real signature unknown
    pass

def CreateEvent(*args, **kwargs): # real signature unknown
    pass

def CreateMutex(*args, **kwargs): # real signature unknown
    pass

def CreateSemaphore(*args, **kwargs): # real signature unknown
    pass

def CreateWaitableTimer(*args, **kwargs): # real signature unknown
    pass

def MsgWaitForMultipleObjects(*args, **kwargs): # real signature unknown
    pass

def MsgWaitForMultipleObjectsEx(*args, **kwargs): # real signature unknown
    pass

def OpenEvent(*args, **kwargs): # real signature unknown
    pass

def OpenMutex(*args, **kwargs): # real signature unknown
    pass

def OpenSemaphore(*args, **kwargs): # real signature unknown
    pass

def OpenWaitableTimer(*args, **kwargs): # real signature unknown
    pass

def PulseEvent(*args, **kwargs): # real signature unknown
    pass

def ReleaseMutex(*args, **kwargs): # real signature unknown
    pass

def ReleaseSemaphore(*args, **kwargs): # real signature unknown
    pass

def ResetEvent(*args, **kwargs): # real signature unknown
    pass

def SetEvent(*args, **kwargs): # real signature unknown
    pass

def SetWaitableTimer(*args, **kwargs): # real signature unknown
    pass

def SignalObjectAndWait(*args, **kwargs): # real signature unknown
    pass

def WaitForInputIdle(*args, **kwargs): # real signature unknown
    pass

def WaitForMultipleObjects(*args, **kwargs): # real signature unknown
    pass

def WaitForMultipleObjectsEx(*args, **kwargs): # real signature unknown
    pass

def WaitForSingleObject(*args, **kwargs): # real signature unknown
    pass

def WaitForSingleObjectEx(*args, **kwargs): # real signature unknown
    pass

# no classes
