import pandas as pd
import numpy as np


from st_aggrid import AgGrid


x = float(input("Введите фиксированное значение x\n"))
z = int(input("Введите количество узлов\n"))

x_arr = [0.00, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1.05]
y_arr = [1.000000, 0.838771, 0.655336, 0.450447, 0.225336, -0.018310, -0.278390, -0.552430]
y_div_arr = [-1.000000, -1.14944, -1.29552, -1.43497, -1.56464, -1.68164, -1.78333, -1.86742]

df = pd.DataFrame({
        "x" : x_arr,
        "y" : y_arr,
        "y'" : y_div_arr
})

grid_return_2 = AgGrid(
        df,
        editable=True,
        height=300,
        reload_data=False,
        theme="balham",
    )

print(df)


def sort_nodes(arr):
    '''Сортировка узлов'''
    return arr[arr[:, 0].argsort()]

def find_nearest(array, x):
    '''Поиск индекса ближайшего к аргументу значения узла'''
    array = np.asarray(nodes[:,0])
    idx = (np.abs(array - x)).argmin()
    return idx

arr = grid_return_2["data"].to_numpy()

nodes = sort_nodes(arr)
idx = find_nearest(nodes, x)

print(idx)

def select_nodes_1():
    # Выбор массива узлов для дальнейших вычислений
    n = z + 2
    divided_diffs = np.zeros([n, n])
    divided_diffs[:, 0] = nodes[idx, 1]
    divided_diffs[2, 0] = nodes[idx + 1, 1]

    divided_diffs[0,1] = nodes[idx,2]
    x = np.zeros(n)
    x[:] = nodes[idx,0]
    x[2] = nodes[idx + 1, 0]
    print(x)

    divided_diffs[1][1] = (divided_diffs[2][0] - divided_diffs[1][0]) / (x[2] - x[0])
    divided_diffs[0][2] = (divided_diffs[1][1] - divided_diffs[0][1]) / (x[2] - x[0])

    return divided_diffs


def select_nodes_2():
    # Выбор массива узлов для дальнейших вычислений
    n = z + 3
    divided_diffs = np.zeros([n, n+1])
    if (x_arr[idx] - x_arr[idx + 1]) < (x_arr[idx] - x_arr[idx - 1]):
        divided_diffs[:, 0] = nodes[idx, 1]
        divided_diffs[2:4, 0] = nodes[idx + 1, 1]
        divided_diffs[4, 0] = nodes[idx + 2, 1]
        divided_diffs[0,1] = y_div_arr[idx]
        divided_diffs[2, 1] = y_div_arr[idx + 1]
        divided_diffs[4, 1] = y_div_arr[idx + 2]
        x = np.zeros(n+1)
        x[:] = nodes[idx, 0]
        x[2:4] = nodes[idx + 1, 0]
        x[4:] = nodes[idx + 2, 0]
        print("A")
    elif (x_arr[idx] - x_arr[idx + 1]) > (x_arr[idx] - x_arr[idx - 1]):
        divided_diffs[:, 0] = nodes[idx-1, 1]
        divided_diffs[2:4, 0] = nodes[idx, 1]
        divided_diffs[4, 0] = nodes[idx + 1, 1]
        divided_diffs[0, 1] = y_div_arr[idx-1]
        divided_diffs[2, 1] = y_div_arr[idx]
        divided_diffs[4, 1] = y_div_arr[idx + 1]
        x = np.zeros(n+1)
        x[:] = nodes[idx-1, 0]
        x[2:4] = nodes[idx, 0]
        x[4:] = nodes[idx + 1, 0]
        print("B")
    else:
        divided_diffs[:, 0] = nodes[idx, 1]
        divided_diffs[2:4, 0] = nodes[idx + 1, 1]
        divided_diffs[4, 0] = nodes[idx + 2, 1]
        divided_diffs[0, 1] = y_div_arr[idx]
        divided_diffs[2, 1] = y_div_arr[idx + 1]
        divided_diffs[4, 1] = y_div_arr[idx + 2]
        x = np.zeros(n+1)
        x[:] = nodes[idx, 0]
        x[2:4] = nodes[idx + 1, 0]
        x[4:] = nodes[idx + 2, 0]
        print("C")


    #print('X',x)

    for j in range(1,2):
        # i - строка
        # j - колонка
        for i in range(1, n-1, 2):
            divided_diffs[i,j] = (divided_diffs[i+1][j-1] - divided_diffs[i][j-1]) / (x[j+1] - x[j-1])

    for j in range(1,n):
        # i - строка
        # j - колонка
        for i in range(n-j):
            divided_diffs[i,j+1] = (divided_diffs[i+1][j] - divided_diffs[i][j]) / (x[j+1] - x[0])

    print(divided_diffs)
    return divided_diffs,x


def select_nodes_3():
    # Выбор массива узлов для дальнейших вычислений
    n = z + 4
    divided_diffs = np.zeros([n+1, n+1])
    divided_diffs[:, 0] = nodes[idx, 1]
    divided_diffs[2:4, 0] = nodes[idx+1, 1]
    divided_diffs[4:, 0] = nodes[idx + 2, 1]
    divided_diffs[6, 0] = nodes[idx + 3, 1]
    divided_diffs[0, 1] = y_div_arr[idx]
    divided_diffs[2, 1] = y_div_arr[idx+1]
    divided_diffs[4, 1] = y_div_arr[idx + 2]
    divided_diffs[6, 1] = y_div_arr[idx + 3]

    x = np.zeros(n+1)
    x[:] = nodes[idx, 0]
    x[2:4] = nodes[idx+1, 0]
    x[4:6] = nodes[idx + 2, 0]
    x[6:] = nodes[idx + 3, 0]

    print('X',x)

    for j in range(1,2):
        # i - строка
        # j - колонка
        for i in range(1, n, 2):
            divided_diffs[i,j] = (divided_diffs[i+1][j-1] - divided_diffs[i][j-1]) / (x[i+1] - x[i-1])


    for j in range(1,n):
        # i - строка
        # j - колонка
        for i in range(n-j):
            divided_diffs[i,j+1] = (divided_diffs[i+1][j] - divided_diffs[i][j]) / (x[j+1] - x[0])

    print(divided_diffs)
    return divided_diffs,x




if z == 1:
    selected_nodes = select_nodes_1()
    print("This are selected nodes\n",selected_nodes)
    p = y_arr[idx] + selected_nodes[0,1]*(x - x_arr[idx]) + selected_nodes[0,2]*(x - x_arr[idx])
    print('This is p',p)
elif z == 2:
    selected_nodes, values = select_nodes_2()
    print("This are selected nodes\n", selected_nodes)
    p = y_arr[idx] + \
        selected_nodes[0,1]*(x-values[0]) + \
        selected_nodes[0,2]*((x - values[0])*(x - values[0])) +\
        selected_nodes[0,3]*((x - values[0])*(x - values[0])) * (x - values[2]) + \
        selected_nodes[0,4]*((x - values[0])*(x - values[0])) * ((x - values[2])*(x - values[2])) + \
        selected_nodes[0,5]*((x - values[0])*(x - values[0])) * ((x - values[2])*(x - values[2]))*(x-values[4])
    print('This is p',p)
elif z == 3:
    selected_nodes, values = select_nodes_3()
    p = y_arr[idx] + \
        selected_nodes[0,1]*(x-values[0]) + \
        selected_nodes[0,2]*((x - values[0])*(x - values[0])) +\
        selected_nodes[0,3]*((x - values[0])*(x - values[0])) * (x - values[2]) + \
        selected_nodes[0,4]*((x - values[0])*(x - values[0])) * ((x - values[2])*(x - values[2])) + \
        selected_nodes[0,5]*((x - values[0])*(x - values[0])) * ((x - values[2])*(x - values[2]))*(x-values[4]) + \
        selected_nodes[0,6]*((x - values[0])*(x - values[0])) * ((x - values[2])*(x - values[2]))*((x-values[4])*(x-values[4])) + \
        selected_nodes[0,7]*((x - values[0])*(x - values[0])) * ((x - values[2])*(x - values[2]))*((x-values[4])*(x-values[4]))*(x-values[6])

    print('This is p',p)