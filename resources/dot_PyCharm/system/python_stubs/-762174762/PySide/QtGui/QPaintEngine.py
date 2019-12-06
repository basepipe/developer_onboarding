# encoding: utf-8
# module PySide.QtGui
# from C:\Python27\lib\site-packages\PySide\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QPaintEngine(__Shiboken.Object):
    # no doc
    def begin(self, *args, **kwargs): # real signature unknown
        pass

    def clearDirty(self, *args, **kwargs): # real signature unknown
        pass

    def coordinateOffset(self, *args, **kwargs): # real signature unknown
        pass

    def drawEllipse(self, *args, **kwargs): # real signature unknown
        pass

    def drawImage(self, *args, **kwargs): # real signature unknown
        pass

    def drawLines(self, *args, **kwargs): # real signature unknown
        pass

    def drawPath(self, *args, **kwargs): # real signature unknown
        pass

    def drawPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def drawPoints(self, *args, **kwargs): # real signature unknown
        pass

    def drawPolygon(self, *args, **kwargs): # real signature unknown
        pass

    def drawRects(self, *args, **kwargs): # real signature unknown
        pass

    def drawTextItem(self, *args, **kwargs): # real signature unknown
        pass

    def drawTiledPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def end(self, *args, **kwargs): # real signature unknown
        pass

    def hasFeature(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isExtended(self, *args, **kwargs): # real signature unknown
        pass

    def paintDevice(self, *args, **kwargs): # real signature unknown
        pass

    def painter(self, *args, **kwargs): # real signature unknown
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        pass

    def setDirty(self, *args, **kwargs): # real signature unknown
        pass

    def setSystemClip(self, *args, **kwargs): # real signature unknown
        pass

    def setSystemRect(self, *args, **kwargs): # real signature unknown
        pass

    def syncState(self, *args, **kwargs): # real signature unknown
        pass

    def systemClip(self, *args, **kwargs): # real signature unknown
        pass

    def systemRect(self, *args, **kwargs): # real signature unknown
        pass

    def testDirty(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gccaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selfDestruct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    AllDirty = PySide.QtGui.QPaintEngine.DirtyFlag.AllDirty
    AllFeatures = PySide.QtGui.QPaintEngine.PaintEngineFeature.AllFeatures
    AlphaBlend = PySide.QtGui.QPaintEngine.PaintEngineFeature.AlphaBlend
    Antialiasing = PySide.QtGui.QPaintEngine.PaintEngineFeature.Antialiasing
    BlendModes = PySide.QtGui.QPaintEngine.PaintEngineFeature.BlendModes
    Blitter = PySide.QtGui.QPaintEngine.Type.Blitter
    BrushStroke = PySide.QtGui.QPaintEngine.PaintEngineFeature.BrushStroke
    ConicalGradientFill = PySide.QtGui.QPaintEngine.PaintEngineFeature.ConicalGradientFill
    ConstantOpacity = PySide.QtGui.QPaintEngine.PaintEngineFeature.ConstantOpacity
    ConvexMode = PySide.QtGui.QPaintEngine.PolygonDrawMode.ConvexMode
    CoreGraphics = PySide.QtGui.QPaintEngine.Type.CoreGraphics
    Direct3D = PySide.QtGui.QPaintEngine.Type.Direct3D
    DirtyBackground = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyBackground
    DirtyBackgroundMode = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyBackgroundMode
    DirtyBrush = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyBrush
    DirtyBrushOrigin = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyBrushOrigin
    DirtyClipEnabled = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyClipEnabled
    DirtyClipPath = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyClipPath
    DirtyClipRegion = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyClipRegion
    DirtyCompositionMode = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyCompositionMode
    DirtyFlag = None # (!) real value is "<type 'PySide.QtGui.QPaintEngine.DirtyFlag'>"
    DirtyFlags = None # (!) real value is "<type 'DirtyFlags'>"
    DirtyFont = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyFont
    DirtyHints = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyHints
    DirtyOpacity = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyOpacity
    DirtyPen = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyPen
    DirtyTransform = PySide.QtGui.QPaintEngine.DirtyFlag.DirtyTransform
    LinearGradientFill = PySide.QtGui.QPaintEngine.PaintEngineFeature.LinearGradientFill
    MacPrinter = PySide.QtGui.QPaintEngine.Type.MacPrinter
    MaskedBrush = PySide.QtGui.QPaintEngine.PaintEngineFeature.MaskedBrush
    MaxUser = PySide.QtGui.QPaintEngine.Type.MaxUser
    ObjectBoundingModeGradients = PySide.QtGui.QPaintEngine.PaintEngineFeature.ObjectBoundingModeGradients
    OddEvenMode = PySide.QtGui.QPaintEngine.PolygonDrawMode.OddEvenMode
    OpenGL = PySide.QtGui.QPaintEngine.Type.OpenGL
    OpenGL2 = PySide.QtGui.QPaintEngine.Type.OpenGL2
    OpenVG = PySide.QtGui.QPaintEngine.Type.OpenVG
    PaintBuffer = PySide.QtGui.QPaintEngine.Type.PaintBuffer
    PaintEngineFeature = None # (!) real value is "<type 'PySide.QtGui.QPaintEngine.PaintEngineFeature'>"
    PaintEngineFeatures = None # (!) real value is "<type 'PaintEngineFeatures'>"
    PainterPaths = PySide.QtGui.QPaintEngine.PaintEngineFeature.PainterPaths
    PaintOutsidePaintEvent = PySide.QtGui.QPaintEngine.PaintEngineFeature.PaintOutsidePaintEvent
    PatternBrush = PySide.QtGui.QPaintEngine.PaintEngineFeature.PatternBrush
    PatternTransform = PySide.QtGui.QPaintEngine.PaintEngineFeature.PatternTransform
    Pdf = PySide.QtGui.QPaintEngine.Type.Pdf
    PerspectiveTransform = PySide.QtGui.QPaintEngine.PaintEngineFeature.PerspectiveTransform
    Picture = PySide.QtGui.QPaintEngine.Type.Picture
    PixmapTransform = PySide.QtGui.QPaintEngine.PaintEngineFeature.PixmapTransform
    PolygonDrawMode = None # (!) real value is "<type 'PySide.QtGui.QPaintEngine.PolygonDrawMode'>"
    PolylineMode = PySide.QtGui.QPaintEngine.PolygonDrawMode.PolylineMode
    PorterDuff = PySide.QtGui.QPaintEngine.PaintEngineFeature.PorterDuff
    PostScript = PySide.QtGui.QPaintEngine.Type.PostScript
    PrimitiveTransform = PySide.QtGui.QPaintEngine.PaintEngineFeature.PrimitiveTransform
    QuickDraw = PySide.QtGui.QPaintEngine.Type.QuickDraw
    QWindowSystem = PySide.QtGui.QPaintEngine.Type.QWindowSystem
    RadialGradientFill = PySide.QtGui.QPaintEngine.PaintEngineFeature.RadialGradientFill
    Raster = PySide.QtGui.QPaintEngine.Type.Raster
    RasterOpModes = PySide.QtGui.QPaintEngine.PaintEngineFeature.RasterOpModes
    SVG = PySide.QtGui.QPaintEngine.Type.SVG
    Type = None # (!) real value is "<type 'PySide.QtGui.QPaintEngine.Type'>"
    User = PySide.QtGui.QPaintEngine.Type.User
    WindingMode = PySide.QtGui.QPaintEngine.PolygonDrawMode.WindingMode
    Windows = PySide.QtGui.QPaintEngine.Type.Windows
    X11 = PySide.QtGui.QPaintEngine.Type.X11


