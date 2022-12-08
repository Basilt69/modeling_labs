import random
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

N = 100 # Число экспериментов
sigma = 3 # стандартное отклонение наблюдаемых значений
k = 0.5 # теоретическое значение параметра k
b = 2 # теоретическое значение параметра b


f = np.array([k*z+b for z in range(N)])
y = f + np.random.normal(0, sigma, N)

print(f)
print(y)

x = np.array(range(N))

mx = x.sum()/N
my = y.sum()/N
a2 = np.dot(x.T, x)/N
a11 = np.dot(x.T, y)/N

kk = (a11 - mx*my)/(a2 - mx**2)
bb = my - kk*mx


ff = np.array([kk*z+bb for z in range(N)])
plt.plot(f) # теоретическая прямая
plt.plot(ff, c='red') # экспертиментальная прямая
plt.scatter(x, y, s=2, c='red')
plt.grid(True)
plt.show()


def main():
    st.markdown("### Лабораторная работа №2")
    st.markdown("**Тема:** Построение и программная реализация алгоритма наилучшего среднеквадратичного приближения.")
    st.markdown("""**Цель работы:**
    Получение навыков построения алгоритма реализации метода наименьших квадратов с использованием полиномов 
    заданной степени в одномерном и двумерном вариантах при аппроксимации табличных функций с весами""")


    x_array = [2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5, 10.]
    y_array = [3.36022917, 1.38151692, 7.75382231, 1.47294493, 4.90192966, 2.65940507, 1.30867122, 6.20313785,
               6.67092352, 8.47001833, 5.25194885, 11.75337077, 8.01389994, 11.24240111, 8.7774639, 8.93281672, 15.72259106]

    df = pd.DataFrame({
        "x": x_array,
        "y": y_array,
    })

    st.subheader("Таблица функции с количеством узлов N:")

    grid_return_2 = AgGrid(
        df,
        editable=True,
        height=300,
        reload_data=False,
        theme="alpine",
    )

    #result = pd.DataFrame(data=df).applymap("{0:.4f}".format)

    #st.table(result.assign(hack="").set_index("hack"))







if __name__=="__main__":
    main()



