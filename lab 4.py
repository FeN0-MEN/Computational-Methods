"""
y = Sh(X)
x      1,5     1,6     1,7     1,8
f(x) 2.12928 2.37557 2.64563 2.94217
"""
f_0 = 2.12928
f_1 = 2.37557
f_2 = 2.64563
f_3 = 2.94217

h = 0.1

delta_f_0 = f_1 - f_0
delta_f_1 = f_2 - f_1
delta_f_2 = f_3 - f_2
delta_2_f_0 = delta_f_1 - delta_f_0
delta_2_f_1 = delta_f_2 - delta_f_1
delta_3_f_0 = delta_2_f_1 - delta_2_f_0

t = (1.75 - 1.8) / 0.1

Pn_x = f_3 + t * delta_f_2 + (t * (t + 1) / 2) * delta_2_f_1 + ((t * (t + 1) * (t + 2)) / 6) * delta_3_f_0

# Sh(1.75) = 2.790414366

print("Sh(1.75) = " + str(Pn_x))

