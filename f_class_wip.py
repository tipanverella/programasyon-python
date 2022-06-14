"""
Module sa pemet ou kalkule integrale par metod simpson ak trapeze.
"""

import ast
from email.policy import default
from math import log, cos, sin, exp
from dataclasses import dataclass, field
from tkinter import Variable
from graph_function import graph1, graph2


@dataclass
class expression:
    var:Variable = None
    expr: ast.Expression = None

    def pow_var(self, value:int):
        globals()[self.var] = self.var
        y = f"{self.var}**{value}"
        return f"y = {y}"

    def pow_exp(self):
        for elem in self.expr:
            a = isinstance(elem, str)
            if a:
                self.var = elem
            
        expression = f"{self.expr}"
        y = f"{expression}"
        return f"y = {y}"

    try:
        eval(self.expr)
        
    except TypeError:
        print("nap vanse")
        continue

y = expression(var="x")
print(y)
print("y = ", y.pow_var(2))

z = expression(expr="x**2 + 2")
print(z)
print("y =", z.pow_exp)
