# encoding: utf-8
# module win32ts
# from C:\Python27\lib\site-packages\win32\win32ts.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

NOTIFY_FOR_ALL_SESSIONS = 1

NOTIFY_FOR_THIS_SESSION = 0

WTSActive = 0
WTSApplicationName = 1
WTSClientAddress = 14
WTSClientBuildNumber = 9
WTSClientDirectory = 11
WTSClientDisplay = 15
WTSClientHardwareId = 13
WTSClientName = 10
WTSClientProductId = 12
WTSClientProtocolType = 16
WTSConnected = 1
WTSConnectQuery = 2
WTSConnectState = 8
WTSDisconnected = 4
WTSDomainName = 7
WTSDown = 8
WTSIdle = 5
WTSInit = 9
WTSInitialProgram = 0
WTSListen = 6
WTSOEMId = 3
WTSReset = 7
WTSSessionId = 4
WTSShadow = 3
WTSUserConfigBrokenTimeoutSettings = 10
WTSUserConfigfAllowLogonTerminalServer = 3
WTSUserConfigfDeviceClientDefaultPrinter = 9
WTSUserConfigfDeviceClientDrives = 7
WTSUserConfigfDeviceClientPrinters = 8
WTSUserConfigfInheritInitialProgram = 2
WTSUserConfigfTerminalServerRemoteHomeDir = 18
WTSUserConfigInitialProgram = 0
WTSUserConfigModemCallbackPhoneNumber = 13
WTSUserConfigModemCallbackSettings = 12
WTSUserConfigReconnectSettings = 11
WTSUserConfigShadowingSettings = 14
WTSUserConfigTerminalServerHomeDir = 16
WTSUserConfigTerminalServerHomeDirDrive = 17
WTSUserConfigTerminalServerProfilePath = 15
WTSUserConfigTimeoutSettingsConnections = 4
WTSUserConfigTimeoutSettingsDisconnections = 5
WTSUserConfigTimeoutSettingsIdle = 6
WTSUserConfigWorkingDirectory = 1
WTSUserName = 5
WTSVirtualClientData = 0
WTSVirtualFileHandle = 1
WTSWinStationName = 6
WTSWorkingDirectory = 2

WTS_CURRENT_SERVER = 0

WTS_CURRENT_SERVER_HANDLE = 0
WTS_CURRENT_SERVER_NAME = None

WTS_CURRENT_SESSION = -1

WTS_EVENT_ALL = 2147483647
WTS_EVENT_CONNECT = 8
WTS_EVENT_CREATE = 1
WTS_EVENT_DELETE = 2
WTS_EVENT_DISCONNECT = 16
WTS_EVENT_FLUSH = -2147483648
WTS_EVENT_LICENSE = 256
WTS_EVENT_LOGOFF = 64
WTS_EVENT_LOGON = 32
WTS_EVENT_NONE = 0
WTS_EVENT_RENAME = 4
WTS_EVENT_STATECHANGE = 128

WTS_PROTOCOL_TYPE_CONSOLE = 0
WTS_PROTOCOL_TYPE_ICA = 1
WTS_PROTOCOL_TYPE_RDP = 2

WTS_WSD_FASTREBOOT = 16
WTS_WSD_LOGOFF = 1
WTS_WSD_POWEROFF = 8
WTS_WSD_REBOOT = 4
WTS_WSD_SHUTDOWN = 2

# functions

def ProcessIdToSessionId(*args, **kwargs): # real signature unknown
    """ Finds the session under which a process is running """
    pass

def WTSCloseServer(*args, **kwargs): # real signature unknown
    """ Closes a terminal server handle """
    pass

def WTSDisconnectSession(*args, **kwargs): # real signature unknown
    """ Disconnects a session without logging it off """
    pass

def WTSEnumerateProcesses(*args, **kwargs): # real signature unknown
    """ Lists processes on a terminal server """
    pass

def WTSEnumerateServers(*args, **kwargs): # real signature unknown
    """ Lists terminal servers in a domain """
    pass

def WTSEnumerateSessions(*args, **kwargs): # real signature unknown
    """ Lists sessions on a server """
    pass

def WTSGetActiveConsoleSessionId(*args, **kwargs): # real signature unknown
    """ Returns the id of the console session """
    pass

def WTSLogoffSession(*args, **kwargs): # real signature unknown
    """ Logs off a user logged in through Terminal Services """
    pass

def WTSOpenServer(*args, **kwargs): # real signature unknown
    """ Opens a handle to a terminal server """
    pass

def WTSQuerySessionInformation(*args, **kwargs): # real signature unknown
    """ Retrieve information about a session """
    pass

def WTSQueryUserConfig(*args, **kwargs): # real signature unknown
    """ Returns user configuration """
    pass

def WTSQueryUserToken(*args, **kwargs): # real signature unknown
    """ Retrieves the access token for a session """
    pass

def WTSRegisterSessionNotification(*args, **kwargs): # real signature unknown
    """ Registers a window to receive terminal service notifications """
    pass

def WTSSendMessage(*args, **kwargs): # real signature unknown
    """ Sends a popup message to a terminal services session """
    pass

def WTSSetUserConfig(*args, **kwargs): # real signature unknown
    """ Changes user configuration """
    pass

def WTSShutdownSystem(*args, **kwargs): # real signature unknown
    """ Issues a shutdown request to a terminal server """
    pass

def WTSTerminateProcess(*args, **kwargs): # real signature unknown
    """ Kills a process on a terminal server """
    pass

def WTSUnRegisterSessionNotification(*args, **kwargs): # real signature unknown
    """ Disables terminal service window messages """
    pass

def WTSWaitSystemEvent(*args, **kwargs): # real signature unknown
    """ Waits for an event to occur """
    pass

# no classes
