import numpy as np
import matplotlib.pyplot as plt

a = int(input("정수를 입력하시오. : "))
x = np.linspace(0, 5)

y = a * x

plt.plot(x, y, "r^")    # "r^" "color, marker"
plt.plot(x, y + 3, "b^")    # y출으로 3만큼 이동
plt.xlabel("x", size = 15)
plt.ylabel("y", size = 15)
plt.grid()

plt.show()