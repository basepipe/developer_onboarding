# encoding: utf-8
# module PySide.QtMultimedia
# from C:\Python27\lib\site-packages\PySide\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QAbstractAudioDeviceInfo(__PySide_QtCore.QObject):
    # no doc
    def byteOrderList(self, *args, **kwargs): # real signature unknown
        pass

    def channelsList(self, *args, **kwargs): # real signature unknown
        pass

    def codecList(self, *args, **kwargs): # real signature unknown
        pass

    def deviceName(self, *args, **kwargs): # real signature unknown
        pass

    def frequencyList(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def preferredFormat(self, *args, **kwargs): # real signature unknown
        pass

    def sampleSizeList(self, *args, **kwargs): # real signature unknown
        pass

    def sampleTypeList(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004ED70C8>'


class QAbstractAudioInput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesReady(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004ED4D08>'


class QAbstractAudioOutput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesFree(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004ED3388>'


class QAbstractVideoBuffer(__Shiboken.Object):
    # no doc
    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def mapMode(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    CoreImageHandle = PySide.QtMultimedia.QAbstractVideoBuffer.HandleType.CoreImageHandle
    GLTextureHandle = PySide.QtMultimedia.QAbstractVideoBuffer.HandleType.GLTextureHandle
    HandleType = None # (!) real value is "<type 'PySide.QtMultimedia.QAbstractVideoBuffer.HandleType'>"
    MapMode = None # (!) real value is "<type 'PySide.QtMultimedia.QAbstractVideoBuffer.MapMode'>"
    NoHandle = PySide.QtMultimedia.QAbstractVideoBuffer.HandleType.NoHandle
    NotMapped = PySide.QtMultimedia.QAbstractVideoBuffer.MapMode.NotMapped
    QPixmapHandle = PySide.QtMultimedia.QAbstractVideoBuffer.HandleType.QPixmapHandle
    ReadOnly = PySide.QtMultimedia.QAbstractVideoBuffer.MapMode.ReadOnly
    ReadWrite = PySide.QtMultimedia.QAbstractVideoBuffer.MapMode.ReadWrite
    UserHandle = PySide.QtMultimedia.QAbstractVideoBuffer.HandleType.UserHandle
    WriteOnly = PySide.QtMultimedia.QAbstractVideoBuffer.MapMode.WriteOnly
    XvShmImageHandle = PySide.QtMultimedia.QAbstractVideoBuffer.HandleType.XvShmImageHandle


class QAbstractVideoSurface(__PySide_QtCore.QObject):
    # no doc
    def activeChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def present(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def supportedFormatsChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def supportedPixelFormats(self, *args, **kwargs): # real signature unknown
        pass

    def surfaceFormat(self, *args, **kwargs): # real signature unknown
        pass

    def surfaceFormatChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Error = None # (!) real value is "<type 'PySide.QtMultimedia.QAbstractVideoSurface.Error'>"
    IncorrectFormatError = PySide.QtMultimedia.QAbstractVideoSurface.Error.IncorrectFormatError
    NoError = PySide.QtMultimedia.QAbstractVideoSurface.Error.NoError
    ResourceError = PySide.QtMultimedia.QAbstractVideoSurface.Error.ResourceError
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004ED4788>'
    StoppedError = PySide.QtMultimedia.QAbstractVideoSurface.Error.StoppedError
    UnsupportedFormatError = PySide.QtMultimedia.QAbstractVideoSurface.Error.UnsupportedFormatError


class QAudio(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ActiveState = PySide.QtMultimedia.QAudio.State.ActiveState
    AudioInput = PySide.QtMultimedia.QAudio.Mode.AudioInput
    AudioOutput = PySide.QtMultimedia.QAudio.Mode.AudioOutput
    Error = None # (!) real value is "<type 'PySide.QtMultimedia.QAudio.Error'>"
    FatalError = PySide.QtMultimedia.QAudio.Error.FatalError
    IdleState = PySide.QtMultimedia.QAudio.State.IdleState
    IOError = PySide.QtMultimedia.QAudio.Error.IOError
    Mode = None # (!) real value is "<type 'PySide.QtMultimedia.QAudio.Mode'>"
    NoError = PySide.QtMultimedia.QAudio.Error.NoError
    OpenError = PySide.QtMultimedia.QAudio.Error.OpenError
    State = None # (!) real value is "<type 'PySide.QtMultimedia.QAudio.State'>"
    StoppedState = PySide.QtMultimedia.QAudio.State.StoppedState
    SuspendedState = PySide.QtMultimedia.QAudio.State.SuspendedState
    UnderrunError = PySide.QtMultimedia.QAudio.Error.UnderrunError


class QAudioDeviceInfo(__Shiboken.Object):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def defaultInputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def defaultOutputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def deviceName(self, *args, **kwargs): # real signature unknown
        pass

    def isFormatSupported(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, *args, **kwargs): # real signature unknown
        pass

    def preferredFormat(self, *args, **kwargs): # real signature unknown
        pass

    def supportedByteOrders(self, *args, **kwargs): # real signature unknown
        pass

    def supportedChannelCounts(self, *args, **kwargs): # real signature unknown
        pass

    def supportedChannels(self, *args, **kwargs): # real signature unknown
        pass

    def supportedCodecs(self, *args, **kwargs): # real signature unknown
        pass

    def supportedFrequencies(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleRates(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleSizes(self, *args, **kwargs): # real signature unknown
        pass

    def supportedSampleTypes(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass


class QAudioEngineFactoryInterface(__PySide_QtCore.QFactoryInterface):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def createDeviceInfo(self, *args, **kwargs): # real signature unknown
        pass

    def createInput(self, *args, **kwargs): # real signature unknown
        pass

    def createOutput(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QAudioEnginePlugin(__PySide_QtCore.QObject, QAudioEngineFactoryInterface):
    # no doc
    def availableDevices(self, *args, **kwargs): # real signature unknown
        pass

    def createDeviceInfo(self, *args, **kwargs): # real signature unknown
        pass

    def createInput(self, *args, **kwargs): # real signature unknown
        pass

    def createOutput(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004ED40C8>'


class QAudioFormat(__Shiboken.Object):
    # no doc
    def byteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def channelCount(self, *args, **kwargs): # real signature unknown
        pass

    def channels(self, *args, **kwargs): # real signature unknown
        pass

    def codec(self, *args, **kwargs): # real signature unknown
        pass

    def frequency(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def sampleRate(self, *args, **kwargs): # real signature unknown
        pass

    def sampleSize(self, *args, **kwargs): # real signature unknown
        pass

    def sampleType(self, *args, **kwargs): # real signature unknown
        pass

    def setByteOrder(self, *args, **kwargs): # real signature unknown
        pass

    def setChannelCount(self, *args, **kwargs): # real signature unknown
        pass

    def setChannels(self, *args, **kwargs): # real signature unknown
        pass

    def setCodec(self, *args, **kwargs): # real signature unknown
        pass

    def setFrequency(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleRate(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleType(self, *args, **kwargs): # real signature unknown
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

    BigEndian = PySide.QtMultimedia.QAudioFormat.Endian.BigEndian
    Endian = None # (!) real value is "<type 'PySide.QtMultimedia.QAudioFormat.Endian'>"
    Float = PySide.QtMultimedia.QAudioFormat.SampleType.Float
    LittleEndian = PySide.QtMultimedia.QAudioFormat.Endian.LittleEndian
    SampleType = None # (!) real value is "<type 'PySide.QtMultimedia.QAudioFormat.SampleType'>"
    SignedInt = PySide.QtMultimedia.QAudioFormat.SampleType.SignedInt
    Unknown = PySide.QtMultimedia.QAudioFormat.SampleType.Unknown
    UnSignedInt = PySide.QtMultimedia.QAudioFormat.SampleType.UnSignedInt


class QAudioInput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesReady(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004ED38C8>'


class QAudioOutput(__PySide_QtCore.QObject):
    # no doc
    def bufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def bytesFree(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def notifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def periodSize(self, *args, **kwargs): # real signature unknown
        pass

    def processedUSecs(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def suspend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000004ED3E08>'


class QVideoFrame(__Shiboken.Object):
    # no doc
    def bits(self, *args, **kwargs): # real signature unknown
        pass

    def bytesPerLine(self, *args, **kwargs): # real signature unknown
        pass

    def endTime(self, *args, **kwargs): # real signature unknown
        pass

    def fieldType(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def imageFormatFromPixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def isMapped(self, *args, **kwargs): # real signature unknown
        pass

    def isReadable(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def mapMode(self, *args, **kwargs): # real signature unknown
        pass

    def mappedBytes(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormatFromImageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setEndTime(self, *args, **kwargs): # real signature unknown
        pass

    def setFieldType(self, *args, **kwargs): # real signature unknown
        pass

    def setStartTime(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def startTime(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BottomField = PySide.QtMultimedia.QVideoFrame.FieldType.BottomField
    FieldType = None # (!) real value is "<type 'PySide.QtMultimedia.QVideoFrame.FieldType'>"
    Format_ARGB32 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_ARGB32
    Format_ARGB32_Premultiplied = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_ARGB32_Premultiplied
    Format_ARGB8565_Premultiplied = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_ARGB8565_Premultiplied
    Format_AYUV444 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_AYUV444
    Format_AYUV444_Premultiplied = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_AYUV444_Premultiplied
    Format_BGR24 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR24
    Format_BGR32 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR32
    Format_BGR555 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR555
    Format_BGR565 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR565
    Format_BGRA32 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_BGRA32
    Format_BGRA32_Premultiplied = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_BGRA32_Premultiplied
    Format_BGRA5658_Premultiplied = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_BGRA5658_Premultiplied
    Format_IMC1 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC1
    Format_IMC2 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC2
    Format_IMC3 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC3
    Format_IMC4 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC4
    Format_Invalid = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_Invalid
    Format_NV12 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_NV12
    Format_NV21 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_NV21
    Format_RGB24 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB24
    Format_RGB32 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB32
    Format_RGB555 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB555
    Format_RGB565 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB565
    Format_User = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_User
    Format_UYVY = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_UYVY
    Format_Y16 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_Y16
    Format_Y8 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_Y8
    Format_YUV420P = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_YUV420P
    Format_YUV444 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_YUV444
    Format_YUYV = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_YUYV
    Format_YV12 = PySide.QtMultimedia.QVideoFrame.PixelFormat.Format_YV12
    InterlacedFrame = PySide.QtMultimedia.QVideoFrame.FieldType.InterlacedFrame
    PixelFormat = None # (!) real value is "<type 'PySide.QtMultimedia.QVideoFrame.PixelFormat'>"
    ProgressiveFrame = PySide.QtMultimedia.QVideoFrame.FieldType.ProgressiveFrame
    TopField = PySide.QtMultimedia.QVideoFrame.FieldType.TopField


class QVideoSurfaceFormat(__Shiboken.Object):
    # no doc
    def frameHeight(self, *args, **kwargs): # real signature unknown
        pass

    def frameRate(self, *args, **kwargs): # real signature unknown
        pass

    def frameSize(self, *args, **kwargs): # real signature unknown
        pass

    def frameWidth(self, *args, **kwargs): # real signature unknown
        pass

    def handleType(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def pixelAspectRatio(self, *args, **kwargs): # real signature unknown
        pass

    def pixelFormat(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyNames(self, *args, **kwargs): # real signature unknown
        pass

    def scanLineDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameRate(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameSize(self, *args, **kwargs): # real signature unknown
        pass

    def setPixelAspectRatio(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setScanLineDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setViewport(self, *args, **kwargs): # real signature unknown
        pass

    def setYCbCrColorSpace(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def viewport(self, *args, **kwargs): # real signature unknown
        pass

    def yCbCrColorSpace(self, *args, **kwargs): # real signature unknown
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

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    BottomToTop = PySide.QtMultimedia.QVideoSurfaceFormat.Direction.BottomToTop
    Direction = None # (!) real value is "<type 'PySide.QtMultimedia.QVideoSurfaceFormat.Direction'>"
    TopToBottom = PySide.QtMultimedia.QVideoSurfaceFormat.Direction.TopToBottom
    YCbCrColorSpace = None # (!) real value is "<type 'PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace'>"
    YCbCr_BT601 = PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_BT601
    YCbCr_BT709 = PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_BT709
    YCbCr_CustomMatrix = PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_CustomMatrix
    YCbCr_JPEG = PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_JPEG
    YCbCr_Undefined = PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_Undefined
    YCbCr_xvYCC601 = PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_xvYCC601
    YCbCr_xvYCC709 = PySide.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_xvYCC709


