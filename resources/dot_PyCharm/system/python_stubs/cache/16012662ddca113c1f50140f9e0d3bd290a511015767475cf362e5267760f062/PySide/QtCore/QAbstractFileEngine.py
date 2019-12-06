# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QAbstractFileEngine(__Shiboken.Object):
    # no doc
    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def beginEntryList(self, *args, **kwargs): # real signature unknown
        pass

    def caseSensitive(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def entryList(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def fileFlags(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def fileTime(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def isRelativePath(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def mkdir(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def owner(self, *args, **kwargs): # real signature unknown
        pass

    def ownerId(self, *args, **kwargs): # real signature unknown
        pass

    def pos(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readLine(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def rename(self, *args, **kwargs): # real signature unknown
        pass

    def rmdir(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, *args, **kwargs): # real signature unknown
        pass

    def setPermissions(self, *args, **kwargs): # real signature unknown
        pass

    def setSize(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def supportsExtension(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AbsoluteName = PySide.QtCore.QAbstractFileEngine.FileName.AbsoluteName
    AbsolutePathName = PySide.QtCore.QAbstractFileEngine.FileName.AbsolutePathName
    AccessTime = PySide.QtCore.QAbstractFileEngine.FileTime.AccessTime
    AtEndExtension = PySide.QtCore.QAbstractFileEngine.Extension.AtEndExtension
    BaseName = PySide.QtCore.QAbstractFileEngine.FileName.BaseName
    BundleName = PySide.QtCore.QAbstractFileEngine.FileName.BundleName
    BundleType = PySide.QtCore.QAbstractFileEngine.FileFlag.BundleType
    CanonicalName = PySide.QtCore.QAbstractFileEngine.FileName.CanonicalName
    CanonicalPathName = PySide.QtCore.QAbstractFileEngine.FileName.CanonicalPathName
    CreationTime = PySide.QtCore.QAbstractFileEngine.FileTime.CreationTime
    DefaultName = PySide.QtCore.QAbstractFileEngine.FileName.DefaultName
    DirectoryType = PySide.QtCore.QAbstractFileEngine.FileFlag.DirectoryType
    ExeGroupPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ExeGroupPerm
    ExeOtherPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ExeOtherPerm
    ExeOwnerPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ExeOwnerPerm
    ExeUserPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ExeUserPerm
    ExistsFlag = PySide.QtCore.QAbstractFileEngine.FileFlag.ExistsFlag
    Extension = None # (!) real value is "<type 'PySide.QtCore.QAbstractFileEngine.Extension'>"
    FastReadLineExtension = PySide.QtCore.QAbstractFileEngine.Extension.FastReadLineExtension
    FileFlag = None # (!) real value is "<type 'PySide.QtCore.QAbstractFileEngine.FileFlag'>"
    FileFlags = None # (!) real value is "<type 'FileFlags'>"
    FileInfoAll = PySide.QtCore.QAbstractFileEngine.FileFlag.FileInfoAll
    FileName = None # (!) real value is "<type 'PySide.QtCore.QAbstractFileEngine.FileName'>"
    FileOwner = None # (!) real value is "<type 'PySide.QtCore.QAbstractFileEngine.FileOwner'>"
    FileTime = None # (!) real value is "<type 'PySide.QtCore.QAbstractFileEngine.FileTime'>"
    FileType = PySide.QtCore.QAbstractFileEngine.FileFlag.FileType
    FlagsMask = PySide.QtCore.QAbstractFileEngine.FileFlag.FlagsMask
    HiddenFlag = PySide.QtCore.QAbstractFileEngine.FileFlag.HiddenFlag
    LinkName = PySide.QtCore.QAbstractFileEngine.FileName.LinkName
    LinkType = PySide.QtCore.QAbstractFileEngine.FileFlag.LinkType
    LocalDiskFlag = PySide.QtCore.QAbstractFileEngine.FileFlag.LocalDiskFlag
    MapExtension = PySide.QtCore.QAbstractFileEngine.Extension.MapExtension
    ModificationTime = PySide.QtCore.QAbstractFileEngine.FileTime.ModificationTime
    NFileNames = PySide.QtCore.QAbstractFileEngine.FileName.NFileNames
    OwnerGroup = PySide.QtCore.QAbstractFileEngine.FileOwner.OwnerGroup
    OwnerUser = PySide.QtCore.QAbstractFileEngine.FileOwner.OwnerUser
    PathName = PySide.QtCore.QAbstractFileEngine.FileName.PathName
    PermsMask = PySide.QtCore.QAbstractFileEngine.FileFlag.PermsMask
    ReadGroupPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ReadGroupPerm
    ReadOtherPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ReadOtherPerm
    ReadOwnerPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ReadOwnerPerm
    ReadUserPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.ReadUserPerm
    Refresh = PySide.QtCore.QAbstractFileEngine.FileFlag.Refresh
    RootFlag = PySide.QtCore.QAbstractFileEngine.FileFlag.RootFlag
    TypesMask = PySide.QtCore.QAbstractFileEngine.FileFlag.TypesMask
    UnMapExtension = PySide.QtCore.QAbstractFileEngine.Extension.UnMapExtension
    WriteGroupPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.WriteGroupPerm
    WriteOtherPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.WriteOtherPerm
    WriteOwnerPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.WriteOwnerPerm
    WriteUserPerm = PySide.QtCore.QAbstractFileEngine.FileFlag.WriteUserPerm


