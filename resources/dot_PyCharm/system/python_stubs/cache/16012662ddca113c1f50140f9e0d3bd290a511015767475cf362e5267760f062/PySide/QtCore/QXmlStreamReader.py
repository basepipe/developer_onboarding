# encoding: utf-8
# module PySide.QtCore
# from C:\Python27\lib\site-packages\PySide\QtCore.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QXmlStreamReader(__Shiboken.Object):
    # no doc
    def addData(self, *args, **kwargs): # real signature unknown
        pass

    def addExtraNamespaceDeclaration(self, *args, **kwargs): # real signature unknown
        pass

    def addExtraNamespaceDeclarations(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def attributes(self, *args, **kwargs): # real signature unknown
        pass

    def characterOffset(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def columnNumber(self, *args, **kwargs): # real signature unknown
        pass

    def device(self, *args, **kwargs): # real signature unknown
        pass

    def documentEncoding(self, *args, **kwargs): # real signature unknown
        pass

    def documentVersion(self, *args, **kwargs): # real signature unknown
        pass

    def dtdName(self, *args, **kwargs): # real signature unknown
        pass

    def dtdPublicId(self, *args, **kwargs): # real signature unknown
        pass

    def dtdSystemId(self, *args, **kwargs): # real signature unknown
        pass

    def entityDeclarations(self, *args, **kwargs): # real signature unknown
        pass

    def entityResolver(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def hasError(self, *args, **kwargs): # real signature unknown
        pass

    def isCDATA(self, *args, **kwargs): # real signature unknown
        pass

    def isCharacters(self, *args, **kwargs): # real signature unknown
        pass

    def isComment(self, *args, **kwargs): # real signature unknown
        pass

    def isDTD(self, *args, **kwargs): # real signature unknown
        pass

    def isEndDocument(self, *args, **kwargs): # real signature unknown
        pass

    def isEndElement(self, *args, **kwargs): # real signature unknown
        pass

    def isEntityReference(self, *args, **kwargs): # real signature unknown
        pass

    def isProcessingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def isStandaloneDocument(self, *args, **kwargs): # real signature unknown
        pass

    def isStartDocument(self, *args, **kwargs): # real signature unknown
        pass

    def isStartElement(self, *args, **kwargs): # real signature unknown
        pass

    def isWhitespace(self, *args, **kwargs): # real signature unknown
        pass

    def lineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceDeclarations(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceProcessing(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceUri(self, *args, **kwargs): # real signature unknown
        pass

    def notationDeclarations(self, *args, **kwargs): # real signature unknown
        pass

    def prefix(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstructionData(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstructionTarget(self, *args, **kwargs): # real signature unknown
        pass

    def qualifiedName(self, *args, **kwargs): # real signature unknown
        pass

    def raiseError(self, *args, **kwargs): # real signature unknown
        pass

    def readElementText(self, *args, **kwargs): # real signature unknown
        pass

    def readNext(self, *args, **kwargs): # real signature unknown
        pass

    def readNextStartElement(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, *args, **kwargs): # real signature unknown
        pass

    def setEntityResolver(self, *args, **kwargs): # real signature unknown
        pass

    def setNamespaceProcessing(self, *args, **kwargs): # real signature unknown
        pass

    def skipCurrentElement(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def tokenString(self, *args, **kwargs): # real signature unknown
        pass

    def tokenType(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Characters = PySide.QtCore.QXmlStreamReader.TokenType.Characters
    Comment = PySide.QtCore.QXmlStreamReader.TokenType.Comment
    CustomError = PySide.QtCore.QXmlStreamReader.Error.CustomError
    DTD = PySide.QtCore.QXmlStreamReader.TokenType.DTD
    EndDocument = PySide.QtCore.QXmlStreamReader.TokenType.EndDocument
    EndElement = PySide.QtCore.QXmlStreamReader.TokenType.EndElement
    EntityReference = PySide.QtCore.QXmlStreamReader.TokenType.EntityReference
    Error = None # (!) real value is "<type 'PySide.QtCore.QXmlStreamReader.Error'>"
    ErrorOnUnexpectedElement = PySide.QtCore.QXmlStreamReader.ReadElementTextBehaviour.ErrorOnUnexpectedElement
    IncludeChildElements = PySide.QtCore.QXmlStreamReader.ReadElementTextBehaviour.IncludeChildElements
    Invalid = PySide.QtCore.QXmlStreamReader.TokenType.Invalid
    NoError = PySide.QtCore.QXmlStreamReader.Error.NoError
    NoToken = PySide.QtCore.QXmlStreamReader.TokenType.NoToken
    NotWellFormedError = PySide.QtCore.QXmlStreamReader.Error.NotWellFormedError
    PrematureEndOfDocumentError = PySide.QtCore.QXmlStreamReader.Error.PrematureEndOfDocumentError
    ProcessingInstruction = PySide.QtCore.QXmlStreamReader.TokenType.ProcessingInstruction
    ReadElementTextBehaviour = None # (!) real value is "<type 'PySide.QtCore.QXmlStreamReader.ReadElementTextBehaviour'>"
    SkipChildElements = PySide.QtCore.QXmlStreamReader.ReadElementTextBehaviour.SkipChildElements
    StartDocument = PySide.QtCore.QXmlStreamReader.TokenType.StartDocument
    StartElement = PySide.QtCore.QXmlStreamReader.TokenType.StartElement
    TokenType = None # (!) real value is "<type 'PySide.QtCore.QXmlStreamReader.TokenType'>"
    UnexpectedElementError = PySide.QtCore.QXmlStreamReader.Error.UnexpectedElementError


