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


def derivative_legendre_polynomial(n: int, x: float) -> float:
    '''значение производной полинома Лежандра'''
    p1, p2 = legendre_polynomial(n - 1, x), legendre_polynomial(n, x)
    return n / (1 - x * x) * (p1 - x * p2)


def roots_legendre_polynomial(n: int, eps: float = 1e-12) -> List[float]:
    '''корни полинома Лежандра n-го порядка'''
    roots = [np.cos(np.pi * (4 * i + 3) / (4 * n + 2)) for i in range(n)]
    for i, root in enumerate(roots): # уточнение корней
        root_val = legendre_polynomial(n, root)
        while abs(root_val) > eps:
            root -= root_val / derivative_legendre_polynomial(n, root)
            root_val = legendre_polynomial(n, root)
        roots[i] = root
    return roots


def gauss_integrate_norm(f: Callable, n: int) -> float:
    '''интегрирование методом Гаусса на промежутке [-1,1]'''
    t = roots_legendre_polynomial(n)
    T = np.array([[t_i ** k for t_i in t] for k in range(n)])

    tk = lambda k: 2 / (k + 1) if k % 2 == 0 else 0
    b = np.array([tk(k) for k in range(n)])
    A = np.linalg.solve(T, b) # решение СЛАУ

    return sum(A_i * f(t_i) for A_i, t_i in zip(A, t))


def gauss_integrate(f: Callable, a: float, b: float, n: int) -> float:
    '''интегрирование методом Гаусса на произвольном промежутке'''
    mean, diff = (a + b) * .5, (b - a) * .5
    g = lambda t: f(mean + diff * t)
    return diff * gauss_integrate_norm(g, n)


def composite_integrate(f:Callable, a1: float, b1: float, a2: float, b2: float, method_1: Callable, method_2:
Callable, n1: int, n2: int) -> float:
    func = lambda y: method_1(lambda x: f(x, y), a1, b1, n1)
    return method_2(func, a2, b2, n2)


def function_integrator(f: Callable, a: float, b: float, c: float, d: float, n: int, m: int) -> float:
    return composite_integrate(f, a, b, c, d, gauss_integrate, simpson_integrate, n, m)


def integrate_function(t: float, n: int, m: int) -> float:
    l_r = lambda theta, phi: 2 * np.cos(theta) / (1 - np.sin(theta) ** 2 * np.cos(phi) ** 2)
    f = lambda theta, phi: (1 - np.exp(-t * l_r(theta, phi))) * np.cos(theta) * np.sin(theta)

    return 4 / np.pi *function_integrator(f, 0, np.pi * .5, 0, np.pi * .5, n, m)


