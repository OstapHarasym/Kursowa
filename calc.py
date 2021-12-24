import scipy.integrate
from math import *
import matplotlib.pyplot as plt
from sympy import limit, oo, Symbol
import datetime


# Обраховує інтегал, приймає рядок з функцією та межі
def integrate(foo, up, down):
    def fun(x):
        return eval(foo)

    return scipy.integrate.quad(fun, eval(up), eval(down))


# Обраховує суму n перших елементів арифметичної прогресії, приймає рядок з функцією та кількість перших елеменів
def progression_sum(foo, count):
    def fun(x):
        return eval(foo)

    s = 0
    for i in range(count):
        s += fun(i)
    return s


# Розраховує дані про диф.рівняння, приймає рядок з функцією, межі та початкове значення y, файл з графіком зберігається
def differential(foo, y0, up, down):
    def fun1(t, y):
        return eval(foo)

    sol = scipy.integrate.solve_ivp(fun1, t_span=[eval(up), eval(down)], y0=[eval(y0)], method='Radau')
    fig, axes = plt.subplots()
    axes.plot(sol.t, sol.y[0])
    axes.grid()
    plt.savefig("./static/chart.png")
    return [sol]


# Обчислює границю, приймає рядок з функцією та значення, куди границя прямує
def lim(foo, to):
    x = Symbol('x')
    y = eval(foo)
    return limit(y, x, eval(to))


# Обчислює визначник матриці, приймає матрицю
def determinant(args):
    matrix = [[], [], []]
    m = 0
    n = 0
    for i in args:
        if i == 'Порахувати визначник':
            break
        if m == 3:
            m = 0
            n += 1
        matrix[n].append(float(i))
        m += 1
    return scipy.linalg.det(matrix)


# Будує графіки і зберігає їхні файли, приймає вибірку даних з БД
def stats(db):
    lst = []
    dt = []
    pie_lst = []
    for i in db:
        if i.calcTime.date().day > datetime.date.today().day - 7:
            lst.append(i.calcType)
            dt.append(i.calcTime.date().day)
        pie_lst.append(i.calcType)
    st = set(pie_lst)
    x = []
    for i in range(6, -1, -1):
        x.append(datetime.date.today() - datetime.timedelta(i))
    fig, axes = plt.subplots()
    axes.hist(x=dt, bins=len(set(dt)))
    plt.savefig("./static/hist.png")

    y = []
    k = 0
    for i in st:
        y.append(0)
        for j in pie_lst:
            if i == j:
                y[k] = y[k] + 1
        k += 1

    fig, axes = plt.subplots()

    axes.pie(x=y, labels=st, autopct='%1.1f%%')

    plt.savefig("./static/pie.png")
