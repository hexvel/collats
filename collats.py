import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

def collats(n):
    sp = [n]
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1 
        sp.append(n)
    fig, ax = plt.subplots()
    ax.plot(sp)
    plt.show()


collats(int(input("Введите число для построени гипотезы Коллатца: ")))
