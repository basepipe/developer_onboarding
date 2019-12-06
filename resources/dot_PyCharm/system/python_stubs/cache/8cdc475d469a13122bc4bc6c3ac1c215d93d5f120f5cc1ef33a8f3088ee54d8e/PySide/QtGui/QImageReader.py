# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QImageReader(__Shiboken.Object):
    # no doc
    def autoDetectImageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def backgroundColor(self, *args, **kwargs): # real signature unknown
        pass

    def canRead(self, *args, **kwargs): # real signature unknown
        pass

    def clipRect(self, *args, **kwargs): # real signature unknown
        pass

    def currentImageNumber(self, *args, **kwargs): # real signature unknown
        pass

    def currentImageRect(self, *args, **kwargs): # real signature unknown
        pass

    def decideFormatFromContent(self, *args, **kwargs): # real signature unknown
        pass

    def device(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def imageCount(self, *args, **kwargs): # real signature unknown
        pass

    def imageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def jumpToImage(self, *args, **kwargs): # real signature unknown
        pass

    def jumpToNextImage(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self, *args, **kwargs): # real signature unknown
        pass

    def nextImageDelay(self, *args, **kwargs): # real signature unknown
        pass

    def quality(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def scaledClipRect(self, *args, **kwargs): # real signature unknown
        pass

    def scaledSize(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoDetectImageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundColor(self, *args, **kwargs): # real signature unknown
        pass

    def setClipRect(self, *args, **kwargs): # real signature unknown
        pass

    def setDecideFormatFromContent(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setQuality(self, *args, **kwargs): # real signature unknown
        pass

    def setScaledClipRect(self, *args, **kwargs): # real signature unknown
        pass

    def setScaledSize(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def supportedImageFormats(self, *args, **kwargs): # real signature unknown
        pass

    def supportsAnimation(self, *args, **kwargs): # real signature unknown
        pass

    def supportsOption(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def textKeys(self, *args, **kwargs): # real signature unknown
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

    DeviceError = PySide.QtGui.QImageReader.ImageReaderError.DeviceError
    FileNotFoundError = PySide.QtGui.QImageReader.ImageReaderError.FileNotFoundError
    ImageReaderError = None # (!) real value is "<type 'PySide.QtGui.QImageReader.ImageReaderError'>"
    InvalidDataError = PySide.QtGui.QImageReader.ImageReaderError.InvalidDataError
    UnknownError = PySide.QtGui.QImageReader.ImageReaderError.UnknownError
    UnsupportedFormatError = PySide.QtGui.QImageReader.ImageReaderError.UnsupportedFormatError


