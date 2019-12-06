# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from QAbstractItemView import QAbstractItemView

class QListView(QAbstractItemView):
    # no doc
    def batchSize(self, *args, **kwargs): # real signature unknown
        pass

    def clearPropertyFlags(self, *args, **kwargs): # real signature unknown
        pass

    def contentsSize(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def doItemsLayout(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def flow(self, *args, **kwargs): # real signature unknown
        pass

    def gridSize(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def indexAt(self, *args, **kwargs): # real signature unknown
        pass

    def indexesMoved(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def internalDrag(self, *args, **kwargs): # real signature unknown
        pass

    def internalDrop(self, *args, **kwargs): # real signature unknown
        pass

    def isIndexHidden(self, *args, **kwargs): # real signature unknown
        pass

    def isRowHidden(self, *args, **kwargs): # real signature unknown
        pass

    def isSelectionRectVisible(self, *args, **kwargs): # real signature unknown
        pass

    def isWrapping(self, *args, **kwargs): # real signature unknown
        pass

    def layoutMode(self, *args, **kwargs): # real signature unknown
        pass

    def modelColumn(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveCursor(self, *args, **kwargs): # real signature unknown
        pass

    def movement(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def rectForIndex(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resizeContents(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def rowsAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def rowsInserted(self, *args, **kwargs): # real signature unknown
        pass

    def scrollContentsBy(self, *args, **kwargs): # real signature unknown
        pass

    def scrollTo(self, *args, **kwargs): # real signature unknown
        pass

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setBatchSize(self, *args, **kwargs): # real signature unknown
        pass

    def setFlow(self, *args, **kwargs): # real signature unknown
        pass

    def setGridSize(self, *args, **kwargs): # real signature unknown
        pass

    def setLayoutMode(self, *args, **kwargs): # real signature unknown
        pass

    def setModelColumn(self, *args, **kwargs): # real signature unknown
        pass

    def setMovement(self, *args, **kwargs): # real signature unknown
        pass

    def setPositionForIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setResizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def setRootIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setRowHidden(self, *args, **kwargs): # real signature unknown
        pass

    def setSelection(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectionRectVisible(self, *args, **kwargs): # real signature unknown
        pass

    def setSpacing(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformItemSizes(self, *args, **kwargs): # real signature unknown
        pass

    def setViewMode(self, *args, **kwargs): # real signature unknown
        pass

    def setWordWrap(self, *args, **kwargs): # real signature unknown
        pass

    def setWrapping(self, *args, **kwargs): # real signature unknown
        pass

    def spacing(self, *args, **kwargs): # real signature unknown
        pass

    def startDrag(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uniformItemSizes(self, *args, **kwargs): # real signature unknown
        pass

    def updateGeometries(self, *args, **kwargs): # real signature unknown
        pass

    def verticalOffset(self, *args, **kwargs): # real signature unknown
        pass

    def viewMode(self, *args, **kwargs): # real signature unknown
        pass

    def viewOptions(self, *args, **kwargs): # real signature unknown
        pass

    def visualRect(self, *args, **kwargs): # real signature unknown
        pass

    def visualRegionForSelection(self, *args, **kwargs): # real signature unknown
        pass

    def wordWrap(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Adjust = PySide.QtGui.QListView.ResizeMode.Adjust
    Batched = PySide.QtGui.QListView.LayoutMode.Batched
    Fixed = PySide.QtGui.QListView.ResizeMode.Fixed
    Flow = None # (!) real value is "<type 'PySide.QtGui.QListView.Flow'>"
    Free = PySide.QtGui.QListView.Movement.Free
    IconMode = PySide.QtGui.QListView.ViewMode.IconMode
    LayoutMode = None # (!) real value is "<type 'PySide.QtGui.QListView.LayoutMode'>"
    LeftToRight = PySide.QtGui.QListView.Flow.LeftToRight
    ListMode = PySide.QtGui.QListView.ViewMode.ListMode
    Movement = None # (!) real value is "<type 'PySide.QtGui.QListView.Movement'>"
    ResizeMode = None # (!) real value is "<type 'PySide.QtGui.QListView.ResizeMode'>"
    SinglePass = PySide.QtGui.QListView.LayoutMode.SinglePass
    Snap = PySide.QtGui.QListView.Movement.Snap
    Static = PySide.QtGui.QListView.Movement.Static
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004066548>'
    TopToBottom = PySide.QtGui.QListView.Flow.TopToBottom
    ViewMode = None # (!) real value is "<type 'PySide.QtGui.QListView.ViewMode'>"


