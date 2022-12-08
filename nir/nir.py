import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from matplotlib.patches import Polygon

np.random.seed(42)


def equation_0(x):
    '''f(x) = sin(x)'''
    return np.sin(x)


def equation_1(x):
    '''f(x) = 3 + 2x - 3x² + 2x³'''
    return 3 + 2 * x - 3 * x ** 2 + x ** 3


def equaition_2(x):
    '''f(x) = 1 / (3cos(x) + 2)'''
    return 1 / (3 * np.cos(x) + 2)


def equation_e(x):
    '''f(x) = x * e^(-x)'''
    return x * np.e ** -x


def equation_3(x, y):
    '''f(x, y) = 4 + 2y + 2x + xy + x³y'''
    return 4 + 2 * y + 2 * x + x * y + x ** 3 * y


def equation_3_2(xa, ya, a, b, c, d):
    x = (b - a) * xa + a
    y = (d - c) * ya + c
    return 4 + 2 * y + 2 * x + x * y + x ** 3 * y


def equation_4(x, y):
    '''f(x,y) = y²/x²'''
    return y ** 2 / x ** 2


def equation_4_2(xa, ya, a, b, c, d):
    x = (b - a) * xa + a
    y = (d - c) * ya + c
    return y ** 2 / x ** 2


def equation_5(x, y):
    '''f(x,y) = sqrt(x * x + y * y) + 3 * cos(sqrt(x * x + y * y)) + 5'''
    return np.sqrt(x * x + y * y) + 3 * np.cos(np.sqrt(x*x + y*y)) + 5


def equation_5_2(xa, ya, a, b, c, d):
    x = (b - a) * xa + a
    y = (d - c) * ya + c
    return np.sqrt(x * x + y * y) + 3 * np.cos(np.sqrt(x * x + y * y)) + 5




