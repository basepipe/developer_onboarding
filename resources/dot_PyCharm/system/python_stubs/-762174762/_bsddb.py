# encoding: utf-8
# module _bsddb
# from (pre-generated)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

cvsid = '$Id$'

DB_AFTER = 1
DB_AGGRESSIVE = 1
DB_APPEND = 2

DB_ARCH_ABS = 1
DB_ARCH_DATA = 2
DB_ARCH_LOG = 4
DB_ARCH_REMOVE = 8

DB_AUTO_COMMIT = 256

DB_BEFORE = 3
DB_BTREE = 1

DB_BUFFER_SMALL = -30999

DB_CDB_ALLDB = 4

DB_CHKSUM = 4
DB_CONSUME = 4

DB_CONSUME_WAIT = 5

DB_CREATE = 1
DB_CURRENT = 6

DB_DIRECT_DB = 64

DB_DIRTY_READ = 512

DB_DONOTINDEX = -30998

DB_DSYNC_DB = 128

DB_DUP = 8
DB_DUPSORT = 2

DB_EID_BROADCAST = -1
DB_EID_INVALID = -2

DB_ENCRYPT = 1

DB_ENCRYPT_AES = 1

DB_EVENT_PANIC = 1

DB_EVENT_REP_CLIENT = 2
DB_EVENT_REP_ELECTED = 3
DB_EVENT_REP_MASTER = 4
DB_EVENT_REP_NEWMASTER = 5

DB_EVENT_REP_PERM_FAILED = 6

DB_EVENT_REP_STARTUPDONE = 7

DB_EVENT_WRITE_FAILED = 8

DB_EXCL = 1024
DB_EXTENT = 4

DB_FAST_STAT = 1

DB_FCNTL_LOCKING = 4096

DB_FIRST = 7
DB_FLUSH = 1
DB_FORCE = 1

DB_FOREIGN_ABORT = 1
DB_FOREIGN_CASCADE = 2
DB_FOREIGN_NULLIFY = 4

DB_FREELIST_ONLY = 1

DB_FREE_SPACE = 2

DB_GET_BOTH = 8

DB_GET_BOTH_RANGE = 10

DB_GET_RECNO = 11

DB_GID_SIZE = 128

DB_HASH = 2

DB_IGNORE_LEASE = 4096

DB_IMMUTABLE_KEY = 2

DB_INIT_CDB = 32
DB_INIT_LOCK = 64
DB_INIT_LOG = 128
DB_INIT_MPOOL = 256
DB_INIT_REP = 512
DB_INIT_TXN = 1024

DB_INORDER = 16
DB_JOINENV = 0

DB_JOIN_ITEM = 12
DB_JOIN_NOSORT = 1

DB_KEYEMPTY = -30996
DB_KEYEXIST = -30995
DB_KEYFIRST = 13
DB_KEYLAST = 14
DB_LAST = 15
DB_LOCKDOWN = 2048

DB_LOCK_CONFLICT = 0
DB_LOCK_DEADLOCK = -30994
DB_LOCK_DEFAULT = 1
DB_LOCK_DUMP = 0
DB_LOCK_EXPIRE = 2
DB_LOCK_GET = 1
DB_LOCK_INHERIT = 3
DB_LOCK_IREAD = 5
DB_LOCK_IWR = 6
DB_LOCK_IWRITE = 4
DB_LOCK_MAXLOCKS = 3
DB_LOCK_MAXWRITE = 4
DB_LOCK_MINLOCKS = 5
DB_LOCK_MINWRITE = 6
DB_LOCK_NG = 0
DB_LOCK_NORUN = 0
DB_LOCK_NOTGRANTED = -30993
DB_LOCK_NOWAIT = 1
DB_LOCK_OLDEST = 7
DB_LOCK_PUT = 4

DB_LOCK_PUT_ALL = 5
DB_LOCK_PUT_OBJ = 6

DB_LOCK_RANDOM = 8
DB_LOCK_READ = 1

DB_LOCK_READ_UNCOMMITTED = 7

DB_LOCK_RECORD = 2
DB_LOCK_SWITCH = 8
DB_LOCK_UPGRADE = 16

DB_LOCK_UPGRADE_WRITE = 10

DB_LOCK_WAIT = 3
DB_LOCK_WRITE = 2
DB_LOCK_WWRITE = 8
DB_LOCK_YOUNGEST = 9

DB_LOG_AUTO_REMOVE = 4

DB_LOG_DIRECT = 1
DB_LOG_DSYNC = 2

DB_LOG_IN_MEMORY = 8

DB_LOG_ZERO = 16

DB_LSTAT_ABORTED = 1
DB_LSTAT_FREE = 3
DB_LSTAT_HELD = 4
DB_LSTAT_PENDING = 5
DB_LSTAT_WAITING = 6

DB_MAX_PAGES = -1
DB_MAX_RECORDS = -1

DB_MULTIPLE = 8192

DB_MULTIPLE_KEY = 256

DB_MULTIVERSION = 8
DB_NEXT = 16

DB_NEXT_DUP = 17
DB_NEXT_NODUP = 18

DB_NODUPDATA = 19
DB_NOLOCKING = 512
DB_NOMMAP = 16
DB_NOORDERCHK = 2
DB_NOOVERWRITE = 20
DB_NOPANIC = 1024
DB_NOSERVER = -30991

DB_NOSERVER_HOME = -30990
DB_NOSERVER_ID = -30989

DB_NOSYNC = 21
DB_NOTFOUND = -30988
DB_ODDFILESIZE = 64

DB_OLD_VERSION = -30987

DB_OPFLAGS_MASK = 255

DB_ORDERCHKONLY = 4
DB_OVERWRITE = 4096

DB_PAGE_NOTFOUND = -30986

DB_PANIC_ENVIRONMENT = 8192

DB_POSITION = 22
DB_PREV = 23

DB_PREV_DUP = 24
DB_PREV_NODUP = 25

DB_PRINTABLE = 8

DB_PRIORITY_DEFAULT = 3
DB_PRIORITY_HIGH = 4
DB_PRIORITY_LOW = 2
DB_PRIORITY_UNCHANGED = 0

DB_PRIORITY_VERY_HIGH = 5
DB_PRIORITY_VERY_LOW = 1

DB_PRIVATE = 4096

DB_PR_PAGE = 16
DB_PR_RECOVERYTEST = 32

DB_QUEUE = 4
DB_RDONLY = 128
DB_RDWRMASTER = 16384

DB_READ_COMMITTED = 1024
DB_READ_UNCOMMITTED = 512

DB_RECNO = 3
DB_RECNUM = 32
DB_RECOVER = 16

DB_RECOVER_FATAL = 8192

DB_REGION_INIT = 16384

DB_REGISTER = 16384
DB_RENUMBER = 64

DB_REPMGR_ACKS_ALL = 1

DB_REPMGR_ACKS_ALL_PEERS = 2

DB_REPMGR_ACKS_NONE = 3
DB_REPMGR_ACKS_ONE = 4

DB_REPMGR_ACKS_ONE_PEER = 5

DB_REPMGR_ACKS_QUORUM = 6

DB_REPMGR_CONF_2SITE_STRICT = 1

DB_REPMGR_CONNECTED = 1
DB_REPMGR_DISCONNECTED = 2
DB_REPMGR_PEER = 1

DB_REP_ACK_TIMEOUT = 1

DB_REP_ANYWHERE = 1

DB_REP_CHECKPOINT_DELAY = 2

DB_REP_CLIENT = 1

DB_REP_CONF_BULK = 2
DB_REP_CONF_DELAYCLIENT = 4
DB_REP_CONF_LEASE = 8
DB_REP_CONF_NOAUTOINIT = 16
DB_REP_CONF_NOWAIT = 32

DB_REP_CONNECTION_RETRY = 3

DB_REP_DUPMASTER = -30985
DB_REP_ELECTION = 4

DB_REP_ELECTION_RETRY = 4
DB_REP_ELECTION_TIMEOUT = 5

DB_REP_FULL_ELECTION_TIMEOUT = 6

DB_REP_HEARTBEAT_MONITOR = 7
DB_REP_HEARTBEAT_SEND = 8

DB_REP_HOLDELECTION = -30983
DB_REP_IGNORE = -30982
DB_REP_ISPERM = -30981

DB_REP_JOIN_FAILURE = -30980

DB_REP_LEASE_EXPIRED = -30979
DB_REP_LEASE_TIMEOUT = 9

DB_REP_MASTER = 2
DB_REP_NEWSITE = -30977
DB_REP_NOBUFFER = 2
DB_REP_NOTPERM = -30976
DB_REP_PERMANENT = 4
DB_REP_REREQUEST = 8

DB_REVSPLITOFF = 128
DB_RMW = 2048
DB_RPCCLIENT = 1
DB_RUNRECOVERY = -30974
DB_SALVAGE = 64

DB_SECONDARY_BAD = -30973

DB_SEQ_DEC = 1
DB_SEQ_INC = 2
DB_SEQ_WRAP = 8

DB_SET = 26

DB_SET_LOCK_TIMEOUT = 2

DB_SET_RANGE = 27
DB_SET_RECNO = 28

DB_SET_TXN_TIMEOUT = 1

DB_SNAPSHOT = 256

DB_STAT_ALL = 2
DB_STAT_CLEAR = 1

DB_STAT_LOCK_CONF = 4
DB_STAT_LOCK_LOCKERS = 8
DB_STAT_LOCK_OBJECTS = 16
DB_STAT_LOCK_PARAMS = 32

DB_STAT_MEMP_HASH = 4

DB_STAT_SUBSYSTEM = 4

DB_SYSTEM_MEM = 32768

DB_THREAD = 4
DB_TIMEOUT = -30888

DB_TIME_NOTGRANTED = 32768

DB_TRUNCATE = 32768

DB_TXN_NOSYNC = 1

DB_TXN_NOT_DURABLE = 512

DB_TXN_NOWAIT = 2
DB_TXN_SNAPSHOT = 2048
DB_TXN_SYNC = 4
DB_TXN_WAIT = 8

DB_TXN_WRITE_NOSYNC = 32

DB_UNKNOWN = 5
DB_UPGRADE = 1

DB_USE_ENVIRON = 2

DB_USE_ENVIRON_ROOT = 8

DB_VERB_DEADLOCK = 1
DB_VERB_FILEOPS = 2

DB_VERB_FILEOPS_ALL = 4

DB_VERB_RECOVERY = 8
DB_VERB_REGISTER = 16
DB_VERB_REPLICATION = 32

DB_VERB_REPMGR_CONNFAIL = 64
DB_VERB_REPMGR_MISC = 128

DB_VERB_REP_ELECT = 256
DB_VERB_REP_LEASE = 512
DB_VERB_REP_MISC = 1024
DB_VERB_REP_MSGS = 2048
DB_VERB_REP_SYNC = 4096

DB_VERB_WAITSFOR = 8192

DB_VERIFY = 2

DB_VERIFY_BAD = -30972

DB_VERSION_MAJOR = 4
DB_VERSION_MINOR = 7
DB_VERSION_PATCH = 25
DB_VERSION_STRING = 'Berkeley DB 4.7.25: (May 15, 2008)'

DB_WRITECURSOR = 30

DB_XA_CREATE = 2048

DB_XIDDATASIZE = 128
DB_YIELDCPU = 65536

EACCES = 13
EAGAIN = 11

EBUSY = 16

EEXIST = 17

EINVAL = 22

ENOENT = 2
ENOMEM = 12
ENOSPC = 28

EPERM = 1

__version__ = '5.3.0'

# functions

def DB(*args, **kwargs): # real signature unknown
    pass

def DBEnv(*args, **kwargs): # real signature unknown
    pass

def DBSequence(*args, **kwargs): # real signature unknown
    pass

def version(*args, **kwargs): # real signature unknown
    """
    Returns a tuple of major, minor, and patch release numbers of the
    underlying DB library.
    """
    pass

# classes

class DBError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DBAccessError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBAgainError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBBusyError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBCursorClosedError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBFileExistsError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBForeignConflictError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBInvalidArgError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBKeyEmptyError(DBError, KeyError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBKeyExistError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBLockDeadlockError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBLockNotGrantedError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBNoMemoryError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBNoServerError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBNoServerHomeError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBNoServerIDError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBNoSpaceError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBNoSuchFileError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBNotFoundError(DBError, KeyError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBOldVersionError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBPageNotFoundError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBPermissionsError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBRepHandleDeadError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBRepLeaseExpiredError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBRepLockoutError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBRepUnavailError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBRunRecoveryError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBSecondaryBadError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DBVerifyBadError(DBError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

api = None # (!) real value is '<capsule object "_bsddb.api" at 0x0000000001AC1C90>'

