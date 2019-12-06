# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from QIODevice import QIODevice

class QProcess(QIODevice):
    # no doc
    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def closeReadChannel(self, *args, **kwargs): # real signature unknown
        pass

    def closeWriteChannel(self, *args, **kwargs): # real signature unknown
        pass

    def environment(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        pass

    def exitCode(self, *args, **kwargs): # real signature unknown
        pass

    def exitStatus(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def kill(self, *args, **kwargs): # real signature unknown
        pass

    def pid(self, *args, **kwargs): # real signature unknown
        pass

    def processChannelMode(self, *args, **kwargs): # real signature unknown
        pass

    def processEnvironment(self, *args, **kwargs): # real signature unknown
        pass

    def readAllStandardError(self, *args, **kwargs): # real signature unknown
        pass

    def readAllStandardOutput(self, *args, **kwargs): # real signature unknown
        pass

    def readChannel(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readyReadStandardError(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def readyReadStandardOutput(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def setEnvironment(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessChannelMode(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessEnvironment(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessState(self, *args, **kwargs): # real signature unknown
        pass

    def setReadChannel(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardErrorFile(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardInputFile(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardOutputFile(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardOutputProcess(self, *args, **kwargs): # real signature unknown
        pass

    def setupChildProcess(self, *args, **kwargs): # real signature unknown
        pass

    def setWorkingDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def startDetached(self, *args, **kwargs): # real signature unknown
        pass

    def started(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def systemEnvironment(self, *args, **kwargs): # real signature unknown
        pass

    def terminate(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForFinished(self, *args, **kwargs): # real signature unknown
        pass

    def waitForReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def waitForStarted(self, *args, **kwargs): # real signature unknown
        pass

    def workingDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Crashed = PySide.QtCore.QProcess.ProcessError.Crashed
    CrashExit = PySide.QtCore.QProcess.ExitStatus.CrashExit
    ExitStatus = None # (!) real value is "<type 'PySide.QtCore.QProcess.ExitStatus'>"
    FailedToStart = PySide.QtCore.QProcess.ProcessError.FailedToStart
    ForwardedChannels = PySide.QtCore.QProcess.ProcessChannelMode.ForwardedChannels
    MergedChannels = PySide.QtCore.QProcess.ProcessChannelMode.MergedChannels
    NormalExit = PySide.QtCore.QProcess.ExitStatus.NormalExit
    NotRunning = PySide.QtCore.QProcess.ProcessState.NotRunning
    ProcessChannel = None # (!) real value is "<type 'PySide.QtCore.QProcess.ProcessChannel'>"
    ProcessChannelMode = None # (!) real value is "<type 'PySide.QtCore.QProcess.ProcessChannelMode'>"
    ProcessError = None # (!) real value is "<type 'PySide.QtCore.QProcess.ProcessError'>"
    ProcessState = None # (!) real value is "<type 'PySide.QtCore.QProcess.ProcessState'>"
    ReadError = PySide.QtCore.QProcess.ProcessError.ReadError
    Running = PySide.QtCore.QProcess.ProcessState.Running
    SeparateChannels = PySide.QtCore.QProcess.ProcessChannelMode.SeparateChannels
    StandardError = PySide.QtCore.QProcess.ProcessChannel.StandardError
    StandardOutput = PySide.QtCore.QProcess.ProcessChannel.StandardOutput
    Starting = PySide.QtCore.QProcess.ProcessState.Starting
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003E75088>'
    Timedout = PySide.QtCore.QProcess.ProcessError.Timedout
    UnknownError = PySide.QtCore.QProcess.ProcessError.UnknownError
    WriteError = PySide.QtCore.QProcess.ProcessError.WriteError


