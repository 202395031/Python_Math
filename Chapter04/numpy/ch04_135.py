'''
작성일 : 2024년 03월 20일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''
import numpy as np

a = np.array([[0,1], [3,4]])

print(a + 3)
print()

print(2 ** a)
print()

print(np.zeros(4))  # 0이 4개로 채워진 배열 생성
print()

print(np.ones((2,3)))   # 2차원 배열(행,열) 을 1로 채워 생성
print()

print(np.arange(10))    # 0부터 10-1까지 범위가 담긴 배열 생성 (정수)
print()

print(np.linspace(0,10,5)) # 0에서 10까지 갯수 5개로 나타냄
print()

a=np.ones((2,3))
print(a)    # * 5를 하면 배열에 값에 5를 곱함(전체 원소에 곱하기)
print(np.shape(a))  # 튜플 형태로 나옴 배열 형태를 나타냄 (행과 열의 값을 나타냄)
print(len(a))   # 배열의 행의 개수를 알 수 있음