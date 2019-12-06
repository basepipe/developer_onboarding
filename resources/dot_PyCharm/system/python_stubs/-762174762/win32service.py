# encoding: utf-8
# module win32service
# from C:\Python27\lib\site-packages\win32\win32service.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

DBT_CONFIGCHANGECANCELED = 25
DBT_CONFIGCHANGED = 24
DBT_CUSTOMEVENT = 32774
DBT_DEVICEARRIVAL = 32768
DBT_DEVICEQUERYREMOVE = 32769
DBT_DEVICEQUERYREMOVEFAILED = 32770
DBT_DEVICEREMOVECOMPLETE = 32772
DBT_DEVICEREMOVEPENDING = 32771
DBT_DEVICETYPESPECIFIC = 32773
DBT_QUERYCHANGECONFIG = 23

DF_ALLOWOTHERACCOUNTHOOK = 1

SC_ACTION_NONE = 0
SC_ACTION_REBOOT = 2
SC_ACTION_RESTART = 1

SC_ACTION_RUN_COMMAND = 3

SC_ENUM_PROCESS_INFO = 0

SC_GROUP_IDENTIFIER = 43

SC_MANAGER_ALL_ACCESS = 983103

SC_MANAGER_CONNECT = 1

SC_MANAGER_CREATE_SERVICE = 2

SC_MANAGER_ENUMERATE_SERVICE = 4

SC_MANAGER_LOCK = 8

SC_MANAGER_MODIFY_BOOT_CONFIG = 32

SC_MANAGER_QUERY_LOCK_STATUS = 16

SERVICE_ACCEPT_HARDWAREPROFILECHANGE = 32
SERVICE_ACCEPT_NETBINDCHANGE = 16
SERVICE_ACCEPT_PARAMCHANGE = 8

SERVICE_ACCEPT_PAUSE_CONTINUE = 2

SERVICE_ACCEPT_POWEREVENT = 64
SERVICE_ACCEPT_PRESHUTDOWN = 256
SERVICE_ACCEPT_SESSIONCHANGE = 128
SERVICE_ACCEPT_SHUTDOWN = 4
SERVICE_ACCEPT_STOP = 1

SERVICE_ACTIVE = 1

SERVICE_ALL_ACCESS = 983551

SERVICE_AUTO_START = 2

SERVICE_BOOT_START = 0

SERVICE_CHANGE_CONFIG = 2

SERVICE_CONFIG_DELAYED_AUTO_START_INFO = 3

SERVICE_CONFIG_DESCRIPTION = 1

SERVICE_CONFIG_FAILURE_ACTIONS = 2

SERVICE_CONFIG_FAILURE_ACTIONS_FLAG = 4

SERVICE_CONFIG_PRESHUTDOWN_INFO = 7

SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO = 6

SERVICE_CONFIG_SERVICE_SID_INFO = 5

SERVICE_CONTINUE_PENDING = 5

SERVICE_CONTROL_CONTINUE = 3
SERVICE_CONTROL_DEVICEEVENT = 11
SERVICE_CONTROL_HARDWAREPROFILECHANGE = 12
SERVICE_CONTROL_INTERROGATE = 4
SERVICE_CONTROL_NETBINDADD = 7
SERVICE_CONTROL_NETBINDDISABLE = 10
SERVICE_CONTROL_NETBINDENABLE = 9
SERVICE_CONTROL_NETBINDREMOVE = 8
SERVICE_CONTROL_PARAMCHANGE = 6
SERVICE_CONTROL_PAUSE = 2
SERVICE_CONTROL_POWEREVENT = 13
SERVICE_CONTROL_PRESHUTDOWN = 15
SERVICE_CONTROL_SESSIONCHANGE = 14
SERVICE_CONTROL_SHUTDOWN = 5
SERVICE_CONTROL_STOP = 1

SERVICE_DEMAND_START = 3

SERVICE_DISABLED = 4
SERVICE_DRIVER = 11

SERVICE_ENUMERATE_DEPENDENTS = 8

SERVICE_ERROR_CRITICAL = 3
SERVICE_ERROR_IGNORE = 0
SERVICE_ERROR_NORMAL = 1
SERVICE_ERROR_SEVERE = 2

SERVICE_FILE_SYSTEM_DRIVER = 2

SERVICE_INACTIVE = 2

SERVICE_INTERACTIVE_PROCESS = 256

SERVICE_INTERROGATE = 128

SERVICE_KERNEL_DRIVER = 1

SERVICE_NO_CHANGE = -1

SERVICE_PAUSED = 7

SERVICE_PAUSE_CONTINUE = 64
SERVICE_PAUSE_PENDING = 6

SERVICE_QUERY_CONFIG = 1
SERVICE_QUERY_STATUS = 4

SERVICE_RUNNING = 4

SERVICE_SID_TYPE_NONE = 0
SERVICE_SID_TYPE_RESTRICTED = 3
SERVICE_SID_TYPE_UNRESTRICTED = 1

SERVICE_SPECIFIC_ERROR = 1066

SERVICE_START = 16

SERVICE_START_PENDING = 2

SERVICE_STATE_ALL = 3

SERVICE_STOP = 32
SERVICE_STOPPED = 1

SERVICE_STOP_PENDING = 3

SERVICE_SYSTEM_START = 1

SERVICE_USER_DEFINED_CONTROL = 256

SERVICE_WIN32 = 48

SERVICE_WIN32_OWN_PROCESS = 16

SERVICE_WIN32_SHARE_PROCESS = 32

UNICODE = 1

UOI_FLAGS = 1
UOI_NAME = 2
UOI_TYPE = 3

UOI_USER_SID = 4

WSF_VISIBLE = 1

# functions

def ChangeServiceConfig(*args, **kwargs): # real signature unknown
    pass

def ChangeServiceConfig2(*args, **kwargs): # real signature unknown
    pass

def CloseServiceHandle(*args, **kwargs): # real signature unknown
    pass

def ControlService(*args, **kwargs): # real signature unknown
    pass

def CreateDesktop(*args, **kwargs): # real signature unknown
    pass

def CreateService(*args, **kwargs): # real signature unknown
    pass

def CreateWindowStation(*args, **kwargs): # real signature unknown
    pass

def DeleteService(*args, **kwargs): # real signature unknown
    pass

def EnumDependentServices(*args, **kwargs): # real signature unknown
    pass

def EnumServicesStatus(*args, **kwargs): # real signature unknown
    pass

def EnumServicesStatusEx(*args, **kwargs): # real signature unknown
    pass

def EnumWindowStations(*args, **kwargs): # real signature unknown
    pass

def GetProcessWindowStation(*args, **kwargs): # real signature unknown
    pass

def GetServiceDisplayName(*args, **kwargs): # real signature unknown
    pass

def GetServiceKeyName(*args, **kwargs): # real signature unknown
    pass

def GetThreadDesktop(*args, **kwargs): # real signature unknown
    pass

def GetUserObjectInformation(*args, **kwargs): # real signature unknown
    pass

def LockServiceDatabase(*args, **kwargs): # real signature unknown
    pass

def OpenDesktop(*args, **kwargs): # real signature unknown
    pass

def OpenInputDesktop(*args, **kwargs): # real signature unknown
    pass

def OpenSCManager(*args, **kwargs): # real signature unknown
    pass

def OpenService(*args, **kwargs): # real signature unknown
    pass

def OpenWindowStation(*args, **kwargs): # real signature unknown
    pass

def QueryServiceConfig(*args, **kwargs): # real signature unknown
    pass

def QueryServiceConfig2(*args, **kwargs): # real signature unknown
    pass

def QueryServiceLockStatus(*args, **kwargs): # real signature unknown
    pass

def QueryServiceObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def QueryServiceStatus(*args, **kwargs): # real signature unknown
    pass

def QueryServiceStatusEx(*args, **kwargs): # real signature unknown
    pass

def SetServiceObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def SetServiceStatus(*args, **kwargs): # real signature unknown
    pass

def SetUserObjectInformation(*args, **kwargs): # real signature unknown
    pass

def StartService(*args, **kwargs): # real signature unknown
    pass

def UnlockServiceDatabase(*args, **kwargs): # real signature unknown
    pass

# classes

class HDESKType(object):
    # no doc
    def CloseDesktop(self, *args, **kwargs): # real signature unknown
        """ Closes the handle """
        pass

    def Detach(self, *args, **kwargs): # real signature unknown
        """ Releases reference to handle without closing it """
        pass

    def EnumDesktopWindows(self, *args, **kwargs): # real signature unknown
        """ Lists all top-level windows on the desktop """
        pass

    def SetThreadDesktop(self, *args, **kwargs): # real signature unknown
        """ Assigns desktop to calling thread """
        pass

    def SwitchDesktop(self, *args, **kwargs): # real signature unknown
        """ Activates the desktop """
        pass

    def __abs__(self): # real signature unknown; restored from __doc__
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hex__(self): # real signature unknown; restored from __doc__
        """ x.__hex__() <==> hex(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __invert__(self): # real signature unknown; restored from __doc__
        """ x.__invert__() <==> ~x """
        pass

    def __long__(self): # real signature unknown; restored from __doc__
        """ x.__long__() <==> long(x) """
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __oct__(self): # real signature unknown; restored from __doc__
        """ x.__oct__() <==> oct(x) """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdivmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass


class HWINSTAType(object):
    # no doc
    def CloseWindowStation(self, *args, **kwargs): # real signature unknown
        """ Closes the window station handle """
        pass

    def Detach(self, *args, **kwargs): # real signature unknown
        """ Releases reference to handle without closing it """
        pass

    def EnumDesktops(self, *args, **kwargs): # real signature unknown
        """ List desktop names within the window station """
        pass

    def SetProcessWindowStation(self, *args, **kwargs): # real signature unknown
        """ Associates the calling process with the window station """
        pass

    def __abs__(self): # real signature unknown; restored from __doc__
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hex__(self): # real signature unknown; restored from __doc__
        """ x.__hex__() <==> hex(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __invert__(self): # real signature unknown; restored from __doc__
        """ x.__invert__() <==> ~x """
        pass

    def __long__(self): # real signature unknown; restored from __doc__
        """ x.__long__() <==> long(x) """
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __oct__(self): # real signature unknown; restored from __doc__
        """ x.__oct__() <==> oct(x) """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdivmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass


