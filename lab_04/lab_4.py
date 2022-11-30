import streamlit as st
import pandas as pd

from typing import List

def one_sided_derivative(n:int, x_arr_len: int, y_arr: List, h: int) -> float:
    '''Односторонняя разностная производная'''
    if n + 1 == x_arr_len:
        return (y_arr[n] - y_arr[n - 1]) / h
    return (y_arr[n + 1] - y_arr[n]) / h


def central_derivative(n:int, x_arr_len: int, y_arr: List, h: int) -> float:
    '''Центральная разностная производная'''
    if n == 0:
        return (-3 * y_arr[0] + 4 * y_arr[1] - y_arr[2]) / (2 * h)
    elif n + 1 < x_arr_len:
        return (y_arr[n + 1] - y_arr[n - 1]) / (2 * h)
    return (y_arr[n - 2] - 4 * y_arr[n - 1] + 3 * y_arr[n]) / (2 * h)


def runge_derivative(n: int, x_arr_len: int, y_arr: List, h: int) -> float:
    '''Рунге (2-ая формула) с использованием односторонней производной'''
    if n + 2 >= x_arr_len:
        return (3 * y_arr[n] - 4 * y_arr[n - 1] + y_arr[n - 2]) / (2 * h)
    return (-y_arr[n + 2] + 4 * y_arr[n + 1] - 3 * y_arr[n]) / (2 * h)


def alignment_variables(n: int, x_arr_len: int, y_arr: List, x_arr: List) -> float:
    '''Выравнивающие переменные'''
    if n + 1 < x_arr_len:
        return y_arr[n] / x_arr[n] * x_arr[n + 1] / y_arr[n + 1] * (y_arr[n] - y_arr[n + 1]) / (x_arr[n] - x_arr[n + 1])
    return y_arr[n - 1] / x_arr[n - 1] * x_arr[n] / y_arr[n] * (y_arr[n - 1] - y_arr[n]) / (x_arr[n - 1] - x_arr[n])


def second_derivative(n: int, x_arr_len: int, y_arr: List, h: int) -> float:
    '''Вторая разностная производная'''
    if n == 0:
        return (y_arr[2] - 2 * y_arr[1] + y_arr[0]) / (h * h)
    elif n + 1 < x_arr_len:
        return (y_arr[n + 1] - 2 * y_arr[n] + y_arr[n - 1]) / (h * h)
    return (y_arr[n] - 2 * y_arr[n - 1] + y_arr[n - 2]) / (h * h)


def main():
    st.markdown("### Лабораторная работа №4")
    st.markdown("**Тема:** Построение и программная реализация алгоритмов численного дифференцирования.")
    st.markdown("""**Цель работы:** 
    Получение навыков построения алгоритма вычисления производных от сеточных функций.""")

    formula = r"""
    $$
    y = \frac{a_0x}{a_1 + a_2x}
    $$
    """
    st.markdown("""**Задание:** 
        Задана табличная (сеточная) функция.
        Имеется информация, что закономерность представленная таблицей, может быть описана формулой""")
    st.write(formula)
    st.write("Параметры функции:")

    a1, a2, a3 = st.columns(3)
    b1, b2, b3 = st.columns(3)
    c1, c2, c3 = st.columns(3)
    d1, d2, d3 = st.columns(3)
    e1, e2, e3 = st.columns(3)
    f1, f2, f3 = st.columns(3)

    x1 = a1.number_input("x₁", min_value=1, max_value=10, value=1, step=1)
    x2 = b1.number_input("x₂", min_value=1, max_value=10, value=2, step=1)
    x3 = c1.number_input("x₃", min_value=1, max_value=10, value=3, step=1)
    x4 = d1.number_input("x₄", min_value=1, max_value=10, value=4, step=1)
    x5 = e1.number_input("x₅", min_value=1, max_value=10, value=5, step=1)
    x6 = f1.number_input("x₆", min_value=1, max_value=10, value=6, step=1)

    y1 = a2.number_input("y₁:", min_value=.001, max_value=10., value=.571, format="%.4f")
    y2 = b2.number_input("y₂", min_value=.001, max_value=10., value=.889, format="%.4f")
    y3 = c2.number_input("y₃", min_value=.001, max_value=10., value=1.091, format="%.4f")
    y4 = d2.number_input("y₄", min_value=.001, max_value=10., value=1.231, format="%.4f")
    y5 = e2.number_input("y₅", min_value=.001, max_value=10., value=1.333, format="%.4f")
    y6 = f2.number_input("y₆", min_value=.001, max_value=10., value=1.412, format="%.4f")

    h = a3.number_input("h:", min_value=1, max_value=10, value=1, step=1)

    x_array = [x1, x2, x3, x4, x5, x6]
    y_array = [y1, y2, y3, y4, y5, y6]
    x_array_len = len(x_array)
    x_array_range = range(x_array_len)

    st.write("---")
    st.write("Итоговая таблица:")
    result_data = {
        "x": x_array,
        "y": y_array,
        "1": [one_sided_derivative(ln, x_array_len, y_array, h) for ln in x_array_range],
        "2": [central_derivative(ln, x_array_len, y_array, h) for ln in x_array_range],
        "3": [runge_derivative(ln, x_array_len, y_array, h) for ln in x_array_range],
        "4": [alignment_variables(ln, x_array_len, y_array, x_array) for ln in x_array_range],
        "5": [second_derivative(ln, x_array_len, y_array, h) for ln in x_array_range],
    }
    result = pd.DataFrame(data=result_data).applymap("{0:.4f}".format)
    st.table(result.assign(hack="").set_index("hack"))

    st.write("Легенда для столбцов 1-5:")
    st.write("1 - Односторонняя разностная производная")
    st.write("2 - Центральная разностная производная")
    st.write("3 - Рунге (2-ая формула) с использованием односторонней производной")
    st.write("4 - Выравнивающие переменные")
    st.write("5 - Вторая разностная производная")


if __name__ == "__main__":
    main()