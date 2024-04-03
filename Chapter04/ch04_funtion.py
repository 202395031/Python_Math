'''
작성일 : 2024년 03월 20일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''

def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def divi(num1, num2):
    return num1 / num2

while True:
    num1 = int(input("첫번째 정수를 입력하시오  : "))
    oper = input("연산자를 입력하시오(+,-,*,/) : ")
    num2 = int(input("두번째 정수를 입력하시오  : "))

    
    if oper == "+":
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))

    elif oper == "-":
        print("{} - {} = {}".format(num1, num2, minus(num1, num2)))

    elif oper == "*":
        print("{} * {} = {}".format(num1, num2, multi(num1, num2)))

    elif oper == "/":
        print("{} / {} = {:.2f}".format(num1, num2, float(divi(num1, num2))))

    else:
        print("잘못된 연산자 입니다.")

    end = input("종료(y/n) : ")
    if end == 'n' or end == 'N':
        break
print("프로그램을 종료합니다.")