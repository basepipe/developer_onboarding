# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from QIODevice import QIODevice

class QFile(QIODevice):
    # no doc
    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def decodeName(self, *args, **kwargs): # real signature unknown
        pass

    def encodeName(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def exists(self, *args, **kwargs): # real signature unknown
        pass

    def fileEngine(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def permissions(self, *args, **kwargs): # real signature unknown
        pass

    def pos(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def readLink(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def rename(self, *args, **kwargs): # real signature unknown
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, *args, **kwargs): # real signature unknown
        pass

    def setPermissions(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def symLinkTarget(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def unsetError(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AbortError = PySide.QtCore.QFile.FileError.AbortError
    AutoCloseHandle = PySide.QtCore.QFile.FileHandleFlag.AutoCloseHandle
    CopyError = PySide.QtCore.QFile.FileError.CopyError
    DontCloseHandle = PySide.QtCore.QFile.FileHandleFlag.DontCloseHandle
    ExeGroup = PySide.QtCore.QFile.Permission.ExeGroup
    ExeOther = PySide.QtCore.QFile.Permission.ExeOther
    ExeOwner = PySide.QtCore.QFile.Permission.ExeOwner
    ExeUser = PySide.QtCore.QFile.Permission.ExeUser
    FatalError = PySide.QtCore.QFile.FileError.FatalError
    FileError = None # (!) real value is "<type 'PySide.QtCore.QFile.FileError'>"
    FileHandleFlag = None # (!) real value is "<type 'PySide.QtCore.QFile.FileHandleFlag'>"
    FileHandleFlags = None # (!) real value is "<type 'FileHandleFlags'>"
    MemoryMapFlags = None # (!) real value is "<type 'PySide.QtCore.QFile.MemoryMapFlags'>"
    NoError = PySide.QtCore.QFile.FileError.NoError
    NoOptions = PySide.QtCore.QFile.MemoryMapFlags.NoOptions
    OpenError = PySide.QtCore.QFile.FileError.OpenError
    Permission = None # (!) real value is "<type 'PySide.QtCore.QFile.Permission'>"
    Permissions = None # (!) real value is "<type 'Permissions'>"
    PermissionsError = PySide.QtCore.QFile.FileError.PermissionsError
    PositionError = PySide.QtCore.QFile.FileError.PositionError
    ReadError = PySide.QtCore.QFile.FileError.ReadError
    ReadGroup = PySide.QtCore.QFile.Permission.ReadGroup
    ReadOther = PySide.QtCore.QFile.Permission.ReadOther
    ReadOwner = PySide.QtCore.QFile.Permission.ReadOwner
    ReadUser = PySide.QtCore.QFile.Permission.ReadUser
    RemoveError = PySide.QtCore.QFile.FileError.RemoveError
    RenameError = PySide.QtCore.QFile.FileError.RenameError
    ResizeError = PySide.QtCore.QFile.FileError.ResizeError
    ResourceError = PySide.QtCore.QFile.FileError.ResourceError
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003E7E208>'
    TimeOutError = PySide.QtCore.QFile.FileError.TimeOutError
    UnspecifiedError = PySide.QtCore.QFile.FileError.UnspecifiedError
    WriteError = PySide.QtCore.QFile.FileError.WriteError
    WriteGroup = PySide.QtCore.QFile.Permission.WriteGroup
    WriteOther = PySide.QtCore.QFile.Permission.WriteOther
    WriteOwner = PySide.QtCore.QFile.Permission.WriteOwner
    WriteUser = PySide.QtCore.QFile.Permission.WriteUser


