'''
작성일 : 2024년 03월 27일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''
import numpy as np
import matplotlib.pyplot as plt


data = np.array([60, 71, 62, 62, 62, 62, 71, 65, 68, 65,66, 66, 67, 67, 68, 68, 68, 69, 60,71])
data2 = np.array([63,71, 63, 63, 65, 65, 68,63,65, 67,69,62,68,62,69,62,65,67,64,63])
plt.hist(data, bins=20)
plt.title("histtype = bar") # bar 형태(기본)

plt.figure()
plt.hist((data,data2), histtype="barstacked")
plt.title("histtype = barstacked")  # 여러 데이터가 쌓인 막대 형태

plt.figure()
plt.hist((data,data2), histtype="step")
plt.title("histtype = step")    # 내부가 비어있는 lineplot 형태

plt.figure()
plt.hist((data,data2), histtype="stepfilled")
plt.title("histtype = stepfilled")  # 내부가 차 있는 lineplot 형태
plt.show()