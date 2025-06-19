import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# --------------------------
# Метод Монте-Карло
# --------------------------
N = 100000  # Кількість випадкових точок

# Генерація випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, b ** 2, N)  # f(x) = x^2, максимум на [0,2] = 4

# Обчислення кількості точок, що потрапили під криву
under_curve = y_rand < f(x_rand)

# Площа прямокутника (висота = 4, ширина = 2)
rectangle_area = (b - a) * (b ** 2)

# Оцінка інтеграла методом Монте-Карло
integral_mc = np.sum(under_curve) / N * rectangle_area

# --------------------------
# Аналітичний результат (через quad)
# --------------------------
integral_analytical, _ = quad(f, a, b)

# --------------------------
# Вивід результатів
# --------------------------
print("Метод Монте-Карло:", integral_mc)
print("Аналітичне значення (quad):", integral_analytical)
print("Абсолютна похибка:", abs(integral_mc - integral_analytical))

# --------------------------
# Побудова графіка з точками Монте-Карло
# --------------------------
fig, ax = plt.subplots()
x_plot = np.linspace(-0.5, 2.5, 400)
y_plot = f(x_plot)

# Побудова графіка функції
ax.plot(x_plot, y_plot, 'r', linewidth=2, label='f(x) = x²')
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)

# Випадкові точки (частину покажемо)
ax.scatter(x_rand[:1000], y_rand[:1000], color='blue', alpha=0.1, s=1)

ax.set_xlim([x_plot[0], x_plot[-1]])
ax.set_ylim([0, max(y_plot) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Метод Монте-Карло для f(x) = x² на [0,2]')
ax.grid(True)
plt.legend()
plt.show()