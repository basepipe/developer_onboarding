# encoding: utf-8
# module operator
# from (built-in)
# by generator 1.147
"""
Operator interface.

This module exports a set of functions implemented in C corresponding
to the intrinsic operators of Python.  For example, operator.add(x, y)
is equivalent to the expression x+y.  The function names are those
used for special methods; variants without leading and trailing
'__' are also provided for convenience.
"""
# no imports

# functions

def abs(a): # real signature unknown; restored from __doc__
    """ abs(a) -- Same as abs(a). """
    pass

def add(a, b): # real signature unknown; restored from __doc__
    """ add(a, b) -- Same as a + b. """
    pass

def and_(a, b): # real signature unknown; restored from __doc__
    """ and_(a, b) -- Same as a & b. """
    pass

def concat(a, b): # real signature unknown; restored from __doc__
    """ concat(a, b) -- Same as a + b, for a and b sequences. """
    pass

def contains(a, b): # real signature unknown; restored from __doc__
    """ contains(a, b) -- Same as b in a (note reversed operands). """
    pass

def countOf(a, b): # real signature unknown; restored from __doc__
    """ countOf(a, b) -- Return the number of times b occurs in a. """
    pass

def delitem(a, b): # real signature unknown; restored from __doc__
    """ delitem(a, b) -- Same as del a[b]. """
    pass

def delslice(a, b, c): # real signature unknown; restored from __doc__
    """ delslice(a, b, c) -- Same as del a[b:c]. """
    pass

def div(a, b): # real signature unknown; restored from __doc__
    """ div(a, b) -- Same as a / b when __future__.division is not in effect. """
    pass

def eq(a, b): # real signature unknown; restored from __doc__
    """ eq(a, b) -- Same as a==b. """
    pass

def floordiv(a, b): # real signature unknown; restored from __doc__
    """ floordiv(a, b) -- Same as a // b. """
    pass

def ge(a, b): # real signature unknown; restored from __doc__
    """ ge(a, b) -- Same as a>=b. """
    pass

def getitem(a, b): # real signature unknown; restored from __doc__
    """ getitem(a, b) -- Same as a[b]. """
    pass

def getslice(a, b, c): # real signature unknown; restored from __doc__
    """ getslice(a, b, c) -- Same as a[b:c]. """
    pass

def gt(a, b): # real signature unknown; restored from __doc__
    """ gt(a, b) -- Same as a>b. """
    pass

def iadd(a, b): # real signature unknown; restored from __doc__
    """ a = iadd(a, b) -- Same as a += b. """
    pass

def iand(a, b): # real signature unknown; restored from __doc__
    """ a = iand(a, b) -- Same as a &= b. """
    pass

def iconcat(a, b): # real signature unknown; restored from __doc__
    """ a = iconcat(a, b) -- Same as a += b, for a and b sequences. """
    pass

def idiv(a, b): # real signature unknown; restored from __doc__
    """ a = idiv(a, b) -- Same as a /= b when __future__.division is not in effect. """
    pass

def ifloordiv(a, b): # real signature unknown; restored from __doc__
    """ a = ifloordiv(a, b) -- Same as a //= b. """
    pass

def ilshift(a, b): # real signature unknown; restored from __doc__
    """ a = ilshift(a, b) -- Same as a <<= b. """
    pass

def imod(a, b): # real signature unknown; restored from __doc__
    """ a = imod(a, b) -- Same as a %= b. """
    pass

def imul(a, b): # real signature unknown; restored from __doc__
    """ a = imul(a, b) -- Same as a *= b. """
    pass

def index(a): # real signature unknown; restored from __doc__
    """ index(a) -- Same as a.__index__() """
    pass

def indexOf(a, b): # real signature unknown; restored from __doc__
    """ indexOf(a, b) -- Return the first index of b in a. """
    pass

def inv(a): # real signature unknown; restored from __doc__
    """ inv(a) -- Same as ~a. """
    pass

def invert(a): # real signature unknown; restored from __doc__
    """ invert(a) -- Same as ~a. """
    pass

def ior(a, b): # real signature unknown; restored from __doc__
    """ a = ior(a, b) -- Same as a |= b. """
    pass

def ipow(a, b): # real signature unknown; restored from __doc__
    """ a = ipow(a, b) -- Same as a **= b. """
    pass

def irepeat(a, b): # real signature unknown; restored from __doc__
    """ a = irepeat(a, b) -- Same as a *= b, where a is a sequence, and b is an integer. """
    pass

def irshift(a, b): # real signature unknown; restored from __doc__
    """ a = irshift(a, b) -- Same as a >>= b. """
    pass

def isCallable(a): # real signature unknown; restored from __doc__
    """ isCallable(a) -- Same as callable(a). """
    pass

def isMappingType(a): # real signature unknown; restored from __doc__
    """ isMappingType(a) -- Return True if a has a mapping type, False otherwise. """
    pass

def isNumberType(a): # real signature unknown; restored from __doc__
    """ isNumberType(a) -- Return True if a has a numeric type, False otherwise. """
    pass

def isSequenceType(a): # real signature unknown; restored from __doc__
    """ isSequenceType(a) -- Return True if a has a sequence type, False otherwise. """
    pass

def isub(a, b): # real signature unknown; restored from __doc__
    """ a = isub(a, b) -- Same as a -= b. """
    pass

def is_(a, b): # real signature unknown; restored from __doc__
    """ is_(a, b) -- Same as a is b. """
    pass

def is_not(a, b): # real signature unknown; restored from __doc__
    """ is_not(a, b) -- Same as a is not b. """
    pass

def itruediv(a, b): # real signature unknown; restored from __doc__
    """ a = itruediv(a, b) -- Same as a /= b when __future__.division is in effect. """
    pass

def ixor(a, b): # real signature unknown; restored from __doc__
    """ a = ixor(a, b) -- Same as a ^= b. """
    pass

def le(a, b): # real signature unknown; restored from __doc__
    """ le(a, b) -- Same as a<=b. """
    pass

def lshift(a, b): # real signature unknown; restored from __doc__
    """ lshift(a, b) -- Same as a << b. """
    pass

def lt(a, b): # real signature unknown; restored from __doc__
    """ lt(a, b) -- Same as a<b. """
    pass

def mod(a, b): # real signature unknown; restored from __doc__
    """ mod(a, b) -- Same as a % b. """
    pass

def mul(a, b): # real signature unknown; restored from __doc__
    """ mul(a, b) -- Same as a * b. """
    pass

def ne(a, b): # real signature unknown; restored from __doc__
    """ ne(a, b) -- Same as a!=b. """
    pass

def neg(a): # real signature unknown; restored from __doc__
    """ neg(a) -- Same as -a. """
    pass

def not_(a): # real signature unknown; restored from __doc__
    """ not_(a) -- Same as not a. """
    pass

def or_(a, b): # real signature unknown; restored from __doc__
    """ or_(a, b) -- Same as a | b. """
    pass

def pos(a): # real signature unknown; restored from __doc__
    """ pos(a) -- Same as +a. """
    pass

def pow(a, b): # real signature unknown; restored from __doc__
    """ pow(a, b) -- Same as a ** b. """
    pass

def repeat(a, b): # real signature unknown; restored from __doc__
    """ repeat(a, b) -- Return a * b, where a is a sequence, and b is an integer. """
    pass

def rshift(a, b): # real signature unknown; restored from __doc__
    """ rshift(a, b) -- Same as a >> b. """
    pass

def sequenceIncludes(a, b): # real signature unknown; restored from __doc__
    """ sequenceIncludes(a, b) -- Same as b in a (note reversed operands; deprecated). """
    pass

def setitem(a, b, c): # real signature unknown; restored from __doc__
    """ setitem(a, b, c) -- Same as a[b] = c. """
    pass

def setslice(a, b, c, d): # real signature unknown; restored from __doc__
    """ setslice(a, b, c, d) -- Same as a[b:c] = d. """
    pass

def sub(a, b): # real signature unknown; restored from __doc__
    """ sub(a, b) -- Same as a - b. """
    pass

def truediv(a, b): # real signature unknown; restored from __doc__
    """ truediv(a, b) -- Same as a / b when __future__.division is in effect. """
    pass

def truth(a): # real signature unknown; restored from __doc__
    """ truth(a) -- Return True if a is true, False otherwise. """
    pass

def xor(a, b): # real signature unknown; restored from __doc__
    """ xor(a, b) -- Same as a ^ b. """
    pass

def _compare_digest(*args, **kwargs): # real signature unknown
    """
    compare_digest(a, b) -> bool
    
    Return 'a == b'.  This function uses an approach designed to prevent
    timing analysis, making it appropriate for cryptography.
    a and b must both be of the same type: either str (ASCII only),
    or any type that supports the buffer protocol (e.g. bytes).
    
    Note: If a and b are of different lengths, or if an error occurs,
    a timing attack could theoretically reveal information about the
    types and lengths of a and b--but not their values.
    """
    pass

def __abs__(*args, **kwargs): # real signature unknown
    """ abs(a) -- Same as abs(a). """
    pass

def __add__(*args, **kwargs): # real signature unknown
    """ add(a, b) -- Same as a + b. """
    pass

def __and__(*args, **kwargs): # real signature unknown
    """ and_(a, b) -- Same as a & b. """
    pass

def __concat__(*args, **kwargs): # real signature unknown
    """ concat(a, b) -- Same as a + b, for a and b sequences. """
    pass

def __contains__(*args, **kwargs): # real signature unknown
    """ contains(a, b) -- Same as b in a (note reversed operands). """
    pass

def __delitem__(*args, **kwargs): # real signature unknown
    """ delitem(a, b) -- Same as del a[b]. """
    pass

def __delslice__(*args, **kwargs): # real signature unknown
    """ delslice(a, b, c) -- Same as del a[b:c]. """
    pass

def __div__(*args, **kwargs): # real signature unknown
    """ div(a, b) -- Same as a / b when __future__.division is not in effect. """
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ eq(a, b) -- Same as a==b. """
    pass

def __floordiv__(*args, **kwargs): # real signature unknown
    """ floordiv(a, b) -- Same as a // b. """
    pass

def __getitem__(*args, **kwargs): # real signature unknown
    """ getitem(a, b) -- Same as a[b]. """
    pass

def __getslice__(*args, **kwargs): # real signature unknown
    """ getslice(a, b, c) -- Same as a[b:c]. """
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ ge(a, b) -- Same as a>=b. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ gt(a, b) -- Same as a>b. """
    pass

def __iadd__(*args, **kwargs): # real signature unknown
    """ a = iadd(a, b) -- Same as a += b. """
    pass

def __iand__(*args, **kwargs): # real signature unknown
    """ a = iand(a, b) -- Same as a &= b. """
    pass

def __iconcat__(*args, **kwargs): # real signature unknown
    """ a = iconcat(a, b) -- Same as a += b, for a and b sequences. """
    pass

def __idiv__(*args, **kwargs): # real signature unknown
    """ a = idiv(a, b) -- Same as a /= b when __future__.division is not in effect. """
    pass

def __ifloordiv__(*args, **kwargs): # real signature unknown
    """ a = ifloordiv(a, b) -- Same as a //= b. """
    pass

def __ilshift__(*args, **kwargs): # real signature unknown
    """ a = ilshift(a, b) -- Same as a <<= b. """
    pass

def __imod__(*args, **kwargs): # real signature unknown
    """ a = imod(a, b) -- Same as a %= b. """
    pass

def __imul__(*args, **kwargs): # real signature unknown
    """ a = imul(a, b) -- Same as a *= b. """
    pass

def __index__(): # real signature unknown; restored from __doc__
    """ index(a) -- Same as a.__index__() """
    pass

def __invert__(*args, **kwargs): # real signature unknown
    """ invert(a) -- Same as ~a. """
    pass

def __inv__(*args, **kwargs): # real signature unknown
    """ inv(a) -- Same as ~a. """
    pass

def __ior__(*args, **kwargs): # real signature unknown
    """ a = ior(a, b) -- Same as a |= b. """
    pass

def __ipow__(*args, **kwargs): # real signature unknown
    """ a = ipow(a, b) -- Same as a **= b. """
    pass

def __irepeat__(*args, **kwargs): # real signature unknown
    """ a = irepeat(a, b) -- Same as a *= b, where a is a sequence, and b is an integer. """
    pass

def __irshift__(*args, **kwargs): # real signature unknown
    """ a = irshift(a, b) -- Same as a >>= b. """
    pass

def __isub__(*args, **kwargs): # real signature unknown
    """ a = isub(a, b) -- Same as a -= b. """
    pass

def __itruediv__(*args, **kwargs): # real signature unknown
    """ a = itruediv(a, b) -- Same as a /= b when __future__.division is in effect. """
    pass

def __ixor__(*args, **kwargs): # real signature unknown
    """ a = ixor(a, b) -- Same as a ^= b. """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ le(a, b) -- Same as a<=b. """
    pass

def __lshift__(*args, **kwargs): # real signature unknown
    """ lshift(a, b) -- Same as a << b. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ lt(a, b) -- Same as a<b. """
    pass

def __mod__(*args, **kwargs): # real signature unknown
    """ mod(a, b) -- Same as a % b. """
    pass

def __mul__(*args, **kwargs): # real signature unknown
    """ mul(a, b) -- Same as a * b. """
    pass

def __neg__(*args, **kwargs): # real signature unknown
    """ neg(a) -- Same as -a. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ ne(a, b) -- Same as a!=b. """
    pass

def __not__(*args, **kwargs): # real signature unknown
    """ not_(a) -- Same as not a. """
    pass

def __or__(*args, **kwargs): # real signature unknown
    """ or_(a, b) -- Same as a | b. """
    pass

def __pos__(*args, **kwargs): # real signature unknown
    """ pos(a) -- Same as +a. """
    pass

def __pow__(*args, **kwargs): # real signature unknown
    """ pow(a, b) -- Same as a ** b. """
    pass

def __repeat__(*args, **kwargs): # real signature unknown
    """ repeat(a, b) -- Return a * b, where a is a sequence, and b is an integer. """
    pass

def __rshift__(*args, **kwargs): # real signature unknown
    """ rshift(a, b) -- Same as a >> b. """
    pass

def __setitem__(*args, **kwargs): # real signature unknown
    """ setitem(a, b, c) -- Same as a[b] = c. """
    pass

def __setslice__(*args, **kwargs): # real signature unknown
    """ setslice(a, b, c, d) -- Same as a[b:c] = d. """
    pass

def __sub__(*args, **kwargs): # real signature unknown
    """ sub(a, b) -- Same as a - b. """
    pass

def __truediv__(*args, **kwargs): # real signature unknown
    """ truediv(a, b) -- Same as a / b when __future__.division is in effect. """
    pass

def __xor__(*args, **kwargs): # real signature unknown
    """ xor(a, b) -- Same as a ^ b. """
    pass

# classes

class attrgetter(object):
    """
    attrgetter(attr, ...) --> attrgetter object
    
    Return a callable object that fetches the given attribute(s) from its operand.
    After f = attrgetter('name'), the call f(r) returns r.name.
    After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
    After h = attrgetter('name.first', 'name.last'), the call h(r) returns
    (r.name.first, r.name.last).
    """
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, attr, *more): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class itemgetter(object):
    """
    itemgetter(item, ...) --> itemgetter object
    
    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
    """
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, item, *more): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class methodcaller(object):
    """
    methodcaller(name, ...) --> methodcaller object
    
    Return a callable object that calls the given method on its operand.
    After f = methodcaller('name'), the call f(r) returns r.name().
    After g = methodcaller('name', 'date', foo=1), the call g(r) returns
    r.name('date', foo=1).
    """
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, name, *more): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


