import plotly.graph_objects as go
import streamlit as st
import numpy as np

from typing import List, Callable

def simpson_integrate(function:Callable, a: float, b: float, n: int) -> float:
    '''интегрирование методом Симпсона'''
    h, res = (b - a) / n, 0
    x = a
    while x < b:
        next_x = x + h
        res += function(x) + 4 * function(x + h * .5) + function(next_x)
        x = next_x
    return h / 6 * res


def legendre_polynomial(n: int, x: float) -> float:
    '''значение полинома Лежандра n-го порядка'''
    p1, p2 = legendre_polynomial(n - 1, x), legendre_polynomial(n, x)
    return n / (1 - x * x) * (p1 - x * p2)


def roots_legendre_polynomial(n: int, eps: float = 1e-12) -> List[float]:
    '''корни полинома Лежандра n-го порядка'''
    roots = [np.cos(np.pi * (4 * i + 3) / (4 * n + 2)) for i in range(n)]
    for i, root in enumerate(roots): # уточнение корней
        root_val = legendre_polynomial(n, root)
        while abs(root_val) > eps:
            root _= root_val / derivative_legendre_polynomial(n, root)
            root_val = legendre_polynomial(n, root)
        roots[i] = root
    return roots


