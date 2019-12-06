# encoding: utf-8
# module win32print
# from C:\Python27\lib\site-packages\win32\win32print.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

DEF_PRIORITY = 1

DI_APPBANDING = 1

DI_ROPS_READ_DESTINATION = 2

DPD_DELETE_ALL_FILES = 4

DPD_DELETE_SPECIFIC_VERSION = 2

DPD_DELETE_UNUSED_FILES = 1

DSPRINT_PENDING = -2147483648
DSPRINT_PUBLISH = 1
DSPRINT_REPUBLISH = 8
DSPRINT_UNPUBLISH = 4
DSPRINT_UPDATE = 2

FORM_BUILTIN = 1
FORM_PRINTER = 2
FORM_USER = 0

JOB_ACCESS_ADMINISTER = 16
JOB_ACCESS_READ = 32

JOB_ALL_ACCESS = 983088

JOB_CONTROL_CANCEL = 3
JOB_CONTROL_DELETE = 5

JOB_CONTROL_LAST_PAGE_EJECTED = 7

JOB_CONTROL_PAUSE = 1
JOB_CONTROL_RESTART = 4
JOB_CONTROL_RESUME = 2

JOB_CONTROL_SENT_TO_PRINTER = 6

JOB_EXECUTE = 131088

JOB_INFO_1 = 1

JOB_POSITION_UNSPECIFIED = 0

JOB_READ = 131104

JOB_STATUS_BLOCKED_DEVQ = 512

JOB_STATUS_COMPLETE = 4096
JOB_STATUS_DELETED = 256
JOB_STATUS_DELETING = 4
JOB_STATUS_ERROR = 2
JOB_STATUS_OFFLINE = 32
JOB_STATUS_PAPEROUT = 64
JOB_STATUS_PAUSED = 1
JOB_STATUS_PRINTED = 128
JOB_STATUS_PRINTING = 16
JOB_STATUS_RESTART = 2048
JOB_STATUS_SPOOLING = 8

JOB_STATUS_USER_INTERVENTION = 1024

JOB_WRITE = 131088

MAX_PRIORITY = 99

MIN_PRIORITY = 1

PORT_STATUS_DOOR_OPEN = 7

PORT_STATUS_NO_TONER = 6

PORT_STATUS_OFFLINE = 1

PORT_STATUS_OUTPUT_BIN_FULL = 4

PORT_STATUS_OUT_OF_MEMORY = 9

PORT_STATUS_PAPER_JAM = 2
PORT_STATUS_PAPER_OUT = 3
PORT_STATUS_PAPER_PROBLEM = 5

PORT_STATUS_POWER_SAVE = 12

PORT_STATUS_TONER_LOW = 10

PORT_STATUS_TYPE_ERROR = 1
PORT_STATUS_TYPE_INFO = 3
PORT_STATUS_TYPE_WARNING = 2

PORT_STATUS_USER_INTERVENTION = 8

PORT_STATUS_WARMING_UP = 11

PORT_TYPE_NET_ATTACHED = 8

PORT_TYPE_READ = 2
PORT_TYPE_REDIRECTED = 4
PORT_TYPE_WRITE = 1

PRINTER_ACCESS_ADMINISTER = 4
PRINTER_ACCESS_USE = 8

PRINTER_ALL_ACCESS = 983052

PRINTER_ATTRIBUTE_DEFAULT = 4
PRINTER_ATTRIBUTE_DIRECT = 2

PRINTER_ATTRIBUTE_DO_COMPLETE_FIRST = 512

PRINTER_ATTRIBUTE_ENABLE_BIDI = 2048
PRINTER_ATTRIBUTE_ENABLE_DEVQ = 128

PRINTER_ATTRIBUTE_FAX = 16384
PRINTER_ATTRIBUTE_HIDDEN = 32
PRINTER_ATTRIBUTE_KEEPPRINTEDJOBS = 256
PRINTER_ATTRIBUTE_LOCAL = 64
PRINTER_ATTRIBUTE_NETWORK = 16
PRINTER_ATTRIBUTE_PUBLISHED = 8192
PRINTER_ATTRIBUTE_QUEUED = 1

PRINTER_ATTRIBUTE_RAW_ONLY = 4096

PRINTER_ATTRIBUTE_SHARED = 8
PRINTER_ATTRIBUTE_TS = 32768

PRINTER_ATTRIBUTE_WORK_OFFLINE = 1024

PRINTER_CONTROL_PAUSE = 1
PRINTER_CONTROL_PURGE = 3
PRINTER_CONTROL_RESUME = 2

PRINTER_CONTROL_SET_STATUS = 4

PRINTER_ENUM_CONNECTIONS = 4
PRINTER_ENUM_CONTAINER = 32768
PRINTER_ENUM_DEFAULT = 1
PRINTER_ENUM_EXPAND = 16384
PRINTER_ENUM_ICON1 = 65536
PRINTER_ENUM_ICON2 = 131072
PRINTER_ENUM_ICON3 = 262144
PRINTER_ENUM_ICON4 = 524288
PRINTER_ENUM_ICON5 = 1048576
PRINTER_ENUM_ICON6 = 2097152
PRINTER_ENUM_ICON7 = 4194304
PRINTER_ENUM_ICON8 = 8388608
PRINTER_ENUM_LOCAL = 2
PRINTER_ENUM_NAME = 8
PRINTER_ENUM_NETWORK = 64
PRINTER_ENUM_REMOTE = 16
PRINTER_ENUM_SHARED = 32

PRINTER_EXECUTE = 131080

PRINTER_INFO_1 = 1

PRINTER_READ = 131080

PRINTER_STATUS_BUSY = 512

PRINTER_STATUS_DOOR_OPEN = 4194304

PRINTER_STATUS_ERROR = 2
PRINTER_STATUS_INITIALIZING = 32768

PRINTER_STATUS_IO_ACTIVE = 256

PRINTER_STATUS_MANUAL_FEED = 32

PRINTER_STATUS_NOT_AVAILABLE = 4096

PRINTER_STATUS_NO_TONER = 262144

PRINTER_STATUS_OFFLINE = 128

PRINTER_STATUS_OUTPUT_BIN_FULL = 2048

PRINTER_STATUS_OUT_OF_MEMORY = 2097152

PRINTER_STATUS_PAGE_PUNT = 524288

PRINTER_STATUS_PAPER_JAM = 8
PRINTER_STATUS_PAPER_OUT = 16
PRINTER_STATUS_PAPER_PROBLEM = 64

PRINTER_STATUS_PAUSED = 1

PRINTER_STATUS_PENDING_DELETION = 4

PRINTER_STATUS_POWER_SAVE = 16777216

PRINTER_STATUS_PRINTING = 1024
PRINTER_STATUS_PROCESSING = 16384

PRINTER_STATUS_SERVER_UNKNOWN = 8388608

PRINTER_STATUS_TONER_LOW = 131072

PRINTER_STATUS_USER_INTERVENTION = 1048576

PRINTER_STATUS_WAITING = 8192

PRINTER_STATUS_WARMING_UP = 65536

PRINTER_WRITE = 131080

SERVER_ACCESS_ADMINISTER = 1
SERVER_ACCESS_ENUMERATE = 2

SERVER_ALL_ACCESS = 983043

SERVER_EXECUTE = 131074
SERVER_READ = 131074
SERVER_WRITE = 131075

# functions

def AbortDoc(*args, **kwargs): # real signature unknown
    pass

def AbortPrinter(*args, **kwargs): # real signature unknown
    pass

def AddForm(*args, **kwargs): # real signature unknown
    pass

def AddJob(*args, **kwargs): # real signature unknown
    pass

def AddPrinter(*args, **kwargs): # real signature unknown
    pass

def AddPrinterConnection(*args, **kwargs): # real signature unknown
    pass

def ClosePrinter(*args, **kwargs): # real signature unknown
    pass

def DeleteForm(*args, **kwargs): # real signature unknown
    pass

def DeletePrinter(*args, **kwargs): # real signature unknown
    pass

def DeletePrinterConnection(*args, **kwargs): # real signature unknown
    pass

def DeletePrinterDriver(*args, **kwargs): # real signature unknown
    pass

def DeletePrinterDriverEx(*args, **kwargs): # real signature unknown
    pass

def DeviceCapabilities(*args, **kwargs): # real signature unknown
    pass

def DocumentProperties(*args, **kwargs): # real signature unknown
    pass

def EndDoc(*args, **kwargs): # real signature unknown
    pass

def EndDocPrinter(*args, **kwargs): # real signature unknown
    pass

def EndPage(*args, **kwargs): # real signature unknown
    pass

def EndPagePrinter(*args, **kwargs): # real signature unknown
    pass

def EnumForms(*args, **kwargs): # real signature unknown
    pass

def EnumJobs(*args, **kwargs): # real signature unknown
    pass

def EnumMonitors(*args, **kwargs): # real signature unknown
    pass

def EnumPorts(*args, **kwargs): # real signature unknown
    pass

def EnumPrinterDrivers(*args, **kwargs): # real signature unknown
    pass

def EnumPrinters(*args, **kwargs): # real signature unknown
    pass

def EnumPrintProcessorDatatypes(*args, **kwargs): # real signature unknown
    pass

def EnumPrintProcessors(*args, **kwargs): # real signature unknown
    pass

def FlushPrinter(*args, **kwargs): # real signature unknown
    pass

def GetDefaultPrinter(*args, **kwargs): # real signature unknown
    pass

def GetDefaultPrinterW(*args, **kwargs): # real signature unknown
    pass

def GetDeviceCaps(*args, **kwargs): # real signature unknown
    pass

def GetForm(*args, **kwargs): # real signature unknown
    pass

def GetJob(*args, **kwargs): # real signature unknown
    pass

def GetPrinter(*args, **kwargs): # real signature unknown
    pass

def GetPrinterDriverDirectory(*args, **kwargs): # real signature unknown
    pass

def GetPrintProcessorDirectory(*args, **kwargs): # real signature unknown
    pass

def OpenPrinter(*args, **kwargs): # real signature unknown
    pass

def ScheduleJob(*args, **kwargs): # real signature unknown
    pass

def SetDefaultPrinter(*args, **kwargs): # real signature unknown
    pass

def SetDefaultPrinterW(*args, **kwargs): # real signature unknown
    pass

def SetForm(*args, **kwargs): # real signature unknown
    pass

def SetJob(*args, **kwargs): # real signature unknown
    pass

def SetPrinter(*args, **kwargs): # real signature unknown
    pass

def StartDoc(*args, **kwargs): # real signature unknown
    pass

def StartDocPrinter(*args, **kwargs): # real signature unknown
    pass

def StartPage(*args, **kwargs): # real signature unknown
    pass

def StartPagePrinter(*args, **kwargs): # real signature unknown
    pass

def WritePrinter(*args, **kwargs): # real signature unknown
    pass

# no classes
