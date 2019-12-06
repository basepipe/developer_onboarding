# encoding: utf-8
# module PySide.QtScript
# from C:\Python27\lib\site-packages\PySide\QtScript.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QScriptable(__Shiboken.Object):
    # no doc
    def argument(self, *args, **kwargs): # real signature unknown
        pass

    def argumentCount(self, *args, **kwargs): # real signature unknown
        pass

    def context(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def thisObject(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QScriptClass(__Shiboken.Object):
    # no doc
    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def newIterator(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyFlags(self, *args, **kwargs): # real signature unknown
        pass

    def prototype(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def supportsExtension(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Callable = PySide.QtScript.QScriptClass.Extension.Callable
    Extension = None # (!) real value is "<type 'PySide.QtScript.QScriptClass.Extension'>"
    HandlesReadAccess = PySide.QtScript.QScriptClass.QueryFlag.HandlesReadAccess
    HandlesWriteAccess = PySide.QtScript.QScriptClass.QueryFlag.HandlesWriteAccess
    HasInstance = PySide.QtScript.QScriptClass.Extension.HasInstance
    QueryFlag = None # (!) real value is "<type 'PySide.QtScript.QScriptClass.QueryFlag'>"


class QScriptClassPropertyIterator(__Shiboken.Object):
    # no doc
    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def hasNext(self, *args, **kwargs): # real signature unknown
        pass

    def hasPrevious(self, *args, **kwargs): # real signature unknown
        pass

    def id(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def object(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def toBack(self, *args, **kwargs): # real signature unknown
        pass

    def toFront(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QScriptContext(__Shiboken.Object):
    # no doc
    def activationObject(self, *args, **kwargs): # real signature unknown
        pass

    def argument(self, *args, **kwargs): # real signature unknown
        pass

    def argumentCount(self, *args, **kwargs): # real signature unknown
        pass

    def argumentsObject(self, *args, **kwargs): # real signature unknown
        pass

    def backtrace(self, *args, **kwargs): # real signature unknown
        pass

    def callee(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def isCalledAsConstructor(self, *args, **kwargs): # real signature unknown
        pass

    def parentContext(self, *args, **kwargs): # real signature unknown
        pass

    def popScope(self, *args, **kwargs): # real signature unknown
        pass

    def pushScope(self, *args, **kwargs): # real signature unknown
        pass

    def returnValue(self, *args, **kwargs): # real signature unknown
        pass

    def scopeChain(self, *args, **kwargs): # real signature unknown
        pass

    def setActivationObject(self, *args, **kwargs): # real signature unknown
        pass

    def setReturnValue(self, *args, **kwargs): # real signature unknown
        pass

    def setThisObject(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def thisObject(self, *args, **kwargs): # real signature unknown
        pass

    def throwError(self, *args, **kwargs): # real signature unknown
        pass

    def throwValue(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Error = None # (!) real value is "<type 'PySide.QtScript.QScriptContext.Error'>"
    ExceptionState = PySide.QtScript.QScriptContext.ExecutionState.ExceptionState
    ExecutionState = None # (!) real value is "<type 'PySide.QtScript.QScriptContext.ExecutionState'>"
    NormalState = PySide.QtScript.QScriptContext.ExecutionState.NormalState
    RangeError = PySide.QtScript.QScriptContext.Error.RangeError
    ReferenceError = PySide.QtScript.QScriptContext.Error.ReferenceError
    SyntaxError = PySide.QtScript.QScriptContext.Error.SyntaxError
    TypeError = PySide.QtScript.QScriptContext.Error.TypeError
    UnknownError = PySide.QtScript.QScriptContext.Error.UnknownError
    URIError = PySide.QtScript.QScriptContext.Error.URIError


class QScriptContextInfo(__Shiboken.Object):
    # no doc
    def columnNumber(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def functionEndLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def functionMetaIndex(self, *args, **kwargs): # real signature unknown
        pass

    def functionName(self, *args, **kwargs): # real signature unknown
        pass

    def functionParameterNames(self, *args, **kwargs): # real signature unknown
        pass

    def functionStartLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def functionType(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def lineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def scriptId(self, *args, **kwargs): # real signature unknown
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

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
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

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    FunctionType = None # (!) real value is "<type 'PySide.QtScript.QScriptContextInfo.FunctionType'>"
    NativeFunction = PySide.QtScript.QScriptContextInfo.FunctionType.NativeFunction
    QtFunction = PySide.QtScript.QScriptContextInfo.FunctionType.QtFunction
    QtPropertyFunction = PySide.QtScript.QScriptContextInfo.FunctionType.QtPropertyFunction
    ScriptFunction = PySide.QtScript.QScriptContextInfo.FunctionType.ScriptFunction


class QScriptEngine(__PySide_QtCore.QObject):
    # no doc
    def abortEvaluation(self, *args, **kwargs): # real signature unknown
        pass

    def agent(self, *args, **kwargs): # real signature unknown
        pass

    def availableExtensions(self, *args, **kwargs): # real signature unknown
        pass

    def canEvaluate(self, *args, **kwargs): # real signature unknown
        pass

    def clearExceptions(self, *args, **kwargs): # real signature unknown
        pass

    def collectGarbage(self, *args, **kwargs): # real signature unknown
        pass

    def currentContext(self, *args, **kwargs): # real signature unknown
        pass

    def defaultPrototype(self, *args, **kwargs): # real signature unknown
        pass

    def evaluate(self, *args, **kwargs): # real signature unknown
        pass

    def globalObject(self, *args, **kwargs): # real signature unknown
        pass

    def hasUncaughtException(self, *args, **kwargs): # real signature unknown
        pass

    def importedExtensions(self, *args, **kwargs): # real signature unknown
        pass

    def importExtension(self, *args, **kwargs): # real signature unknown
        pass

    def installTranslatorFunctions(self, *args, **kwargs): # real signature unknown
        pass

    def isEvaluating(self, *args, **kwargs): # real signature unknown
        pass

    def newActivationObject(self, *args, **kwargs): # real signature unknown
        pass

    def newArray(self, *args, **kwargs): # real signature unknown
        pass

    def newDate(self, *args, **kwargs): # real signature unknown
        pass

    def newObject(self, *args, **kwargs): # real signature unknown
        pass

    def newQMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def newQObject(self, *args, **kwargs): # real signature unknown
        pass

    def newRegExp(self, *args, **kwargs): # real signature unknown
        pass

    def newVariant(self, *args, **kwargs): # real signature unknown
        pass

    def nullValue(self, *args, **kwargs): # real signature unknown
        pass

    def objectById(self, *args, **kwargs): # real signature unknown
        pass

    def popContext(self, *args, **kwargs): # real signature unknown
        pass

    def processEventsInterval(self, *args, **kwargs): # real signature unknown
        pass

    def pushContext(self, *args, **kwargs): # real signature unknown
        pass

    def reportAdditionalMemoryCost(self, *args, **kwargs): # real signature unknown
        pass

    def setAgent(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultPrototype(self, *args, **kwargs): # real signature unknown
        pass

    def setGlobalObject(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessEventsInterval(self, *args, **kwargs): # real signature unknown
        pass

    def signalHandlerException(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def toObject(self, *args, **kwargs): # real signature unknown
        pass

    def toStringHandle(self, *args, **kwargs): # real signature unknown
        pass

    def uncaughtException(self, *args, **kwargs): # real signature unknown
        pass

    def uncaughtExceptionBacktrace(self, *args, **kwargs): # real signature unknown
        pass

    def uncaughtExceptionLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def undefinedValue(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AutoCreateDynamicProperties = PySide.QtScript.QScriptEngine.QObjectWrapOption.AutoCreateDynamicProperties
    AutoOwnership = PySide.QtScript.QScriptEngine.ValueOwnership.AutoOwnership
    ExcludeChildObjects = PySide.QtScript.QScriptEngine.QObjectWrapOption.ExcludeChildObjects
    ExcludeDeleteLater = PySide.QtScript.QScriptEngine.QObjectWrapOption.ExcludeDeleteLater
    ExcludeSlots = PySide.QtScript.QScriptEngine.QObjectWrapOption.ExcludeSlots
    ExcludeSuperClassContents = PySide.QtScript.QScriptEngine.QObjectWrapOption.ExcludeSuperClassContents
    ExcludeSuperClassMethods = PySide.QtScript.QScriptEngine.QObjectWrapOption.ExcludeSuperClassMethods
    ExcludeSuperClassProperties = PySide.QtScript.QScriptEngine.QObjectWrapOption.ExcludeSuperClassProperties
    PreferExistingWrapperObject = PySide.QtScript.QScriptEngine.QObjectWrapOption.PreferExistingWrapperObject
    QObjectWrapOption = None # (!) real value is "<type 'PySide.QtScript.QScriptEngine.QObjectWrapOption'>"
    QObjectWrapOptions = None # (!) real value is "<type 'QObjectWrapOptions'>"
    QtOwnership = PySide.QtScript.QScriptEngine.ValueOwnership.QtOwnership
    ScriptOwnership = PySide.QtScript.QScriptEngine.ValueOwnership.ScriptOwnership
    SkipMethodsInEnumeration = PySide.QtScript.QScriptEngine.QObjectWrapOption.SkipMethodsInEnumeration
    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003E576C8>'
    ValueOwnership = None # (!) real value is "<type 'PySide.QtScript.QScriptEngine.ValueOwnership'>"


class QScriptEngineAgent(__Shiboken.Object):
    # no doc
    def contextPop(self, *args, **kwargs): # real signature unknown
        pass

    def contextPush(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def exceptionCatch(self, *args, **kwargs): # real signature unknown
        pass

    def exceptionThrow(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, *args, **kwargs): # real signature unknown
        pass

    def functionEntry(self, *args, **kwargs): # real signature unknown
        pass

    def functionExit(self, *args, **kwargs): # real signature unknown
        pass

    def positionChange(self, *args, **kwargs): # real signature unknown
        pass

    def scriptLoad(self, *args, **kwargs): # real signature unknown
        pass

    def scriptUnload(self, *args, **kwargs): # real signature unknown
        pass

    def supportsExtension(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    DebuggerInvocationRequest = PySide.QtScript.QScriptEngineAgent.Extension.DebuggerInvocationRequest
    Extension = None # (!) real value is "<type 'PySide.QtScript.QScriptEngineAgent.Extension'>"


class QScriptExtensionInterface(__PySide_QtCore.QFactoryInterface):
    # no doc
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QScriptExtensionPlugin(__PySide_QtCore.QObject, QScriptExtensionInterface):
    # no doc
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def setupPackage(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x0000000003E57888>'


class QScriptProgram(__Shiboken.Object):
    # no doc
    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def firstLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def sourceCode(self, *args, **kwargs): # real signature unknown
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


class QScriptString(__Shiboken.Object):
    # no doc
    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def toArrayIndex(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
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


class QScriptValue(__Shiboken.Object):
    # no doc
    def call(self, *args, **kwargs): # real signature unknown
        pass

    def construct(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def instanceOf(self, *args, **kwargs): # real signature unknown
        pass

    def isArray(self, *args, **kwargs): # real signature unknown
        pass

    def isBool(self, *args, **kwargs): # real signature unknown
        pass

    def isBoolean(self, *args, **kwargs): # real signature unknown
        pass

    def isDate(self, *args, **kwargs): # real signature unknown
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        pass

    def isFunction(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isNumber(self, *args, **kwargs): # real signature unknown
        pass

    def isObject(self, *args, **kwargs): # real signature unknown
        pass

    def isQMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def isQObject(self, *args, **kwargs): # real signature unknown
        pass

    def isRegExp(self, *args, **kwargs): # real signature unknown
        pass

    def isString(self, *args, **kwargs): # real signature unknown
        pass

    def isUndefined(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def isVariant(self, *args, **kwargs): # real signature unknown
        pass

    def lessThan(self, *args, **kwargs): # real signature unknown
        pass

    def objectId(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyFlags(self, *args, **kwargs): # real signature unknown
        pass

    def prototype(self, *args, **kwargs): # real signature unknown
        pass

    def scope(self, *args, **kwargs): # real signature unknown
        pass

    def scriptClass(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setPrototype(self, *args, **kwargs): # real signature unknown
        pass

    def setScope(self, *args, **kwargs): # real signature unknown
        pass

    def setScriptClass(self, *args, **kwargs): # real signature unknown
        pass

    def strictlyEquals(self, *args, **kwargs): # real signature unknown
        pass

    def toBool(self, *args, **kwargs): # real signature unknown
        pass

    def toBoolean(self, *args, **kwargs): # real signature unknown
        pass

    def toDateTime(self, *args, **kwargs): # real signature unknown
        pass

    def toInt32(self, *args, **kwargs): # real signature unknown
        pass

    def toInteger(self, *args, **kwargs): # real signature unknown
        pass

    def toNumber(self, *args, **kwargs): # real signature unknown
        pass

    def toObject(self, *args, **kwargs): # real signature unknown
        pass

    def toQMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def toQObject(self, *args, **kwargs): # real signature unknown
        pass

    def toRegExp(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def toUInt16(self, *args, **kwargs): # real signature unknown
        pass

    def toUInt32(self, *args, **kwargs): # real signature unknown
        pass

    def toVariant(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
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

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    KeepExistingFlags = PySide.QtScript.QScriptValue.PropertyFlag.KeepExistingFlags
    NullValue = PySide.QtScript.QScriptValue.SpecialValue.NullValue
    PropertyFlag = None # (!) real value is "<type 'PySide.QtScript.QScriptValue.PropertyFlag'>"
    PropertyFlags = None # (!) real value is "<type 'PropertyFlags'>"
    PropertyGetter = PySide.QtScript.QScriptValue.PropertyFlag.PropertyGetter
    PropertySetter = PySide.QtScript.QScriptValue.PropertyFlag.PropertySetter
    QObjectMember = PySide.QtScript.QScriptValue.PropertyFlag.QObjectMember
    ReadOnly = PySide.QtScript.QScriptValue.PropertyFlag.ReadOnly
    ResolveFlag = None # (!) real value is "<type 'PySide.QtScript.QScriptValue.ResolveFlag'>"
    ResolveFlags = None # (!) real value is "<type 'ResolveFlags'>"
    ResolveFull = PySide.QtScript.QScriptValue.ResolveFlag.ResolveFull
    ResolveLocal = PySide.QtScript.QScriptValue.ResolveFlag.ResolveLocal
    ResolvePrototype = PySide.QtScript.QScriptValue.ResolveFlag.ResolvePrototype
    ResolveScope = PySide.QtScript.QScriptValue.ResolveFlag.ResolveScope
    SkipInEnumeration = PySide.QtScript.QScriptValue.PropertyFlag.SkipInEnumeration
    SpecialValue = None # (!) real value is "<type 'PySide.QtScript.QScriptValue.SpecialValue'>"
    UndefinedValue = PySide.QtScript.QScriptValue.SpecialValue.UndefinedValue
    Undeletable = PySide.QtScript.QScriptValue.PropertyFlag.Undeletable
    UserRange = PySide.QtScript.QScriptValue.PropertyFlag.UserRange


class QScriptValueIterator(__Shiboken.Object):
    # no doc
    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def hasNext(self, *args, **kwargs): # real signature unknown
        pass

    def hasPrevious(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def scriptName(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def toBack(self, *args, **kwargs): # real signature unknown
        pass

    def toFront(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
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


