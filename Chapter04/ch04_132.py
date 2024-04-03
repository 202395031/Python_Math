'''
작성일 : 2024년 03월 20일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''

i = 0
sum = 0

while i < 100:
    i+=1
    sum += i
print("sum =",sum)

sum = 0

for i in range(1, 101):
    sum += i

print("sum =",sum)