# encoding: utf-8
# module zipimport
# from (built-in)
# by generator 1.147
"""
zipimport provides support for importing Python modules from Zip archives.

This module exports three objects:
- zipimporter: a class; its constructor takes a path to a Zip archive.
- ZipImportError: exception raised by zipimporter objects. It's a
  subclass of ImportError, so it can be caught as ImportError, too.
- _zip_directory_cache: a dict, mapping archive paths to zip directory
  info dicts, as used in zipimporter._files.

It is usually not needed to use the zipimport module explicitly; it is
used by the builtin import mechanism for sys.path items that are paths
to Zip archives.
"""
# no imports

# no functions
# classes

class zipimporter(object):
    """
    zipimporter(archivepath) -> zipimporter object
    
    Create a new zipimporter instance. 'archivepath' must be a path to
    a zipfile, or to a specific path inside a zipfile. For example, it can be
    '/tmp/myimport.zip', or '/tmp/myimport.zip/mydirectory', if mydirectory is a
    valid directory inside the archive.
    
    'ZipImportError is raised if 'archivepath' doesn't point to a valid Zip
    archive.
    
    The 'archive' attribute of zipimporter objects contains the name of the
    zipfile targeted.
    """
    def find_module(self, fullname, path=None): # real signature unknown; restored from __doc__
        """
        find_module(fullname, path=None) -> self or None.
        
        Search for a module specified by 'fullname'. 'fullname' must be the
        fully qualified (dotted) module name. It returns the zipimporter
        instance itself if the module was found, or None if it wasn't.
        The optional 'path' argument is ignored -- it's there for compatibility
        with the importer protocol.
        """
        return self

    def get_code(self, fullname): # real signature unknown; restored from __doc__
        """
        get_code(fullname) -> code object.
        
        Return the code object for the specified module. Raise ZipImportError
        if the module couldn't be found.
        """
        pass

    def get_data(self, pathname): # real signature unknown; restored from __doc__
        """
        get_data(pathname) -> string with file data.
        
        Return the data associated with 'pathname'. Raise IOError if
        the file wasn't found.
        """
        return ""

    def get_filename(self, fullname): # real signature unknown; restored from __doc__
        """
        get_filename(fullname) -> filename string.
        
        Return the filename for the specified module.
        """
        pass

    def get_source(self, fullname): # real signature unknown; restored from __doc__
        """
        get_source(fullname) -> source string.
        
        Return the source code for the specified module. Raise ZipImportError
        if the module couldn't be found, return None if the archive does
        contain the module, but has no source for it.
        """
        pass

    def is_package(self, fullname): # real signature unknown; restored from __doc__
        """
        is_package(fullname) -> bool.
        
        Return True if the module specified by fullname is a package.
        Raise ZipImportError if the module couldn't be found.
        """
        pass

    def load_module(self, fullname): # real signature unknown; restored from __doc__
        """
        load_module(fullname) -> module.
        
        Load the module specified by 'fullname'. 'fullname' must be the
        fully qualified (dotted) module name. It returns the imported
        module, or raises ZipImportError if it wasn't found.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, archivepath): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    archive = property(lambda self: '')
    """:type: string"""

    prefix = property(lambda self: '')
    """:type: string"""

    _files = property(lambda self: {})
    """:type: dict"""



class ZipImportError(ImportError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

_zip_directory_cache = {} # real value of type <type 'dict'> skipped

