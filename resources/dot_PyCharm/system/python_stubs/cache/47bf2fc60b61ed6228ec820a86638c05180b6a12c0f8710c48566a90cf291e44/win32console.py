# encoding: utf-8
# module win32console
# from C:\Python27\lib\site-packages\win32\win32console.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

ATTACH_PARENT_PROCESS = -1

BACKGROUND_BLUE = 16
BACKGROUND_GREEN = 32
BACKGROUND_INTENSITY = 128
BACKGROUND_RED = 64

COMMON_LVB_GRID_HORIZONTAL = 1024
COMMON_LVB_GRID_LVERTICAL = 2048
COMMON_LVB_GRID_RVERTICAL = 4096

COMMON_LVB_LEADING_BYTE = 256

COMMON_LVB_REVERSE_VIDEO = 16384

COMMON_LVB_TRAILING_BYTE = 512

COMMON_LVB_UNDERSCORE = 32768

CONSOLE_FULLSCREEN = 1

CONSOLE_FULLSCREEN_HARDWARE = 2
CONSOLE_FULLSCREEN_MODE = 1

CONSOLE_MOUSE_DOWN = 8
CONSOLE_MOUSE_SELECTION = 4

CONSOLE_NO_SELECTION = 0

CONSOLE_SELECTION_IN_PROGRESS = 1

CONSOLE_SELECTION_NOT_EMPTY = 2

CONSOLE_TEXTMODE_BUFFER = 1

CONSOLE_WINDOWED_MODE = 2

CTRL_BREAK_EVENT = 1

CTRL_C_EVENT = 0

ENABLE_ECHO_INPUT = 4

ENABLE_LINE_INPUT = 2

ENABLE_MOUSE_INPUT = 16

ENABLE_PROCESSED_INPUT = 1
ENABLE_PROCESSED_OUTPUT = 1

ENABLE_WINDOW_INPUT = 8

ENABLE_WRAP_AT_EOL_OUTPUT = 2

FOCUS_EVENT = 16

FOREGROUND_BLUE = 1
FOREGROUND_GREEN = 2
FOREGROUND_INTENSITY = 8
FOREGROUND_RED = 4

KEY_EVENT = 1

LOCALE_USER_DEFAULT = 1024

MENU_EVENT = 8

MOUSE_EVENT = 2

STD_ERROR_HANDLE = -12

STD_INPUT_HANDLE = -10

STD_OUTPUT_HANDLE = -11

WINDOW_BUFFER_SIZE_EVENT = 4

# functions

def AddConsoleAlias(*args, **kwargs): # real signature unknown
    """ Creates a new console alias """
    pass

def AllocConsole(*args, **kwargs): # real signature unknown
    """ Creates a new console for the calling process """
    pass

def AttachConsole(*args, **kwargs): # real signature unknown
    """ Attaches calling process to console of another process """
    pass

def CreateConsoleScreenBuffer(*args, **kwargs): # real signature unknown
    """ Creates a new console screen buffer """
    pass

def FreeConsole(*args, **kwargs): # real signature unknown
    """ Detaches process from its console """
    pass

def GenerateConsoleCtrlEvent(*args, **kwargs): # real signature unknown
    """ Sends a control signal to a group of processes attached to a common console """
    pass

def GetConsoleAliases(*args, **kwargs): # real signature unknown
    """ Retrieves aliases defined under specified executable """
    pass

def GetConsoleAliasExes(*args, **kwargs): # real signature unknown
    """ Lists all executables that have console aliases defined """
    pass

def GetConsoleCP(*args, **kwargs): # real signature unknown
    """ Returns the input code page for calling process's console """
    pass

def GetConsoleDisplayMode(*args, **kwargs): # real signature unknown
    """ Returns the current console's display mode """
    pass

def GetConsoleOutputCP(*args, **kwargs): # real signature unknown
    """ Returns the output code page for calling process's console """
    pass

def GetConsoleProcessList(*args, **kwargs): # real signature unknown
    """ Returns pids of all processes attached to current console """
    pass

def GetConsoleSelectionInfo(*args, **kwargs): # real signature unknown
    """ Returns info on text selection within the current console """
    pass

def GetConsoleTitle(*args, **kwargs): # real signature unknown
    """ Returns the title of console to which calling process is attached """
    pass

def GetConsoleWindow(*args, **kwargs): # real signature unknown
    """ Returns a handle to the console's window, or 0 if none exists """
    pass

def GetNumberOfConsoleFonts(*args, **kwargs): # real signature unknown
    """ Returns the number of fonts available to the console """
    pass

def GetStdHandle(*args, **kwargs): # real signature unknown
    """ Returns one of calling process's standard handles """
    pass

def SetConsoleCP(*args, **kwargs): # real signature unknown
    """ Sets the input code page for calling process's console """
    pass

def SetConsoleOutputCP(*args, **kwargs): # real signature unknown
    """ Sets the output code page for calling process's console """
    pass

def SetConsoleTitle(*args, **kwargs): # real signature unknown
    """ Sets the title of calling process's console """
    pass

# classes

class PyConsoleScreenBufferType(object):
    """
    Handle to a console screen buffer.
    Create using CreateConsoleScreenBuffer or PyConsoleScreenBufferType(Handle)
    """
    def Close(self, *args, **kwargs): # real signature unknown
        """ Closes the handle """
        pass

    def Detach(self, *args, **kwargs): # real signature unknown
        """ Releases reference to handle without closing it """
        pass

    def FillConsoleOutputAttribute(self, *args, **kwargs): # real signature unknown
        """ Sets text attributes for a consecutive series of characters """
        pass

    def FillConsoleOutputCharacter(self, *args, **kwargs): # real signature unknown
        """ Sets consecutive character positions to a specified character """
        pass

    def FlushConsoleInputBuffer(self, *args, **kwargs): # real signature unknown
        """ Flush input buffer for console """
        pass

    def GetConsoleCursorInfo(self, *args, **kwargs): # real signature unknown
        """ Retrieves size and visibility of console's cursor """
        pass

    def GetConsoleFontSize(self, *args, **kwargs): # real signature unknown
        """ Returns size of specified font for the console """
        pass

    def GetConsoleMode(self, *args, **kwargs): # real signature unknown
        """ Returns the input or output mode of the console buffer """
        pass

    def GetConsoleScreenBufferInfo(self, *args, **kwargs): # real signature unknown
        """ Returns the state of the screen buffer """
        pass

    def GetCurrentConsoleFont(self, *args, **kwargs): # real signature unknown
        """ Returns the currently displayed font """
        pass

    def GetLargestConsoleWindowSize(self, *args, **kwargs): # real signature unknown
        """ Returns the largest possible size for the console's window """
        pass

    def GetNumberOfConsoleInputEvents(self, *args, **kwargs): # real signature unknown
        """ Returns the number of unread records in the input queue """
        pass

    def PeekConsoleInput(self, *args, **kwargs): # real signature unknown
        """ Returns pending input records without removing them from the input queue """
        pass

    def ReadConsole(self, *args, **kwargs): # real signature unknown
        """ Reads characters from the console input buffer """
        pass

    def ReadConsoleInput(self, *args, **kwargs): # real signature unknown
        """ Reads input records and removes them from the input queue """
        pass

    def ReadConsoleOutputAttribute(self, *args, **kwargs): # real signature unknown
        """ Retrieves attributes from consecutive character cells """
        pass

    def ReadConsoleOutputCharacter(self, *args, **kwargs): # real signature unknown
        """ Reads consecutive characters from a starting position """
        pass

    def ScrollConsoleScreenBuffer(self, *args, **kwargs): # real signature unknown
        """ Scrolls a region of the display """
        pass

    def SetConsoleActiveScreenBuffer(self, *args, **kwargs): # real signature unknown
        """ Sets this handle as the currently displayed screen buffer """
        pass

    def SetConsoleCursorInfo(self, *args, **kwargs): # real signature unknown
        """ Sets the size and visibility of console's cursor """
        pass

    def SetConsoleCursorPosition(self, *args, **kwargs): # real signature unknown
        """ Sets the console screen buffer's cursor position """
        pass

    def SetConsoleDisplayMode(self, *args, **kwargs): # real signature unknown
        """ Sets the display mode of the console buffer """
        pass

    def SetConsoleFont(self, *args, **kwargs): # real signature unknown
        """ Changes the font used by the screen buffer """
        pass

    def SetConsoleMode(self, *args, **kwargs): # real signature unknown
        """ Sets the input or output mode of the console buffer """
        pass

    def SetConsoleScreenBufferSize(self, *args, **kwargs): # real signature unknown
        """ Sets the size of the console screen buffer """
        pass

    def SetConsoleTextAttribute(self, *args, **kwargs): # real signature unknown
        """ Sets character attributes for subsequent write operations """
        pass

    def SetConsoleWindowInfo(self, *args, **kwargs): # real signature unknown
        """ Changes size and position of a console's window """
        pass

    def SetStdHandle(self, *args, **kwargs): # real signature unknown
        """ Replaces one of calling process's standard handles with this handle """
        pass

    def WriteConsole(self, *args, **kwargs): # real signature unknown
        """ Writes characters at current cursor position """
        pass

    def WriteConsoleInput(self, *args, **kwargs): # real signature unknown
        """ Places input records in the console's input queue """
        pass

    def WriteConsoleOutputAttribute(self, *args, **kwargs): # real signature unknown
        """ Sets the attributes of a range of character cells """
        pass

    def WriteConsoleOutputCharacter(self, *args, **kwargs): # real signature unknown
        """ Writes a string of characters at a specified position """
        pass

    def __abs__(self): # real signature unknown; restored from __doc__
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hex__(self): # real signature unknown; restored from __doc__
        """ x.__hex__() <==> hex(x) """
        pass

    def __init__(self, Handle): # real signature unknown; restored from __doc__
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __invert__(self): # real signature unknown; restored from __doc__
        """ x.__invert__() <==> ~x """
        pass

    def __long__(self): # real signature unknown; restored from __doc__
        """ x.__long__() <==> long(x) """
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __oct__(self): # real signature unknown; restored from __doc__
        """ x.__oct__() <==> oct(x) """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdivmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass


class PyCOORDType(object):
    """ Wrapper for a COORD struct. Create using PyCOORDType(X,Y) """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, X, Y): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Horizontal coordinate"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertical coordinate"""



class PyINPUT_RECORDType(object):
    """ Wrapper for a INPUT_RECORD struct. Create using PyINPUT_RECORDType(EventType) """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, EventType): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    ButtonState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bitmask representing which mouse buttons were pressed"""

    Char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Single unicode character generated by the keypress"""

    CommandId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved"""

    ControlKeyState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """State of modifier keys, combination of CAPSLOCK_ON, ENHANCED_KEY, LEFT_ALT_PRESSED, LEFT_CTRL_PRESSED,NUMLOCK_ON, RIGHT_ALT_PRESSED, RIGHT_CTRL_PRESSED, SCROLLLOCK_ON, SHIFT_PRESSED"""

    EventFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DOUBLE_CLICK, MOUSE_MOVED or MOUSE_WHEELED, or 0.  If 0, indicates a mouse button press"""

    EventType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """One of KEY_EVENT, MOUSE_EVENT, WINDOW_BUFFER_SIZE_EVENT, MENU_EVENT, FOCUS_EVENT.  Cannot be changed after object is created"""

    KeyDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True for a key press, False for key release"""

    MousePosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Position in character coordinates"""

    RepeatCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nbr of repeats generated (key was held down if >1)"""

    SetFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """New size of screen buffer in character rows/columns"""

    VirtualKeyCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device-independent key code, win32con.VK_*"""

    VirtualScanCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Device-dependent scan code generated by keyboard"""



class PySMALL_RECTType(object):
    """ Wrapper for a SMALL_RECT struct. Create using PySMALL_RECTType(Left, Top, Right, Bottom) """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, Left, Top, Right, Bottom): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



