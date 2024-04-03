'''
작성일 : 2024년 03월 27일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''
import numpy as np

def func_ex1(x):    # x에 배열이 들어왔기에
    y= x * 2 + 1
    return y

a = np.array([[0,1,2], [3,4,5]])

print(a[0, :])  # 0행의 : (모든 값)을 출력

b = func_ex1(a) # 배열을 인수로 전달하고 반환값으로 배열을 받는다.
print(b)

print("[2차원 배열]")
print("합계 :", np.sum(a))     # 합계
print("평균 :", np.average(a)) # 평균
print("최댓값 :", np.max(a))   # 최댓값
print("최솟값 :", np.min(a))   # 최솟값

c = np.array([[[0,1,2], [3,4,5]], [[6,7,8], [9,10,11]]])

print("[3차원 배열]")
print("합계 :", np.sum(c))
print("평균 :", np.average(c))
print("최댓값 :", np.max(c))
print("최솟값 :", np.min(c))

print("배열의 크기 :", np.shape(c)) # 배열의 크기를 확인하는 함수   (면, 행, 열)순으로 값이 나옴
print("배열의 차원 :", np.ndim(c))  # 배열이 몇 차원인지 확인하는 함수     

d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(d)
print(d.sum())
print(d.sum(axis=0))    # 배열 열의 합
print(d.sum(axis=1))    # 배열 행의 합