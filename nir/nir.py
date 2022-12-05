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

