# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from QObject import QObject

class QIODevice(QObject):
    # no doc
    def aboutToClose(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def bytesWritten(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def getChar(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def isReadable(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def isTextModeEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def openMode(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, *args, **kwargs): # real signature unknown
        pass

    def pos(self, *args, **kwargs): # real signature unknown
        pass

    def putChar(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readAll(self, *args, **kwargs): # real signature unknown
        pass

    def readChannelFinished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLine(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setTextModeEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def ungetChar(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Append = PySide.QtCore.QIODevice.OpenModeFlag.Append
    NotOpen = PySide.QtCore.QIODevice.OpenModeFlag.NotOpen
    OpenMode = None # (!) real value is "<type 'OpenMode'>"
    OpenModeFlag = None # (!) real value is "<type 'PySide.QtCore.QIODevice.OpenModeFlag'>"
    ReadOnly = PySide.QtCore.QIODevice.OpenModeFlag.ReadOnly
    ReadWrite = PySide.QtCore.QIODevice.OpenModeFlag.ReadWrite
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003E6D888>'
    Text = PySide.QtCore.QIODevice.OpenModeFlag.Text
    Truncate = PySide.QtCore.QIODevice.OpenModeFlag.Truncate
    Unbuffered = PySide.QtCore.QIODevice.OpenModeFlag.Unbuffered
    WriteOnly = PySide.QtCore.QIODevice.OpenModeFlag.WriteOnly


