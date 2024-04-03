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

plt.plot(x, y, "ro")   # color="r" 빨간색 선으로 그래프를 나타낸다. "ro"는 산포도 형식으로 보여줌
plt.show()  # 그래프를 보여준다.