from types import FunctionType
from typing import Callable, Tuple, Dict
from functools import reduce

def pure(f: Callable, namespace: Dict = {}): return FunctionType(f.__code__, namespace)
@pure
def idf(x): return x
def mu(*fs: Tuple[Callable]): return reduce(lambda f, g: lambda x: f(g(x)), fs, idf)
