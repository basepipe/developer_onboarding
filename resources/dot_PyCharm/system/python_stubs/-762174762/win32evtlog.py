# encoding: utf-8
# module win32evtlog
# from C:\Python27\lib\site-packages\win32\win32evtlog.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

EVENTLOG_AUDIT_FAILURE = 16
EVENTLOG_AUDIT_SUCCESS = 8

EVENTLOG_BACKWARDS_READ = 8

EVENTLOG_END_ALL_PAIRED_EVENTS = 4

EVENTLOG_END_PAIRED_EVENT = 2

EVENTLOG_ERROR_TYPE = 1

EVENTLOG_FORWARDS_READ = 4

EVENTLOG_INFORMATION_TYPE = 4

EVENTLOG_PAIRED_EVENT_ACTIVE = 8
EVENTLOG_PAIRED_EVENT_INACTIVE = 16

EVENTLOG_SEEK_READ = 2

EVENTLOG_SEQUENTIAL_READ = 1

EVENTLOG_START_PAIRED_EVENT = 1

EVENTLOG_SUCCESS = 0

EVENTLOG_WARNING_TYPE = 2

EventMetadataEventChannel = 2
EventMetadataEventID = 0
EventMetadataEventKeyword = 6
EventMetadataEventLevel = 3
EventMetadataEventMessageID = 7
EventMetadataEventOpcode = 4
EventMetadataEventTask = 5
EventMetadataEventTemplate = 8
EventMetadataEventVersion = 1
EvtChannelConfigAccess = 5
EvtChannelConfigClassicEventlog = 4
EvtChannelConfigEnabled = 0
EvtChannelConfigIsolation = 1
EvtChannelConfigOwningPublisher = 3
EvtChannelConfigPropertyIdEND = 21
EvtChannelConfigType = 2
EvtChannelLoggingConfigAutoBackup = 7
EvtChannelLoggingConfigLogFilePath = 9
EvtChannelLoggingConfigMaxSize = 8
EvtChannelLoggingConfigRetention = 6
EvtChannelPublisherList = 19
EvtChannelPublishingConfigBufferSize = 13
EvtChannelPublishingConfigClockType = 17
EvtChannelPublishingConfigControlGuid = 12
EvtChannelPublishingConfigKeywords = 11
EvtChannelPublishingConfigLatency = 16
EvtChannelPublishingConfigLevel = 10
EvtChannelPublishingConfigMaxBuffers = 15
EvtChannelPublishingConfigMinBuffers = 14
EvtChannelPublishingConfigSidType = 18
EvtEventMetadataPropertyIdEND = 9
EvtEventPath = 1
EvtEventPropertyIdEND = 2
EvtEventQueryIDs = 0
EvtExportLogChannelPath = 1
EvtExportLogFilePath = 2
EvtExportLogTolerateQueryErrors = 4096
EvtLogAttributes = 4
EvtLogCreationTime = 0
EvtLogFileSize = 3
EvtLogFull = 7
EvtLogLastAccessTime = 1
EvtLogLastWriteTime = 2
EvtLogNumberOfLogRecords = 5
EvtLogOldestRecordNumber = 6
EvtOpenChannelPath = 1
EvtOpenFilePath = 2
EvtPublisherMetadataChannelReferenceFlags = 10
EvtPublisherMetadataChannelReferenceID = 9
EvtPublisherMetadataChannelReferenceIndex = 8
EvtPublisherMetadataChannelReferenceMessageID = 11
EvtPublisherMetadataChannelReferencePath = 7
EvtPublisherMetadataChannelReferences = 6
EvtPublisherMetadataHelpLink = 4
EvtPublisherMetadataKeywordMessageID = 28
EvtPublisherMetadataKeywordName = 26
EvtPublisherMetadataKeywords = 25
EvtPublisherMetadataKeywordValue = 27
EvtPublisherMetadataLevelMessageID = 15
EvtPublisherMetadataLevelName = 13
EvtPublisherMetadataLevels = 12
EvtPublisherMetadataLevelValue = 14
EvtPublisherMetadataMessageFilePath = 3
EvtPublisherMetadataOpcodeMessageID = 24
EvtPublisherMetadataOpcodeName = 22
EvtPublisherMetadataOpcodes = 21
EvtPublisherMetadataOpcodeValue = 23
EvtPublisherMetadataParameterFilePath = 2
EvtPublisherMetadataPropertyIdEND = 29
EvtPublisherMetadataPublisherGuid = 0
EvtPublisherMetadataPublisherMessageID = 5
EvtPublisherMetadataResourceFilePath = 1
EvtPublisherMetadataTaskEventGuid = 18
EvtPublisherMetadataTaskMessageID = 20
EvtPublisherMetadataTaskName = 17
EvtPublisherMetadataTasks = 16
EvtPublisherMetadataTaskValue = 19
EvtQueryChannelPath = 1
EvtQueryFilePath = 2
EvtQueryForwardDirection = 256
EvtQueryReverseDirection = 512
EvtQueryTolerateQueryErrors = 4096
EvtRenderBookmark = 2
EvtRenderEventValues = 0
EvtRenderEventXml = 1
EvtRpcLogin = 1
EvtRpcLoginAuthDefault = 0
EvtRpcLoginAuthKerberos = 2
EvtRpcLoginAuthNegotiate = 1
EvtRpcLoginAuthNTLM = 3
EvtSeekOriginMask = 7
EvtSeekRelativeToBookmark = 4
EvtSeekRelativeToCurrent = 3
EvtSeekRelativeToFirst = 1
EvtSeekRelativeToLast = 2
EvtSeekStrict = 65536
EvtSubscribeActionDeliver = 1
EvtSubscribeActionError = 0
EvtSubscribeOriginMask = 3
EvtSubscribeStartAfterBookmark = 3
EvtSubscribeStartAtOldestRecord = 2
EvtSubscribeStrict = 65536
EvtSubscribeToFutureEvents = 1
EvtSubscribeTolerateQueryErrors = 4096
EvtVarTypeAnsiString = 2
EvtVarTypeBinary = 14
EvtVarTypeBoolean = 13
EvtVarTypeByte = 4
EvtVarTypeDouble = 12
EvtVarTypeEvtHandle = 32
EvtVarTypeEvtXml = 35
EvtVarTypeFileTime = 17
EvtVarTypeGuid = 15
EvtVarTypeHexInt32 = 20
EvtVarTypeHexInt64 = 21
EvtVarTypeInt16 = 5
EvtVarTypeInt32 = 7
EvtVarTypeInt64 = 9
EvtVarTypeNull = 0
EvtVarTypeSByte = 3
EvtVarTypeSid = 19
EvtVarTypeSingle = 11
EvtVarTypeSizeT = 16
EvtVarTypeString = 1
EvtVarTypeSysTime = 18
EvtVarTypeUInt16 = 6
EvtVarTypeUInt32 = 8
EvtVarTypeUInt64 = 10

UNICODE = 0

# functions

def BackupEventLog(*args, **kwargs): # real signature unknown
    pass

def ClearEventLog(*args, **kwargs): # real signature unknown
    pass

def CloseEventLog(*args, **kwargs): # real signature unknown
    pass

def DeregisterEventSource(*args, **kwargs): # real signature unknown
    pass

def EvtArchiveExportedLog(*args, **kwargs): # real signature unknown
    pass

def EvtClearLog(*args, **kwargs): # real signature unknown
    pass

def EvtCreateBookmark(*args, **kwargs): # real signature unknown
    pass

def EvtExportLog(*args, **kwargs): # real signature unknown
    pass

def EvtGetChannelConfigProperty(*args, **kwargs): # real signature unknown
    pass

def EvtGetEventInfo(*args, **kwargs): # real signature unknown
    pass

def EvtGetEventMetadataProperty(*args, **kwargs): # real signature unknown
    pass

def EvtGetExtendedStatus(*args, **kwargs): # real signature unknown
    pass

def EvtGetLogInfo(*args, **kwargs): # real signature unknown
    pass

def EvtGetObjectArrayProperty(*args, **kwargs): # real signature unknown
    pass

def EvtGetObjectArraySize(*args, **kwargs): # real signature unknown
    pass

def EvtGetPublisherMetadataProperty(*args, **kwargs): # real signature unknown
    pass

def EvtNext(*args, **kwargs): # real signature unknown
    pass

def EvtNextChannelPath(*args, **kwargs): # real signature unknown
    pass

def EvtNextEventMetadata(*args, **kwargs): # real signature unknown
    pass

def EvtNextPublisherId(*args, **kwargs): # real signature unknown
    pass

def EvtOpenChannelConfig(*args, **kwargs): # real signature unknown
    pass

def EvtOpenChannelEnum(*args, **kwargs): # real signature unknown
    pass

def EvtOpenEventMetadataEnum(*args, **kwargs): # real signature unknown
    pass

def EvtOpenLog(*args, **kwargs): # real signature unknown
    pass

def EvtOpenPublisherEnum(*args, **kwargs): # real signature unknown
    pass

def EvtOpenPublisherMetadata(*args, **kwargs): # real signature unknown
    pass

def EvtOpenSession(*args, **kwargs): # real signature unknown
    pass

def EvtQuery(*args, **kwargs): # real signature unknown
    pass

def EvtRender(*args, **kwargs): # real signature unknown
    pass

def EvtSeek(*args, **kwargs): # real signature unknown
    pass

def EvtSubscribe(*args, **kwargs): # real signature unknown
    pass

def EvtUpdateBookmark(*args, **kwargs): # real signature unknown
    pass

def GetNumberOfEventLogRecords(*args, **kwargs): # real signature unknown
    pass

def GetOldestEventLogRecord(*args, **kwargs): # real signature unknown
    pass

def NotifyChangeEventLog(*args, **kwargs): # real signature unknown
    pass

def OpenBackupEventLog(*args, **kwargs): # real signature unknown
    pass

def OpenEventLog(*args, **kwargs): # real signature unknown
    pass

def ReadEventLog(*args, **kwargs): # real signature unknown
    pass

def RegisterEventSource(*args, **kwargs): # real signature unknown
    pass

def ReportEvent(*args, **kwargs): # real signature unknown
    pass

# no classes
