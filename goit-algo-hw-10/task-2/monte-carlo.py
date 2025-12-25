import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# 1. Визначення функції
def f(x):
    return x ** 2


# Межі інтегрування
a = 0
b = 2

# -------------------------------
# 2. Метод Монте-Карло
# -------------------------------
def monte_carlo_integral(func, a, b, n=1_000_000):
    x_random = np.random.uniform(a, b, n)
    y_values = func(x_random)
    return (b - a) * np.mean(y_values)


mc_result = monte_carlo_integral(f, a, b)

# -------------------------------
# 3. Перевірка через SciPy quad
# -------------------------------
quad_result, quad_error = spi.quad(f, a, b)

# -------------------------------
# 4. Аналітичне значення
# -------------------------------
analytic_result = (b ** 3) / 3

# -------------------------------
# 5. Виведення результатів
# -------------------------------
print("Метод Монте-Карло:", mc_result)
print("Аналітичний результат:", analytic_result)
print("SciPy quad:", quad_result)
print("Похибка quad:", quad_error)

# -------------------------------
# 6. Побудова графіка
# -------------------------------
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.5])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Інтегрування f(x) = x² від 0 до 2 (Метод Монте-Карло)")
ax.grid()

plt.show()
