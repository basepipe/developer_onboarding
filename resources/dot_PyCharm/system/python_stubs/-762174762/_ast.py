# encoding: utf-8
# module _ast
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

PyCF_ONLY_AST = 1024

__version__ = '82160'

# no functions
# classes

class AST(object):
    # no doc
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    _attributes = ()
    _fields = ()


class operator(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': (), '__dict__': <attribute '__dict__' of 'operator' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'operator' objects>, '__doc__': None})"


class Add(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class alias(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _fields = (
        'name',
        'asname',
    )
    __dict__ = None # (!) real value is "dict_proxy({'__dict__': <attribute '__dict__' of 'alias' objects>, '__module__': '_ast', '_fields': ('name', 'asname'), '__weakref__': <attribute '__weakref__' of 'alias' objects>, '__doc__': None})"


class boolop(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': (), '__dict__': <attribute '__dict__' of 'boolop' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'boolop' objects>, '__doc__': None})"


class And(boolop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class arguments(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _fields = (
        'args',
        'vararg',
        'kwarg',
        'defaults',
    )
    __dict__ = None # (!) real value is "dict_proxy({'__dict__': <attribute '__dict__' of 'arguments' objects>, '__module__': '_ast', '_fields': ('args', 'vararg', 'kwarg', 'defaults'), '__weakref__': <attribute '__weakref__' of 'arguments' objects>, '__doc__': None})"


class stmt(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = (
        'lineno',
        'col_offset',
    )
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': ('lineno', 'col_offset'), '__dict__': <attribute '__dict__' of 'stmt' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'stmt' objects>, '__doc__': None})"


class Assert(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'msg',
    )


class Assign(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'targets',
        'value',
    )


class expr(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = (
        'lineno',
        'col_offset',
    )
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': ('lineno', 'col_offset'), '__dict__': <attribute '__dict__' of 'expr' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'expr' objects>, '__doc__': None})"


class Attribute(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
        'attr',
        'ctx',
    )


class AugAssign(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'target',
        'op',
        'value',
    )


class expr_context(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': (), '__dict__': <attribute '__dict__' of 'expr_context' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'expr_context' objects>, '__doc__': None})"


class AugLoad(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class AugStore(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class BinOp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'left',
        'op',
        'right',
    )


class BitAnd(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class BitOr(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class BitXor(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class BoolOp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'op',
        'values',
    )


class Break(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Call(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'func',
        'args',
        'keywords',
        'starargs',
        'kwargs',
    )


class ClassDef(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'name',
        'bases',
        'body',
        'decorator_list',
    )


class cmpop(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': (), '__dict__': <attribute '__dict__' of 'cmpop' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'cmpop' objects>, '__doc__': None})"


class Compare(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'left',
        'ops',
        'comparators',
    )


class comprehension(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _fields = (
        'target',
        'iter',
        'ifs',
    )
    __dict__ = None # (!) real value is "dict_proxy({'__dict__': <attribute '__dict__' of 'comprehension' objects>, '__module__': '_ast', '_fields': ('target', 'iter', 'ifs'), '__weakref__': <attribute '__weakref__' of 'comprehension' objects>, '__doc__': None})"


class Continue(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Del(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Delete(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'targets',
    )


class Dict(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'keys',
        'values',
    )


class DictComp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'key',
        'value',
        'generators',
    )


class Div(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class slice(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': (), '__dict__': <attribute '__dict__' of 'slice' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'slice' objects>, '__doc__': None})"


class Ellipsis(slice):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Eq(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class excepthandler(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = (
        'lineno',
        'col_offset',
    )
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': ('lineno', 'col_offset'), '__dict__': <attribute '__dict__' of 'excepthandler' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'excepthandler' objects>, '__doc__': None})"


class ExceptHandler(excepthandler):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'type',
        'name',
        'body',
    )


class Exec(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
        'globals',
        'locals',
    )


class Expr(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class mod(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': (), '__dict__': <attribute '__dict__' of 'mod' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'mod' objects>, '__doc__': None})"


class Expression(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
    )


class ExtSlice(slice):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'dims',
    )


class FloorDiv(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class For(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'target',
        'iter',
        'body',
        'orelse',
    )


class FunctionDef(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'name',
        'args',
        'body',
        'decorator_list',
    )


class GeneratorExp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elt',
        'generators',
    )


class Global(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'names',
    )


class Gt(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class GtE(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class If(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )


class IfExp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )


class Import(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'names',
    )


class ImportFrom(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'module',
        'names',
        'level',
    )


class In(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Index(slice):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class Interactive(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
    )


class unaryop(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = ()
    _fields = ()
    __dict__ = None # (!) real value is "dict_proxy({'__module__': '_ast', '_attributes': (), '__dict__': <attribute '__dict__' of 'unaryop' objects>, '_fields': (), '__weakref__': <attribute '__weakref__' of 'unaryop' objects>, '__doc__': None})"


class Invert(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Is(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class IsNot(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class keyword(AST):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _fields = (
        'arg',
        'value',
    )
    __dict__ = None # (!) real value is "dict_proxy({'__dict__': <attribute '__dict__' of 'keyword' objects>, '__module__': '_ast', '_fields': ('arg', 'value'), '__weakref__': <attribute '__weakref__' of 'keyword' objects>, '__doc__': None})"


class Lambda(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'args',
        'body',
    )


class List(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elts',
        'ctx',
    )


class ListComp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elt',
        'generators',
    )


class Load(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class LShift(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Lt(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class LtE(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Mod(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Module(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
    )


class Mult(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Name(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'id',
        'ctx',
    )


class Not(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class NotEq(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class NotIn(cmpop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Num(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'n',
    )


class Or(boolop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Param(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Pass(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Pow(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Print(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'dest',
        'values',
        'nl',
    )


class Raise(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'type',
        'inst',
        'tback',
    )


class Repr(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class Return(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


class RShift(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Set(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elts',
    )


class SetComp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elt',
        'generators',
    )


class Slice(slice):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'lower',
        'upper',
        'step',
    )


class Store(expr_context):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Str(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        's',
    )


class Sub(operator):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class Subscript(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
        'slice',
        'ctx',
    )


class Suite(mod):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
    )


class TryExcept(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
        'handlers',
        'orelse',
    )


class TryFinally(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'body',
        'finalbody',
    )


class Tuple(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'elts',
        'ctx',
    )


class UAdd(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class UnaryOp(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'op',
        'operand',
    )


class USub(unaryop):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = ()


class While(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'test',
        'body',
        'orelse',
    )


class With(stmt):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'context_expr',
        'optional_vars',
        'body',
    )


class Yield(expr):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _fields = (
        'value',
    )


