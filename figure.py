import matplotlib.pyplot as plt
import numpy as np

def createfig(implicit, analitical):
    x = np.linspace(0, np.pi / 2, implicit.I + 1)

    impY = implicit.getModel()
    analY = analitical.getAnalitical(x)

    fig, ax = plt.subplots()

    ax.plot(x, analY, color="green", label="Аналитическое решение")
    ax.plot(x, impY, color="red", label="Численое решение")

    ax.set_xlabel("θ")
    ax.set_ylabel("u(θ,t)")
    ax.legend()
    plt.grid()

    return fig