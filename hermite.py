from scipy import special
import matplotlib.pyplot as plt
import numpy as np

input_ = input("Enter degree: ")
n = int(input_)

p_monic = special.hermite(n, monic=True)
x = np.linspace(-3, 3, 400)
y = p_monic(x)
plt.plot(x, y)
plt.title("Monic Hermite polynomial of degree {}".format(n))
plt.xlabel("x")
plt.ylabel("H_{}(x)".format(n))
plt.show()