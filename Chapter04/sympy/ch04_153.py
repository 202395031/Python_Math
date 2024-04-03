'''
작성일 : 2024년 03월 27일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
'''
from sympy import * 

x = symbols('x')
print(sqrt(x**2))

'''
real : 실수
positive : 양수
negative : 음수
integer : 정수
odd : 기수
prime : 소수
complex : 복소수
'''

'''
pi : 원주율 
E : 네이피어 수 e
I : 허수 단위 i
00 : 무한대
'''
y = symbols("y", positive=True)
print(sqrt(y**2))

print(cos(pi))

F = Function('f')   # 수학함수를 나타내는 Fuction 클래스
print(F)
print(type(F))

print(exp(x) + exp (I * pi))

x = Float(1.1, 5)
print(x)

print(Float(0.2, 20))   # 반올림 오류가 포함된 값
print(Float('0.2', '20'))   # 반올림 오류가 포함되지 않은 값

print(Rational('1/3'))  # 분수는 Rational클래스를 나타낸다.


y = symbols('y')

print((x + x * y).subs(x, y))

eq = pi / 2
print(eq)
print(eq.evalf(5))   # 부동 소수점 정밀도를 인수로 지정 가능, 기본적으로 15자리임

z = symbols('z')
print((x + y).subs({x: z**2, y: sqrt(z)}))

x = symbols('x')
print(solveset(x**2 - 2*x + 1))

# 방정식을 나타내는 Eq클래스가 있음 
# Eq클래스의 인수는 방정식의 좌변과 우변을 제공
print(solveset(Eq(x**2, 2*x-1)))
print(solveset(Eq(x**2 - 2*x, -1)))

# 연립 방정식은 linsolve() 함수와 nonlinsolve()함수를 사용한다.
# 방정식이 선형인 경우 linsolve() 함수, 비선형인 경우에는 nonlinsolve() 함수를 사용

# 선형 방정식
eq1 = x + y - 7
eq2 = -3 * x - y + 5
print(linsolve([eq1, eq2], [x, y]))

# 비선형 방정식
eq3 = x * y -1
eq4 = x - 2
print(nonlinsolve([eq3, eq4], [x, y]))

# simplify() 함수는 수식을 간단하게 만들 수 있다.
expr = x**2 + 5*x + 3*(x-1) + (x-1)**2
print(simplify(expr))

print(simplify(cos(x)**2 + sin(x)**2))

# expand() 함수는 수식을 전개 해준다.
print(expand((x-1)*(x-2)))

# factor() 함수는 수식을 인수분해 해준다.
print(factor(x**3-8))

# collect() 함수는 수식을 특정 변수의 다항식으로 정리
expr = x*y + x -3 + 2*x**2 - z*x**2 + x**3
print(expr)
print(collect(expr, x))

# cancel() 함수는 분수의 분자와 분모를 약분하여 간단한 형태로 만든다.
expr = (x**2 + 2*x + 1)/(x**2 + x)
print(cancel(expr))