# encoding: utf-8
# module msvcrt
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CRT_ASSEMBLY_VERSION = '9.0.21022.8'

LIBRARIES_ASSEMBLY_NAME_PREFIX = 'Microsoft.VC90'

LK_LOCK = 1
LK_NBLCK = 2
LK_NBRLCK = 4
LK_RLCK = 3
LK_UNLCK = 0

VC_ASSEMBLY_PUBLICKEYTOKEN = '1fc8b3b9a1e18e3b'

# functions

def getch(): # real signature unknown; restored from __doc__
    """
    getch() -> key character
    
    Read a keypress and return the resulting character. Nothing is echoed to
    the console. This call will block if a keypress is not already
    available, but will not wait for Enter to be pressed. If the pressed key
    was a special function key, this will return '\000' or '\xe0'; the next
    call will return the keycode. The Control-C keypress cannot be read with
    this function.
    """
    pass

def getche(): # real signature unknown; restored from __doc__
    """
    getche() -> key character
    
    Similar to getch(), but the keypress will be echoed if it represents
    a printable character.
    """
    pass

def getwch(): # real signature unknown; restored from __doc__
    """
    getwch() -> Unicode key character
    
    Wide char variant of getch(), returning a Unicode value.
    """
    return u""

def getwche(): # real signature unknown; restored from __doc__
    """
    getwche() -> Unicode key character
    
    Wide char variant of getche(), returning a Unicode value.
    """
    return u""

def get_osfhandle(fd): # real signature unknown; restored from __doc__
    """
    get_osfhandle(fd) -> file handle
    
    Return the file handle for the file descriptor fd. Raises IOError
    if fd is not recognized.
    """
    return file('/dev/null')

def heapmin(): # real signature unknown; restored from __doc__
    """
    heapmin() -> None
    
    Force the malloc() heap to clean itself up and return unused blocks
    to the operating system. On failure, this raises IOError.
    """
    pass

def kbhit(): # real signature unknown; restored from __doc__
    """
    kbhit() -> bool
    
    Return true if a keypress is waiting to be read.
    """
    return False

def locking(fd, mode, nbytes): # real signature unknown; restored from __doc__
    """
    locking(fd, mode, nbytes) -> None
    
    Lock part of a file based on file descriptor fd from the C runtime.
    Raises IOError on failure. The locked region of the file extends from
    the current file position for nbytes bytes, and may continue beyond
    the end of the file. mode must be one of the LK_* constants listed
    below. Multiple regions in a file may be locked at the same time, but
    may not overlap. Adjacent regions are not merged; they must be unlocked
    individually.
    """
    pass

def open_osfhandle(handle, flags): # real signature unknown; restored from __doc__
    """
    open_osfhandle(handle, flags) -> file descriptor
    
    Create a C runtime file descriptor from the file handle handle. The
    flags parameter should be a bitwise OR of os.O_APPEND, os.O_RDONLY,
    and os.O_TEXT. The returned file descriptor may be used as a parameter
    to os.fdopen() to create a file object.
    """
    return file('/dev/null')

def putch(char): # real signature unknown; restored from __doc__
    """
    putch(char) -> None
    
    Print the character char to the console without buffering.
    """
    pass

def putwch(unicode_char): # real signature unknown; restored from __doc__
    """
    putwch(unicode_char) -> None
    
    Wide char variant of putch(), accepting a Unicode value.
    """
    pass

def setmode(fd, mode): # real signature unknown; restored from __doc__
    """
    setmode(fd, mode) -> Previous mode
    
    Set the line-end translation mode for the file descriptor fd. To set
    it to text mode, flags should be os.O_TEXT; for binary, it should be
    os.O_BINARY.
    """
    pass

def ungetch(char): # real signature unknown; restored from __doc__
    """
    ungetch(char) -> None
    
    Cause the character char to be "pushed back" into the console buffer;
    it will be the next character read by getch() or getche().
    """
    pass

def ungetwch(unicode_char): # real signature unknown; restored from __doc__
    """
    ungetwch(unicode_char) -> None
    
    Wide char variant of ungetch(), accepting a Unicode value.
    """
    pass

# no classes
