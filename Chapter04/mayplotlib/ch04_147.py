'''
작성일 : 2024년 03월 27일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7]) # 날짜 데이터
y = np.array([78.8, 78.4, 78.7, 78.5, 78.4, 79.2, 78.6])    # 체중 데이터

plt.plot(x, y, color = "r", marker="o")   # marker="o" 그래프에 점을 추가해줌
plt.grid()  # 그리디(격자) 형식으로 배경에 나타나게 함
plt.show()  # 그래프를 보여준다.