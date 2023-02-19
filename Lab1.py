def x_new(y_0, z_0):
    x_1 = ((0.53 * y_0) / 2.01) + ((-1.13 * z_0) / 2.01) + (-2.09 / 2.01)
    return x_1


def y_new(x_0, z_0):
    y_1 = ((0.53 * x_0) / 1.62) + ((1.03 * z_0) / 1.62) + (0.39 / 1.62)
    return y_1


def z_new(x_0, y_0):
    z_1 = ((-1.13 * x_0) / 2.34) + ((1.03 * y_0) / 2.34) + (2.13 / 2.34)
    return z_1


def max():
    list = [(0.53 / 2.01 + 1.13 / 2.01), (0.53 / 1.62 + 1.03 / 1.62), (1.13 / 2.34 + 1.03 / 2.34)]
    max_ = list[0]
    for ele in list:
        print(str(ele) + " < 1")
        if ele > max_:
            max_ = ele
    return max_


if max() > 1:
    print("Не сходится")
else:
    print("Метод сходится")

E = 0.0005
x_0 = -2.09 / 2.01
y_0 = 0.39 / 1.62
z_0 = 2.13 / 2.34

while (abs(x_new(y_0, z_0) - x_0) >= E) or (abs(y_new(x_0, z_0) - y_0) >= E) or (abs(z_new(x_0, y_0) - z_0) >= E):

    x_0 = x_new(y_0, z_0)
    y_0 = y_new(x_0, z_0)
    z_0 = z_new(x_0, y_0)

    print("x1 = " + str(x_0))
    print("x2 = " + str(y_0))
    print("x3 = " + str(z_0))

first = 2.01 * x_0 + (-0.53) * y_0 + 1.13 * z_0
second = -0.53 * x_0 + 1.62 * y_0 - 1.03 * z_0
third = 1.13 * x_0 - 1.03 * y_0 + 2.34 * z_0
print("Проверка -2,09 = " + str(first))
print("Проверка 0.39 = " + str(second))
print("Проверка 2,13 = " + str(third))
