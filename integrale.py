"""
Module sa pemet ou kalkule integrale par metod simpson ak trapeze.
"""

import ast
from ast import Expression
from cmath import cos
from math import log, cos, sin, exp, pi
from dataclasses import dataclass
from mmap import PROT_WRITE
from multiprocessing.sharedctypes import Value
from re import X
from tkinter import Variable, StringVar
from typing import Tuple

from graph_function import graph_eq

@dataclass
class functions:

    def __init__(self, var, power):
        self.var = var
        self.power = power

    @property
    def equation(self):
        eq_formula = self.var**self.power
        return eq_formula

    def calcul(self, value):
        self.var = value
        y = value**self.power
        return y

    def graph(self):
        courbe = graph_eq(self.equation)
        return courbe

    


    y = (var**power)

    @property
    def expression(self):
        "Fonksyon sa aprann rekonet expression"
        equation  = var**power
        return equation

    def another_thing(self):
        verif = y in self
        if verif:
            return y
        else:
            raise KeyboardInterrupt
        

y = functions(var="x", power=2)
y1 = functions(var="x", power=3)
print(y)
print(y1)
print(y.expression)

def interval(interval:Tuple, nonmb_enteval:int):
    """
    fonksyon sa 
    """

    pas = (interval[1]-interval[0])/nonmb_enteval
    y = input("entre equation fonction ou lan ")


exp_func  = input("antre expression fonction ou an... ")

try:
    exp_func = eval(exp_func)
except NameError:
    "Nap vanse!"

y = repr(exp_func)


Expression(y, eval)


code = ast.parse(y)  
print(code) 
print(ast.dump(code))
exec(compile(code, filename="", mode="eval"))