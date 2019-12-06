# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from QDialog import QDialog

class QFileDialog(QDialog):
    # no doc
    def accept(self, *args, **kwargs): # real signature unknown
        pass

    def acceptMode(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def confirmOverwrite(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def defaultSuffix(self, *args, **kwargs): # real signature unknown
        pass

    def directory(self, *args, **kwargs): # real signature unknown
        pass

    def directoryEntered(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        pass

    def fileMode(self, *args, **kwargs): # real signature unknown
        pass

    def fileSelected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def filesSelected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def filter(self, *args, **kwargs): # real signature unknown
        pass

    def filters(self, *args, **kwargs): # real signature unknown
        pass

    def filterSelected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def getExistingDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def getOpenFileName(self, *args, **kwargs): # real signature unknown
        pass

    def getOpenFileNames(self, *args, **kwargs): # real signature unknown
        pass

    def getSaveFileName(self, *args, **kwargs): # real signature unknown
        pass

    def history(self, *args, **kwargs): # real signature unknown
        pass

    def iconProvider(self, *args, **kwargs): # real signature unknown
        pass

    def isNameFilterDetailsVisible(self, *args, **kwargs): # real signature unknown
        pass

    def isReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def itemDelegate(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self, *args, **kwargs): # real signature unknown
        pass

    def nameFilters(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def options(self, *args, **kwargs): # real signature unknown
        pass

    def proxyModel(self, *args, **kwargs): # real signature unknown
        pass

    def resolveSymlinks(self, *args, **kwargs): # real signature unknown
        pass

    def restoreState(self, *args, **kwargs): # real signature unknown
        pass

    def saveState(self, *args, **kwargs): # real signature unknown
        pass

    def selectedFiles(self, *args, **kwargs): # real signature unknown
        pass

    def selectedFilter(self, *args, **kwargs): # real signature unknown
        pass

    def selectedNameFilter(self, *args, **kwargs): # real signature unknown
        pass

    def selectFile(self, *args, **kwargs): # real signature unknown
        pass

    def selectFilter(self, *args, **kwargs): # real signature unknown
        pass

    def selectNameFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptMode(self, *args, **kwargs): # real signature unknown
        pass

    def setConfirmOverwrite(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultSuffix(self, *args, **kwargs): # real signature unknown
        pass

    def setDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def setFileMode(self, *args, **kwargs): # real signature unknown
        pass

    def setFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setFilters(self, *args, **kwargs): # real signature unknown
        pass

    def setHistory(self, *args, **kwargs): # real signature unknown
        pass

    def setIconProvider(self, *args, **kwargs): # real signature unknown
        pass

    def setItemDelegate(self, *args, **kwargs): # real signature unknown
        pass

    def setLabelText(self, *args, **kwargs): # real signature unknown
        pass

    def setNameFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setNameFilterDetailsVisible(self, *args, **kwargs): # real signature unknown
        pass

    def setNameFilters(self, *args, **kwargs): # real signature unknown
        pass

    def setOption(self, *args, **kwargs): # real signature unknown
        pass

    def setOptions(self, *args, **kwargs): # real signature unknown
        pass

    def setProxyModel(self, *args, **kwargs): # real signature unknown
        pass

    def setReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setResolveSymlinks(self, *args, **kwargs): # real signature unknown
        pass

    def setSidebarUrls(self, *args, **kwargs): # real signature unknown
        pass

    def setViewMode(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        pass

    def sidebarUrls(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Accept = PySide.QtGui.QFileDialog.DialogLabel.Accept
    AcceptMode = None # (!) real value is "<type 'PySide.QtGui.QFileDialog.AcceptMode'>"
    AcceptOpen = PySide.QtGui.QFileDialog.AcceptMode.AcceptOpen
    AcceptSave = PySide.QtGui.QFileDialog.AcceptMode.AcceptSave
    AnyFile = PySide.QtGui.QFileDialog.FileMode.AnyFile
    Detail = PySide.QtGui.QFileDialog.ViewMode.Detail
    DialogLabel = None # (!) real value is "<type 'PySide.QtGui.QFileDialog.DialogLabel'>"
    Directory = PySide.QtGui.QFileDialog.FileMode.Directory
    DirectoryOnly = PySide.QtGui.QFileDialog.FileMode.DirectoryOnly
    DontConfirmOverwrite = PySide.QtGui.QFileDialog.Option.DontConfirmOverwrite
    DontResolveSymlinks = PySide.QtGui.QFileDialog.Option.DontResolveSymlinks
    DontUseCustomDirectoryIcons = PySide.QtGui.QFileDialog.Option.DontUseCustomDirectoryIcons
    DontUseNativeDialog = PySide.QtGui.QFileDialog.Option.DontUseNativeDialog
    DontUseSheet = PySide.QtGui.QFileDialog.Option.DontUseSheet
    ExistingFile = PySide.QtGui.QFileDialog.FileMode.ExistingFile
    ExistingFiles = PySide.QtGui.QFileDialog.FileMode.ExistingFiles
    FileMode = None # (!) real value is "<type 'PySide.QtGui.QFileDialog.FileMode'>"
    FileName = PySide.QtGui.QFileDialog.DialogLabel.FileName
    FileType = PySide.QtGui.QFileDialog.DialogLabel.FileType
    HideNameFilterDetails = PySide.QtGui.QFileDialog.Option.HideNameFilterDetails
    List = PySide.QtGui.QFileDialog.ViewMode.List
    LookIn = PySide.QtGui.QFileDialog.DialogLabel.LookIn
    Option = None # (!) real value is "<type 'PySide.QtGui.QFileDialog.Option'>"
    Options = None # (!) real value is "<type 'Options'>"
    ReadOnly = PySide.QtGui.QFileDialog.Option.ReadOnly
    Reject = PySide.QtGui.QFileDialog.DialogLabel.Reject
    ShowDirsOnly = PySide.QtGui.QFileDialog.Option.ShowDirsOnly
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004C16BC8>'
    ViewMode = None # (!) real value is "<type 'PySide.QtGui.QFileDialog.ViewMode'>"


