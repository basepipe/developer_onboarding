# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDataStream(__Shiboken.Object):
    # no doc
    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def byteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def device(self, *args, **kwargs): # real signature unknown
        pass

    def floatingPointPrecision(self, *args, **kwargs): # real signature unknown
        pass

    def readBool(self, *args, **kwargs): # real signature unknown
        pass

    def readDouble(self, *args, **kwargs): # real signature unknown
        pass

    def readFloat(self, *args, **kwargs): # real signature unknown
        pass

    def readInt16(self, *args, **kwargs): # real signature unknown
        pass

    def readInt32(self, *args, **kwargs): # real signature unknown
        pass

    def readInt64(self, *args, **kwargs): # real signature unknown
        pass

    def readInt8(self, *args, **kwargs): # real signature unknown
        pass

    def readQChar(self, *args, **kwargs): # real signature unknown
        pass

    def readQString(self, *args, **kwargs): # real signature unknown
        pass

    def readQStringList(self, *args, **kwargs): # real signature unknown
        pass

    def readQVariant(self, *args, **kwargs): # real signature unknown
        pass

    def readRawData(self, *args, **kwargs): # real signature unknown
        pass

    def readString(self, *args, **kwargs): # real signature unknown
        pass

    def readUInt16(self, *args, **kwargs): # real signature unknown
        pass

    def readUInt32(self, *args, **kwargs): # real signature unknown
        pass

    def readUInt64(self, *args, **kwargs): # real signature unknown
        pass

    def readUInt8(self, *args, **kwargs): # real signature unknown
        pass

    def resetStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setByteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, *args, **kwargs): # real signature unknown
        pass

    def setFloatingPointPrecision(self, *args, **kwargs): # real signature unknown
        pass

    def setStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setVersion(self, *args, **kwargs): # real signature unknown
        pass

    def skipRawData(self, *args, **kwargs): # real signature unknown
        pass

    def status(self, *args, **kwargs): # real signature unknown
        pass

    def unsetDevice(self, *args, **kwargs): # real signature unknown
        pass

    def version(self, *args, **kwargs): # real signature unknown
        pass

    def writeBool(self, *args, **kwargs): # real signature unknown
        pass

    def writeDouble(self, *args, **kwargs): # real signature unknown
        pass

    def writeFloat(self, *args, **kwargs): # real signature unknown
        pass

    def writeInt16(self, *args, **kwargs): # real signature unknown
        pass

    def writeInt32(self, *args, **kwargs): # real signature unknown
        pass

    def writeInt64(self, *args, **kwargs): # real signature unknown
        pass

    def writeInt8(self, *args, **kwargs): # real signature unknown
        pass

    def writeQChar(self, *args, **kwargs): # real signature unknown
        pass

    def writeQString(self, *args, **kwargs): # real signature unknown
        pass

    def writeQStringList(self, *args, **kwargs): # real signature unknown
        pass

    def writeQVariant(self, *args, **kwargs): # real signature unknown
        pass

    def writeRawData(self, *args, **kwargs): # real signature unknown
        pass

    def writeString(self, *args, **kwargs): # real signature unknown
        pass

    def writeUInt16(self, *args, **kwargs): # real signature unknown
        pass

    def writeUInt32(self, *args, **kwargs): # real signature unknown
        pass

    def writeUInt64(self, *args, **kwargs): # real signature unknown
        pass

    def writeUInt8(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    BigEndian = PySide.QtCore.QDataStream.ByteOrder.BigEndian
    ByteOrder = None # (!) real value is "<type 'PySide.QtCore.QDataStream.ByteOrder'>"
    DoublePrecision = PySide.QtCore.QDataStream.FloatingPointPrecision.DoublePrecision
    FloatingPointPrecision = None # (!) real value is "<type 'PySide.QtCore.QDataStream.FloatingPointPrecision'>"
    LittleEndian = PySide.QtCore.QDataStream.ByteOrder.LittleEndian
    Ok = PySide.QtCore.QDataStream.Status.Ok
    Qt_1_0 = PySide.QtCore.QDataStream.Version.Qt_1_0
    Qt_2_0 = PySide.QtCore.QDataStream.Version.Qt_2_0
    Qt_2_1 = PySide.QtCore.QDataStream.Version.Qt_2_1
    Qt_3_0 = PySide.QtCore.QDataStream.Version.Qt_3_0
    Qt_3_1 = PySide.QtCore.QDataStream.Version.Qt_3_1
    Qt_3_3 = PySide.QtCore.QDataStream.Version.Qt_3_3
    Qt_4_0 = PySide.QtCore.QDataStream.Version.Qt_4_0
    Qt_4_1 = PySide.QtCore.QDataStream.Version.Qt_4_1
    Qt_4_2 = PySide.QtCore.QDataStream.Version.Qt_4_2
    Qt_4_3 = PySide.QtCore.QDataStream.Version.Qt_4_3
    Qt_4_4 = PySide.QtCore.QDataStream.Version.Qt_4_4
    Qt_4_5 = PySide.QtCore.QDataStream.Version.Qt_4_5
    Qt_4_6 = PySide.QtCore.QDataStream.Version.Qt_4_6
    Qt_4_7 = PySide.QtCore.QDataStream.Version.Qt_4_7
    Qt_4_8 = PySide.QtCore.QDataStream.Version.Qt_4_8
    ReadCorruptData = PySide.QtCore.QDataStream.Status.ReadCorruptData
    ReadPastEnd = PySide.QtCore.QDataStream.Status.ReadPastEnd
    SinglePrecision = PySide.QtCore.QDataStream.FloatingPointPrecision.SinglePrecision
    Status = None # (!) real value is "<type 'PySide.QtCore.QDataStream.Status'>"
    Version = None # (!) real value is "<type 'PySide.QtCore.QDataStream.Version'>"
    WriteFailed = PySide.QtCore.QDataStream.Status.WriteFailed


