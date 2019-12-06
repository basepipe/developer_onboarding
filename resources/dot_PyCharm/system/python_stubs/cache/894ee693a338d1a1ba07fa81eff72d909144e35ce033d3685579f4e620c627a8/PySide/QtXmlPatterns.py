# encoding: utf-8
# module PySide.QtXmlPatterns
# from C:\Python27\lib\site-packages\PySide\QtXmlPatterns.pyd
# by generator 1.147
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QAbstractMessageHandler(__PySide_QtCore.QObject):
    # no doc
    def handleMessage(self, *args, **kwargs): # real signature unknown
        pass

    def message(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000031ED9C8>'


class QAbstractUriResolver(__PySide_QtCore.QObject):
    # no doc
    def resolve(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    staticMetaObject = None # (!) real value is '<PySide.QtCore.QMetaObject object at 0x00000000031ED848>'


class QAbstractXmlNodeModel(__Shiboken.Object):
    # no doc
    def attributes(self, *args, **kwargs): # real signature unknown
        pass

    def baseUri(self, *args, **kwargs): # real signature unknown
        pass

    def compareOrder(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def documentUri(self, *args, **kwargs): # real signature unknown
        pass

    def elementById(self, *args, **kwargs): # real signature unknown
        pass

    def isDeepEqual(self, *args, **kwargs): # real signature unknown
        pass

    def kind(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBindings(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceForPrefix(self, *args, **kwargs): # real signature unknown
        pass

    def nextFromSimpleAxis(self, *args, **kwargs): # real signature unknown
        pass

    def nodesByIdref(self, *args, **kwargs): # real signature unknown
        pass

    def root(self, *args, **kwargs): # real signature unknown
        pass

    def sendNamespaces(self, *args, **kwargs): # real signature unknown
        pass

    def sourceLocation(self, *args, **kwargs): # real signature unknown
        pass

    def stringValue(self, *args, **kwargs): # real signature unknown
        pass

    def typedValue(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    FirstChild = PySide.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.FirstChild
    InheritNamespaces = PySide.QtXmlPatterns.QAbstractXmlNodeModel.NodeCopySetting.InheritNamespaces
    NextSibling = PySide.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.NextSibling
    NodeCopySetting = None # (!) real value is "<type 'PySide.QtXmlPatterns.QAbstractXmlNodeModel.NodeCopySetting'>"
    Parent = PySide.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.Parent
    PreserveNamespaces = PySide.QtXmlPatterns.QAbstractXmlNodeModel.NodeCopySetting.PreserveNamespaces
    PreviousSibling = PySide.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.PreviousSibling
    SimpleAxis = None # (!) real value is "<type 'PySide.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis'>"


class QAbstractXmlReceiver(__Shiboken.Object):
    # no doc
    def atomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def characters(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def endDocument(self, *args, **kwargs): # real signature unknown
        pass

    def endElement(self, *args, **kwargs): # real signature unknown
        pass

    def endOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBinding(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def startDocument(self, *args, **kwargs): # real signature unknown
        pass

    def startElement(self, *args, **kwargs): # real signature unknown
        pass

    def startOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def whitespaceOnly(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QSourceLocation(__Shiboken.Object):
    # no doc
    def column(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def line(self, *args, **kwargs): # real signature unknown
        pass

    def setColumn(self, *args, **kwargs): # real signature unknown
        pass

    def setLine(self, *args, **kwargs): # real signature unknown
        pass

    def setUri(self, *args, **kwargs): # real signature unknown
        pass

    def uri(self, *args, **kwargs): # real signature unknown
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


class QXmlSerializer(QAbstractXmlReceiver):
    # no doc
    def atomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def characters(self, *args, **kwargs): # real signature unknown
        pass

    def codec(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def endDocument(self, *args, **kwargs): # real signature unknown
        pass

    def endElement(self, *args, **kwargs): # real signature unknown
        pass

    def endOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBinding(self, *args, **kwargs): # real signature unknown
        pass

    def outputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def setCodec(self, *args, **kwargs): # real signature unknown
        pass

    def startDocument(self, *args, **kwargs): # real signature unknown
        pass

    def startElement(self, *args, **kwargs): # real signature unknown
        pass

    def startOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QXmlFormatter(QXmlSerializer):
    # no doc
    def atomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def characters(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def endDocument(self, *args, **kwargs): # real signature unknown
        pass

    def endElement(self, *args, **kwargs): # real signature unknown
        pass

    def endOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def indentationDepth(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def setIndentationDepth(self, *args, **kwargs): # real signature unknown
        pass

    def startDocument(self, *args, **kwargs): # real signature unknown
        pass

    def startElement(self, *args, **kwargs): # real signature unknown
        pass

    def startOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QXmlItem(__Shiboken.Object):
    # no doc
    def isAtomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def isNode(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def toAtomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def toNodeModelIndex(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass


class QXmlName(__Shiboken.Object):
    # no doc
    def fromClarkName(self, *args, **kwargs): # real signature unknown
        pass

    def isNCName(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def localName(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceUri(self, *args, **kwargs): # real signature unknown
        pass

    def prefix(self, *args, **kwargs): # real signature unknown
        pass

    def toClarkName(self, *args, **kwargs): # real signature unknown
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


class QXmlNamePool(__Shiboken.Object):
    # no doc
    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QXmlNodeModelIndex(__Shiboken.Object):
    # no doc
    def additionalData(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def internalPointer(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def model(self, *args, **kwargs): # real signature unknown
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

    Attribute = PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Attribute
    Comment = PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Comment
    Document = PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Document
    DocumentOrder = None # (!) real value is "<type 'PySide.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder'>"
    Element = PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Element
    Follows = PySide.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder.Follows
    Is = PySide.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder.Is
    Namespace = PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Namespace
    NodeKind = None # (!) real value is "<type 'PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind'>"
    Precedes = PySide.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder.Precedes
    ProcessingInstruction = PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.ProcessingInstruction
    Text = PySide.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Text


class QXmlQuery(__Shiboken.Object):
    # no doc
    def bindVariable(self, *args, **kwargs): # real signature unknown
        pass

    def evaluateTo(self, *args, **kwargs): # real signature unknown
        pass

    def initialTemplateName(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def messageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def namePool(self, *args, **kwargs): # real signature unknown
        pass

    def queryLanguage(self, *args, **kwargs): # real signature unknown
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialTemplateName(self, *args, **kwargs): # real signature unknown
        pass

    def setMessageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setUriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def uriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    QueryLanguage = None # (!) real value is "<type 'PySide.QtXmlPatterns.QXmlQuery.QueryLanguage'>"
    XmlSchema11IdentityConstraintField = PySide.QtXmlPatterns.QXmlQuery.QueryLanguage.XmlSchema11IdentityConstraintField
    XmlSchema11IdentityConstraintSelector = PySide.QtXmlPatterns.QXmlQuery.QueryLanguage.XmlSchema11IdentityConstraintSelector
    XPath20 = PySide.QtXmlPatterns.QXmlQuery.QueryLanguage.XPath20
    XQuery10 = PySide.QtXmlPatterns.QXmlQuery.QueryLanguage.XQuery10
    XSLT20 = PySide.QtXmlPatterns.QXmlQuery.QueryLanguage.XSLT20


class QXmlResultItems(__Shiboken.Object):
    # no doc
    def current(self, *args, **kwargs): # real signature unknown
        pass

    def hasError(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QXmlSchema(__Shiboken.Object):
    # no doc
    def documentUri(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def messageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def namePool(self, *args, **kwargs): # real signature unknown
        pass

    def setMessageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def setUriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def uriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class QXmlSchemaValidator(__Shiboken.Object):
    # no doc
    def messageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def namePool(self, *args, **kwargs): # real signature unknown
        pass

    def schema(self, *args, **kwargs): # real signature unknown
        pass

    def setMessageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def setSchema(self, *args, **kwargs): # real signature unknown
        pass

    def setUriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def uriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


