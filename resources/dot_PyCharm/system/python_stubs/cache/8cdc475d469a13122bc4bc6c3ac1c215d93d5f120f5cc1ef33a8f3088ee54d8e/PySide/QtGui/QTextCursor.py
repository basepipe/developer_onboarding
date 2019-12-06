# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QTextCursor(__Shiboken.Object):
    # no doc
    def anchor(self, *args, **kwargs): # real signature unknown
        pass

    def atBlockEnd(self, *args, **kwargs): # real signature unknown
        pass

    def atBlockStart(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def atStart(self, *args, **kwargs): # real signature unknown
        pass

    def beginEditBlock(self, *args, **kwargs): # real signature unknown
        pass

    def block(self, *args, **kwargs): # real signature unknown
        pass

    def blockCharFormat(self, *args, **kwargs): # real signature unknown
        pass

    def blockFormat(self, *args, **kwargs): # real signature unknown
        pass

    def blockNumber(self, *args, **kwargs): # real signature unknown
        pass

    def charFormat(self, *args, **kwargs): # real signature unknown
        pass

    def clearSelection(self, *args, **kwargs): # real signature unknown
        pass

    def columnNumber(self, *args, **kwargs): # real signature unknown
        pass

    def createList(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrame(self, *args, **kwargs): # real signature unknown
        pass

    def currentList(self, *args, **kwargs): # real signature unknown
        pass

    def currentTable(self, *args, **kwargs): # real signature unknown
        pass

    def deleteChar(self, *args, **kwargs): # real signature unknown
        pass

    def deletePreviousChar(self, *args, **kwargs): # real signature unknown
        pass

    def document(self, *args, **kwargs): # real signature unknown
        pass

    def endEditBlock(self, *args, **kwargs): # real signature unknown
        pass

    def hasComplexSelection(self, *args, **kwargs): # real signature unknown
        pass

    def hasSelection(self, *args, **kwargs): # real signature unknown
        pass

    def insertBlock(self, *args, **kwargs): # real signature unknown
        pass

    def insertFragment(self, *args, **kwargs): # real signature unknown
        pass

    def insertFrame(self, *args, **kwargs): # real signature unknown
        pass

    def insertHtml(self, *args, **kwargs): # real signature unknown
        pass

    def insertImage(self, *args, **kwargs): # real signature unknown
        pass

    def insertList(self, *args, **kwargs): # real signature unknown
        pass

    def insertTable(self, *args, **kwargs): # real signature unknown
        pass

    def insertText(self, *args, **kwargs): # real signature unknown
        pass

    def isCopyOf(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def joinPreviousEditBlock(self, *args, **kwargs): # real signature unknown
        pass

    def keepPositionOnInsert(self, *args, **kwargs): # real signature unknown
        pass

    def mergeBlockCharFormat(self, *args, **kwargs): # real signature unknown
        pass

    def mergeBlockFormat(self, *args, **kwargs): # real signature unknown
        pass

    def mergeCharFormat(self, *args, **kwargs): # real signature unknown
        pass

    def movePosition(self, *args, **kwargs): # real signature unknown
        pass

    def position(self, *args, **kwargs): # real signature unknown
        pass

    def positionInBlock(self, *args, **kwargs): # real signature unknown
        pass

    def removeSelectedText(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectedTableCells(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self, *args, **kwargs): # real signature unknown
        pass

    def selection(self, *args, **kwargs): # real signature unknown
        pass

    def selectionEnd(self, *args, **kwargs): # real signature unknown
        pass

    def selectionStart(self, *args, **kwargs): # real signature unknown
        pass

    def setBlockCharFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setBlockFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setCharFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setKeepPositionOnInsert(self, *args, **kwargs): # real signature unknown
        pass

    def setPosition(self, *args, **kwargs): # real signature unknown
        pass

    def setVerticalMovementX(self, *args, **kwargs): # real signature unknown
        pass

    def setVisualNavigation(self, *args, **kwargs): # real signature unknown
        pass

    def verticalMovementX(self, *args, **kwargs): # real signature unknown
        pass

    def visualNavigation(self, *args, **kwargs): # real signature unknown
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

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    BlockUnderCursor = PySide.QtGui.QTextCursor.SelectionType.BlockUnderCursor
    Document = PySide.QtGui.QTextCursor.SelectionType.Document
    Down = PySide.QtGui.QTextCursor.MoveOperation.Down
    End = PySide.QtGui.QTextCursor.MoveOperation.End
    EndOfBlock = PySide.QtGui.QTextCursor.MoveOperation.EndOfBlock
    EndOfLine = PySide.QtGui.QTextCursor.MoveOperation.EndOfLine
    EndOfWord = PySide.QtGui.QTextCursor.MoveOperation.EndOfWord
    KeepAnchor = PySide.QtGui.QTextCursor.MoveMode.KeepAnchor
    Left = PySide.QtGui.QTextCursor.MoveOperation.Left
    LineUnderCursor = PySide.QtGui.QTextCursor.SelectionType.LineUnderCursor
    MoveAnchor = PySide.QtGui.QTextCursor.MoveMode.MoveAnchor
    MoveMode = None # (!) real value is "<type 'PySide.QtGui.QTextCursor.MoveMode'>"
    MoveOperation = None # (!) real value is "<type 'PySide.QtGui.QTextCursor.MoveOperation'>"
    NextBlock = PySide.QtGui.QTextCursor.MoveOperation.NextBlock
    NextCell = PySide.QtGui.QTextCursor.MoveOperation.NextCell
    NextCharacter = PySide.QtGui.QTextCursor.MoveOperation.NextCharacter
    NextRow = PySide.QtGui.QTextCursor.MoveOperation.NextRow
    NextWord = PySide.QtGui.QTextCursor.MoveOperation.NextWord
    NoMove = PySide.QtGui.QTextCursor.MoveOperation.NoMove
    PreviousBlock = PySide.QtGui.QTextCursor.MoveOperation.PreviousBlock
    PreviousCell = PySide.QtGui.QTextCursor.MoveOperation.PreviousCell
    PreviousCharacter = PySide.QtGui.QTextCursor.MoveOperation.PreviousCharacter
    PreviousRow = PySide.QtGui.QTextCursor.MoveOperation.PreviousRow
    PreviousWord = PySide.QtGui.QTextCursor.MoveOperation.PreviousWord
    Right = PySide.QtGui.QTextCursor.MoveOperation.Right
    SelectionType = None # (!) real value is "<type 'PySide.QtGui.QTextCursor.SelectionType'>"
    Start = PySide.QtGui.QTextCursor.MoveOperation.Start
    StartOfBlock = PySide.QtGui.QTextCursor.MoveOperation.StartOfBlock
    StartOfLine = PySide.QtGui.QTextCursor.MoveOperation.StartOfLine
    StartOfWord = PySide.QtGui.QTextCursor.MoveOperation.StartOfWord
    Up = PySide.QtGui.QTextCursor.MoveOperation.Up
    WordLeft = PySide.QtGui.QTextCursor.MoveOperation.WordLeft
    WordRight = PySide.QtGui.QTextCursor.MoveOperation.WordRight
    WordUnderCursor = PySide.QtGui.QTextCursor.SelectionType.WordUnderCursor


