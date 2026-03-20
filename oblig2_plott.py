import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return np.exp(-x/4) * np.arctan(x)

def equation(x):
    return np.arctan(x) - 4/(x**2 + 1)

# Finn toppunkt
x0 = 1  # startverdi
x_max = fsolve(equation, x0)[0]
y_max = f(x_max)

print(f"x = {x_max:.4f}")
print(f"f(x) = {y_max:.4f}")

# Plot
x = np.linspace(0, 5, 100)
y = f(x)

plt.plot(x, y)
plt.scatter(x_max, y_max, color='red')
plt.title("Graf av f(x)")
plt.savefig("plot.png")
plt.show()