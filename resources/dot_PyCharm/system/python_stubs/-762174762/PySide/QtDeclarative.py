# encoding: utf-8
# module PySide.QtDeclarative
# from C:\Python27\lib\site-packages\PySide\QtDeclarative.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import PySide.QtGui as __PySide_QtGui
import Shiboken as __Shiboken


# Variables with simple values

QML_HAS_ATTACHED_PROPERTIES = 1

# functions

def qmlRegisterType(*args, **kwargs): # real signature unknown
    pass

# classes

class ListProperty(Property):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QDeclarativeComponent(__PySide_QtCore.QObject):
    # no doc
    def beginCreate(self, *args, **kwargs): # real signature unknown
        pass

    def completeCreate(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def creationContext(self, *args, **kwargs): # real signature unknown
        pass

    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        pass

    def isLoading(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isReady(self, *args, **kwargs): # real signature unknown
        pass

    def loadUrl(self, *args, **kwargs): # real signature unknown
        pass

    def progress(self, *args, **kwargs): # real signature unknown
        pass

    def progressChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def status(self, *args, **kwargs): # real signature unknown
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def url(self, *args, **kwargs): # real signature unknown
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

    Error = PySide.QtDeclarative.QDeclarativeComponent.Status.Error
    Loading = PySide.QtDeclarative.QDeclarativeComponent.Status.Loading
    Null = PySide.QtDeclarative.QDeclarativeComponent.Status.Null
    Ready = PySide.QtDeclarative.QDeclarativeComponent.Status.Ready
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000053B3508>'
    Status = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeComponent.Status'>"


class QDeclarativeContext(__PySide_QtCore.QObject):
    # no doc
    def baseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def contextObject(self, *args, **kwargs): # real signature unknown
        pass

    def contextProperty(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def parentContext(self, *args, **kwargs): # real signature unknown
        pass

    def resolvedUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setContextObject(self, *args, **kwargs): # real signature unknown
        pass

    def setContextProperty(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000534E208>'


class QDeclarativeEngine(__PySide_QtCore.QObject):
    # no doc
    def addImageProvider(self, *args, **kwargs): # real signature unknown
        pass

    def addImportPath(self, *args, **kwargs): # real signature unknown
        pass

    def addPluginPath(self, *args, **kwargs): # real signature unknown
        pass

    def baseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def clearComponentCache(self, *args, **kwargs): # real signature unknown
        pass

    def contextForObject(self, *args, **kwargs): # real signature unknown
        pass

    def imageProvider(self, *args, **kwargs): # real signature unknown
        pass

    def importPathList(self, *args, **kwargs): # real signature unknown
        pass

    def importPlugin(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessManager(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessManagerFactory(self, *args, **kwargs): # real signature unknown
        pass

    def objectOwnership(self, *args, **kwargs): # real signature unknown
        pass

    def offlineStoragePath(self, *args, **kwargs): # real signature unknown
        pass

    def outputWarningsToStandardError(self, *args, **kwargs): # real signature unknown
        pass

    def pluginPathList(self, *args, **kwargs): # real signature unknown
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def removeImageProvider(self, *args, **kwargs): # real signature unknown
        pass

    def rootContext(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setContextForObject(self, *args, **kwargs): # real signature unknown
        pass

    def setImportPathList(self, *args, **kwargs): # real signature unknown
        pass

    def setNetworkAccessManagerFactory(self, *args, **kwargs): # real signature unknown
        pass

    def setObjectOwnership(self, *args, **kwargs): # real signature unknown
        pass

    def setOfflineStoragePath(self, *args, **kwargs): # real signature unknown
        pass

    def setOutputWarningsToStandardError(self, *args, **kwargs): # real signature unknown
        pass

    def setPluginPathList(self, *args, **kwargs): # real signature unknown
        pass

    def warnings(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    CppOwnership = PySide.QtDeclarative.QDeclarativeEngine.ObjectOwnership.CppOwnership
    JavaScriptOwnership = PySide.QtDeclarative.QDeclarativeEngine.ObjectOwnership.JavaScriptOwnership
    ObjectOwnership = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeEngine.ObjectOwnership'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000053515C8>'


class QDeclarativeError(__Shiboken.Object):
    # no doc
    def column(self, *args, **kwargs): # real signature unknown
        pass

    def description(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def line(self, *args, **kwargs): # real signature unknown
        pass

    def setColumn(self, *args, **kwargs): # real signature unknown
        pass

    def setDescription(self, *args, **kwargs): # real signature unknown
        pass

    def setLine(self, *args, **kwargs): # real signature unknown
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class QDeclarativeExpression(__PySide_QtCore.QObject):
    # no doc
    def clearError(self, *args, **kwargs): # real signature unknown
        pass

    def context(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def evaluate(self, *args, **kwargs): # real signature unknown
        pass

    def expression(self, *args, **kwargs): # real signature unknown
        pass

    def hasError(self, *args, **kwargs): # real signature unknown
        pass

    def lineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def notifyOnValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def scopeObject(self, *args, **kwargs): # real signature unknown
        pass

    def setExpression(self, *args, **kwargs): # real signature unknown
        pass

    def setNotifyOnValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setSourceLocation(self, *args, **kwargs): # real signature unknown
        pass

    def sourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000005351E88>'


class QDeclarativeExtensionInterface(__Shiboken.Object):
    # no doc
    def initializeEngine(self, *args, **kwargs): # real signature unknown
        pass

    def registerTypes(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QDeclarativeExtensionPlugin(__PySide_QtCore.QObject, QDeclarativeExtensionInterface):
    # no doc
    def initializeEngine(self, *args, **kwargs): # real signature unknown
        pass

    def registerTypes(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000534F8C8>'


class QDeclarativeImageProvider(__Shiboken.Object):
    # no doc
    def imageType(self, *args, **kwargs): # real signature unknown
        pass

    def requestImage(self, *args, **kwargs): # real signature unknown
        pass

    def requestPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Image = PySide.QtDeclarative.QDeclarativeImageProvider.ImageType.Image
    ImageType = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeImageProvider.ImageType'>"
    Pixmap = PySide.QtDeclarative.QDeclarativeImageProvider.ImageType.Pixmap


class QDeclarativeParserStatus(__Shiboken.Object):
    # no doc
    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QDeclarativeItem(__PySide_QtGui.QGraphicsObject, QDeclarativeParserStatus):
    # no doc
    def activeFocusChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def baselineOffset(self, *args, **kwargs): # real signature unknown
        pass

    def baselineOffsetChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def boundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def childAt(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRect(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRectChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def clip(self, *args, **kwargs): # real signature unknown
        pass

    def clipChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def focusChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def forceActiveFocus(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hasActiveFocus(self, *args, **kwargs): # real signature unknown
        pass

    def hasFocus(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def heightValid(self, *args, **kwargs): # real signature unknown
        pass

    def implicitHeight(self, *args, **kwargs): # real signature unknown
        pass

    def implicitHeightChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def implicitWidth(self, *args, **kwargs): # real signature unknown
        pass

    def implicitWidthChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodPreHandler(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def isComponentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def itemChange(self, *args, **kwargs): # real signature unknown
        pass

    def keepMouseGrab(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressPreHandler(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleasePreHandler(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, *args, **kwargs): # real signature unknown
        pass

    def parentChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def parentItem(self, *args, **kwargs): # real signature unknown
        pass

    def resetHeight(self, *args, **kwargs): # real signature unknown
        pass

    def resetWidth(self, *args, **kwargs): # real signature unknown
        pass

    def sceneEvent(self, *args, **kwargs): # real signature unknown
        pass

    def setBaselineOffset(self, *args, **kwargs): # real signature unknown
        pass

    def setClip(self, *args, **kwargs): # real signature unknown
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        pass

    def setHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setImplicitHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setImplicitWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setKeepMouseGrab(self, *args, **kwargs): # real signature unknown
        pass

    def setParentItem(self, *args, **kwargs): # real signature unknown
        pass

    def setSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSmooth(self, *args, **kwargs): # real signature unknown
        pass

    def setTransformOrigin(self, *args, **kwargs): # real signature unknown
        pass

    def setWidth(self, *args, **kwargs): # real signature unknown
        pass

    def smooth(self, *args, **kwargs): # real signature unknown
        pass

    def smoothChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def transformOrigin(self, *args, **kwargs): # real signature unknown
        pass

    def transformOriginChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def widthValid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Bottom = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.Bottom
    BottomLeft = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.BottomLeft
    BottomRight = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.BottomRight
    Center = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.Center
    Left = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.Left
    Right = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.Right
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000534F708>'
    Top = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.Top
    TopLeft = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.TopLeft
    TopRight = PySide.QtDeclarative.QDeclarativeItem.TransformOrigin.TopRight
    TransformOrigin = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeItem.TransformOrigin'>"


class QDeclarativeListReference(__Shiboken.Object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def canAppend(self, *args, **kwargs): # real signature unknown
        pass

    def canAt(self, *args, **kwargs): # real signature unknown
        pass

    def canClear(self, *args, **kwargs): # real signature unknown
        pass

    def canCount(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def listElementType(self, *args, **kwargs): # real signature unknown
        pass

    def object(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QDeclarativeNetworkAccessManagerFactory(__Shiboken.Object):
    # no doc
    def create(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QDeclarativeProperty(__Shiboken.Object):
    # no doc
    def connectNotifySignal(self, *args, **kwargs): # real signature unknown
        pass

    def hasNotifySignal(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, *args, **kwargs): # real signature unknown
        pass

    def isDesignable(self, *args, **kwargs): # real signature unknown
        pass

    def isProperty(self, *args, **kwargs): # real signature unknown
        pass

    def isResettable(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalProperty(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def isWritable(self, *args, **kwargs): # real signature unknown
        pass

    def method(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def needsNotifySignal(self, *args, **kwargs): # real signature unknown
        pass

    def object(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyType(self, *args, **kwargs): # real signature unknown
        pass

    def propertyTypeCategory(self, *args, **kwargs): # real signature unknown
        pass

    def propertyTypeName(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
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

    Invalid = PySide.QtDeclarative.QDeclarativeProperty.Type.Invalid
    InvalidCategory = PySide.QtDeclarative.QDeclarativeProperty.PropertyTypeCategory.InvalidCategory
    List = PySide.QtDeclarative.QDeclarativeProperty.PropertyTypeCategory.List
    Normal = PySide.QtDeclarative.QDeclarativeProperty.PropertyTypeCategory.Normal
    Object = PySide.QtDeclarative.QDeclarativeProperty.PropertyTypeCategory.Object
    Property = PySide.QtDeclarative.QDeclarativeProperty.Type.Property
    PropertyTypeCategory = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeProperty.PropertyTypeCategory'>"
    SignalProperty = PySide.QtDeclarative.QDeclarativeProperty.Type.SignalProperty
    Type = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeProperty.Type'>"


class QDeclarativePropertyMap(__PySide_QtCore.QObject):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000005351908>'


class QDeclarativePropertyValueSource(__Shiboken.Object):
    # no doc
    def setTarget(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QDeclarativeScriptString(__Shiboken.Object):
    # no doc
    def context(self, *args, **kwargs): # real signature unknown
        pass

    def scopeObject(self, *args, **kwargs): # real signature unknown
        pass

    def script(self, *args, **kwargs): # real signature unknown
        pass

    def setContext(self, *args, **kwargs): # real signature unknown
        pass

    def setScopeObject(self, *args, **kwargs): # real signature unknown
        pass

    def setScript(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QDeclarativeView(__PySide_QtGui.QGraphicsView):
    # no doc
    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def initialSize(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def rootContext(self, *args, **kwargs): # real signature unknown
        pass

    def rootObject(self, *args, **kwargs): # real signature unknown
        pass

    def sceneResized(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def setResizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def setRootObject(self, *args, **kwargs): # real signature unknown
        pass

    def setSource(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def source(self, *args, **kwargs): # real signature unknown
        pass

    def status(self, *args, **kwargs): # real signature unknown
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Error = PySide.QtDeclarative.QDeclarativeView.Status.Error
    Loading = PySide.QtDeclarative.QDeclarativeView.Status.Loading
    Null = PySide.QtDeclarative.QDeclarativeView.Status.Null
    Ready = PySide.QtDeclarative.QDeclarativeView.Status.Ready
    ResizeMode = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeView.ResizeMode'>"
    SizeRootObjectToView = PySide.QtDeclarative.QDeclarativeView.ResizeMode.SizeRootObjectToView
    SizeViewToRootObject = PySide.QtDeclarative.QDeclarativeView.ResizeMode.SizeViewToRootObject
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000053B3DC8>'
    Status = None # (!) real value is "<type 'PySide.QtDeclarative.QDeclarativeView.Status'>"


