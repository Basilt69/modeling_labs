import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from st_aggrid import AgGrid


class NewtonInterpolationPolynomial(object):
    '''
    Класс для интерполяции полинома Эрмита
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