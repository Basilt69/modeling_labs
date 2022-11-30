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


