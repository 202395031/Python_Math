'''
작성일 : 2024년 03월 27일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300) # -5부터 5까지 300개의 구간으로 나타내라
y1 = x ** 2 
y2 = (x-2) ** 2

plt.plot(x, y1, color="r", label="y1 value")
# plt.plot(x, y2, color = "k", linestyle = "--",label="y2 value")  # 색은 검정색, 선 스타일은 점선으로
# plt.xlabel("X-Axis", size = 14)
plt.ylabel("Y-Axis", size = 14)
plt.title("Graph Title")
plt.legend()
plt.grid()
plt.show()