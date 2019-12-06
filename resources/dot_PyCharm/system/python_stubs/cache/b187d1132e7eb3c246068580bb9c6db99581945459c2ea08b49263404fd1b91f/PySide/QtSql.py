# encoding: utf-8
# module PySide.QtSql
# from C:\Python27\lib\site-packages\PySide\QtSql.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import PySide.QtGui as __PySide_QtGui
import Shiboken as __Shiboken


# no functions
# classes

class QSql(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AfterLastRow = PySide.QtSql.QSql.Location.AfterLastRow
    AllTables = PySide.QtSql.QSql.TableType.AllTables
    BeforeFirstRow = PySide.QtSql.QSql.Location.BeforeFirstRow
    Binary = PySide.QtSql.QSql.ParamTypeFlag.Binary
    HighPrecision = PySide.QtSql.QSql.NumericalPrecisionPolicy.HighPrecision
    In = PySide.QtSql.QSql.ParamTypeFlag.In
    InOut = PySide.QtSql.QSql.ParamTypeFlag.InOut
    Location = None # (!) real value is "<type 'PySide.QtSql.QSql.Location'>"
    LowPrecisionDouble = PySide.QtSql.QSql.NumericalPrecisionPolicy.LowPrecisionDouble
    LowPrecisionInt32 = PySide.QtSql.QSql.NumericalPrecisionPolicy.LowPrecisionInt32
    LowPrecisionInt64 = PySide.QtSql.QSql.NumericalPrecisionPolicy.LowPrecisionInt64
    NumericalPrecisionPolicy = None # (!) real value is "<type 'PySide.QtSql.QSql.NumericalPrecisionPolicy'>"
    Out = PySide.QtSql.QSql.ParamTypeFlag.Out
    ParamType = None # (!) real value is "<type 'ParamType'>"
    ParamTypeFlag = None # (!) real value is "<type 'PySide.QtSql.QSql.ParamTypeFlag'>"
    SystemTables = PySide.QtSql.QSql.TableType.SystemTables
    Tables = PySide.QtSql.QSql.TableType.Tables
    TableType = None # (!) real value is "<type 'PySide.QtSql.QSql.TableType'>"
    Views = PySide.QtSql.QSql.TableType.Views


class QSqlDatabase(__Shiboken.Object):
    # no doc
    def addDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def cloneDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        pass

    def connectionName(self, *args, **kwargs): # real signature unknown
        pass

    def connectionNames(self, *args, **kwargs): # real signature unknown
        pass

    def connectOptions(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def database(self, *args, **kwargs): # real signature unknown
        pass

    def databaseName(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def driverName(self, *args, **kwargs): # real signature unknown
        pass

    def drivers(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def hostName(self, *args, **kwargs): # real signature unknown
        pass

    def isDriverAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def isOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def password(self, *args, **kwargs): # real signature unknown
        pass

    def port(self, *args, **kwargs): # real signature unknown
        pass

    def primaryIndex(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def registerSqlDriver(self, *args, **kwargs): # real signature unknown
        pass

    def removeDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        pass

    def setConnectOptions(self, *args, **kwargs): # real signature unknown
        pass

    def setDatabaseName(self, *args, **kwargs): # real signature unknown
        pass

    def setHostName(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setPassword(self, *args, **kwargs): # real signature unknown
        pass

    def setPort(self, *args, **kwargs): # real signature unknown
        pass

    def setUserName(self, *args, **kwargs): # real signature unknown
        pass

    def tables(self, *args, **kwargs): # real signature unknown
        pass

    def transaction(self, *args, **kwargs): # real signature unknown
        pass

    def userName(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
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

    defaultConnection = 'qt_sql_default_connection'


class QSqlDriver(__PySide_QtCore.QObject):
    # no doc
    def beginTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commitTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def createResult(self, *args, **kwargs): # real signature unknown
        pass

    def escapeIdentifier(self, *args, **kwargs): # real signature unknown
        pass

    def formatValue(self, *args, **kwargs): # real signature unknown
        pass

    def hasFeature(self, *args, **kwargs): # real signature unknown
        pass

    def isIdentifierEscaped(self, *args, **kwargs): # real signature unknown
        pass

    def isIdentifierEscapedImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def isOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def notification(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def primaryIndex(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def rollbackTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setOpen(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def sqlStatement(self, *args, **kwargs): # real signature unknown
        pass

    def stripDelimiters(self, *args, **kwargs): # real signature unknown
        pass

    def stripDelimitersImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def subscribedToNotifications(self, *args, **kwargs): # real signature unknown
        pass

    def subscribedToNotificationsImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def subscribeToNotification(self, *args, **kwargs): # real signature unknown
        pass

    def subscribeToNotificationImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def tables(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotification(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotificationImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BatchOperations = PySide.QtSql.QSqlDriver.DriverFeature.BatchOperations
    BLOB = PySide.QtSql.QSqlDriver.DriverFeature.BLOB
    DeleteStatement = PySide.QtSql.QSqlDriver.StatementType.DeleteStatement
    DriverFeature = None # (!) real value is "<type 'PySide.QtSql.QSqlDriver.DriverFeature'>"
    EventNotifications = PySide.QtSql.QSqlDriver.DriverFeature.EventNotifications
    FieldName = PySide.QtSql.QSqlDriver.IdentifierType.FieldName
    FinishQuery = PySide.QtSql.QSqlDriver.DriverFeature.FinishQuery
    IdentifierType = None # (!) real value is "<type 'PySide.QtSql.QSqlDriver.IdentifierType'>"
    InsertStatement = PySide.QtSql.QSqlDriver.StatementType.InsertStatement
    LastInsertId = PySide.QtSql.QSqlDriver.DriverFeature.LastInsertId
    LowPrecisionNumbers = PySide.QtSql.QSqlDriver.DriverFeature.LowPrecisionNumbers
    MultipleResultSets = PySide.QtSql.QSqlDriver.DriverFeature.MultipleResultSets
    NamedPlaceholders = PySide.QtSql.QSqlDriver.DriverFeature.NamedPlaceholders
    PositionalPlaceholders = PySide.QtSql.QSqlDriver.DriverFeature.PositionalPlaceholders
    PreparedQueries = PySide.QtSql.QSqlDriver.DriverFeature.PreparedQueries
    QuerySize = PySide.QtSql.QSqlDriver.DriverFeature.QuerySize
    SelectStatement = PySide.QtSql.QSqlDriver.StatementType.SelectStatement
    SimpleLocking = PySide.QtSql.QSqlDriver.DriverFeature.SimpleLocking
    StatementType = None # (!) real value is "<type 'PySide.QtSql.QSqlDriver.StatementType'>"
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000476BB48>'
    TableName = PySide.QtSql.QSqlDriver.IdentifierType.TableName
    Transactions = PySide.QtSql.QSqlDriver.DriverFeature.Transactions
    Unicode = PySide.QtSql.QSqlDriver.DriverFeature.Unicode
    UpdateStatement = PySide.QtSql.QSqlDriver.StatementType.UpdateStatement
    WhereStatement = PySide.QtSql.QSqlDriver.StatementType.WhereStatement


class QSqlDriverCreatorBase(__Shiboken.Object):
    # no doc
    def createObject(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QSqlError(__Shiboken.Object):
    # no doc
    def databaseText(self, *args, **kwargs): # real signature unknown
        pass

    def driverText(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def number(self, *args, **kwargs): # real signature unknown
        pass

    def setDatabaseText(self, *args, **kwargs): # real signature unknown
        pass

    def setDriverText(self, *args, **kwargs): # real signature unknown
        pass

    def setNumber(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
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

    ConnectionError = PySide.QtSql.QSqlError.ErrorType.ConnectionError
    ErrorType = None # (!) real value is "<type 'PySide.QtSql.QSqlError.ErrorType'>"
    NoError = PySide.QtSql.QSqlError.ErrorType.NoError
    StatementError = PySide.QtSql.QSqlError.ErrorType.StatementError
    TransactionError = PySide.QtSql.QSqlError.ErrorType.TransactionError
    UnknownError = PySide.QtSql.QSqlError.ErrorType.UnknownError


class QSqlField(__Shiboken.Object):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def defaultValue(self, *args, **kwargs): # real signature unknown
        pass

    def isAutoValue(self, *args, **kwargs): # real signature unknown
        pass

    def isGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def length(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def precision(self, *args, **kwargs): # real signature unknown
        pass

    def requiredStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoValue(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultValue(self, *args, **kwargs): # real signature unknown
        pass

    def setGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def setLength(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def setPrecision(self, *args, **kwargs): # real signature unknown
        pass

    def setReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setRequired(self, *args, **kwargs): # real signature unknown
        pass

    def setRequiredStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setSqlType(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def typeID(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
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

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    Optional = PySide.QtSql.QSqlField.RequiredStatus.Optional
    Required = PySide.QtSql.QSqlField.RequiredStatus.Required
    RequiredStatus = None # (!) real value is "<type 'PySide.QtSql.QSqlField.RequiredStatus'>"
    Unknown = PySide.QtSql.QSqlField.RequiredStatus.Unknown


class QSqlRecord(__Shiboken.Object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clearValues(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def field(self, *args, **kwargs): # real signature unknown
        pass

    def fieldName(self, *args, **kwargs): # real signature unknown
        pass

    def indexOf(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def isGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        pass

    def setGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def setNull(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
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


class QSqlIndex(QSqlRecord):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def cursorName(self, *args, **kwargs): # real signature unknown
        pass

    def isDescending(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def setCursorName(self, *args, **kwargs): # real signature unknown
        pass

    def setDescending(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QSqlQuery(__Shiboken.Object):
    # no doc
    def addBindValue(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def bindValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValues(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def execBatch(self, *args, **kwargs): # real signature unknown
        pass

    def executedQuery(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def finish(self, *args, **kwargs): # real signature unknown
        pass

    def first(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isSelect(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def last(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def lastInsertId(self, *args, **kwargs): # real signature unknown
        pass

    def lastQuery(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def nextResult(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def numRowsAffected(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def result(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def setForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BatchExecutionMode = None # (!) real value is "<type 'PySide.QtSql.QSqlQuery.BatchExecutionMode'>"
    ValuesAsColumns = PySide.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsColumns
    ValuesAsRows = PySide.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsRows


class QSqlQueryModel(__PySide_QtCore.QAbstractTableModel):
    # no doc
    def canFetchMore(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, *args, **kwargs): # real signature unknown
        pass

    def headerData(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def query(self, *args, **kwargs): # real signature unknown
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, *args, **kwargs): # real signature unknown
        pass

    def setHeaderData(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000047E1548>'


class QSqlRelation(__Shiboken.Object):
    # no doc
    def displayColumn(self, *args, **kwargs): # real signature unknown
        pass

    def indexColumn(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def tableName(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QSqlRelationalDelegate(__PySide_QtGui.QItemDelegate):
    # no doc
    def createEditor(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def setModelData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x000000000476BD08>'


class QSqlTableModel(QSqlQueryModel):
    # no doc
    def beforeDelete(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def beforeInsert(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def beforeUpdate(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def database(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, *args, **kwargs): # real signature unknown
        pass

    def editStrategy(self, *args, **kwargs): # real signature unknown
        pass

    def fieldIndex(self, *args, **kwargs): # real signature unknown
        pass

    def filter(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def headerData(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertRecord(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, *args, **kwargs): # real signature unknown
        pass

    def insertRows(self, *args, **kwargs): # real signature unknown
        pass

    def isDirty(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self, *args, **kwargs): # real signature unknown
        pass

    def primaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def primeInsert(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def removeRows(self, *args, **kwargs): # real signature unknown
        pass

    def revert(self, *args, **kwargs): # real signature unknown
        pass

    def revertAll(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectStatement(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setEditStrategy(self, *args, **kwargs): # real signature unknown
        pass

    def setFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setRecord(self, *args, **kwargs): # real signature unknown
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        pass

    def submit(self, *args, **kwargs): # real signature unknown
        pass

    def submitAll(self, *args, **kwargs): # real signature unknown
        pass

    def tableName(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    EditStrategy = None # (!) real value is "<type 'PySide.QtSql.QSqlTableModel.EditStrategy'>"
    OnFieldChange = PySide.QtSql.QSqlTableModel.EditStrategy.OnFieldChange
    OnManualSubmit = PySide.QtSql.QSqlTableModel.EditStrategy.OnManualSubmit
    OnRowChange = PySide.QtSql.QSqlTableModel.EditStrategy.OnRowChange
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000047E22C8>'


class QSqlRelationalTableModel(QSqlTableModel):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self, *args, **kwargs): # real signature unknown
        pass

    def relation(self, *args, **kwargs): # real signature unknown
        pass

    def relationModel(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectStatement(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setRelation(self, *args, **kwargs): # real signature unknown
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000047E2748>'


class QSqlResult(__Shiboken.Object):
    # no doc
    def addBindValue(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def bindingSyntax(self, *args, **kwargs): # real signature unknown
        pass

    def bindValue(self, *args, **kwargs): # real signature unknown
        pass

    def bindValueType(self, *args, **kwargs): # real signature unknown
        pass

    def boundValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValueCount(self, *args, **kwargs): # real signature unknown
        pass

    def boundValueName(self, *args, **kwargs): # real signature unknown
        pass

    def boundValues(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def detachFromResultSet(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def execBatch(self, *args, **kwargs): # real signature unknown
        pass

    def executedQuery(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def fetch(self, *args, **kwargs): # real signature unknown
        pass

    def fetchFirst(self, *args, **kwargs): # real signature unknown
        pass

    def fetchLast(self, *args, **kwargs): # real signature unknown
        pass

    def fetchNext(self, *args, **kwargs): # real signature unknown
        pass

    def fetchPrevious(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOutValues(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isSelect(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def lastInsertId(self, *args, **kwargs): # real signature unknown
        pass

    def lastQuery(self, *args, **kwargs): # real signature unknown
        pass

    def nextResult(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def numRowsAffected(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def savePrepare(self, *args, **kwargs): # real signature unknown
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        pass

    def setAt(self, *args, **kwargs): # real signature unknown
        pass

    def setForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setSelect(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    BatchOperation = PySide.QtSql.QSqlResult.VirtualHookOperation.BatchOperation
    BindingSyntax = None # (!) real value is "<type 'PySide.QtSql.QSqlResult.BindingSyntax'>"
    DetachFromResultSet = PySide.QtSql.QSqlResult.VirtualHookOperation.DetachFromResultSet
    NamedBinding = PySide.QtSql.QSqlResult.BindingSyntax.NamedBinding
    NextResult = PySide.QtSql.QSqlResult.VirtualHookOperation.NextResult
    PositionalBinding = PySide.QtSql.QSqlResult.BindingSyntax.PositionalBinding
    SetNumericalPrecision = PySide.QtSql.QSqlResult.VirtualHookOperation.SetNumericalPrecision
    VirtualHookOperation = None # (!) real value is "<type 'PySide.QtSql.QSqlResult.VirtualHookOperation'>"


