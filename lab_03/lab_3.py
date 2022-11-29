import plotly.graph_objects as go
import streamlit as st
import numpy as np

from typing import List, Callable


def simpson_integrate(function: Callable, a: float, b: float, n: int) -> float:
    """ интегрирование методом Симпсона """
    h, res = (b - a) / n, 0
    x = a
    while x < b:
        next_x = x + h
        res += function(x) + 4 * function(x + h * .5) + function(next_x)
        x = next_x
    return h / 6 * res


def legendre_polynomial(n: int, x: float) -> float:
    """ значение полинома Лежандра n-го порядка """
    if n < 2:
        return [1, x][n]
    p1, p2 = legendre_polynomial(n - 1, x), legendre_polynomial(n - 2, x)
    return ((2 * n - 1) * x * p1 - (n - 1) * p2) / n


def derivative_legendre_polynomial(n: int, x: float) -> float:
    """ значение производной полинома Лежандра """
    p1, p2 = legendre_polynomial(n - 1, x), legendre_polynomial(n, x)
    return n / (1 - x * x) * (p1 - x * p2)


def roots_legendre_polynomial(n: int, eps: float = 1e-12) -> List[float]:
    """ корни полинома Лежандра n-го порядка """
    roots = [np.cos(np.pi * (4 * i + 3) / (4 * n + 2)) for i in range(n)]
    for i, root in enumerate(roots):  # уточнение корней
        root_val = legendre_polynomial(n, root)
        while abs(root_val) > eps:
            root -= root_val / derivative_legendre_polynomial(n, root)
            root_val = legendre_polynomial(n, root)
        roots[i] = root
    return roots


def gauss_integrate_norm(f: Callable, n: int) -> float:
    """ интегрирование методом Гаусса на промежутке [-1, 1] """
    t = roots_legendre_polynomial(n)
    T = np.array([[t_i ** k for t_i in t] for k in range(n)])

    tk = lambda k: 2 / (k + 1) if k % 2 == 0 else 0
    b = np.array([tk(k) for k in range(n)])
    A = np.linalg.solve(T, b)  # решение СЛАУ

    return sum(A_i * f(t_i) for A_i, t_i in zip(A, t))


def gauss_integrate(f: Callable, a: float, b: float, n: int) -> float:
    """ интегрирование методом Гаусса на произвольном промежутке """
    mean, diff = (a + b) * .5, (b - a) * .5
    g = lambda t: f(mean + diff * t)
    return diff * gauss_integrate_norm(g, n)


def composite_integrate(f: Callable, a1: float, b1: float, a2: float, b2: float,
                        method_1: Callable, method_2: Callable, n1: int, n2: int) -> float:
    func = lambda y: method_1(lambda x: f(x, y), a1, b1, n1)
    return method_2(func, a2, b2, n2)


def function_integrator(f: Callable, a: float, b: float, c: float, d: float, n: int, m: int) -> float:
    return composite_integrate(f, a, b, c, d, gauss_integrate, simpson_integrate, n, m)


def integrate_function(t: float, n: int, m: int) -> float:
    l_r = lambda theta, phi: 2 * np.cos(theta) / (1 - np.sin(theta) ** 2 * np.cos(phi) ** 2)
    f = lambda theta, phi: (1 - np.exp(-t * l_r(theta, phi))) * np.cos(theta) * np.sin(theta)

    return 4 / np.pi * function_integrator(f, 0, np.pi * .5, 0, np.pi * .5, n, m)


def plot(func: Callable, n: int, m: int, test: bool = False, test_func: Callable = None, test_func2: Callable = None):
    """ отрисовка графика """
    st.markdown("---")
    x = np.arange(.05, 10, .001) if not test else np.arange(-10, 10, .001)
    y = [func(t, n, m) for t in x] if not test else test_func2(x) - test_func2(0 * x)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
    ))

    if test:
        def test_y(n_test):
            return [func(test_func, 0, x_test, n_test) for x_test in x]

        fig.add_trace(go.Scatter(
            x=x,
            y=test_y(1),
            mode='lines',
        ))

    fig.update_layout(
        title_text=f"График зависимости ε(τ)" if not test else "График тестирования",
        xaxis_title="τ" if not test else "",
        yaxis_title="ε" if not test else "",
        showlegend=False
    )

    st.write(fig)
    st.markdown("---")


def test_function(func: Callable):
    def test_f(x):
        return .3 * (x - 1) ** 2 - .1 * (x + 4) ** 2 - x

    def act_int_f(x):
        return .1 * (x - 1) ** 3 - .1 / 3 * (x + 4) ** 3 - .5 * x ** 2

    plot(func, 0, 0, test=True, test_func=test_f, test_func2=act_int_f)


def main():
    st.markdown("### Лабораторная работа №3")
    st.markdown("**Тема:** Построение и программная реализация алгоритмов численного интегрирования.")
    st.markdown("""**Цель работы:** Получение навыков построения алгоритма вычисления двукратного 
        интеграла с использованием квадратурных формул Гаусса и Симпсона.""")

    st.write("---")

    c0, c1, c2 = st.columns(3)
    tau = c0.number_input("Введите значение параметра τ:", min_value=.0, max_value=1., value=.808, format="%.3f")
    N = c1.number_input("Введите значение N:", min_value=1, max_value=100, value=4, step=1)
    M = c2.number_input("Введите значение M:", min_value=1, max_value=100, value=5, step=1)

    result = integrate_function(tau, N, M)
    st.write(f"Результат интегрирования: {round(result, 5)}")

    plot(integrate_function, N, M)

    test = st.selectbox("Выберите метод тестирования", ("Гаусс", "Симпсон"))
    if test == "Симпсон":
        test_function(simpson_integrate)
    elif test == "Гаусс":
        test_function(gauss_integrate)


if __name__ == "__main__":
    main()