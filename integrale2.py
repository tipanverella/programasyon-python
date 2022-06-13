"""
suite module integrale la
"""

import cmath

from ast import Expression
from tkinter import Variable


function:Expression = "x**2"

def funct(y:Expression):
    return y

for index, value in enumerate(function):
    if value == "x":
        x:Variable
        function[index] = x
    print(function)

f = eval(function)

expression = funct(function)

#methode des trapezes

a:int = input()
b:int = input()
N:int = input()

pas = (b-a)/N
k = a

Somme = []

while k < N:
    somme = pas*((f(k)+f(k+1))/2)
    Somme.append(somme)

integrale = sum(Somme)

