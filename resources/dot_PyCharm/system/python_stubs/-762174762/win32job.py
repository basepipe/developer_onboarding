# encoding: utf-8
# module win32job
# from C:\Python27\lib\site-packages\win32\win32job.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

JobObjectAssociateCompletionPortInformation = 7
JobObjectBasicAccountingInformation = 1
JobObjectBasicAndIoAccountingInformation = 8
JobObjectBasicLimitInformation = 2
JobObjectBasicProcessIdList = 3
JobObjectBasicUIRestrictions = 4
JobObjectEndOfJobTimeInformation = 6
JobObjectExtendedLimitInformation = 9
JobObjectJobSetInformation = 10
JobObjectSecurityLimitInformation = 5

JOB_OBJECT_ALL_ACCESS = 2031647

JOB_OBJECT_ASSIGN_PROCESS = 1

JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS = 255

JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS = 32767

JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 8

JOB_OBJECT_LIMIT_AFFINITY = 16

JOB_OBJECT_LIMIT_BREAKAWAY_OK = 2048

JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION = 1024

JOB_OBJECT_LIMIT_JOB_MEMORY = 512
JOB_OBJECT_LIMIT_JOB_TIME = 4

JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 8192

JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME = 64

JOB_OBJECT_LIMIT_PRIORITY_CLASS = 32

JOB_OBJECT_LIMIT_PROCESS_MEMORY = 256
JOB_OBJECT_LIMIT_PROCESS_TIME = 2

JOB_OBJECT_LIMIT_SCHEDULING_CLASS = 128

JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK = 4096

JOB_OBJECT_LIMIT_VALID_FLAGS = 524287

JOB_OBJECT_LIMIT_WORKINGSET = 1

JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS = 8

JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT = 3
JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO = 4

JOB_OBJECT_MSG_END_OF_JOB_TIME = 1

JOB_OBJECT_MSG_END_OF_PROCESS_TIME = 2

JOB_OBJECT_MSG_EXIT_PROCESS = 7

JOB_OBJECT_MSG_JOB_MEMORY_LIMIT = 10

JOB_OBJECT_MSG_NEW_PROCESS = 6

JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT = 9

JOB_OBJECT_POST_AT_END_OF_JOB = 1

JOB_OBJECT_QUERY = 4

JOB_OBJECT_RESERVED_LIMIT_VALID_FLAGS = 524287

JOB_OBJECT_SECURITY_FILTER_TOKENS = 8

JOB_OBJECT_SECURITY_NO_ADMIN = 1

JOB_OBJECT_SECURITY_ONLY_TOKEN = 4

JOB_OBJECT_SECURITY_RESTRICTED_TOKEN = 2

JOB_OBJECT_SECURITY_VALID_FLAGS = 15

JOB_OBJECT_SET_ATTRIBUTES = 2

JOB_OBJECT_SET_SECURITY_ATTRIBUTES = 16

JOB_OBJECT_TERMINATE = 8

JOB_OBJECT_TERMINATE_AT_END_OF_JOB = 0

JOB_OBJECT_UILIMIT_ALL = 255
JOB_OBJECT_UILIMIT_DESKTOP = 64
JOB_OBJECT_UILIMIT_DISPLAYSETTINGS = 16
JOB_OBJECT_UILIMIT_EXITWINDOWS = 128
JOB_OBJECT_UILIMIT_GLOBALATOMS = 32
JOB_OBJECT_UILIMIT_HANDLES = 1
JOB_OBJECT_UILIMIT_NONE = 0
JOB_OBJECT_UILIMIT_READCLIPBOARD = 2
JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS = 8
JOB_OBJECT_UILIMIT_WRITECLIPBOARD = 4

JOB_OBJECT_UI_VALID_FLAGS = 255

MaxJobObjectInfoClass = 27

UNICODE = 1

# functions

def AssignProcessToJobObject(*args, **kwargs): # real signature unknown
    pass

def CreateJobObject(*args, **kwargs): # real signature unknown
    pass

def IsProcessInJob(*args, **kwargs): # real signature unknown
    pass

def OpenJobObject(*args, **kwargs): # real signature unknown
    pass

def QueryInformationJobObject(*args, **kwargs): # real signature unknown
    pass

def SetInformationJobObject(*args, **kwargs): # real signature unknown
    pass

def TerminateJobObject(*args, **kwargs): # real signature unknown
    pass

def UserHandleGrantAccess(*args, **kwargs): # real signature unknown
    pass

# no classes
