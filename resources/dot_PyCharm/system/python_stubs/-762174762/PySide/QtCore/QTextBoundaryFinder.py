# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QTextBoundaryFinder(__Shiboken.Object):
    # no doc
    def boundaryReasons(self, *args, **kwargs): # real signature unknown
        pass

    def isAtBoundary(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def position(self, *args, **kwargs): # real signature unknown
        pass

    def setPosition(self, *args, **kwargs): # real signature unknown
        pass

    def string(self, *args, **kwargs): # real signature unknown
        pass

    def toEnd(self, *args, **kwargs): # real signature unknown
        pass

    def toNextBoundary(self, *args, **kwargs): # real signature unknown
        pass

    def toPreviousBoundary(self, *args, **kwargs): # real signature unknown
        pass

    def toStart(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BoundaryReason = None # (!) real value is "<type 'PySide.QtCore.QTextBoundaryFinder.BoundaryReason'>"
    BoundaryReasons = None # (!) real value is "<type 'BoundaryReasons'>"
    BoundaryType = None # (!) real value is "<type 'PySide.QtCore.QTextBoundaryFinder.BoundaryType'>"
    EndWord = PySide.QtCore.QTextBoundaryFinder.BoundaryReason.EndWord
    Grapheme = PySide.QtCore.QTextBoundaryFinder.BoundaryType.Grapheme
    Line = PySide.QtCore.QTextBoundaryFinder.BoundaryType.Line
    NotAtBoundary = PySide.QtCore.QTextBoundaryFinder.BoundaryReason.NotAtBoundary
    Sentence = PySide.QtCore.QTextBoundaryFinder.BoundaryType.Sentence
    StartWord = PySide.QtCore.QTextBoundaryFinder.BoundaryReason.StartWord
    Word = PySide.QtCore.QTextBoundaryFinder.BoundaryType.Word


