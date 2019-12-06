# encoding: utf-8
# module win32wnet
# from C:\Python27\lib\site-packages\win32\win32wnet.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# functions

def NCBBuffer(*args, **kwargs): # real signature unknown
    """ Creates a memory buffer """
    pass

def Netbios(*args, **kwargs): # real signature unknown
    """ Calls the windows Netbios function """
    pass

def WNetAddConnection2(NetResource, Password, UserName, Flags): # real signature unknown; restored from __doc__
    """ WNetAddConnection2(NetResource, Password, UserName, Flags) """
    pass

def WNetAddConnection3(HwndParent, NetResource, Password, UserName, Flags): # real signature unknown; restored from __doc__
    """ WNetAddConnection3(HwndParent, NetResource, Password, UserName, Flags) """
    pass

def WNetCancelConnection2(*args, **kwargs): # real signature unknown
    """ localname,dwflags,bforce """
    pass

def WNetCloseEnum(*args, **kwargs): # real signature unknown
    """ PyHANDLE from WNetOpenEnum() """
    pass

def WNetEnumResource(*args, **kwargs): # real signature unknown
    """ Enum """
    pass

def WNetGetConnection(*args, **kwargs): # real signature unknown
    """ Retrieves the name of the network resource associated with a local device """
    pass

def WNetGetLastError(*args, **kwargs): # real signature unknown
    """ Retrieves extended error information set by a network provider when one of the WNet* functions fails """
    pass

def WNetGetResourceInformation(*args, **kwargs): # real signature unknown
    """ Finds the type and provider of a network resource """
    pass

def WNetGetResourceParent(*args, **kwargs): # real signature unknown
    """ Finds the parent resource of a network resource """
    pass

def WNetGetUniversalName(*args, **kwargs): # real signature unknown
    """ localPath, infoLevel=UNIVERSAL_NAME_INFO_LEVEL """
    pass

def WNetGetUser(*args, **kwargs): # real signature unknown
    """ connectionName=None """
    pass

def WNetOpenEnum(*args, **kwargs): # real signature unknown
    """ dwScope,dwType,dwUsage,NETRESOURCE - returns PyHANDLE """
    pass

# classes

class NCBType(object):
    # no doc
    def Reset(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    Bufflen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Callname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Cmd_cplt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Lana_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Lsn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Post = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Retcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Rto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Sto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



NCB = NCBType


class NETRESOURCEType(object):
    # no doc
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
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

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    dwDisplayType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dwUsage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lpComment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lpLocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lpProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lpRemoteName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



NETRESOURCE = NETRESOURCEType


