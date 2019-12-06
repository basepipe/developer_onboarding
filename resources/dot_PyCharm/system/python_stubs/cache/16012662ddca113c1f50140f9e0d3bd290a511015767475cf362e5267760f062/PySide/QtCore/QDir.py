# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDir(__Shiboken.Object):
    # no doc
    def absoluteFilePath(self, *args, **kwargs): # real signature unknown
        pass

    def absolutePath(self, *args, **kwargs): # real signature unknown
        pass

    def addResourceSearchPath(self, *args, **kwargs): # real signature unknown
        pass

    def addSearchPath(self, *args, **kwargs): # real signature unknown
        pass

    def canonicalPath(self, *args, **kwargs): # real signature unknown
        pass

    def cd(self, *args, **kwargs): # real signature unknown
        pass

    def cdUp(self, *args, **kwargs): # real signature unknown
        pass

    def cleanPath(self, *args, **kwargs): # real signature unknown
        pass

    def convertSeparators(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def current(self, *args, **kwargs): # real signature unknown
        pass

    def currentPath(self, *args, **kwargs): # real signature unknown
        pass

    def dirName(self, *args, **kwargs): # real signature unknown
        pass

    def drives(self, *args, **kwargs): # real signature unknown
        pass

    def entryInfoList(self, *args, **kwargs): # real signature unknown
        pass

    def entryList(self, *args, **kwargs): # real signature unknown
        pass

    def exists(self, *args, **kwargs): # real signature unknown
        pass

    def filePath(self, *args, **kwargs): # real signature unknown
        pass

    def filter(self, *args, **kwargs): # real signature unknown
        pass

    def fromNativeSeparators(self, *args, **kwargs): # real signature unknown
        pass

    def home(self, *args, **kwargs): # real signature unknown
        pass

    def homePath(self, *args, **kwargs): # real signature unknown
        pass

    def isAbsolute(self, *args, **kwargs): # real signature unknown
        pass

    def isAbsolutePath(self, *args, **kwargs): # real signature unknown
        pass

    def isReadable(self, *args, **kwargs): # real signature unknown
        pass

    def isRelative(self, *args, **kwargs): # real signature unknown
        pass

    def isRelativePath(self, *args, **kwargs): # real signature unknown
        pass

    def isRoot(self, *args, **kwargs): # real signature unknown
        pass

    def makeAbsolute(self, *args, **kwargs): # real signature unknown
        pass

    def match(self, *args, **kwargs): # real signature unknown
        pass

    def mkdir(self, *args, **kwargs): # real signature unknown
        pass

    def mkpath(self, *args, **kwargs): # real signature unknown
        pass

    def nameFilters(self, *args, **kwargs): # real signature unknown
        pass

    def nameFiltersFromString(self, *args, **kwargs): # real signature unknown
        pass

    def path(self, *args, **kwargs): # real signature unknown
        pass

    def refresh(self, *args, **kwargs): # real signature unknown
        pass

    def relativeFilePath(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def rename(self, *args, **kwargs): # real signature unknown
        pass

    def rmdir(self, *args, **kwargs): # real signature unknown
        pass

    def rmpath(self, *args, **kwargs): # real signature unknown
        pass

    def root(self, *args, **kwargs): # real signature unknown
        pass

    def rootPath(self, *args, **kwargs): # real signature unknown
        pass

    def searchPaths(self, *args, **kwargs): # real signature unknown
        pass

    def separator(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def setFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setNameFilters(self, *args, **kwargs): # real signature unknown
        pass

    def setPath(self, *args, **kwargs): # real signature unknown
        pass

    def setSearchPaths(self, *args, **kwargs): # real signature unknown
        pass

    def setSorting(self, *args, **kwargs): # real signature unknown
        pass

    def sorting(self, *args, **kwargs): # real signature unknown
        pass

    def temp(self, *args, **kwargs): # real signature unknown
        pass

    def tempPath(self, *args, **kwargs): # real signature unknown
        pass

    def toNativeSeparators(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    AccessMask = PySide.QtCore.QDir.Filter.AccessMask
    AllDirs = PySide.QtCore.QDir.Filter.AllDirs
    AllEntries = PySide.QtCore.QDir.Filter.AllEntries
    CaseSensitive = PySide.QtCore.QDir.Filter.CaseSensitive
    Dirs = PySide.QtCore.QDir.Filter.Dirs
    DirsFirst = PySide.QtCore.QDir.SortFlag.DirsFirst
    DirsLast = PySide.QtCore.QDir.SortFlag.DirsLast
    Drives = PySide.QtCore.QDir.Filter.Drives
    Executable = PySide.QtCore.QDir.Filter.Executable
    Files = PySide.QtCore.QDir.Filter.Files
    Filter = None # (!) real value is "<type 'PySide.QtCore.QDir.Filter'>"
    Filters = None # (!) real value is "<type 'Filters'>"
    Hidden = PySide.QtCore.QDir.Filter.Hidden
    IgnoreCase = PySide.QtCore.QDir.SortFlag.IgnoreCase
    LocaleAware = PySide.QtCore.QDir.SortFlag.LocaleAware
    Modified = PySide.QtCore.QDir.Filter.Modified
    Name = PySide.QtCore.QDir.SortFlag.Name
    NoDot = PySide.QtCore.QDir.Filter.NoDot
    NoDotAndDotDot = PySide.QtCore.QDir.Filter.NoDotAndDotDot
    NoDotDot = PySide.QtCore.QDir.Filter.NoDotDot
    NoFilter = PySide.QtCore.QDir.Filter.NoFilter
    NoSort = PySide.QtCore.QDir.SortFlag.NoSort
    NoSymLinks = PySide.QtCore.QDir.Filter.NoSymLinks
    PermissionMask = PySide.QtCore.QDir.Filter.PermissionMask
    Readable = PySide.QtCore.QDir.Filter.Readable
    Reversed = PySide.QtCore.QDir.SortFlag.Reversed
    Size = PySide.QtCore.QDir.SortFlag.Size
    SortByMask = PySide.QtCore.QDir.SortFlag.SortByMask
    SortFlag = None # (!) real value is "<type 'PySide.QtCore.QDir.SortFlag'>"
    SortFlags = None # (!) real value is "<type 'SortFlags'>"
    System = PySide.QtCore.QDir.Filter.System
    Time = PySide.QtCore.QDir.SortFlag.Time
    Type = PySide.QtCore.QDir.SortFlag.Type
    TypeMask = PySide.QtCore.QDir.Filter.TypeMask
    Unsorted = PySide.QtCore.QDir.SortFlag.Unsorted
    Writable = PySide.QtCore.QDir.Filter.Writable


