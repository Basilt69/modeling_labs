import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from st_aggrid import AgGrid


class NewtonInterpolationPolynomial(object):
    '''
    Класс для интерполяции полинома Ньютона
    ------
    Принимаемые параметры:
    nodes : список узлов
    n : степень полинома
    x : значение аргумента
    '''

    def __init__(self, nodes, n, x):
        self.nodes = self.sort_nodes(nodes)
        self.range_ = n + 1
        self.n = n
        self.x = x

    @staticmethod
    def sort_nodes(arr):
        '''Сортировка узлов'''
        return arr[arr[:,0].argsort()]

    @staticmethod
    def find_nearest(self):
        '''Поиск индекса ближайшего к аргументу значения узла'''
        array = np.asarray(self.nodes[:,0])
        idx = (np.abs(array - self.x)).argmin()
        return idx

    @staticmethod
    def select_nodes(self):
        '''Выбор новых массивов узлов в диапазоне n+1 от ближайшей к аргументу точки'''
        from_ = self.find_nearest(self) - self.range_ // 2
        if from_ < 0:
            from_ = 0

        to = from_ + self.range_
        if to > self.nodes.shape[0]:
            to = self.nodes.shape[0]
            from_ = to - self.range_

        return self.nodes[np.ix_(range(from_, to), [0,1])]

    @staticmethod
    def calc_divided_diffs(self, nodes):
        '''Расчёт значений разделенных разностей'''
        n = self.range_
        divided_diffs = np.zeros([n,n])
        divided_diffs[:,0] = nodes[:,1]
        x = nodes[:,0]

        for j in range(1,n):
            for i in range(n - j):
                divided_diffs[i][j] = (divided_diffs[i + 1][j - 1] - divided_diffs[i][j-1]) / (x[i+j] - x[i])

        return divided_diffs

    @staticmethod
    def find_polynomial(self, nodes, diffs):
        '''Поиск полинома Ньютона при фиксированном x'''
        x_data = nodes[:, 0]
        coefficients = diffs[0]
        n = self.n
        p = coefficients[n]

        for k in range(1, n+1):
            p = coefficients[n-k] + (self.x - x_data[n-k]) * p

        return p

    def calc(self):
        '''Вычисление значения полинома Ньютона()'''
        selected_nodes = self.select_nodes(self)
        divided_diffs = self.calc_divided_diffs(self, selected_nodes)
        polynomial = self.find_polynomial(self, selected_nodes, divided_diffs)

        return selected_nodes, divided_diffs, polynomial


def main():
    st.markdown("### Лабораторная работа 1.1 - Построение и программная реализация алгоритма полиномиальной "
                "интерполяции табличных функций")
    st.markdown("Цель работы - Получение навыков построения алгоритма интерполяции таблично заданных функций "
                "полиномом Ньютона")

    x_arr = [0.00, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1.05]
    y_arr = [1.000000, 0.838771, 0.655336, 0.450447, 0.225336, -0.018310, -0.278390, -0.552430]
    y_div_arr = [-1.000000, -1.14944, -1.29552, -1.43497, -1.56464, -1.68164, -1.78333, -1.86742]

    df = pd.DataFrame({
        "x" : x_arr,
        "y" : y_arr,
        "y'" : y_div_arr
    })


    st.subheader("Таблица функции с количеством узлов N:")
    grid_return = AgGrid(
        df,
        editable=True,
        height=300,
        reload_data=False,
        theme="alpine",
    )
    arr = grid_return["data"].to_numpy()

    c0, c1 = st.columns(2)
    n = c0.number_input("Введите степень полинома - n", min_value=0, max_value=7, value=3, step=1)
    x = c1.number_input("Введите значение аргумента - x", min_value=.0, max_value=1., value=.545, format="%.3f")

    st.write("-----")

    ni = NewtonInterpolationPolynomial(arr, int(n), x)
    new_nodes, diffs, poly = ni.calc()
    st.subheader("Таблица значений разделенных разностей:")
    st.write(pd.DataFrame(diffs).replace(0, np.nan))
    st.write(f"Значение полинома y(x) = {poly:.5f}")

    st.write("-----")

    ni_root = NewtonInterpolationPolynomial(np.fliplr(arr), int(n), 0)
    _, _, root = ni_root.calc()
    st.write(f"Значение корня y(x̄) = {root:.5f}")

    st.write("-----")

    st.subheader("График функции:")
    plt.figure(figsize=(12,8))
    plt.plot(arr[:,0], arr[:,1], 'bo')
    plt.plot(new_nodes[:,0], new_nodes[:,1])
    st.pyplot(plt)

if __name__ == "__main__":
    main()



