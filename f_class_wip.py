"""
Module sa pemet ou kreye objet tip fonksyon.
"""

import ast
from math import log, cos, sin, exp
from dataclasses import dataclass, field
import math
from operator import add, eq
from tkinter import Variable
from typing_extensions import Self
from graph_function import graph1, graph2


def find(value, pattern="*"):
    from fnmatch import fnmatch

    return [x for x in dir(value) if fnmatch(x, pattern)]


@dataclass(order=True)
class expression:
    var: Variable = None
    expr: ast.Expression = None
    pow: float = None

    @property
    def pow_var(self):
        globals()[self.var] = self.var
        y = f"{self.var}**{self.pow}"
        return f"y = {y}"

    @property
    def exp(self):
        for elem in self.expr:
            a = isinstance(elem, str)
            if a:
                self.var = elem

        expression = f"{self.expr}"
        y = f"{expression}"
        return y


@dataclass(order=True)
class type:
    """
    classe sa a kreye objet fonction tankou nenpot expression an, oubyen fonksyon ki utilise fonction ki soti nan module math yo.
    """

    name: str = None
    o_type: str = None
    formula: expression = None

    @property
    def type_assign(self):
        if self.name is not None:
            l_func = find(math, self.name)
            for elem in l_func:
                func = elem
        else:
            pass
        return func

    @property
    def eq(self):
        "Returns the equation of a given function."
        if self.o_type is not None:
            equation = expression(expr=self.formula)
            return equation.exp
        else:
            pass


@dataclass(order=True, frozen=True)
class functions:
    sort_index: int = field(init=False, repr=False)
    eq: str
    name: str = "function"
    power: int = 1
    type: str = None

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.power)

    def __str__(self):
        return f"The {self.name}, is a function powered at level {self.power}, which has the equation: y = {self.eq_func}"

    def __add__(self, other: Self):
        new_eq: str = self.eq_func + other.eq_func
        return functions(new_eq)

    def add(self, other: Self):
        return functions()

    @property
    def eq_func(self):
        equation = type(o_type=self.type, formula=self.eq)
        return equation.eq
    
    def calcul(self, value: float) -> float:
        y = self.eq_func.replace("(x)", str(value))
        z = eval(y)
        if z - round(z) == 0.0:
            z = round(z)
        return f"{self.eq_func} = {z},  for x = {value}"

    def calcul_for_graph(self, value:float) -> float:
        y = self.eq_func.replace("(x)", str(value))
        z = eval(y)
        if z - round(z) == 0.0:
            z = round(z)
        return z

    @property
    def graph(self):
        "fonction sa a graph quelque soit objet functions* que ou genyen an"
        abscisse = [elem for elem in graph1(100)]
        ordonnee = []
        for elem in abscisse:
            imag = self.calcul_for_graph(elem)
            ordonnee.append(imag)
        courbe = graph2([abscisse, ordonnee])
        return courbe

    def integrale_trap(self) -> float:
        a: int = input()
        b: int = input()
        n: int = input()
        pas = (b - a) / n
        k = a
        Somme = [float]

        while k <= n:
            somme = pas * ((self.calcul_for_graph(k) + self.calcul_for_graph(k + 1)) / 2)
            Somme.append(somme)
            k += pas
        integrale:float = sum(Somme)

        return integrale


y = expression(var="x", pow=2)
print(y.pow_var)

z = expression(expr="(x)**2 + 2")
print(z.exp)

x = type("cos")
print(x.type_assign)

a = type(o_type="parametric", formula="2*((x)**2)+5")
print(a.eq)

b = functions(power=2, type="parametric", eq="2*((x)**2) + 4*(x) + 1")
print(b.eq_func)
print(b.calcul(4))


c = functions(name="logarithm function", power=1, type="other", eq="log((x))")
print(c.eq_func)
print(c.calcul(1))

d = functions(name="exponential function", power=1, type="other", eq="sin((x))")
print(d)
print(d.eq_func)
print(d.calcul(1))
print(d.graph)


e = c + d
#pati __add__ method la pa mache nan klas mwen an
# #bug
print(e)



"""
1) fe methode graph la mache....msuspek problem nan c nan utilisation eq_func an li ye
2) modifye graph2 pou li pran nom fonksyon an kom params and then map ka use li kom legend()...
"""