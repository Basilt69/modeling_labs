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


def estimate_ab(a, b, eps):
    if abs(a % np.pi) < eps:
        a = int(a / np.pi) * np.pi
    elif abs(a % np.e) < eps:
        a = int(a / np.e) * np.e
    if abs(b % np.pi) < np.pi:
        b = int(b / np.pi) * np.pi
    elif abs(b % np.e) < eps:
        b = int(b / np.e) * np.e
    return a, b


def generate_random(a, b, num_samples):
    return np.random.uniform(a, b, num_samples)


def calculate_average(list_random_nums, num_samples, func):
    sum_ = 0
    for i in range(0, num_samples):
        sum_ += func(list_random_nums[i])

    return sum_ / num_samples


def calculate(a, b, num_samples, func):
    list_random_uniform_nums = generate_random(a, b, num_samples)
    average = calculate_average(list_random_uniform_nums, num_samples, func)
    integral = (b - a) * average

    return integral


def calculate_integral(a, b, num_samples, num_iter, func):
    '''Расчёт однократного интеграла'''
    avg_sum = 0
    areas = []
    for i in range(0, num_iter):
        integral = calculate(a, b, num_samples, func)
        avg_sum += integral
        areas.append(integral)
    avg_integral = avg_sum / num_iter

    return areas, avg_integral





