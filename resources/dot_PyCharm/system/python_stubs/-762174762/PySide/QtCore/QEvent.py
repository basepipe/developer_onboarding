# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QEvent(__Shiboken.Object):
    # no doc
    def accept(self, *args, **kwargs): # real signature unknown
        pass

    def ignore(self, *args, **kwargs): # real signature unknown
        pass

    def isAccepted(self, *args, **kwargs): # real signature unknown
        pass

    def registerEventType(self, *args, **kwargs): # real signature unknown
        pass

    def setAccepted(self, *args, **kwargs): # real signature unknown
        pass

    def spontaneous(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
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

    AcceptDropsChange = PySide.QtCore.QEvent.Type.AcceptDropsChange
    AccessibilityDescription = PySide.QtCore.QEvent.Type.AccessibilityDescription
    AccessibilityHelp = PySide.QtCore.QEvent.Type.AccessibilityHelp
    AccessibilityPrepare = PySide.QtCore.QEvent.Type.AccessibilityPrepare
    ActionAdded = PySide.QtCore.QEvent.Type.ActionAdded
    ActionChanged = PySide.QtCore.QEvent.Type.ActionChanged
    ActionRemoved = PySide.QtCore.QEvent.Type.ActionRemoved
    ActivateControl = PySide.QtCore.QEvent.Type.ActivateControl
    ActivationChange = PySide.QtCore.QEvent.Type.ActivationChange
    ApplicationActivate = PySide.QtCore.QEvent.Type.ApplicationActivate
    ApplicationActivated = PySide.QtCore.QEvent.Type.ApplicationActivated
    ApplicationDeactivate = PySide.QtCore.QEvent.Type.ApplicationDeactivate
    ApplicationDeactivated = PySide.QtCore.QEvent.Type.ApplicationDeactivated
    ApplicationFontChange = PySide.QtCore.QEvent.Type.ApplicationFontChange
    ApplicationLayoutDirectionChange = PySide.QtCore.QEvent.Type.ApplicationLayoutDirectionChange
    ApplicationPaletteChange = PySide.QtCore.QEvent.Type.ApplicationPaletteChange
    ApplicationWindowIconChange = PySide.QtCore.QEvent.Type.ApplicationWindowIconChange
    ChildAdded = PySide.QtCore.QEvent.Type.ChildAdded
    ChildPolished = PySide.QtCore.QEvent.Type.ChildPolished
    ChildRemoved = PySide.QtCore.QEvent.Type.ChildRemoved
    Clipboard = PySide.QtCore.QEvent.Type.Clipboard
    Close = PySide.QtCore.QEvent.Type.Close
    CloseSoftwareInputPanel = PySide.QtCore.QEvent.Type.CloseSoftwareInputPanel
    ContentsRectChange = PySide.QtCore.QEvent.Type.ContentsRectChange
    ContextMenu = PySide.QtCore.QEvent.Type.ContextMenu
    Create = PySide.QtCore.QEvent.Type.Create
    CursorChange = PySide.QtCore.QEvent.Type.CursorChange
    DeactivateControl = PySide.QtCore.QEvent.Type.DeactivateControl
    DeferredDelete = PySide.QtCore.QEvent.Type.DeferredDelete
    Destroy = PySide.QtCore.QEvent.Type.Destroy
    DragEnter = PySide.QtCore.QEvent.Type.DragEnter
    DragLeave = PySide.QtCore.QEvent.Type.DragLeave
    DragMove = PySide.QtCore.QEvent.Type.DragMove
    DragResponse = PySide.QtCore.QEvent.Type.DragResponse
    Drop = PySide.QtCore.QEvent.Type.Drop
    DynamicPropertyChange = PySide.QtCore.QEvent.Type.DynamicPropertyChange
    EmbeddingControl = PySide.QtCore.QEvent.Type.EmbeddingControl
    EnabledChange = PySide.QtCore.QEvent.Type.EnabledChange
    Enter = PySide.QtCore.QEvent.Type.Enter
    EnterWhatsThisMode = PySide.QtCore.QEvent.Type.EnterWhatsThisMode
    FileOpen = PySide.QtCore.QEvent.Type.FileOpen
    FocusIn = PySide.QtCore.QEvent.Type.FocusIn
    FocusOut = PySide.QtCore.QEvent.Type.FocusOut
    FontChange = PySide.QtCore.QEvent.Type.FontChange
    FutureCallOut = PySide.QtCore.QEvent.Type.FutureCallOut
    Gesture = PySide.QtCore.QEvent.Type.Gesture
    GestureOverride = PySide.QtCore.QEvent.Type.GestureOverride
    GrabKeyboard = PySide.QtCore.QEvent.Type.GrabKeyboard
    GrabMouse = PySide.QtCore.QEvent.Type.GrabMouse
    GraphicsSceneContextMenu = PySide.QtCore.QEvent.Type.GraphicsSceneContextMenu
    GraphicsSceneDragEnter = PySide.QtCore.QEvent.Type.GraphicsSceneDragEnter
    GraphicsSceneDragLeave = PySide.QtCore.QEvent.Type.GraphicsSceneDragLeave
    GraphicsSceneDragMove = PySide.QtCore.QEvent.Type.GraphicsSceneDragMove
    GraphicsSceneDrop = PySide.QtCore.QEvent.Type.GraphicsSceneDrop
    GraphicsSceneHelp = PySide.QtCore.QEvent.Type.GraphicsSceneHelp
    GraphicsSceneHoverEnter = PySide.QtCore.QEvent.Type.GraphicsSceneHoverEnter
    GraphicsSceneHoverLeave = PySide.QtCore.QEvent.Type.GraphicsSceneHoverLeave
    GraphicsSceneHoverMove = PySide.QtCore.QEvent.Type.GraphicsSceneHoverMove
    GraphicsSceneMouseDoubleClick = PySide.QtCore.QEvent.Type.GraphicsSceneMouseDoubleClick
    GraphicsSceneMouseMove = PySide.QtCore.QEvent.Type.GraphicsSceneMouseMove
    GraphicsSceneMousePress = PySide.QtCore.QEvent.Type.GraphicsSceneMousePress
    GraphicsSceneMouseRelease = PySide.QtCore.QEvent.Type.GraphicsSceneMouseRelease
    GraphicsSceneMove = PySide.QtCore.QEvent.Type.GraphicsSceneMove
    GraphicsSceneResize = PySide.QtCore.QEvent.Type.GraphicsSceneResize
    GraphicsSceneWheel = PySide.QtCore.QEvent.Type.GraphicsSceneWheel
    HelpRequest = PySide.QtCore.QEvent.Type.HelpRequest
    Hide = PySide.QtCore.QEvent.Type.Hide
    HideToParent = PySide.QtCore.QEvent.Type.HideToParent
    HoverEnter = PySide.QtCore.QEvent.Type.HoverEnter
    HoverLeave = PySide.QtCore.QEvent.Type.HoverLeave
    HoverMove = PySide.QtCore.QEvent.Type.HoverMove
    IconDrag = PySide.QtCore.QEvent.Type.IconDrag
    IconTextChange = PySide.QtCore.QEvent.Type.IconTextChange
    InputMethod = PySide.QtCore.QEvent.Type.InputMethod
    KeyboardLayoutChange = PySide.QtCore.QEvent.Type.KeyboardLayoutChange
    KeyPress = PySide.QtCore.QEvent.Type.KeyPress
    KeyRelease = PySide.QtCore.QEvent.Type.KeyRelease
    LanguageChange = PySide.QtCore.QEvent.Type.LanguageChange
    LayoutDirectionChange = PySide.QtCore.QEvent.Type.LayoutDirectionChange
    LayoutRequest = PySide.QtCore.QEvent.Type.LayoutRequest
    Leave = PySide.QtCore.QEvent.Type.Leave
    LeaveWhatsThisMode = PySide.QtCore.QEvent.Type.LeaveWhatsThisMode
    LocaleChange = PySide.QtCore.QEvent.Type.LocaleChange
    MacGLClearDrawable = PySide.QtCore.QEvent.Type.MacGLClearDrawable
    MacGLWindowChange = PySide.QtCore.QEvent.Type.MacGLWindowChange
    MacSizeChange = PySide.QtCore.QEvent.Type.MacSizeChange
    MaxUser = PySide.QtCore.QEvent.Type.MaxUser
    MenubarUpdated = PySide.QtCore.QEvent.Type.MenubarUpdated
    MetaCall = PySide.QtCore.QEvent.Type.MetaCall
    ModifiedChange = PySide.QtCore.QEvent.Type.ModifiedChange
    MouseButtonDblClick = PySide.QtCore.QEvent.Type.MouseButtonDblClick
    MouseButtonPress = PySide.QtCore.QEvent.Type.MouseButtonPress
    MouseButtonRelease = PySide.QtCore.QEvent.Type.MouseButtonRelease
    MouseMove = PySide.QtCore.QEvent.Type.MouseMove
    MouseTrackingChange = PySide.QtCore.QEvent.Type.MouseTrackingChange
    Move = PySide.QtCore.QEvent.Type.Move
    NativeGesture = PySide.QtCore.QEvent.Type.NativeGesture
    NetworkReplyUpdated = PySide.QtCore.QEvent.Type.NetworkReplyUpdated
    NonClientAreaMouseButtonDblClick = PySide.QtCore.QEvent.Type.NonClientAreaMouseButtonDblClick
    NonClientAreaMouseButtonPress = PySide.QtCore.QEvent.Type.NonClientAreaMouseButtonPress
    NonClientAreaMouseButtonRelease = PySide.QtCore.QEvent.Type.NonClientAreaMouseButtonRelease
    NonClientAreaMouseMove = PySide.QtCore.QEvent.Type.NonClientAreaMouseMove
    None = PySide.QtCore.QEvent.Type.None
    OkRequest = PySide.QtCore.QEvent.Type.OkRequest
    Paint = PySide.QtCore.QEvent.Type.Paint
    PaletteChange = PySide.QtCore.QEvent.Type.PaletteChange
    ParentAboutToChange = PySide.QtCore.QEvent.Type.ParentAboutToChange
    ParentChange = PySide.QtCore.QEvent.Type.ParentChange
    PlatformPanel = PySide.QtCore.QEvent.Type.PlatformPanel
    Polish = PySide.QtCore.QEvent.Type.Polish
    PolishRequest = PySide.QtCore.QEvent.Type.PolishRequest
    QueryWhatsThis = PySide.QtCore.QEvent.Type.QueryWhatsThis
    Quit = PySide.QtCore.QEvent.Type.Quit
    RequestSoftwareInputPanel = PySide.QtCore.QEvent.Type.RequestSoftwareInputPanel
    Resize = PySide.QtCore.QEvent.Type.Resize
    Shortcut = PySide.QtCore.QEvent.Type.Shortcut
    ShortcutOverride = PySide.QtCore.QEvent.Type.ShortcutOverride
    Show = PySide.QtCore.QEvent.Type.Show
    ShowToParent = PySide.QtCore.QEvent.Type.ShowToParent
    ShowWindowRequest = PySide.QtCore.QEvent.Type.ShowWindowRequest
    SockAct = PySide.QtCore.QEvent.Type.SockAct
    Speech = PySide.QtCore.QEvent.Type.Speech
    StateMachineSignal = PySide.QtCore.QEvent.Type.StateMachineSignal
    StateMachineWrapped = PySide.QtCore.QEvent.Type.StateMachineWrapped
    StatusTip = PySide.QtCore.QEvent.Type.StatusTip
    Style = PySide.QtCore.QEvent.Type.Style
    StyleChange = PySide.QtCore.QEvent.Type.StyleChange
    TabletEnterProximity = PySide.QtCore.QEvent.Type.TabletEnterProximity
    TabletLeaveProximity = PySide.QtCore.QEvent.Type.TabletLeaveProximity
    TabletMove = PySide.QtCore.QEvent.Type.TabletMove
    TabletPress = PySide.QtCore.QEvent.Type.TabletPress
    TabletRelease = PySide.QtCore.QEvent.Type.TabletRelease
    ThreadChange = PySide.QtCore.QEvent.Type.ThreadChange
    Timer = PySide.QtCore.QEvent.Type.Timer
    ToolBarChange = PySide.QtCore.QEvent.Type.ToolBarChange
    ToolTip = PySide.QtCore.QEvent.Type.ToolTip
    ToolTipChange = PySide.QtCore.QEvent.Type.ToolTipChange
    TouchBegin = PySide.QtCore.QEvent.Type.TouchBegin
    TouchEnd = PySide.QtCore.QEvent.Type.TouchEnd
    TouchUpdate = PySide.QtCore.QEvent.Type.TouchUpdate
    Type = None # (!) real value is "<type 'PySide.QtCore.QEvent.Type'>"
    UngrabKeyboard = PySide.QtCore.QEvent.Type.UngrabKeyboard
    UngrabMouse = PySide.QtCore.QEvent.Type.UngrabMouse
    UpdateLater = PySide.QtCore.QEvent.Type.UpdateLater
    UpdateRequest = PySide.QtCore.QEvent.Type.UpdateRequest
    UpdateSoftKeys = PySide.QtCore.QEvent.Type.UpdateSoftKeys
    User = PySide.QtCore.QEvent.Type.User
    WhatsThis = PySide.QtCore.QEvent.Type.WhatsThis
    WhatsThisClicked = PySide.QtCore.QEvent.Type.WhatsThisClicked
    Wheel = PySide.QtCore.QEvent.Type.Wheel
    WindowActivate = PySide.QtCore.QEvent.Type.WindowActivate
    WindowBlocked = PySide.QtCore.QEvent.Type.WindowBlocked
    WindowDeactivate = PySide.QtCore.QEvent.Type.WindowDeactivate
    WindowIconChange = PySide.QtCore.QEvent.Type.WindowIconChange
    WindowStateChange = PySide.QtCore.QEvent.Type.WindowStateChange
    WindowTitleChange = PySide.QtCore.QEvent.Type.WindowTitleChange
    WindowUnblocked = PySide.QtCore.QEvent.Type.WindowUnblocked
    WinEventAct = PySide.QtCore.QEvent.Type.WinEventAct
    WinIdChange = PySide.QtCore.QEvent.Type.WinIdChange
    ZeroTimerEvent = PySide.QtCore.QEvent.Type.ZeroTimerEvent
    ZOrderChange = PySide.QtCore.QEvent.Type.ZOrderChange


