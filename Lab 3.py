import math

"""
Вариант 24 => Вариант 4
5x - 6y + 20lgx + 16 = 0
2x + y - 10lgy - 4 = 0
Используя метод простой итерации решить систему
уравнений с точностью до 0.001. Корни отделить графически.
"""


def x_new(X0_2, Y0_2):
    x_1 = (6 * Y0_2 - 20 * math.log10(X0_2) - 16) / 5
    return x_1


def y_new(X0_2, Y0_2):
    y_1 = 10 * math.log10(Y0_2) - 2 * X0_2 + 4
    return y_1


E = 0.001

X0_1 = 0.2
Y0_1 = 0.485
X0_2 = 2.8
Y0_2 = 6.5

"""
Приводим систему к виду пригодному для иттерации:

x = (6y - 20lgx - 16)/5

y = 10lgy - 2x + 4

"""
# Находим производную и проверяем условие сходимости для первых x0, y0
derivative_1_x = (20 + 5 * math.log10(X0_2)) / (6 * math.log10(X0_2))
derivative_1_y = (6 * math.log10(X0_2)) / (5 * math.log10(X0_2) + 20)
derivative_2_x = (2 * math.log10(X0_2)) / (math.log10(Y0_2) - 10)
derivative_2_y = (10 - math.log10(Y0_2)) / 2 * math.log10(Y0_2)

if (derivative_1_x <= 1) and (derivative_1_y <= 1) and (derivative_2_x <= 1) and (derivative_2_y <= 1):
    print("Метод сходится")
else:
    print("Не сходится")

while (abs(x_new(X0_2, Y0_2) - X0_2) >= E) and (abs(y_new(X0_2, Y0_2) - Y0_2) >= E):
    X0_2 = x_new(X0_2, Y0_2)
    Y0_2 = y_new(X0_2, Y0_2)
    print("x = " + str(X0_2))
    print("y = " + str(Y0_2))

print("Проверка подстановкой в F(x) и G(y)")
print(str(X0_2) + " = " + str((6 * Y0_2 - 20 * math.log10(X0_2) - 16) / 5))
print(str(Y0_2) + " = " + str(10 * math.log10(Y0_2) - 2 * X0_2 + 4))

