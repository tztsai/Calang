from operator import add, sub, mul, floordiv, mod, ne, neg, lt, gt, le, ge, xor, pow as pow_, and_, or_, not_
from functools import reduce
from numbers import Number, Rational
from fractions import Fraction
from math import inf
from sympy import Symbol, solve, limit, integrate, diff, simplify, expand, factor, Integer, Float, Matrix, Expr, Add, sqrt, log, exp, gcd, factorial, floor, sin, cos, tan, asin, acos, atan, cosh, sinh, tanh, E, pi

from _obj import Op, function, Env, config, Range
from _funcs import is_iter, is_function, is_matrix, is_number, is_vector, is_symbol, is_, all_, any_, add_, sub_, div_, mul_, db_fact, transpose, dot, equal, power, range_, depth, shape, substitute, flatten, row, col, row, cols, findall, compose


def standardize(name, val):

    def pynumfy(val):
        # convert a number into a python number type
        if any(isinstance(val, c) for c in (int, float, complex, Fraction)):
            return val
        elif isinstance(val, Integer):
            return int(val)
        elif isinstance(val, Float):
            return float(val)
        else:
            z = complex(val)
            if equal(z.imag, 0): return z.real
            else: return z

    def unify_types(x):
        if type(x) is bool:
            return 1 if x else 0
        elif is_iter(x) and not any_(range, Range, set, lambda c: isinstance(x, c)):
            return tuple(unify_types(a) for a in x)
        else:
            try: return pynumfy(x)
            except (ValueError, TypeError):
                if isinstance(x, Expr): return simplify(factor(x))
                else: return x

    if is_function(val):
        fun = compose(unify_types, val)
        fun.str = name
        return fun
    else:
        return val


binary_ops = {'+': (add_, 6), '-': (sub_, 6), '*': (mul_, 8), '.*': (dot, 7), '/': (div_, 8), '//': (floordiv, 8), '^': (power, 14), '%': (mod, 8), '=': (equal, 0), '!=': (ne, 0), '<': (lt, 0), '>': (gt, 0), '<=': (le, 0), '>=': (ge, 0), 'xor': (xor, 3), 'in': (lambda x, y: x in y, -2), 'outof': (lambda x, y: x not in y, -2), '~': (Range, 5), '..': (range_, 5), 'and': (and_, -5), 'is': (None, 0), 'or': (or_, -6), '/\\': (and_, 8), '\\/': (or_, 7)}

for op in binary_ops:
    fun, pri = binary_ops[op]
    binary_ops[op] = Op(type, standardize(op, fun), pri)

unary_l_ops = {'-': neg, 'not': not_, '@': transpose}
unary_r_ops = {'!': factorial, '!!': db_fact}

op_list = set(binary_ops).union(set(unary_l_ops)).union(set(unary_r_ops))

keywords = {'if', 'else', 'in', 'dir', 'load', 'conf', 'when', 'import', 'del'}

builtins = {'add': add_, 'sub': sub_, 'mul': mul_, 'div': div_,
            'sin': sin, 'cos': cos, 'tan': tan, 'asin': asin, 'acos': acos,
            'atan': atan, 'abs': abs, 'sqrt': sqrt, 'floor': floor, 'log': log,
            'E': E, 'PI': pi, 'I': 1j, 'INF': inf, 'range': range, 'max': max, 'min': min, 'gcd': gcd,
            'binom': lambda n, m: factorial(n) / (factorial(m) * factorial(n-m)), 
            'len': len, 'sort': sorted, 'exit': lambda: exit(),
            'exp': exp, 'lg': lambda x: log(x)/log(10), 'ln': log, 'log2': lambda x: log(x)/log(2),
            'number?': is_number, 'symbol?': is_symbol, 'iter?': is_iter, 'lambda?': is_function, 'matrix?': is_matrix, 'vector?': is_vector, 'function?': is_function,
             'list': list, 'sum': lambda l: reduce(add, l), 'product': lambda l: reduce(mul, l), 'matrix': Matrix, 'set': set,
            'car': lambda l: l[0], 'cdr': lambda l: l[1:], 'cons': lambda a, l: (a,) + l, 'enum': enumerate,
            'row': row, 'col': col, 'shape': shape, 'depth': depth, 'transp': transpose, 'flatten': flatten,
            'all': all_, 'any': any, 'same': lambda l: True if l == [] else all(x == l[0] for x in l[1:]),
            'sinh': sinh, 'cosh': cosh, 'tanh': tanh, 'degrees': lambda x: x / pi * 180,
            'real': lambda z: z.real if type(z) is complex else z, 'imag': lambda z: z.imag if type(z) is complex else 0,
            'conj': lambda z: z.conjugate(), 'angle': lambda z: atan(z.imag / z.real),
            'reduce': reduce, 'filter': filter, 'map': map, 'zip': zip, 'find': findall,
            'solve': solve, 'lim': limit, 'diff': diff, 'int': integrate, 'subs': substitute,
            'expand': expand, 'factor': factor}

for name in builtins:
    val = builtins[name]
    if is_function(val):
        builtins[name] = standardize(name, val)
        builtins[name].str = f'<built-in: {name}>'


if __name__ == "__main__":
    import doctest
    doctest.testmod()