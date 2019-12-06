# encoding: utf-8
# module PySide.QtOpenGL
# from C:\Python27\lib\site-packages\PySide\QtOpenGL.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import PySide.QtGui as __PySide_QtGui
import Shiboken as __Shiboken


# no functions
# classes

class QGL(__Shiboken.Object):
    # no doc
    def setPreferredPaintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AccumBuffer = PySide.QtOpenGL.QGL.FormatOption.AccumBuffer
    AlphaChannel = PySide.QtOpenGL.QGL.FormatOption.AlphaChannel
    ColorIndex = PySide.QtOpenGL.QGL.FormatOption.ColorIndex
    DeprecatedFunctions = PySide.QtOpenGL.QGL.FormatOption.DeprecatedFunctions
    DepthBuffer = PySide.QtOpenGL.QGL.FormatOption.DepthBuffer
    DirectRendering = PySide.QtOpenGL.QGL.FormatOption.DirectRendering
    DoubleBuffer = PySide.QtOpenGL.QGL.FormatOption.DoubleBuffer
    FormatOption = None # (!) real value is "<type 'PySide.QtOpenGL.QGL.FormatOption'>"
    FormatOptions = None # (!) real value is "<type 'FormatOptions'>"
    HasOverlay = PySide.QtOpenGL.QGL.FormatOption.HasOverlay
    IndirectRendering = PySide.QtOpenGL.QGL.FormatOption.IndirectRendering
    NoAccumBuffer = PySide.QtOpenGL.QGL.FormatOption.NoAccumBuffer
    NoAlphaChannel = PySide.QtOpenGL.QGL.FormatOption.NoAlphaChannel
    NoDeprecatedFunctions = PySide.QtOpenGL.QGL.FormatOption.NoDeprecatedFunctions
    NoDepthBuffer = PySide.QtOpenGL.QGL.FormatOption.NoDepthBuffer
    NoOverlay = PySide.QtOpenGL.QGL.FormatOption.NoOverlay
    NoSampleBuffers = PySide.QtOpenGL.QGL.FormatOption.NoSampleBuffers
    NoStencilBuffer = PySide.QtOpenGL.QGL.FormatOption.NoStencilBuffer
    NoStereoBuffers = PySide.QtOpenGL.QGL.FormatOption.NoStereoBuffers
    Rgba = PySide.QtOpenGL.QGL.FormatOption.Rgba
    SampleBuffers = PySide.QtOpenGL.QGL.FormatOption.SampleBuffers
    SingleBuffer = PySide.QtOpenGL.QGL.FormatOption.SingleBuffer
    StencilBuffer = PySide.QtOpenGL.QGL.FormatOption.StencilBuffer
    StereoBuffers = PySide.QtOpenGL.QGL.FormatOption.StereoBuffers


class QGLBuffer(__Shiboken.Object):
    # no doc
    def allocate(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bufferId(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def isCreated(self, *args, **kwargs): # real signature unknown
        pass

    def map(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def setUsagePattern(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def unmap(self, *args, **kwargs): # real signature unknown
        pass

    def usagePattern(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
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

    Access = None # (!) real value is "<type 'PySide.QtOpenGL.QGLBuffer.Access'>"
    DynamicCopy = PySide.QtOpenGL.QGLBuffer.UsagePattern.DynamicCopy
    DynamicDraw = PySide.QtOpenGL.QGLBuffer.UsagePattern.DynamicDraw
    DynamicRead = PySide.QtOpenGL.QGLBuffer.UsagePattern.DynamicRead
    IndexBuffer = PySide.QtOpenGL.QGLBuffer.Type.IndexBuffer
    PixelPackBuffer = PySide.QtOpenGL.QGLBuffer.Type.PixelPackBuffer
    PixelUnpackBuffer = PySide.QtOpenGL.QGLBuffer.Type.PixelUnpackBuffer
    ReadOnly = PySide.QtOpenGL.QGLBuffer.Access.ReadOnly
    ReadWrite = PySide.QtOpenGL.QGLBuffer.Access.ReadWrite
    StaticCopy = PySide.QtOpenGL.QGLBuffer.UsagePattern.StaticCopy
    StaticDraw = PySide.QtOpenGL.QGLBuffer.UsagePattern.StaticDraw
    StaticRead = PySide.QtOpenGL.QGLBuffer.UsagePattern.StaticRead
    StreamCopy = PySide.QtOpenGL.QGLBuffer.UsagePattern.StreamCopy
    StreamDraw = PySide.QtOpenGL.QGLBuffer.UsagePattern.StreamDraw
    StreamRead = PySide.QtOpenGL.QGLBuffer.UsagePattern.StreamRead
    Type = None # (!) real value is "<type 'PySide.QtOpenGL.QGLBuffer.Type'>"
    UsagePattern = None # (!) real value is "<type 'PySide.QtOpenGL.QGLBuffer.UsagePattern'>"
    VertexBuffer = PySide.QtOpenGL.QGLBuffer.Type.VertexBuffer
    WriteOnly = PySide.QtOpenGL.QGLBuffer.Access.WriteOnly


class QGLColormap(__Shiboken.Object):
    # no doc
    def entryColor(self, *args, **kwargs): # real signature unknown
        pass

    def entryRgb(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, *args, **kwargs): # real signature unknown
        pass

    def findNearest(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def setEntry(self, *args, **kwargs): # real signature unknown
        pass

    def setHandle(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QGLContext(__Shiboken.Object):
    # no doc
    def areSharing(self, *args, **kwargs): # real signature unknown
        pass

    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def chooseContext(self, *args, **kwargs): # real signature unknown
        pass

    def colorIndex(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentContext(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def device(self, *args, **kwargs): # real signature unknown
        pass

    def deviceIsPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def getProcAddress(self, *args, **kwargs): # real signature unknown
        pass

    def initialized(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def overlayTransparentColor(self, *args, **kwargs): # real signature unknown
        pass

    def requestedFormat(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialized(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureCacheLimit(self, *args, **kwargs): # real signature unknown
        pass

    def setValid(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowCreated(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def textureCacheLimit(self, *args, **kwargs): # real signature unknown
        pass

    def windowCreated(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BindOption = None # (!) real value is "<type 'PySide.QtOpenGL.QGLContext.BindOption'>"
    BindOptions = None # (!) real value is "<type 'BindOptions'>"
    CanFlipNativePixmapBindOption = PySide.QtOpenGL.QGLContext.BindOption.CanFlipNativePixmapBindOption
    DefaultBindOption = PySide.QtOpenGL.QGLContext.BindOption.DefaultBindOption
    InternalBindOption = PySide.QtOpenGL.QGLContext.BindOption.InternalBindOption
    InvertedYBindOption = PySide.QtOpenGL.QGLContext.BindOption.InvertedYBindOption
    LinearFilteringBindOption = PySide.QtOpenGL.QGLContext.BindOption.LinearFilteringBindOption
    MemoryManagedBindOption = PySide.QtOpenGL.QGLContext.BindOption.MemoryManagedBindOption
    MipmapBindOption = PySide.QtOpenGL.QGLContext.BindOption.MipmapBindOption
    NoBindOption = PySide.QtOpenGL.QGLContext.BindOption.NoBindOption
    PremultipliedAlphaBindOption = PySide.QtOpenGL.QGLContext.BindOption.PremultipliedAlphaBindOption


class QGLFormat(__Shiboken.Object):
    # no doc
    def accum(self, *args, **kwargs): # real signature unknown
        pass

    def accumBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def alpha(self, *args, **kwargs): # real signature unknown
        pass

    def alphaBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def blueBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFormat(self, *args, **kwargs): # real signature unknown
        pass

    def defaultOverlayFormat(self, *args, **kwargs): # real signature unknown
        pass

    def depth(self, *args, **kwargs): # real signature unknown
        pass

    def depthBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def directRendering(self, *args, **kwargs): # real signature unknown
        pass

    def doubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def greenBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGL(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLOverlays(self, *args, **kwargs): # real signature unknown
        pass

    def hasOverlay(self, *args, **kwargs): # real signature unknown
        pass

    def majorVersion(self, *args, **kwargs): # real signature unknown
        pass

    def minorVersion(self, *args, **kwargs): # real signature unknown
        pass

    def openGLVersionFlags(self, *args, **kwargs): # real signature unknown
        pass

    def plane(self, *args, **kwargs): # real signature unknown
        pass

    def profile(self, *args, **kwargs): # real signature unknown
        pass

    def redBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def rgba(self, *args, **kwargs): # real signature unknown
        pass

    def sampleBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def samples(self, *args, **kwargs): # real signature unknown
        pass

    def setAccum(self, *args, **kwargs): # real signature unknown
        pass

    def setAccumBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setAlpha(self, *args, **kwargs): # real signature unknown
        pass

    def setAlphaBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setBlueBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultOverlayFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setDepth(self, *args, **kwargs): # real signature unknown
        pass

    def setDepthBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setDirectRendering(self, *args, **kwargs): # real signature unknown
        pass

    def setDoubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def setGreenBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setOption(self, *args, **kwargs): # real signature unknown
        pass

    def setOverlay(self, *args, **kwargs): # real signature unknown
        pass

    def setPlane(self, *args, **kwargs): # real signature unknown
        pass

    def setProfile(self, *args, **kwargs): # real signature unknown
        pass

    def setRedBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setRgba(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def setSamples(self, *args, **kwargs): # real signature unknown
        pass

    def setStencil(self, *args, **kwargs): # real signature unknown
        pass

    def setStencilBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setStereo(self, *args, **kwargs): # real signature unknown
        pass

    def setSwapInterval(self, *args, **kwargs): # real signature unknown
        pass

    def setVersion(self, *args, **kwargs): # real signature unknown
        pass

    def stencil(self, *args, **kwargs): # real signature unknown
        pass

    def stencilBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def stereo(self, *args, **kwargs): # real signature unknown
        pass

    def swapInterval(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, *args, **kwargs): # real signature unknown
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

    CompatibilityProfile = PySide.QtOpenGL.QGLFormat.OpenGLContextProfile.CompatibilityProfile
    CoreProfile = PySide.QtOpenGL.QGLFormat.OpenGLContextProfile.CoreProfile
    NoProfile = PySide.QtOpenGL.QGLFormat.OpenGLContextProfile.NoProfile
    OpenGLContextProfile = None # (!) real value is "<type 'PySide.QtOpenGL.QGLFormat.OpenGLContextProfile'>"
    OpenGLVersionFlag = None # (!) real value is "<type 'PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag'>"
    OpenGLVersionFlags = None # (!) real value is "<type 'OpenGLVersionFlags'>"
    OpenGL_ES_CommonLite_Version_1_0 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_CommonLite_Version_1_0
    OpenGL_ES_CommonLite_Version_1_1 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_CommonLite_Version_1_1
    OpenGL_ES_Common_Version_1_0 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_Common_Version_1_0
    OpenGL_ES_Common_Version_1_1 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_Common_Version_1_1
    OpenGL_ES_Version_2_0 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_ES_Version_2_0
    OpenGL_Version_1_1 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_1
    OpenGL_Version_1_2 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_2
    OpenGL_Version_1_3 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_3
    OpenGL_Version_1_4 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_4
    OpenGL_Version_1_5 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_1_5
    OpenGL_Version_2_0 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_2_0
    OpenGL_Version_2_1 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_2_1
    OpenGL_Version_3_0 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_0
    OpenGL_Version_3_1 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_1
    OpenGL_Version_3_2 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_2
    OpenGL_Version_3_3 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_3_3
    OpenGL_Version_4_0 = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_4_0
    OpenGL_Version_None = PySide.QtOpenGL.QGLFormat.OpenGLVersionFlag.OpenGL_Version_None


class QGLFramebufferObject(__PySide_QtGui.QPaintDevice):
    # no doc
    def attachment(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bindDefault(self, *args, **kwargs): # real signature unknown
        pass

    def blitFramebuffer(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLFramebufferBlit(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLFramebufferObjects(self, *args, **kwargs): # real signature unknown
        pass

    def isBound(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def texture(self, *args, **kwargs): # real signature unknown
        pass

    def toImage(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Attachment = None # (!) real value is "<type 'PySide.QtOpenGL.QGLFramebufferObject.Attachment'>"
    CombinedDepthStencil = PySide.QtOpenGL.QGLFramebufferObject.Attachment.CombinedDepthStencil
    Depth = PySide.QtOpenGL.QGLFramebufferObject.Attachment.Depth
    NoAttachment = PySide.QtOpenGL.QGLFramebufferObject.Attachment.NoAttachment


class QGLFramebufferObjectFormat(__Shiboken.Object):
    # no doc
    def attachment(self, *args, **kwargs): # real signature unknown
        pass

    def internalTextureFormat(self, *args, **kwargs): # real signature unknown
        pass

    def mipmap(self, *args, **kwargs): # real signature unknown
        pass

    def samples(self, *args, **kwargs): # real signature unknown
        pass

    def setAttachment(self, *args, **kwargs): # real signature unknown
        pass

    def setInternalTextureFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setMipmap(self, *args, **kwargs): # real signature unknown
        pass

    def setSamples(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureTarget(self, *args, **kwargs): # real signature unknown
        pass

    def textureTarget(self, *args, **kwargs): # real signature unknown
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


class QGLPixelBuffer(__PySide_QtGui.QPaintDevice):
    # no doc
    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def bindToDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def generateDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLPbuffers(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def releaseFromDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def toImage(self, *args, **kwargs): # real signature unknown
        pass

    def updateDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QGLShader(__PySide_QtCore.QObject):
    # no doc
    def compileSourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def compileSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaders(self, *args, **kwargs): # real signature unknown
        pass

    def isCompiled(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def shaderId(self, *args, **kwargs): # real signature unknown
        pass

    def shaderType(self, *args, **kwargs): # real signature unknown
        pass

    def sourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Fragment = PySide.QtOpenGL.QGLShader.ShaderTypeBit.Fragment
    Geometry = PySide.QtOpenGL.QGLShader.ShaderTypeBit.Geometry
    ShaderType = None # (!) real value is "<type 'ShaderType'>"
    ShaderTypeBit = None # (!) real value is "<type 'PySide.QtOpenGL.QGLShader.ShaderTypeBit'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000485A5C8>'
    Vertex = PySide.QtOpenGL.QGLShader.ShaderTypeBit.Vertex


class QGLShaderProgram(__PySide_QtCore.QObject):
    # no doc
    def addShader(self, *args, **kwargs): # real signature unknown
        pass

    def addShaderFromSourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def addShaderFromSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def attributeLocation(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bindAttributeLocation(self, *args, **kwargs): # real signature unknown
        pass

    def disableAttributeArray(self, *args, **kwargs): # real signature unknown
        pass

    def enableAttributeArray(self, *args, **kwargs): # real signature unknown
        pass

    def geometryInputType(self, *args, **kwargs): # real signature unknown
        pass

    def geometryOutputType(self, *args, **kwargs): # real signature unknown
        pass

    def geometryOutputVertexCount(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaderPrograms(self, *args, **kwargs): # real signature unknown
        pass

    def isLinked(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def maxGeometryOutputVertices(self, *args, **kwargs): # real signature unknown
        pass

    def programId(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllShaders(self, *args, **kwargs): # real signature unknown
        pass

    def removeShader(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray2D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray3D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray4D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeValue(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometryInputType(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometryOutputType(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometryOutputVertexCount(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValue(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArrayInt(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArrayUint(self, *args, **kwargs): # real signature unknown
        pass

    def shaders(self, *args, **kwargs): # real signature unknown
        pass

    def uniformLocation(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000485A088>'


class QGLWidget(__PySide_QtGui.QWidget):
    # no doc
    def autoBufferSwap(self, *args, **kwargs): # real signature unknown
        pass

    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def colormap(self, *args, **kwargs): # real signature unknown
        pass

    def context(self, *args, **kwargs): # real signature unknown
        pass

    def convertToGLFormat(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def doubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def glDraw(self, *args, **kwargs): # real signature unknown
        pass

    def glInit(self, *args, **kwargs): # real signature unknown
        pass

    def grabFrameBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self, *args, **kwargs): # real signature unknown
        pass

    def initializeOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def makeOverlayCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def overlayContext(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintGL(self, *args, **kwargs): # real signature unknown
        pass

    def paintOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def qglClearColor(self, *args, **kwargs): # real signature unknown
        pass

    def qglColor(self, *args, **kwargs): # real signature unknown
        pass

    def renderPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def renderText(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeGL(self, *args, **kwargs): # real signature unknown
        pass

    def resizeOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoBufferSwap(self, *args, **kwargs): # real signature unknown
        pass

    def setColormap(self, *args, **kwargs): # real signature unknown
        pass

    def setMouseTracking(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def updateGL(self, *args, **kwargs): # real signature unknown
        pass

    def updateOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000485D148>'


