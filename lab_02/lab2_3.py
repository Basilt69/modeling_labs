import random
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    st.markdown("### Лабораторная работа №2")
    st.markdown("**Тема:** Построение и программная реализация алгоритма наилучшего среднеквадратичного приближения.")
    st.markdown("""**Цель работы:**
    Получение навыков построения алгоритма реализации метода наименьших квадратов с использованием полиномов 
    заданной степени в одномерном и двумерном вариантах при аппроксимации табличных функций с весами""")

    a1, a2, a3 = st.columns(3)
    b1, b2, b3 = st.columns(3)
    c1, c2, c3 = st.columns(3)
    d1, d2, d3 = st.columns(3)
    e1, e2, e3 = st.columns(3)
    f1, f2, f3 = st.columns(3)


    x1 = a1.number_input("x₁", min_value=-10, max_value=10, value=2., step=1)
    x2 = b1.number_input("x₂", min_value=-10, max_value=10, value=2.5, step=1)
    x3 = c1.number_input("x₃", min_value=-10, max_value=10, value=3., step=1)
    x4 = d1.number_input("x₄", min_value=-10, max_value=10, value=3.5, step=1)
    x5 = e1.number_input("x₅", min_value=-10, max_value=10, value=4., step=1)
    x6 = f1.number_input("x₆", min_value=-10, max_value=10, value=4.5, step=1)

    y1 = a2.number_input("y₁:", min_value=-10, max_value=10., value=3.36022917, format="%.4f")
    y2 = b2.number_input("y₂", min_value=-10, max_value=10., value=1.38151692, format="%.4f")
    y3 = c2.number_input("y₃", min_value=-10, max_value=10., value=7.75382231, format="%.4f")
    y4 = d2.number_input("y₄", min_value=-10, max_value=10., value=1.47294493, format="%.4f")
    y5 = e2.number_input("y₅", min_value=-10, max_value=10., value=4.90192966, format="%.4f")
    y6 = f2.number_input("y₆", min_value=-10, max_value=10., value=2.65940507, format="%.4f")

    x_array = [x1, x2, x3, x4, x5, x6]
    y_array = [y1, y2, y3, y4, y5, y6]
    x_array_len = len(x_array)
    x_array_range = range(x_array_len)

    st.write("---")
    st.write("Итоговая таблица:")
    result_data = {
        "x": x_array,
        "y": y_array,
        }
    result = pd.DataFrame(data=result_data).applymap("{0:.4f}".format)
    st.table(result.assign(hack="").set_index("hack"))

if __name__=="__main__":
    main()