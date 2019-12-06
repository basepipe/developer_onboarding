# encoding: utf-8
# module PySide.QtNetwork
# from C:\Python27\lib\site-packages\PySide\QtNetwork.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QFtp(__PySide_QtCore.QObject):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def cd(self, *args, **kwargs): # real signature unknown
        pass

    def clearPendingCommands(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commandFinished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def commandStarted(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def connectToHost(self, *args, **kwargs): # real signature unknown
        pass

    def currentCommand(self, *args, **kwargs): # real signature unknown
        pass

    def currentDevice(self, *args, **kwargs): # real signature unknown
        pass

    def currentId(self, *args, **kwargs): # real signature unknown
        pass

    def dataTransferProgress(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingCommands(self, *args, **kwargs): # real signature unknown
        pass

    def list(self, *args, **kwargs): # real signature unknown
        pass

    def listInfo(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def login(self, *args, **kwargs): # real signature unknown
        pass

    def mkdir(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def rawCommand(self, *args, **kwargs): # real signature unknown
        pass

    def rawCommandReply(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readAll(self, *args, **kwargs): # real signature unknown
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def rename(self, *args, **kwargs): # real signature unknown
        pass

    def rmdir(self, *args, **kwargs): # real signature unknown
        pass

    def setProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setTransferMode(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Active = PySide.QtNetwork.QFtp.TransferMode.Active
    Ascii = PySide.QtNetwork.QFtp.TransferType.Ascii
    Binary = PySide.QtNetwork.QFtp.TransferType.Binary
    Cd = PySide.QtNetwork.QFtp.Command.Cd
    Close = PySide.QtNetwork.QFtp.Command.Close
    Closing = PySide.QtNetwork.QFtp.State.Closing
    Command = None # (!) real value is "<type 'PySide.QtNetwork.QFtp.Command'>"
    Connected = PySide.QtNetwork.QFtp.State.Connected
    Connecting = PySide.QtNetwork.QFtp.State.Connecting
    ConnectionRefused = PySide.QtNetwork.QFtp.Error.ConnectionRefused
    ConnectToHost = PySide.QtNetwork.QFtp.Command.ConnectToHost
    Error = None # (!) real value is "<type 'PySide.QtNetwork.QFtp.Error'>"
    Get = PySide.QtNetwork.QFtp.Command.Get
    HostLookup = PySide.QtNetwork.QFtp.State.HostLookup
    HostNotFound = PySide.QtNetwork.QFtp.Error.HostNotFound
    List = PySide.QtNetwork.QFtp.Command.List
    LoggedIn = PySide.QtNetwork.QFtp.State.LoggedIn
    Login = PySide.QtNetwork.QFtp.Command.Login
    Mkdir = PySide.QtNetwork.QFtp.Command.Mkdir
    NoError = PySide.QtNetwork.QFtp.Error.NoError
    None = PySide.QtNetwork.QFtp.Command.None
    NotConnected = PySide.QtNetwork.QFtp.Error.NotConnected
    Passive = PySide.QtNetwork.QFtp.TransferMode.Passive
    Put = PySide.QtNetwork.QFtp.Command.Put
    RawCommand = PySide.QtNetwork.QFtp.Command.RawCommand
    Remove = PySide.QtNetwork.QFtp.Command.Remove
    Rename = PySide.QtNetwork.QFtp.Command.Rename
    Rmdir = PySide.QtNetwork.QFtp.Command.Rmdir
    SetProxy = PySide.QtNetwork.QFtp.Command.SetProxy
    SetTransferMode = PySide.QtNetwork.QFtp.Command.SetTransferMode
    State = None # (!) real value is "<type 'PySide.QtNetwork.QFtp.State'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000038A6E48>'
    TransferMode = None # (!) real value is "<type 'PySide.QtNetwork.QFtp.TransferMode'>"
    TransferType = None # (!) real value is "<type 'PySide.QtNetwork.QFtp.TransferType'>"
    Unconnected = PySide.QtNetwork.QFtp.State.Unconnected
    UnknownError = PySide.QtNetwork.QFtp.Error.UnknownError


