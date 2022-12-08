import random
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from st_aggrid import AgGrid

n = int(input('Введите степень полинома(n)\n'))

x_array = [2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5, 10.]
y_array = [3.36022917, 1.38151692, 7.75382231, 1.47294493, 4.90192966, 2.65940507, 1.30867122, 6.20313785,
           6.67092352, 8.47001833, 5.25194885, 11.75337077, 8.01389994, 11.24240111, 8.7774639, 8.93281672, 15.72259106]


m = 17 # Количество узлов