"""
Module sa pemet ou kalkule integrale par metod simpson ak trapeze.
"""


from cmath import cos
from dataclasses import dataclass
from typing import Tuple


@dataclass
class functions():
    coeff: float


    def find_expr(y):
        "Fonksyon sa aprann rekonet expression"

        import math
        from math import pi
        
        if True:
            a= y.count(cos)
            b = y.count(pi)
            c = y.count("x")
            if a is not None:
                replace



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

