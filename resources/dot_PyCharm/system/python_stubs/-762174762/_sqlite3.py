# encoding: utf-8
# module _sqlite3
# from (pre-generated)
# by generator 1.147
# no doc

# imports
import sqlite3 as __sqlite3


# Variables with simple values

PARSE_COLNAMES = 2
PARSE_DECLTYPES = 1

SQLITE_ALTER_TABLE = 26

SQLITE_ANALYZE = 28
SQLITE_ATTACH = 24

SQLITE_CREATE_INDEX = 1
SQLITE_CREATE_TABLE = 2

SQLITE_CREATE_TEMP_INDEX = 3
SQLITE_CREATE_TEMP_TABLE = 4
SQLITE_CREATE_TEMP_TRIGGER = 5
SQLITE_CREATE_TEMP_VIEW = 6

SQLITE_CREATE_TRIGGER = 7
SQLITE_CREATE_VIEW = 8

SQLITE_DELETE = 9
SQLITE_DENY = 1
SQLITE_DETACH = 25

SQLITE_DROP_INDEX = 10
SQLITE_DROP_TABLE = 11

SQLITE_DROP_TEMP_INDEX = 12
SQLITE_DROP_TEMP_TABLE = 13
SQLITE_DROP_TEMP_TRIGGER = 14
SQLITE_DROP_TEMP_VIEW = 15

SQLITE_DROP_TRIGGER = 16
SQLITE_DROP_VIEW = 17

SQLITE_IGNORE = 2
SQLITE_INSERT = 18
SQLITE_OK = 0
SQLITE_PRAGMA = 19
SQLITE_READ = 20
SQLITE_REINDEX = 27
SQLITE_SELECT = 21
SQLITE_TRANSACTION = 22
SQLITE_UPDATE = 23

sqlite_version = '3.14.2'

version = '2.6.0'

# functions

def adapt(obj, protocol, alternate): # real signature unknown; restored from __doc__
    """ adapt(obj, protocol, alternate) -> adapt obj to given protocol. Non-standard. """
    pass

def complete_statement(sql): # real signature unknown; restored from __doc__
    """
    complete_statement(sql)
    
    Checks if a string contains a complete SQL statement. Non-standard.
    """
    pass

def connect(database, timeout=None, isolation_level=None, detect_types=None, factory=None): # real signature unknown; restored from __doc__
    """
    connect(database[, timeout, isolation_level, detect_types, factory])
    
    Opens a connection to the SQLite database file *database*. You can use
    ":memory:" to open a database connection to a database that resides in
    RAM instead of on disk.
    """
    pass

def enable_callback_tracebacks(flag): # real signature unknown; restored from __doc__
    """
    enable_callback_tracebacks(flag)
    
    Enable or disable callback functions throwing errors to stderr.
    """
    pass

def enable_shared_cache(do_enable): # real signature unknown; restored from __doc__
    """
    enable_shared_cache(do_enable)
    
    Enable or disable shared cache mode for the calling thread.
    Experimental/Non-standard.
    """
    pass

def register_adapter(type, callable): # real signature unknown; restored from __doc__
    """
    register_adapter(type, callable)
    
    Registers an adapter with pysqlite's adapter registry. Non-standard.
    """
    pass

def register_converter(typename, callable): # real signature unknown; restored from __doc__
    """
    register_converter(typename, callable)
    
    Registers a converter with pysqlite. Non-standard.
    """
    pass

# classes

class Cache(object):
    # no doc
    def display(self, *args, **kwargs): # real signature unknown
        """ For debugging only. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """ Gets an entry from the cache or calls the factory function to produce one. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Connection(object):
    """ SQLite database connection object. """
    def close(self, *args, **kwargs): # real signature unknown
        """ Closes the connection. """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """ Commit the current transaction. """
        pass

    def create_aggregate(self, *args, **kwargs): # real signature unknown
        """ Creates a new aggregate. Non-standard. """
        pass

    def create_collation(self, *args, **kwargs): # real signature unknown
        """ Creates a collation function. Non-standard. """
        pass

    def create_function(self, *args, **kwargs): # real signature unknown
        """ Creates a new function. Non-standard. """
        pass

    def cursor(self, *args, **kwargs): # real signature unknown
        """ Return a cursor for the connection. """
        pass

    def enable_load_extension(self, *args, **kwargs): # real signature unknown
        """ Enable dynamic loading of SQLite extension modules. Non-standard. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes a SQL statement. Non-standard. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes a SQL statement. Non-standard. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes a multiple SQL statements at once. Non-standard. """
        pass

    def interrupt(self, *args, **kwargs): # real signature unknown
        """ Abort any pending database operation. Non-standard. """
        pass

    def iterdump(self, *args, **kwargs): # real signature unknown
        """ Returns iterator to the dump of the database in an SQL text format. Non-standard. """
        pass

    def load_extension(self, *args, **kwargs): # real signature unknown
        """ Load SQLite extension module. Non-standard. """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Roll back the current transaction. """
        pass

    def set_authorizer(self, *args, **kwargs): # real signature unknown
        """ Sets authorizer callback. Non-standard. """
        pass

    def set_progress_handler(self, *args, **kwargs): # real signature unknown
        """ Sets progress handler callback. Non-standard. """
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """ For context manager. Non-standard. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """ For context manager. Non-standard. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    DatabaseError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DataError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IntegrityError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InterfaceError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InternalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    isolation_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NotSupportedError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OperationalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProgrammingError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_changes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Warning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Cursor(object):
    """ SQLite database cursor class. """
    def close(self, *args, **kwargs): # real signature unknown
        """ Closes the cursor. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes a SQL statement. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes a SQL statement. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes a multiple SQL statements at once. Non-standard. """
        pass

    def fetchall(self, *args, **kwargs): # real signature unknown
        """ Fetches all rows from the resultset. """
        pass

    def fetchmany(self, *args, **kwargs): # real signature unknown
        """ Fetches several rows from the resultset. """
        pass

    def fetchone(self, *args, **kwargs): # real signature unknown
        """ Fetches one row from the resultset. """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def setinputsizes(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in pysqlite. """
        pass

    def setoutputsize(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in pysqlite. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    arraysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lastrowid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rowcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Error(StandardError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DatabaseError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DataError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class IntegrityError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InternalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NotSupportedError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OperationalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OptimizedUnicode(object):
    # no doc
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    cell_contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PrepareProtocol(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ProgrammingError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Row(object):
    # no doc
    def keys(self, *args, **kwargs): # real signature unknown
        """ Returns the keys of the row. """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
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


class Statement(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Warning(StandardError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

adapters = {
    (
        None, # (!) real value is "<type 'datetime.date'>"
        PrepareProtocol,
    ): 
        None # (!) real value is '<function adapt_date at 0x00000000021017B8>'
    ,
    (
        None, # (!) real value is "<type 'datetime.datetime'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is '<function adapt_datetime at 0x0000000002101828>'
    ,
}

converters = {
    'DATE': None, # (!) real value is '<function convert_date at 0x0000000002101898>'
    'TIMESTAMP': None, # (!) real value is '<function convert_timestamp at 0x0000000002101908>'
}

