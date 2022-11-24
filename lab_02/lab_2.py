import random
import matplotlib.pyplot as plt
import numpy as np

def datasets_make_regression(coef, data_size, noise_sigma, random_state):
    x = np.arange(0, data_size, 1.)
    mu = 0.0
    random.seed(random_state)
    noise = np.empty((data_size, 1))
    y = np.empty((data_size, 1))

    for i in range(data_size):
        noise[i] = random.gauss(mu, noise_sigma)
        y[i] = coef[0] + coef[1]*x[i] + noise[i]

    return x, y

coef_true = [34.2, 2.] # весовые коэффициенты
data_size = 200 # размер генерируемого набора данных
noise_sigma = 10 # СКО шума в данных
random_state = 42
x_scale, y_estimate = datasets_make_regression(coef_true, data_size, noise_sigma, random_state)

plt.plot(x_scale, y_estimate, 'o')
plt.xlabel('x (порядковый номер измерения)', fontsize=14)
plt.ylabel('y (оценка температуры)', fontsize=14)


def coefficient_reg_stat(x, y):
    size = len(x)
    avg_x = sum(x) / len(x)  # оценка МО величины x
    avg_y = sum(y) / len(y)  # оценка МО величины y
    # оценка МО величины x*y
    avg_xy = sum(x[i] * y[i] for i in range(0, size)) / size
    # оценка СКО величины x
    std_x = (sum((x[i] - avg_x) ** 2 for i in range(0, size)) / size) ** 0.5
    # оценка СКО величины y
    std_y = (sum((y[i] - avg_y) ** 2 for i in range(0, size)) / size) ** 0.5
    # оценка коэффициента корреляции величин x и y
    corr_xy = (avg_xy - avg_x * avg_y) / (std_x * std_y)

    # расчет искомых коэффициентов
    w1 = corr_xy * std_y / std_x
    w0 = avg_y - avg_x * w1
    return w0, w1

a = []
[w0_3, w1_3] = coefficient_reg_stat(x_scale, y_estimate)
print(w0_3, w1_3)

def predict(w0, w1, x_scale):
    y_pred = [w0 + val*w1 for val in x_scale]
    return y_pred

y_predict = predict(w0_3, w1_3, x_scale)

plt.plot(x_scale, y_estimate, 'o', label = 'Истинные значения')
plt.plot(x_scale, y_predict, '*', label = 'Расчетные значения')
plt.legend(loc = 'best', fontsize=12)
plt.xlabel('x (порядковый номер измерения)', fontsize=14)
plt.ylabel('y (оценка температуры)', fontsize=14)
plt.show()