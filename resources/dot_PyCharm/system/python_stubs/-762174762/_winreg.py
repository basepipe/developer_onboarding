# encoding: utf-8
# module _winreg
# from (built-in)
# by generator 1.147
"""
This module provides access to the Windows registry API.

Functions:

CloseKey() - Closes a registry key.
ConnectRegistry() - Establishes a connection to a predefined registry handle
                    on another computer.
CreateKey() - Creates the specified key, or opens it if it already exists.
DeleteKey() - Deletes the specified key.
DeleteValue() - Removes a named value from the specified registry key.
EnumKey() - Enumerates subkeys of the specified open registry key.
EnumValue() - Enumerates values of the specified open registry key.
ExpandEnvironmentStrings() - Expand the env strings in a REG_EXPAND_SZ string.
FlushKey() - Writes all the attributes of the specified key to the registry.
LoadKey() - Creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and stores
            registration information from a specified file into that subkey.
OpenKey() - Alias for <om win32api.RegOpenKeyEx>
OpenKeyEx() - Opens the specified key.
QueryValue() - Retrieves the value associated with the unnamed value for a
               specified key in the registry.
QueryValueEx() - Retrieves the type and data for a specified value name
                 associated with an open registry key.
QueryInfoKey() - Returns information about the specified key.
SaveKey() - Saves the specified key, and all its subkeys a file.
SetValue() - Associates a value with a specified key.
SetValueEx() - Stores data in the value field of an open registry key.

Special objects:

HKEYType -- type object for HKEY objects
error -- exception raised for Win32 errors

Integer constants:
Many constants are defined - see the documentation for each function
to see what constants are used, and where.
"""

# imports
from exceptions import error


# Variables with simple values

HKEY_CLASSES_ROOT = 18446744071562067968L

HKEY_CURRENT_CONFIG = 18446744071562067973L
HKEY_CURRENT_USER = 18446744071562067969L

HKEY_DYN_DATA = 18446744071562067974L

HKEY_LOCAL_MACHINE = 18446744071562067970L

HKEY_PERFORMANCE_DATA = 18446744071562067972L

HKEY_USERS = 18446744071562067971L

KEY_ALL_ACCESS = 983103

KEY_CREATE_LINK = 32

KEY_CREATE_SUB_KEY = 4

KEY_ENUMERATE_SUB_KEYS = 8

KEY_EXECUTE = 131097
KEY_NOTIFY = 16

KEY_QUERY_VALUE = 1

KEY_READ = 131097

KEY_SET_VALUE = 2

KEY_WOW64_32KEY = 512
KEY_WOW64_64KEY = 256

KEY_WRITE = 131078

REG_BINARY = 3

REG_CREATED_NEW_KEY = 1

REG_DWORD = 4

REG_DWORD_BIG_ENDIAN = 5

REG_DWORD_LITTLE_ENDIAN = 4

REG_EXPAND_SZ = 2

REG_FULL_RESOURCE_DESCRIPTOR = 9

REG_LEGAL_CHANGE_FILTER = 15

REG_LEGAL_OPTION = 15

REG_LINK = 6

REG_MULTI_SZ = 7

REG_NONE = 0

REG_NOTIFY_CHANGE_ATTRIBUTES = 2

REG_NOTIFY_CHANGE_LAST_SET = 4

REG_NOTIFY_CHANGE_NAME = 1
REG_NOTIFY_CHANGE_SECURITY = 8

REG_NO_LAZY_FLUSH = 4

REG_OPENED_EXISTING_KEY = 2

REG_OPTION_BACKUP_RESTORE = 4

REG_OPTION_CREATE_LINK = 2

REG_OPTION_NON_VOLATILE = 0

REG_OPTION_OPEN_LINK = 8

REG_OPTION_RESERVED = 0
REG_OPTION_VOLATILE = 1

REG_REFRESH_HIVE = 2

REG_RESOURCE_LIST = 8

REG_RESOURCE_REQUIREMENTS_LIST = 10

REG_SZ = 1

REG_WHOLE_HIVE_VOLATILE = 1

# functions

def CloseKey(hkey): # real signature unknown; restored from __doc__
    """
    CloseKey(hkey) - Closes a previously opened registry key.
    
    The hkey argument specifies a previously opened key.
    
    Note that if the key is not closed using this method, it will be
    closed when the hkey object is destroyed by Python.
    """
    pass

def ConnectRegistry(computer_name, key): # real signature unknown; restored from __doc__
    """
    key = ConnectRegistry(computer_name, key) - Establishes a connection to a predefined registry handle on another computer.
    
    computer_name is the name of the remote computer, of the form \\computername.
     If None, the local computer is used.
    key is the predefined handle to connect to.
    
    The return value is the handle of the opened key.
    If the function fails, a WindowsError exception is raised.
    """
    pass

def CreateKey(key, sub_key): # real signature unknown; restored from __doc__
    """
    key = CreateKey(key, sub_key) - Creates or opens the specified key.
    
    key is an already open key, or one of the predefined HKEY_* constants
    sub_key is a string that names the key this method opens or creates.
     If key is one of the predefined keys, sub_key may be None. In that case,
     the handle returned is the same key handle passed in to the function.
    
    If the key already exists, this function opens the existing key
    
    The return value is the handle of the opened key.
    If the function fails, an exception is raised.
    """
    pass

def CreateKeyEx(key, sub_key, res, sam): # real signature unknown; restored from __doc__
    """
    key = CreateKeyEx(key, sub_key, res, sam) - Creates or opens the specified key.
    
    key is an already open key, or one of the predefined HKEY_* constants
    sub_key is a string that names the key this method opens or creates.
    res is a reserved integer, and must be zero.  Default is zero.
    sam is an integer that specifies an access mask that describes the desired
     If key is one of the predefined keys, sub_key may be None. In that case,
     the handle returned is the same key handle passed in to the function.
    
    If the key already exists, this function opens the existing key
    
    The return value is the handle of the opened key.
    If the function fails, an exception is raised.
    """
    pass

def DeleteKey(key, sub_key): # real signature unknown; restored from __doc__
    """
    DeleteKey(key, sub_key) - Deletes the specified key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    sub_key is a string that must be a subkey of the key identified by the key parameter.
     This value must not be None, and the key may not have subkeys.
    
    This method can not delete keys with subkeys.
    
    If the method succeeds, the entire key, including all of its values,
    is removed.  If the method fails, a WindowsError exception is raised.
    """
    pass

def DeleteKeyEx(key, sub_key, sam, res): # real signature unknown; restored from __doc__
    """
    DeleteKeyEx(key, sub_key, sam, res) - Deletes the specified key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    sub_key is a string that must be a subkey of the key identified by the key parameter.
    res is a reserved integer, and must be zero.  Default is zero.
    sam is an integer that specifies an access mask that describes the desired
     This value must not be None, and the key may not have subkeys.
    
    This method can not delete keys with subkeys.
    
    If the method succeeds, the entire key, including all of its values,
    is removed.  If the method fails, a WindowsError exception is raised.
    On unsupported Windows versions, NotImplementedError is raised.
    """
    pass

def DeleteValue(key, value): # real signature unknown; restored from __doc__
    """
    DeleteValue(key, value) - Removes a named value from a registry key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    value is a string that identifies the value to remove.
    """
    pass

def DisableReflectionKey(*args, **kwargs): # real signature unknown
    """
    Disables registry reflection for 32-bit processes running on a 64-bit
    Operating System.  Will generally raise NotImplemented if executed on
    a 32-bit Operating System.
    If the key is not on the reflection list, the function succeeds but has no effect.
    Disabling reflection for a key does not affect reflection of any subkeys.
    """
    pass

def EnableReflectionKey(*args, **kwargs): # real signature unknown
    """
    Restores registry reflection for the specified disabled key.
    Will generally raise NotImplemented if executed on a 32-bit Operating System.
    Restoring reflection for a key does not affect reflection of any subkeys.
    """
    pass

def EnumKey(key, index): # real signature unknown; restored from __doc__
    """
    string = EnumKey(key, index) - Enumerates subkeys of an open registry key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    index is an integer that identifies the index of the key to retrieve.
    
    The function retrieves the name of one subkey each time it is called.
    It is typically called repeatedly until a WindowsError exception is
    raised, indicating no more values are available.
    """
    pass

def EnumValue(key, index): # real signature unknown; restored from __doc__
    """
    tuple = EnumValue(key, index) - Enumerates values of an open registry key.
    key is an already open key, or any one of the predefined HKEY_* constants.
    index is an integer that identifies the index of the value to retrieve.
    
    The function retrieves the name of one subkey each time it is called.
    It is typically called repeatedly, until a WindowsError exception
    is raised, indicating no more values.
    
    The result is a tuple of 3 items:
    value_name is a string that identifies the value.
    value_data is an object that holds the value data, and whose type depends
     on the underlying registry type.
    data_type is an integer that identifies the type of the value data.
    """
    pass

def ExpandEnvironmentStrings(string): # real signature unknown; restored from __doc__
    """ string = ExpandEnvironmentStrings(string) - Expand environment vars. """
    pass

def FlushKey(key): # real signature unknown; restored from __doc__
    """
    FlushKey(key) - Writes all the attributes of a key to the registry.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    
    It is not necessary to call RegFlushKey to change a key.
    Registry changes are flushed to disk by the registry using its lazy flusher.
    Registry changes are also flushed to disk at system shutdown.
    Unlike CloseKey(), the FlushKey() method returns only when all the data has
    been written to the registry.
    An application should only call FlushKey() if it requires absolute certainty that registry changes are on disk.
    If you don't know whether a FlushKey() call is required, it probably isn't.
    """
    pass

def LoadKey(key, sub_key, file_name): # real signature unknown; restored from __doc__
    """
    LoadKey(key, sub_key, file_name) - Creates a subkey under the specified key
    and stores registration information from a specified file into that subkey.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    sub_key is a string that identifies the sub_key to load
    file_name is the name of the file to load registry data from.
     This file must have been created with the SaveKey() function.
     Under the file allocation table (FAT) file system, the filename may not
    have an extension.
    
    A call to LoadKey() fails if the calling process does not have the
    SE_RESTORE_PRIVILEGE privilege.
    
    If key is a handle returned by ConnectRegistry(), then the path specified
    in fileName is relative to the remote computer.
    
    The docs imply key must be in the HKEY_USER or HKEY_LOCAL_MACHINE tree
    """
    pass

def OpenKey(key, sub_key, res=0, sam=None): # real signature unknown; restored from __doc__
    """
    key = OpenKey(key, sub_key, res = 0, sam = KEY_READ) - Opens the specified key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    sub_key is a string that identifies the sub_key to open
    res is a reserved integer, and must be zero.  Default is zero.
    sam is an integer that specifies an access mask that describes the desired
     security access for the key.  Default is KEY_READ
    
    The result is a new handle to the specified key
    If the function fails, a WindowsError exception is raised.
    """
    pass

def OpenKeyEx(*args, **kwargs): # real signature unknown
    """ See OpenKey() """
    pass

def QueryInfoKey(key): # real signature unknown; restored from __doc__
    """
    tuple = QueryInfoKey(key) - Returns information about a key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    
    The result is a tuple of 3 items:An integer that identifies the number of sub keys this key has.
    An integer that identifies the number of values this key has.
    A long integer that identifies when the key was last modified (if available)
     as 100's of nanoseconds since Jan 1, 1600.
    """
    pass

def QueryReflectionKey(hkey): # real signature unknown; restored from __doc__
    """
    bool = QueryReflectionKey(hkey) - Determines the reflection state for the specified key.
    Will generally raise NotImplemented if executed on a 32-bit Operating System.
    """
    pass

def QueryValue(key, sub_key): # real signature unknown; restored from __doc__
    """
    string = QueryValue(key, sub_key) - retrieves the unnamed value for a key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    sub_key is a string that holds the name of the subkey with which the value
     is associated.  If this parameter is None or empty, the function retrieves
     the value set by the SetValue() method for the key identified by key.
    Values in the registry have name, type, and data components. This method
    retrieves the data for a key's first value that has a NULL name.
    But the underlying API call doesn't return the type, Lame Lame Lame, DONT USE THIS!!!
    """
    pass

def QueryValueEx(key, value_name): # real signature unknown; restored from __doc__
    """
    value,type_id = QueryValueEx(key, value_name) - Retrieves the type and data for a specified value name associated with an open registry key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    value_name is a string indicating the value to query
    """
    pass

def SaveKey(key, file_name): # real signature unknown; restored from __doc__
    """
    SaveKey(key, file_name) - Saves the specified key, and all its subkeys to the specified file.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    file_name is the name of the file to save registry data to.
     This file cannot already exist. If this filename includes an extension,
     it cannot be used on file allocation table (FAT) file systems by the
     LoadKey(), ReplaceKey() or RestoreKey() methods.
    
    If key represents a key on a remote computer, the path described by
    file_name is relative to the remote computer.
    The caller of this method must possess the SeBackupPrivilege security privilege.
    This function passes NULL for security_attributes to the API.
    """
    pass

def SetValue(key, sub_key, type, value): # real signature unknown; restored from __doc__
    """
    SetValue(key, sub_key, type, value) - Associates a value with a specified key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    sub_key is a string that names the subkey with which the value is associated.
    type is an integer that specifies the type of the data.  Currently this
     must be REG_SZ, meaning only strings are supported.
    value is a string that specifies the new value.
    
    If the key specified by the sub_key parameter does not exist, the SetValue
    function creates it.
    
    Value lengths are limited by available memory. Long values (more than
    2048 bytes) should be stored as files with the filenames stored in 
    the configuration registry.  This helps the registry perform efficiently.
    
    The key identified by the key parameter must have been opened with
    KEY_SET_VALUE access.
    """
    pass

def SetValueEx(key, value_name, reserved, type, value): # real signature unknown; restored from __doc__
    """
    SetValueEx(key, value_name, reserved, type, value) - Stores data in the value field of an open registry key.
    
    key is an already open key, or any one of the predefined HKEY_* constants.
    value_name is a string containing the name of the value to set, or None
    type is an integer that specifies the type of the data.  This should be one of:
      REG_BINARY -- Binary data in any form.
      REG_DWORD -- A 32-bit number.
      REG_DWORD_LITTLE_ENDIAN -- A 32-bit number in little-endian format.
      REG_DWORD_BIG_ENDIAN -- A 32-bit number in big-endian format.
      REG_EXPAND_SZ -- A null-terminated string that contains unexpanded references
                       to environment variables (for example, %PATH%).
      REG_LINK -- A Unicode symbolic link.
      REG_MULTI_SZ -- A sequence of null-terminated strings, terminated by
                      two null characters.  Note that Python handles this
                      termination automatically.
      REG_NONE -- No defined value type.
      REG_RESOURCE_LIST -- A device-driver resource list.
      REG_SZ -- A null-terminated string.
    reserved can be anything - zero is always passed to the API.
    value is a string that specifies the new value.
    
    This method can also set additional value and type information for the
    specified key.  The key identified by the key parameter must have been
    opened with KEY_SET_VALUE access.
    
    To open the key, use the CreateKeyEx() or OpenKeyEx() methods.
    
    Value lengths are limited by available memory. Long values (more than
    2048 bytes) should be stored as files with the filenames stored in 
    the configuration registry.  This helps the registry perform efficiently.
    """
    pass

# classes

class HKEYType(object):
    """
    PyHKEY Object - A Python object, representing a win32 registry key.
    
    This object wraps a Windows HKEY object, automatically closing it when
    the object is destroyed.  To guarantee cleanup, you can call either
    the Close() method on the PyHKEY, or the CloseKey() method.
    
    All functions which accept a handle object also accept an integer - 
    however, use of the handle object is encouraged.
    
    Functions:
    Close() - Closes the underlying handle.
    Detach() - Returns the integer Win32 handle, detaching it from the object
    
    Properties:
    handle - The integer Win32 handle.
    
    Operations:
    __nonzero__ - Handles with an open object return true, otherwise false.
    __int__ - Converting a handle to an integer returns the Win32 handle.
    __cmp__ - Handle objects are compared using the handle value.
    """
    def Close(self): # real signature unknown; restored from __doc__
        """
        key.Close() - Closes the underlying Windows handle.
        
        If the handle is already closed, no error is raised.
        """
        pass

    def Detach(self): # real signature unknown; restored from __doc__
        """
        int = key.Detach() - Detaches the Windows handle from the handle object.
        
        The result is the value of the handle before it is detached.  If the
        handle is already detached, this will return zero.
        
        After calling this function, the handle is effectively invalidated,
        but the handle is not closed.  You would call this function when you
        need the underlying win32 handle to exist beyond the lifetime of the
        handle object.
        On 64 bit windows, the result of this function is a long integer
        """
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

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __hex__(self): # real signature unknown; restored from __doc__
        """ x.__hex__() <==> hex(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass

    handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



