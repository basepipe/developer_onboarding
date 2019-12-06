# encoding: utf-8
# module win32file
# from C:\Python27\lib\site-packages\win32\win32file.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

CALLBACK_CHUNK_FINISHED = 0

CALLBACK_STREAM_SWITCH = 1

CBR_110 = 110
CBR_115200 = 115200
CBR_1200 = 1200
CBR_128000 = 128000
CBR_14400 = 14400
CBR_19200 = 19200
CBR_2400 = 2400
CBR_256000 = 256000
CBR_300 = 300
CBR_38400 = 38400
CBR_4800 = 4800
CBR_56000 = 56000
CBR_57600 = 57600
CBR_600 = 600
CBR_9600 = 9600

CLRBREAK = 9
CLRDTR = 6
CLRRTS = 4

COPY_FILE_ALLOW_DECRYPTED_DESTINATION = 8

COPY_FILE_FAIL_IF_EXISTS = 1

COPY_FILE_OPEN_SOURCE_FOR_WRITE = 4

COPY_FILE_RESTARTABLE = 2

CREATE_ALWAYS = 2

CREATE_FOR_DIR = 2
CREATE_FOR_IMPORT = 1

CREATE_NEW = 1

DRIVE_CDROM = 5
DRIVE_FIXED = 3

DRIVE_NO_ROOT_DIR = 1

DRIVE_RAMDISK = 6
DRIVE_REMOTE = 4
DRIVE_REMOVABLE = 2
DRIVE_UNKNOWN = 0

DTR_CONTROL_DISABLE = 0
DTR_CONTROL_ENABLE = 1
DTR_CONTROL_HANDSHAKE = 2

EVENPARITY = 2
EV_BREAK = 64
EV_CTS = 8
EV_DSR = 16
EV_ERR = 128
EV_RING = 256
EV_RLSD = 32
EV_RXCHAR = 1
EV_RXFLAG = 2
EV_TXEMPTY = 4

FD_ACCEPT = 8

FD_ADDRESS_LIST_CHANGE = 512

FD_CLOSE = 32
FD_CONNECT = 16

FD_GROUP_QOS = 128

FD_OOB = 4
FD_QOS = 64
FD_READ = 1

FD_ROUTING_INTERFACE_CHANGE = 256

FD_WRITE = 2

FileAllocationInfo = 5
FileAttributeTagInfo = 9
FileBasicInfo = 0
FileCompressionInfo = 8
FileDispositionInfo = 4
FileEndOfFileInfo = 6
FileIdBothDirectoryInfo = 10
FileIdBothDirectoryRestartInfo = 11
FileIdType = 0
FileIoPriorityHintInfo = 12
FileNameInfo = 2
FileRenameInfo = 3
FileStandardInfo = 1
FileStreamInfo = 7

FILE_ALL_ACCESS = 2032127

FILE_ATTRIBUTE_ARCHIVE = 32
FILE_ATTRIBUTE_COMPRESSED = 2048
FILE_ATTRIBUTE_DIRECTORY = 16
FILE_ATTRIBUTE_HIDDEN = 2
FILE_ATTRIBUTE_NORMAL = 128
FILE_ATTRIBUTE_OFFLINE = 4096
FILE_ATTRIBUTE_READONLY = 1
FILE_ATTRIBUTE_SYSTEM = 4
FILE_ATTRIBUTE_TEMPORARY = 256

FILE_BEGIN = 0
FILE_CURRENT = 1
FILE_ENCRYPTABLE = 0
FILE_END = 2

FILE_FLAG_BACKUP_SEMANTICS = 33554432

FILE_FLAG_DELETE_ON_CLOSE = 67108864

FILE_FLAG_NO_BUFFERING = 536870912

FILE_FLAG_OPEN_REPARSE_POINT = 2097152

FILE_FLAG_OVERLAPPED = 1073741824

FILE_FLAG_POSIX_SEMANTICS = 16777216

FILE_FLAG_RANDOM_ACCESS = 268435456

FILE_FLAG_SEQUENTIAL_SCAN = 134217728

FILE_FLAG_WRITE_THROUGH = -2147483648

FILE_GENERIC_READ = 1179785
FILE_GENERIC_WRITE = 1179926

FILE_IS_ENCRYPTED = 1

FILE_READ_ONLY = 8

FILE_ROOT_DIR = 3

FILE_SHARE_DELETE = 4
FILE_SHARE_READ = 1
FILE_SHARE_WRITE = 2

FILE_SYSTEM_ATTR = 2
FILE_SYSTEM_DIR = 4

FILE_SYSTEM_NOT_SUPPORT = 6

FILE_TYPE_CHAR = 2
FILE_TYPE_DISK = 1
FILE_TYPE_PIPE = 3
FILE_TYPE_UNKNOWN = 0

FILE_UNKNOWN = 5

FILE_USER_DISALLOWED = 7

GENERIC_EXECUTE = 536870912
GENERIC_READ = -2147483648
GENERIC_WRITE = 1073741824

GetFileExInfoStandard = 1

INVALID_HANDLE_VALUE = -1L

IoPriorityHintLow = 1
IoPriorityHintNormal = 2
IoPriorityHintVeryLow = 0

MARKPARITY = 3

MOVEFILE_COPY_ALLOWED = 2

MOVEFILE_CREATE_HARDLINK = 16

MOVEFILE_DELAY_UNTIL_REBOOT = 4

MOVEFILE_FAIL_IF_NOT_TRACKABLE = 32

MOVEFILE_REPLACE_EXISTING = 1

MOVEFILE_WRITE_THROUGH = 8

NOPARITY = 0

ObjectIdType = 1

ODDPARITY = 1

ONE5STOPBITS = 1
ONESTOPBIT = 0

OPEN_ALWAYS = 4
OPEN_EXISTING = 3

OVERWRITE_HIDDEN = 4

PROGRESS_CANCEL = 1
PROGRESS_CONTINUE = 0
PROGRESS_QUIET = 3
PROGRESS_STOP = 2

PURGE_RXABORT = 2
PURGE_RXCLEAR = 8
PURGE_TXABORT = 1
PURGE_TXCLEAR = 4

REPLACEFILE_IGNORE_MERGE_ERRORS = 2

REPLACEFILE_WRITE_THROUGH = 1

RTS_CONTROL_DISABLE = 0
RTS_CONTROL_ENABLE = 1
RTS_CONTROL_HANDSHAKE = 2
RTS_CONTROL_TOGGLE = 3

SCS_32BIT_BINARY = 0

SCS_DOS_BINARY = 1

SCS_OS216_BINARY = 5

SCS_PIF_BINARY = 3

SCS_POSIX_BINARY = 4

SCS_WOW_BINARY = 2

SECURITY_ANONYMOUS = 0

SECURITY_CONTEXT_TRACKING = 262144

SECURITY_DELEGATION = 196608

SECURITY_EFFECTIVE_ONLY = 524288

SECURITY_IDENTIFICATION = 65536
SECURITY_IMPERSONATION = 131072

SETBREAK = 8
SETDTR = 5
SETRTS = 3
SETXOFF = 1
SETXON = 2

SO_CONNECT_TIME = 28684

SO_UPDATE_ACCEPT_CONTEXT = 28683

SO_UPDATE_CONNECT_CONTEXT = 28688

SPACEPARITY = 4

SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE = 2

SYMBOLIC_LINK_FLAG_DIRECTORY = 1

TF_DISCONNECT = 1

TF_REUSE_SOCKET = 2

TF_USE_DEFAULT_WORKER = 0

TF_USE_KERNEL_APC = 32

TF_USE_SYSTEM_THREAD = 16

TF_WRITE_BEHIND = 4

TRUNCATE_EXISTING = 5

TWOSTOPBITS = 2

UNICODE = 0

WSAECONNABORTED = 10053
WSAECONNRESET = 10054
WSAEDISCON = 10101
WSAEFAULT = 10014
WSAEINPROGRESS = 10036
WSAEINTR = 10004
WSAEINVAL = 10022
WSAEMSGSIZE = 10040
WSAENETDOWN = 10050
WSAENETRESET = 10052
WSAENOBUFS = 10055
WSAENOTCONN = 10057
WSAENOTSOCK = 10038
WSAEOPNOTSUPP = 10045
WSAESHUTDOWN = 10058
WSAEWOULDBLOCK = 10035

WSA_IO_PENDING = 997

WSA_OPERATION_ABORTED = 995

# functions

def AcceptEx(*args, **kwargs): # real signature unknown
    pass

def AddUsersToEncryptedFile(*args, **kwargs): # real signature unknown
    pass

def AllocateReadBuffer(*args, **kwargs): # real signature unknown
    pass

def AreFileApisANSI(*args, **kwargs): # real signature unknown
    pass

def BackupRead(*args, **kwargs): # real signature unknown
    pass

def BackupSeek(*args, **kwargs): # real signature unknown
    pass

def BackupWrite(*args, **kwargs): # real signature unknown
    pass

def BuildCommDCB(*args, **kwargs): # real signature unknown
    pass

def CalculateSocketEndPointSize(*args, **kwargs): # real signature unknown
    pass

def CancelIo(*args, **kwargs): # real signature unknown
    pass

def ClearCommBreak(*args, **kwargs): # real signature unknown
    pass

def ClearCommError(*args, **kwargs): # real signature unknown
    pass

def CloseEncryptedFileRaw(*args, **kwargs): # real signature unknown
    pass

def CloseHandle(*args, **kwargs): # real signature unknown
    pass

def ConnectEx(*args, **kwargs): # real signature unknown
    pass

def CopyFile(*args, **kwargs): # real signature unknown
    pass

def CopyFileEx(*args, **kwargs): # real signature unknown
    pass

def CopyFileW(*args, **kwargs): # real signature unknown
    pass

def CreateDirectory(*args, **kwargs): # real signature unknown
    pass

def CreateDirectoryEx(*args, **kwargs): # real signature unknown
    pass

def CreateDirectoryExW(*args, **kwargs): # real signature unknown
    pass

def CreateDirectoryW(*args, **kwargs): # real signature unknown
    pass

def CreateFile(*args, **kwargs): # real signature unknown
    pass

def CreateFileW(*args, **kwargs): # real signature unknown
    pass

def CreateHardLink(*args, **kwargs): # real signature unknown
    pass

def CreateIoCompletionPort(*args, **kwargs): # real signature unknown
    pass

def CreateMailslot(*args, **kwargs): # real signature unknown
    pass

def CreateSymbolicLink(*args, **kwargs): # real signature unknown
    pass

def DCB(*args, **kwargs): # real signature unknown
    pass

def DecryptFile(*args, **kwargs): # real signature unknown
    pass

def DefineDosDevice(*args, **kwargs): # real signature unknown
    pass

def DefineDosDeviceW(*args, **kwargs): # real signature unknown
    pass

def DeleteFile(*args, **kwargs): # real signature unknown
    pass

def DeleteFileW(*args, **kwargs): # real signature unknown
    pass

def DeleteVolumeMountPoint(*args, **kwargs): # real signature unknown
    pass

def DeviceIoControl(*args, **kwargs): # real signature unknown
    pass

def DuplicateEncryptionInfoFile(*args, **kwargs): # real signature unknown
    pass

def EncryptFile(*args, **kwargs): # real signature unknown
    pass

def EncryptionDisable(*args, **kwargs): # real signature unknown
    pass

def EscapeCommFunction(*args, **kwargs): # real signature unknown
    pass

def FileEncryptionStatus(*args, **kwargs): # real signature unknown
    pass

def FILE_NOTIFY_INFORMATION(*args, **kwargs): # real signature unknown
    pass

def FindClose(*args, **kwargs): # real signature unknown
    pass

def FindCloseChangeNotification(*args, **kwargs): # real signature unknown
    pass

def FindFileNames(*args, **kwargs): # real signature unknown
    pass

def FindFilesIterator(*args, **kwargs): # real signature unknown
    pass

def FindFilesW(*args, **kwargs): # real signature unknown
    pass

def FindFirstChangeNotification(*args, **kwargs): # real signature unknown
    pass

def FindNextChangeNotification(*args, **kwargs): # real signature unknown
    pass

def FindStreams(*args, **kwargs): # real signature unknown
    pass

def FlushFileBuffers(*args, **kwargs): # real signature unknown
    pass

def GetAcceptExSockaddrs(*args, **kwargs): # real signature unknown
    pass

def GetBinaryType(*args, **kwargs): # real signature unknown
    pass

def GetCommMask(*args, **kwargs): # real signature unknown
    pass

def GetCommModemStatus(*args, **kwargs): # real signature unknown
    pass

def GetCommState(*args, **kwargs): # real signature unknown
    pass

def GetCommTimeouts(*args, **kwargs): # real signature unknown
    pass

def GetCompressedFileSize(*args, **kwargs): # real signature unknown
    pass

def GetDiskFreeSpace(*args, **kwargs): # real signature unknown
    pass

def GetDiskFreeSpaceEx(*args, **kwargs): # real signature unknown
    pass

def GetDriveType(*args, **kwargs): # real signature unknown
    pass

def GetDriveTypeW(*args, **kwargs): # real signature unknown
    pass

def GetFileAttributes(*args, **kwargs): # real signature unknown
    pass

def GetFileAttributesEx(*args, **kwargs): # real signature unknown
    pass

def GetFileAttributesExW(*args, **kwargs): # real signature unknown
    pass

def GetFileAttributesW(*args, **kwargs): # real signature unknown
    pass

def GetFileInformationByHandle(*args, **kwargs): # real signature unknown
    pass

def GetFileInformationByHandleEx(*args, **kwargs): # real signature unknown
    pass

def GetFileSize(*args, **kwargs): # real signature unknown
    pass

def GetFileTime(*args, **kwargs): # real signature unknown
    pass

def GetFileType(*args, **kwargs): # real signature unknown
    pass

def GetFinalPathNameByHandle(*args, **kwargs): # real signature unknown
    pass

def GetFullPathName(*args, **kwargs): # real signature unknown
    pass

def GetLogicalDrives(*args, **kwargs): # real signature unknown
    pass

def GetLongPathName(*args, **kwargs): # real signature unknown
    pass

def GetMailslotInfo(*args, **kwargs): # real signature unknown
    pass

def GetOverlappedResult(*args, **kwargs): # real signature unknown
    pass

def GetQueuedCompletionStatus(*args, **kwargs): # real signature unknown
    pass

def GetVolumeNameForVolumeMountPoint(*args, **kwargs): # real signature unknown
    pass

def GetVolumePathName(*args, **kwargs): # real signature unknown
    pass

def GetVolumePathNamesForVolumeName(*args, **kwargs): # real signature unknown
    pass

def LockFile(*args, **kwargs): # real signature unknown
    pass

def LockFileEx(*args, **kwargs): # real signature unknown
    pass

def MoveFile(*args, **kwargs): # real signature unknown
    pass

def MoveFileEx(*args, **kwargs): # real signature unknown
    pass

def MoveFileExW(*args, **kwargs): # real signature unknown
    pass

def MoveFileW(*args, **kwargs): # real signature unknown
    pass

def MoveFileWithProgress(*args, **kwargs): # real signature unknown
    pass

def OpenEncryptedFileRaw(*args, **kwargs): # real signature unknown
    pass

def OpenFileById(*args, **kwargs): # real signature unknown
    pass

def OVERLAPPED(*args, **kwargs): # real signature unknown
    pass

def PostQueuedCompletionStatus(*args, **kwargs): # real signature unknown
    pass

def PurgeComm(*args, **kwargs): # real signature unknown
    pass

def QueryDosDevice(*args, **kwargs): # real signature unknown
    pass

def QueryRecoveryAgentsOnEncryptedFile(*args, **kwargs): # real signature unknown
    pass

def QueryUsersOnEncryptedFile(*args, **kwargs): # real signature unknown
    pass

def ReadDirectoryChangesW(*args, **kwargs): # real signature unknown
    pass

def ReadEncryptedFileRaw(*args, **kwargs): # real signature unknown
    pass

def ReadFile(*args, **kwargs): # real signature unknown
    pass

def RemoveDirectory(*args, **kwargs): # real signature unknown
    pass

def RemoveUsersFromEncryptedFile(*args, **kwargs): # real signature unknown
    pass

def ReOpenFile(*args, **kwargs): # real signature unknown
    pass

def ReplaceFile(*args, **kwargs): # real signature unknown
    pass

def SetCommBreak(*args, **kwargs): # real signature unknown
    pass

def SetCommMask(*args, **kwargs): # real signature unknown
    pass

def SetCommState(*args, **kwargs): # real signature unknown
    pass

def SetCommTimeouts(*args, **kwargs): # real signature unknown
    pass

def SetCurrentDirectory(*args, **kwargs): # real signature unknown
    pass

def SetEndOfFile(*args, **kwargs): # real signature unknown
    pass

def SetFileApisToANSI(*args, **kwargs): # real signature unknown
    pass

def SetFileApisToOEM(*args, **kwargs): # real signature unknown
    pass

def SetFileAttributes(*args, **kwargs): # real signature unknown
    pass

def SetFileAttributesW(*args, **kwargs): # real signature unknown
    pass

def SetFileInformationByHandle(*args, **kwargs): # real signature unknown
    pass

def SetFilePointer(*args, **kwargs): # real signature unknown
    pass

def SetFileShortName(*args, **kwargs): # real signature unknown
    pass

def SetFileTime(*args, **kwargs): # real signature unknown
    pass

def SetMailslotInfo(*args, **kwargs): # real signature unknown
    pass

def SetupComm(*args, **kwargs): # real signature unknown
    pass

def SetVolumeLabel(*args, **kwargs): # real signature unknown
    pass

def SetVolumeMountPoint(*args, **kwargs): # real signature unknown
    pass

def SfcGetNextProtectedFile(*args, **kwargs): # real signature unknown
    pass

def SfcIsFileProtected(*args, **kwargs): # real signature unknown
    pass

def TransmitCommChar(*args, **kwargs): # real signature unknown
    pass

def TransmitFile(*args, **kwargs): # real signature unknown
    pass

def UnlockFile(*args, **kwargs): # real signature unknown
    pass

def UnlockFileEx(*args, **kwargs): # real signature unknown
    pass

def WaitCommEvent(*args, **kwargs): # real signature unknown
    pass

def Wow64DisableWow64FsRedirection(*args, **kwargs): # real signature unknown
    pass

def Wow64RevertWow64FsRedirection(*args, **kwargs): # real signature unknown
    pass

def WriteEncryptedFileRaw(*args, **kwargs): # real signature unknown
    pass

def WriteFile(*args, **kwargs): # real signature unknown
    pass

def WSAAsyncSelect(*args, **kwargs): # real signature unknown
    pass

def WSAEnumNetworkEvents(*args, **kwargs): # real signature unknown
    pass

def WSAEventSelect(*args, **kwargs): # real signature unknown
    pass

def WSARecv(*args, **kwargs): # real signature unknown
    pass

def WSASend(*args, **kwargs): # real signature unknown
    pass

def _getmaxstdio(*args, **kwargs): # real signature unknown
    pass

def _get_osfhandle(*args, **kwargs): # real signature unknown
    pass

def _open_osfhandle(*args, **kwargs): # real signature unknown
    pass

def _setmaxstdio(*args, **kwargs): # real signature unknown
    pass

# no classes
